from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateBuildRunTriageStatus(Tool):
    """Modifies the triage status of a build run."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: Any = None,
        new_status: str = None,
        run_id: str = None,
        triage_status: str = None
    ) -> str:
        # Support 'triage_status' as an alternative to 'new_status'
        if triage_status is not None:
            new_status = triage_status
        build_runs = data.get("build_runs", [])
        for run in build_runs:
            if run.get("id") == run_id:
                run["triage_status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Triage status for build run '{run_id}' updated to '{new_status}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Build run with ID '{run_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateBuildRunTriageStatus",
                "description": "Updates the triage status of a build run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "triage_status": {"type": "string"},
                    },
                    "required": ["id", "triage_status"],
                },
            },
        }
