# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindReposWithDockerCompose(Tool):
    """Returns repositories that contain a 'docker-compose.yml' file in any branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        results = []

        for r in _repos(data):
            if r.get("owner") != me:
                continue
            for files in r.get("branch_files", []):
                if "docker-compose.yml" in files:
                    results.append(r["repo_name"])
                    break

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "find_repos_with_docker_compose",
                "description": "Finds repositories that contain 'docker-compose.yml'.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
