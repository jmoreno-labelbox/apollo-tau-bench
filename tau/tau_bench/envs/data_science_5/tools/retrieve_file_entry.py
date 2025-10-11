# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RetrieveFileEntry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], file_id, path) -> str:
        files = list(data.get("file_store", {}).values()) or []
        fid = file_id
        row = None
        if fid is not None:
            row = next((f for f in files if str(f.get("file_id")) == str(fid)), None)
        elif path:
            row = next((f for f in files if f.get("path") == path), None)
        return json.dumps(row or {"error": "File not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "retrieve_file_entry",
            "description": "Read a file metadata record by id or path.",
            "parameters": {"type": "object", "properties": {
                "file_id": {"type": "string"},
                "path": {"type": "string"}
            }, "required": []}
        }}
