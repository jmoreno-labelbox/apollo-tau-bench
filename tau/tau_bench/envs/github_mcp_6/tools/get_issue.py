# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetIssue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, issue_number: int) -> str:
        """Get comprehensive issue information with metadata, relationships, and statistics."""
        issues_data = list(data.get("issues", {}).values())
        commits_data = list(data.get("commits", {}).values())
        pull_requests_data = list(data.get("pull_requests", {}).values())

        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                try:
                    issue_idx = issue_entry["issue_numbers"].index(issue_number)

                    # Retrieve fundamental issue information.
                    title = issue_entry["issue_titles"][issue_idx]
                    body = issue_entry["issue_bodies"][issue_idx] if issue_idx < len(issue_entry.get("issue_bodies", [])) else ""
                    state = issue_entry["issue_states"][issue_idx]
                    labels = issue_entry["labels"][issue_idx]
                    assignees = issue_entry["assignees"][issue_idx]
                    comments = issue_entry.get("issue_comments", [[]])[issue_idx] if issue_idx < len(issue_entry.get("issue_comments", [])) else []
                    created_at = issue_entry.get("created_ts", ["2023-12-05T12:00:00Z"])[issue_idx] if issue_idx < len(issue_entry.get("created_ts", [])) else "2023-12-05T12:00:00Z"
                    updated_at = issue_entry.get("updated_ts", ["2023-12-05T12:00:00Z"])[issue_idx] if issue_idx < len(issue_entry.get("updated_ts", [])) else "2023-12-05T12:00:00Z"

                    # Create simulated responses.
                    reactions = {
                        "+1": len(assignees),
                        "-1": 0,
                        "laugh": 0,
                        "confused": 1 if "bug" in labels else 0,
                        "heart": 0,
                        "hooray": 1 if state == "closed" else 0,
                        "rocket": 0,
                        "eyes": len(comments) + 1
                    }

                    # Retrieve associated pull requests based on comparable titles/labels.
                    linked_prs = []
                    for pr_entry in pull_requests_data:
                        if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                            for i, pr_title in enumerate(pr_entry.get("pr_titles", [])):
                                if any(word in pr_title.lower() for word in title.lower().split() if len(word) > 3):
                                    linked_prs.append(pr_entry["pr_numbers"][i])

                    # Locate commits based on keywords in titles.
                    referenced_commits = []
                    for commit_entry in commits_data:
                        if commit_entry["owner"] == owner and commit_entry["repo_name"] == repo:
                            for branch_messages in commit_entry.get("commit_messages", []):
                                for j, message in enumerate(branch_messages):
                                    if f"#{issue_number}" in message or any(word in message.lower() for word in title.lower().split() if len(word) > 3):
                                        branch_idx = commit_entry["commit_messages"].index(branch_messages)
                                        if j < len(commit_entry["commit_shas"][branch_idx]):
                                            referenced_commits.append(commit_entry["commit_shas"][branch_idx][j])

                    result = {
                        "success": True,
                        "data": {
                            "number": issue_number,
                            "title": title,
                            "body": body,
                            "state": state,
                            "labels": labels,
                            "assignees": assignees,
                            "milestone": None,
                            "author": assignees[0] if assignees else owner,
                            "locked": False,
                            "reactions": reactions
                        },
                        "metadata": {
                            "created_at": created_at,
                            "updated_at": updated_at,
                            "closed_at": None if state == "open" else updated_at,
                            "url": f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}",
                            "html_url": f"https://github.com/{owner}/{repo}/issues/{issue_number}"
                        },
                        "relationships": {
                            "repository": f"{owner}/{repo}",
                            "comments_count": len(comments),
                            "linked_pull_requests": linked_prs[:3],  # Restrict to a maximum of 3.
                            "referenced_in_commits": referenced_commits[:5],  # Restrict to the initial 5.
                            "parent_issue": None,
                            "child_issues": []
                        },
                        "counts": {
                            "comments": len(comments),
                            "reactions_total": sum(reactions.values()),
                            "referenced_commits": len(referenced_commits)
                        }
                    }
                    return json.dumps(result, indent=2)
                except ValueError:
                    pass

        return json.dumps({
            "success": False,
            "error": f"Issue # {issue_number} is not present in the repository {owner}/{repo}.",
            "error_code": "ISSUE_NOT_FOUND",
            "metadata": {
                "repository": f"{owner}/{repo}",
                "requested_issue": issue_number,
                "search_timestamp": "2023-12-05T12:00:00Z"
            },
            "suggestions": [
                f"Check if issue # {issue_number} is present in the {owner}/{repo} repository.",
                "Verify repository name and owner are correct",
                "Use search_issues tool to find available issues"
            ]
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_issue",
                "description": "Get comprehensive issue information including metadata, relationships to pull requests and commits, reaction counts, and timeline data.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "issue_number": {"type": "integer", "description": "Issue number"}
                    },
                    "required": ["owner", "repo", "issue_number"]
                }
            }
        }