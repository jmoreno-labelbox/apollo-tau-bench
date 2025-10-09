from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetFileContents(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], owner: str, repo: str, path: str, branch: str = "main"
    ) -> str:
        """Read comprehensive file information including content, metadata, relationships, and statistics."""
        pass
        repositories = data.get("repositories", [])
        commits_data = data.get("commits", [])

        #Identify the repository
        target_repo = None
        for repository in repositories:
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
                        "Use search_repositories tool to find available repositories",
                    ],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Determine the branch index
        try:
            branch_idx = target_repo["branches"].index(branch)
        except ValueError:
            payload = {
                    "success": False,
                    "error": f"Branch {branch} not found in repository {owner}/{repo}",
                    "error_code": "BRANCH_NOT_FOUND",
                    "metadata": {
                        "repository": f"{owner}/{repo}",
                        "requested_branch": branch,
                        "available_branches": target_repo["branches"],
                        "search_timestamp": "2023-12-05T12:00:00Z",
                    },
                    "suggestions": [
                        f"Use one of the available branches: {target_repo['branches']}",
                        "Check branch name spelling",
                        "Create the branch if it doesn't exist",
                    ],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Verify if the file is present in the branch
        if path not in target_repo["branch_files"][branch_idx]:
            payload = {
                    "success": False,
                    "error": f"File {path} not found in branch {branch}",
                    "error_code": "FILE_NOT_FOUND",
                    "metadata": {
                        "repository": f"{owner}/{repo}",
                        "branch": branch,
                        "requested_path": path,
                        "available_files": target_repo["branch_files"][branch_idx][
                            :10
                        ],  #The initial 10 files
                        "search_timestamp": "2023-12-05T12:00:00Z",
                    },
                    "suggestions": [
                        "Check file path spelling and case sensitivity",
                        "Verify file exists in the specified branch",
                        "Create the file if it should exist",
                    ],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Retrieve content and metadata of the file
        file_idx = target_repo["branch_files"][branch_idx].index(path)
        content = target_repo["branch_contents"][branch_idx][file_idx]

        #Compute statistics for the file
        lines = content.split("\n")
        lines_count = len(lines)
        lines_of_code = len(
            [
                line
                for line in lines
                if line.strip() and not line.strip().startswith("#")
            ]
        )
        comments = len([line for line in lines if line.strip().startswith("#")])
        blank_lines = len([line for line in lines if not line.strip()])

        #Identify the file type and its language
        file_extension = path.split(".")[-1] if "." in path else ""
        language_map = {
            "py": "python",
            "js": "javascript",
            "ts": "typescript",
            "java": "java",
            "cpp": "cpp",
            "c": "c",
            "go": "go",
            "rs": "rust",
            "rb": "ruby",
            "php": "php",
            "md": "markdown",
            "txt": "text",
            "json": "json",
            "yml": "yaml",
            "yaml": "yaml",
            "xml": "xml",
            "html": "html",
        }
        language = language_map.get(file_extension.lower(), "text")

        #Locate related files (in the same directory, with similar extensions)
        directory = "/".join(path.split("/")[:-1]) if "/" in path else ""
        related_files = [
            file_path
            for file_path in target_repo["branch_files"][branch_idx]
            if file_path != path
            and (
                file_path.startswith(directory)
                or file_path.endswith(f".{file_extension}")
            )
        ][
            :5
        ]  #Restrict to 5 related files

        #Identify imports and dependencies (basic analysis)
        imports = []
        imported_by = []
        if language == "python":
            imports = [
                line.strip()
                for line in lines
                if line.strip().startswith(("import ", "from "))
            ]
        elif language in ["javascript", "typescript"]:
            imports = [
                line.strip()
                for line in lines
                if "import " in line or "require(" in line
            ]

        #Simulate commit information (retrieve the latest commit for this file)
        last_commit_sha = f"commit_latest_{path.replace('/', '_')}"
        last_commit_message = f"Update {path.split('/')[-1]}"
        last_author = owner

        #Locate commits that altered this file
        for commit_entry in commits_data:
            if commit_entry["owner"] == owner and commit_entry["repo_name"] == repo:
                for branch_messages in commit_entry.get("commit_messages", []):
                    for j, message in enumerate(branch_messages):
                        if path.split("/")[-1] in message:
                            branch_commit_idx = commit_entry["commit_messages"].index(
                                branch_messages
                            )
                            if j < len(commit_entry["commit_shas"][branch_commit_idx]):
                                last_commit_sha = commit_entry["commit_shas"][
                                    branch_commit_idx
                                ][j]
                                last_commit_message = message
                                last_author = commit_entry.get(
                                    "commit_authors", [[owner]]
                                )[branch_commit_idx][j]
                                break

        result = {
            "success": True,
            "data": {
                "content": content,
                "encoding": "utf-8",
                "size": len(content.encode("utf-8")),
                "sha": f"file_{hash(content) % 1000000:06d}",
                "download_url": f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}",
            },
            "metadata": {
                "path": path,
                "type": "file",
                "language": language,
                "last_modified": "2023-12-05T12:00:00Z",
                "last_commit_sha": last_commit_sha,
                "last_commit_message": last_commit_message,
                "last_author": last_author,
            },
            "relationships": {
                "repository": f"{owner}/{repo}",
                "branch": branch,
                "directory": directory,
                "related_files": related_files,
                "imports": imports[:10],  #Restrict to 10 imports
                "imported_by": imported_by[:5],  #Restrict to 5 files that reference this
            },
            "counts": {
                "lines": lines_count,
                "lines_of_code": lines_of_code,
                "comments": comments,
                "blank_lines": blank_lines,
            },
        }
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFileContents",
                "description": "Read comprehensive file information including content, metadata, statistics, relationships to other files, and commit history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "path": {"type": "string", "description": "File path"},
                        "branch": {
                            "type": "string",
                            "description": "Branch name (defaults to 'main')",
                            "default": "main",
                        },
                    },
                    "required": ["owner", "repo", "path"],
                },
            },
        }
