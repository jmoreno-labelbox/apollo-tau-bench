# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateIssue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, title: str, body: str, assignees: List[str], labels: List[str] = None) -> str:
        """Create an issue with labels/assignees."""
        issues_data = list(data.get("issues", {}).values())

        # Check the assignees parameter for validity.
        if assignees is None:
            assignees = []
        elif not isinstance(assignees, list):
            assignees = [assignees] if assignees else []

        # Check the validity of the labels parameter.
        if labels is None:
            labels = []
        elif not isinstance(labels, list):
            labels = [labels] if labels else []

        # Locate the current issue record for this repository.
        repo_issues = None
        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                repo_issues = issue_entry
                break

        if not repo_issues:
            # Generate a new issue record.
            issue_number = 1
            repo_issues = {
                "owner": owner,
                "repo_name": repo,
                "issue_numbers": [issue_number],
                "issue_titles": [title],
                "issue_bodies": [body],
                "issue_states": ["open"],
                "labels": [labels],
                "assignees": [assignees],
                "issue_comments": [[]],
                "issue_comment_users": [[]],
                "created_ts": ["2023-12-05T12:00:00Z"],
                "updated_ts": ["2023-12-05T12:00:00Z"]
            }
            issues_data.append(repo_issues)
        else:
            # Increment the highest current issue number by 1 and append it to the issue entry.
            issue_number = max(repo_issues["issue_numbers"]) + 1
            repo_issues["issue_numbers"].append(issue_number)
            repo_issues["issue_titles"].append(title)
            repo_issues["issue_bodies"].append(body)
            repo_issues["issue_states"].append("open")
            repo_issues["labels"].append(labels)
            repo_issues["assignees"].append(assignees)
            repo_issues["issue_comments"].append([])
            repo_issues["issue_comment_users"].append([])
            repo_issues["created_ts"].append("2023-12-05T12:00:00Z")
            repo_issues["updated_ts"].append("2023-12-05T12:00:00Z")

        return json.dumps({"issue_number": issue_number}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_issue",
                "description": "Create an issue with labels/assignees.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "title": {"type": "string", "description": "Issue title"},
                        "body": {"type": "string", "description": "Issue body"},
                        "assignees": {"type": "array", "items": {"type": "string"}, "description": "Issue assignees"},
                        "labels": {"type": "array", "items": {"type": "string"}, "description": "Issue labels"}
                    },
                    "required": ["owner", "repo", "title", "body", "assignees"]
                }
            }
        }
