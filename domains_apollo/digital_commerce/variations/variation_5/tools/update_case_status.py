from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class UpdateCaseStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], case_id: Any, status: Any) -> str:
        if not case_id or not status:
            return _err("case_id and status are required.")
        case_id = _as_id(case_id)
        cases = data.get("cases", [])
        case = next((c for c in cases if _as_id(c.get("case_id")) == case_id), None)
        if not case:
            return _err("Case not found.")
        case["status"] = status
        payload = {"case_id": case_id, "status": status}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCaseStatus",
                "description": "Update the status of a support case.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["case_id", "status"],
                },
            },
        }
