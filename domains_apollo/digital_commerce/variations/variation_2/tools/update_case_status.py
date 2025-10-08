from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class UpdateCaseStatus(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], case_id: Any, status: Any) -> str:
        if not case_id or not status:
            payload = {"error": "Missing required fields: case_id and/or status"}
            out = json.dumps(payload, indent=2)
            return out
        cases = data.get("cases", [])
        for case in cases:
            if case.get("case_id") == case_id:
                case["status"] = status
                payload = case
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No case found with ID '{case_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCaseStatus",
                "description": "Update the status of an existing case.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_id": {
                            "type": "string",
                            "description": "Exact case ID to update.",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status to set for the case (e.g., New, In Progress, Closed).",
                        },
                    },
                    "required": ["case_id", "status"],
                },
            },
        }
