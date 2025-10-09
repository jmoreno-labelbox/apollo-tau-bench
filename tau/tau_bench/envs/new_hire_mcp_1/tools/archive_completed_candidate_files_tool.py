from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class ArchiveCompletedCandidateFilesTool(Tool):
    """Refreshes file paths for archiving and generates a summary file."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str, archive_path_prefix: str = "/archived") -> str:
        files = data.setdefault("onboarding_files", [])

        updated_files = []
        archived_paths = []
        for file in files:
            if file.get("candidate_id") == candidate_id:
                old_path = file["file_path"]
                file["file_path"] = f"{archive_path_prefix}{old_path}"
                file["updated_ts"] = HARD_TS
                updated_files.append(file)
                archived_paths.append(old_path)

        summary_content = (
            f"Archived {len(archived_paths)} files for candidate {candidate_id}:\n"
            + "\n".join(archived_paths)
        )
        summary_file = {
            "file_path": f"{archive_path_prefix}/{candidate_id}/archive_summary.md",
            "content_text": summary_content,
            "mime_type": "text/markdown",
            "created_ts": HARD_TS,
            "updated_ts": HARD_TS,
            "candidate_id": candidate_id,
        }
        files.append(summary_file)
        payload = updated_files + [summary_file]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "archiveCompletedCandidateFiles",
                "description": "Archives files for a completed candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "archive_path_prefix": {"type": "string"},
                    },
                    "required": ["candidate_id"],
                },
            },
        }
