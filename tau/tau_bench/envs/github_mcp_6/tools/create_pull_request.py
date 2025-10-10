# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePullRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, title: str, body: str, head: str, base: str, draft: bool = False) -> str:
        """Create a comprehensive pull request with detailed information, relationships, and status checks."""
        pull_requests = list(data.get("pull_requests", {}).values())
        repositories = list(data.get("repositories", {}).values())
        commits_data = list(data.get("commits", {}).values())
        issues_data = list(data.get("issues", {}).values())

        # Check if the repository is present.
        target_repo = None
        for repository in repositories:
            if repository["owner"] == owner and repository["repo_name"] == repo:
                target_repo = repository
                break

        if not target_repo:
            return json.dumps({
                "success": False,
                "error": f"Repository {owner}/{repo} not found",
                "error_code": "REPOSITORY_NOT_FOUND",
                "metadata": {
                    "requested_repository": f"{owner}/{repo}",
                    "search_timestamp": "2023-12-05T12:00:00Z"
                },
                "suggestions": [
                    f"Verify repository {owner}/{repo} exists",
                    "Check repository owner and name spelling"
                ]
            }, indent=2)

        # Check for the existence of branches.
        if head not in target_repo.get("branches", []):
            return json.dumps({
                "success": False,
                "error": f"Head branch '{head}' not found in repository",
                "error_code": "HEAD_BRANCH_NOT_FOUND",
                "metadata": {
                    "repository": f"{owner}/{repo}",
                    "requested_head": head,
                    "available_branches": target_repo.get("branches", [])
                },
                "suggestions": [
                    f"Use one of the available branches: {target_repo.get('branches', [])}",
                    f"Create branch '{head}' before creating the pull request"
                ]
            }, indent=2)

        if base not in target_repo.get("branches", []):
            return json.dumps({
                "success": False,
                "error": f"Base branch '{base}' not found in repository",
                "error_code": "BASE_BRANCH_NOT_FOUND",
                "metadata": {
                    "repository": f"{owner}/{repo}",
                    "requested_base": base,
                    "available_branches": target_repo.get("branches", [])
                },
                "suggestions": [
                    f"Use one of the available branches: {target_repo.get('branches', [])}",
                    f"Create branch '{base}' before creating the pull request"
                ]
            }, indent=2)

        # Locate the current PR entry for this repository.
        repo_prs = None
        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                repo_prs = pr_entry
                break

        if not repo_prs:
            # Generate a new pull request entry.
            pr_number = 1
            repo_prs = {
                "owner": owner,
                "repo_name": repo,
                "pr_numbers": [pr_number],
                "pr_titles": [title],
                "pr_bodies": [body],
                "pr_states": ["open"],
                "head_branches": [head],
                "base_branches": [base],
                "head_shas": [f"head_sha_{pr_number}"],
                "mergeable_flags": [True],
                "merged_flags": [False],
                "pr_files": [[[]]],
                "pr_comments": [[[]]],
                "pr_comment_users": [[[]]],
                "reviewers": [[[]]],
                "review_states": [[[]]],
                "review_events": [[[]]],
                "created_ts": ["2023-12-05T12:00:00Z"],
                "updated_ts": ["2023-12-05T12:00:00Z"]
            }
            pull_requests.append(repo_prs)
        else:
            # Append to the current PR record.
            pr_number = max(repo_prs["pr_numbers"]) + 1
            repo_prs["pr_numbers"].append(pr_number)
            repo_prs["pr_titles"].append(title)
            repo_prs["pr_bodies"].append(body)
            repo_prs["pr_states"].append("open")
            repo_prs["head_branches"].append(head)
            repo_prs["base_branches"].append(base)
            repo_prs["head_shas"].append(f"head_sha_{pr_number}")
            repo_prs["mergeable_flags"].append(True)
            repo_prs["merged_flags"].append(False)
            repo_prs["pr_files"].append([[]])
            repo_prs["pr_comments"].append([[]])
            repo_prs["pr_comment_users"].append([[]])
            repo_prs["reviewers"].append([[]])
            repo_prs["review_states"].append([[]])
            repo_prs["review_events"].append([[]])
            repo_prs["created_ts"].append("2023-12-05T12:00:00Z")
            repo_prs["updated_ts"].append("2023-12-05T12:00:00Z")

        # Determine modified files and commit counts.
        head_idx = target_repo["branches"].index(head)
        base_idx = target_repo["branches"].index(base)

        head_files = set(target_repo.get("branch_files", [[]])[head_idx] if head_idx < len(target_repo.get("branch_files", [])) else [])
        base_files = set(target_repo.get("branch_files", [[]])[base_idx] if base_idx < len(target_repo.get("branch_files", [])) else [])

        changed_files = list(head_files.symmetric_difference(base_files))
        additions = len(head_files - base_files) * 20  # Create a mock file containing 20 lines each.
        deletions = len(base_files - head_files) * 10   # Simulate 10 lines for each removed file.

        # Identify commits present in the head branch that are absent in the base branch.
        commits_in_pr = []
        for commit_entry in commits_data:
            if commit_entry["owner"] == owner and commit_entry["repo_name"] == repo:
                if head in commit_entry.get("branch_names", []):
                    head_branch_idx = commit_entry["branch_names"].index(head)
                    commits_in_pr = commit_entry.get("commit_shas", [[]])[head_branch_idx][:5]  # Restrict to a maximum of 5 commits.
                    break

        # Identify associated issues (analyze content for issue mentions)
        linked_issues = []
        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                for i, issue_number in enumerate(issue_entry.get("issue_numbers", [])):
                    if f"#{issue_number}" in body or f"closes #{issue_number}" in body.lower() or f"fixes # {issue_number} is present in body.lower() or f"fixes #{issue_number}" exists in body.lower():
                        linked_issues.append(issue_number)

        # Identify conflicting pull requests (mocked on the same base branch).
        conflicts_with = []
        for i, pr_base in enumerate(repo_prs.get("base_branches", [])):
            if pr_base == base and repo_prs["pr_numbers"][i] != pr_number and repo_prs["pr_states"][i] == "open":
                conflicts_with.append(repo_prs["pr_numbers"][i])

        # Simulated status verification
        checks = {
            "status": "pending",
            "total": 3,
            "passed": 1,
            "failed": 0,
            "pending": 2
        }

        if "test" in title.lower() or "fix" in title.lower():
            checks["status"] = "success"
            checks["passed"] = 3
            checks["pending"] = 0
        elif "wip" in title.lower() or draft:
            checks["status"] = "pending"
            checks["passed"] = 0
            checks["pending"] = 3

        result = {
            "success": True,
            "data": {
                "number": pr_number,
                "state": "open",
                "title": title,
                "body": body,
                "head": head,
                "base": base,
                "mergeable": True,
                "draft": draft,
                "url": f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}",
                "html_url": f"https://github.com/{owner}/{repo}/pull/{pr_number}"
            },
            "metadata": {
                "created_at": "2023-12-05T12:00:00Z",
                "updated_at": "2023-12-05T12:00:00Z",
                "merged_at": None,
                "closed_at": None,
                "author": owner,
                "merge_commit_sha": None
            },
            "relationships": {
                "repository": f"{owner}/{repo}",
                "base_repository": f"{owner}/{repo}",
                "head_repository": f"{owner}/{repo}",
                "linked_issues": linked_issues,
                "conflicts_with": conflicts_with,
                "depends_on": []
            },
            "counts": {
                "commits": len(commits_in_pr),
                "changed_files": len(changed_files),
                "additions": additions,
                "deletions": deletions,
                "comments": 0,
                "review_comments": 0,
                "reviews": 0
            },
            "checks": checks
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_pull_request",
                "description": "Create a comprehensive pull request with detailed information including commit counts, file changes, status checks, linked issues, and conflict detection.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "title": {"type": "string", "description": "PR title"},
                        "body": {"type": "string", "description": "PR description"},
                        "head": {"type": "string", "description": "Head branch"},
                        "base": {"type": "string", "description": "Base branch"},
                        "draft": {"type": "boolean", "description": "Create as draft PR (defaults to false)", "default": False}
                    },
                    "required": ["owner", "repo", "title", "body", "head", "base"]
                }
            }
        }
