from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpsertPricebookEntriesBatch(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], pricebook_name: str, items: list[dict[str, Any]]
    ) -> str:
        pbs = _ensure_table(data, "pricebooks")
        pbes = _ensure_table(data, "pricebook_entries")
        products = _ensure_table(data, "products")

        pb = _find_one(pbs, name=pricebook_name)
        if not pb:
            pb = {
                "pricebook_id": _stable_id("pb", pricebook_name),
                "name": pricebook_name,
            }
            pbs.append(pb)

        pbe_ids = []
        for it in items:
            code = it["product_code"]
            unit_price = float(it["unit_price"])
            prod = _find_one(products, product_code=code)
            if not prod:
                prod = {
                    "product_id": _stable_id("prod", code),
                    "name": code,
                    "product_code": code,
                }
                data["products"][product_id] = prod

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
        pass
        pbs = _ensure_table(data, "pricebooks")
        pbes = _ensure_table(data, "pricebook_entries")
        products = _ensure_table(data, "products")

        pb = _find_one(pbs, name=pricebook_name)
        if not pb:
            pb = {
                "pricebook_id": _stable_id("pb", pricebook_name),
                "name": pricebook_name,
            }
            pbs.append(pb)

        pbe_ids = []
        for it in items:
            code = it["product_code"]
            unit_price = float(it["unit_price"])
            prod = _find_one(products, product_code=code)
            if not prod:
                prod = {
                    "product_id": _stable_id("prod", code),
                    "name": code,
                    "product_code": code,
                }
                data["products"][product_id] = prod

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
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertPricebookEntriesBatch",
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
