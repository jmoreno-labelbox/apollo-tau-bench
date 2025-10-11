# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOrUpdateFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, path: str, message: str, content: str, branch: str) -> str:
        """Create/update a file on a branch."""
        repositories = list(data.get("repositories", {}).values())
        commits = list(data.get("commits", {}).values())

        # Locate the repository.
        target_repo = None
        for repository in repositories:
            if repository["owner"] == owner and repository["repo_name"] == repo:
                target_repo = repository
                break

        if not target_repo:
            return json.dumps({"error": f"Repository {owner}/{repo} not found"}, indent=2)

        # Locate the index of the branch.
        try:
            branch_idx = target_repo["branches"].index(branch)
        except ValueError:
            return json.dumps({"error": f"Branch {branch} not found in repository"}, indent=2)

        # Modify file in branch
        if path not in target_repo["branch_files"][branch_idx]:
            target_repo["branch_files"][branch_idx].append(path)
            target_repo["branch_contents"][branch_idx].append(content)
        else:
            file_idx = target_repo["branch_files"][branch_idx].index(path)
            target_repo["branch_contents"][branch_idx][file_idx] = content

        # Generate commit message
        commit_sha = f"commit_{len(commits) + 1}_{path.replace('/', '_')}"

        # Append to commit records.
        repo_commits = None
        for commit_entry in commits:
            if commit_entry["owner"] == owner and commit_entry["repo_name"] == repo:
                repo_commits = commit_entry
                break

        if not repo_commits:
            repo_commits = {
                "owner": owner,
                "repo_name": repo,
                "branch_names": [branch],
                "commit_shas": [[commit_sha]],
                "commit_messages": [[message]],
                "commit_authors": [[owner]],
                "commit_timestamps": [["2023-12-05T12:00:00Z"]]
            }
            commits.append(repo_commits)
        else:
            try:
                branch_idx_commits = repo_commits["branch_names"].index(branch)
                repo_commits["commit_shas"][branch_idx_commits].append(commit_sha)
                repo_commits["commit_messages"][branch_idx_commits].append(message)
                repo_commits["commit_authors"][branch_idx_commits].append(owner)
                repo_commits["commit_timestamps"][branch_idx_commits].append("2023-12-05T12:00:00Z")
            except ValueError:
                repo_commits["branch_names"].append(branch)
                repo_commits["commit_shas"].append([commit_sha])
                repo_commits["commit_messages"].append([message])
                repo_commits["commit_authors"].append([owner])
                repo_commits["commit_timestamps"].append(["2023-12-05T12:00:00Z"])

        return json.dumps({"commit_sha": commit_sha}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_or_update_file",
                "description": "Create/update a file on a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "path": {"type": "string", "description": "File path"},
                        "message": {"type": "string", "description": "Commit message"},
                        "content": {"type": "string", "description": "File content"},
                        "branch": {"type": "string", "description": "Branch name"}
                    },
                    "required": ["owner", "repo", "path", "message", "content", "branch"]
                }
            }
        }
