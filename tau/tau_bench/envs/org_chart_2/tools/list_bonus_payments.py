# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_bonus_payments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        bonuses = data.get("bonus_payments", [])
        hits = [b for b in bonuses if b.get("employee_id") == employee_id]
        return json.dumps({"count": len(hits), "results": hits}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_bonus_payments",
                "description": "Return all bonus payments for a given employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Unique ID of the employee whose bonus payments are requested",
                        }
                    },
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }
