# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPullRequestStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, pullNumber: int) -> str:
        """Get combined status checks for a PR."""
        pull_requests = list(data.get("pull_requests", {}).values())

        # Find the pull request
        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)
                    pr_state = pr_entry["pr_states"][pr_idx]

                    # Generate realistic status checks based on PR state and title
                    checks = []

                    # Always include CI check
                    if pr_state == "open":
                        checks.append({"context": "continuous-integration", "state": "success"})
                        checks.append({"context": "code-review", "state": "pending"})
                        checks.append({"context": "security-scan", "state": "success"})
                    elif pr_state == "merged":
                        checks.append({"context": "continuous-integration", "state": "success"})
                        checks.append({"context": "code-review", "state": "success"})
                        checks.append({"context": "security-scan", "state": "success"})
                    else:
                        checks.append({"context": "continuous-integration", "state": "failure"})
                        checks.append({"context": "code-review", "state": "pending"})

                    # Add additional checks based on PR title
                    pr_title = pr_entry.get("pr_titles", [""])[pr_idx] if pr_idx < len(pr_entry.get("pr_titles", [])) else ""
                    if "test" in pr_title.lower():
                        checks.append({"context": "unit-tests", "state": "success"})
                    if "security" in pr_title.lower():
                        checks.append({"context": "security-audit", "state": "success"})

                    result = {
                        "state": "success" if all(check["state"] == "success" for check in checks) else "pending",
                        "total_count": len(checks),
                        "statuses": checks
                    }
                    return json.dumps(result, indent=2)
                except ValueError:
                    pass

        # Default response if PR not found
        result = {
            "state": "pending",
            "total_count": 2,
            "statuses": [
                {"context": "continuous-integration", "state": "pending"},
                {"context": "code-review", "state": "pending"}
            ]
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pull_request_status",
                "description": "Get combined status checks for a PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number"}
                    },
                    "required": ["owner", "repo", "pullNumber"]
                }
            }
        }
