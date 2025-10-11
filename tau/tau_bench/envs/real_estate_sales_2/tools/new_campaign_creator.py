# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _now_iso_fixed() -> str:
    return "2025-08-20T00:00:00Z"

def _next_auto_id(rows: List[Dict[str, Any]], key: str) -> int:
    return max((int(r.get(key, 0)) for r in rows), default=0) + 1

class NewCampaignCreator(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], created_by, name, type) -> str:
        name, ctype, created_by = name, type, created_by
        c = list(list(list(data.get("campaigns", {}).values())) if isinstance(data.get("campaigns"), dict) else data.get("campaigns", []))
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