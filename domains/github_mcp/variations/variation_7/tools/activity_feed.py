from tau_bench.envs.tool import Tool
import json
from typing import Any

class ActivityFeed(Tool):
    """Provide a straightforward combined feed of recent issues, pull requests, and commits for a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, limit: int = 20) -> str:
        owner = owner or _actor_name(data)
        feed: list[dict[str, Any]] = []
        for i in _issues(data):
            if i.get("owner") == owner and i.get("repo") == repo:
                feed.append(
                    {
                        "type": "issue",
                        "title": i.get("title"),
                        "state": i.get("state"),
                        "ts": i.get("created_at"),
                    }
                )
        for p in _prs(data):
            if p.get("owner") == owner and p.get("repo") == repo:
                feed.append(
                    {
                        "type": "pr",
                        "title": p.get("title"),
                        "state": p.get("state"),
                        "ts": p.get("created_at"),
                    }
                )
        for c in _commits(data):
            if c.get("owner") == owner and c.get("repo") == repo:
                feed.append(
                    {
                        "type": "commit",
                        "title": c.get("message"),
                        "state": "n/a",
                        "ts": c.get("timestamp"),
                    }
                )
        feed.sort(key=lambda x: x.get("ts") or "", reverse=True)
        payload = feed[:limit]
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "activityFeed",
                "description": "Return a simple sorted feed of repo activity (issues/PRs/commits).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "limit": {"type": "integer"},
                    },
                    "required": ["repo"],
                },
            },
        }
