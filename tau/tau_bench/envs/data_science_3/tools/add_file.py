from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddFile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], path: str = None, mime_type: str = None, size: int = None) -> str:
        files = data.get("file_store", [])
        max_id = 0
        for f in files:
            try:
                fid = int(f.get("file_id", 0))
                if fid > max_id:
                    max_id = fid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "file_id": new_id,
            "path": path,
            "mime_type": mime_type,
            "size": size,
            "created_at": _fixed_now_iso(),
        }
        files.append(row)
        payload = {"file_id": new_id, "path": row["path"]}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertFile",
                "description": "Insert a file metadata row into the file store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "mime_type": {"type": "string"},
                        "size": {"type": ["integer", "null"]},
                    },
                    "required": ["path", "mime_type"],
                },
            },
        }
