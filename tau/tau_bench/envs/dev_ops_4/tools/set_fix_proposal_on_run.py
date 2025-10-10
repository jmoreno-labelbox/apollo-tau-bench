# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetFixProposalOnRun(Tool):
    """Set fix_proposal_id on a run."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        fix_proposal_id = kwargs.get("fix_proposal_id")
        runs = data.get("build_runs", [])
        idx = _idx_by_id(runs, run_id)
        updated = None
        if idx is not None:
            run = runs[idx]
            run["fix_proposal_id"] = fix_proposal_id
            runs[idx] = run
            updated = run
        return json.dumps({"run": updated}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_fix_proposal_on_run",
                "description": "Attach fix proposal reference to a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "fix_proposal_id": {"type": "string"}
                    },
                    "required": ["run_id", "fix_proposal_id"]
                }
            }
        }
