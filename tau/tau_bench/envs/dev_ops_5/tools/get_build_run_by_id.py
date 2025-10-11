# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBuildRunById(Tool):
    """Retrieves a specific build run by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], id) -> str:
        build_run_id = id
        build_runs = data.get("build_runs", [])
        for run in build_runs:
            if run.get("id") == build_run_id:
                return json.dumps(run)
        return json.dumps({"error": f"Build run with ID '{build_run_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_build_run_by_id",
                "description": "Retrieves a specific build run by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string", "description": "The unique ID of the build run."}},
                    "required": ["id"],
                },
            },
        }
