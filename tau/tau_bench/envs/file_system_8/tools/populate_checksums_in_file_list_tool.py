# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PopulateChecksumsInFileListTool(Tool):
    """Computes and populates checksums for all files in the file_list."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "populate_checksums_in_file_list",
                "description": "Iterates through the file_list and populates the 'checksum' field for each entry using SHA256.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if "file_list" not in data:
            return json.dumps({"error": "file_list not found."})
        for file in data["file_list"]:
            file["checksum"] = hashlib.sha256(file["path"].encode()).hexdigest()
        return json.dumps(
            {"status": "success", "populated_count": len(data["file_list"])}
        )
