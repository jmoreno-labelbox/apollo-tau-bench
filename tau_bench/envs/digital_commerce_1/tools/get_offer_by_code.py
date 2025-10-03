from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetOfferByCode(Tool):
    @staticmethod
    def invoke(data, offer_code: str, offer_id: str = None, id: str = None, discount_type: str = None, discount_value: float = None, is_active: bool = None, active: bool = False) -> str:
        rows = data.setdefault("offers", [])
        row = next((r for r in rows if str(r.get("offer_code")) == offer_code), None)
        if not row:
            raise ValueError(f"offer not found: {offer_code}")
        payload = {
            "offer_id": row.get("offer_id") or row.get("id"),
            "offer_code": row["offer_code"],
            "discount_type": row.get("discount_type"),
            "discount_value": row.get("discount_value"),
            "is_active": bool(row.get("is_active", row.get("active", False))),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetOfferByCode",
                "description": "Read an existing promotion/offer by code.",
                "parameters": {
                    "type": "object",
                    "properties": {"offer_code": {"type": "string"}},
                    "required": ["offer_code"],
                },
            },
        }
