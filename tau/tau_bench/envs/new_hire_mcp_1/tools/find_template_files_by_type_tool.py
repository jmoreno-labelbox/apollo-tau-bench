# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _err(msg: str, code: str = "bad_request", **extra) -> str:
    """Creates a JSON error message."""
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class FindTemplateFilesByTypeTool(Tool):
    """Searches onboarding_files table for available templates, filtering by content type and last update."""

    @staticmethod
    def invoke(data: Dict[str, Any], mime_type, template_category) -> str:

        if not template_category:
            return _err("template_category is required")

        files = data.get("onboarding_files", [])

        # Templates are recognized by their file path.
        templates = [
            f for f in files
            if f"/templates/{template_category}/" in f.get("file_path", "")
        ]

        if mime_type:
            templates = [t for t in templates if t.get("mime_type") == mime_type]

        return json.dumps(templates, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_template_files_by_type",
                "description": "Searches onboarding_files table for available templates, filtering by content type and last update.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "template_category": {"type": "string", "description": "Template type needed ('welcome', 'asset_request', 'reminder')"},
                        "mime_type": {"type": "string", "description": "File format filter"}
                    },
                    "required": ["template_category"],
                },
            },
        }