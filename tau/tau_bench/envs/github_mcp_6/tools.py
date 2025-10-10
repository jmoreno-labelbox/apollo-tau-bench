import json
from typing import Any, Dict, List
from domains.dto import Tool


class GetMe(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], username: str = None, auth_key: str = None, instruction: str = None) -> str:
        """Authenticate user by validating username and AUTH_KEY, return comprehensive user information."""
        import re
        auth_users = data.get("authentication", [])
        repositories = data.get("repositories", [])

        if not auth_users:
            return json.dumps({
                "success": False,
                "error": "No authentication data available",
                "error_code": "AUTH_DATA_NOT_FOUND",
                "metadata": {
                    "authentication_method": "unknown",
                    "session_expires": None,
                    "last_login": None
                },
                "suggestions": ["Ensure authentication data is loaded", "Check system configuration"]
            }, indent=2)

        # Extract auth_key from instruction if provided
        if instruction and not auth_key:
            # Look for pattern: "auth_key is xxx (owner: yyy)"
            auth_key_match = re.search(r'auth_key is ([a-zA-Z0-9_]+) \(owner: ([^)]+)\)', instruction)
            if auth_key_match:
                auth_key = auth_key_match.group(1)
                if not username:
                    username = auth_key_match.group(2)

        # Determine authentication method and find user
        user = None
        auth_method = "default"

        if username and auth_key:
            # Full authentication: validate both username and auth_key match
            auth_method = "username_and_key"
            for auth_user in auth_users:
                if auth_user.get("username") == username and auth_user.get("auth_key") == auth_key:
                    user = auth_user
                    break

            if not user:
                return json.dumps({
                    "success": False,
                    "error": "Authentication failed: username and auth_key combination invalid",
                    "error_code": "AUTH_MISMATCH",
                    "metadata": {
                        "provided_username": username,
                        "provided_key": auth_key[:10] + "..." if auth_key else None,
                        "authentication_method": "username_and_key",
                        "session_expires": None,
                        "last_login": None
                    },
                    "suggestions": [
                        "Verify both username and AUTH_KEY are correct",
                        "Check that the username matches the token owner",
                        "Ensure you're using valid GitHub credentials"
                    ]
                }, indent=2)

        elif auth_key and not username:
            # Auth key only: find user by matching AUTH_KEY
            auth_method = "auth_key_only"
            for auth_user in auth_users:
                if auth_user.get("auth_key") == auth_key:
                    user = auth_user
                    break

            if not user:
                return json.dumps({
                    "success": False,
                    "error": "Invalid authentication key",
                    "error_code": "INVALID_AUTH_KEY",
                    "metadata": {
                        "provided_key": auth_key[:10] + "..." if auth_key else None,
                        "authentication_method": "auth_key_only",
                        "session_expires": None,
                        "last_login": None
                    },
                    "suggestions": [
                        "Verify the AUTH_KEY is correct",
                        "Check that the token hasn't expired",
                        "Ensure you're using a valid GitHub token"
                    ]
                }, indent=2)

        elif username and not auth_key:
            # Username only: find user by username (less secure)
            auth_method = "username_only"
            for auth_user in auth_users:
                if auth_user.get("username") == username:
                    user = auth_user
                    break

            if not user:
                return json.dumps({
                    "success": False,
                    "error": "Username not found",
                    "error_code": "USERNAME_NOT_FOUND",
                    "metadata": {
                        "provided_username": username,
                        "authentication_method": "username_only",
                        "session_expires": None,
                        "last_login": None
                    },
                    "suggestions": [
                        "Verify the username is correct",
                        "Check available usernames in the system",
                        "Consider using auth_key for better security"
                    ]
                }, indent=2)
        else:
            # No parameters provided: use first user (backward compatibility)
            auth_method = "default"
            user = auth_users[0]

        final_username = user["username"]

        # Calculate repository statistics
        owned_repos = [repo for repo in repositories if repo["owner"] == final_username]
        total_owned = len(owned_repos)

        # Get organization memberships (users with shared email domains)
        user_domain = user["email"].split("@")[1]
        organizations = list(set([
            auth_user["email"].split("@")[1]
            for auth_user in auth_users
            if auth_user["email"].split("@")[1] == user_domain and auth_user["username"] != final_username
        ]))

        # Mock additional user data based on username patterns
        display_name = final_username.replace("-", " ").title()
        avatar_url = f"https://avatars.githubusercontent.com/{final_username}"
        member_since = "2023-01-15T09:30:00Z"
        two_factor_enabled = "team" in final_username or "lead" in final_username

        # Enhanced response with authentication validation
        result = {
            "success": True,
            "authenticated": True,
            "data": {
                "username": final_username,
                "email": user["email"],
                "auth_key": user["auth_key"],
                "display_name": display_name,
                "avatar_url": avatar_url,
                "permissions": ["read", "write", "admin"] if "lead" in final_username or "manager" in final_username else ["read", "write"],
                "member_since": member_since,
                "two_factor_enabled": two_factor_enabled
            },
            "metadata": {
                "authentication_method": "token",
                "authenticated_at": "2023-12-05T10:00:00Z",
                "session_expires": "2024-12-31T23:59:59Z",
                "last_login": "2023-12-05T10:00:00Z",
                "auth_validation": auth_method
            },
            "relationships": {
                "organizations": organizations,
                "repositories_count": len([repo for repo in repositories if final_username in [repo["owner"]] or final_username in str(repo)]),
                "owned_repositories_count": total_owned
            },
            "authentication_details": {
                "username_verified": username is not None,
                "email_verified": True,
                "auth_key_verified": auth_key is not None,
                "authentication_source": auth_method,
                "security_level": "high" if auth_method == "username_and_key" else "medium" if auth_method in ["auth_key_only", "username_only"] else "low"
            }
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_me",
                "description": "Authenticate user by validating username and AUTH_KEY, return comprehensive user information including profile data, permissions, repository relationships, and organizational memberships. Can extract auth_key from instruction if provided.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string", "description": "GitHub username for user identification (optional)"},
                        "auth_key": {"type": "string", "description": "GitHub authentication token/key for validation (optional)"},
                        "instruction": {"type": "string", "description": "Task instruction that may contain auth_key information in format 'auth_key is xxx (owner: yyy)' (optional)"}
                    },
                    "required": []
                }
            }
        }


class SearchRepositories(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], query: str) -> str:
        """Search repositories by query string (exact-match permitted)."""
        repositories = data.get("repositories", [])
        matching_repos = []

        for repo in repositories:
            if query.lower() in repo["repo_name"].lower():
                matching_repos.append(repo["repo_name"])

        return json.dumps({"repo_names": matching_repos}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_repositories",
                "description": "Search repositories by query string (exact-match permitted).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Search query string"}
                    },
                    "required": ["query"]
                }
            }
        }


class GetRepository(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str) -> str:
        """Get detailed information about a specific repository."""
        repositories = data.get("repositories", [])

        # Find the repository
        target_repo = None
        for repository in repositories:
            repo_name = repository.get("repo_name") or repository.get("name")
            if repository.get("owner") == owner and repo_name == repo:
                target_repo = repository
                break

        if not target_repo:
            return json.dumps({
                "success": False,
                "error": f"Repository '{owner}/{repo}' not found",
                "error_code": "REPO_NOT_FOUND",
                "metadata": {
                    "searched_owner": owner,
                    "searched_repo": repo,
                    "available_repos": [f"{r.get('owner')}/{r.get('repo_name') or r.get('name')}" for r in repositories]
                }
            }, indent=2)

        return json.dumps({
            "success": True,
            "repository": {
                "name": target_repo.get("repo_name"),
                "owner": target_repo.get("owner"),
                "description": target_repo.get("description"),
                "private": target_repo.get("private", False),
                "default_branch": target_repo.get("default_branch", "main"),
                "created_at": target_repo.get("created_at"),
                "updated_at": target_repo.get("updated_at"),
                "language": target_repo.get("language"),
                "topics": target_repo.get("topics", []),
                "open_issues_count": target_repo.get("open_issues_count", 0),
                "forks_count": target_repo.get("forks_count", 0),
                "stars_count": target_repo.get("stars_count", 0)
            },
            "metadata": {
                "verification_method": "direct_repository_lookup",
                "repository_id": f"{owner}/{repo}"
            }
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repository",
                "description": "Get detailed information about a specific repository",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "Repository owner (username or organization)"
                        },
                        "repo": {
                            "type": "string",
                            "description": "Repository name"
                        }
                    },
                    "required": ["owner", "repo"]
                }
            }
        }


class CreateRepository(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: str, description: str, private: bool, autoInit: bool) -> str:
        """Create a repository with metadata."""
        repositories = data.get("repositories", [])

        # Check if repository name exists
        existing_names = [repo["repo_name"] for repo in repositories]
        repo_name = name
        if name in existing_names:
            repo_name = f"{name}_v2"

        # Get authenticated user
        auth_users = data.get("authentication", [])
        username = auth_users[0]["username"] if auth_users else "default_user"

        # Create new repository entry
        new_repo = {
            "owner": username,
            "repo_name": repo_name,
            "description": description,
            "private": private,
            "default_branch": "main",
            "file_paths": ["README.md"] if autoInit else [],
            "file_contents": [f"# {repo_name}\n\nAutomatically created repository."] if autoInit else [],
            "branches": ["main"],
            "branch_files": [["README.md"]] if autoInit else [[]],
            "branch_contents": [[f"# {repo_name}\n\nAutomatically created repository."]] if autoInit else [[]],
            "branch_shas": [f"repo_{len(repositories) + 1}_init_sha"],
            "created_at": "2023-12-05T12:00:00Z",
            "updated_at": "2023-12-05T12:00:00Z"
        }

        repositories.append(new_repo)

        return json.dumps({
            "name": repo_name,
            "default_branch": "main"
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_repository",
                "description": "Create a repository with metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Repository name"},
                        "description": {"type": "string", "description": "Repository description"},
                        "private": {"type": "boolean", "description": "Whether repository is private"},
                        "autoInit": {"type": "boolean", "description": "Auto-initialize with README"}
                    },
                    "required": ["name", "description", "private", "autoInit"]
                }
            }
        }


class CreateOrUpdateFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, path: str, message: str, content: str, branch: str) -> str:
        """Create/update a file on a branch."""
        repositories = data.get("repositories", [])
        commits = data.get("commits", [])

        # Find the repository
        target_repo = None
        for repository in repositories:
            if repository["owner"] == owner and repository["repo_name"] == repo:
                target_repo = repository
                break

        if not target_repo:
            return json.dumps({"error": f"Repository {owner}/{repo} not found"}, indent=2)

        # Find branch index
        try:
            branch_idx = target_repo["branches"].index(branch)
        except ValueError:
            return json.dumps({"error": f"Branch {branch} not found in repository"}, indent=2)

        # Update file in branch
        if path not in target_repo["branch_files"][branch_idx]:
            target_repo["branch_files"][branch_idx].append(path)
            target_repo["branch_contents"][branch_idx].append(content)
        else:
            file_idx = target_repo["branch_files"][branch_idx].index(path)
            target_repo["branch_contents"][branch_idx][file_idx] = content

        # Create commit entry
        commit_sha = f"commit_{len(commits) + 1}_{path.replace('/', '_')}"

        # Add to commits data
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


class GetFileContents(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, path: str, branch: str = "main") -> str:
        """Read comprehensive file information including content, metadata, relationships, and statistics."""
        repositories = data.get("repositories", [])
        commits_data = data.get("commits", [])

        # Find the repository
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
                    "Check repository owner and name spelling",
                    "Use search_repositories tool to find available repositories"
                ]
            }, indent=2)

        # Find branch index
        try:
            branch_idx = target_repo["branches"].index(branch)
        except ValueError:
            return json.dumps({
                "success": False,
                "error": f"Branch {branch} not found in repository {owner}/{repo}",
                "error_code": "BRANCH_NOT_FOUND",
                "metadata": {
                    "repository": f"{owner}/{repo}",
                    "requested_branch": branch,
                    "available_branches": target_repo["branches"],
                    "search_timestamp": "2023-12-05T12:00:00Z"
                },
                "suggestions": [
                    f"Use one of the available branches: {target_repo['branches']}",
                    "Check branch name spelling",
                    "Create the branch if it doesn't exist"
                ]
            }, indent=2)

        # Check if file exists in branch
        if path not in target_repo["branch_files"][branch_idx]:
            return json.dumps({
                "success": False,
                "error": f"File {path} not found in branch {branch}",
                "error_code": "FILE_NOT_FOUND",
                "metadata": {
                    "repository": f"{owner}/{repo}",
                    "branch": branch,
                    "requested_path": path,
                    "available_files": target_repo["branch_files"][branch_idx][:10],  # First 10 files
                    "search_timestamp": "2023-12-05T12:00:00Z"
                },
                "suggestions": [
                    "Check file path spelling and case sensitivity",
                    "Verify file exists in the specified branch",
                    "Create the file if it should exist"
                ]
            }, indent=2)

        # Get file content and metadata
        file_idx = target_repo["branch_files"][branch_idx].index(path)
        content = target_repo["branch_contents"][branch_idx][file_idx]

        # Calculate file statistics
        lines = content.split('\n')
        lines_count = len(lines)
        lines_of_code = len([line for line in lines if line.strip() and not line.strip().startswith('#')])
        comments = len([line for line in lines if line.strip().startswith('#')])
        blank_lines = len([line for line in lines if not line.strip()])

        # Determine file type and language
        file_extension = path.split('.')[-1] if '.' in path else ''
        language_map = {
            'py': 'python', 'js': 'javascript', 'ts': 'typescript', 'java': 'java',
            'cpp': 'cpp', 'c': 'c', 'go': 'go', 'rs': 'rust', 'rb': 'ruby',
            'php': 'php', 'md': 'markdown', 'txt': 'text', 'json': 'json',
            'yml': 'yaml', 'yaml': 'yaml', 'xml': 'xml', 'html': 'html'
        }
        language = language_map.get(file_extension.lower(), 'text')

        # Find related files (same directory, similar extensions)
        directory = '/'.join(path.split('/')[:-1]) if '/' in path else ''
        related_files = [
            file_path for file_path in target_repo["branch_files"][branch_idx]
            if file_path != path and (
                file_path.startswith(directory) or
                file_path.endswith(f'.{file_extension}')
            )
        ][:5]  # Limit to 5 related files

        # Find imports and dependencies (basic parsing)
        imports = []
        imported_by = []
        if language == 'python':
            imports = [line.strip() for line in lines if line.strip().startswith(('import ', 'from '))]
        elif language in ['javascript', 'typescript']:
            imports = [line.strip() for line in lines if 'import ' in line or 'require(' in line]

        # Mock commit information (find latest commit for this file)
        last_commit_sha = f"commit_latest_{path.replace('/', '_')}"
        last_commit_message = f"Update {path.split('/')[-1]}"
        last_author = owner

        # Find commits that modified this file
        for commit_entry in commits_data:
            if commit_entry["owner"] == owner and commit_entry["repo_name"] == repo:
                for branch_messages in commit_entry.get("commit_messages", []):
                    for j, message in enumerate(branch_messages):
                        if path.split('/')[-1] in message:
                            branch_commit_idx = commit_entry["commit_messages"].index(branch_messages)
                            if j < len(commit_entry["commit_shas"][branch_commit_idx]):
                                last_commit_sha = commit_entry["commit_shas"][branch_commit_idx][j]
                                last_commit_message = message
                                last_author = commit_entry.get("commit_authors", [[owner]])[branch_commit_idx][j]
                                break

        result = {
            "success": True,
            "data": {
                "content": content,
                "encoding": "utf-8",
                "size": len(content.encode('utf-8')),
                "sha": f"file_{hash(content) % 1000000:06d}",
                "download_url": f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}"
            },
            "metadata": {
                "path": path,
                "type": "file",
                "language": language,
                "last_modified": "2023-12-05T12:00:00Z",
                "last_commit_sha": last_commit_sha,
                "last_commit_message": last_commit_message,
                "last_author": last_author
            },
            "relationships": {
                "repository": f"{owner}/{repo}",
                "branch": branch,
                "directory": directory,
                "related_files": related_files,
                "imports": imports[:10],  # Limit to 10 imports
                "imported_by": imported_by[:5]  # Limit to 5 files that import this
            },
            "counts": {
                "lines": lines_count,
                "lines_of_code": lines_of_code,
                "comments": comments,
                "blank_lines": blank_lines
            }
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_file_contents",
                "description": "Read comprehensive file information including content, metadata, statistics, relationships to other files, and commit history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "path": {"type": "string", "description": "File path"},
                        "branch": {"type": "string", "description": "Branch name (defaults to 'main')", "default": "main"}
                    },
                    "required": ["owner", "repo", "path"]
                }
            }
        }


class ListCommits(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, branch: str, page: int = 1, per_page: int = 30) -> str:
        """List comprehensive commit information with metadata, relationships, and statistics."""
        commits = data.get("commits", [])
        repositories = data.get("repositories", [])
        pull_requests_data = data.get("pull_requests", [])
        issues_data = data.get("issues", [])

        # Find repository to validate it exists
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

        # Find commits for the repository and branch
        for commit_entry in commits:
            if commit_entry["owner"] == owner and commit_entry["repo_name"] == repo:
                try:
                    branch_idx = commit_entry["branch_names"].index(branch)
                    all_commits = []

                    # Build comprehensive commit information
                    for i, sha in enumerate(commit_entry["commit_shas"][branch_idx]):
                        message = commit_entry["commit_messages"][branch_idx][i]
                        author = commit_entry["commit_authors"][branch_idx][i]
                        timestamp = commit_entry["commit_timestamps"][branch_idx][i]

                        # Mock additional commit data
                        tree_sha = f"tree_{sha[-8:]}"
                        parent_shas = [f"parent_{i-1}_{sha[-6:]}"] if i > 0 else []

                        # Calculate stats (mock based on message)
                        is_merge = "merge" in message.lower()
                        additions = 50 if not is_merge else 100
                        deletions = 10 if not is_merge else 20

                        # Find affected files (mock based on file patterns in message)
                        files_changed = []
                        for file_path in target_repo.get("file_paths", []):
                            filename = file_path.split('/')[-1]
                            if filename.lower() in message.lower() or file_path.split('.')[-1] in message.lower():
                                files_changed.append(file_path)

                        if not files_changed and not is_merge:
                            # Default to some common files if no specific matches
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
                                "total": additions + deletions
                            },
                            "files_changed": files_changed,
                            "verification": {
                                "verified": "bot" not in author.lower(),
                                "reason": "valid" if "bot" not in author.lower() else "unsigned"
                            }
                        }
                        all_commits.append(commit_data)

                    # Apply pagination
                    start_idx = (page - 1) * per_page
                    end_idx = start_idx + per_page
                    paginated_commits = all_commits[start_idx:end_idx]

                    # Find related pull requests and issues
                    related_prs = []
                    related_issues = []

                    for pr_entry in pull_requests_data:
                        if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                            for i, pr_title in enumerate(pr_entry.get("pr_titles", [])):
                                if any(sha[:8] in pr_title for sha in [c["sha"] for c in all_commits]):
                                    related_prs.append(pr_entry["pr_numbers"][i])

                    for issue_entry in issues_data:
                        if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                            for i, issue_title in enumerate(issue_entry.get("issue_titles", [])):
                                if any(word in " ".join([c["message"] for c in all_commits]) for word in issue_title.lower().split() if len(word) > 3):
                                    related_issues.append(issue_entry["issue_numbers"][i])

                    # Calculate statistics
                    unique_authors = list(set([c["author"] for c in all_commits]))
                    merge_commits = [c for c in all_commits if "merge" in c["message"].lower()]
                    files_touched = list(set([f for c in all_commits for f in c["files_changed"]]))

                    # Find tags (mock some version tags)
                    tags = []
                    if len(all_commits) > 10:
                        tags = [f"v1.{len(all_commits) // 10}.0"]

                    result = {
                        "success": True,
                        "data": {
                            "commits": paginated_commits
                        },
                        "metadata": {
                            "branch": branch,
                            "total_commits": len(all_commits),
                            "date_range": {
                                "earliest": all_commits[-1]["timestamp"] if all_commits else None,
                                "latest": all_commits[0]["timestamp"] if all_commits else None
                            },
                            "pagination": {
                                "page": page,
                                "per_page": per_page,
                                "has_more": end_idx < len(all_commits)
                            }
                        },
                        "relationships": {
                            "repository": f"{owner}/{repo}",
                            "pull_requests": related_prs[:5],
                            "issues": related_issues[:5],
                            "tags": tags
                        },
                        "counts": {
                            "total_commits": len(all_commits),
                            "unique_authors": len(unique_authors),
                            "merge_commits": len(merge_commits),
                            "files_touched": len(files_touched)
                        }
                    }

                    return json.dumps(result, indent=2)
                except ValueError:
                    pass

        # Branch not found
        return json.dumps({
            "success": False,
            "error": f"Branch {branch} not found in repository {owner}/{repo}",
            "error_code": "BRANCH_NOT_FOUND",
            "metadata": {
                "repository": f"{owner}/{repo}",
                "requested_branch": branch,
                "available_branches": target_repo.get("branches", []),
                "search_timestamp": "2023-12-05T12:00:00Z"
            },
            "suggestions": [
                f"Use one of the available branches: {target_repo.get('branches', [])}",
                "Check branch name spelling",
                "Create the branch if it doesn't exist"
            ]
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_commits",
                "description": "List comprehensive commit information including stats, file changes, verification status, and relationships to pull requests and issues, with pagination support.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "branch": {"type": "string", "description": "Branch name"},
                        "page": {"type": "integer", "description": "Page number for pagination (defaults to 1)", "default": 1},
                        "per_page": {"type": "integer", "description": "Number of commits per page (defaults to 30)", "default": 30}
                    },
                    "required": ["owner", "repo", "branch"]
                }
            }
        }


class SearchCode(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], query: str, language: str = None, repo_filter: str = None, page: int = 1, per_page: int = 30) -> str:
        """Search code patterns with comprehensive results, metadata, and filtering capabilities."""
        import time
        import re

        start_time = time.time()
        repositories = data.get("repositories", [])
        all_matches = []

        if not query.strip():
            return json.dumps({
                "success": False,
                "error": "Search query cannot be empty",
                "error_code": "EMPTY_QUERY",
                "metadata": {
                    "search_timestamp": "2023-12-05T12:00:00Z"
                },
                "suggestions": [
                    "Provide a non-empty search query",
                    "Use specific keywords or patterns to search for"
                ]
            }, indent=2)

        # File extension to language mapping
        language_map = {
            'py': 'python', 'js': 'javascript', 'ts': 'typescript', 'java': 'java',
            'cpp': 'cpp', 'c': 'c', 'go': 'go', 'rs': 'rust', 'rb': 'ruby',
            'php': 'php', 'md': 'markdown', 'txt': 'text', 'json': 'json',
            'yml': 'yaml', 'yaml': 'yaml', 'xml': 'xml', 'html': 'html'
        }

        repositories_searched = []
        file_types_found = set()
        by_language = {}
        by_repository = {}

        for repo in repositories:
            repo_name = f"{repo['owner']}/{repo['repo_name']}"
            repositories_searched.append(repo_name)

            # Apply repository filter if specified
            if repo_filter and repo_filter.lower() not in repo_name.lower():
                continue

            repo_matches = 0

            for branch_idx, files in enumerate(repo["branch_files"]):
                branch_name = repo.get("branches", ["main"])[branch_idx] if branch_idx < len(repo.get("branches", [])) else "main"

                for file_idx, file_path in enumerate(files):
                    content = repo["branch_contents"][branch_idx][file_idx]

                    # Determine file language
                    file_extension = file_path.split('.')[-1].lower() if '.' in file_path else 'txt'
                    file_language = language_map.get(file_extension, 'text')
                    file_types_found.add(file_language)

                    # Apply language filter if specified
                    if language and language.lower() != file_language.lower():
                        continue

                    # Search for matches (case-insensitive)
                    lines = content.split('\n')
                    for line_num, line in enumerate(lines, 1):
                        if query.lower() in line.lower():
                            # Find the exact match position and context
                            match_start = line.lower().find(query.lower())
                            matched_text = line[match_start:match_start + len(query)]

                            # Get context before and after
                            context_before = ""
                            context_after = ""
                            if line_num > 1:
                                context_before = lines[line_num - 2].strip()
                            if line_num < len(lines):
                                context_after = lines[line_num].strip() if line_num < len(lines) else ""

                            # Calculate relevance score based on multiple factors
                            score = 1.0
                            if query.lower() in file_path.lower():
                                score += 0.5  # Filename match bonus
                            if line.strip().startswith(query):
                                score += 0.3  # Start of line bonus
                            if file_language in ['python', 'javascript', 'java']:
                                score += 0.2  # Popular language bonus

                            match = {
                                "repository": repo_name,
                                "path": file_path,
                                "filename": file_path.split('/')[-1],
                                "language": file_language,
                                "score": round(score, 2),
                                "excerpt": line.strip(),
                                "line_number": line_num,
                                "matched_text": matched_text,
                                "context_before": context_before,
                                "context_after": context_after,
                                "sha": f"file_{hash(content) % 1000000:06d}"
                            }
                            all_matches.append(match)
                            repo_matches += 1

            # Update repository statistics
            if repo_matches > 0:
                by_repository[repo_name] = repo_matches

        # Update language statistics
        for match in all_matches:
            lang = match["language"]
            by_language[lang] = by_language.get(lang, 0) + 1

        # Sort matches by score (descending)
        all_matches.sort(key=lambda x: x["score"], reverse=True)

        # Apply pagination
        total_matches = len(all_matches)
        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        paginated_matches = all_matches[start_idx:end_idx]

        # Calculate search time
        search_time_ms = int((time.time() - start_time) * 1000)

        # Generate related query suggestions
        related_queries = []
        if query.lower() in ['function', 'def', 'class']:
            related_queries = [f"{query} name", f"{query} definition", f"public {query}"]
        elif len(query.split()) == 1:
            related_queries = [f"{query} implementation", f"{query} usage", f"import {query}"]
        else:
            words = query.split()
            if len(words) > 1:
                related_queries = [words[0], words[-1], " ".join(words[:-1])]

        # Filter applied information
        filters_applied = {
            "language": language,
            "repository": repo_filter,
            "case_sensitive": False
        }

        result = {
            "success": True,
            "data": {
                "matches": paginated_matches
            },
            "metadata": {
                "query": query,
                "total_results": total_matches,
                "search_time_ms": search_time_ms,
                "filters_applied": filters_applied,
                "pagination": {
                    "page": page,
                    "per_page": per_page,
                    "has_more": end_idx < total_matches
                }
            },
            "relationships": {
                "repositories_searched": repositories_searched,
                "file_types_found": list(file_types_found),
                "related_queries": related_queries[:3]  # Limit to 3 suggestions
            },
            "counts": {
                "total_matches": total_matches,
                "repositories_with_matches": len(by_repository),
                "unique_files": len(set(match["path"] for match in all_matches)),
                "by_language": by_language,
                "by_repository": by_repository
            }
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_code",
                "description": "Search code patterns with comprehensive results including relevance scoring, language filtering, context extraction, and detailed statistics with pagination support.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Code search query"},
                        "language": {"type": "string", "description": "Filter by programming language (optional)"},
                        "repo_filter": {"type": "string", "description": "Filter by repository name pattern (optional)"},
                        "page": {"type": "integer", "description": "Page number for pagination (defaults to 1)", "default": 1},
                        "per_page": {"type": "integer", "description": "Results per page (defaults to 30)", "default": 30}
                    },
                    "required": ["query"]
                }
            }
        }


class ListCodeScanningAlerts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str) -> str:
        """List code scanning alerts for a repo."""
        alerts_data = data.get("code_scanning_alerts", [])

        for alert_entry in alerts_data:
            if alert_entry["owner"] == owner and alert_entry["repo_name"] == repo:
                alerts = []
                for i, alert_num in enumerate(alert_entry["alert_numbers"]):
                    alerts.append({
                        "number": alert_num,
                        "severity": alert_entry["severities"][i],
                        "state": alert_entry["states"][i],
                        "ref": alert_entry["refs"][i]
                    })
                return json.dumps({"alerts": alerts}, indent=2)

        return json.dumps({"alerts": []}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_code_scanning_alerts",
                "description": "List code scanning alerts for a repo.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"}
                    },
                    "required": ["owner", "repo"]
                }
            }
        }


class CreateBranch(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, branch: str, sha: str = None, base_branch: str = "main") -> str:
        """Create a comprehensive branch with detailed information, relationships, and metadata."""
        repositories = data.get("repositories", [])
        commits_data = data.get("commits", [])
        pull_requests_data = data.get("pull_requests", [])

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


class CreatePullRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, title: str, body: str, head: str, base: str, draft: bool = False) -> str:
        """Create a comprehensive pull request with detailed information, relationships, and status checks."""
        pull_requests = data.get("pull_requests", [])
        repositories = data.get("repositories", [])
        commits_data = data.get("commits", [])
        issues_data = data.get("issues", [])

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

        # Validate branches exist
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

        # Find existing PR entry for this repo
        repo_prs = None
        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                repo_prs = pr_entry
                break

        if not repo_prs:
            # Create new PR entry
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
            # Add to existing PR entry
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

        # Calculate changed files and commits
        head_idx = target_repo["branches"].index(head)
        base_idx = target_repo["branches"].index(base)

        head_files = set(target_repo.get("branch_files", [[]])[head_idx] if head_idx < len(target_repo.get("branch_files", [])) else [])
        base_files = set(target_repo.get("branch_files", [[]])[base_idx] if base_idx < len(target_repo.get("branch_files", [])) else [])

        changed_files = list(head_files.symmetric_difference(base_files))
        additions = len(head_files - base_files) * 20  # Mock 20 lines per new file
        deletions = len(base_files - head_files) * 10   # Mock 10 lines per deleted file

        # Find commits in head branch but not in base
        commits_in_pr = []
        for commit_entry in commits_data:
            if commit_entry["owner"] == owner and commit_entry["repo_name"] == repo:
                if head in commit_entry.get("branch_names", []):
                    head_branch_idx = commit_entry["branch_names"].index(head)
                    commits_in_pr = commit_entry.get("commit_shas", [[]])[head_branch_idx][:5]  # Limit to 5 commits
                    break

        # Find linked issues (parse body for issue references)
        linked_issues = []
        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                for i, issue_number in enumerate(issue_entry.get("issue_numbers", [])):
                    if f"#{issue_number}" in body or f"closes #{issue_number}" in body.lower() or f"fixes #{issue_number}" in body.lower():
                        linked_issues.append(issue_number)

        # Find conflicting PRs (mock based on same base branch)
        conflicts_with = []
        for i, pr_base in enumerate(repo_prs.get("base_branches", [])):
            if pr_base == base and repo_prs["pr_numbers"][i] != pr_number and repo_prs["pr_states"][i] == "open":
                conflicts_with.append(repo_prs["pr_numbers"][i])

        # Mock status checks
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


class GetPullRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, pullNumber: int) -> str:
        """Get PR details by number."""
        pull_requests = data.get("pull_requests", [])

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)
                    result = {
                        "state": pr_entry["pr_states"][pr_idx],
                        "head": pr_entry["head_branches"][pr_idx],
                        "base": pr_entry["base_branches"][pr_idx],
                        "mergeable": pr_entry["mergeable_flags"][pr_idx]
                    }
                    return json.dumps(result, indent=2)
                except ValueError:
                    pass

        return json.dumps({"error": f"Pull request #{pullNumber} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pull_request",
                "description": "Get PR details by number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number"}
                    },
                    "required": ["owner", "repo", "pullNumber"]
                }
            }
        }


class ListPullRequests(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, state: str) -> str:
        """List PRs filtered by state."""
        pull_requests = data.get("pull_requests", [])

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                prs = []
                for i, pr_number in enumerate(pr_entry["pr_numbers"]):
                    pr_state = pr_entry["pr_states"][i]
                    if state == "all" or pr_state == state:
                        prs.append({
                            "number": pr_number,
                            "state": pr_state,
                            "title": pr_entry["pr_titles"][i]
                        })
                return json.dumps({"prs": prs}, indent=2)

        return json.dumps({"prs": []}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_pull_requests",
                "description": "List PRs filtered by state.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "state": {"type": "string", "description": "PR state filter"}
                    },
                    "required": ["owner", "repo", "state"]
                }
            }
        }


class GetPullRequestStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, pullNumber: int) -> str:
        """Get combined status checks for a PR."""
        pull_requests = data.get("pull_requests", [])

        # Find the pull request
        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)
                    pr_state = pr_entry["pr_states"][pr_idx]

                    # Generate realistic status checks based on PR state and title
                    checks = []

                    # Always include CI check
                    if pr_state == "open":
                        checks.append({"context": "continuous-integration", "state": "success"})
                        checks.append({"context": "code-review", "state": "pending"})
                        checks.append({"context": "security-scan", "state": "success"})
                    elif pr_state == "merged":
                        checks.append({"context": "continuous-integration", "state": "success"})
                        checks.append({"context": "code-review", "state": "success"})
                        checks.append({"context": "security-scan", "state": "success"})
                    else:
                        checks.append({"context": "continuous-integration", "state": "failure"})
                        checks.append({"context": "code-review", "state": "pending"})

                    # Add additional checks based on PR title
                    pr_title = pr_entry.get("pr_titles", [""])[pr_idx] if pr_idx < len(pr_entry.get("pr_titles", [])) else ""
                    if "test" in pr_title.lower():
                        checks.append({"context": "unit-tests", "state": "success"})
                    if "security" in pr_title.lower():
                        checks.append({"context": "security-audit", "state": "success"})

                    result = {
                        "state": "success" if all(check["state"] == "success" for check in checks) else "pending",
                        "total_count": len(checks),
                        "statuses": checks
                    }
                    return json.dumps(result, indent=2)
                except ValueError:
                    pass

        # Default response if PR not found
        result = {
            "state": "pending",
            "total_count": 2,
            "statuses": [
                {"context": "continuous-integration", "state": "pending"},
                {"context": "code-review", "state": "pending"}
            ]
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pull_request_status",
                "description": "Get combined status checks for a PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number"}
                    },
                    "required": ["owner", "repo", "pullNumber"]
                }
            }
        }


class CheckPullRequestMergeability(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, pullNumber: int) -> str:
        """Check if a pull request is mergeable by examining its status and review state."""
        pull_requests = data.get("pull_requests", [])

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)

                    # Get PR details
                    pr_state = pr_entry["pr_states"][pr_idx]
                    mergeable = pr_entry["mergeable_flags"][pr_idx]
                    merged = pr_entry["merged_flags"][pr_idx]
                    review_states = pr_entry["review_states"][pr_idx] if pr_idx < len(pr_entry["review_states"]) else []

                    # Check if PR is already merged
                    if merged:
                        return json.dumps({
                            "mergeable": False,
                            "reason": "Pull request is already merged",
                            "state": pr_state,
                            "review_states": review_states
                        }, indent=2)

                    # Check if PR is closed
                    if pr_state == "closed":
                        return json.dumps({
                            "mergeable": False,
                            "reason": "Pull request is closed",
                            "state": pr_state,
                            "review_states": review_states
                        }, indent=2)

                    # Check if PR is mergeable
                    if not mergeable:
                        return json.dumps({
                            "mergeable": False,
                            "reason": "Pull request has conflicts or is not mergeable",
                            "state": pr_state,
                            "review_states": review_states
                        }, indent=2)

                    # Check review states
                    if not review_states:
                        return json.dumps({
                            "mergeable": False,
                            "reason": "Pull request has no reviews",
                            "state": pr_state,
                            "review_states": review_states
                        }, indent=2)

                    # Check if any review is pending or requires changes
                    for review_state in review_states:
                        if review_state in ["PENDING", "REQUEST_CHANGES", "COMMENT"]:
                            return json.dumps({
                                "mergeable": False,
                                "reason": f"Pull request has {review_state} review state",
                                "state": pr_state,
                                "review_states": review_states
                            }, indent=2)

                    # If we get here, the PR should be mergeable
                    return json.dumps({
                        "mergeable": True,
                        "reason": "All checks passed and reviews approved",
                        "state": pr_state,
                        "review_states": review_states
                    }, indent=2)

                except (ValueError, IndexError):
                    pass

        return json.dumps({"error": f"Pull request #{pullNumber} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_pull_request_mergeability",
                "description": "Check if a pull request is mergeable by examining its status, review states, and mergeable flags.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number to check"}
                    },
                    "required": ["owner", "repo", "pullNumber"]
                }
            }
        }


class MergePullRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, pullNumber: int, merge_method: str, commit_message: str = None) -> str:
        """Merge a PR using the specified method with optional commit message."""
        pull_requests = data.get("pull_requests", [])

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)
                    pr_entry["pr_states"][pr_idx] = "merged"
                    pr_entry["merged_flags"][pr_idx] = True

                    # Use commit_message if provided, otherwise generate default
                    if commit_message:
                        merge_sha = f"merge_{pullNumber}_{merge_method}_{hash(commit_message) % 10000}"
                    else:
                        merge_sha = f"merge_{pullNumber}_{merge_method}"

                    result = {"merged": True, "sha": merge_sha}
                    if commit_message:
                        result["commit_message"] = commit_message

                    return json.dumps(result, indent=2)
                except ValueError:
                    pass

        return json.dumps({"error": f"Pull request #{pullNumber} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "merge_pull_request",
                "description": "Merge a PR using the specified method with optional commit message.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number"},
                        "merge_method": {"type": "string", "description": "Merge method"},
                        "commit_message": {"type": "string", "description": "Optional commit message for the merge"}
                    },
                    "required": ["owner", "repo", "pullNumber", "merge_method"]
                }
            }
        }


class SubmitPullRequestForReview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, pullNumber: int, reviewers: str, submission_message: str = None) -> str:
        """Submit a PR for review by requesting specific reviewers and marking it ready for review."""
        pull_requests = data.get("pull_requests", [])
        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)
                    # Mark PR as ready for review (not draft)
                    pr_entry["pr_states"][pr_idx] = "open"

                    # Parse reviewers (comma-separated string)
                    reviewer_list = [r.strip() for r in reviewers.split(",") if r.strip()]

                    # Initialize review structures if needed
                    if len(pr_entry["reviewers"][pr_idx]) == 0:
                        pr_entry["reviewers"][pr_idx] = [[]]
                        pr_entry["review_states"][pr_idx] = [[]]
                        pr_entry["review_events"][pr_idx] = [[]]

                    # Add reviewers with pending status
                    for reviewer in reviewer_list:
                        if reviewer not in pr_entry["reviewers"][pr_idx][0]:
                            pr_entry["reviewers"][pr_idx][0].append(reviewer)
                            pr_entry["review_states"][pr_idx][0].append("pending")
                            pr_entry["review_events"][pr_idx][0].append("review_requested")

                    # Add submission comment if provided
                    if submission_message:
                        if len(pr_entry["pr_comments"][pr_idx]) == 0:
                            pr_entry["pr_comments"][pr_idx] = [[]]
                            pr_entry["pr_comment_users"][pr_idx] = [[]]
                        pr_entry["pr_comments"][pr_idx][0].append(submission_message)
                        pr_entry["pr_comment_users"][pr_idx][0].append(owner)

                    result = {
                        "submitted": True,
                        "pr_number": pullNumber,
                        "state": "ready_for_review",
                        "requested_reviewers": reviewer_list,
                        "submission_timestamp": "2023-12-05T12:30:00Z"
                    }
                    if submission_message:
                        result["submission_message"] = submission_message

                    return json.dumps(result, indent=2)
                except ValueError:
                    pass
        return json.dumps({"error": f"Pull request #{pullNumber} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "submit_pull_request_for_review",
                "description": "Submit a PR for review by requesting specific reviewers and marking it ready for review.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number"},
                        "reviewers": {"type": "string", "description": "Comma-separated list of reviewer usernames"},
                        "submission_message": {"type": "string", "description": "Optional comment to add when submitting for review"}
                    },
                    "required": ["owner", "repo", "pullNumber", "reviewers"]
                }
            }
        }


class SearchIssues(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], query: str) -> str:
        """Search issues by query."""
        issues_data = data.get("issues", [])
        matching_issues = []

        for issue_entry in issues_data:
            for i, title in enumerate(issue_entry["issue_titles"]):
                if query.lower() in title.lower() or query.lower() in issue_entry["issue_bodies"][i].lower():
                    matching_issues.append({
                        "number": issue_entry["issue_numbers"][i],
                        "title": title,
                        "state": issue_entry["issue_states"][i]
                    })

        return json.dumps({"issues": matching_issues}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_issues",
                "description": "Search issues by query.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Issue search query"}
                    },
                    "required": ["query"]
                }
            }
        }


class CreateIssue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, title: str, body: str, assignees: List[str], labels: List[str] = None) -> str:
        """Create an issue with labels/assignees."""
        issues_data = data.get("issues", [])

        # Validate assignees parameter
        if assignees is None:
            assignees = []
        elif not isinstance(assignees, list):
            assignees = [assignees] if assignees else []

        # Validate labels parameter
        if labels is None:
            labels = []
        elif not isinstance(labels, list):
            labels = [labels] if labels else []

        # Find existing issue entry for this repo
        repo_issues = None
        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                repo_issues = issue_entry
                break

        if not repo_issues:
            # Create new issue entry
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
            # Add to existing issue entry - get the highest existing issue number and add 1
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


class GetIssue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, issue_number: int) -> str:
        """Get comprehensive issue information with metadata, relationships, and statistics."""
        issues_data = data.get("issues", [])
        commits_data = data.get("commits", [])
        pull_requests_data = data.get("pull_requests", [])

        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                try:
                    issue_idx = issue_entry["issue_numbers"].index(issue_number)

                    # Get basic issue data
                    title = issue_entry["issue_titles"][issue_idx]
                    body = issue_entry["issue_bodies"][issue_idx] if issue_idx < len(issue_entry.get("issue_bodies", [])) else ""
                    state = issue_entry["issue_states"][issue_idx]
                    labels = issue_entry["labels"][issue_idx]
                    assignees = issue_entry["assignees"][issue_idx]
                    comments = issue_entry.get("issue_comments", [[]])[issue_idx] if issue_idx < len(issue_entry.get("issue_comments", [])) else []
                    created_at = issue_entry.get("created_ts", ["2023-12-05T12:00:00Z"])[issue_idx] if issue_idx < len(issue_entry.get("created_ts", [])) else "2023-12-05T12:00:00Z"
                    updated_at = issue_entry.get("updated_ts", ["2023-12-05T12:00:00Z"])[issue_idx] if issue_idx < len(issue_entry.get("updated_ts", [])) else "2023-12-05T12:00:00Z"

                    # Generate mock reactions
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

                    # Find linked pull requests (mock based on similar titles/labels)
                    linked_prs = []
                    for pr_entry in pull_requests_data:
                        if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                            for i, pr_title in enumerate(pr_entry.get("pr_titles", [])):
                                if any(word in pr_title.lower() for word in title.lower().split() if len(word) > 3):
                                    linked_prs.append(pr_entry["pr_numbers"][i])

                    # Find referenced commits (mock based on title keywords)
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
                            "linked_pull_requests": linked_prs[:3],  # Limit to first 3
                            "referenced_in_commits": referenced_commits[:5],  # Limit to first 5
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
            "error": f"Issue #{issue_number} not found in repository {owner}/{repo}",
            "error_code": "ISSUE_NOT_FOUND",
            "metadata": {
                "repository": f"{owner}/{repo}",
                "requested_issue": issue_number,
                "search_timestamp": "2023-12-05T12:00:00Z"
            },
            "suggestions": [
                f"Check if issue #{issue_number} exists in repository {owner}/{repo}",
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


class UpdateIssue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, issue_number: int, labels: List[str] = None, assignees: List[str] = None, title: str = None, body: str = None, state: str = None, milestone: str = None) -> str:
        """Update issue with comprehensive tracking of changes, activity, and automated workflow triggers."""
        issues_data = data.get("issues", [])
        auth_users = data.get("authentication", [])

        # Get current user for tracking
        current_user = auth_users[0]["username"] if auth_users else "system"
        update_timestamp = "2023-12-05T12:00:00Z"

        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                try:
                    issue_idx = issue_entry["issue_numbers"].index(issue_number)

                    # Store previous values for change tracking
                    previous_values = {
                        "title": issue_entry["issue_titles"][issue_idx],
                        "body": issue_entry.get("issue_bodies", [""])[issue_idx] if issue_idx < len(issue_entry.get("issue_bodies", [])) else "",
                        "state": issue_entry["issue_states"][issue_idx],
                        "labels": issue_entry["labels"][issue_idx].copy(),
                        "assignees": issue_entry["assignees"][issue_idx].copy(),
                        "updated_at": issue_entry.get("updated_ts", [""])[issue_idx] if issue_idx < len(issue_entry.get("updated_ts", [])) else ""
                    }

                    # Track which fields are being updated
                    updated_fields = []

                    # Update fields if provided
                    if title is not None and title != previous_values["title"]:
                        issue_entry["issue_titles"][issue_idx] = title
                        updated_fields.append("title")

                    if body is not None and body != previous_values["body"]:
                        if "issue_bodies" not in issue_entry:
                            issue_entry["issue_bodies"] = [""] * len(issue_entry["issue_numbers"])
                        if issue_idx < len(issue_entry["issue_bodies"]):
                            issue_entry["issue_bodies"][issue_idx] = body
                        else:
                            issue_entry["issue_bodies"].append(body)
                        updated_fields.append("body")

                    if state is not None and state != previous_values["state"]:
                        issue_entry["issue_states"][issue_idx] = state
                        updated_fields.append("state")

                    if labels is not None and labels != previous_values["labels"]:
                        issue_entry["labels"][issue_idx] = labels
                        updated_fields.append("labels")

                    if assignees is not None and assignees != previous_values["assignees"]:
                        # Validate assignees parameter
                        if assignees is None:
                            assignees = []
                        elif not isinstance(assignees, list):
                            assignees = [assignees] if assignees else []

                        issue_entry["assignees"][issue_idx] = assignees
                        updated_fields.append("assignees")

                    # Update timestamp
                    if "updated_ts" not in issue_entry:
                        issue_entry["updated_ts"] = ["2023-12-05T12:00:00Z"] * len(issue_entry["issue_numbers"])
                    issue_entry["updated_ts"][issue_idx] = update_timestamp

                    # Calculate activity metrics (mock based on changes)
                    comments_added_today = 1 if any(field in ["body", "assignees"] for field in updated_fields) else 0
                    label_changes_this_week = 1 if "labels" in updated_fields else 0
                    assignee_changes = 1 if "assignees" in updated_fields else 0
                    state_changes = 1 if "state" in updated_fields else 0

                    # Generate timeline events
                    timeline_events = []
                    for field in updated_fields:
                        if field == "labels":
                            timeline_events.append(f"Labels changed from {previous_values['labels']} to {labels}")
                        elif field == "assignees":
                            timeline_events.append(f"Assignees changed from {previous_values['assignees']} to {assignees}")
                        elif field == "state":
                            timeline_events.append(f"State changed from {previous_values['state']} to {state}")
                        elif field == "title":
                            timeline_events.append(f"Title updated")
                        elif field == "body":
                            timeline_events.append(f"Description updated")

                    # Mock notifications sent (based on assignee changes)
                    notifications_sent = []
                    if "assignees" in updated_fields:
                        notifications_sent = assignees[:3] if assignees else []  # Limit to 3

                    # Mock automation triggered (based on label/state changes)
                    automation_triggered = []
                    if "labels" in updated_fields:
                        if "bug" in (labels or []):
                            automation_triggered.append("bug-triage-workflow")
                        if "high-priority" in (labels or []):
                            automation_triggered.append("priority-escalation")
                    if "state" in updated_fields:
                        if state == "closed":
                            automation_triggered.append("closure-notification")
                        elif state == "open":
                            automation_triggered.append("reopened-alert")

                    # Get current issue data for response
                    current_data = {
                        "number": issue_number,
                        "title": issue_entry["issue_titles"][issue_idx],
                        "state": issue_entry["issue_states"][issue_idx],
                        "labels": issue_entry["labels"][issue_idx],
                        "assignees": issue_entry["assignees"][issue_idx],
                        "milestone": milestone,  # Use provided milestone or None
                        "updated_fields": updated_fields
                    }

                    # Generate version number (mock incremental version)
                    version = len(updated_fields) + 1

                    result = {
                        "success": True,
                        "data": current_data,
                        "metadata": {
                            "updated_at": update_timestamp,
                            "updated_by": current_user,
                            "previous_values": previous_values,
                            "version": version
                        },
                        "relationships": {
                            "repository": f"{owner}/{repo}",
                            "timeline_events": timeline_events,
                            "notifications_sent": notifications_sent,
                            "automation_triggered": automation_triggered
                        },
                        "activity": {
                            "comments_added_today": comments_added_today,
                            "label_changes_this_week": label_changes_this_week,
                            "assignee_changes": assignee_changes,
                            "state_changes": state_changes
                        }
                    }

                    return json.dumps(result, indent=2)
                except ValueError:
                    pass

        return json.dumps({
            "success": False,
            "error": f"Issue #{issue_number} not found in repository {owner}/{repo}",
            "error_code": "ISSUE_NOT_FOUND",
            "metadata": {
                "repository": f"{owner}/{repo}",
                "requested_issue": issue_number,
                "search_timestamp": update_timestamp
            },
            "suggestions": [
                f"Check if issue #{issue_number} exists in repository {owner}/{repo}",
                "Verify repository name and owner are correct",
                "Use search_issues tool to find available issues"
            ]
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_issue",
                "description": "Update issue with comprehensive change tracking, activity monitoring, automation triggers, and detailed audit trail of all modifications.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "issue_number": {"type": "integer", "description": "Issue number"},
                        "labels": {"type": "array", "items": {"type": "string"}, "description": "New labels (optional)"},
                        "assignees": {"type": "array", "items": {"type": "string"}, "description": "New assignees (optional)"},
                        "title": {"type": "string", "description": "New title (optional)"},
                        "body": {"type": "string", "description": "New body/description (optional)"},
                        "state": {"type": "string", "description": "New state: 'open' or 'closed' (optional)"},
                        "milestone": {"type": "string", "description": "Milestone name (optional)"}
                    },
                    "required": ["owner", "repo", "issue_number"]
                }
            }
        }


class AddIssueComment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, issue_number: int, body: str) -> str:
        """Add a comment to an issue."""
        issues_data = data.get("issues", [])

        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                try:
                    issue_idx = issue_entry["issue_numbers"].index(issue_number)
                    issue_entry["issue_comments"][issue_idx].append(body)
                    issue_entry["issue_comment_users"][issue_idx].append(owner)
                    issue_entry["updated_ts"][issue_idx] = "2023-12-05T12:00:00Z"

                    comment_id = len(issue_entry["issue_comments"][issue_idx])
                    return json.dumps({"comment_id": comment_id}, indent=2)
                except ValueError:
                    pass

        return json.dumps({"error": f"Issue #{issue_number} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_issue_comment",
                "description": "Add a comment to an issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "issue_number": {"type": "integer", "description": "Issue number"},
                        "body": {"type": "string", "description": "Comment body"}
                    },
                    "required": ["owner", "repo", "issue_number", "body"]
                }
            }
        }


class ListIssues(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, state: str, labels: List[str] = None) -> str:
        """List issues filtered by label/state. When no labels are provided, returns all issues."""
        issues_data = data.get("issues", [])

        # Handle None or empty labels as "retrieve all"
        if labels is None:
            labels = []

        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                issues = []
                for i, issue_number in enumerate(issue_entry["issue_numbers"]):
                    issue_state = issue_entry["issue_states"][i]
                    issue_labels = issue_entry["labels"][i]

                    # Filter by state
                    if state != "all" and issue_state != state:
                        continue

                    # Filter by labels (if labels filter is provided and not empty)
                    if labels and not any(label in issue_labels for label in labels):
                        continue

                    issues.append({
                        "number": issue_number,
                        "title": issue_entry["issue_titles"][i],
                        "state": issue_state
                    })

                return json.dumps({"issues": issues}, indent=2)

        return json.dumps({"issues": []}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_issues",
                "description": "List issues filtered by label/state. When no labels are provided, returns all issues.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "state": {"type": "string", "description": "State filter"},
                        "labels": {"type": "array", "items": {"type": "string"}, "description": "Label filter (optional - if not provided, returns all issues)"}
                    },
                    "required": ["owner", "repo", "state"]
                }
            }
        }


class CreatePullRequestReview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, pullNumber: int, body: str, event: str) -> str:
        """Create a PR review (comment/approval)."""
        pull_requests = data.get("pull_requests", [])

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)

                    # Add review to existing structure
                    if not pr_entry["pr_comments"][pr_idx]:
                        pr_entry["pr_comments"][pr_idx] = [[]]
                        pr_entry["pr_comment_users"][pr_idx] = [[]]
                        pr_entry["reviewers"][pr_idx] = [[]]
                        pr_entry["review_states"][pr_idx] = [[]]
                        pr_entry["review_events"][pr_idx] = [[]]

                    pr_entry["pr_comments"][pr_idx][0].append(body)
                    pr_entry["pr_comment_users"][pr_idx][0].append(owner)
                    pr_entry["reviewers"][pr_idx][0].append(owner)
                    pr_entry["review_states"][pr_idx][0].append(event)
                    pr_entry["review_events"][pr_idx][0].append(event)

                    review_id = len(pr_entry["pr_comments"][pr_idx][0])
                    return json.dumps({"review_id": review_id, "state": event}, indent=2)
                except ValueError:
                    pass

        return json.dumps({"error": f"Pull request #{pullNumber} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_pull_request_review",
                "description": "Create a PR review (comment/approval).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number"},
                        "body": {"type": "string", "description": "Review body"},
                        "event": {"type": "string", "description": "Review event type"}
                    },
                    "required": ["owner", "repo", "pullNumber", "body", "event"]
                }
            }
        }


class DeleteRepository(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str) -> str:
        """Delete a repository permanently."""
        repositories = data.get("repositories", [])

        # Find and remove the repository
        for i, repository in enumerate(repositories):
            if repository["owner"] == owner and repository["repo_name"] == repo:
                repositories.pop(i)

                # Also clean up related data
                # Remove commits
                commits = data.get("commits", [])
                for j in range(len(commits) - 1, -1, -1):
                    if commits[j]["owner"] == owner and commits[j]["repo_name"] == repo:
                        commits.pop(j)

                # Remove pull requests
                pull_requests = data.get("pull_requests", [])
                for j in range(len(pull_requests) - 1, -1, -1):
                    if pull_requests[j]["owner"] == owner and pull_requests[j]["repo_name"] == repo:
                        pull_requests.pop(j)

                # Remove issues
                issues = data.get("issues", [])
                for j in range(len(issues) - 1, -1, -1):
                    if issues[j]["owner"] == owner and issues[j]["repo_name"] == repo:
                        issues.pop(j)

                # Remove code scanning alerts
                alerts = data.get("code_scanning_alerts", [])
                for j in range(len(alerts) - 1, -1, -1):
                    if alerts[j]["owner"] == owner and alerts[j]["repo_name"] == repo:
                        alerts.pop(j)

                return json.dumps({"deleted": True, "repository": f"{owner}/{repo}"}, indent=2)

        return json.dumps({"error": f"Repository {owner}/{repo} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_repository",
                "description": "Delete a repository permanently.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"}
                    },
                    "required": ["owner", "repo"]
                }
            }
        }


class GetLabels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str) -> str:
        """Get all available labels for a repository."""
        issues_data = data.get("issues", [])

        # Find the repository in issues data
        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                # Collect all unique labels from all issues in this repository
                all_labels = set()
                for labels_list in issue_entry["labels"]:
                    if isinstance(labels_list, list):
                        all_labels.update(labels_list)
                    elif isinstance(labels_list, str):
                        all_labels.add(labels_list)

                # Convert to sorted list for consistent output
                available_labels = sorted(list(all_labels))

                return json.dumps({
                    "success": True,
                    "data": {
                        "repository": f"{owner}/{repo}",
                        "available_labels": available_labels,
                        "total_labels": len(available_labels)
                    },
                    "metadata": {
                        "owner": owner,
                        "repo": repo,
                        "labels_discovered": len(available_labels)
                    }
                }, indent=2)

        # If repository not found, return empty labels list
        return json.dumps({
            "success": True,
            "data": {
                "repository": f"{owner}/{repo}",
                "available_labels": [],
                "total_labels": 0
            },
            "metadata": {
                "owner": owner,
                "repo": repo,
                "labels_discovered": 0
            }
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_labels",
                "description": "Get all available labels for a repository to understand the labeling system and available options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"}
                    },
                    "required": ["owner", "repo"]
                }
            }
        }


class ResolvePullRequestBlockers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, pullNumber: int) -> str:
        """Resolve blocking issues on a pull request to make it mergeable."""
        pull_requests = data.get("pull_requests", [])

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)

                    pr_state = pr_entry["pr_states"][pr_idx]
                    mergeable = pr_entry["mergeable_flags"][pr_idx]
                    merged = pr_entry["merged_flags"][pr_idx]
                    review_states = pr_entry["review_states"][pr_idx] if pr_idx < len(pr_entry["review_states"]) else []

                    if merged:
                        return json.dumps({"resolved": False, "reason": "Pull request is already merged", "state": pr_state}, indent=2)
                    if pr_state == "closed":
                        return json.dumps({"resolved": False, "reason": "Pull request is closed", "state": pr_state}, indent=2)

                    # Check if there are blocking review states
                    blocking_states = []
                    for review_state in review_states:
                        if review_state in ["PENDING", "REQUEST_CHANGES", "COMMENT"]:
                            blocking_states.append(review_state)

                    if blocking_states:
                        # Resolve blocking states by changing them to APPROVE
                        resolved_states = []
                        for state in review_states:
                            if state in blocking_states:
                                resolved_states.append("APPROVE")
                            else:
                                resolved_states.append(state)

                        # Update the review states in the data
                        pr_entry["review_states"][pr_idx] = resolved_states
                        pr_entry["review_events"][pr_idx] = resolved_states

                        return json.dumps({
                            "resolved": True,
                            "reason": f"Resolved blocking review states: {blocking_states} -> APPROVE",
                            "original_states": review_states,
                            "resolved_states": resolved_states,
                            "mergeable": True
                        }, indent=2)

                    if not mergeable:
                        # If not mergeable due to conflicts, we can't resolve programmatically
                        return json.dumps({"resolved": False, "reason": "Pull request has conflicts that require manual resolution", "mergeable": False}, indent=2)

                    return json.dumps({"resolved": True, "reason": "Pull request is already mergeable", "mergeable": True}, indent=2)

                except (ValueError, IndexError):
                    pass

        return json.dumps({"error": f"Pull request #{pullNumber} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "resolve_pull_request_blockers",
                "description": "Resolve blocking issues on a pull request to make it mergeable by addressing pending reviews, request changes, and other blockers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number to resolve blockers for"}
                    },
                    "required": ["owner", "repo", "pullNumber"]
                }
            }
        }


class AppendTerminal(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], command: str) -> str:
        """Execute terminal-like commands for GitHub operations analysis and workflow insights."""
        # Ensure terminal data exists and has the correct structure
        if "terminal" not in data or not data["terminal"]:
            data["terminal"] = [{
                "printed_ts": [],
                "commands": [],
                "outputs": []
            }]

        terminal_data = data["terminal"]

        # Ensure the first element exists and has the correct structure
        if not terminal_data or not isinstance(terminal_data[0], dict):
            terminal_data[0] = {
                "printed_ts": [],
                "commands": [],
                "outputs": []
            }

        # Ensure all required keys exist
        if "printed_ts" not in terminal_data[0]:
            terminal_data[0]["printed_ts"] = []
        if "commands" not in terminal_data[0]:
            terminal_data[0]["commands"] = []
        if "outputs" not in terminal_data[0]:
            terminal_data[0]["outputs"] = []

        timestamp = "2023-12-05T12:00:00Z"
        terminal_data[0]["printed_ts"].append(timestamp)
        terminal_data[0]["commands"].append(command)

        # Process different terminal commands for GitHub workflow analysis
        if command.startswith("git status"):
            output = "Repository status: Clean working directory, all changes committed"
        elif command.startswith("git log"):
            output = "Recent commits: Latest changes include security fixes and feature updates"
        elif command.startswith("ps aux"):
            output = "GitHub Actions: workflow running, authentication verified, API rate limits OK"
        elif command.startswith("ls -la"):
            output = "Repository contents: .github/ workflows/ src/ docs/ README.md .gitignore"
        elif command.startswith("env"):
            output = "Environment: GITHUB_TOKEN=*****, NODE_ENV=production, CI=true"
        elif command.startswith("curl"):
            output = "API Health Check: GitHub API responding, rate limit: 4999/5000 remaining"
        elif command.startswith("docker"):
            output = "Container Status: GitHub Actions runner healthy, image pulls successful"
        elif command.startswith("npm"):
            output = "Dependencies: All packages installed, security audit passed, no vulnerabilities"
        elif command.startswith("echo"):
            # Extract message after echo
            message = command.replace("echo ", "").strip('"\'')
            output = f"DEBUG: {message}"
        elif command.startswith("cat"):
            output = "File contents: Configuration loaded successfully, secrets validated"
        elif command.startswith("grep"):
            output = "Search results: Pattern found in 3 files, context extracted"
        elif command.startswith("tail"):
            output = "Log tail: [INFO] Authentication successful [INFO] Repository access granted [INFO] Operation completed"
        elif command.startswith("whoami"):
            output = "Current user: github-actions-bot (authenticated via token)"
        elif command.startswith("pwd"):
            output = "Current directory: /github/workspace/repository-name"
        elif command.startswith("free"):
            output = "Memory usage: 2.1GB used / 7GB total, GitHub Actions limits OK"
        elif command.startswith("top"):
            output = "Processes: git-daemon, node, npm, github-runner (all healthy)"
        else:
            output = f"Command executed: {command} - GitHub workflow operation logged"

        terminal_data[0]["outputs"].append(output)

        return json.dumps({
            "command": command,
            "output": output,
            "timestamp": timestamp,
            "session_id": "github-actions-session-001"
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_terminal",
                "description": "Execute terminal-like commands for GitHub operations analysis, debugging, and workflow insights. Supports git, system, and CI/CD commands.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "command": {
                            "type": "string",
                            "description": "Terminal command to execute (e.g., 'git status', 'ps aux', 'echo \"Debug message\"', 'curl api/health')"
                        }
                    },
                    "required": ["command"]
                }
            }
        }


# Export tools as instances
TOOLS = [
    GetMe(),
    SearchRepositories(),
    CreateRepository(),
    DeleteRepository(),
    CreateOrUpdateFile(),
    GetFileContents(),
    ListCommits(),
    SearchCode(),
    ListCodeScanningAlerts(),
    CreateBranch(),
    CreatePullRequest(),
    GetPullRequest(),
    ListPullRequests(),
    GetPullRequestStatus(),
    CheckPullRequestMergeability(),
    ResolvePullRequestBlockers(),
    MergePullRequest(),
    SubmitPullRequestForReview(),
    SearchIssues(),
    CreateIssue(),
    GetIssue(),
    UpdateIssue(),
    AddIssueComment(),
    ListIssues(),
    CreatePullRequestReview(),
    GetRepository(),
    GetLabels(),
    AppendTerminal(),
]
