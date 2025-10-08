from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class RemoveRepoTopic(Tool):
    """Detaches a topic from a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, topic: str = None) -> str:
        repo = _find_repo_record(data, repo_name)
        if not topic:
            payload = {"error": "topic is required."}
            out = json.dumps(payload, indent=2)
            return out

        repo["topics"] = [t for t in repo.get("topics", []) if t != topic]
        payload = {"message": f"Topic '{topic}' removed."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "RemoveRepoTopic",
                "description": "Removes a topic from a repository.",
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
