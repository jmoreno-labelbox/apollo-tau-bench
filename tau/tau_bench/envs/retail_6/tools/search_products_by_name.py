# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchProductsByName(Tool):
    """Case-insensitive substring name search (read-only)."""
    @staticmethod
    def invoke(data, query = '') -> str:
        q = query.lower()
        out = [p for p in list(data.get('products', {}).values()) if q in p.get('name','').lower()]
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"search_products_by_name","description":"Search products by name (case-insensitive contains).","parameters":{"type":"object","properties":{"query":{"type":"string"}}}}}
