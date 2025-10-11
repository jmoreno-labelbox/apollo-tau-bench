# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _idx_by_id(rows: List[Dict[str, Any]], _id: str) -> Optional[int]:
    for i, r in enumerate(rows):
        if r.get("id") == _id:
            return i
    return None

class SetBuildTriageStatus(Tool):
    """Set triage_status on a run, optionally persisting a triage owner into metadata."""
    @staticmethod
    def invoke(data: Dict[str, Any], owner_id, run_id, triage_status) -> str:

        runs = list(data.get("build_runs", {}).values())
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
        return json.dumps({"run": updated}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_build_triage_status",
                "description": "Update triage_status for a run and optionally set metadata.triage_owner_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "triage_status": {"type": "string", "enum": ["in_progress", "manual_review"]},
                        "owner_id": {"type": "string"}
                    },
                    "required": ["run_id", "triage_status"]
                }
            }
        }