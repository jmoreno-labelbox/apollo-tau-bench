from tau_bench.envs.tool import Tool
import json
from typing import Any

class ResolveCatalogEntities(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], kind: str, names: list[str]) -> str:
        out = []
        if kind == "product":
            products = _ensure_table(data, "products")
            for n in names:
                row = _find_one(products, name=n) or _find_one(products, product_code=n)
                if not row:
                    # generate in a deterministic manner if absent
                    pid = _stable_id("prod", n)
                    code = n if "-" in n else f"{n.upper().replace(' ','_')}-001"
                    row = {"product_id": pid, "name": n, "product_code": code}
                    data["products"][product_id] = row
                out.append(
                    {
                        "name": row.get("name", n),
                        "id": row.get("product_id"),
                        "product_code": row.get("product_code"),
                    }
                )
        elif kind == "pricebook":
            pbs = _ensure_table(data, "pricebooks")
            for n in names:
                row = _find_one(pbs, name=n)
                if not row:
                    pbid = _stable_id("pb", n)
                    row = {"pricebook_id": pbid, "name": n}
                    pbs.append(row)
                out.append({"name": row["name"], "id": row["pricebook_id"]})
        elif kind == "offer":
            offers = _ensure_table(data, "offers")
            for n in names:
                row = _find_one(offers, offer_code=n) or _find_one(offers, name=n)
                if not row:
                    oid = _stable_id("off", n)
                    row = {
                        "offer_id": oid,
                        "offer_code": n,
                        "description": n,
                        "active": False,
                    }
                    data["offers"][offer_id] = row
                out.append(
                    {
                        "name": row.get("name", row.get("offer_code")),
                        "id": row["offer_id"],
                    }
                )
        elif kind == "pbe":
            pbes = _ensure_table(data, "pricebook_entries")
            for n in names:
                row = _find_one(pbes, pbe_id=n)
                if row:
                    out.append(
                        {
                            "name": n,
                            "id": row["pbe_id"],
                            "product_code": row.get("product_code"),
                        }
                    )
        else:
            raise ValueError(f"Unsupported kind: {kind}")
        return _json({"entities": out})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "resolveCatalogEntities",
                "description": "Resolve names to canonical catalog entity ids and codes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {
                            "type": "string",
                            "enum": ["product", "pricebook", "offer", "pbe"],
                        },
                        "names": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["kind", "names"],
                },
            },
        }
