# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListRepoTopics(Tool):
    """Lists all topics for a given repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo = _find_repo_record(data, kwargs.get("repo_name"))
        return json.dumps({"topics": repo.get("topics", [])}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_repo_topics",
                "description": "Returns the list of repository topics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"}
                    },
                    "required": ["repo_name"]
                }
            }
        }
