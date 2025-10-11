# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ActivityFeed(Tool):
    """Return a simple combined feed of recent issues/PRs/commits for a repo."""
    @staticmethod
    def invoke(data: Dict[str, Any], owner, repo, limit = 20) -> str:
        owner = owner or _actor_name(data)
        limit = int(limit)
        feed: List[Dict[str, Any]] = []
        for i in _issues(data):
            if i.get("owner") == owner and i.get("repo") == repo:
                feed.append({"type": "issue", "title": i.get("title"), "state": i.get("state"), "ts": i.get("created_at")})
        for p in _prs(data):
            if p.get("owner") == owner and p.get("repo") == repo:
                feed.append({"type": "pr", "title": p.get("title"), "state": p.get("state"), "ts": p.get("created_at")})
        for c in _commits(data):
            if c.get("owner") == owner and c.get("repo") == repo:
                feed.append({"type": "commit", "title": c.get("message"), "state": "n/a", "ts": c.get("timestamp")})
        feed.sort(key=lambda x: x.get("ts") or "", reverse=True)
        return json.dumps(feed[:limit])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "activity_feed",
                "description": "Return a simple sorted feed of repo activity (issues/PRs/commits).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "limit": {"type": "integer"}
                    },
                    "required": ["repo"]
                }
            },
        }
