# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table


class UpsertOffer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], offer_code: str, active: bool) -> str:
        offers = _ensure_table(data, "offers")
        row = _find_one(offers, offer_code=offer_code) or _find_one(offers, name=offer_code)
        if not row:
            raise ValueError(f"Offer code not found: {offer_code}")
        row["active"] = (
            bool(active)
            if "active" in row
            else bool(active) if "is_active" not in row else row.update({"is_active": bool(active)})
        )
        row["updated_at"] = FIXED_NOW
        return _json(
            {
                "offer_id": row.get("offer_id") or _stable_id("off", offer_code),
                "active": bool(row.get("active") or row.get("is_active", False)),
            }
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "upsert_offer",
                "description": "Activate/deactivate an existing offer by code (no free-text fields).",
                "parameters": {
                    "type": "object",
                    "properties": {"offer_code": {"type": "string"}, "active": {"type": "boolean"}},
                    "required": ["offer_code", "active"],
                },
            },
        }
