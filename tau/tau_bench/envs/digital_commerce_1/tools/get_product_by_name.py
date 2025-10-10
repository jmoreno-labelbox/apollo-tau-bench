# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductByName(Tool):
    @staticmethod
    def invoke(data, name: str) -> str:
        rows = data.setdefault("products", [])
        row = next((r for r in rows if str(r.get("name")) == name), None)
        if not row:
            raise ValueError(f"product not found: {name}")
        return json.dumps(
            {
                "product_id": row["product_id"],
                "name": row["name"],
                "sku": row.get("sku") or row.get("product_code"),
            }
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_product_by_name",
                "description": "Read an existing product by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
