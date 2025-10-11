# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table
def _slugify(text: str, max_len: int = 40) -> str:
    s = str(text).lower()
    out = []
    prev_dash = False
    for ch in s:
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        else:
            if not prev_dash:
                out.append("-")
                prev_dash = True
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug[:max_len] if max_len > 0 else slug


def _stable_id(prefix: str, *parts: str) -> str:
    base = "-".join(_slugify(p) for p in parts if p is not None and str(p) != "")
    return f"{prefix}-{base}" if base else prefix

def _json(x: Any) -> str:
    return json.dumps(x, separators=(",", ":"))

def _find_one(rows: List[Dict[str, Any]], ):
    crit_items = sorted(crit.items(), key=lambda kv: kv[0])
    for r in rows:
        match = True
        for k, v in crit_items:
            if str(r.get(k)) != str(v):
                match = False
                break
        if match:
            return r
    return None

def _ensure_table(db: Dict[str, Any], name: str):
    if name not in db:
        db[name] = []
    return db[name]

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