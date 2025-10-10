# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetWorkflowDetails(Tool):
    """Fetch the full details of a specific HR workflow by its ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        wid = kwargs.get("workflow_id")
        for wf in data.get("hr_workflows", []):
            if wf.get("workflow_id") == wid:
                return json.dumps(wf, indent=2)
        return json.dumps({"error": "Workflow not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_workflow_details",
                "description": "Fetch the full details of a specific HR workflow by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"workflow_id": {"type": "string"}},
                    "required": ["workflow_id"],
                },
            },
        }
