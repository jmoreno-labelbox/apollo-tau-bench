# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_hr_workflow_for_user(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        workflows = data.get("hr_workflows", [])
        # A user may act as either the main employee or a candidate within a workflow.
        workflow = next(
            (
                w
                for w in workflows
                if w.get("employee_id") == user_id
                or user_id in [c.get("employee_id") for c in w.get("candidates", [])]
            ),
            None,
        )
        if workflow:
            return json.dumps({"workflow_id": workflow["workflow_id"]}, indent=2)
        return json.dumps({"error": f"Workflow for user {user_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "find_hr_workflow_for_user",
                "description": "Find an HR workflow associated with a specific user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
