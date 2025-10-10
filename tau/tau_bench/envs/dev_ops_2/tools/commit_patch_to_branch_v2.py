# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CommitPatchToBranchV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], branch_ref: str, patch_id: str, run_id: str) -> str:
        commits = _get_table(data, "commits")
        max_id = _max_int_suffix(commits, "commit_id", "CMT", 0)
        commit_id = f"CMT-{max_id + 1}"
        commits.append({"commit_id": commit_id, "ref": commit_id, "message": f"auto tentative fix for run {run_id}", "branch": branch_ref, "patch_id": patch_id})
        return json.dumps({"commit_sha": commit_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "commit_patch_to_branch_v2", "description": "Commits the proposed patch deterministically (next CMT-<n>).", "parameters": {"type": "object", "properties": {"branch_ref": {"type": "string"}, "patch_id": {"type": "string"}, "run_id": {"type": "string"}}, "required": ["branch_ref", "patch_id", "run_id"]}}}
