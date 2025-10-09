from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetFilesForDirectoryOperation(Tool):
    """Fetches the list of files designated for movement in a file organization task."""

    @staticmethod
    def invoke(data: dict[str, Any], operation_id: str = None) -> str:
        files = [
            f
            for f in data.get("file_lists", [])
            if f.get("operation_id") == operation_id
        ]
        payload = {"files": files, "count": len(files)}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFilesForDirectoryOperation",
                "description": "Retrieves the manifest of files associated with a specific file organization operation.",
                "parameters": {
                    "type": "object",
                    "properties": {"operation_id": {"type": "string"}},
                    "required": ["operation_id"],
                },
            },
        }
