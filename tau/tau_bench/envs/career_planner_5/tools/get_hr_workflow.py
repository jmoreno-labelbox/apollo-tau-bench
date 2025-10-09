from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetHrWorkflow(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], workflow_id: str) -> str:
        workflow = next(
            (
                w
                for w in data.get("hr_workflows", {}).values()
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
        pass
        return {
            "type": "function",
            "function": {
                "name": "getHrWorkflow",
                "description": "Get HR workflow details by workflow ID",
                "parameters": {
                    "type": "object",
                    "properties": {"workflow_id": {"type": "string"}},
                    "required": ["workflow_id"],
                },
            },
        }
