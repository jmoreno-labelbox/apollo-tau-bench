from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindTemplateFilesByTypeTool(Tool):
    """Looks through the onboarding_files table for accessible templates, filtering by content type and last updated date."""

    @staticmethod
    def invoke(data: dict[str, Any], template_category: str = None, mime_type: str = None) -> str:
        if not template_category:
            return _err("template_category is required")

        files = data.get("onboarding_files", [])

        # Templates are recognized by their path.
        templates = [
            f
            for f in files
            if f"/templates/{template_category}/" in f.get("file_path", "")
        ]

        if mime_type:
            templates = [t for t in templates if t.get("mime_type") == mime_type]
        payload = templates
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findTemplateFilesByType",
                "description": "Searches onboarding_files table for available templates, filtering by content type and last update.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "template_category": {
                            "type": "string",
                            "description": "Template type needed ('welcome', 'asset_request', 'reminder')",
                        },
                        "mime_type": {
                            "type": "string",
                            "description": "File format filter",
                        },
                    },
                    "required": ["template_category"],
                },
            },
        }
