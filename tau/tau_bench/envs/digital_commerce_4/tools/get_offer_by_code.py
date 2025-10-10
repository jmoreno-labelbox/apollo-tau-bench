# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOfferByCode(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], code: Any) -> str:
        offers = data.get("offers", [])
        match = next((o for o in offers if o.get("offer_code") == code), None)
        return json.dumps(match or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_offer_by_code",
                "description": "Return an offer by code (discount_type=PERCENTAGE|FIXED_AMOUNT).",
                "parameters": {
                    "type": "object",
                    "properties": {"code": {"type": "string"}},
                    "required": ["code"],
                },
            },
        }
