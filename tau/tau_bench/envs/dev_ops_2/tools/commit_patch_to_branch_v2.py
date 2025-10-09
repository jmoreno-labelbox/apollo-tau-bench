from tau_bench.envs.tool import Tool
import json
from typing import Any

class CommitPatchToBranchV2(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], branch_ref: str, patch_id: str, run_id: str
    ) -> str:
        pass
        commits = _get_table(data, "commits")
        max_id = _max_int_suffix(commits, "commit_id", "CMT", 0)
        commit_id = f"CMT-{max_id + 1}"
        commits.append(
            {
                "commit_id": commit_id,
                "ref": commit_id,
                "message": f"auto tentative fix for run {run_id}",
                "branch": branch_ref,
                "patch_id": patch_id,
            }
        )
        payload = {"commit_sha": commit_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CommitPatchToBranchV2",
                "description": "Commits the proposed patch deterministically (next CMT-<n>).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "branch_ref": {"type": "string"},
                        "patch_id": {"type": "string"},
                        "run_id": {"type": "string"},
                    },
                    "required": ["branch_ref", "patch_id", "run_id"],
                },
            },
        }
