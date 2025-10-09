from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListCommits(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str,
        repo: str,
        branch: str,
        page: int = 1,
        per_page: int = 30,
    ) -> str:
        """List comprehensive commit information with metadata, relationships, and statistics."""
        pass
        commits = data.get("commits", {}).values()
        repositories = data.get("repositories", {}).values()
        pull_requests_data = data.get("pull_requests", {}).values()
        issues_data = data.get("issues", {}).values()

        #Locate the repository to confirm its existence
        target_repo = None
        for repository in repositories.values():
            if repository["owner"] == owner and repository["repo_name"] == repo:
                target_repo = repository
                break

        if not target_repo:
            payload = {
                    "success": False,
                    "error": f"Repository {owner}/{repo} not found",
                    "error_code": "REPOSITORY_NOT_FOUND",
                    "metadata": {
                        "requested_repository": f"{owner}/{repo}",
                        "search_timestamp": "2023-12-05T12:00:00Z",
                    },
                    "suggestions": [
                        f"Verify repository {owner}/{repo} exists",
                        "Check repository owner and name spelling",
                    ],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Identify commits for the specified repository and branch
        for commit_entry in commits.values():
            if commit_entry["owner"] == owner and commit_entry["repo_name"] == repo:
                try:
                    branch_idx = commit_entry["branch_names"].index(branch)
                    all_commits = []

                    #Construct detailed commit information
                    for i, sha in enumerate(commit_entry["commit_shas"][branch_idx]):
                        message = commit_entry["commit_messages"][branch_idx][i]
                        author = commit_entry["commit_authors"][branch_idx][i]
                        timestamp = commit_entry["commit_timestamps"][branch_idx][i]

                        #Simulate extra commit data
                        tree_sha = f"tree_{sha[-8:]}"
                        parent_shas = [f"parent_{i-1}_{sha[-6:]}"] if i > 0 else []

                        #Compute statistics (simulated based on the message)
                        is_merge = "merge" in message.lower()
                        additions = 50 if not is_merge else 100
                        deletions = 10 if not is_merge else 20

                        #Identify impacted files (simulated based on file patterns in the message)
                        files_changed = []
                        for file_path in target_repo.get("file_paths", []):
                            filename = file_path.split("/")[-1]
                            if (
                                filename.lower() in message.lower()
                                or file_path.split(".")[-1] in message.lower()
                            ):
                                files_changed.append(file_path)

                        if not files_changed and not is_merge:
                            #Fallback to common files if no specific matches are found
                            files_changed = target_repo.get("file_paths", [])[:3]

                        commit_data = {
                            "sha": sha,
                            "message": message,
                            "author": author,
                            "timestamp": timestamp,
                            "committer": author,
                            "tree_sha": tree_sha,
                            "parent_shas": parent_shas,
                            "stats": {
                                "additions": additions,
                                "deletions": deletions,
                                "total": additions + deletions,
                            },
                            "files_changed": files_changed,
                            "verification": {
                                "verified": "bot" not in author.lower(),
                                "reason": (
                                    "valid"
                                    if "bot" not in author.lower()
                                    else "unsigned"
                                ),
                            },
                        }
                        all_data["commits"][commit_data["commit_id"]] = commit_data

                    #Implement pagination
                    start_idx = (page - 1) * per_page
                    end_idx = start_idx + per_page
                    paginated_commits = all_commits[start_idx:end_idx]

                    #Identify associated pull requests and issues
                    related_prs = []
                    related_issues = []

                    for pr_entry in pull_requests_data.values():
                        if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                            for i, pr_title in enumerate(pr_entry.get("pr_titles", [])):
                                if any(
                                    sha[:8] in pr_title
                                    for sha in [c["sha"] for c in all_commits]
                                ):
                                    related_prs.append(pr_entry["pr_numbers"][i])

                    for issue_entry in issues_data.values():
                        if (
                            issue_entry["owner"] == owner
                            and issue_entry["repo_name"] == repo
                        ):
                            for i, issue_title in enumerate(
                                issue_entry.get("issue_titles", [])
                            ):
                                if any(
                                    word
                                    in " ".join([c["message"] for c in all_commits])
                                    for word in issue_title.lower().split()
                                    if len(word) > 3
                                ):
                                    related_issues.append(
                                        issue_entry["issue_numbers"][i]
                                    )

                    #Compute statistics
                    unique_authors = list({c["author"] for c in all_commits})
                    merge_commits = [
                        c for c in all_commits if "merge" in c["message"].lower()
                    ]
                    files_touched = list(
                        {f for c in all_commits for f in c["files_changed"]}
                    )

                    #Identify tags (simulate some version tags)
                    tags = []
                    if len(all_commits) > 10:
                        tags = [f"v1.{len(all_commits) // 10}.0"]

                    result = {
                        "success": True,
                        "data": {"commits": paginated_commits},
                        "metadata": {
                            "branch": branch,
                            "total_commits": len(all_commits),
                            "date_range": {
                                "earliest": (
                                    all_commits[-1]["timestamp"]
                                    if all_commits
                                    else None
                                ),
                                "latest": (
                                    all_commits[0]["timestamp"] if all_commits else None
                                ),
                            },
                            "pagination": {
                                "page": page,
                                "per_page": per_page,
                                "has_more": end_idx < len(all_commits),
                            },
                        },
                        "relationships": {
                            "repository": f"{owner}/{repo}",
                            "pull_requests": related_prs[:5],
                            "issues": related_issues[:5],
                            "tags": tags,
                        },
                        "counts": {
                            "total_commits": len(all_commits),
                            "unique_authors": len(unique_authors),
                            "merge_commits": len(merge_commits),
                            "files_touched": len(files_touched),
                        },
                    }
                    payload = result
                    out = json.dumps(payload, indent=2)
                    return out
                except ValueError:
                    pass
        payload = {
                "success": False,
                "error": f"Branch {branch} not found in repository {owner}/{repo}",
                "error_code": "BRANCH_NOT_FOUND",
                "metadata": {
                    "repository": f"{owner}/{repo}",
                    "requested_branch": branch,
                    "available_branches": target_repo.get("branches", []),
                    "search_timestamp": "2023-12-05T12:00:00Z",
                },
                "suggestions": [
                    f"Use one of the available branches: {target_repo.get('branches', [])}",
                    "Check branch name spelling",
                    "Create the branch if it doesn't exist",
                ],
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listCommits",
                "description": "List comprehensive commit information including stats, file changes, verification status, and relationships to pull requests and issues, with pagination support.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "branch": {"type": "string", "description": "Branch name"},
                        "page": {
                            "type": "integer",
                            "description": "Page number for pagination (defaults to 1)",
                            "default": 1,
                        },
                        "per_page": {
                            "type": "integer",
                            "description": "Number of commits per page (defaults to 30)",
                            "default": 30,
                        },
                    },
                    "required": ["owner", "repo", "branch"],
                },
            },
        }
