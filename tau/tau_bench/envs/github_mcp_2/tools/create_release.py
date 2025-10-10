# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateRelease(Tool):
    """Creates a release for a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name, tag, body = kwargs.get("repo_name"), kwargs.get("tag"), kwargs.get("body", "")
        if not all([repo_name, tag]):
            return json.dumps({"error": "repo_name and tag are required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        repo.setdefault("releases", []).append({
            "tag_name": tag,
            "body": body,
            "created_by": _auth(data)["username"],
            "created_at": get_current_timestamp()
        })

        return json.dumps({
            "message": "Release created.",
            "repo_name": repo_name,
            "tag_name": tag,
            "title": kwargs.get("title", "")
        }, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_release",
                "description": "Creates a new release (tag + body).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "tag": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"}
                    },
                    "required": ["repo_name", "tag"]
                }
            }
        }
