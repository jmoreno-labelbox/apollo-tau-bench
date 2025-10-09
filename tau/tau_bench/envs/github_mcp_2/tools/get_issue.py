from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class GetIssue(Tool):
    """Delivers information regarding a specific issue."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, issue_number: int = None) -> str:
        if not all([repo_name, issue_number]):
            payload = {"error": "repo_name and issue_number are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        for issue in _issues(data):
            #print("ISUEEE: ", issue)

            #✅ Scenario 1: flat dictionary containing a single issue
            if issue.get("repo_name") == repo_name and issue.get("number") == int(
                issue_number
            ):
                payload = issue
                out = json.dumps(payload, indent=2)
                return out

            #✅ Scenario 2: batched structure for issues
            if issue.get("repo_name") == repo_name and int(issue_number) in (
                issue.get("issue_numbers") or []
            ):
                idx = issue["issue_numbers"].index(int(issue_number))
                payload = {
                        "repo_name": repo_name,
                        "number": int(issue_number),
                        "title": issue["issue_titles"][idx],
                        "body": issue["issue_bodies"][idx],
                        "state": issue["issue_states"][idx],
                        "labels": issue["labels"][idx],
                        "assignees": issue["assignees"][idx],
                        "comments": issue["issue_comments"][idx],
                        "comment_users": issue["issue_comment_users"][idx],
                        "created_ts": issue["created_ts"][idx],
                        "updated_ts": issue["updated_ts"][idx],
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": "Issue not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetIssue",
                "description": "Returns details of a specific issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "issue_number"],
                },
            },
        }
