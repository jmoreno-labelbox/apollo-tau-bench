# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadRoute(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], route_id) -> str:
        rid = route_id
        r = next((x for x in list(list(list(data.get("routes", {}).values())) if isinstance(data.get("routes"), dict) else data.get("routes", [])) if x.get("route_id") == rid), None)
        if not r:
            return json.dumps({"error": f"route_id {rid} not found"}, indent=2)
        return json.dumps(r, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "read_route",
                "description": "Fetch a route by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"route_id": {"type": "integer"}},
                    "required": ["route_id"],
                },
            },
        }
