# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WritePendingTasksFile(Tool):
    """Write pending_tasks.md under /onboarding/<candidate>/, content provided by caller."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        content_md = kwargs.get("content_markdown", "# Pending Tasks\n")
        file_path = kwargs.get("file_path") or f"/onboarding/{cand_id}/pending_tasks.md"
        return WriteOnboardingFile.invoke(
            data,
            candidate_id=cand_id,
            file_path=file_path,
            content_text=content_md,
            mime_type="text/markdown",
            created_ts=kwargs.get("created_ts"),
            updated_ts=kwargs.get("updated_ts"),
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
