# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetNeighborhoodDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], neighborhood_id) -> str:
        n = next((n for n in data.get("neighborhoods", []) if n.get("neighborhood_id") == neighborhood_id), None)
        if not n:
            return json.dumps({"error": f"Neighborhood {neighborhood_id} not found"}, indent=2)
        return json.dumps(n, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_neighborhood_details",
            "description":"Return a neighborhood row including bordering_ids_json.",
            "parameters":{"type":"object","properties":{"neighborhood_id":{"type":"integer"}},"required":["neighborhood_id"]}
        }}
