from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class GetLatestRelease(Tool):
    """Provides the most recent release (sorted by timestamp) for a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None) -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        repo = _find_repo_record(data, repo_name)
        releases = repo.get("releases", [])
        if not releases:
            payload = {"error": "No releases found."}
            out = json.dumps(payload, indent=2)
            return out

        latest = sorted(releases, key=lambda r: r["created_at"], reverse=True)[0]
        payload = latest
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetLatestRelease",
                "description": "Gets the latest release for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
