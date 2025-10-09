from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindPreviousSuccessfulDeployment(Tool):
    """Locates the most recent successful deployment for a specified pipeline prior to a certain time."""

    @staticmethod
    def invoke(data: dict[str, Any], pipeline_id: str = None, before_timestamp: str = None) -> str:
        deployments = sorted(
            [
                d
                for d in data.get("deployments", {}).values()
                if d.get("pipeline_id") == pipeline_id
                and d.get("deployed_at") < before_timestamp
            ],
            key=lambda x: x["deployed_at"],
            reverse=True,
        )

        for d in deployments:
            if d.get("status") == "successful":
                payload = d
                out = json.dumps(payload)
                return out
        payload = {
                "error": f"No successful deployment found for pipeline '{pipeline_id}' before '{before_timestamp}'."
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindPreviousSuccessfulDeployment",
                "description": "Finds the last successful deployment for a pipeline before a specific time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pipeline_id": {"type": "string"},
                        "before_timestamp": {"type": "string"},
                    },
                    "required": ["pipeline_id", "before_timestamp"],
                },
            },
        }
