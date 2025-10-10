# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckFileStorageOrganizationTool(Tool):
    """Reviews onboarding_files table analyzing file path organization, duplicate content, and candidate file completeness."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")

        files = data.get("onboarding_files", [])

        if candidate_id:
            files = [f for f in files if str(f.get("candidate_id")) == str(candidate_id)]

        # Examine duplicates according to content_text.
        content_map = {}
        duplicates = []
        for file in files:
            content = file.get("content_text")
            if content:
                if content in content_map:
                    duplicates.append({
                        "original": content_map[content],
                        "duplicate": file.get("file_path")
                    })
                else:
                    content_map[content] = file.get("file_path")

        # Examine the structure of the path within the organization.
        improperly_organized = [
            f.get("file_path") for f in files
            if not re.match(r"/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+/", str(f.get("file_path", "")))
        ]

        result = {
            "total_files_analyzed": len(files),
            "duplicate_files_found": len(duplicates),
            "improperly_organized_paths": improperly_organized,
            "duplicates": duplicates
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_file_storage_organization",
                "description": "Reviews onboarding_files table analyzing file path organization, duplicate content, and candidate file completeness.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "Specific candidate or null for system analysis"}
                    },
                    "required": [],
                },
            },
        }
