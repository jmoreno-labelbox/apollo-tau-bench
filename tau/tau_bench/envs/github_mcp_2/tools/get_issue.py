# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetIssue(Tool):
    """Returns details of a specific issue."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        number = kwargs.get("issue_number")
        if not all([repo_name, number]):
            return json.dumps({"error": "repo_name and issue_number are required."}, indent=2)

        for issue in _issues(data):
            # print("ISSUE: ", issue)

            # ✅ Scenario 1: simple dictionary with one problem
            if issue.get("repo_name") == repo_name and issue.get("number") == int(number):
                return json.dumps(issue, indent=2)

            # ✅ Scenario 2: grouped issue framework
            if issue.get("repo_name") == repo_name and int(number) in (issue.get("issue_numbers") or []):
                idx = issue["issue_numbers"].index(int(number))
                return json.dumps({
                    "repo_name": repo_name,
                    "number": int(number),
                    "title": issue["issue_titles"][idx],
                    "body": issue["issue_bodies"][idx],
                    "state": issue["issue_states"][idx],
                    "labels": issue["labels"][idx],
                    "assignees": issue["assignees"][idx],
                    "comments": issue["issue_comments"][idx],
                    "comment_users": issue["issue_comment_users"][idx],
                    "created_ts": issue["created_ts"][idx],
                    "updated_ts": issue["updated_ts"][idx],
                }, indent=2)

        return json.dumps({"error": "Issue not found."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_issue",
                "description": "Returns details of a specific issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"}
                    },
                    "required": ["repo_name", "issue_number"]
                }
            }
        }
