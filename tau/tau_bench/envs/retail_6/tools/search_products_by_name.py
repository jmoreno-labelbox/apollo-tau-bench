from tau_bench.envs.tool import Tool
import json
from typing import Any

class SearchProductsByName(Tool):
    """Search for a substring in names without case sensitivity (read-only)."""

    @staticmethod
    def invoke(data, query: str = "") -> str:
        q = query.lower()
        out = [p for p in data.get("products", []) if q in p.get("name", "").lower()]
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "searchProductsByName",
                "description": "Search products by name (case-insensitive contains).",
                "parameters": {
                    "type": "object",
                    "properties": {"query": {"type": "string"}},
                },
            },
        }
