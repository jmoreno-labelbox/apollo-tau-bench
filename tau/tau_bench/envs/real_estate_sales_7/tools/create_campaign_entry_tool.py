from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class CreateCampaignEntryTool(Tool):
    """Inserts a record into the campaigns table along with a corresponding audit event."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_name: str = None, campaign_type: str = None, created_by: int = None,
    type: Any = None,
    ) -> str:
        if not campaign_name or not campaign_type or created_by is None:
            return _err("campaign_name, campaign_type, and created_by are required")

        #--- Generate Campaign Entry ---
        campaign_rows = data.setdefault("campaigns", [])
        campaign_id = _next_int_id(campaign_rows, "campaign_id")
        campaign_rec = {
            "campaign_id": campaign_id,
            "name": str(campaign_name),
            "type": str(campaign_type),
            "created_by": int(created_by),
            "created_at": HARD_TS,
        }
        data["campaigns"][campaign_rec["campaign_id"]] = campaign_rec

        #--- Generate Audit Event Entry ---
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
        data["audit_events"][audit_rec["audit_event_id"]] = audit_rec
        payload = {"campaign": campaign_rec, "audit_event": audit_rec}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCampaignEntry",
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
