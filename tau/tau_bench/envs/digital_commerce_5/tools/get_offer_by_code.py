from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetOfferByCode(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], code: Any) -> str:
        offers = data.get("offers", {}).values()
        match = next((o for o in offers.values() if o.get("offer_code") == code), None)
        payload = match or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOfferByCode",
                "description": "Return an offer by code (discount_type=PERCENTAGE|FIXED_AMOUNT).",
                "parameters": {
                    "type": "object",
                    "properties": {"code": {"type": "string"}},
                    "required": ["code"],
                },
            },
        }
