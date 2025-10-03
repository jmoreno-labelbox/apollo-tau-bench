from tau_bench.envs.tool import Tool
import json
from typing import Any

class ZoteroItemMetadata(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        abstracts_nullable: Any = None,
        authors: Any = None,
        fetched_ts: Any = None,
        item_ids: Any = None,
        saved_path_nullable: Any = None,
        titles: Any = None,
        urls_nullable: Any = None,
        venues_nullable: Any = None,
        years: Any = None
    ) -> str:
        req = ["item_ids", "titles", "fetched_ts"]
        kwargs = {
            "item_ids": item_ids,
            "titles": titles,
            "fetched_ts": fetched_ts
        }
        err = _require(kwargs, req)
        if err:
            return err
        row = {
            "item_ids": item_ids,
            "titles": titles,
            "authors": authors,
            "years": years,
            "venues_nullable": venues_nullable,
            "urls_nullable": urls_nullable,
            "abstracts_nullable": abstracts_nullable,
            "saved_path_nullable": saved_path_nullable,
            "fetched_ts": fetched_ts,
        }
        payload = _append(data.setdefault("zotero_metadata", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ZoteroItemMetadata",
                "description": "Stores bibliographic metadata for Zotero items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "titles": {"type": "array", "items": {"type": "string"}},
                        "authors": {
                            "type": "array",
                            "items": {"type": "array", "items": {"type": "string"}},
                        },
                        "years": {"type": "array", "items": {"type": "integer"}},
                        "venues_nullable": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "urls_nullable": {"type": "array", "items": {"type": "string"}},
                        "abstracts_nullable": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "saved_path_nullable": {"type": "string"},
                        "fetched_ts": {"type": "string"},
                    },
                    "required": ["item_ids", "titles", "fetched_ts"],
                },
            },
        }
