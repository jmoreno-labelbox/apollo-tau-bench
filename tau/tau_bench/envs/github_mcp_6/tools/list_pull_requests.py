# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListPullRequests(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, state: str) -> str:
        """List PRs filtered by state."""
        pull_requests = list(data.get("pull_requests", {}).values())

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                prs = []
                for i, pr_number in enumerate(pr_entry["pr_numbers"]):
                    pr_state = pr_entry["pr_states"][i]
                    if state == "all" or pr_state == state:
                        prs.append({
                            "number": pr_number,
                            "state": pr_state,
                            "title": pr_entry["pr_titles"][i]
                        })
                return json.dumps({"prs": prs}, indent=2)

        return json.dumps({"prs": []}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_pull_requests",
                "description": "List PRs filtered by state.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "state": {"type": "string", "description": "PR state filter"}
                    },
                    "required": ["owner", "repo", "state"]
                }
            }
        }
