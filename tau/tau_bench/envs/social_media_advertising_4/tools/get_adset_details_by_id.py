# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsetDetailsByID(Tool):
    """Retrieves the details of a single ad set."""
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id) -> str:
        for adset in data.get('adsets', []):
            if adset.get('adset_id') == adset_id:
                return json.dumps(adset)
        return json.dumps({"error": f"Ad set ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adset_details_by_id", "description": "Retrieves the full details for a single ad set using its ID.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}}, "required": ["adset_id"]}}}
