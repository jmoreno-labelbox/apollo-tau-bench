# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAd(Tool):
    """Creates a new ad creative."""
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, creative_type, name) -> str:
        ads = list(data.get('ads', {}).values())
        new_id = max((int(a['ad_id']) for a in ads), default=1100) + 1
        new_ad = {"ad_id": str(new_id), "adset_id": adset_id, "name": name, "creative_type": creative_type, "status": "paused", "start_date": "2025-08-15", "end_date": None}
        ads.append(new_ad)
        data['ads'] = ads
        return json.dumps(new_ad)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_ad", "description": "Creates a new ad within a specified ad set.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "name": {"type": "string"}, "creative_type": {"type": "string"}}, "required": ["adset_id", "name", "creative_type"]}}}
