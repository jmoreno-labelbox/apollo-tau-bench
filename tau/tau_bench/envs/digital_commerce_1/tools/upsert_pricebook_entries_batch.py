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

class UpsertPricebookEntriesBatch(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], pricebook_name: str, items: List[Dict[str, Any]]) -> str:
        pbs = _ensure_table(data, "pricebooks")
        pbes = _ensure_table(data, "pricebook_entries")
        products = _ensure_table(data, "products")

        pb = _find_one(pbs, name=pricebook_name)
        if not pb:
            pb = {"pricebook_id": _stable_id("pb", pricebook_name), "name": pricebook_name}
            pbs.append(pb)

        pbe_ids = []
        for it in items:
            code = it["product_code"]
            unit_price = float(it["unit_price"])
            prod = _find_one(products, product_code=code)
            if not prod:
                prod = {"product_id": _stable_id("prod", code), "name": code, "product_code": code}
                products.append(prod)

            pbe_id = _stable_id("pbe", pb["pricebook_id"], code)
            row = _find_one(pbes, pbe_id=pbe_id)
            payload = {
                "pbe_id": pbe_id,
                "pricebook_id": pb["pricebook_id"],
                "product_code": code,
                "unit_price": unit_price,
                "updated_at": FIXED_NOW,
            }
            if row:
                row.update(payload)
            else:
                pbes.append(payload)
            pbe_ids.append(pbe_id)

        return _json({"upserted_count": len(pbe_ids), "pbe_ids": pbe_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_pricebook_entries_batch",
                "description": "Upsert multiple price book entries at once.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pricebook_name": {"type": "string"},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_code": {"type": "string"},
                                    "unit_price": {"type": "number"},
                                },
                                "required": ["product_code", "unit_price"],
                            },
                        },
                    },
                    "required": ["pricebook_name", "items"],
                },
            },
        }