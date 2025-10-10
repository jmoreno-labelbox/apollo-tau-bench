# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateBranch(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, branch: str, sha: str = None, base_branch: str = "main") -> str:
        """Create a comprehensive branch with detailed information, relationships, and metadata."""
        repositories = list(data.get("repositories", {}).values())
        commits_data = list(data.get("commits", {}).values())
        pull_requests_data = list(data.get("pull_requests", {}).values())

        # Validate repository exists
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

        # Validate base branch exists
        if base_branch not in target_repo.get("branches", []):
            return json.dumps({
                "success": False,
                "error": f"Base branch '{base_branch}' not found in repository",
                "error_code": "BASE_BRANCH_NOT_FOUND",
                "metadata": {
                    "repository": f"{owner}/{repo}",
                    "requested_base": base_branch,
                    "available_branches": target_repo.get("branches", [])
                },
                "suggestions": [
                    f"Use one of the available branches: {target_repo.get('branches', [])}",
                    f"Create base branch '{base_branch}' first"
                ]
            }, indent=2)

        # Check if branch already exists
        if branch in target_repo.get("branches", []):
            return json.dumps({
                "success": False,
                "error": f"Branch '{branch}' already exists in repository",
                "error_code": "BRANCH_ALREADY_EXISTS",
                "metadata": {
                    "repository": f"{owner}/{repo}",
                    "existing_branch": branch,
                    "all_branches": target_repo.get("branches", [])
                },
                "suggestions": [
                    f"Choose a different branch name",
                    f"Delete branch '{branch}' first if you want to recreate it",
                    f"Use an existing branch: {target_repo.get('branches', [])}"
                ]
            }, indent=2)

        # Find base branch index
        base_branch_idx = target_repo["branches"].index(base_branch)

        # If no SHA provided, use fallback logic to find latest commit from base branch
        if sha is None:
            fallback_sha = None
            for commit_entry in commits_data:
                if commit_entry["owner"] == owner and commit_entry["repo_name"] == repo:
                    if base_branch in commit_entry.get("branch_names", []):
                        branch_idx = commit_entry["branch_names"].index(base_branch)
                        if commit_entry.get("commit_shas", [[]])[branch_idx]:
                            fallback_sha = commit_entry["commit_shas"][branch_idx][0]  # Use latest commit
                            break

            if fallback_sha:
                sha = fallback_sha
            else:
                return json.dumps({
                    "success": False,
                    "error": f"No commits found in base branch '{base_branch}'",
                    "error_code": "NO_COMMITS_FOUND",
                    "metadata": {
                        "repository": f"{owner}/{repo}",
                        "base_branch": base_branch
                    },
                    "suggestions": [
                        "Ensure the base branch has at least one commit",
                        "Provide a specific SHA parameter",
                        "Create a commit in the base branch first"
                    ]
                }, indent=2)

        # Validate SHA exists in commit history
        sha_valid = False
        base_commit = None
        for commit_entry in commits_data:
            if commit_entry["owner"] == owner and commit_entry["repo_name"] == repo:
                for branch_commits in commit_entry.get("commit_shas", []):
                    if sha in branch_commits:
                        sha_valid = True
                        # Find commit details
                        sha_idx = branch_commits.index(sha)
                        branch_idx = commit_entry["commit_shas"].index(branch_commits)
                        base_commit = {
                            "sha": sha,
                            "message": commit_entry["commit_messages"][branch_idx][sha_idx],
                            "author": commit_entry["commit_authors"][branch_idx][sha_idx],
                            "timestamp": commit_entry["commit_timestamps"][branch_idx][sha_idx]
                        }
                        break
                if sha_valid:
                    break

        if not sha_valid:
            # Try to find a valid SHA from the base branch as fallback
            fallback_sha = None
            for commit_entry in commits_data:
                if commit_entry["owner"] == owner and commit_entry["repo_name"] == repo:
                    if base_branch in commit_entry.get("branch_names", []):
                        branch_idx = commit_entry["branch_names"].index(base_branch)
                        if commit_entry.get("commit_shas", [[]])[branch_idx]:
                            fallback_sha = commit_entry["commit_shas"][branch_idx][0]  # Use latest commit
                            break

            if fallback_sha:
                # Use fallback SHA instead of failing
                sha = fallback_sha
                sha_valid = True
                # Find commit details for fallback SHA
                for commit_entry in commits_data:
                    if commit_entry["owner"] == owner and commit_entry["repo_name"] == repo:
                        for branch_commits in commit_entry.get("commit_shas", []):
                            if sha in branch_commits:
                                sha_idx = branch_commits.index(sha)
                                branch_idx = commit_entry["commit_shas"].index(branch_commits)
                                base_commit = {
                                    "sha": sha,
                                    "message": commit_entry["commit_messages"][branch_idx][sha_idx],
                                    "author": commit_entry["commit_authors"][branch_idx][sha_idx],
                                    "timestamp": commit_entry["commit_timestamps"][branch_idx][sha_idx]
                                }
                                break
                        if base_commit:
                            break
            else:
                return json.dumps({
                    "success": False,
                    "error": f"SHA '{sha}' not found in repository commit history",
                    "error_code": "SHA_NOT_FOUND",
                    "metadata": {
                        "repository": f"{owner}/{repo}",
                        "requested_sha": sha,
                        "base_branch": base_branch
                    },
                    "suggestions": [
                        "Use a valid commit SHA from the repository",
                        "List commits first to find a valid SHA",
                        "Use the latest commit SHA from the base branch"
                    ]
                }, indent=2)

        # Create new branch - copy from base branch
        target_repo["branches"].append(branch)
        target_repo["branch_files"].append(target_repo["branch_files"][base_branch_idx].copy())
        target_repo["branch_contents"].append(target_repo["branch_contents"][base_branch_idx].copy())
        target_repo["branch_shas"].append(sha)

        # Calculate branch statistics
        base_files = target_repo["branch_files"][base_branch_idx]
        files_changed = 0  # Initially same as base
        commits_ahead = 0  # New branch, no commits ahead yet
        commits_behind = 0  # New branch, not behind
        contributors = 1   # Creator

        # Find derived branches (other branches created from the same base)
        derived_branches = []
        for existing_branch in target_repo.get("branches", []):
            if existing_branch != branch and existing_branch != base_branch:
                derived_branches.append(existing_branch)

        # Find pull requests that use this branch (should be empty for new branch)
        pull_requests_using_branch = []
        for pr_entry in pull_requests_data:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                for i, head_branch in enumerate(pr_entry.get("head_branches", [])):
                    if head_branch == branch:
                        pull_requests_using_branch.append(pr_entry["pr_numbers"][i])

        # Find commits unique to this branch (should be empty for new branch)
        commits_unique_to_branch = []

        # Check if branch is protected (mock based on naming patterns)
        protected = branch in ["main", "master", "develop", "production"] or "release" in branch.lower()

        result = {
            "success": True,
            "data": {
                "name": branch,
                "sha": sha,
                "protected": protected,
                "url": f"https://api.github.com/repos/{owner}/{repo}/branches/{branch}",
                "commit": base_commit
            },
            "metadata": {
                "created_at": "2023-12-05T12:00:00Z",
                "created_by": owner,
                "base_branch": base_branch,
                "base_sha": sha,
                "ahead_by": commits_ahead,
                "behind_by": commits_behind
            },
            "relationships": {
                "repository": f"{owner}/{repo}",
                "parent_branch": base_branch,
                "derived_branches": derived_branches[:5],  # Limit to 5
                "pull_requests": pull_requests_using_branch,
                "commits_unique_to_branch": commits_unique_to_branch
            },
            "counts": {
                "commits_ahead": commits_ahead,
                "commits_behind": commits_behind,
                "files_changed": files_changed,
                "contributors": contributors
            }
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_branch",
                "description": "Create a comprehensive branch with detailed information including commit details, protection status, relationships to other branches, and statistics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "branch": {"type": "string", "description": "New branch name"},
                        "sha": {"type": "string", "description": "Base SHA for branch"},
                        "base_branch": {"type": "string", "description": "Base branch to create from (defaults to 'main')", "default": "main"}
                    },
                    "required": ["owner", "repo", "branch"]
                }
            }
        }
