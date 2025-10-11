# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table


class SetPricingTierForCustomer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_email: str, pricing_tier_name: str) -> str:
        customers = _ensure_table(data, "customers")
        cust = _find_one(customers, email=customer_email)
        if cust:
            cust["pricing_tier"] = pricing_tier_name
            cust["updated_at"] = FIXED_NOW
            cid = cust["customer_id"]
        else:
            cid = _stable_id("cust", customer_email)
            customers.append(
                {
                    "customer_id": cid,
                    "email": customer_email,
                    "pricing_tier": pricing_tier_name,
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"customer_id": cid, "applied_tier": pricing_tier_name})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_pricing_tier_for_customer",
                "description": "Apply a named pricing tier for a customer by email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_email": {"type": "string"},
                        "pricing_tier_name": {"type": "string"},
                    },
                    "required": ["customer_email", "pricing_tier_name"],
                },
            },
        }
