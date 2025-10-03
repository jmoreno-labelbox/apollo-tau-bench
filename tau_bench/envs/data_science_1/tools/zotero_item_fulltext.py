from tau_bench.envs.tool import Tool
import json
from typing import Any

class ZoteroItemFulltext(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        fetched_ts: Any = None,
        file_paths: Any = None,
        item_ids: Any = None
    ) -> str:
        req = ["item_ids", "file_paths"]
        err = _require({"item_ids": item_ids, "file_paths": file_paths}, req)
        if err:
            return err
        row = {
            "item_ids": item_ids,
            "file_paths": file_paths,
            "fetched_ts": fetched_ts,
        }
        payload = _append(data.setdefault("zotero_fulltexts", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ZoteroItemFulltext",
                "description": "Stores file paths for fetched Zotero fulltexts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "file_paths": {"type": "array", "items": {"type": "string"}},
                        "fetched_ts": {"type": "string"},
                    },
                    "required": ["item_ids", "file_paths"],
                },
            },
        }
