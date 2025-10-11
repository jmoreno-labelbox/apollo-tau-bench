# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateReport(Tool):
    """Write a Markdown report file and return a stable report_id + path."""

    @staticmethod
    def _slug(s: str) -> str:
        s = s.lower().strip()
        s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
        return s or "report"

    @staticmethod
    def _auto_title(date: str, tags: List[str]) -> str:
        """
        Generate a clean, predictable title if none is provided.
        Uses the first tag (alphabetically) when available, otherwise a generic label.
        """
        primary = sorted(tags)[0] if tags else "Report"
        return f"{primary} – {date}"

    @staticmethod
    def invoke(data: Dict[str, Any], date, body_markdown = "", tags = [], title = "") -> str:
        date: str = date
        title: str = title
        body_markdown: str = body_markdown
        tags: List[str] = tags

        final_title = title.strip() if isinstance(title, str) else ""
        if not final_title:
            final_title = GenerateReport._auto_title(date, tags)

        slug = GenerateReport._slug(final_title)
        filename = f"report_{date}_{slug}.md"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {final_title}\n\n")
            if tags:
                f.write(f"Tags: {', '.join(tags)}\n\n")
            if body_markdown:
                f.write(f"{body_markdown}\n")

        report_id = f"rep_{date}_{slug}"
        return json.dumps(
            {"success": True, "report_id": report_id, "path": filename, "title": final_title, "tags": tags},
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_report",
                "description": "Write a Markdown report to disk and return its id/path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "title": {"type": "string",
                                  "description": "Optional. If omitted, a readable title is derived."},
                        "body_markdown": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["date"],
                    "additionalProperties": False
                }
            }
        }
