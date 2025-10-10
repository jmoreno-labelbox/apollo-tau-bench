# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAdjacentNeighborhoods(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        nid = kwargs.get("neighborhood_id")
        n = next((n for n in data.get("neighborhoods", []) if n.get("neighborhood_id") == nid), None)
        if not n:
            return json.dumps({"error": f"Neighborhood {nid} not found"}, indent=2)
        return json.dumps({"neighborhood_id": nid, "bordering": n.get("bordering_ids_json") or []}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_adjacent_neighborhoods",
                "description": "List bordering neighborhood IDs for a given neighborhood.",
                "parameters": {
                    "type": "object",
                    "properties": {"neighborhood_id": {"type": "integer"}},
                    "required": ["neighborhood_id"],
                },
            },
        }
