# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DetectChangedStringsV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], pr_number: int) -> str:
        loc_strings = _get_table(data, "loc_strings")
        prs = _get_table(data, "pull_requests")
        pr = next((p for p in prs if p.get("pr_number") == pr_number), None)
        head_commit = (pr or {}).get("head")
        changed = [row.get("string_key") for row in loc_strings if row.get("last_changed_commit") == head_commit]
        return json.dumps({"changed_keys": changed}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "detect_changed_strings_v2", "description": "Returns string keys whose last_changed_commit equals the PR head commit.", "parameters": {"type": "object", "properties": {"pr_number": {"type": "integer"}}, "required": ["pr_number"]}}}
