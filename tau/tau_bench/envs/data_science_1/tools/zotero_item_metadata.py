# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class ZoteroItemMetadata(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], abstracts_nullable, authors, fetched_ts, item_ids, saved_path_nullable, titles, urls_nullable, venues_nullable, years) -> str:
        req = ["item_ids", "titles", "fetched_ts"]
        err = _require(kwargs, req)
        if err: return err
        row = {"item_ids": item_ids, "titles": titles, "authors": authors,
               "years": years, "venues_nullable": venues_nullable,
               "urls_nullable": urls_nullable, "abstracts_nullable": abstracts_nullable,
               "saved_path_nullable": saved_path_nullable, "fetched_ts": fetched_ts}
        return json.dumps(_append(data.setdefault("zotero_metadata", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "zotero_item_metadata",
            "description": "Stores bibliographic metadata for Zotero items.",
            "parameters": {"type": "object", "properties": {
                "item_ids": {"type": "array", "items": {"type": "string"}},
                "titles": {"type": "array", "items": {"type": "string"}},
                "authors": {"type": "array", "items": {"type": "array", "items": {"type": "string"}}},
                "years": {"type": "array", "items": {"type": "integer"}},
                "venues_nullable": {"type": "array", "items": {"type": "string"}},
                "urls_nullable": {"type": "array", "items": {"type": "string"}},
                "abstracts_nullable": {"type": "array", "items": {"type": "string"}},
                "saved_path_nullable": {"type": "string"},
                "fetched_ts": {"type": "string"}}, "required": ["item_ids", "titles", "fetched_ts"]}}}
