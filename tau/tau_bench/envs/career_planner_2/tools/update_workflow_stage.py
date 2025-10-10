# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateWorkflowStage(Tool):
    """Update HR workflow stage status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        wid = kwargs.get("workflow_id")
        stg = kwargs.get("stage")
        st = kwargs.get("status")
        for wf in data.get("hr_workflows", []):
            if wf.get("workflow_id") == wid:
                for s in wf.get("workflow_stages", []):
                    if s.get("stage") == stg:
                        s["status"] = st
                        s["date"] = datetime.utcnow().date().isoformat()
                        return json.dumps({"success": f"{stg} -> {st}"}, indent=2)
        return json.dumps({"error": "Not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_workflow_stage",
                "description": "Update stage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "workflow_id": {"type": "string"},
                        "stage": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["workflow_id", "stage", "status"],
                },
            },
        }
