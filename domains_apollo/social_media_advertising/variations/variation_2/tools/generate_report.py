from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class GenerateReport(Tool):
    """Generate a Markdown report file and return a consistent report_id along with its path."""

    @staticmethod
    def _slug(s: str) -> str:
        _sL = s or ''.lower()
        pass
        s = (s or "").lower().strip()
        s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
        return s or "report"

    @staticmethod
    def _auto_title(date: str, tags: list[str]) -> str:
        """
        Create a clear, consistent title if one is not supplied.
        Utilizes the first tag (in alphabetical order) when available, or defaults to a generic label.
        """
        pass
        primary = sorted(tags)[0] if tags else "Report"
        return f"{primary} – {date or 'unknown'}"

    @staticmethod
    def invoke(data: dict[str, Any], date: str, title: str = "", body_markdown: str = "", tags: list[str] = []) -> str:
        final_title = title.strip() if isinstance(title, str) else ""
        if not final_title:
            final_title = GenerateReport._auto_title(date, tags)
        
        # Ensure final_title is not None
        final_title = final_title or "Report"
        slug = GenerateReport._slug(final_title)
        filename = f"report_{date}_{slug}.md"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {final_title}\n\n")
            if tags:
                f.write(f"Tags: {', '.join(tags)}\n\n")
            if body_markdown:
                f.write(f"{body_markdown}\n")

        report_id = f"rep_{date}_{slug}"
        payload = {
                "success": True,
                "report_id": report_id,
                "path": filename,
                "title": final_title,
                "tags": tags,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateReport",
                "description": "Write a Markdown report to disk and return its id/path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "title": {
                            "type": "string",
                            "description": "Optional. If omitted, a readable title is derived.",
                        },
                        "body_markdown": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["date"],
                    "additionalProperties": False,
                },
            },
        }
