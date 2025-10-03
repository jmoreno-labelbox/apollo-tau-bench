from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class AddRepoTopic(Tool):
    """Attaches a topic to a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, topic: str = None) -> str:
        repo = _find_repo_record(data, repo_name)
        if not topic:
            payload = {"error": "topic is required."}
            out = json.dumps(payload, indent=2)
            return out

        topics = set(repo.get("topics", []))
        topics.add(topic)
        repo["topics"] = list(topics)
        payload = {"message": f"Topic '{topic}' added."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddRepoTopic",
                "description": "Adds a topic to a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "topic": {"type": "string"},
                    },
                    "required": ["repo_name", "topic"],
                },
            },
        }
