# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeterministicAutofixV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], qa_json: Any, tex_report: Any) -> str:
        commits = _get_table(data, "commits")
        next_idx = _max_int_suffix(commits, "patch_id", "AF", 0) + 1
        patch_id = f"AF-{next_idx}"
        return json.dumps({"patch_set": {"mechanical_changes": True, "patch_id": patch_id}}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "deterministic_autofix_v2", "description": "Produces a deterministic patch_set representing mechanical fixes only.", "parameters": {"type": "object", "properties": {"qa_json": {"type": "array", "items": {"type": "string"}}, "tex_report": {"type": "array", "items": {"type": "string"}}}, "required": ["qa_json", "tex_report"]}}}
