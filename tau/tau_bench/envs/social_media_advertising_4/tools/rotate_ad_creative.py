# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RotateAdCreative(Tool):
    """Pauses one ad and activates another."""
    @staticmethod
    def invoke(data: Dict[str, Any], ad_id_to_activate, ad_id_to_pause) -> str:
        ad_to_activate, ad_to_pause = ad_id_to_activate, ad_id_to_pause
        activated, paused = False, False
        for ad in list(data.get('ads', {}).values()):
            if ad.get('ad_id') == ad_to_activate:
                ad['status'], activated = 'active', True
            if ad.get('ad_id') == ad_to_pause:
                ad['status'], paused = 'paused', True
        if activated and paused:
            return json.dumps({"status": "success"})
        return json.dumps({"error": "One or both ad IDs not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "rotate_ad_creative", "description": "Activates one ad and pauses another, effectively rotating the active creative.", "parameters": {"type": "object", "properties": {"ad_id_to_activate": {"type": "string"}, "ad_id_to_pause": {"type": "string"}}, "required": ["ad_id_to_activate", "ad_id_to_pause"]}}}
