# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCaseStatus(Tool):
    """Update the status of an existing case."""

    @staticmethod
    def invoke(data: Dict[str, Any], case_id: Any, status: Any) -> str:
        case_id = case_id
        if not case_id or not status:
            return json.dumps({"error": "Missing required fields: case_id and/or status"}, indent=2)
        cases = list(data.get("cases", {}).values())
        for case in cases:
            if case.get("case_id") == case_id:
                case["status"] = status
                return json.dumps(case, indent=2)

        return json.dumps({"error": f"No case found with ID '{case_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_case_status",
                "description": "Update the status of an existing case.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_id": {"type": "string", "description": "Exact case ID to update."},
                        "status": {
                            "type": "string",
                            "description": "New status to set for the case (e.g., New, In Progress, Closed).",
                        },
                    },
                    "required": ["case_id", "status"],
                },
            },
        }
