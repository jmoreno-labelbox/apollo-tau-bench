# Copyright belongs to Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class ZoteroItemFulltext(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], fetched_ts, file_paths, item_ids) -> str:
        req = ["item_ids", "file_paths"]
        err = _require(kwargs, req)
        if err: return err
        row = {"item_ids": item_ids, "file_paths": file_paths, "fetched_ts": fetched_ts}
        return json.dumps(_append(data.setdefault("zotero_fulltexts", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "zotero_item_fulltext",
            "description": "Stores file paths for fetched Zotero fulltexts.",
            "parameters": {"type": "object", "properties": {
                "item_ids": {"type": "array", "items": {"type": "string"}},
                "file_paths": {"type": "array", "items": {"type": "string"}},
                "fetched_ts": {"type": "string"}}, "required": ["item_ids", "file_paths"]}}}
