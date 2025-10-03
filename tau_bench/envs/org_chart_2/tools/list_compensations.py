from tau_bench.envs.tool import Tool
import json
from typing import Any

class list_compensations(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        all_compensations = data.get("compensation_records", [])
        history = [
            comp for comp in all_compensations if comp.get("employee_id") == employee_id
        ]
        if not history:
            payload = {"count": 0, "results": []}
            out = json.dumps(payload, indent=2)
            return out
        history.sort(key=lambda c: c.get("effective_date", ""), reverse=True)
        payload = {"count": len(history), "results": history}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listCompensations",
                "description": "Return an employee's full compensation history, sorted from most to least recent.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The ID of the employee.",
                        }
                    },
                    "required": ["employee_id"],
                },
            },
        }
