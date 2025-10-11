# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _next_int_id(rows: List[Dict[str, Any]], key: str) -> int:
    mx = 0
    for r in rows:
        try:
            v = int(r.get(key, 0))
            if v > mx:
                mx = v
        except Exception:
            continue
    return mx + 1

def _err(msg: str, code: str = "bad_request", ) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class CreateCampaignEntryTool(Tool):
    """Creates an entry in the campaigns table and an accompanying audit event."""

    @staticmethod
    def invoke(data: Dict[str, Any], campaign_name, campaign_type, created_by) -> str:

        if not campaign_name or not campaign_type or created_by is None:
            return _err("campaign_name, campaign_type, and created_by are required")

        # --- Initialize Campaign Entry ---
        campaign_rows = data.setdefault("campaigns", [])
        campaign_id = _next_int_id(campaign_rows, "campaign_id")
        campaign_rec = {
            "campaign_id": campaign_id,
            "name": str(campaign_name),
            "type": str(campaign_type),
            "created_by": int(created_by),
            "created_at": HARD_TS,
        }
        campaign_rows.append(campaign_rec)

        # --- Generate Audit Event Record ---
        audit_rows = data.setdefault("audit_events", [])
        audit_event_id = _next_int_id(audit_rows, "event_id")
        audit_rec = {
            "event_id": audit_event_id,
            "actor_id": int(created_by),
            "action": "launched",
            "entity_type": "campaign",
            "entity_id": str(campaign_id),
            "occurred_at": HARD_TS,
            "metadata_json": {
                "campaign_name": campaign_name,
                "campaign_type": campaign_type,
            },
        }
        audit_rows.append(audit_rec)

        return json.dumps(
            {"campaign": campaign_rec, "audit_event": audit_rec}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_campaign_entry",
                "description": (
                    "Creates an entry in the campaigns table and a corresponding audit event."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_name": {"type": "string"},
                        "campaign_type": {
                            "type": "string",
                            "enum": ["general_update", "new_homeowner", "likely_buyer"],
                        },
                        "created_by": {"type": "integer"},
                    },
                    "required": ["campaign_name", "campaign_type", "created_by"],
                },
            },
        }