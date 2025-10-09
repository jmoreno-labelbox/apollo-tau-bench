from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FetchClientFullContextTool(Tool):
    """Combines client preferences, mortgage profile, inferred assigned broker, and counts of recent activities."""

    @staticmethod
    def invoke(data: dict[str, Any], client_id: int = None) -> str:
        client_id = _as_int(client_id)
        if client_id is None:
            return _err("client_id is required")

        #--- User Preferences ---
        p = _get_client_prefs(data, client_id) or {}
        prefs_out = {
            "neighborhoods_json": p.get("neighborhoods_json") or [],
            "price_range": [p.get("price_min"), p.get("price_max")],
            "property_type": p.get("property_type"),
            "beds": p.get("beds"),
            "baths": p.get("baths"),
            "sqft_min": p.get("sqft_min"),
            "sqft_max": p.get("sqft_max"),
            "amenities_json": p.get("amenities_json") or [],
            "commute_to_address": p.get("commute_to_address"),
            "commute_max_minutes": p.get("commute_max_minutes"),
        }

        #--- Mortgage profile (accept mortage_profiles misspelling) ---
        msrc = data.get("mortgage_profiles") or data.get("mortage_profiles") or []
        m = (
            next((r for r in msrc.values() if _as_int(r.get("client_id")) == client_id), None)
            or {}
        )
        mort_out = {
            "mortgage_id": m.get("mortgage_id"),
            "credit_score": m.get("credit_score"),
            "annual_income": m.get("annual_income"),
            "down_payment": m.get("down_payment"),
            "desired_loan_amount": m.get("desired_loan_amount"),
            "region": m.get("region"),
            "last_reviewed_at": m.get("last_reviewed_at"),
        }

        #--- Assigned broker inferred (clients table not present) ---
        assigned_broker_id, assignment_basis, last_interaction, broker_active = (
            None,
            None,
            None,
            None,
        )

        #1) Latest comp_report for this client
        crs = [
            r
            for r in data.get("comp_reports", {}).values()
            if _as_int(r.get("client_id")) == client_id
        ]
        if crs:
            crs.sort(
                key=lambda r: (r.get("updated_at") or r.get("created_at") or ""),
                reverse=True,
            )
            latest = crs[0]
            assigned_broker_id = _as_int(latest.get("created_by_broker_id"))
            assignment_basis = "recent_comp_report"
            last_interaction = latest.get("updated_at") or latest.get("created_at")
            broker_active = True

        #2) Backup: latest calendar event
        if assigned_broker_id is None:
            evs = [
                e
                for e in data.get("calendar_events", {}).values()
                if _as_int(e.get("client_id")) == client_id
            ]
            if evs:
                evs.sort(
                    key=lambda e: (e.get("end_at") or e.get("start_at") or ""),
                    reverse=True,
                )
                latest = evs[0]
                assigned_broker_id = _as_int(latest.get("broker_id"))
                assignment_basis = "recent_calendar_event"
                last_interaction = HARD_TS
                broker_active = True

        client_basic = {
            "client_id": client_id,
            "assigned_broker_id": assigned_broker_id,
            "assignment_basis": assignment_basis,
            "last_interaction": last_interaction,
            "broker_active": broker_active,
        }

        #--- Counts of recent activities ---
        emails_cnt = sum(
            1
            for e in data.get("emails", {}).values()
            if _as_int(e.get("client_id")) == client_id
        )
        reports_cnt = sum(
            1
            for r in data.get("comp_reports", {}).values()
            if _as_int(r.get("client_id")) == client_id
        )
        events_cnt = sum(
            1
            for e in data.get("calendar_events", {}).values()
            if _as_int(e.get("client_id")) == client_id
        )

        recent_out = {
            "emails_sent": emails_cnt,
            "reports_generated": reports_cnt,
            "properties_viewed": events_cnt,
        }

        #If absolutely nothing is found for this client, return not_found
        if not p and not m and emails_cnt == 0 and reports_cnt == 0 and events_cnt == 0:
            return _err(f"client_id {client_id} not found", code="not_found")
        payload = {
                "client_basic": client_basic,
                "preferences": prefs_out,
                "mortgage_profile": mort_out,
                "recent_activity": recent_out,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchClientFullContext",
                "description": (
                    "Fetch client preferences, mortgage profile, inferred assigned broker, and activity counts."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }
