# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCaseStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], case_id: str, status: Any) -> str:
        if not case_id or not status:
            return _err("case_id and status are required.")
        case_id = _as_id(case_id)
        cases = data.get("cases", [])
        case = next((c for c in cases if _as_id(c.get("case_id")) == case_id), None)
        if not case:
            return _err("Case not found.")
        case["status"] = status
        return json.dumps({"case_id": case_id, "status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_case_status",
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
