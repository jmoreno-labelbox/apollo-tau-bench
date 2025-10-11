# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AggregateRepositoryActivity(Tool):
    """Returns activity summary for each repo owned by acting user — counts of PRs, issues, alerts, commits."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        repos = [r for r in _repos(data) if r.get("owner") == me]
        repo_names = [r["repo_name"] for r in repos]

        prs = _prs(data)
        issues = _issues(data)
        alerts = _alerts(data)
        commits = _commits(data)

        summary = []
        for repo_name in repo_names:
            pr_count = sum(1 for pr in prs if pr.get("owner") == me and pr.get("repo_name") == repo_name)
            issue_count = sum(1 for i in issues if i.get("owner") == me and i.get("repo_name") == repo_name)
            alert_count = sum(1 for a in alerts if a.get("repo_name") == repo_name)
            commit_block = next((c for c in commits if c["owner"] == me and c["repo_name"] == repo_name), None)
            commit_count = sum(len(c) for c in commit_block["commit_shas"]) if commit_block else 0

            summary.append({
                "repo_name": repo_name,
                "prs": pr_count,
                "issues": issue_count,
                "alerts": alert_count,
                "commits": commit_count
            })

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "aggregate_repo_activity",
                "description": "Returns counts of PRs, issues, alerts, and commits per repository owned by current user.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
