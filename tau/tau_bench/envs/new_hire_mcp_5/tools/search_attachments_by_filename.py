from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class SearchAttachmentsByFilename(Tool):
    """Simulate a gdrive search: return any attachments that match the filename, or an empty list if none exist."""

    @staticmethod
    def invoke(data: dict[str, Any], filename: str) -> str:
        matches = [
            a for a in data.get("attachments", []) if a.get("filename") == filename
        ]
        payload = {"matches": matches}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchAttachmentsByFilename",
                "description": "Search attachments (simulated Drive) by exact filename.",
                "parameters": {
                    "type": "object",
                    "properties": {"filename": {"type": "string"}},
                    "required": ["filename"],
                },
            },
        }
