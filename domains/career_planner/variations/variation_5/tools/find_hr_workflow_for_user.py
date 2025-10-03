from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindHrWorkflowForUser(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: Any = None
    ) -> str:
        hr_workflows = data.get("hr_workflows", [])
        # A user may serve as the main employee or a candidate within a workflow
        workflow = next(
            (
                w
                for w in hr_workflows
                if w.get("employee_id") == user_id
                or user_id in [c.get("employee_id") for c in w.get("candidates", [])]
            ),
            None,
        )
        if workflow:
            payload = {"workflow_id": workflow["workflow_id"]}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Workflow for user {user_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "findHrWorkflowForUser",
                "description": "Find an HR workflow associated with a specific user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
