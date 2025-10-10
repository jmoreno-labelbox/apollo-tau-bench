import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict, List
from domains.dto import Tool


branch_sha_num = 100
merge_sha_num = 100
commit_sha_num = 100
pr_num = 100
alert_num = 100
issue_num = 100


def get_current_timestamp() -> str:
    return "2025-08-21T12:00:00Z" # per rules

def get_current_updated_timestamp() -> str:
    return "2025-08-21T12:30:00Z" # per rules


def get_next_branch_sha(data):
    global branch_sha_num
    branch_sha_num = branch_sha_num + 1
    return f"branch_sha_{branch_sha_num}"

def get_next_merge_sha(data):
    global merge_sha_num
    merge_sha_num = merge_sha_num + 1
    return f"merge_sha_{merge_sha_num}"

def get_next_commit_sha(data):
    global commit_sha_num
    commit_sha_num = commit_sha_num + 1
    return f"commit_sha_{commit_sha_num}"

def get_next_pr_number(data):
    global pr_num
    pr_num = pr_num + 1
    return pr_num

def get_next_alert_number(data):
    global alert_num
    alert_num = alert_num + 1
    return alert_num

def get_next_issue_number(data):
    global issue_num
    issue_num = issue_num + 1
    return issue_num


def reset_variables():
    global branch_sha_num,merge_sha_num,commit_sha_num,pr_num,alert_num,issue_num

    branch_sha_num = 100
    merge_sha_num = 100
    commit_sha_num = 100
    pr_num = 100
    alert_num = 100
    issue_num = 100


# def get_next_branch_sha(data):
#     repo = data.get("repositories", [])
#     next_num = 88 + len(repo) + 1
#     return f"branch_sha_{next_num}"

# def get_next_merge_sha(data):
#     repo = data.get("repositories", [])
#     next_num = 88 + len(repo) + 1
#     return f"merge_sha_{next_num}"

# def get_next_commit_sha(data):
#     commits = data.get("commits", [])
#     next_num = 88 + len(commits) + 1
#     return f"commit_sha_{next_num}"

# def get_next_pr_number(data):
#     prs = len(data.get("pull_requests", []))
#     next_num = 91 + prs + 1
#     return next_num

# def get_next_alert_number(data):
#     prs = len(data.get("code_scanning_alerts", []))
#     next_num = 91 + prs + 1
#     return next_num

# def get_next_issue_number(data):
#     prs = len(data.get("issues", []))
#     next_num = 89 + prs + 1
#     return next_num

# def ensure_align(arr: List[List[str]], length: int) -> None:
#     """Pad a list-of-lists to the given length with empty lists."""
#     while len(arr) < length:
#         arr.append([])

# def ensure_len(lst: List[str], target_len: int, pad_val: str = "") -> None:
#     """Pad a flat list to target_len with pad_val."""
#     while len(lst) < target_len:
#         lst.append(pad_val)

# def merge_files(
#     src_files: List[str],
#     src_contents: List[str],
#     tgt_files: List[str],
#     tgt_contents: List[str],
#     conflict_strategy: str = "source_wins",
# ):
#     """
#     Merge source into target.
#     Returns (new_files, new_contents, added_files, overwritten_files)
#     - Adds new files from source in source order
#     - On conflict: 'source_wins' overwrites target; 'target_wins' keeps target
#     """
#     ensure_len(src_contents, len(src_files), "")
#     ensure_len(tgt_contents, len(tgt_files), "")

#     new_files = list(tgt_files)
#     new_contents = list(tgt_contents)
#     added_files: List[str] = []
#     overwritten_files: List[str] = []

#     for i, fname in enumerate(src_files):
#         s_content = src_contents[i]
#         if fname in new_files:
#             t_idx = new_files.index(fname)
#             if conflict_strategy == "source_wins":
#                 if new_contents[t_idx] != s_content:
#                     overwritten_files.append(fname)
#                 new_contents[t_idx] = s_content
#             else:
#                 # target_wins → do nothing
#                 pass
#         else:
#             new_files.append(fname)
#             new_contents.append(s_content)
#             added_files.append(fname)

#     return new_files, new_contents, added_files, overwritten_files


def add_terminal_message(data: Dict[str, Any], message: str, timestamp: str) -> Dict[str, Any]:
    """
    Append a terminal message with a provided timestamp into data['terminal'].

    - data['terminal'] may be a list (first item is the entry) or a dict.
    - Ensures 'printed_ts' and 'messages' arrays exist and appends to both.
    - Returns a dict with either {'success': ..., 'message': ...} or {'error': ...}.
    """
    message = (message or "").strip()
    timestamp = (timestamp or "").strip()

    if not message or not timestamp:
        return {"error": "Both 'message' and 'timestamp' are required."}

    terminal = data.get("terminal", [])

    # Normalize to the terminal entry object that has 'printed_ts' and 'messages'
    if isinstance(terminal, list):
        if len(terminal) == 0:
            terminal.append({"printed_ts": [], "messages": []})
        entry = terminal[0]
    elif isinstance(terminal, dict):
        entry = terminal
    else:
        return {"error": "Invalid database format: 'terminal' must be a list or dict."}

    if not isinstance(entry, dict):
        return {"error": "Invalid terminal entry: expected an object with 'printed_ts' and 'messages'."}

    entry.setdefault("printed_ts", []).append(timestamp)
    entry.setdefault("messages", []).append(message)

    # return json.dumps({"success": f"Message added at {timestamp}", "message": message})




class AuthenticateUser(Tool):
    """Validates a user by username, email, and auth_key; returns full record on success."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        username = kwargs.get("username", "").strip()
        email = kwargs.get("email", "").strip()
        auth_key = kwargs.get("auth_key", "").strip()

        reset_variables()

        if not username or not email or not auth_key:
            return json.dumps(
                {"error": "username, email, and auth_key are all required."},
                indent=2
            )

        # Primary store: data.get("authentication", [])
        authentication = data.get("authentication", [])

        # Fallback if the DB was provided as a top-level list
        if not isinstance(authentication, list) and isinstance(data, list):
            authentication = data

        # Lookup by username first
        user = next((u for u in authentication if u.get("username") == username), None)
        if not user:
            return json.dumps({"error": "User not found."}, indent=2)

        # Validate remaining credentials
        if user.get("email") != email or user.get("auth_key") != auth_key:
            return json.dumps({"error": "Credentials invalid."}, indent=2)
    

        # Success: include full user record
        return json.dumps(
            {
                "success": f"User '{username}' authenticated successfully.",
                "user": user
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "authenticate_user",
                "description": "Validates user credentials using username (primary lookup), then email and auth_key. Returns full record on success.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string", "description": "The username of the user"},
                        "email": {"type": "string", "description": "The registered email address of the user"},
                        "auth_key": {"type": "string", "description": "Authentication key for the user"}
                    },
                    "required": ["username", "email", "auth_key"]
                }
            }
        }
   

class GetRepoInfoForOwner(Tool):
    """Returns key repository info (including file paths and contents) for a given owner + repo_name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = kwargs.get("repo_name", "").strip()

        if not owner or not repo_name:
            return json.dumps(
                {"error": "Both 'owner' and 'repo_name' are required."},
                indent=2
            )

        # DB may be { "repositories": [...] } or a direct list
        repos = data.get("repositories", [])

        repo = next(
            (r for r in repos
             if r.get("owner") == owner and r.get("repo_name") == repo_name),
            None
        )
        if not repo:
            return json.dumps(
                {"error": f"Repository '{owner}/{repo_name}' not found."},
                indent=2
            )

        result = {
            "owner": repo.get("owner"),
            "repo_name": repo.get("repo_name"),
            "description": repo.get("description_nullable"),
            "private": repo.get("private_flag"),
            "auto_init": repo.get("auto_init_flag"),
            "default_branch": repo.get("default_branch"),
            "file_paths": repo.get("file_paths", []),
            "file_contents": repo.get("file_contents", []),
            "branches": repo.get("branches", []),
            "branch_shas": repo.get("branch_shas", []),
            "created_ts": repo.get("created_ts"),
            "updated_ts": repo.get("updated_ts"),
            
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repo_info_for_owner",
                "description": "Fetches repository metadata including owner, repo_name, description, private flag, auto_init, default branch, branches, branch SHAs, timestamps, and file paths/contents.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "Repository owner (account/team)."
                        },
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name."
                        }
                    },
                    "required": ["owner", "repo_name"]
                }
            }
        }


class GetBranchContent(Tool):
    """
    Returns branch-specific information for a given owner/repository/branch.
    Output includes: branch name, branch files, branch contents, and branch SHA,
    all aligned by the same branch index.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = kwargs.get("repo_name", "").strip()
        branch = kwargs.get("branch_name", "").strip()

        if not owner or not repo_name or not branch:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', and 'branch' are all required."},
                indent=2
            )

        # Support either {"repositories": [...]} or a direct list
        repos = data.get("repositories", [])

        repo = next(
            (r for r in repos if r.get("owner") == owner and r.get("repo_name") == repo_name),
            None
        )
        if not repo:
            return json.dumps(
                {"error": f"Repository '{owner}/{repo_name}' not found."},
                indent=2
            )

        branches = repo.get("branches", [])
        if branch not in branches:
            return json.dumps(
                {"error": f"Branch '{branch}' not found in repository '{owner}/{repo_name}'."},
                indent=2
            )

        idx = branches.index(branch)

        # Fetch aligned per-branch artifacts (defensive against missing keys)
        branch_files_all = repo.get("branch_files", [])
        branch_contents_all = repo.get("branch_contents", [])
        branch_shas_all = repo.get("branch_shas", [])

        # Fallbacks: if per-branch arrays are missing, fall back to repo-wide files/contents
        files  = None
        contents  = None

        if idx < len(branch_files_all):
            files = branch_files_all[idx]
        elif "file_paths" in repo:
            files = repo.get("file_paths", [])

        if idx < len(branch_contents_all):
            contents = branch_contents_all[idx]
        elif "file_contents" in repo:
            contents = repo.get("file_contents", [])

        sha = branch_shas_all[idx] if idx < len(branch_shas_all) else None

        result = {
            "branch": branch,
            "branch_files": files if files is not None else [],
            "branch_contents": contents if contents is not None else [],
            "branch_sha": sha
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_branch_content",
                "description": "Fetch branch-level files, contents, and SHA for a given owner/repository/branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "Repository owner (account/team)."
                        },
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name."
                        },
                        "branch_name": {
                            "type": "string",
                            "description": "Branch name to retrieve."
                        }
                    },
                    "required": ["owner", "repo_name", "branch_name"]
                }
            }
        }


class DeleteRepository(Tool):
    """Deletes a repository identified by owner and repo name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        # Accept either 'repo_name' or 'repo_name' for convenience
        repo_name = kwargs.get("repo_name", kwargs.get("repo_name", "")).strip()

        if not owner or not repo_name:
            return json.dumps(
                {"error": "Both 'owner' and 'repo_name' are required."},
                indent=2
            )

        # Support either {"repositories": [...]} or a direct list
        repos = None
        if isinstance(data, dict) and "repositories" in data:
            repos = data.get("repositories", [])
        elif isinstance(data, list):
            repos = data
        else:
            return json.dumps(
                {"error": "Invalid database format: expected a list or a dict with 'repositories'."},
                indent=2
            )

        # Find the repository index deterministically (first exact match)
        idx = next(
            (i for i, r in enumerate(repos)
             if r.get("owner") == owner and r.get("repo_name") == repo_name),
            None
        )

        if idx is None:
            return json.dumps(
                {"error": f"Repository '{owner}/{repo_name}' not found."},
                indent=2
            )

        # Remove the repo in place (deterministic mutation)
        removed = repos.pop(idx)

        add_terminal_message(data, f"Repository '{owner}/{repo_name}' deleted.", get_current_timestamp())

        return json.dumps(
            {
                "success": f"Repository '{owner}/{repo_name}' deleted.",
                "deleted": {
                    "owner": removed.get("owner"),
                    "repo_name": removed.get("repo_name"),
                    "deleted_ts": get_current_timestamp()
                }
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_repository",
                "description": "Deletes a repository for the given owner and repository name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "Repository owner (account/team)."
                        },
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name."
                        }
                    },
                    "required": ["owner", "repo_name"]
                }
            }
        }


class CreateRepository(Tool):
    """
    Creates a repository for the given owner and settings.
    - If a repo with (owner, repo_name) exists, the name becomes repo_name + "_v2".
    - Creates default branch 'main' with a deterministic SHA.
    - Sets created_ts/updated_ts deterministically as (max existing created_ts + 1 minute),
      or a fixed baseline if none exist.
    - If autoinit_flag is true, adds a minimal README to file paths/contents (and to branch files/contents).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = kwargs.get("repo_name", "").strip()
        description = kwargs.get("description", None)
        private_flag = kwargs.get("private_flag", False)
        autoinit_flag = kwargs.get("auto_init_flag", False)

        if not owner or not repo_name:
            return json.dumps(
                {"error": "Both 'owner' and 'repo_name' are required."},
                indent=2
            )


        repos = data.get("repositories", [])



        # Normalize description to the nullable field name used in the DB
        description_nullable = description if description is not None else None

        # Collision handling: if (owner, repo_name) exists, try single '_v2' suffix
        def _exists(o: str, n: str) -> bool:
            return any(r.get("owner") == o and r.get("repo_name") == n for r in repos)

        if _exists(owner, repo_name):
            candidate = f"{repo_name}_v2"
            if _exists(owner, candidate):
                return json.dumps(
                    {"error": f"Repository '{owner}/{repo_name}' exists and '{candidate}' also exists."},
                    indent=2
                )
            repo_name = candidate  # single deterministic suffix

        # Deterministic timestamps
        created_ts = get_current_timestamp()
        updated_ts = created_ts  # start equal on creation

        # Defaults
        default_branch = "main"
        branches = ["main"]

        # Deterministic SHA for 'main'
        main_sha = get_next_branch_sha(data)
        branch_shas = [main_sha]

        # Auto-init file tree (repo-wide)
        file_paths= []
        file_contents= []

        # Per-branch aligned structures
        branch_files = [[]]
        branch_contents = [[]]

        if autoinit_flag:
            readme_content = f"# {repo_name}\n\nInitial commit."
            file_paths = ["README.md"]
            file_contents = [readme_content]
            branch_files = [file_paths.copy()]
            branch_contents = [file_contents.copy()]

        # Assemble the new repo record following existing schema
        new_repo = {
            "owner": owner,
            "repo_name": repo_name,
            "description_nullable": description_nullable,
            "private_flag": bool(private_flag),
            "auto_init_flag": bool(autoinit_flag),
            "default_branch": default_branch,
            "file_paths": file_paths,
            "file_contents": file_contents,
            "branches": branches,
            "branch_files": branch_files,
            "branch_contents": branch_contents,
            "branch_shas": branch_shas,
            "created_ts": created_ts,
            "updated_ts": updated_ts,
        }

        # Insert deterministically at the end
        repos.append(new_repo)

        add_terminal_message(data, f"Repository '{owner}/{repo_name}' created.", get_current_timestamp())

        return json.dumps(
            {
                "success": f"Repository '{owner}/{repo_name}' created.",
                "repository": {
                    "owner": owner,
                    "repo_name": repo_name,
                    "default_branch": default_branch,
                    "branch_shas": branch_shas,
                    "created_ts": created_ts,
                    "updated_ts": updated_ts,
                    "file_paths": file_paths,
                    "file_contents": file_contents
                }
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_repository",
                "description": "Creates a new repository with default branch 'main', a deterministic branch SHA, and deterministic timestamps. If name exists, appends '_v2'. If autoinit_flag is true, seeds README.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "Repository owner (account/team)."
                        },
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name to create (may be suffixed with '_v2' if taken)."
                        },
                        "description": {
                            "type": "string",
                            "nullable": True,
                            "description": "Optional description of the repository."
                        },
                        "private_flag": {
                            "type": "boolean",
                            "description": "Whether the repo is private."
                        },
                        "autoinit_flag": {
                            "type": "boolean",
                            "description": "If true, adds README to file paths/contents and to the main branch."
                        }
                    },
                    "required": ["owner", "repo_name", "private_flag", "auto_init_flag"]
                }
            }
        }


class AddNewFileInRepo(Tool):
    """
    Appends a new file and its content to a repository branch.
    - Adds to branch_files[idx] and branch_contents[idx] (same index as the branch).
    - If branch is 'main', also adds to repo-level file_paths and file_contents.
    - Prevents duplicate file_names within the same branch.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = kwargs.get("repo_name", "").strip()
        branch_name = kwargs.get("branch_name", "").strip()
        file_name = kwargs.get("file_name", "").strip()
        file_content = kwargs.get("file_content", "")

        if not owner or not repo_name or not branch_name or not file_name:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', 'branch_name', and 'file_name' are required."},
                indent=2
            )

        # Preferred repository access pattern
        repos = data.get("repositories", [])
        if not isinstance(repos, list):
            return json.dumps(
                {"error": "Invalid database format: expected 'repositories' to be a list."},
                indent=2
            )

        # Locate repository
        repo = next(
            (r for r in repos if r.get("owner") == owner and r.get("repo_name") == repo_name),
            None
        )
        if not repo:
            return json.dumps(
                {"error": f"Repository '{owner}/{repo_name}' not found."},
                indent=2
            )

        branches = repo.get("branches", [])
        if branch_name not in branches:
            return json.dumps(
                {"error": f"Branch '{branch_name}' not found in repository '{owner}/{repo_name}'."},
                indent=2
            )
        idx = branches.index(branch_name)

        # Ensure per-branch structures exist and are aligned to branches length
        branch_files_all = repo.setdefault("branch_files", [])
        branch_contents_all = repo.setdefault("branch_contents", [])

        while len(branch_files_all) < len(branches):
            branch_files_all.append([])
        while len(branch_contents_all) < len(branches):
            branch_contents_all.append([])

        branch_files = branch_files_all[idx]
        branch_contents = branch_contents_all[idx]

        if not isinstance(branch_files, list) or not isinstance(branch_contents, list):
            return json.dumps(
                {"error": "Invalid repository format: branch_files/branch_contents must be lists."},
                indent=2
            )

        # Prevent duplicate file_name in the branch
        if file_name in branch_files:
            return json.dumps(
                {"error": f"File '{file_name}' already exists in branch '{branch_name}'."},
                indent=2
            )

        # Append to branch-scoped arrays (same index)
        branch_files.append(file_name)
        branch_contents.append(file_content)

        # If 'main' branch, also append to repo-wide file lists (avoid duplicates)
        if branch_name == "main":
            repo.setdefault("file_paths", [])
            repo.setdefault("file_contents", [])
            if file_name not in repo["file_paths"]:
                repo["file_paths"].append(file_name)
                repo["file_contents"].append(file_content)

        repo["updated_ts"] = get_current_updated_timestamp()

        add_terminal_message(data, f"Added '{file_name}' to {owner}/{repo_name}@{branch_name}.", get_current_timestamp())

        return json.dumps(
            {
                "success": f"Added '{file_name}' to {owner}/{repo_name}@{branch_name}.",
                "repo": f"{owner}/{repo_name}",
                "branch": branch_name,
                "added": {
                    "file_name": file_name,
                    "file_content": file_content
                },
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_new_file_in_repo",
                "description": "Append a new file and content to a repository branch; if branch is 'main', also append to repo-level file paths/contents.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner (account/team)."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "branch_name": {"type": "string", "description": "Branch to modify (e.g., 'main')."},
                        "file_name": {"type": "string", "description": "Path/name of the file to add (e.g., 'src/app.ts')."},
                        "file_content": {"type": "string", "description": "File contents to store."}
                    },
                    "required": ["owner", "repo_name", "branch_name", "file_name", "file_content"]
                }
            }
        }


class UpdateFileInRepo(Tool):
    """
    Updates the content of an existing file in a repository branch.
    - Finds the branch by name and locates the file_name in branch_files[idx].
    - Updates branch_contents[idx] at the same file index.
    - If branch is 'main', also updates repo-level file_contents at the file_name's index.
    - Deterministic, no timestamps or randomness.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = kwargs.get("repo_name", "").strip()
        branch_name = kwargs.get("branch_name", "").strip()
        file_name = kwargs.get("file_name", "").strip()
        file_content = kwargs.get("file_content", "")

        if not owner or not repo_name or not branch_name or not file_name:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', 'branch_name', and 'file_name' are required."},
                indent=2
            )

        # Preferred repository access pattern
        repos: List[Dict[str, Any]] = data.get("repositories", [])
        if not isinstance(repos, list):
            return json.dumps(
                {"error": "Invalid database format: expected 'repositories' to be a list."},
                indent=2
            )

        # Locate repository
        repo = next(
            (r for r in repos if r.get("owner") == owner and r.get("repo_name") == repo_name),
            None
        )
        if not repo:
            return json.dumps(
                {"error": f"Repository '{owner}/{repo_name}' not found."},
                indent=2
            )

        branches: List[str] = repo.get("branches", [])
        if branch_name not in branches:
            return json.dumps(
                {"error": f"Branch '{branch_name}' not found in repository '{owner}/{repo_name}'."},
                indent=2
            )
        idx = branches.index(branch_name)

        # Ensure per-branch structures exist and are aligned
        branch_files_all: List[List[str]] = repo.setdefault("branch_files", [])
        branch_contents_all: List[List[str]] = repo.setdefault("branch_contents", [])
        while len(branch_files_all) < len(branches):
            branch_files_all.append([])
        while len(branch_contents_all) < len(branches):
            branch_contents_all.append([])

        branch_files = branch_files_all[idx]
        branch_contents = branch_contents_all[idx]
        if not isinstance(branch_files, list) or not isinstance(branch_contents, list):
            return json.dumps(
                {"error": "Invalid repository format: branch_files/branch_contents must be lists."},
                indent=2
            )

        if file_name not in branch_files:
            return json.dumps(
                {"error": f"File '{file_name}' not found in branch '{branch_name}'."},
                indent=2
            )

        fidx = branch_files.index(file_name)
        # Keep arrays aligned
        while len(branch_contents) < len(branch_files):
            branch_contents.append("")

        previous_content = branch_contents[fidx]
        branch_contents[fidx] = file_content

        # If main branch, also update repo-level file_contents
        if branch_name == "main":
            repo.setdefault("file_paths", [])
            repo.setdefault("file_contents", [])
            # Align lengths
            while len(repo["file_contents"]) < len(repo["file_paths"]):
                repo["file_contents"].append("")
            if file_name in repo["file_paths"]:
                ridx = repo["file_paths"].index(file_name)
                repo["file_contents"][ridx] = file_content

        repo["updated_ts"] = get_current_updated_timestamp()

        add_terminal_message(data, f"Updated '{file_name}' in {owner}/{repo_name}@{branch_name}.", get_current_updated_timestamp())

        return json.dumps(
            {
                "success": f"Updated '{file_name}' in {owner}/{repo_name}@{branch_name}.",
                "repo": f"{owner}/{repo_name}",
                "branch": branch_name,
                "file": {
                    "file_name": file_name,
                    "previous_content": previous_content,
                    "new_content": file_content
                }
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_file_in_repo",
                "description": "Update the content of an existing file in a repository branch; if branch is 'main', also update repo-level file contents.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner (account/team)."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "branch_name": {"type": "string", "description": "Branch name (e.g., 'main')."},
                        "file_name": {"type": "string", "description": "Path/name of the file to update."},
                        "file_content": {"type": "string", "description": "New content to write into the file."}
                    },
                    "required": ["owner", "repo_name", "branch_name", "file_name", "file_content"]
                }
            }
        }


class DeleteFileInRepo(Tool):
    """
    Deletes a file from a repository branch.
    - Removes from branch_files[idx] and branch_contents[idx] at the same index.
    - If branch is 'main', also removes from repo-level file_paths/file_contents.
    - Returns remaining files in the branch (and repo-level files if branch is 'main').
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = kwargs.get("repo_name", "").strip()
        branch_name = kwargs.get("branch_name", "").strip()
        file_name = kwargs.get("file_name", "").strip()

        if not owner or not repo_name or not branch_name or not file_name:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', 'branch_name', and 'file_name' are required."},
                indent=2
            )

        # Preferred repository access pattern
        repos: List[Dict[str, Any]] = data.get("repositories", [])
        if not isinstance(repos, list):
            return json.dumps(
                {"error": "Invalid database format: expected 'repositories' to be a list."},
                indent=2
            )

        # Locate repository
        repo = next(
            (r for r in repos if r.get("owner") == owner and r.get("repo_name") == repo_name),
            None
        )
        if not repo:
            return json.dumps(
                {"error": f"Repository '{owner}/{repo_name}' not found."},
                indent=2
            )

        branches: List[str] = repo.get("branches", [])
        if branch_name not in branches:
            return json.dumps(
                {"error": f"Branch '{branch_name}' not found in repository '{owner}/{repo_name}'."},
                indent=2
            )
        idx = branches.index(branch_name)

        # Ensure per-branch structures exist and are aligned
        branch_files_all: List[List[str]] = repo.setdefault("branch_files", [])
        branch_contents_all: List[List[str]] = repo.setdefault("branch_contents", [])
        while len(branch_files_all) < len(branches):
            branch_files_all.append([])
        while len(branch_contents_all) < len(branches):
            branch_contents_all.append([])

        branch_files = branch_files_all[idx]
        branch_contents = branch_contents_all[idx]

        if not isinstance(branch_files, list) or not isinstance(branch_contents, list):
            return json.dumps(
                {"error": "Invalid repository format: branch_files/branch_contents must be lists."},
                indent=2
            )

        if file_name not in branch_files:
            return json.dumps(
                {"error": f"File '{file_name}' not found in branch '{branch_name}'."},
                indent=2
            )

        # Keep arrays aligned before deletion
        while len(branch_contents) < len(branch_files):
            branch_contents.append("")

        fidx = branch_files.index(file_name)
        removed_content = branch_contents[fidx]

        # Delete from branch-level arrays (same index)
        branch_files.pop(fidx)
        branch_contents.pop(fidx)

        # If 'main' branch, also remove from repo-level lists (by filename)
        repo_files_after = None
        if branch_name == "main":
            repo.setdefault("file_paths", [])
            repo.setdefault("file_contents", [])
            if file_name in repo["file_paths"]:
                ridx = repo["file_paths"].index(file_name)
                # Align before deletion
                while len(repo["file_contents"]) < len(repo["file_paths"]):
                    repo["file_contents"].append("")
                repo["file_paths"].pop(ridx)
                repo["file_contents"].pop(ridx)
            repo_files_after = list(repo.get("file_paths", []))


        repo["updated_ts"] = get_current_updated_timestamp()
        add_terminal_message(data, f"Deleted '{file_name}' from {owner}/{repo_name}@{branch_name}.", get_current_updated_timestamp())

        result = {
            "success": f"Deleted '{file_name}' from {owner}/{repo_name}@{branch_name}.",
            "repo": f"{owner}/{repo_name}",
            "branch": branch_name,
            "deleted": {
                "file_name": file_name,
                "content": removed_content
            },
            "available_files": list(branch_files)  # remaining files in this branch
        }
        if repo_files_after is not None:
            result["repo_available_files"] = repo_files_after  # remaining repo-level files (main only)

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_file_in_repo",
                "description": "Delete a file from a repository branch; if branch is 'main', also delete from repo-level file paths/contents. Returns remaining files.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner (account/team)."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "branch_name": {"type": "string", "description": "Branch name (e.g., 'main')."},
                        "file_name": {"type": "string", "description": "Path/name of the file to delete."}
                    },
                    "required": ["owner", "repo_name", "branch_name", "file_name"]
                }
            }
        }


class CreateNewBranch(Tool):
    """
    Creates a new branch in a repository.
    - Inputs: owner, repo_name, branch_name, (optional) base_branch.
    - If base_branch is provided (or defaults to repo.default_branch), the new branch's files/contents
      are copied from it (deterministically, no timestamps).
    - Appends a deterministic branch SHA using DB size and branch index: "branch_sha_<len(repos)>_<new_index>".
    - Keeps branch_files and branch_contents aligned with branches.
    - Does NOT modify repo-level file_paths/file_contents (those reflect 'main' updates via other tools).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = kwargs.get("repo_name", "").strip()
        branch_name = kwargs.get("branch_name", "").strip()
        base_branch = kwargs.get("base_branch", "").strip()  # optional

        if not owner or not repo_name or not branch_name:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', and 'branch_name' are required."},
                indent=2
            )

        # Preferred repository access pattern
        repos: List[Dict[str, Any]] = data.get("repositories", [])
        if not isinstance(repos, list):
            return json.dumps(
                {"error": "Invalid database format: expected 'repositories' to be a list."},
                indent=2
            )

        # Locate repo
        repo = next((r for r in repos if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if not repo:
            return json.dumps({"error": f"Repository '{owner}/{repo_name}' not found."}, indent=2)

        branches: List[str] = repo.get("branches", [])
        if branch_name in branches:
            return json.dumps({"error": f"Branch '{branch_name}' already exists."}, indent=2)

        # Resolve base branch (default to repo's default_branch)
        if not base_branch:
            base_branch = repo.get("default_branch", "main")

        if base_branch not in branches:
            return json.dumps(
                {"error": f"Base branch '{base_branch}' not found in '{owner}/{repo_name}'."},
                indent=2
            )

        base_idx = branches.index(base_branch)

        # Ensure per-branch structures exist & are aligned
        branch_files_all: List[List[str]] = repo.setdefault("branch_files", [])
        branch_contents_all: List[List[str]] = repo.setdefault("branch_contents", [])
        while len(branch_files_all) < len(branches):
            branch_files_all.append([])
        while len(branch_contents_all) < len(branches):
            branch_contents_all.append([])

        # Prepare new branch data (copy from base deterministically)
        base_files = branch_files_all[base_idx] if base_idx < len(branch_files_all) else []
        base_contents = branch_contents_all[base_idx] if base_idx < len(branch_contents_all) else []

        new_files = list(base_files) if isinstance(base_files, list) else []
        new_contents = list(base_contents) if isinstance(base_contents, list) else []

        # New branch index will be the current length (appending at the end)
        new_branch_index = len(branches)

        # Append branch name
        branches.append(branch_name)

        # Append aligned arrays for the new branch
        branch_files_all.append(new_files)
        branch_contents_all.append(new_contents)

        # Ensure branch_shas exists and append deterministic SHA
        branch_shas: List[str] = repo.setdefault("branch_shas", [])
        # If branch_shas is shorter than existing branches, pad to align first
        while len(branch_shas) < new_branch_index:
            branch_shas.append("")  # placeholder to align lengths deterministically

        new_branch_sha = get_next_branch_sha(data)
        branch_shas.append(new_branch_sha)

        repo["updated_ts"] = get_current_updated_timestamp()

        # (No repo-level file_paths/file_contents changes here)

        add_terminal_message(data, f"Branch '{branch_name}' created in {owner}/{repo_name} from '{base_branch}'.", get_current_timestamp())

        return json.dumps(
            {
                "success": f"Branch '{branch_name}' created in {owner}/{repo_name} from '{base_branch}'.",
                "repo": f"{owner}/{repo_name}",
                "created_branch": branch_name,
                "base_branch": base_branch,
                "branch_index": new_branch_index,
                "branch_sha": new_branch_sha,
                "branch_file": new_files
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_branch",
                "description": "Create a new branch (optionally from a base branch) with deterministic SHA; copies files/contents from base.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner (account/team)."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "branch_name": {"type": "string", "description": "Name of the new branch to create."},
                        "base_branch": {"type": "string", "description": "Existing branch to copy from (defaults to repo default branch)."}
                    },
                    "required": ["owner", "repo_name", "branch_name"]
                }
            }
        }


class DeleteBranch(Tool):
    """
    Deletes a branch from a repository.
    - Inputs: owner, repo_name, branch_name
    - Refuses to delete the repo's default branch.
    - Removes the branch entry and its aligned entries in branch_files, branch_contents, and branch_shas.
    - Returns details of what was removed and the remaining branches.
    - Deterministic (no timestamps or randomness).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = kwargs.get("repo_name", "").strip()
        branch_name = kwargs.get("branch_name", "").strip()

        if not owner or not repo_name or not branch_name:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', and 'branch_name' are required."},
                indent=2
            )

        # Preferred repository access pattern
        repos: List[Dict[str, Any]] = data.get("repositories", [])
        if not isinstance(repos, list):
            return json.dumps(
                {"error": "Invalid database format: expected 'repositories' to be a list."},
                indent=2
            )

        # Locate repository
        repo = next(
            (r for r in repos if r.get("owner") == owner and r.get("repo_name") == repo_name),
            None
        )
        if not repo:
            return json.dumps(
                {"error": f"Repository '{owner}/{repo_name}' not found."},
                indent=2
            )
    

        branches: List[str] = repo.get("branches", [])
        if branch_name not in branches:
            return json.dumps(
                {"error": f"Branch '{branch_name}' not found in repository '{owner}/{repo_name}'."},
                indent=2
            )

        # Do not allow deleting default branch
        default_branch = repo.get("default_branch", "main")
        if branch_name == default_branch:
            return json.dumps(
                {"error": f"Cannot delete the default branch '{default_branch}'."},
                indent=2
            )

        idx = branches.index(branch_name)

        # Ensure per-branch arrays exist and are aligned to current branches
        branch_files_all: List[List[str]] = repo.setdefault("branch_files", [])
        branch_contents_all: List[List[str]] = repo.setdefault("branch_contents", [])
        branch_shas: List[str] = repo.setdefault("branch_shas", [])


        while len(branch_files_all) < len(branches):
            branch_files_all.append([])
        while len(branch_contents_all) < len(branches):
            branch_contents_all.append([])
        while len(branch_shas) < len(branches):
            branch_shas.append("")

        # Collect removed info (defensive indexing)
        removed_files = branch_files_all[idx] if idx < len(branch_files_all) else []

        # Perform deletions (keep arrays aligned)
        branches.pop(idx)
        if idx < len(branch_files_all):
            branch_files_all.pop(idx)
        if idx < len(branch_contents_all):
            branch_contents_all.pop(idx)
        if idx < len(branch_shas):
            branch_shas.pop(idx)

        updated_ts = get_current_updated_timestamp()
        repo["updated_ts"] = updated_ts

        add_terminal_message(data, f"Branch '{branch_name}' deleted from {owner}/{repo_name}.", get_current_updated_timestamp())

        return json.dumps(
            {
                "success": f"Branch '{branch_name}' deleted from {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "deleted_branch": branch_name,
                "removed_file_count": len(removed_files),
                "remaining_branches": list(branches)
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_branch",
                "description": "Delete a non-default branch from a repository; updates branch_files, branch_contents, and branch_shas accordingly.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner (account/team)."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "branch_name": {"type": "string", "description": "Branch name to delete."}
                    },
                    "required": ["owner", "repo_name", "branch_name"]
                }
            }
        }


# class MergeBranch(Tool):
#     """
#     Merges source_branch_name into target_branch_name for a repository.
#     - Deterministic merge: source files overwrite target on conflicts by default.
#     - Keeps per-branch arrays (branch_files/branch_contents/branch_shas) aligned.
#     - If target is the repo's default branch, repo-level file_paths/file_contents are synced to target.
#     """

#     @staticmethod
#     def invoke(data: Dict[str, Any], **kwargs) -> str:
#         owner = kwargs.get("owner", "").strip()
#         repo_name = kwargs.get("repo_name", "").strip()
#         source_branch_name = kwargs.get("source_branch_name", "").strip()
#         target_branch_name = kwargs.get("target_branch_name", "").strip()
#         conflict_strategy = kwargs.get("conflict_strategy", "source_wins").strip()  # 'source_wins' | 'target_wins'

#         if not owner or not repo_name or not source_branch_name or not target_branch_name:
#             return json.dumps(
#                 {"error": "Parameters 'owner', 'repo_name', 'source_branch_name', and 'target_branch_name' are required."},
#                 indent=2
#             )
#         if conflict_strategy not in ("source_wins", "target_wins"):
#             return json.dumps({"error": "conflict_strategy must be 'source_wins' or 'target_wins'."}, indent=2)
#         if source_branch_name == target_branch_name:
#             return json.dumps({"error": "source_branch_name and target_branch_name must be different."}, indent=2)

#         # Preferred repository access pattern
#         repos: List[Dict[str, Any]] = data.get("repositories", [])
#         if not isinstance(repos, list):
#             return json.dumps({"error": "Invalid database format: expected 'repositories' to be a list."}, indent=2)

#         # Find repo
#         repo = next((r for r in repos if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
#         if not repo:
#             return json.dumps({"error": f"Repository '{owner}/{repo_name}' not found."}, indent=2)

#         branches: List[str] = repo.get("branches", [])
#         if source_branch_name not in branches:
#             return json.dumps({"error": f"Source branch '{source_branch_name}' not found."}, indent=2)
#         if target_branch_name not in branches:
#             return json.dumps({"error": f"Target branch '{target_branch_name}' not found."}, indent=2)

#         src_idx = branches.index(source_branch_name)
#         tgt_idx = branches.index(target_branch_name)

#         # Ensure per-branch structures exist & align
#         branch_files_all: List[List[str]] = repo.setdefault("branch_files", [])
#         branch_contents_all: List[List[str]] = repo.setdefault("branch_contents", [])
#         branch_shas: List[str] = repo.setdefault("branch_shas", [])

#         ensure_align(branch_files_all, len(branches))
#         ensure_align(branch_contents_all, len(branches))
#         ensure_len(branch_shas, len(branches), "")

#         src_files = branch_files_all[src_idx]
#         src_contents = branch_contents_all[src_idx]
#         tgt_files = branch_files_all[tgt_idx]
#         tgt_contents = branch_contents_all[tgt_idx]

#         # Merge
#         new_files, new_contents, added_files, overwritten_files = merge_files(
#             src_files, src_contents, tgt_files, tgt_contents, conflict_strategy
#         )

#         # Write back merged target branch
#         branch_files_all[tgt_idx] = new_files
#         branch_contents_all[tgt_idx] = new_contents

#         # Update target branch SHA deterministically
#         new_sha = get_next_branch_sha(data)
#         branch_shas[tgt_idx] = new_sha

#         repo["updated_ts"] = get_current_updated_timestamp()

#         # If target is default branch, sync repo-level files/contents to target branch
#         default_branch = repo.get("default_branch", "main")
#         if target_branch_name == default_branch:
#             repo["file_paths"] = list(new_files)
#             repo["file_contents"] = list(new_contents)

#         add_terminal_message(data, f"Merged '{source_branch_name}' into '{target_branch_name}' for {owner}/{repo_name}.", get_current_updated_timestamp())

#         return json.dumps(
#             {
#                 "success": f"Merged '{source_branch_name}' into '{target_branch_name}' for {owner}/{repo_name}.",
#                 "repo": f"{owner}/{repo_name}",
#                 "source_branch": source_branch_name,
#                 "target_branch": target_branch_name,
#                 "conflict_strategy": conflict_strategy,
#                 "added_files": added_files,
#                 "overwritten_files": overwritten_files,
#                 "target_branch_file_count": len(new_files),
#                 "target_branch_sha": new_sha
#             },
#             indent=2
#         )

#     @staticmethod
#     def get_info() -> Dict[str, Any]:
#         return {
#             "type": "function",
#             "function": {
#                 "name": "merge_branch",
#                 "description": "Merge source_branch_name into target_branch_name; source wins by default on conflicts; syncs repo files if target is default branch.",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "owner": {"type": "string", "description": "Repository owner (account/team)."},
#                         "repo_name": {"type": "string", "description": "Repository name."},
#                         "source_branch_name": {"type": "string", "description": "Branch to merge from."},
#                         "target_branch_name": {"type": "string", "description": "Branch to merge into."},
#                         "conflict_strategy": {"type": "string", "enum": ["source_wins", "target_wins"], "description": "Conflict resolution policy (default: source_wins)."}
#                     },
#                     "required": ["owner", "repo_name", "source_branch_name", "target_branch_name"]
#                 }
#             }
#         }

class MergeBranch(Tool):
    """
    Replace the target branch's file list with the source branch's file list (source snapshot wins).
    - Inputs: owner, repo_name, source_branch_name, target_branch_name
    - Behavior:
        * Validates repo and branch existence; rejects self-merge.
        * Sets target branch files/contents to EXACT copies of source branch files/contents.
          (Any previous files on the target branch are discarded.)
        * If target is the default branch, mirrors to repo-level file_paths/file_contents.
        * Assigns a new deterministic SHA to the target branch (via get_next_branch_sha(data)).
        * Updates repo['updated_ts'] via get_current_updated_timestamp().
        * Appends a terminal log entry via add_terminal_message(data, msg, timestamp).
    - Deterministic and idempotent for repeated runs on unchanged source.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = (kwargs.get("owner") or "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("reponame") or "").strip()
        source_branch_name = (kwargs.get("source_branch_name") or "").strip()
        target_branch_name = (kwargs.get("target_branch_name") or "").strip()

        if not owner or not repo_name or not source_branch_name or not target_branch_name:
            return json.dumps(
                {"error": "Required: owner, repo_name, source_branch_name, target_branch_name."},
                indent=2
            )
        if source_branch_name == target_branch_name:
            return json.dumps(
                {"error": "source_branch_name and target_branch_name must differ."},
                indent=2
            )

        # Load repositories DB
        repos: List[Dict[str, Any]] = data.get("repositories", [])
        if not isinstance(repos, list):
            return json.dumps({"error": "Invalid database: 'repositories' must be a list."}, indent=2)

        # Locate repository
        repo = next((r for r in repos if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if repo is None:
            return json.dumps({"error": f"Repository '{owner}/{repo_name}' not found."}, indent=2)

        branches: List[str] = repo.get("branches", [])
        if source_branch_name not in branches:
            return json.dumps({"error": f"Source branch '{source_branch_name}' not found."}, indent=2)
        if target_branch_name not in branches:
            return json.dumps({"error": f"Target branch '{target_branch_name}' not found."}, indent=2)

        src_idx = branches.index(source_branch_name)
        tgt_idx = branches.index(target_branch_name)

        # Ensure per-branch arrays are present and padded
        branch_files_all: List[List[str]] = repo.setdefault("branch_files", [])
        branch_contents_all: List[List[str]] = repo.setdefault("branch_contents", [])
        branch_shas: List[str] = repo.setdefault("branch_shas", [])

        while len(branch_files_all)    < len(branches): branch_files_all.append([])
        while len(branch_contents_all) < len(branches): branch_contents_all.append([])
        while len(branch_shas)        < len(branches): branch_shas.append("")

        # Source snapshot
        src_files = list(branch_files_all[src_idx])
        src_contents_full = list(branch_contents_all[src_idx])
        # Normalize content length to file list length
        normalized_src_contents: List[str] = []
        for i, _path in enumerate(src_files):
            normalized_src_contents.append(src_contents_full[i] if i < len(src_contents_full) else "")

        # Replace target with source snapshot
        branch_files_all[tgt_idx] = list(src_files)
        branch_contents_all[tgt_idx] = list(normalized_src_contents)

        # If target is default branch, mirror to repo-level files
        default_branch = repo.get("default_branch", "main")
        if target_branch_name == default_branch:
            repo["file_paths"] = list(src_files)
            repo["file_contents"] = list(normalized_src_contents)

        # Deterministic timestamp and new target SHA
        new_ts = get_current_updated_timestamp()
        repo["updated_ts"] = new_ts

        new_target_sha = get_next_merge_sha(data)  # e.g., "branch_sha_<N>"

        branch_shas[tgt_idx] = new_target_sha

        # Terminal log
        add_terminal_message(
            data,
            f"Merged '{source_branch_name}' into '{target_branch_name}' for {owner}/{repo_name} with SHA {new_target_sha}.",
            new_ts
        )

        return json.dumps(
            {
                "success": f"Merged '{source_branch_name}' into '{target_branch_name}' for {owner}/{repo_name} with SHA {new_target_sha}.",
                "repo": f"{owner}/{repo_name}",
                "source_branch": source_branch_name,
                "target_branch": target_branch_name,
                "target_branch_file_count": len(src_files),
                "target_branch_sha": new_target_sha,
                "updated_ts": new_ts
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "merge_branch",
                "description": "Replace target branch files/contents with a snapshot of source (source snapshot wins); mirrors to repo-level if target is default; assigns new deterministic SHA to target; updates repo updated_ts; logs a terminal entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: reponame)."},
                        "source_branch_name": {"type": "string", "description": "Branch to copy FROM."},
                        "target_branch_name": {"type": "string", "description": "Branch to replace (copy INTO)."}
                    },
                    "required": ["owner", "repo_name", "source_branch_name", "target_branch_name"]
                }
            }
        }


class InitialCommit(Tool):
    """
    Adds a new commit entry to the commits DB for owner/repo_name/branch_name.
    - Creates the repo record if missing.
    - Creates the branch bucket if missing.
    - Uses deterministic commit SHA ('commit_sha_<total>') and timestamp (max(existing)+1min).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = kwargs.get("repo_name", "").strip()
        branch_name = kwargs.get("branch_name", "").strip()
        commit_message = kwargs.get("commit_message", "").strip()
        commit_author = kwargs.get("commit_author", "").strip()

        if not owner or not repo_name or not branch_name or not commit_message or not commit_author:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', 'branch_name', 'commit_message', and 'commit_author' are required."},
                indent=2
            )

        # Load commits DB (supports either {"commits": [...]} or a top-level list)
        commits_db = data.get("commits", [])
        if isinstance(commits_db, list):
            pass
        elif isinstance(data, list):
            commits_db = data
        else:
            return json.dumps(
                {"error": "Invalid database format: expected a list or a dict with 'commits'."},
                indent=2
            )

        # Find or create the repo record
        rec = next((r for r in commits_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            rec = {
                "owner": owner,
                "repo_name": repo_name,
                "branch_names": [],
                "commit_shas": [],
                "commit_messages": [],
                "commit_authors": [],
                "commit_timestamps": []
            }
            commits_db.append(rec)

        branch_names: List[str] = rec.get("branch_names", [])
        commit_shas: List[List[str]] = rec.get("commit_shas", [])
        commit_messages: List[List[str]] = rec.get("commit_messages", [])
        commit_authors: List[List[str]] = rec.get("commit_authors", [])
        commit_timestamps: List[List[str]] = rec.get("commit_timestamps", [])

        # Ensure branch exists and arrays are aligned
        if branch_name not in branch_names:
            branch_names.append(branch_name)
            commit_shas.append([])
            commit_messages.append([])
            commit_authors.append([])
            commit_timestamps.append([])

        idx = branch_names.index(branch_name)

        # Deterministic commit fields
        new_sha = get_next_commit_sha(data)
        new_ts = get_current_timestamp()

        # Append new commit
        commit_shas[idx].append(new_sha)
        commit_messages[idx].append(commit_message)
        commit_authors[idx].append(commit_author)
        commit_timestamps[idx].append(new_ts)

        # Write back (in case keys were missing initially)
        rec["branch_names"] = branch_names
        rec["commit_shas"] = commit_shas
        rec["commit_messages"] = commit_messages
        rec["commit_authors"] = commit_authors
        rec["commit_timestamps"] = commit_timestamps

        add_terminal_message(data, f"Initial commit added to {owner}/{repo_name}@{branch_name}.", get_current_timestamp())

        return json.dumps(
            {
                "success": f"Initial commit added to {owner}/{repo_name}@{branch_name}.",
                "commit": {
                    "sha": new_sha,
                    "message": commit_message,
                    "author": commit_author,
                    "timestamp": new_ts
                },
                "branch_commit_count": len(commit_shas[idx])
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "initial_commit",
                "description": "Add a new commit to commits DB (creates repo/branch buckets if needed) with deterministic SHA and timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner (account/team)."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "branch_name": {"type": "string", "description": "Branch name to commit to."},
                        "commit_message": {"type": "string", "description": "Commit message."},
                        "commit_author": {"type": "string", "description": "Author username for the commit."}
                    },
                    "required": ["owner", "repo_name", "branch_name", "commit_message", "commit_author"]
                }
            }
        }


class MakeCommit(Tool):
    """
    Append a new commit to an existing commits entry for (owner/repo_name/branch_name).
    - Errors if repo or branch bucket doesn't exist (use InitialCommit first).
    - Deterministic commit SHA ('commit_sha_<total>') and timestamp (max(existing)+1min).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = kwargs.get("repo_name", "").strip()
        branch_name = kwargs.get("branch_name", "").strip()
        commit_message = kwargs.get("commit_message", "").strip()
        commit_author = kwargs.get("commit_author", "").strip()

        if not owner or not repo_name or not branch_name or not commit_message or not commit_author:
            return json.dumps({
                "error": "Parameters 'owner', 'repo_name', 'branch_name', 'commit_message', and 'commit_author' are required."
            })

        # Load commits DB (prefer dict["commits"], fallback to top-level list)
        commits_db = None
        if isinstance(data, dict):
            commits_db = data.get("commits", [])
        elif isinstance(data, list):
            commits_db = data
        else:
            return json.dumps({"error": "Invalid database format for commits."})

        if not isinstance(commits_db, list):
            return json.dumps({"error": "Invalid commits store: expected a list."})

        # Find existing repo record
        rec = next((r for r in commits_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No commits entry for {owner}/{repo_name}. Use InitialCommit first."})

        branch_names: List[str] = rec.get("branch_names", [])
        commit_shas: List[List[str]] = rec.get("commit_shas", [])
        commit_messages: List[List[str]] = rec.get("commit_messages", [])
        commit_authors: List[List[str]] = rec.get("commit_authors", [])
        commit_timestamps: List[List[str]] = rec.get("commit_timestamps", [])

        if branch_name not in branch_names:
            return json.dumps({"error": f"No commit bucket for branch '{branch_name}' in {owner}/{repo_name}. Use InitialCommit first."})

        idx = branch_names.index(branch_name)

        # Defensive alignment (ensure branch arrays exist)
        while len(commit_shas) <= idx: commit_shas.append([])
        while len(commit_messages) <= idx: commit_messages.append([])
        while len(commit_authors) <= idx: commit_authors.append([])
        while len(commit_timestamps) <= idx: commit_timestamps.append([])

        # Deterministic fields
        new_sha = get_next_commit_sha(data)         # <- called
        new_ts = get_current_updated_timestamp()

        # Append commit
        commit_shas[idx].append(new_sha)
        commit_messages[idx].append(commit_message)
        commit_authors[idx].append(commit_author)
        commit_timestamps[idx].append(new_ts)

        # Write back (in case keys were missing initially)
        rec["branch_names"] = branch_names
        rec["commit_shas"] = commit_shas
        rec["commit_messages"] = commit_messages
        rec["commit_authors"] = commit_authors
        rec["commit_timestamps"] = commit_timestamps

        add_terminal_message(data, f"Commit added to {owner}/{repo_name}@{branch_name}.", new_ts)

        return json.dumps({
            "success": f"Commit added to {owner}/{repo_name}@{branch_name}.",
            "commit": {
                "sha": new_sha,
                "message": commit_message,
                "author": commit_author,
                "timestamp": new_ts
            },
            "branch_commit_count": len(commit_shas[idx])
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "make_commit",
                "description": "Append a new commit to an existing commits entry (owner/repo_name/branch_name) with deterministic SHA and timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner (account/team)."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "branch_name": {"type": "string", "description": "Branch name to commit to."},
                        "commit_message": {"type": "string", "description": "Commit message."},
                        "commit_author": {"type": "string", "description": "Author username for the commit."}
                    },
                    "required": ["owner", "repo_name", "branch_name", "commit_message", "commit_author"]
                }
            }
        }


class CreatePullRequest(Tool):
    """
    Creates a new pull request entry.
    Inputs: owner, repo_name, pr_title, pr_body, head_branch_name, base_branch_name, head_sha, pr_files
    Behavior:
      - Creates/locates the repo record in the PR DB.
      - Appends aligned fields (titles, bodies, states, branches, shas, flags, files, comments, reviewers, timestamps).
      - PR number = max(all pr_numbers) + 1 (global uniqueness).
      - created_ts/updated_ts = deterministic next timestamp.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        pr_title = (kwargs.get("pr_title") or kwargs.get("pr_titile") or "").strip()
        pr_body = (kwargs.get("pr_body") or "").strip()
        head_branch_name = (kwargs.get("head_branch_name") or kwargs.get("head_branch") or "").strip()
        base_branch_name = (kwargs.get("base_branch_name") or kwargs.get("base_branch") or "").strip()
        head_sha = (kwargs.get("head_sha") or kwargs.get("head_sha_value") or "").strip()
        pr_files_input = kwargs.get("pr_files", [])

        if not owner or not repo_name or not pr_title or not head_branch_name or not base_branch_name or not head_sha:
            return json.dumps({
                "error": "Required: owner, repo_name, pr_title, head_branch_name, base_branch_name, head_sha."
            }, indent=2)

        if not isinstance(pr_files_input, list) or not all(isinstance(x, str) for x in pr_files_input):
            return json.dumps({"error": "pr_files must be a list of filenames (strings)."}, indent=2)

        # Load PR DB (supports dict with 'pull_requests' or top-level list)
        pr_db = data.get("pull_requests", [])


        # Find or create repo bucket
        rec = next((r for r in pr_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            rec = {
                "owner": owner,
                "repo_name": repo_name,
                "pr_numbers": [],
                "pr_titles": [],
                "pr_bodies": [],
                "pr_states": [],
                "head_branches": [],
                "base_branches": [],
                "head_shas": [],
                "mergeable_flags": [],
                "merged_flags": [],
                "pr_files": [],
                "pr_comments": [],
                "pr_comment_users": [],
                "reviewers": [],
                "review_states": [],
                "review_events": [],
                "created_ts": [],
                "updated_ts": []
            }
            pr_db.append(rec)

        # Deterministic number & timestamps
        new_pr_number = get_next_pr_number(data)
        new_ts = get_current_timestamp()

        # Ensure arrays exist
        rec.setdefault("pr_numbers", [])
        rec.setdefault("pr_titles", [])
        rec.setdefault("pr_bodies", [])
        rec.setdefault("pr_states", [])
        rec.setdefault("head_branches", [])
        rec.setdefault("base_branches", [])
        rec.setdefault("head_shas", [])
        rec.setdefault("mergeable_flags", [])
        rec.setdefault("merged_flags", [])
        rec.setdefault("pr_files", [])
        rec.setdefault("pr_comments", [])
        rec.setdefault("pr_comment_users", [])
        rec.setdefault("reviewers", [])
        rec.setdefault("review_states", [])
        rec.setdefault("review_events", [])
        rec.setdefault("created_ts", [])
        rec.setdefault("updated_ts", [])

        # Append aligned fields
        rec["pr_numbers"].append(new_pr_number)
        rec["pr_titles"].append(pr_title)
        rec["pr_bodies"].append(pr_body)
        rec["pr_states"].append("open")
        rec["head_branches"].append(head_branch_name)
        rec["base_branches"].append(base_branch_name)
        rec["head_shas"].append(head_sha)
        rec["mergeable_flags"].append(True)
        rec["merged_flags"].append(False)

        # DB shape expects a nested list per PR: [ [ "fileA", "fileB" ] ]
        rec["pr_files"].append([list(pr_files_input)])

        # Empty placeholders for comments/reviews (match nested shapes)
        rec["pr_comments"].append([[]])
        rec["pr_comment_users"].append([[]])
        rec["reviewers"].append([[]])
        rec["review_states"].append([[]])
        rec["review_events"].append([[]])

        rec["created_ts"].append(new_ts)
        rec["updated_ts"].append(new_ts)

        add_terminal_message(data, f"Pull request #{new_pr_number} created for {owner}/{repo_name}.", get_current_timestamp())

        return json.dumps({
            "success": f"Pull request #{new_pr_number} created for {owner}/{repo_name}.",
            "pull_request": {
                "number": new_pr_number,
                "title": pr_title,
                "body": pr_body,
                "state": "open",
                "base": base_branch_name,
                "head": head_branch_name,
                "head_sha": head_sha,
                "files": pr_files_input,
                "created_ts": new_ts,
                "updated_ts": new_ts
            }
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_pull_request",
                "description": "Create a new pull request entry with deterministic PR number and timestamps; creates repo bucket if needed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "pr_title": {"type": "string", "description": "Pull request title."},
                        "pr_body": {"type": "string", "description": "Pull request description/body."},
                        "head_branch_name": {"type": "string", "description": "Source (head) branch name."},
                        "base_branch_name": {"type": "string", "description": "Target (base) branch name."},
                        "head_sha": {"type": "string", "description": "Head commit SHA for the PR."},
                        "pr_files": {"type": "array", "items": {"type": "string"}, "description": "List of file paths included in the PR."}
                    },
                    "required": ["owner", "repo_name", "pr_title", "pr_body", "head_branch_name", "base_branch_name", "head_sha", "pr_files"]
                }
            }
        }


class GetPRDetails(Tool):
    """
    Returns all details for a pull request identified by (owner, repo_name, pr_number).
    - Accepts 'pr_number' (preferred) or 'prnumber' as an alias.
    - Reads from data.get('pull_requests', []) or top-level list.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        # Support both 'pr_number' and 'prnumber'
        pr_number_raw = kwargs.get("pr_number", kwargs.get("prnumber", None))

        if not owner or not repo_name or pr_number_raw is None:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', and 'pr_number' are required."},
                indent=2
            )

        # Normalize pr_number to int
        try:
            pr_number = int(pr_number_raw)
        except Exception:
            return json.dumps(
                {"error": "pr_number must be an integer."},
                indent=2
            )

        # Load PR DB (supports dict with 'pull_requests' or a top-level list)
        pr_db = data.get("pull_requests", [])


        if not isinstance(pr_db, list):
            return json.dumps(
                {"error": "Invalid pull requests DB: expected a list."},
                indent=2
            )

        # Find the repo bucket
        rec = next((r for r in pr_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps(
                {"error": f"No pull requests found for repository '{owner}/{repo_name}'."},
                indent=2
            )

        pr_numbers: List[int] = rec.get("pr_numbers", [])
        if pr_number not in pr_numbers:
            return json.dumps(
                {"error": f"PR #{pr_number} not found for '{owner}/{repo_name}'."},
                indent=2
            )

        idx = pr_numbers.index(pr_number)

        # Helper to safely fetch an indexed value from a list, else None
        def _get_at(lst_name: str):
            lst = rec.get(lst_name, [])
            return lst[idx] if idx < len(lst) else None

        # Extract all relevant fields (defensive on lengths)
        details = {
            "number": pr_number,
            "title": _get_at("pr_titles"),
            "body": _get_at("pr_bodies"),
            "state": _get_at("pr_states"),
            "base_branch": _get_at("base_branches"),
            "head_branch": _get_at("head_branches"),
            "head_sha": _get_at("head_shas"),
            "mergeable": _get_at("mergeable_flags"),
            "merged": _get_at("merged_flags"),
            # Files/comments/reviews are often nested; return as stored in DB
            "files": _get_at("pr_files"),
            "comments": _get_at("pr_comments"),
            "comment_users": _get_at("pr_comment_users"),
            "reviewers": _get_at("reviewers"),
            "review_states": _get_at("review_states"),
            "review_events": _get_at("review_events"),
            "created_ts": _get_at("created_ts"),
            "updated_ts": _get_at("updated_ts"),
        }

        return json.dumps(details, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pr_details",
                "description": "Fetch all stored details for a pull request (owner, repo_name, pr_number).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "pr_number": {"type": "integer", "description": "Pull request number."}
                    },
                    "required": ["owner", "repo_name", "pr_number"]
                }
            }
        }


class ListOfPRForRepo(Tool):
    """
    Lists pull requests for a repository.
    - Inputs: owner, repo_name, (optional) state in {'open','closed','merged'}
    - Returns an array of PR summaries (number, title, state, branches, head_sha, timestamps, files).
    - Reads from data.get('pull_requests', []) or top-level list.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        state_filter = (kwargs.get("state") or "").strip().lower()  # optional

        if not owner or not repo_name:
            return json.dumps(
                {"error": "Parameters 'owner' and 'repo_name' are required."},
                indent=2
            )

        if state_filter and state_filter not in {"open", "closed", "merged"}:
            return json.dumps(
                {"error": "Invalid 'state'. Use one of: 'open', 'closed', 'merged'."},
                indent=2
            )

        # Load PR DB (supports dict with 'pull_requests' or a top-level list)
        pr_db = data.get("pull_requests", [])
        

        if not isinstance(pr_db, list):
            return json.dumps({"error": "Invalid pull requests DB: expected a list."}, indent=2)

        # Find the repo bucket
        rec = next((r for r in pr_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps(
                {"error": f"No pull requests found for repository '{owner}/{repo_name}'."},
                indent=2
            )

        pr_numbers: List[int] = rec.get("pr_numbers", [])

        def get_at(name: str, i: int):
            arr = rec.get(name, [])
            return arr[i] if i < len(arr) else None

        # Build list of (number, index) and sort by PR number ascending
        indexed: List[tuple] = [(num, i) for i, num in enumerate(pr_numbers)]
        indexed.sort(key=lambda t: t[0])

        results: List[Dict[str, Any]] = []
        for num, idx in indexed:
            pr_state = get_at("pr_states", idx)
            merged_flag = bool(get_at("merged_flags", idx))
            # If a state filter is set, apply it
            if state_filter:
                if state_filter == "merged" and not merged_flag:
                    continue
                if state_filter in {"open", "closed"} and pr_state != state_filter:
                    continue

            files_entry = get_at("pr_files", idx)  # stored shape is typically [ [ "fileA", ... ] ]
            pr_summary = {
                "number": num,
                "title": get_at("pr_titles", idx),
                "body": get_at("pr_bodies", idx),
                "state": pr_state,
                "merged": merged_flag,
                "mergeable": get_at("mergeable_flags", idx),
                "base_branch": get_at("base_branches", idx),
                "head_branch": get_at("head_branches", idx),
                "head_sha": get_at("head_shas", idx),
                "files": files_entry,
                "created_ts": get_at("created_ts", idx),
                "updated_ts": get_at("updated_ts", idx),
            }
            results.append(pr_summary)

        return json.dumps(
            {
                "owner": owner,
                "repo_name": repo_name,
                "count": len(results),
                "pull_requests": results
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_of_pr_for_repo",
                "description": "List pull requests for a repository, optionally filtered by state.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "state": {
                            "type": "string",
                            "enum": ["open", "closed", "merged"],
                            "description": "Optional filter by PR state."
                        }
                    },
                    "required": ["owner", "repo_name"]
                }
            }
        }
    

class AddPullRequestComment(Tool):
    """
    Adds a comment to a pull request for (owner, repo_name, pr_number).
    - Appends the comment to the first thread of the PR (creates it if missing).
    - Mirrors the comment author in pr_comment_users with the same indices.
    - Updates reviewer state/event for the comment_user:
        * Sets review_state to input value
        * Sets review_event to the same value
        * Adds the reviewer if not already present
    - Updates the PR's updated_ts (via get_current_updated_timestamp()).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        pr_number_raw = kwargs.get("pr_number", kwargs.get("prnumber", None))
        comment = (kwargs.get("comment") or kwargs.get("comment_body") or "").strip()
        comment_user = (kwargs.get("comment_user") or kwargs.get("user") or "").strip()
        review_state = (kwargs.get("review_state") or "").strip()

        if not owner or not repo_name or pr_number_raw is None or not comment or not comment_user or not review_state:
            return json.dumps(
                {"error": "Required: owner, repo_name, pr_number, comment, comment_user, review_state."},
                indent=2
            )

        try:
            pr_number = int(pr_number_raw)
        except Exception:
            return json.dumps({"error": "pr_number must be an integer."}, indent=2)

        # Load PR DB (expects list at data['pull_requests'])
        pr_db = data.get("pull_requests", [])
        if not isinstance(pr_db, list):
            return json.dumps({"error": "Invalid pull requests DB: expected a list."}, indent=2)

        # Find repo bucket
        rec = next((r for r in pr_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No pull requests found for '{owner}/{repo_name}'."}, indent=2)

        pr_numbers = rec.get("pr_numbers", [])
        if pr_number not in pr_numbers:
            return json.dumps({"error": f"PR #{pr_number} not found for '{owner}/{repo_name}'."}, indent=2)
        idx = pr_numbers.index(pr_number)

        # ---- Ensure comments/users structures exist (thread 0) ----
        rec.setdefault("pr_comments", [])
        rec.setdefault("pr_comment_users", [])
        while len(rec["pr_comments"]) <= idx: rec["pr_comments"].append([])
        while len(rec["pr_comment_users"]) <= idx: rec["pr_comment_users"].append([])

        if not isinstance(rec["pr_comments"][idx], list): rec["pr_comments"][idx] = []
        if not isinstance(rec["pr_comment_users"][idx], list): rec["pr_comment_users"][idx] = []

        if len(rec["pr_comments"][idx]) == 0: rec["pr_comments"][idx].append([])
        if len(rec["pr_comment_users"][idx]) == 0: rec["pr_comment_users"][idx].append([])

        thread_idx = 0
        comments_thread = rec["pr_comments"][idx][thread_idx]
        users_thread = rec["pr_comment_users"][idx][thread_idx]
        if not isinstance(comments_thread, list):
            comments_thread = []
            rec["pr_comments"][idx][thread_idx] = comments_thread
        if not isinstance(users_thread, list):
            users_thread = []
            rec["pr_comment_users"][idx][thread_idx] = users_thread

        comments_thread.append(comment)
        users_thread.append(comment_user)
        comment_index = len(comments_thread) - 1

        # ---- Ensure reviewers/state/event structures exist (group 0) ----
        rec.setdefault("reviewers", [])
        rec.setdefault("review_states", [])
        rec.setdefault("review_events", [])
        while len(rec["reviewers"]) <= idx: rec["reviewers"].append([])
        while len(rec["review_states"]) <= idx: rec["review_states"].append([])
        while len(rec["review_events"]) <= idx: rec["review_events"].append([])

        if not isinstance(rec["reviewers"][idx], list): rec["reviewers"][idx] = []
        if not isinstance(rec["review_states"][idx], list): rec["review_states"][idx] = []
        if not isinstance(rec["review_events"][idx], list): rec["review_events"][idx] = []

        if len(rec["reviewers"][idx]) == 0: rec["reviewers"][idx].append([])
        if len(rec["review_states"][idx]) == 0: rec["review_states"][idx].append([])
        if len(rec["review_events"][idx]) == 0: rec["review_events"][idx].append([])

        reviewers_list = rec["reviewers"][idx][0]
        states_container = rec["review_states"][idx][0]
        events_container = rec["review_events"][idx][0]

        # ---- Normalize to per-reviewer histories (lists of lists) ----
        # reviewers_list: List[str]
        # states_hist: List[List[str]], events_hist: List[List[str]]
        if not isinstance(reviewers_list, list):
            reviewers_list = []
        # States
        if isinstance(states_container, list) and all(isinstance(x, list) for x in states_container):
            states_hist = states_container
        elif isinstance(states_container, list):
            # old shape: per-reviewer single strings
            states_hist = [[x] if isinstance(x, str) and x != "" else [] for x in states_container]
        else:
            states_hist = []
        # Events
        if isinstance(events_container, list) and all(isinstance(x, list) for x in events_container):
            events_hist = events_container
        elif isinstance(events_container, list):
            events_hist = [[x] if isinstance(x, str) and x != "" else [] for x in events_container]
        else:
            events_hist = []

        # Align lengths with reviewers
        while len(states_hist) < len(reviewers_list): states_hist.append([])
        while len(events_hist) < len(reviewers_list): events_hist.append([])
        if len(states_hist) > len(reviewers_list): states_hist = states_hist[:len(reviewers_list)]
        if len(events_hist) > len(reviewers_list): events_hist = events_hist[:len(reviewers_list)]

        # Ensure reviewer exists; then APPEND review_state/event
        if comment_user in reviewers_list:
            ridx = reviewers_list.index(comment_user)
        else:
            reviewers_list.append(comment_user)
            states_hist.append([])
            events_hist.append([])
            ridx = len(reviewers_list) - 1

        states_hist[ridx].append(review_state)
        events_hist[ridx].append(review_state)  # event mirrors state

        # Persist back
        rec["reviewers"][idx][0] = reviewers_list
        rec["review_states"][idx][0] = states_hist
        rec["review_events"][idx][0] = events_hist

        # ---- Bump updated_ts deterministically via env helper ----
        rec.setdefault("updated_ts", [])
        while len(rec["updated_ts"]) <= idx: rec["updated_ts"].append(None)
        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        add_terminal_message(data, f"Comment added to PR #{pr_number} for {owner}/{repo_name}; review state/event appended.", get_current_updated_timestamp())

        return json.dumps(
            {
                "success": f"Comment added to PR #{pr_number} for {owner}/{repo_name}; review state/event appended.",
                "repo": f"{owner}/{repo_name}",
                "pr_number": pr_number,
                "thread_index": thread_idx,
                "comment_index": comment_index,
                "comment": comment,
                "comment_user": comment_user,
                "appended_review_state": review_state,
                "appended_review_event": review_state,
                "updated_ts": new_updated_ts
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_pull_request_comment",
                "description": "Add a PR comment and set the comment_user's review_state and review_event (event mirrors state); bumps updated_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "pr_number": {"type": "integer", "description": "Pull request number."},
                        "comment": {"type": "string", "description": "Comment text to add."},
                        "comment_user": {"type": "string", "description": "Username of the commenter (reviewer)."},
                        "review_state": {"type": "string", "description": "New review state; review_event will match this value."}
                    },
                    "required": ["owner", "repo_name", "pr_number", "comment", "comment_user", "review_state"]
                }
            }
        }


class AssignPullRequestReviewers(Tool):
    """
    Assign reviewers to a pull request.
    - Inputs: owner, repo_name, pr_number, reviewers (list[str])
    - Adds new reviewers (no duplicates) and aligns review_states/review_events.
    - Bumps PR updated_ts deterministically (max existing + 1 minute).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        pr_number_raw = kwargs.get("pr_number", kwargs.get("prnumber", None))
        reviewers_input = kwargs.get("reviewers", None)

        if not owner or not repo_name or pr_number_raw is None or reviewers_input is None:
            return json.dumps(
                {"error": "Required: owner, repo_name, pr_number, reviewers."},
                indent=2
            )

        # Normalize pr_number
        try:
            pr_number = int(pr_number_raw)
        except Exception:
            return json.dumps({"error": "pr_number must be an integer."}, indent=2)

        # Validate reviewers list
        if (not isinstance(reviewers_input, list)
            or any((not isinstance(u, str) or not u.strip()) for u in reviewers_input)):
            return json.dumps({"error": "reviewers must be a non-empty list of non-empty strings."}, indent=2)

        reviewers_input = [u.strip() for u in reviewers_input if isinstance(u, str) and u.strip()]
        if not reviewers_input:
            return json.dumps({"error": "reviewers cannot be empty."}, indent=2)

        # Load PR DB (supports dict with 'pull_requests' or top-level list)
        pr_db = data.get("pull_requests", [])

        if not isinstance(pr_db, list):
            return json.dumps({"error": "Invalid pull requests DB: expected a list."}, indent=2)

        # Find repo bucket
        rec = next((r for r in pr_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No pull requests found for '{owner}/{repo_name}'."}, indent=2)

        pr_numbers: List[int] = rec.get("pr_numbers", [])
        if pr_number not in pr_numbers:
            return json.dumps({"error": f"PR #{pr_number} not found for '{owner}/{repo_name}'."}, indent=2)
        idx = pr_numbers.index(pr_number)

        # Ensure nested arrays exist and are properly shaped
        rec.setdefault("reviewers", [])
        rec.setdefault("review_states", [])
        rec.setdefault("review_events", [])
        rec.setdefault("updated_ts", [])
        rec.setdefault("created_ts", [])

        while len(rec["reviewers"]) <= idx: rec["reviewers"].append([])
        while len(rec["review_states"]) <= idx: rec["review_states"].append([])
        while len(rec["review_events"]) <= idx: rec["review_events"].append([])
        while len(rec["updated_ts"]) <= idx: rec["updated_ts"].append(None)

        # Each PR keeps reviewers/states/events as a list of groups; ensure first group exists
        if not isinstance(rec["reviewers"][idx], list): rec["reviewers"][idx] = []
        if not isinstance(rec["review_states"][idx], list): rec["review_states"][idx] = []
        if not isinstance(rec["review_events"][idx], list): rec["review_events"][idx] = []

        if len(rec["reviewers"][idx]) == 0: rec["reviewers"][idx].append([])
        if len(rec["review_states"][idx]) == 0: rec["review_states"][idx].append([])
        if len(rec["review_events"][idx]) == 0: rec["review_events"][idx].append([])

        reviewers_list: List[str] = rec["reviewers"][idx][0]
        states_list: List[str] = rec["review_states"][idx][0]
        events_list: List[str] = rec["review_events"][idx][0]

        if not isinstance(reviewers_list, list): 
            reviewers_list = []
            rec["reviewers"][idx][0] = reviewers_list
        if not isinstance(states_list, list): 
            states_list = []
            rec["review_states"][idx][0] = states_list
        if not isinstance(events_list, list): 
            events_list = []
            rec["review_events"][idx][0] = events_list

        added: List[str] = []
        skipped_existing: List[str] = []

        for user in reviewers_input:
            if user in reviewers_list:
                skipped_existing.append(user)
            else:
                reviewers_list.append(user)
                states_list.append("REQUESTED")  # initial state for new reviewer
                events_list.append("REQUESTED")
                added.append(user)

        # Deterministic updated_ts bump
        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        add_terminal_message(data, f"Assigned reviewers to PR #{pr_number} for {owner}/{repo_name}.", get_current_updated_timestamp())

        return json.dumps(
            {
                "success": f"Assigned reviewers to PR #{pr_number} for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "pr_number": pr_number,
                "added_reviewers": added,
                "skipped_existing": skipped_existing,
                "total_reviewers": len(reviewers_list),
                "updated_ts": new_updated_ts
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_pull_request_reviewers",
                "description": "Assign reviewers to a pull request; aligns reviewers/states/events and bumps updated_ts deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "pr_number": {"type": "integer", "description": "Pull request number."},
                        "reviewers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of usernames to assign as reviewers."
                        }
                    },
                    "required": ["owner", "repo_name", "pr_number", "reviewers"]
                }
            }
        }


class ApprovePR(Tool):
    """
    Appends an 'APPROVE' entry to review_states and review_events for all assigned reviewers
    on a pull request, and sets the PR's mergeable flag to True.
    Inputs: owner, repo_name, pr_number
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        pr_number_raw = kwargs.get("pr_number", kwargs.get("prnumber", None))

        if not owner or not repo_name or pr_number_raw is None:
            return json.dumps(
                {"error": "Required: owner, repo_name, pr_number."},
                indent=2
            )

        try:
            pr_number = int(pr_number_raw)
        except Exception:
            return json.dumps({"error": "pr_number must be an integer."}, indent=2)

        # Load PR DB (expects list at data['pull_requests'])
        pr_db = data.get("pull_requests", [])
        if not isinstance(pr_db, list):
            return json.dumps({"error": "Invalid pull requests DB: expected a list."}, indent=2)

        # Find repo bucket
        rec = next((r for r in pr_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No pull requests found for '{owner}/{repo_name}'."}, indent=2)

        pr_numbers: List[int] = rec.get("pr_numbers", [])
        if pr_number not in pr_numbers:
            return json.dumps({"error": f"PR #{pr_number} not found for '{owner}/{repo_name}'."}, indent=2)
        idx = pr_numbers.index(pr_number)

        # Ensure structures exist
        rec.setdefault("reviewers", [])
        rec.setdefault("review_states", [])
        rec.setdefault("review_events", [])
        rec.setdefault("mergeable_flags", [])
        rec.setdefault("updated_ts", [])

        while len(rec["reviewers"]) <= idx: rec["reviewers"].append([])
        while len(rec["review_states"]) <= idx: rec["review_states"].append([])
        while len(rec["review_events"]) <= idx: rec["review_events"].append([])
        while len(rec["mergeable_flags"]) <= idx: rec["mergeable_flags"].append(False)
        while len(rec["updated_ts"]) <= idx: rec["updated_ts"].append(None)

        # Ensure first group exists
        if not isinstance(rec["reviewers"][idx], list): rec["reviewers"][idx] = []
        if not isinstance(rec["review_states"][idx], list): rec["review_states"][idx] = []
        if not isinstance(rec["review_events"][idx], list): rec["review_events"][idx] = []

        if len(rec["reviewers"][idx]) == 0: rec["reviewers"][idx].append([])
        if len(rec["review_states"][idx]) == 0: rec["review_states"][idx].append([])
        if len(rec["review_events"][idx]) == 0: rec["review_events"][idx].append([])

        reviewers_list: List[str] = rec["reviewers"][idx][0]
        states_container = rec["review_states"][idx][0]
        events_container = rec["review_events"][idx][0]

        # Normalize states/events to per-reviewer histories (lists of lists)
        if isinstance(states_container, list) and all(isinstance(x, list) for x in states_container):
            states_hist = states_container
        elif isinstance(states_container, list):
            states_hist = [[x] if isinstance(x, str) and x != "" else [] for x in states_container]
        else:
            states_hist = []

        if isinstance(events_container, list) and all(isinstance(x, list) for x in events_container):
            events_hist = events_container
        elif isinstance(events_container, list):
            events_hist = [[x] if isinstance(x, str) and x != "" else [] for x in events_container]
        else:
            events_hist = []

        # Align with reviewers
        while len(states_hist) < len(reviewers_list): states_hist.append([])
        while len(events_hist) < len(reviewers_list): events_hist.append([])
        if len(states_hist) > len(reviewers_list): states_hist = states_hist[:len(reviewers_list)]
        if len(events_hist) > len(reviewers_list): events_hist = events_hist[:len(reviewers_list)]

        # Append "APPROVE" for all assigned reviewers (if any)
        appended_for: List[str] = []
        for i, reviewer in enumerate(reviewers_list):
            states_hist[i].append("APPROVE")
            events_hist[i].append("APPROVE")
            appended_for.append(reviewer)

        # Persist back
        rec["review_states"][idx][0] = states_hist
        rec["review_events"][idx][0] = events_hist

        # Set mergeable flag to True
        rec["mergeable_flags"][idx] = True

        # Bump updated_ts deterministically (env-provided helper)
        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        add_terminal_message(data, f"PR #{pr_number} marked APPROVE for {owner}/{repo_name}.", get_current_updated_timestamp())

        return json.dumps(
            {
                "success": f"PR #{pr_number} marked APPROVE for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "pr_number": pr_number,
                "mergeable": True,
                "appended_review_event": "APPROVE",
                "appended_for_reviewers": appended_for,
                "updated_ts": new_updated_ts
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "approve_pr",
                "description": "Append 'APPROVE' to review_states and review_events for all assigned reviewers and set mergeable flag to true.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "pr_number": {"type": "integer", "description": "Pull request number."}
                    },
                    "required": ["owner", "repo_name", "pr_number"]
                }
            }
        }
    

# class MergePullRequest(Tool):
#     """
#     Marks a pull request as merged, but only if it is currently mergeable.
#     Additionally merges the PR's files from the head branch into the base branch.
#     - Requires mergeable_flags[idx] == True
#     - Sets pr_states[idx] = "merged" (and pr_status[idx] if present)
#     - Sets merged_flags[idx] = True
#     - Copies/updates files from head -> base (and into repo-level files if base == default branch)
#     - Bumps updated_ts via get_current_updated_timestamp()
#     Inputs: owner, repo_name, pr_number
#     """

#     @staticmethod
#     def invoke(data: Dict[str, Any], **kwargs) -> str:
#         owner = (kwargs.get("owner") or "").strip()
#         repo_name = (kwargs.get("repo_name") or kwargs.get("reponame") or "").strip()
#         pr_number_raw = kwargs.get("pr_number", kwargs.get("prnumber", None))

#         if not owner or not repo_name or pr_number_raw is None:
#             return json.dumps(
#                 {"error": "Required: owner, repo_name, pr_number."},
#                 indent=2
#             )

#         try:
#             pr_number = int(pr_number_raw)
#         except Exception:
#             return json.dumps({"error": "pr_number must be an integer."}, indent=2)

#         # Load PR DB (expects list at data['pull_requests'])
#         pr_db = data.get("pull_requests", [])
#         if not isinstance(pr_db, list):
#             return json.dumps({"error": "Invalid pull requests DB: expected a list."}, indent=2)

#         # Find repository bucket (PR store)
#         rec = next((r for r in pr_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
#         if rec is None:
#             return json.dumps({"error": f"No pull requests found for '{owner}/{repo_name}'."}, indent=2)

#         pr_numbers: List[int] = rec.get("pr_numbers", [])
#         if pr_number not in pr_numbers:
#             return json.dumps({"error": f"PR #{pr_number} not found for '{owner}/{repo_name}'."}, indent=2)
#         idx = pr_numbers.index(pr_number)

#         # Ensure required arrays exist and are padded
#         rec.setdefault("pr_states", [])
#         rec.setdefault("merged_flags", [])
#         rec.setdefault("mergeable_flags", [])
#         rec.setdefault("updated_ts", [])
#         rec.setdefault("pr_status", [])
#         rec.setdefault("base_branches", [])
#         rec.setdefault("head_branches", [])
#         rec.setdefault("pr_files", [])

#         while len(rec["pr_states"])        <= idx: rec["pr_states"].append("open")
#         while len(rec["merged_flags"])     <= idx: rec["merged_flags"].append(False)
#         while len(rec["mergeable_flags"])  <= idx: rec["mergeable_flags"].append(False)
#         while len(rec["updated_ts"])       <= idx: rec["updated_ts"].append(None)
#         while len(rec["pr_status"])        <= idx: rec["pr_status"].append("open")
#         while len(rec["base_branches"])    <= idx: rec["base_branches"].append("main")
#         while len(rec["head_branches"])    <= idx: rec["head_branches"].append(None)
#         while len(rec["pr_files"])         <= idx: rec["pr_files"].append([])

#         # Must be mergeable to merge
#         if not bool(rec["mergeable_flags"][idx]):
#             return json.dumps(
#                 {
#                     "error": f"PR #{pr_number} is not mergeable for '{owner}/{repo_name}'.",
#                     "mergeable": False,
#                     "current_state": rec["pr_states"][idx]
#                 },
#                 indent=2
#             )

#         # Early idempotency check
#         if bool(rec["merged_flags"][idx]) and rec["pr_states"][idx] == "merged":
#             current_ts = rec["updated_ts"][idx]
#             return json.dumps(
#                 {
#                     "success": f"PR #{pr_number} is already merged for {owner}/{repo_name}.",
#                     "repo": f"{owner}/{repo_name}",
#                     "pr_number": pr_number,
#                     "state": "merged",
#                     "merged": True,
#                     "updated_ts": current_ts
#                 },
#                 indent=2
#             )

#         base_branch = rec["base_branches"][idx]
#         head_branch = rec["head_branches"][idx]
#         pr_files = rec["pr_files"][idx] if isinstance(rec["pr_files"][idx], list) else []

#         # Load repository DB to actually merge files head -> base
#         repos = data.get("repositories", [])
#         if not isinstance(repos, list):
#             return json.dumps({"error": "Invalid repositories DB: expected a list."}, indent=2)

#         repo = next((r for r in repos if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
#         if repo is None:
#             return json.dumps({"error": f"Repository '{owner}/{repo_name}' not found."}, indent=2)

#         branches: List[str] = repo.get("branches", [])
#         if base_branch not in branches:
#             return json.dumps({"error": f"Base branch '{base_branch}' not found in repository '{owner}/{repo_name}'."}, indent=2)
#         if head_branch not in branches:
#             return json.dumps({"error": f"Head branch '{head_branch}' not found in repository '{owner}/{repo_name}'."}, indent=2)

#         base_idx = branches.index(base_branch)
#         head_idx = branches.index(head_branch)

#         # Ensure per-branch arrays exist/padded
#         branch_files_all: List[List[str]] = repo.setdefault("branch_files", [])
#         branch_contents_all: List[List[str]] = repo.setdefault("branch_contents", [])
#         branch_shas: List[str] = repo.setdefault("branch_shas", [])

#         while len(branch_files_all)   < len(branches): branch_files_all.append([])
#         while len(branch_contents_all) < len(branches): branch_contents_all.append([])
#         while len(branch_shas)       < len(branches): branch_shas.append("")

#         head_files = branch_files_all[head_idx]
#         head_contents = branch_contents_all[head_idx]
#         base_files = branch_files_all[base_idx]
#         base_contents = branch_contents_all[base_idx]

#         merged_files: List[str] = []
#         skipped_files: List[str] = []

#         # Merge the files listed on the PR from head -> base
#         for path in pr_files:
#             try:
#                 i = head_files.index(path)
#                 content = head_contents[i] if i < len(head_contents) else None
#             except ValueError:
#                 content = None

#             if content is None:
#                 skipped_files.append(path)
#                 continue

#             if path in base_files:
#                 j = base_files.index(path)
#                 # Update existing file in base
#                 if j < len(base_contents):
#                     base_contents[j] = content
#                 else:
#                     # Defensive: pad if needed
#                     while len(base_contents) < len(base_files):
#                         base_contents.append("")
#                     base_contents[j] = content
#             else:
#                 # Append new file to base
#                 base_files.append(path)
#                 base_contents.append(content)

#             merged_files.append(path)

#         # If base is default branch, mirror changes to repo-level files
#         default_branch = repo.get("default_branch", "main")
#         if base_branch == default_branch and merged_files:
#             file_paths = repo.setdefault("file_paths", [])
#             file_contents = repo.setdefault("file_contents", [])
#             for path in merged_files:
#                 # Content in base (now updated)
#                 try:
#                     k = base_files.index(path)
#                     content = base_contents[k] if k < len(base_contents) else ""
#                 except ValueError:
#                     content = ""

#                 if path in file_paths:
#                     m = file_paths.index(path)
#                     if m < len(file_contents):
#                         file_contents[m] = content
#                     else:
#                         while len(file_contents) < len(file_paths):
#                             file_contents.append("")
#                         file_contents[m] = content
#                 else:
#                     file_paths.append(path)
#                     file_contents.append(content)

#         # Update PR state flags
#         rec["pr_states"][idx] = "merged"
#         rec["pr_status"][idx] = "merged"
#         rec["merged_flags"][idx] = True

#         # Deterministic timestamp updates
#         new_updated_ts = get_current_updated_timestamp()
#         rec["updated_ts"][idx] = new_updated_ts
#         repo["updated_ts"] = new_updated_ts

#         # Terminal log (single deterministic timestamp)
#         add_terminal_message(
#             data,
#             f"PR #{pr_number} merged into '{base_branch}' for {owner}/{repo_name}. Files merged: {len(merged_files)}.",
#             new_updated_ts
#         )

#         return json.dumps(
#             {
#                 "success": f"PR #{pr_number} merged for {owner}/{repo_name}.",
#                 "repo": f"{owner}/{repo_name}",
#                 "pr_number": pr_number,
#                 "state": "merged",
#                 "merged": True,
#                 "base_branch": base_branch,
#                 "head_branch": head_branch,
#                 "merged_files": merged_files,
#                 "skipped_files": skipped_files or [],
#                 "updated_ts": new_updated_ts
#             },
#             indent=2
#         )

#     @staticmethod
#     def get_info() -> Dict[str, Any]:
#         return {
#             "type": "function",
#             "function": {
#                 "name": "merge_pull_request",
#                 "description": "Merge a PR only if mergeable; sets merged flags/states and merges PR files from head into base (and default-branch repo-level files).",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "owner": {"type": "string", "description": "Repository owner."},
#                         "repo_name": {"type": "string", "description": "Repository name (alias: reponame)."},
#                         "pr_number": {"type": "integer", "description": "Pull request number."}
#                     },
#                     "required": ["owner", "repo_name", "pr_number"]
#                 }
#             }
#         }


class MarkPRasMerged(Tool):
    """
    Marks a pull request as merged, but only if it is currently mergeable.
    NOTE: This tool does NOT copy files or perform any branch/content merge. It only:
      - verifies the PR is mergeable,
      - sets merged flags/states,
      - bumps the PR's updated_ts deterministically,
      - logs a terminal message.
    Inputs: owner, repo_name, pr_number
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = (kwargs.get("owner") or "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("reponame") or "").strip()
        pr_number_raw = kwargs.get("pr_number", kwargs.get("prnumber", None))

        if not owner or not repo_name or pr_number_raw is None:
            return json.dumps(
                {"error": "Required: owner, repo_name, pr_number."},
                indent=2
            )

        try:
            pr_number = int(pr_number_raw)
        except Exception:
            return json.dumps({"error": "pr_number must be an integer."}, indent=2)

        # Load PR DB
        pr_db = data.get("pull_requests", [])
        if not isinstance(pr_db, list):
            return json.dumps({"error": "Invalid pull requests DB: expected a list."}, indent=2)

        # Find PR bucket for repo
        rec = next((r for r in pr_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No pull requests found for '{owner}/{repo_name}'."}, indent=2)

        pr_numbers: List[int] = rec.get("pr_numbers", [])
        if pr_number not in pr_numbers:
            return json.dumps({"error": f"PR #{pr_number} not found for '{owner}/{repo_name}'."}, indent=2)
        idx = pr_numbers.index(pr_number)

        # Ensure arrays exist/padded
        rec.setdefault("pr_states", [])
        rec.setdefault("merged_flags", [])
        rec.setdefault("mergeable_flags", [])
        rec.setdefault("updated_ts", [])
        rec.setdefault("pr_status", [])

        while len(rec["pr_states"])       <= idx: rec["pr_states"].append("open")
        while len(rec["merged_flags"])    <= idx: rec["merged_flags"].append(False)
        while len(rec["mergeable_flags"]) <= idx: rec["mergeable_flags"].append(False)
        while len(rec["updated_ts"])      <= idx: rec["updated_ts"].append(None)
        while len(rec["pr_status"])       <= idx: rec["pr_status"].append("open")

        # Must be mergeable
        if not bool(rec["mergeable_flags"][idx]):
            return json.dumps(
                {
                    "error": f"PR #{pr_number} is not mergeable for '{owner}/{repo_name}'.",
                    "mergeable": False,
                    "current_state": rec["pr_states"][idx]
                },
                indent=2
            )

        # Idempotent path: already merged
        if bool(rec["merged_flags"][idx]) and rec["pr_states"][idx] == "merged":
            return json.dumps(
                {
                    "success": f"PR #{pr_number} is already merged for {owner}/{repo_name}.",
                    "repo": f"{owner}/{repo_name}",
                    "pr_number": pr_number,
                    "state": "merged",
                    "merged": True,
                    "mergeable": True,
                    "updated_ts": rec["updated_ts"][idx]
                },
                indent=2
            )

        # Mark as merged and update timestamp (no file operations)
        rec["pr_states"][idx] = "merged"
        rec["pr_status"][idx] = "merged"
        rec["merged_flags"][idx] = True

        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        # Terminal log
        add_terminal_message(
            data,
            f"PR #{pr_number} merged for {owner}/{repo_name}.",
            new_updated_ts
        )

        return json.dumps(
            {
                "success": f"PR #{pr_number} merged for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "pr_number": pr_number,
                "state": "merged",
                "merged": True,
                "mergeable": True,
                "updated_ts": new_updated_ts
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "mark_pr_as_merged",
                "description": "Mark a PR as merged if mergeable; sets merged flags/states and updates PR updated_ts (no file merges).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: reponame)."},
                        "pr_number": {"type": "integer", "description": "Pull request number."}
                    },
                    "required": ["owner", "repo_name", "pr_number"]
                }
            }
        }


class CreateNewIssue(Tool):
    """
    Create a new issue entry for a repo in the issues DB.
    - Inputs: owner, repo_name (alias: repo_name), plus optional: title, body, label(s), assignee(s)
    - Behavior:
        * If (owner, repo_name) bucket does NOT exist: create a brand-new record and add the first issue.
        * Else: append a new issue to the existing record with next issue_number from get_next_issue_number(data).
    - Timestamps: created_ts/updated_ts come from get_current_updated_timestamp().
    - Defaults: title/body "", state "open", labels/assignees/comments empty.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()

        # Optional fields
        title = (kwargs.get("title") or kwargs.get("issue_title") or "").strip()
        body = (kwargs.get("body") or kwargs.get("issue_body") or "").strip()

        # Accept label(s) via 'label', 'lable' (typo), or 'labels'
        labels_input = kwargs.get("labels", kwargs.get("label", kwargs.get("lable", None)))
        if isinstance(labels_input, str):
            labels_list: List[str] = [labels_input.strip()] if labels_input.strip() else []
        elif isinstance(labels_input, list):
            labels_list = [str(x).strip() for x in labels_input if isinstance(x, (str, int, float)) and str(x).strip()]
        else:
            labels_list = []

        # Accept assignee(s) via 'assignees' or 'assignee'
        assignees_input = kwargs.get("assignees", kwargs.get("assignee", None))
        if isinstance(assignees_input, str):
            assignees_list: List[str] = [assignees_input.strip()] if assignees_input.strip() else []
        elif isinstance(assignees_input, list):
            assignees_list = [str(x).strip() for x in assignees_input if isinstance(x, (str, int, float)) and str(x).strip()]
        else:
            assignees_list = []

        if not owner or not repo_name:
            return json.dumps(
                {"error": "Parameters 'owner' and 'repo_name' (or 'repo_name') are required."},
                indent=2
            )

        # Load issues DB
        issues_db = data.get("issues", [])
        if not isinstance(issues_db, list):
            return json.dumps({"error": "Invalid issues DB: expected a list at data['issues']."}, indent=2)

        # Find or create the repo bucket
        rec = next((r for r in issues_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        created_bucket = False
        if rec is None:
            rec = {
                "owner": owner,
                "repo_name": repo_name,
                "issue_numbers": [],
                "issue_titles": [],
                "issue_bodies": [],
                "issue_states": [],
                "labels": [],
                "assignees": [],
                "issue_comments": [],
                "issue_comment_users": [],
                "created_ts": [],
                "updated_ts": []
            }
            issues_db.append(rec)
            created_bucket = True

        # Next issue number & timestamp (helpers provided by your env)
        next_issue_number = get_next_issue_number(data)
        new_ts = get_current_timestamp()

        # Ensure arrays exist
        for key, default in [
            ("issue_numbers", []),
            ("issue_titles", []),
            ("issue_bodies", []),
            ("issue_states", []),
            ("labels", []),
            ("assignees", []),
            ("issue_comments", []),
            ("issue_comment_users", []),
            ("created_ts", []),
            ("updated_ts", []),
        ]:
            rec.setdefault(key, default)

        # Append the new issue
        rec["issue_numbers"].append(next_issue_number)
        rec["issue_titles"].append(title)            # provided or ""
        rec["issue_bodies"].append(body)             # provided or ""
        rec["issue_states"].append("open")
        rec["labels"].append(labels_list)            # list[str]
        rec["assignees"].append(assignees_list)      # list[str]
        rec["issue_comments"].append([])             # none yet
        rec["issue_comment_users"].append([])        # none yet
        rec["created_ts"].append(new_ts)
        rec["updated_ts"].append(new_ts)

        add_terminal_message(data, f"Created new issues bucket and issue #{next_issue_number}" if created_bucket else f"Added issue #{next_issue_number} to existing bucket", get_current_timestamp())

        return json.dumps(
            {
                "success": (
                    f"Created new issues bucket and issue #{next_issue_number}"
                    if created_bucket else
                    f"Added issue #{next_issue_number} to existing bucket"
                ),
                "repo": f"{owner}/{repo_name}",
                "issue": {
                    "number": next_issue_number,
                    "title": title,
                    "body": body,
                    "state": "open",
                    "labels": labels_list,
                    "assignees": assignees_list,
                    "created_ts": new_ts,
                    "updated_ts": new_ts
                }
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_issue",
                "description": "Create a new issue for a repo in the issues DB (creates repo bucket if missing). Supports title, body, labels, assignees.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias accepted as 'repo_name')."},
                        "title": {"type": "string", "description": "Issue title."},
                        "body": {"type": "string", "description": "Issue body/description."},
                        "labels": {"type": "array", "items": {"type": "string"}, "description": "List of labels to attach."},
                        "assignees": {"type": "array", "items": {"type": "string"}, "description": "List of usernames to assign."}
                    },
                    "required": ["owner", "repo_name","title","body","labels","assignees"]
                }
            }
        }


class GetAllIssuesForRepo(Tool):
    """
    Lists all issues for a given repository from the issues DB.
    Inputs: owner, repo_name (alias: repo_name)
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()

        if not owner or not repo_name:
            return json.dumps(
                {"error": "Parameters 'owner' and 'repo_name' (or 'repo_name') are required."},
                indent=2
            )

        # Load issues DB
        issues_db = data.get("issues", [])
        if not isinstance(issues_db, list):
            return json.dumps({"error": "Invalid issues DB: expected a list at data['issues']."}, indent=2)

        # Find repo bucket
        rec = next((r for r in issues_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No issues found for repository '{owner}/{repo_name}'."}, indent=2)

        issue_numbers: List[int] = rec.get("issue_numbers", [])

        def get_at(key: str, i: int):
            arr = rec.get(key, [])
            return arr[i] if i < len(arr) else None

        # Build (number, index) pairs and sort by issue number
        indexed: List[tuple] = [(num, i) for i, num in enumerate(issue_numbers)]
        indexed.sort(key=lambda t: t[0])

        issues_out: List[Dict[str, Any]] = []
        for num, idx in indexed:
            issues_out.append({
                "number": num,
                "title": get_at("issue_titles", idx),
                "body": get_at("issue_bodies", idx),
                "state": get_at("issue_states", idx),
                "labels": get_at("labels", idx),
                "assignees": get_at("assignees", idx),
                "comments": get_at("issue_comments", idx),
                "comment_users": get_at("issue_comment_users", idx),
                "created_ts": get_at("created_ts", idx),
                "updated_ts": get_at("updated_ts", idx),
            })

        return json.dumps(
            {
                "owner": owner,
                "repo_name": repo_name,
                "count": len(issues_out),
                "issues": issues_out
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_issues_for_repo",
                "description": "List all issues for a repository from the issues DB.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias accepted as 'repo_name')."}
                    },
                    "required": ["owner", "repo_name"]
                }
            }
        }


class AddCommentToIssue(Tool):
    """
    Append a comment to an issue in the issues DB.
    Inputs:
      - owner (str)
      - repo_name (str)  [alias: repo_name]
      - issue_number (int) [alias: issue number, issue_no, number]
      - issue_comment (str)
      - issue_comment_user (str)
    Behavior:
      - Finds the repo bucket and issue by number.
      - Appends the comment and commenter to aligned arrays.
      - Bumps updated_ts for that issue via get_current_updated_timestamp().
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = (kwargs.get("owner") or "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        # accept several aliases for the issue number
        issue_number_raw = (
            kwargs.get("issue_number",
                kwargs.get("issue number",
                    kwargs.get("issue_no",
                        kwargs.get("number", None)
                    )
                )
            )
        )
        issue_comment = (kwargs.get("issue_comment") or "").strip()
        issue_comment_user = (kwargs.get("issue_comment_user") or "").strip()

        if not owner or not repo_name or issue_number_raw is None or not issue_comment or not issue_comment_user:
            return json.dumps(
                {"error": "Required: owner, repo_name (or repo_name), issue_number, issue_comment, issue_comment_user."},
                indent=2
            )

        # Normalize issue_number
        try:
            issue_number = int(issue_number_raw)
        except Exception:
            return json.dumps({"error": "issue_number must be an integer."}, indent=2)

        # Load issues DB
        issues_db = data.get("issues", [])
        if not isinstance(issues_db, list):
            return json.dumps({"error": "Invalid issues DB: expected a list at data['issues']."}, indent=2)

        # Find repo bucket
        rec = next((r for r in issues_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No issues found for repository '{owner}/{repo_name}'."}, indent=2)

        issue_numbers: List[int] = rec.get("issue_numbers", [])
        if issue_number not in issue_numbers:
            return json.dumps({"error": f"Issue #{issue_number} not found for '{owner}/{repo_name}'."}, indent=2)

        idx = issue_numbers.index(issue_number)

        # Ensure arrays exist and are padded
        rec.setdefault("issue_comments", [])
        rec.setdefault("issue_comment_users", [])
        rec.setdefault("updated_ts", [])
        while len(rec["issue_comments"]) <= idx: rec["issue_comments"].append([])
        while len(rec["issue_comment_users"]) <= idx: rec["issue_comment_users"].append([])
        while len(rec["updated_ts"]) <= idx: rec["updated_ts"].append(None)

        # Ensure per-issue comment containers are lists
        if not isinstance(rec["issue_comments"][idx], list):
            rec["issue_comments"][idx] = []
        if not isinstance(rec["issue_comment_users"][idx], list):
            rec["issue_comment_users"][idx] = []

        # Append comment and user (keep indices aligned)
        rec["issue_comments"][idx].append(issue_comment)
        rec["issue_comment_users"][idx].append(issue_comment_user)
        comment_index = len(rec["issue_comments"][idx]) - 1

        # Bump updated_ts using environment helper
        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        add_terminal_message(data, f"Comment added to issue #{issue_number} for {owner}/{repo_name}.", get_current_updated_timestamp())

        return json.dumps(
            {
                "success": f"Comment added to issue #{issue_number} for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "issue_number": issue_number,
                "comment_index": comment_index,
                "issue_comment": issue_comment,
                "issue_comment_user": issue_comment_user,
                "updated_ts": new_updated_ts
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_comment_to_issue",
                "description": "Append a comment to an issue and update the issue's updated_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: repo_name)."},
                        "issue_number": {"type": "integer", "description": "Issue number."},
                        "issue_comment": {"type": "string", "description": "Comment text to add."},
                        "issue_comment_user": {"type": "string", "description": "Username adding the comment."}
                    },
                    "required": ["owner", "repo_name", "issue_number", "issue_comment", "issue_comment_user"]
                }
            }
        }


class CloseIssue(Tool):
    """
    Close an issue in the issues DB.
    - Inputs: owner, repo_name (alias: repo_name), issue_number (aliases supported)
    - Sets issue_states[idx] = "closed" and bumps updated_ts via get_current_updated_timestamp().
    - Idempotent: if already closed, returns current state without changing anything.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = (kwargs.get("owner")).strip()
        repo_name = (kwargs.get("repo_name")).strip()
        issue_number_raw = kwargs.get("issue_number")
                

        if not owner or not repo_name or issue_number_raw is None:
            return json.dumps(
                {"error": "Required: owner, repo_name (or repo_name), issue_number."},
                indent=2
            )

        # Normalize issue_number
        try:
            issue_number = int(issue_number_raw)
        except Exception:
            return json.dumps({"error": "issue_number must be an integer."}, indent=2)

        # Load issues DB
        issues_db = data.get("issues", [])
        if not isinstance(issues_db, list):
            return json.dumps({"error": "Invalid issues DB: expected a list at data['issues']."}, indent=2)

        # Find repo bucket
        rec = next((r for r in issues_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No issues found for repository '{owner}/{repo_name}'."}, indent=2)

        issue_numbers: List[int] = rec.get("issue_numbers", [])
        if issue_number not in issue_numbers:
            return json.dumps({"error": f"Issue #{issue_number} not found for '{owner}/{repo_name}'."}, indent=2)

        idx = issue_numbers.index(issue_number)

        # Ensure arrays exist and are padded
        rec.setdefault("issue_states", [])
        rec.setdefault("updated_ts", [])
        while len(rec["issue_states"]) <= idx: rec["issue_states"].append("open")
        while len(rec["updated_ts"]) <= idx: rec["updated_ts"].append(None)

        current_state = rec["issue_states"][idx]
        if current_state == "closed":
            # Idempotent response if already closed
            return json.dumps(
                {
                    "success": f"Issue #{issue_number} is already closed for {owner}/{repo_name}.",
                    "repo": f"{owner}/{repo_name}",
                    "issue_number": issue_number,
                    "state": "closed",
                    "updated_ts": rec["updated_ts"][idx]
                },
                indent=2
            )

        # Close the issue
        rec["issue_states"][idx] = "closed"

        # Bump updated_ts using environment-provided deterministic helper
        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        add_terminal_message(data, f"Issue #{issue_number} closed for {owner}/{repo_name}.", get_current_updated_timestamp())

        return json.dumps(
            {
                "success": f"Issue #{issue_number} closed for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "issue_number": issue_number,
                "state": "closed",
                "updated_ts": new_updated_ts
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "close_issue",
                "description": "Close an issue (sets state to 'closed') and update its updated_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: repo_name)."},
                        "issue_number": {"type": "integer", "description": "Issue number to close."}
                    },
                    "required": ["owner", "repo_name", "issue_number"]
                }
            }
        }


class CreateCodeScanningAlert(Tool):
    """
    Create a new code scanning alert for a repository in the code_scanning_alerts DB.
    - Inputs: owner, repo_name (alias: repo_name), severity, description, ref
    - Behavior:
        * If (owner, repo_name) bucket does NOT exist: create a new record and add alert #1.
        * Else: append a new alert with next alert_number = max(existing)+1.
    - Fields:
        * state: "open"
        * created_ts: get_current_updated_timestamp()
        * dismissed_ts_nullables: null
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = (kwargs.get("owner") or "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        severity_raw = (kwargs.get("severity") or "").strip()
        description = (kwargs.get("description") or "").strip()
        ref = (kwargs.get("ref") or "").strip()

        if not owner or not repo_name or not severity_raw or not description or not ref:
            return json.dumps(
                {"error": "Required: owner, repo_name (or repo_name), severity, description, ref."},
                indent=2
            )

        # Normalize/validate severity
        severity = severity_raw.lower()
        allowed = {"critical", "high", "medium", "low"}
        if severity not in allowed:
            return json.dumps(
                {"error": f"Invalid severity '{severity_raw}'. Use one of: critical, high, medium, low."},
                indent=2
            )

        # Load alerts DB
        alerts_db = data.get("code_scanning_alerts", [])
        if not isinstance(alerts_db, list):
            return json.dumps(
                {"error": "Invalid DB: expected a list at data['code_scanning_alerts']."},
                indent=2
            )

        # Find or create repo bucket
        rec = next((r for r in alerts_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        created_bucket = False
        if rec is None:
            rec = {
                "owner": owner,
                "repo_name": repo_name,
                "alert_numbers": [],
                "severities": [],
                "states": [],
                "descriptions": [],
                "refs": [],
                "created_ts": [],
                "dismissed_ts_nullables": []
            }
            alerts_db.append(rec)
            created_bucket = True

        # Ensure arrays exist
        for key in ["alert_numbers","severities","states","descriptions","refs","created_ts","dismissed_ts_nullables"]:
            rec.setdefault(key, [])

        # Next alert number (per repo)
        next_alert_number = get_next_alert_number(data)

        # Deterministic timestamp from your environment helper
        new_ts = get_current_timestamp()

        # Append new alert
        rec["alert_numbers"].append(next_alert_number)
        rec["severities"].append(severity)
        rec["states"].append("open")
        rec["descriptions"].append(description)
        rec["refs"].append(ref)
        rec["created_ts"].append(new_ts)
        rec["dismissed_ts_nullables"].append(None)

        add_terminal_message(data, f"Created new alerts bucket and alert #{next_alert_number}" if created_bucket else f"Added alert #{next_alert_number} to existing bucket", get_current_timestamp())

        return json.dumps(
            {
                "success": (
                    f"Created new alerts bucket and alert #{next_alert_number}"
                    if created_bucket else
                    f"Added alert #{next_alert_number} to existing bucket"
                ),
                "repo": f"{owner}/{repo_name}",
                "alert": {
                    "number": next_alert_number,
                    "severity": severity,
                    "state": "open",
                    "description": description,
                    "ref": ref,
                    "created_ts": new_ts,
                    "dismissed_ts": None
                }
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_code_scanning_alert",
                "description": "Create a new code scanning alert for a repository; creates the repo bucket if missing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: repo_name)."},
                        "severity": {"type": "string", "description": "Severity: critical, high, medium, or low."},
                        "description": {"type": "string", "description": "Alert description."},
                        "ref": {"type": "string", "description": "Git ref (e.g., refs/heads/main)."}
                    },
                    "required": ["owner", "repo_name", "severity", "description", "ref"]
                }
            }
        }


class GetAlertDetails(Tool):
    """
    Return all stored details for a code scanning alert identified by
    (owner, repo_name, alert_number).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = (kwargs.get("owner") or "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        alert_number_raw = kwargs.get("alert_number", kwargs.get("alertnumber", None))

        if not owner or not repo_name or alert_number_raw is None:
            return json.dumps(
                {"error": "Required: owner, repo_name (or repo_name), alert_number."},
                indent=2
            )

        # Normalize alert_number
        try:
            alert_number = int(alert_number_raw)
        except Exception:
            return json.dumps({"error": "alert_number must be an integer."}, indent=2)

        # Load alerts DB
        alerts_db = data.get("code_scanning_alerts", [])
        if not isinstance(alerts_db, list):
            return json.dumps(
                {"error": "Invalid DB: expected a list at data['code_scanning_alerts']."},
                indent=2
            )

        # Find repo bucket
        rec = next((r for r in alerts_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps(
                {"error": f"No alerts found for repository '{owner}/{repo_name}'."},
                indent=2
            )

        alert_numbers: List[int] = rec.get("alert_numbers", [])
        if alert_number not in alert_numbers:
            return json.dumps(
                {"error": f"Alert #{alert_number} not found for '{owner}/{repo_name}'."},
                indent=2
            )

        idx = alert_numbers.index(alert_number)

        def get_at(key: str):
            arr = rec.get(key, [])
            return arr[idx] if idx < len(arr) else None

        details = {
            "owner": owner,
            "repo_name": repo_name,
            "number": alert_number,
            "severity": get_at("severities"),
            "state": get_at("states"),
            "description": get_at("descriptions"),
            "ref": get_at("refs"),
            "created_ts": get_at("created_ts"),
            "dismissed_ts": get_at("dismissed_ts_nullables")
        }

        return json.dumps(details, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_alert_details",
                "description": "Fetch full details for a code scanning alert (owner, repo_name, alert_number).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: repo_name)."},
                        "alert_number": {"type": "integer", "description": "Alert number within the repository."}
                    },
                    "required": ["owner", "repo_name", "alert_number"]
                }
            }
        }


class ListOpenAlertsForRepo(Tool):
    """
    List open code scanning alerts for a repository.
    - Inputs (required): owner, repo_name (alias: repo_name)
    - Inputs (optional): severity (critical/high/medium/low), ref (e.g., refs/heads/main)
    - Returns a list of open alerts with basic details, sorted by alert number.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = (kwargs.get("owner") or "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        severity_raw = (kwargs.get("severity") or "").strip()
        ref_filter = (kwargs.get("ref") or "").strip()

        if not owner or not repo_name:
            return json.dumps(
                {"error": "Required: owner, repo_name (or repo_name)."},
                indent=2
            )

        # Normalize optional severity
        severity_filter = None
        if severity_raw:
            sev = severity_raw.lower()
            if sev not in {"critical", "high", "medium", "low"}:
                return json.dumps(
                    {"error": "Invalid 'severity'. Use one of: critical, high, medium, low."},
                    indent=2
                )
            severity_filter = sev

        # Load alerts DB
        alerts_db = data.get("code_scanning_alerts", [])
        if not isinstance(alerts_db, list):
            return json.dumps(
                {"error": "Invalid DB: expected a list at data['code_scanning_alerts']."},
                indent=2
            )

        # Find repo bucket
        rec = next((r for r in alerts_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps(
                {"error": f"No alerts found for repository '{owner}/{repo_name}'."},
                indent=2
            )

        alert_numbers: List[int] = rec.get("alert_numbers", [])

        def get_at(key: str, i: int):
            arr = rec.get(key, [])
            return arr[i] if i < len(arr) else None

        # Build list of open alerts, optionally filter by severity/ref
        indexed: List[tuple] = [(num, i) for i, num in enumerate(alert_numbers)]
        indexed.sort(key=lambda t: t[0])

        results: List[Dict[str, Any]] = []
        for num, idx in indexed:
            state = get_at("states", idx)
            if state != "open":
                continue

            sev = (get_at("severities", idx) or "").lower()
            alert_ref = get_at("refs", idx) or ""

            if severity_filter and sev != severity_filter:
                continue
            if ref_filter and alert_ref != ref_filter:
                continue

            results.append({
                "number": num,
                "severity": sev,
                "state": state,
                "description": get_at("descriptions", idx),
                "ref": alert_ref,
                "created_ts": get_at("created_ts", idx),
                "dismissed_ts": get_at("dismissed_ts_nullables", idx),
            })

        return json.dumps(
            {
                "owner": owner,
                "repo_name": repo_name,
                "count": len(results),
                "alerts": results
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_open_alerts_for_repo",
                "description": "List open code scanning alerts for a repository, optionally filtered by severity and ref.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: repo_name)."},
                        "severity": {
                            "type": "string",
                            "enum": ["critical", "high", "medium", "low"],
                            "description": "Optional severity filter."
                        },
                        "ref": {"type": "string", "description": "Optional Git ref filter (e.g., refs/heads/main)."}
                    },
                    "required": ["owner", "repo_name"]
                }
            }
        }


class DismissAlert(Tool):
    """
    Dismiss a code scanning alert for a given repository.
    - Sets states[idx] = "dismissed"
    - Sets dismissed_ts_nullables[idx] = get_current_updated_timestamp()
    - Idempotent: if already dismissed, returns current info without changing anything.
    Inputs: owner, repo_name (alias: repo_name), alert_number
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = (kwargs.get("owner") or "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        alert_number_raw = kwargs.get("alert_number", kwargs.get("alertnumber", None))

        if not owner or not repo_name or alert_number_raw is None:
            return json.dumps(
                {"error": "Required: owner, repo_name (or repo_name), alert_number."},
                indent=2
            )

        # Normalize alert_number
        try:
            alert_number = int(alert_number_raw)
        except Exception:
            return json.dumps({"error": "alert_number must be an integer."}, indent=2)

        # Load alerts DB
        alerts_db = data.get("code_scanning_alerts", [])
        if not isinstance(alerts_db, list):
            return json.dumps(
                {"error": "Invalid DB: expected a list at data['code_scanning_alerts']."},
                indent=2
            )

        # Find repo bucket
        rec = next((r for r in alerts_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps(
                {"error": f"No alerts found for repository '{owner}/{repo_name}'."},
                indent=2
            )

        alert_numbers: List[int] = rec.get("alert_numbers", [])
        if alert_number not in alert_numbers:
            return json.dumps(
                {"error": f"Alert #{alert_number} not found for '{owner}/{repo_name}'."},
                indent=2
            )

        idx = alert_numbers.index(alert_number)

        # Ensure required arrays exist/padded
        rec.setdefault("states", [])
        rec.setdefault("dismissed_ts_nullables", [])
        while len(rec["states"]) <= idx: rec["states"].append("open")
        while len(rec["dismissed_ts_nullables"]) <= idx: rec["dismissed_ts_nullables"].append(None)

        current_state = rec["states"][idx]
        current_dismissed_ts = rec["dismissed_ts_nullables"][idx]

        # Idempotent behavior if already dismissed
        if current_state == "dismissed":
            return json.dumps(
                {
                    "success": f"Alert #{alert_number} is already dismissed for {owner}/{repo_name}.",
                    "repo": f"{owner}/{repo_name}",
                    "alert_number": alert_number,
                    "state": "dismissed",
                    "dismissed_ts": current_dismissed_ts
                },
                indent=2
            )

        # Dismiss the alert
        rec["states"][idx] = "dismissed"
        new_dismissed_ts = get_current_updated_timestamp()
        rec["dismissed_ts_nullables"][idx] = new_dismissed_ts

        add_terminal_message(data, f"Alert #{alert_number} dismissed for {owner}/{repo_name}.", get_current_updated_timestamp())

        return json.dumps(
            {
                "success": f"Alert #{alert_number} dismissed for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "alert_number": alert_number,
                "state": "dismissed",
                "dismissed_ts": new_dismissed_ts
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "dismiss_alert",
                "description": "Dismiss a code scanning alert: sets state='dismissed' and records dismissed timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: repo_name)."},
                        "alert_number": {"type": "integer", "description": "Alert number within the repository."}
                    },
                    "required": ["owner", "repo_name", "alert_number"]
                }
            }
        }


class ListAllTerminalMessage(Tool):
    """
    Return all terminal log lines formatted as 'timestamp : message'.
    Reads from data['terminal'] which may be a list (entry at index 0) or a dict
    with keys 'printed_ts' and 'messages'.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Load terminal entry
        terminal = data.get("terminal", [])
        if isinstance(terminal, list):
            entry = terminal[0] if terminal else {"printed_ts": [], "messages": []}
        elif isinstance(terminal, dict):
            entry = terminal
        else:
            return json.dumps(
                {"error": "Invalid database format: 'terminal' must be a list or dict."},
                indent=2
            )

        ts_list = entry.get("printed_ts", [])
        msg_list = entry.get("messages", [])

        if not isinstance(ts_list, list) or not isinstance(msg_list, list):
            return json.dumps(
                {"error": "Invalid terminal entry: 'printed_ts' and 'messages' must be lists."},
                indent=2
            )

        # Pair up to the shortest length
        n = min(len(ts_list), len(msg_list))
        lines: List[str] = [f"{ts_list[i]} : {msg_list[i]}" for i in range(n)]

        result = {
            "messages": lines[32:]
        }
        if len(ts_list) != len(msg_list):
            result["note"] = "Lengths differ; output truncated to the shortest list."

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_all_terminal_message",
                "description": "List all terminal messages formatted as 'timestamp : message'.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }


TOOLS = [
    AuthenticateUser(),
    GetRepoInfoForOwner(),
    GetBranchContent(),
    DeleteRepository(),
    CreateRepository(),
    AddNewFileInRepo(),
    UpdateFileInRepo(),
    DeleteFileInRepo(),
    CreateNewBranch(),
    DeleteBranch(),
    MergeBranch(),
    InitialCommit(),
    MakeCommit(),
    CreatePullRequest(),
    GetPRDetails(),
    ListOfPRForRepo(),
    AddPullRequestComment(),
    AssignPullRequestReviewers(),
    ApprovePR(),
    MarkPRasMerged(),
    CreateNewIssue(),
    GetAllIssuesForRepo(),
    AddCommentToIssue(),
    CloseIssue(),
    CreateCodeScanningAlert(),
    GetAlertDetails(),
    ListOpenAlertsForRepo(),
    DismissAlert(),
    ListAllTerminalMessage(),



]