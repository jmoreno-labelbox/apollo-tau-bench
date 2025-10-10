# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindWorkflow(Tool):
    """Find a workflow ID by employee ID and workflow name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("employee_id")
        name = kwargs.get("workflow_name")

        for wf in data.get("hr_workflows", []):
            # Check if the workflow name matches first
            if wf.get("workflow_name", "").lower() == name.lower():
                # Check for a top-level employee_id (e.g., Performance Review)
                if wf.get("employee_id") == uid:
                    return json.dumps({"workflow_id": wf.get("workflow_id")})

                # Check if the user is in the 'candidates' list (e.g., Succession Planning)
                if any(
                    candidate.get("employee_id") == uid
                    for candidate in wf.get("candidates", [])
                ):
                    return json.dumps({"workflow_id": wf.get("workflow_id")})

                # Check if the user is in the 'target_audience' list (e.g., Training Initiative)
                if uid in wf.get("target_audience", []):
                    return json.dumps({"workflow_id": wf.get("workflow_id")})

        return json.dumps({"error": "Workflow not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_workflow",
                "description": "Find a workflow ID by employee and workflow name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "workflow_name": {"type": "string"},
                    },
                    "required": ["employee_id", "workflow_name"],
                },
            },
        }
