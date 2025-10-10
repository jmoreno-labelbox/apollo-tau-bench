# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBuildRunDetails(Tool):
    """Return full details for a build run by its id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        runs = data.get("build_runs", [])
        run = _find_by_id(runs, run_id)
        return json.dumps({"run": run}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_build_run_details",
                "description": "Fetch a single build run by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"}
                    },
                    "required": ["run_id"]
                }
            }
        }
