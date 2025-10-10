# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class NewCampaignCreator(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name, ctype, created_by = kwargs.get("name"), kwargs.get("type"), kwargs.get("created_by")
        c = list(data.get("campaigns", {}).values())
        new_id = _next_auto_id(c, "campaign_id")
        row = {"campaign_id": new_id, "name": name, "type": ctype, "created_by": created_by, "created_at": _now_iso_fixed()}
        c.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "new_campaign_creator",
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
