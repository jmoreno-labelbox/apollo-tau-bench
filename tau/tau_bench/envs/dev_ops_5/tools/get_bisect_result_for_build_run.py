from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetBisectResultForBuildRun(Tool):
    """Obtains the bisect result for a designated build run ID."""

    @staticmethod
    def invoke(data: dict[str, Any], build_run_id: str = None) -> str:
        bisect_results = data.get("bisect_results", [])
        for result in bisect_results:
            if result.get("build_run_id") == build_run_id:
                payload = result
                out = json.dumps(payload)
                return out
        payload = {"error": f"Bisect result for build run ID '{build_run_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBisectResultForBuildRun",
                "description": "Retrieves the bisect result for a specific build run ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "build_run_id": {
                            "type": "string",
                            "description": "The unique ID of the build run.",
                        }
                    },
                    "required": ["build_run_id"],
                },
            },
        }
