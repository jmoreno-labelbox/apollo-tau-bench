# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WritePendingTasksFile(Tool):
    """Write pending_tasks.md under /onboarding/<candidate>/, content provided by caller."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, created_ts, file_path, updated_ts, content_markdown = "# Pending Tasks\n") -> str:
        cand_id = candidate_id
        content_md = content_markdown
        file_path = file_path or f"/onboarding/{cand_id}/pending_tasks.md"
        return WriteOnboardingFile.invoke(
            data,
            candidate_id=cand_id,
            file_path=file_path,
            content_text=content_md,
            mime_type="text/markdown",
            created_ts=created_ts,
            updated_ts=updated_ts,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "write_pending_tasks_file",
                "description": "Write a markdown summary of pending checklist items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "content_markdown": {"type": "string"},
                        "file_path": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"}
                    },
                    "required": ["candidate_id"]
                }
            }
        }
