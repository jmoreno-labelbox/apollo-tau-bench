# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class OpenAutoBranchV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], base_ref: str, run_id: str) -> str:
        branches = _get_table(data, "branches")
        name = f"auto/fix-{run_id}"
        existing = next((b for b in branches if b.get("name") == name), None)
        if existing:
            return json.dumps({"branch_ref": name}, indent=2)
        branches.append({"name": name, "base": base_ref})
        return json.dumps({"branch_ref": name}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "open_auto_branch_v2", "description": "Creates deterministic automation branch 'auto/fix-<run_id>'.", "parameters": {"type": "object", "properties": {"base_ref": {"type": "string"}, "run_id": {"type": "string"}}, "required": ["base_ref", "run_id"]}}}
