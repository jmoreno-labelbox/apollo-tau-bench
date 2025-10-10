# Copyright Sierra Inc.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchClientFullContextTool(Tool):
    """Aggregates client preferences, mortgage profile, inferred assigned broker, and recent-activity counts."""

    @staticmethod
    def invoke(data: Dict[str, Any], client_id) -> str:
        client_id = _as_int(client_id)
        if client_id is None:
            return _err("client_id is required")

        # --- User Settings ---
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

        # --- Mortgage configuration (allow mortgage_profiles misspelling) ---
        msrc = data.get("mortgage_profiles") or data.get("mortage_profiles") or []
        m = (
            next((r for r in msrc if _as_int(r.get("client_id")) == client_id), None)
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

        # --- Deducted assigned broker (clients table not present) ---
        assigned_broker_id, assignment_basis, last_interaction, broker_active = (
            None,
            None,
            None,
            None,
        )

        # Latest comp_report for this client
        crs = [
            r
            for r in data.get("comp_reports", [])
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

        # 2) Backup: latest calendar appointment
        if assigned_broker_id is None:
            evs = [
                e
                for e in data.get("calendar_events", [])
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

        # --- Count of recent activities ---
        emails_cnt = sum(
            1
            for e in data.get("emails", [])
            if _as_int(e.get("client_id")) == client_id
        )
        reports_cnt = sum(
            1
            for r in data.get("comp_reports", [])
            if _as_int(r.get("client_id")) == client_id
        )
        events_cnt = sum(
            1
            for e in data.get("calendar_events", [])
            if _as_int(e.get("client_id")) == client_id
        )

        recent_out = {
            "emails_sent": emails_cnt,
            "reports_generated": reports_cnt,
            "properties_viewed": events_cnt,
        }

        # If there are no records for this client, return not_found.
        if not p and not m and emails_cnt == 0 and reports_cnt == 0 and events_cnt == 0:
            return _err(f"client_id {client_id} not found", code="not_found")

        return json.dumps(
            {
                "client_basic": client_basic,
                "preferences": prefs_out,
                "mortgage_profile": mort_out,
                "recent_activity": recent_out,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_client_full_context",
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
