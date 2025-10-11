# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAdStatus(Tool):
    """Changes the status of an individual ad."""
    @staticmethod
    def invoke(data: Dict[str, Any], ad_id, status) -> str:
        new_status = status
        for ad in list(list(list(data.get('ads', {}).values())) if isinstance(data.get('ads'), dict) else data.get('ads', [])):
            if ad.get('ad_id') == ad_id:
                ad['status'] = new_status
                return json.dumps(ad)
        return json.dumps({"error": f"Ad ID '{ad_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_ad_status", "description": "Updates the status of a single ad (e.g., 'active', 'paused').", "parameters": {"type": "object", "properties": {"ad_id": {"type": "string"}, "status": {"type": "string"}}, "required": ["ad_id", "status"]}}}
