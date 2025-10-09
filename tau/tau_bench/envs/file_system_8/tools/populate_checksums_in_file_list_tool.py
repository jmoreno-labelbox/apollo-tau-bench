from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class PopulateChecksumsInFileListTool(Tool):
    """Calculates and fills in checksums for every file in the file_list."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PopulateChecksumsInFileList",
                "description": "Iterates through the file_list and populates the 'checksum' field for each entry using SHA256.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], file_list_directory: Any = None) -> str:
        if "file_list" not in data:
            payload = {"error": "file_list not found."}
            out = json.dumps(payload)
            return out
        for file in data["file_list"].values():
            file["checksum"] = hashlib.sha256(file["path"].encode()).hexdigest()
        payload = {"status": "success", "populated_count": len(data["file_list"])}
        out = json.dumps(payload)
        return out
