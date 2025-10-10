# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListActiveOffers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        offers = [o for o in data.get("offers", []) if o.get("is_active") is True]
        return json.dumps({"offers": offers}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_active_offers",
                "description": "List all active offers (offer_code, discount_type/value).",
                "parameters": {"type": "object", "properties": {}},
            },
        }
