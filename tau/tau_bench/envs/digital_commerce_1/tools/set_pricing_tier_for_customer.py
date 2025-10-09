from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetPricingTierForCustomer(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], customer_email: str, pricing_tier_name: str
    ) -> str:
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
        pass
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
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetPricingTierForCustomer",
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
