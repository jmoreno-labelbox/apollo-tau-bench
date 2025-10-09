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

class CheckFileStorageOrganizationTool(Tool):
    """Assesses the onboarding_files table to analyze file path organization, duplicate content, and the completeness of candidate files."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None) -> str:
        files = data.get("onboarding_files", [])

        if candidate_id:
            files = [
                f for f in files if str(f.get("candidate_id")) == str(candidate_id)
            ]

        # Evaluate duplicates based on content_text
        content_map = {}
        duplicates = []
        for file in files:
            content = file.get("content_text")
            if content:
                if content in content_map:
                    duplicates.append(
                        {
                            "original": content_map[content],
                            "duplicate": file.get("file_path"),
                        }
                    )
                else:
                    content_map[content] = file.get("file_path")

        # Examine organization (basic check for path structure)
        improperly_organized = [
            f.get("file_path")
            for f in files
            if not re.match(
                r"/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+/", str(f.get("file_path", ""))
            )
        ]

        result = {
            "total_files_analyzed": len(files),
            "duplicate_files_found": len(duplicates),
            "improperly_organized_paths": improperly_organized,
            "duplicates": duplicates,
        }
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "checkFileStorageOrganization",
                "description": "Reviews onboarding_files table analyzing file path organization, duplicate content, and candidate file completeness.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {
                            "type": "string",
                            "description": "Specific candidate or null for system analysis",
                        }
                    },
                    "required": [],
                },
            },
        }
