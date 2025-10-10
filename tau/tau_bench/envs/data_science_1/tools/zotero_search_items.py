# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class ZoteroSearchItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], limit, query, result_item_ids, saved_path_nullable, search_ts, year_from, year_to) -> str:
        req = ["query", "result_item_ids", "search_ts"]
        err = _require(kwargs, req)
        if err: return err
        row = {"query": query, "year_from": year_from, "year_to": year_to,
               "limit": limit, "result_item_ids": result_item_ids,
               "saved_path_nullable": saved_path_nullable, "search_ts": search_ts}
        return json.dumps(_append(data.setdefault("zotero_searches", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "zotero_search_items",
            "description": "Stores results of a Zotero query (top-N IDs).",
            "parameters": {"type": "object", "properties": {
                "query": {"type": "string"}, "year_from": {"type": "integer"}, "year_to": {"type": "integer"},
                "limit": {"type": "integer"}, "result_item_ids": {"type": "array", "items": {"type": "string"}},
                "saved_path_nullable": {"type": "string"}, "search_ts": {"type": "string"}},
                "required": ["query", "result_item_ids", "search_ts"]}}}
