from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SetBuildTriageStatus(Tool):
    """Assign triage_status to a run, with the option to save a triage owner in the metadata."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None, triage_status: str = None, owner_id: str = None) -> str:
        runs = data.get("build_runs", [])
        idx = _idx_by_id(runs, run_id)
        updated = None
        if idx is not None:
            run = runs[idx]
            run["triage_status"] = triage_status
            if owner_id:
                run.setdefault("metadata", {})
                run["metadata"]["triage_owner_id"] = owner_id
            runs[idx] = run
            updated = run
        payload = {"run": updated}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetBuildTriageStatus",
                "description": "Update triage_status for a run and optionally set metadata.triage_owner_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "triage_status": {
                            "type": "string",
                            "enum": ["in_progress", "manual_review"],
                        },
                        "owner_id": {"type": "string"},
                    },
                    "required": ["run_id", "triage_status"],
                },
            },
        }
