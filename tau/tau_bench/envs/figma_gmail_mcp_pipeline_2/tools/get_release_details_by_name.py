# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReleaseDetailsByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("release_name"):
            return json.dumps({"error": "Missing required field: release_name"}, indent=2)

        release_name = kwargs.get("release_name")
        releases: List[Dict[str, Any]] = data.get("releases", [])

        results: List[Dict[str, Any]] = [r for r in releases if r.get("release_name") == release_name]
        results.sort(key=lambda r: (str(r.get("created_ts")), str(r.get("release_id"))))

        if not results:
            return json.dumps({"error": f"No release found with release_name '{release_name}'"}, indent=2)

        return json.dumps({"count": len(results), "releases": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_release_details_by_name",
                "description": "Return releases matching an exact release_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_name": {"type": "string"}
                    },
                    "required": ["release_name"]
                }
            }
        }
