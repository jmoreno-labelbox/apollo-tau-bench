# Copyright Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_hr_workflow(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], workflow_id: str) -> str:
        workflow = next(
            (
                w
                for w in data.get("hr_workflows", [])
                if w.get("workflow_id") == workflow_id
            ),
            None,
        )
        return (
            json.dumps(workflow, indent=2)
            if workflow
            else json.dumps({"error": "Workflow not found"}, indent=2)
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_hr_workflow",
                "description": "Get HR workflow details by workflow ID",
                "parameters": {
                    "type": "object",
                    "properties": {"workflow_id": {"type": "string"}},
                    "required": ["workflow_id"],
                },
            },
        }
