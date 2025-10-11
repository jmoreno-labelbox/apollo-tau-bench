# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_repo_record(data: Dict[str, Any], repo_name: str) -> Dict[str, Any]:
    """
    Find a repo owned by the acting user. repositories is a LIST in our dataset,
    so iterate; do NOT use dict.get.
    """
    me = _auth(data)["username"]
    repos = data.get("repositories") or []
    for r in repos:
        if r.get("owner") == me and r.get("repo_name") == repo_name:
            return r
    # Mirror RULES: if not found, surface a crisp error (no workarounds)
    raise Exception(f"Repository not found for owner '{me}': {repo_name}")

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