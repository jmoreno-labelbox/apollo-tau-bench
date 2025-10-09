from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateOrUpdateFile(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str,
        repo: str,
        path: str,
        message: str,
        content: str,
        branch: str,
    ) -> str:
        """Create/update a file on a branch."""
        pass
        repositories = data.get("repositories", [])
        commits = data.get("commits", [])

        #Identify the repository
        target_repo = None
        for repository in repositories:
            if repository["owner"] == owner and repository["repo_name"] == repo:
                target_repo = repository
                break

        if not target_repo:
            payload = {"error": f"Repository {owner}/{repo} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #Determine the index of the branch
        try:
            branch_idx = target_repo["branches"].index(branch)
        except ValueError:
            payload = {"error": f"Branch {branch} not found in repository"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #Modify file within the branch
        if path not in target_repo["branch_files"][branch_idx]:
            target_repo["branch_files"][branch_idx].append(path)
            target_repo["branch_contents"][branch_idx].append(content)
        else:
            file_idx = target_repo["branch_files"][branch_idx].index(path)
            target_repo["branch_contents"][branch_idx][file_idx] = content

        #Generate a commit entry
        commit_sha = f"commit_{len(commits) + 1}_{path.replace('/', '_')}"

        #Append to commit data
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
                "commit_timestamps": [["2023-12-05T12:00:00Z"]],
            }
            commits.append(repo_commits)
        else:
            try:
                branch_idx_commits = repo_commits["branch_names"].index(branch)
                repo_commits["commit_shas"][branch_idx_commits].append(commit_sha)
                repo_commits["commit_messages"][branch_idx_commits].append(message)
                repo_commits["commit_authors"][branch_idx_commits].append(owner)
                repo_commits["commit_timestamps"][branch_idx_commits].append(
                    "2023-12-05T12:00:00Z"
                )
            except ValueError:
                repo_commits["branch_names"].append(branch)
                repo_commits["commit_shas"].append([commit_sha])
                repo_commits["commit_messages"].append([message])
                repo_commits["commit_authors"].append([owner])
                repo_commits["commit_timestamps"].append(["2023-12-05T12:00:00Z"])
        payload = {"commit_sha": commit_sha}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOrUpdateFile",
                "description": "Create/update a file on a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "path": {"type": "string", "description": "File path"},
                        "message": {"type": "string", "description": "Commit message"},
                        "content": {"type": "string", "description": "File content"},
                        "branch": {"type": "string", "description": "Branch name"},
                    },
                    "required": [
                        "owner",
                        "repo",
                        "path",
                        "message",
                        "content",
                        "branch",
                    ],
                },
            },
        }
