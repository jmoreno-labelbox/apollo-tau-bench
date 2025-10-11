# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table










def _stable_id(prefix: str, *parts: str) -> str:
    base = "-".join(_slugify(p) for p in parts if p is not None and str(p) != "")
    return f"{prefix}-{base}" if base else prefix

def _json(x: Any) -> str:
    return json.dumps(x, separators=(",", ":"))

def _find_one(rows: List[Dict[str, Any]], **crit):
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

class UpsertPromotion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], code: str, active: bool) -> str:
        offers = _ensure_table(data, "offers")
        row = _find_one(offers, offer_code=code) or _find_one(offers, name=code)
        if not row:
            raise ValueError(f"Promotion code not found: {code}")
        if "is_active" in row:
            row["is_active"] = bool(active)
        else:
            row["active"] = bool(active)
        row["updated_at"] = FIXED_NOW
        return _json(
            {
                "promo_id": row.get("offer_id") or _stable_id("promo", code),
                "active": bool(row.get("active") or row.get("is_active", False)),
            }
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "upsert_promotion",
                "description": "Activate/deactivate an existing promotion by code.",
                "parameters": {
                    "type": "object",
                    "properties": {"code": {"type": "string"}, "active": {"type": "boolean"}},
                    "required": ["code", "active"],
                },
            },
        }