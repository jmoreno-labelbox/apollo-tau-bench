from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetBuildRunById(Tool):
    """Fetches a particular build run using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        build_run_id = id
        build_runs = data.get("build_runs", [])
        for run in build_runs:
            if run.get("id") == build_run_id:
                payload = run
                out = json.dumps(payload)
                return out
        payload = {"error": f"Build run with ID '{build_run_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBuildRunById",
                "description": "Retrieves a specific build run by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "The unique ID of the build run.",
                        }
                    },
                    "required": ["id"],
                },
            },
        }
