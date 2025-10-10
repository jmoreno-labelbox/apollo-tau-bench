# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddRepoTopic(Tool):
    """Adds a topic to a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], repo_name, topic) -> str:
        repo = _find_repo_record(data, repo_name)
        if not topic:
            return json.dumps({"error": "topic is required."}, indent=2)

        topics = set(repo.get("topics", []))
        topics.add(topic)
        repo["topics"] = list(topics)
        return json.dumps({"message": f"Topic '{topic}' added."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "add_repo_topic",
                "description": "Adds a topic to a repository.",
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
