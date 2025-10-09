from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RegisterFileEntry(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], path: str = None, mime_type: str = None, size: int = None) -> str:
        files = data.get("file_store", {}).values()
        max_id = 0
        for f in files.values():
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
            "created_at": _now_iso_fixed(),
        }
        data["files"][file_id] = row
        payload = {"file_id": new_id, "path": row["path"]}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterFileEntry",
                "description": "Create a file metadata record.",
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
