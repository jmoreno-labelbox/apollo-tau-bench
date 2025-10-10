# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRouteDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rid = kwargs.get("route_id")
        r = next((x for x in list(data.get("routes", {}).values()) if x.get("route_id") == rid), None)
        if not r:
            return json.dumps({"error": f"route_id {rid} not found"}, indent=2)
        return json.dumps(r, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_route_details",
            "description":"Fetch a route by ID.",
            "parameters":{"type":"object","properties":{"route_id":{"type":"integer"}},"required":["route_id"]}
        }}
