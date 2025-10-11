# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ArchiveCompletedCandidateFilesTool(Tool):
    """Updates file paths to archive them and creates a summary file."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, archive_path_prefix = "/archived") -> str:
        prefix = archive_path_prefix
        files = data.setdefault("onboarding_files", [])

        updated_files = []
        archived_paths = []
        for file in files:
            if file.get("candidate_id") == candidate_id:
                old_path = file["file_path"]
                file["file_path"] = f"{prefix}{old_path}"
                file["updated_ts"] = HARD_TS
                updated_files.append(file)
                archived_paths.append(old_path)

        summary_content = f"Archived {len(archived_paths)} files for candidate {candidate_id}:\n" + "\n".join(archived_paths)
        summary_file = {
            "file_path": f"{prefix}/{candidate_id}/archive_summary.md",
            "content_text": summary_content, "mime_type": "text/markdown",
            "created_ts": HARD_TS, "updated_ts": HARD_TS,
            "candidate_id": candidate_id
        }
        files.append(summary_file)

        return json.dumps(updated_files + [summary_file], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {"name": "archive_completed_candidate_files",
            "description": "Archives files for a completed candidate.",
            "parameters": {"type": "object", "properties": {
                "candidate_id": {"type": "string"}, "archive_path_prefix": {"type": "string"}
            }, "required": ["candidate_id"]}}}
