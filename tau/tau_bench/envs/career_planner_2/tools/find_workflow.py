from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindWorkflow(Tool):
    """Locate a workflow ID using the employee ID and workflow name."""

    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, workflow_name: str = None) -> str:
        uid = employee_id
        name = workflow_name

        for wf in data.get("hr_workflows", []):
            # Verify if the workflow name matches initially
            if wf.get("workflow_name", "").lower() == name.lower():
                # Verify the presence of a top-level employee_id (e.g., Performance Review)
                if wf.get("employee_id") == uid:
                    payload = {"workflow_id": wf.get("workflow_id")}
                    out = json.dumps(payload)
                    return out

                # Confirm if the user is included in the 'candidates' list (e.g., Succession Planning)
                if any(
                    candidate.get("employee_id") == uid
                    for candidate in wf.get("candidates", [])
                ):
                    payload = {"workflow_id": wf.get("workflow_id")}
                    out = json.dumps(payload)
                    return out

                # Verify if the user appears in the 'target_audience' list (e.g., Training Initiative)
                if uid in wf.get("target_audience", []):
                    payload = {"workflow_id": wf.get("workflow_id")}
                    out = json.dumps(payload)
                    return out
        payload = {"error": "Workflow not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindWorkflow",
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
