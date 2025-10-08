from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetOwnershipForPath(Tool):
    """Retrieve ownership entry for a specified file_path."""

    @staticmethod
    def invoke(data: dict[str, Any], file_path: str = None) -> str:
        path = file_path
        rows = _table(data, "ownership_map")
        row = next((r for r in rows if r.get("file_path") == path), None)
        return _ok({"ownership": row}) if row else _err("ownership not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOwnershipForPath",
                "description": "Fetch ownership record by file_path.",
                "parameters": {
                    "type": "object",
                    "properties": {"file_path": {"type": "string"}},
                    "required": ["file_path"],
                },
            },
        }
