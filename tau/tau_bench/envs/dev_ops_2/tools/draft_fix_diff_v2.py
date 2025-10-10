# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DraftFixDiffV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str) -> str:
        fixes = _get_table(data, "fix_proposals")
        existing = next((f for f in fixes if f.get("run_id") == run_id), None)
        if existing:
            return json.dumps(existing, indent=2)
        patch_id = f"FP-{run_id}"
        proposal = {
            "patch_id": patch_id,
            "run_id": run_id,
            "status": "proposed",
            "summary": f"auto tentative fix for run {run_id}",
        }
        fixes.append(proposal)
        return json.dumps(proposal, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "draft_fix_diff_v2", "description": "Creates a deterministic fix proposal entry using policy templates.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}}, "required": ["run_id"]}}}
