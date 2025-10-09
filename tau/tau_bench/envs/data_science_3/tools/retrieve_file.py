from tau_bench.envs.tool import Tool
import json
from typing import Any

class RetrieveFile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], file_id: str = None, path: str = None) -> str:
        files = data.get("file_store", []) or []
        row = None
        if file_id is not None:
            row = next((f for f in files if str(f.get("file_id")) == str(file_id)), None)
        elif path:
            row = next((f for f in files if f.get("path") == path), None)
        payload = row or {"error": "File not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFile",
                "description": "Read a file store record by id or by path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_id": {"type": "string"},
                        "path": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
