from tau_bench.envs.tool import Tool
import json
from typing import Any

class list_bonus_payments(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        bonuses = data.get("bonus_payments", [])
        hits = [b for b in bonuses if b.get("employee_id") == employee_id]
        payload = {"count": len(hits), "results": hits}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listBonusPayments",
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
