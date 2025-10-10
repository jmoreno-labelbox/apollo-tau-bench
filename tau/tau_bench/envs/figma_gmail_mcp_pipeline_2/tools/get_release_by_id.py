# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReleaseById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("release_id"):
            return json.dumps({"error": "Missing required field: release_id"}, indent=2)

        release_id = kwargs.get("release_id")
        releases: List[Dict[str, Any]] = list(data.get("releases", {}).values())
        for row in releases:
            if row.get("release_id") == release_id:
                return json.dumps(row, indent=2)

        return json.dumps({"error": f"No release with id '{release_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_release_by_id",
                "description": "Fetch a single release by release_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string"}
                    },
                    "required": ["release_id"]
                }
            }
        }
