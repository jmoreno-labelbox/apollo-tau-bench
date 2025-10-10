# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchPullRequestsByRepositoryId(Tool):
    """Searches for all pull requests within a specific repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repository_id = kwargs.get("repository_id")
        pull_requests = list(data.get("pull_requests", {}).values())
        
        matching_prs = [
            pr for pr in pull_requests if pr.get("repository_id") == repository_id
        ]
        
        return json.dumps({"pull_requests": matching_prs})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_pull_requests_by_repository_id",
                "description": "Searches for all pull requests within a specific repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {
                            "type": "string",
                            "description": "The unique ID of the repository to search within.",
                        }
                    },
                    "required": ["repository_id"],
                },
            },
        }
