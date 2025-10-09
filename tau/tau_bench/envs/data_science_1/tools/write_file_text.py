from tau_bench.envs.tool import Tool
import json
from typing import Any

class WriteFileText(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        content: str = None,
        created_ts: str = None,
        mime_type: str = None,
        path: str = None,
        updated_ts: str = None
    ) -> str:
        err = _require({"path": path, "content": content}, ["path", "content"])
        if err:
            return err
        tbl = data.setdefault("file_store", [])
        row = {
            "path": path,
            "file_contents_text": content,
            "file_mime_types": mime_type,
            "char_counts": len(content),
            "created_ts": created_ts,
            "updated_ts": updated_ts,
        }
        existing = next((r for r in tbl if r.get("path") == row["path"]), None)
        if existing:
            existing.update(row)
            payload = existing
            out = json.dumps(payload, indent=2)
            return out
        payload = _append(tbl, row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteFileText",
                "description": "Stores or updates a text file into file_store deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "content": {"type": "string"},
                        "mime_type": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["path", "content"],
                },
            },
        }
