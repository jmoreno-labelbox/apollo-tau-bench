# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateBuildRunTriageStatus(Tool):
    """Updates the triage status of a build run."""
    @staticmethod
    def invoke(data: Dict[str, Any], id, triage_status) -> str:
        run_id = id
        new_status = triage_status
        build_runs = data.get("build_runs", [])
        for run in build_runs:
            if run.get("id") == run_id:
                run["triage_status"] = new_status
                return json.dumps({"status": "success", "message": f"Triage status for build run '{run_id}' updated to '{new_status}'."})
        return json.dumps({"error": f"Build run with ID '{run_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_build_run_triage_status",
                "description": "Updates the triage status of a build run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "triage_status": {"type": "string"}
                    },
                    "required": ["id", "triage_status"]
                }
            }
        }
