# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBisectResultForBuildRun(Tool):
    """Retrieves the bisect result for a specific build run ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], build_run_id) -> str:
        bisect_results = data.get("bisect_results", [])
        for result in bisect_results:
            if result.get("build_run_id") == build_run_id:
                return json.dumps(result)
        return json.dumps({"error": f"Bisect result for build run ID '{build_run_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_bisect_result_for_build_run",
                "description": "Retrieves the bisect result for a specific build run ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"build_run_id": {"type": "string", "description": "The unique ID of the build run."}},
                    "required": ["build_run_id"],
                },
            },
        }
