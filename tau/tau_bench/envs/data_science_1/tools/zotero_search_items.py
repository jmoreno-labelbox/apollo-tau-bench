from tau_bench.envs.tool import Tool
import json
from typing import Any

class ZoteroSearchItems(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        limit: int = None,
        query: str = None,
        result_item_ids: list = None,
        saved_path_nullable: str = None,
        search_ts: str = None,
        year_from: int = None,
        year_to: int = None
    ) -> str:
        req = ["query", "result_item_ids", "search_ts"]
        err = _require(locals(), req)
        if err:
            return err
        row = {
            "query": query,
            "year_from": year_from,
            "year_to": year_to,
            "limit": limit,
            "result_item_ids": result_item_ids,
            "saved_path_nullable": saved_path_nullable,
            "search_ts": search_ts,
        }
        payload = _append(data.setdefault("zotero_searches", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ZoteroSearchItems",
                "description": "Stores results of a Zotero query (top-N IDs).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "year_from": {"type": "integer"},
                        "year_to": {"type": "integer"},
                        "limit": {"type": "integer"},
                        "result_item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "saved_path_nullable": {"type": "string"},
                        "search_ts": {"type": "string"},
                    },
                    "required": ["query", "result_item_ids", "search_ts"],
                },
            },
        }
