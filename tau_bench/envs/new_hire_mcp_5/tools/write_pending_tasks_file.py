from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class WritePendingTasksFile(Tool):
    """Create pending_tasks.md in /onboarding/<candidate>/, with content supplied by the caller."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        candidate_id: str,
        content_markdown: str = "# Pending Tasks\n",
        file_path: str = None,
        created_ts: str = None,
        updated_ts: str = None
,
    due_date_lte: Any = None,
    ) -> str:
        file_path = file_path or f"/onboarding/{candidate_id}/pending_tasks.md"
        return WriteOnboardingFile.invoke(
            data,
            candidate_id=candidate_id,
            file_path=file_path,
            content_text=content_markdown,
            mime_type="text/markdown",
            created_ts=created_ts,
            updated_ts=updated_ts,
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WritePendingTasksFile",
                "description": "Write a markdown summary of pending checklist items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "content_markdown": {"type": "string"},
                        "file_path": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["candidate_id"],
                },
            },
        }
