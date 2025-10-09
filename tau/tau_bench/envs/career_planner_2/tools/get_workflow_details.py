from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetWorkflowDetails(Tool):
    """Retrieve comprehensive details of a specific HR workflow using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], workflow_id: str = None) -> str:
        wid = workflow_id
        for wf in data.get("hr_workflows", {}).values():
            if wf.get("workflow_id") == wid:
                payload = wf
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Workflow not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWorkflowDetails",
                "description": "Fetch the full details of a specific HR workflow by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"workflow_id": {"type": "string"}},
                    "required": ["workflow_id"],
                },
            },
        }
