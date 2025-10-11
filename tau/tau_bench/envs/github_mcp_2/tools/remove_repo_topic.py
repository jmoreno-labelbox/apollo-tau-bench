# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveRepoTopic(Tool):
    """Removes a topic from a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], repo_name, topic) -> str:
        repo = _find_repo_record(data, repo_name)
        if not topic:
            return json.dumps({"error": "topic is required."}, indent=2)

        repo["topics"] = [t for t in repo.get("topics", []) if t != topic]
        return json.dumps({"message": f"Topic '{topic}' removed."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "remove_repo_topic",
                "description": "Removes a topic from a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "topic": {"type": "string"}
                    },
                    "required": ["repo_name", "topic"]
                }
            }
        }
