from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetRollbackByDeploymentId(Tool):
    """Obtains rollback information for a failed deployment ID."""

    @staticmethod
    def invoke(data: dict[str, Any], deployment_id: str = None) -> str:
        rollbacks = data.get("rollbacks", [])
        for r in rollbacks:
            if r.get("deployment_id") == deployment_id:
                payload = r
                out = json.dumps(payload)
                return out
        payload = {"error": f"Rollback for deployment ID '{deployment_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRollbackByDeploymentId",
                "description": "Retrieves rollback details for a failed deployment ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"deployment_id": {"type": "string"}},
                    "required": ["deployment_id"],
                },
            },
        }
