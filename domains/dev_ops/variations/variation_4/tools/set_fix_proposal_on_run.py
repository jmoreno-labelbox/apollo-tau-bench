from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetFixProposalOnRun(Tool):
    """Assign fix_proposal_id to a run."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None, fix_proposal_id: str = None) -> str:
        runs = data.get("build_runs", [])
        idx = _idx_by_id(runs, run_id)
        updated = None
        if idx is not None:
            run = runs[idx]
            run["fix_proposal_id"] = fix_proposal_id
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
                "name": "SetFixProposalOnRun",
                "description": "Attach fix proposal reference to a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "fix_proposal_id": {"type": "string"},
                    },
                    "required": ["run_id", "fix_proposal_id"],
                },
            },
        }
