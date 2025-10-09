from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetProductByName(Tool):
    @staticmethod
    def invoke(data, name: str) -> str:
        rows = data.setdefault("products", [])
        row = next((r for r in rows if str(r.get("name")) == name), None)
        if not row:
            raise ValueError(f"product not found: {name}")
        payload = {
            "product_id": row["product_id"],
            "name": row["name"],
            "sku": row.get("sku") or row.get("product_code"),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetProductByName",
                "description": "Read an existing product by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
