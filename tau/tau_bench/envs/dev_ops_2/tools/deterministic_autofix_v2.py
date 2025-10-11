# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _max_int_suffix(items: List[Dict[str, Any]], key: str, prefix: str, default: int = 0) -> int:
    max_val = default
    for it in items:
        raw = it.get(key)
        if isinstance(raw, str) and raw.startswith(prefix + "-"):
            try:
                num = int(raw.split("-")[-1])
                if num > max_val:
                    max_val = num
            except ValueError:
                continue
    return max_val

def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

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