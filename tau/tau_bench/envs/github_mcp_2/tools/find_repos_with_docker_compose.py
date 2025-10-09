from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class FindReposWithDockerCompose(Tool):
    """Provides repositories that include a 'docker-compose.yml' file in any branch."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        results = []

        for r in _repos(data):
            if r.get("owner") != me:
                continue
            for files in r.get("branch_files", []):
                if "docker-compose.yml" in files:
                    results.append(r["repo_name"])
                    break
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "findReposWithDockerCompose",
                "description": "Finds repositories that contain 'docker-compose.yml'.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
