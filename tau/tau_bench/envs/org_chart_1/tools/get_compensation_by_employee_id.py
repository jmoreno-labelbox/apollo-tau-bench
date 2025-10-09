from tau_bench.envs.tool import Tool
import json
from typing import Any

class get_compensation_by_employee_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        comp = data.get("compensation_records", [])
        latest = [c for c in comp if c["employee_id"] == employee_id]
        latest.sort(key=lambda c: c["effective_date"], reverse=True)
        payload = latest[0] if latest else {"error": "not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCompensationByEmployeeId",
                "description": "Return the most recent compensation record for employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }
