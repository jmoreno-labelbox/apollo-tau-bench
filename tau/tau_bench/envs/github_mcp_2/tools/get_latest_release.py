# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLatestRelease(Tool):
    """Returns the latest release (by timestamp) for a repo."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        releases = repo.get("releases", [])
        if not releases:
            return json.dumps({"error": "No releases found."}, indent=2)

        latest = sorted(releases, key=lambda r: r["created_at"], reverse=True)[0]
        return json.dumps(latest, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_latest_release",
                "description": "Gets the latest release for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"}
                    },
                    "required": ["repo_name"]
                }
            }
        }
