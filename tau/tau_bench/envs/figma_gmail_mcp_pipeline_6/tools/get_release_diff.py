# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_release_diff(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], release_id: str) -> str:
        diffs = data.get("release_diffs", [])
        for diff in diffs:
            if diff.get("release_id") == release_id:
                return json.dumps(diff, indent=2)
        return json.dumps({"error": f"Release diff for {release_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "get_release_diff",
            "description": "Retrieve the diff summary for a given release_id.",
            "parameters": {"type": "object","properties": {"release_id": {"type": "string"}},"required": ["release_id"]}
        }}
