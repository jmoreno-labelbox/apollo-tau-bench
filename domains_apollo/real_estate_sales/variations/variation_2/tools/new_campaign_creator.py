from tau_bench.envs.tool import Tool
import json
from itertools import islice
from typing import Any

class NewCampaignCreator(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, ctype: str = None, created_by: str = None,
    type: Any = None,
    ) -> str:
        c = data.get("campaigns", [])
        new_id = _next_auto_id(c, "campaign_id")
        row = {
            "campaign_id": new_id,
            "name": name,
            "type": ctype,
            "created_by": created_by,
            "created_at": _now_iso_fixed(),
        }
        c.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NewCampaignCreator",
                "description": "Create a new campaign row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string"},
                        "created_by": {"type": "integer"},
                    },
                    "required": ["name", "type", "created_by"],
                },
            },
        }
