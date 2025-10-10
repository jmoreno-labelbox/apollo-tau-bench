# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckWorkflowExistsForChangeRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cr_id) -> str:

        if not cr_id:
            return json.dumps({"error": "cr_id is required"})

        approval_workflows = list(data.get("approval_workflows", {}).values())

        existing = next(
            (w for w in approval_workflows if w.get("cr_id") == cr_id), None
        )
        if existing:
            return json.dumps({"success": True, "exists": True})

        return json.dumps({"success": True, "exists": False})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_workflow_exists_for_change_request",
                "description": "Check if a workflow exists for a change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                    },
                    "required": ["cr_id"],
                },
            },
        }
