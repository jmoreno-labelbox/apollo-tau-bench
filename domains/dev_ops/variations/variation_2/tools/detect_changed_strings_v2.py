from tau_bench.envs.tool import Tool
import json
from typing import Any

class DetectChangedStringsV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], pr_number: int) -> str:
        pass
        loc_strings = _get_table(data, "loc_strings")
        prs = _get_table(data, "pull_requests")
        pr = next((p for p in prs if p.get("pr_number") == pr_number), None)
        head_commit = (pr or {}).get("head")
        changed = [
            row.get("string_key")
            for row in loc_strings
            if row.get("last_changed_commit") == head_commit
        ]
        payload = {"changed_keys": changed}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DetectChangedStringsV2",
                "description": "Returns string keys whose last_changed_commit equals the PR head commit.",
                "parameters": {
                    "type": "object",
                    "properties": {"pr_number": {"type": "integer"}},
                    "required": ["pr_number"],
                },
            },
        }
