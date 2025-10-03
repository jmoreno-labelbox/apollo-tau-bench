import calendar
import json
import os
import random
import uuid
from datetime import datetime, timezone
from typing import Any

from tau_bench.envs.tool import Tool

random.seed(42)

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


def get_data(elements_list, element_name):
    pass
    return next((c for c in elements_list if c["username"] == element_name), None)


def load_json(filename):
    pass
    with open(os.path.join(DATA_DIR, filename), encoding="utf-8") as f:
        return json.load(f)


def get_repo_with_owner(repositories, repo, owner):
    pass
    return next(
        (r for r in repositories if r["repo_name"] == repo and r["owner"] == owner),
        None,
    )


def add_months(orig_date: datetime, months: int) -> datetime:
    """Return a new datetime that is `months` after `orig_date`, capping the day to month's length."""
    pass
    month = orig_date.month - 1 + months
    year = orig_date.year + month // 12
    month = month % 12 + 1
    day = min(orig_date.day, calendar.monthrange(year, month)[1])
    return orig_date.replace(year=year, month=month, day=day)


# 
class AuthenticateUserTool(Tool):
    """
    Tool to verify a customer's identity based on their official ID document.

    This tool confirms whether the given document corresponds to a known customer
    based on the customer_id and document number.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Validates customer identity and returns a structured result.

        get_info() -> Dict[str, Any]:
            Returns metadata about the expected input parameters and verification logic.
    """

    @staticmethod
    def invoke(data: dict[str, Any], username: str = None, email: str = None, auth_key: str = None) -> str:
        user_name = username
        user_email = email
        auth_key = auth_key

        if not user_name or not user_email:
            payload = {
                    "status": "error",
                    "message": "Missing required parameters: 'user_name' and/or 'user_email'.",
                    "required": ["user_name", "user_email"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        users = data.get("authentication", [])
        user = next((c for c in users if c["username"] == user_name), None)
        #user = get_data(users, user_name)

        if not user:
            payload = {"status": "fail", "verified": False, "reason": "User Name not found"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        elif user_email != user["email"]:
            payload = {
                    "status": "fail",
                    "verified": False,
                    "reason": "Incorrect user email ID",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        elif auth_key != user["auth_key"]:
            payload = {
                    "status": "fail",
                    "verified": False,
                    "reason": "Incorrect user authentication key",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {"status": "success", "verified": True, "confidence": 0.97}
            out = json.dumps(
                payload, indent=2
            )
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "authenticateUser",
                "description": "Authenticate user using user name, email, and auth key.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "Unique identifier of the user in the database.",
                        },
                        "email": {
                            "type": "string",
                            "description": "Unique email address of the user.",
                        },
                    },
                    "required": ["username", "email"],
                },
            },
        }


# 
class SearchRepositoriesTool(Tool):
    """
    Tool to verify a customer's identity based on their official ID document.

    This tool confirms whether the given document corresponds to a known customer
    based on the customer_id and document number.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Validates customer identity and returns a structured result.

        get_info() -> Dict[str, Any]:
            Returns metadata about the expected input parameters and verification logic.
    """

    @staticmethod
    def invoke(data: dict[str, Any], query: str = None) -> str:
        if not query:
            payload = {
                    "status": "error",
                    "message": "Missing required parameters: 'query'.",
                    "required": ["query"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repos = data.get("repositories", [])
        repo = next((c for c in repos if c["repo_name"] == query), None)
        #repo = get_data(repos, query)

        if not repo:
            payload = {
                    "status": "success",
                    "exists": False,
                    "message": "Target repo not found",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {"status": "success", "exists": True, "message": "Target repo found"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchRepositories",
                "description": "Search if the target repository already exists in the database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Repository name to search in the database.",
                        },
                    },
                    "required": ["query"],
                },
            },
        }


# 
class UpdateRepositoryNameTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], target_name: str = None, repo_already_exists: bool = False) -> str:
        if not target_name:
            payload = {
                    "status": "error",
                    "message": "Missing required parameters: 'target_name'.",
                    "required": ["target_name"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if repo_already_exists:
            new_target_name = target_name + "_v2"
            repos = data.get("repositories", [])
            repo = next((c for c in repos if c["repo_name"] == new_target_name), None)
            #repo = get_data(repos, new_target_name)

            if not repo:
                payload = {
                        "status": "success",
                        "target_name": new_target_name,
                        "message": "Target repo name updated",
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            else:
                payload = {
                        "status": "error",
                        "message": f"New Target repo name {new_target_name} already exists in the database.",
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        else:
            payload = {
                    "status": "success",
                    "target_name": target_name,
                    "message": "Target repo name unchanged",
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
                "name": "updateRepositoryName",
                "description": "Updates the name of the target repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_name": {
                            "type": "string",
                            "description": "Repository name to search in the database.",
                        },
                        "repo_already_exists": {
                            "type": "boolean",
                            "description": "Does the repository already exist in the database?",
                        },
                    },
                    "required": ["target_name", "repo_already_exists"],
                },
            },
        }


# 
class CreateRepositoryTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], target_name: str = None, description: str = None, private_flag: bool = None, auto_init_flag: bool = None) -> str:
        repos = data.get("repositories", [])

        new_repo = {
            "owner": "maya-w",
            "repo_name": target_name,
            "description_nullable": description,
            "private_flag": private_flag,
            "auto_init_flag": auto_init_flag,
            "default_branch": "main",
            "file_paths": [],
            "file_contents": [],
        }

        repos.append(new_repo)
        payload = {"repo_name": target_name, "status": "Created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRepository",
                "description": "Create a new repository in the database",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_name": {
                            "type": "string",
                            "description": "Created repository name",
                        },
                        "description": {
                            "type": "string",
                            "description": "Detailed issue description",
                        },
                        "private_flag": {
                            "type": "boolean",
                            "description": "Is it private repository",
                        },
                        "auto_init": {
                            "type": "boolean",
                            "description": "Should the repository be auto-initialized with a README?",
                        },
                    },
                    "required": [
                        "target_name",
                        "description",
                        "private_flag",
                        "auto_init",
                    ],
                },
            },
        }


# 
class CreateOrUpdateFileTool(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str = None,
        repo: str = None,
        path: str = None,
        content: str = None,
        message: str = None,
        branch: str = None
    ) -> str:
        if not all([owner, repo, path, content, message, branch]):
            payload = {
                "status": "error",
                "message": "Missing required parameters for create_or_update_file.",
                "required": [
                    "owner",
                    "repo",
                    "path",
                    "content",
                    "message",
                    "branch",
                ],
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repositories = data.get("repositories", [])
        repository = next(
            (r for r in repositories if r["repo_name"] == repo and r["owner"] == owner),
            None,
        )
        #repository = get_repo_with_owner(repositories, repo, owner)

        if not repository:
            payload = {
                "status": "error",
                "message": f"Repository '{repo}' not found for owner '{owner}'.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Check if file already exists
        file_index = None
        try:
            file_index = repository.get("file_paths", []).index(path)
        except ValueError:
            print(f"File {path} does not exist. Creating new file!")

        if file_index is None:
            repository.setdefault("file_paths", []).append(path)
            repository.setdefault("file_contents", []).append(content)
        else:
            repository["file_contents"][file_index] = content

        #Simulate adding a commit
        repository.setdefault("commits", []).append(
            {
                "commit_shas": [str(uuid.uuid4())[:6]],  #Short SHA
                "commit_messages": [message],
                "commit_authors": [[owner]],
                "commit_timestamps": [[datetime.now(timezone.utc).isoformat()]],
                "branch_names": [branch],
            }
        )
        payload = {
            "status": "success",
            "message": f"File '{path}' created/updated successfully in repository '{repo}'.",
            "commit_sha": repository["commits"][-1]["commit_shas"][0],
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
                "name": "createOrUpdateFile",
                "description": "Creates or updates a file in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "The owner of the repository.",
                        },
                        "repo": {
                            "type": "string",
                            "description": "The name of the repository.",
                        },
                        "path": {
                            "type": "string",
                            "description": "The path of the file to create/update.",
                        },
                        "content": {
                            "type": "string",
                            "description": "The content of the file.",
                        },
                        "message": {
                            "type": "string",
                            "description": "The commit message for the change.",
                        },
                        "branch": {
                            "type": "string",
                            "description": "The branch to commit to.",
                        },
                    },
                    "required": [
                        "owner",
                        "repo",
                        "path",
                        "content",
                        "message",
                        "branch",
                    ],
                },
            },
        }


# 
class GetFileContentsTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, path: str = None, ref: str = "main") -> str:
        if not all([owner, repo, path]):
            payload = {
                    "status": "error",
                    "message": "Missing required parameters for get_file_contents.",
                    "required": ["owner", "repo", "path"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repositories = data.get("repositories", [])
        repository = next(
            (r for r in repositories if r["repo_name"] == repo and r["owner"] == owner),
            None,
        )

        if not repository:
            payload = {
                    "status": "error",
                    "message": f"Repository '{repo}' not found for owner '{owner}'.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if path in repository.get("file_contents", {}):
            payload = {
                    "status": "success",
                    "content": repository["file_contents"][path],
                    "path": path,
                    "commit_sha": (
                        repository.get("commits", [{}])[-1].get("commit_shas", [""])[0]
                        if repository.get("commits")
                        else ""
                    ),
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                    "status": "error",
                    "message": f"File '{path}' not found in repository '{repo}'.",
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
                "name": "getFileContents",
                "description": "Gets the content of a file in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "The owner of the repository.",
                        },
                        "repo": {
                            "type": "string",
                            "description": "The name of the repository.",
                        },
                        "path": {
                            "type": "string",
                            "description": "The path of the file.",
                        },
                        "ref": {
                            "type": "string",
                            "description": "The branch or commit SHA to get the file from.",
                        },
                    },
                    "required": ["owner", "repo", "path"],
                },
            },
        }


# 
class ListCommitsTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, path: str = None) -> str:
        # This parameter seems unused in the provided data structure for commits, but kept for consistency if needed later.

        if not all([owner, repo]):
            payload = {
                    "status": "error",
                    "message": "Missing required parameters for list_commits.",
                    "required": ["owner", "repo"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repositories = data.get("repositories", [])
        repository = next(
            (r for r in repositories if r["repo_name"] == repo and r["owner"] == owner),
            None,
        )

        if not repository:
            payload = {
                    "status": "error",
                    "message": f"Repository '{repo}' not found for owner '{owner}'.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        commits_data = repository.get("commits", [])
        payload = {"status": "success", "commits": commits_data}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listCommits",
                "description": "Lists the commits in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "The owner of the repository.",
                        },
                        "repo": {
                            "type": "string",
                            "description": "The name of the repository.",
                        },
                        "path": {
                            "type": "string",
                            "description": "The path to filter commits by (optional).",
                        },
                    },
                    "required": ["owner", "repo"],
                },
            },
        }


# 
class SearchCodeTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, query: str = None) -> str:
        if not all([owner, repo, query]):
            payload = {
                    "status": "error",
                    "message": "Missing required parameters for search_code.",
                    "required": ["owner", "repo", "query"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repositories = data.get("repositories", [])
        repository = next(
            (r for r in repositories if r["repo_name"] == repo and r["owner"] == owner),
            None,
        )

        if not repository:
            payload = {
                    "status": "error",
                    "message": f"Repository '{repo}' not found for owner '{owner}'.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Search code based on file contents
        found_occurrences = []
        for file_path, file_content in zip(
            repository.get("file_paths", {}), repository.get("file_contents", {})
        ):
            if query in file_content:
                # Code snippet contains the keyword
                found_occurrences.append(
                    {
                        "path": file_path,
                        "line": file_content.count(
                            query
                        ),  # A simplistic way to indicate presence
                        "match": query,
                    }
                )
        payload = {"status": "success", "query": query, "occurrences": found_occurrences}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchCode",
                "description": "Searches for code patterns within the files of a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "The owner of the repository.",
                        },
                        "repo": {
                            "type": "string",
                            "description": "The name of the repository.",
                        },
                        "query": {
                            "type": "string",
                            "description": "The code pattern to search for.",
                        },
                    },
                    "required": ["owner", "repo", "query"],
                },
            },
        }


# 
class ListCodeScanningAlertsTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None) -> str:
        if not all([owner, repo]):
            payload = {
                    "status": "error",
                    "message": "Missing required parameters for list_code_scanning_alerts.",
                    "required": ["owner", "repo"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repositories = data.get("repositories", [])
        repository = next(
            (r for r in repositories if r["repo_name"] == repo and r["owner"] == owner),
            None,
        )

        if not repository:
            payload = {
                    "status": "error",
                    "message": f"Repository '{repo}' not found for owner '{owner}'.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        alerts = data.get("code_scanning_alerts", [])
        repo_alerts = [
            alert
            for alert in alerts
            if alert["owner"] == owner and alert["repo_name"] == repo
        ]
        payload = {"status": "success", "alerts": repo_alerts}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listCodeScanningAlerts",
                "description": "Lists code scanning alerts for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "The owner of the repository.",
                        },
                        "repo": {
                            "type": "string",
                            "description": "The name of the repository.",
                        },
                    },
                    "required": ["owner", "repo"],
                },
            },
        }


#--- New tools for Task 2 ---
# 
class CreateBranchTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, branch_name: str = None, sha: str = None) -> str:
        if not all([owner, repo, branch_name, sha]):
            payload = {
                    "status": "error",
                    "message": "Missing required parameters for create_branch.",
                    "required": ["owner", "repo", "branch_name", "sha"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repositories = data.get("repositories", [])
        repository = next(
            (r for r in repositories if r["repo_name"] == repo and r["owner"] == owner),
            None,
        )

        if not repository:
            payload = {
                    "status": "error",
                    "message": f"Repository '{repo}' not found for owner '{owner}'.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Simulate creating a branch
        repository.setdefault("branches", []).append(
            {"name": branch_name, "commit_sha": sha}
        )
        repository.setdefault("branch_files", []).append(
            []
        )  # Add empty file list for new branch
        repository.setdefault("branch_contents", []).append(
            []
        )  # Add empty contents list
        payload = {
                "status": "success",
                "message": f"Branch '{branch_name}' created successfully.",
                "ref": f"refs/heads/{branch_name}",
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
                "name": "createBranch",
                "description": "Creates a new branch in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "The owner of the repository.",
                        },
                        "repo": {
                            "type": "string",
                            "description": "The name of the repository.",
                        },
                        "branch_name": {
                            "type": "string",
                            "description": "The name of the new branch.",
                        },
                        "sha": {
                            "type": "string",
                            "description": "The SHA of the commit to branch from.",
                        },
                    },
                    "required": ["owner", "repo", "branch_name", "sha"],
                },
            },
        }


# 
class CreatePullRequestTool(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str = None,
        repo: str = None,
        title: str = None,
        body: str = None,
        head: str = None,
        base: str = "main"
    ) -> str:
        if not all([owner, repo, title, body, head, base]):
            payload = {
                "status": "error",
                "message": "Missing required parameters for create_pull_request.",
                "required": ["owner", "repo", "title", "body", "head", "base"],
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repositories = data.get("repositories", [])
        repository = next(
            (r for r in repositories if r["repo_name"] == repo and r["owner"] == owner),
            None,
        )

        if not repository:
            payload = {
                "status": "error",
                "message": f"Repository '{repo}' not found for owner '{owner}'.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Simulate creating a pull request
        pr_number = len(repository.get("pull_requests", [])) + 1
        repository.setdefault("pull_requests", []).append(
            {
                "pr_number": pr_number,
                "owner": owner,
                "repo_name": repo,
                "pr_titles": [title],
                "pr_bodies": [body],
                "pr_states": ["open"],
                "head_branches": [head],
                "base_branches": [base],
                "head_shas": [""],  # Placeholder for SHA
                "mergeable_flags": [True],
                "merged_flags": [False],
                "pr_files": [],  # This will be populated by get_pull_request_files later
                "pr_comments": [],
                "pr_comment_users": [],
                "reviewers": [],
                "review_states": [],
                "review_events": [],
                "created_ts": [datetime.now(timezone.utc).isoformat()],
                "updated_ts": [datetime.now(timezone.utc).isoformat()],
            }
        )
        payload = {
            "status": "success",
            "message": f"Pull request #{pr_number} created successfully.",
            "pr_number": pr_number,
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
                "name": "createPullRequest",
                "description": "Creates a pull request from a head branch to a base branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "The owner of the repository.",
                        },
                        "repo": {
                            "type": "string",
                            "description": "The name of the repository.",
                        },
                        "title": {
                            "type": "string",
                            "description": "The title of the pull request.",
                        },
                        "body": {
                            "type": "string",
                            "description": "The body/description of the pull request.",
                        },
                        "head": {
                            "type": "string",
                            "description": "The name of the branch where your changes are implemented.",
                        },
                        "base": {
                            "type": "string",
                            "description": "The name of the branch you want your changes pulled into.",
                        },
                    },
                    "required": ["owner", "repo", "title", "body", "head", "base"],
                },
            },
        }


# 
class GetPullRequestTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, pr_number: int = None) -> str:
        if not all([owner, repo, pr_number]):
            payload = {
                    "status": "error",
                    "message": "Missing required parameters for get_pull_request.",
                    "required": ["owner", "repo", "pr_number"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repositories = data.get("repositories", [])
        repository = next(
            (r for r in repositories if r["repo_name"] == repo and r["owner"] == owner),
            None,
        )

        if not repository:
            payload = {
                    "status": "error",
                    "message": f"Repository '{repo}' not found for owner '{owner}'.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        pull_requests = repository.get("pull_requests", [])
        pull_request = next(
            (pr for pr in pull_requests if pr["pr_number"] == pr_number), None
        )

        if not pull_request:
            payload = {
                    "status": "error",
                    "message": f"Pull request #{pr_number} not found in repository '{repo}'.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"status": "success", "pull_request": pull_request}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPullRequest",
                "description": "Retrieves a specific pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "The owner of the repository.",
                        },
                        "repo": {
                            "type": "string",
                            "description": "The name of the repository.",
                        },
                        "pr_number": {
                            "type": "integer",
                            "description": "The number of the pull request.",
                        },
                    },
                    "required": ["owner", "repo", "pr_number"],
                },
            },
        }


# 
class GetPullRequestFilesTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, pr_number: int = None) -> str:
        if not all([owner, repo, pr_number]):
            payload = {
                    "status": "error",
                    "message": "Missing required parameters for get_pull_request_files.",
                    "required": ["owner", "repo", "pr_number"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repositories = data.get("repositories", [])
        repository = next(
            (r for r in repositories if r["repo_name"] == repo and r["owner"] == owner),
            None,
        )

        if not repository:
            payload = {
                    "status": "error",
                    "message": f"Repository '{repo}' not found for owner '{owner}'.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        pull_requests = repository.get("pull_requests", [])
        pull_request = next(
            (pr for pr in pull_requests if pr["pr_number"] == pr_number), None
        )

        if not pull_request:
            payload = {
                    "status": "error",
                    "message": f"Pull request #{pr_number} not found in repository '{repo}'.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # In a real scenario, you would fetch the files associated with the PR's commits.
        # For simulation, we'll return the file_paths from the repository's current state
        # that were likely involved in the PR's HEAD branch.
        head_branch = pull_request.get("head_branches", [""])[0]
        if head_branch:
            branch_index = next(
                (
                    i
                    for i, branch in enumerate(repository.get("branches", []))
                    if branch["name"] == head_branch
                ),
                -1,
            )
            if branch_index != -1:
                pr_files = repository.get("branch_files", [[]])[branch_index]
            else:
                pr_files = []  # Default if branch not found
        else:
            pr_files = []  # Default if no head branch specified

        # Update the PR object with the simulated files
        pull_request["pr_files"] = [{"filename": f} for f in pr_files]
        payload = {"status": "success", "files": [{"filename": f} for f in pr_files]}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPullRequestFiles",
                "description": "Retrieves the list of files changed in a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "The owner of the repository.",
                        },
                        "repo": {
                            "type": "string",
                            "description": "The name of the repository.",
                        },
                        "pr_number": {
                            "type": "integer",
                            "description": "The number of the pull request.",
                        },
                    },
                    "required": ["owner", "repo", "pr_number"],
                },
            },
        }


# 
class ListPullRequestsTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None) -> str:
        if not all([owner, repo]):
            payload = {
                    "status": "error",
                    "message": "Missing required parameters for list_pull_requests.",
                    "required": ["owner", "repo"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repositories = data.get("repositories", [])
        repository = next(
            (r for r in repositories if r["repo_name"] == repo and r["owner"] == owner),
            None,
        )

        if not repository:
            payload = {
                    "status": "error",
                    "message": f"Repository '{repo}' not found for owner '{owner}'.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        pull_requests = repository.get("pull_requests", [])
        payload = {"status": "success", "pull_requests": pull_requests}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListPullRequests",
                "description": "Lists all pull requests for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "The owner of the repository.",
                        },
                        "repo": {
                            "type": "string",
                            "description": "The name of the repository.",
                        },
                    },
                    "required": ["owner", "repo"],
                },
            },
        }


# 
class GetPullRequestStatusTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, pr_number: int = None) -> str:
        if not all([owner, repo, pr_number]):
            payload = {
                    "status": "error",
                    "message": "Missing required parameters for get_pull_request_status.",
                    "required": ["owner", "repo", "pr_number"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repositories = data.get("repositories", [])
        repository = next(
            (r for r in repositories if r["repo_name"] == repo and r["owner"] == owner),
            None,
        )

        if not repository:
            payload = {
                    "status": "error",
                    "message": f"Repository '{repo}' not found for owner '{owner}'.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        pull_requests = repository.get("pull_requests", [])
        pull_request = next(
            (pr for pr in pull_requests if pr["pr_number"] == pr_number), None
        )

        if not pull_request:
            payload = {
                    "status": "error",
                    "message": f"Pull request #{pr_number} not found in repository '{repo}'.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Simulate getting status, e.g., checks and mergeability
        #In a real API, this would be more detailed.
        status = {
            "checks": [
                {"name": "CI Check", "status": "success"},
                {"name": "Code Style", "status": "success"},
            ],
            "mergeable": pull_request.get("mergeable_flags", [False])[0],
            "state": pull_request.get("pr_states", ["open"])[0],
        }
        payload = {"status": "success", "pull_request_status": status}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPullRequestStatus",
                "description": "Retrieves the status of a pull request, including checks and mergeability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "The owner of the repository.",
                        },
                        "repo": {
                            "type": "string",
                            "description": "The name of the repository.",
                        },
                        "pr_number": {
                            "type": "integer",
                            "description": "The number of the pull request.",
                        },
                    },
                    "required": ["owner", "repo", "pr_number"],
                },
            },
        }


TOOLS = [
    #Task 1
    AuthenticateUserTool(),
    SearchRepositoriesTool(),
    UpdateRepositoryNameTool(),
    CreateRepositoryTool(),
    CreateOrUpdateFileTool(),
    GetFileContentsTool(),
    ListCommitsTool(),
    SearchCodeTool(),
    ListCodeScanningAlertsTool(),
    #Task 2
    CreateBranchTool(),
    CreatePullRequestTool(),
    GetPullRequestTool(),
    GetPullRequestFilesTool(),
    ListPullRequestsTool(),
    GetPullRequestStatusTool(),
]
"""
DevSecOps Tools
===============

A deterministic toolkit for analyzing repositories, commits, issues,
pull requests, security alerts, and terminal logs.

Notes:
- All lookups use `data.get(...)`.
- No external writes or persistence: tools only work in memory.
- All IDs and relationships must be deterministic.
- CURRENT_DATE is fixed and must be used for deterministic outputs.
"""

import hashlib
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool

CURRENT_DATE = "2025-08-26"

ERROR_MESSAGES = {
    "INVALID_PARAMETER_TYPE": "Parameter '{param}' must be a {expected_type}.",
    "REQUIRED_PARAMETER": "Parameter '{param}' is required.",
    "NOT_FOUND": "{entity} with id '{entity_id}' not found.",
    "ALREADY_EXISTS": "{entity} with id '{entity_id}' already exists.",
    "NO_DATA_FOUND": "No data found for {entity}.",
}


def _safe_id(
    obj: dict[str, Any],
    explicit_id: str,
    fallback_prefix: str,
    fallback_fields: list[str],
) -> str:
    """
    Generate a deterministic ID for an object, with robust fallback.

    Args:
        obj (Dict[str, Any]): The dictionary representing the entity.
        explicit_id (str): Key name for an existing ID in the object (e.g., "issue_id").
        fallback_prefix (str): Prefix for the ID (e.g., "ISSUE_", "PR_", "ALERT_").
        fallback_fields (List[str]): List of fields to build the ID seed (used in order).

    Returns:
        str: Deterministic ID string derived from existing ID, selected fields,
             or the full object JSON as fallback.
    """
    pass
    if obj.get(explicit_id):
        return obj[explicit_id]

    seed_parts = [str(obj.get(f, "")) for f in fallback_fields if obj.get(f)]
    seed = "_".join(seed_parts)

    if not seed:
        seed = json.dumps(obj, sort_keys=True)

    return f"{fallback_prefix}{hashlib.sha1(seed.encode()).hexdigest()[:8]}"


def _normalize_user(user: Any) -> str:
    """
    Normalize user identifiers for deterministic outputs.

    Args:
        user (Any): Raw user field (string, int, or None).

    Returns:
        str: Stringified user identifier, or "unknown" if empty/None.
    """
    pass
    return str(user) if user else "unknown"


def _generate_commit_sha(repo: str, branch: str, seq: int) -> str:
    """
    Generate a deterministic 12-character hexadecimal SHA for commits.

    Args:
        repo (str): Repository name.
        branch (str): Branch name.
        seq (int): Sequential number of the commit.

    Returns:
        str: Deterministic 12-character hexadecimal SHA.
    """
    pass
    seed = f"{repo}_{branch}_{seq}"
    return hashlib.sha1(seed.encode()).hexdigest()[:12]


def _response(status: str, data_or_message: Any, error_code: str = None) -> str:
    """
    Build a standardized JSON response.

    Args:
        status (str): Response status, either "ok" or "error".
        data_or_message (Any): Data payload when status is "ok", or error message when status is "error".
        error_code (str, optional): Machine-friendly error code to include when status is "error".

    Returns:
        str: A JSON-formatted string containing either:
             {"status": "ok", "data": ...}
             or {"status": "error", "error_code": ..., "message": ...},
             indented for readability.
    """
    pass
    if status == "ok":
        payload = {"status": "ok", "data": data_or_message}
        out = json.dumps(payload, indent=2)
        return out
    payload = {
            "status": "error",
            "error_code": error_code or "UNKNOWN_ERROR",
            "message": data_or_message,
        }
    out = json.dumps(
        payload, indent=2,
    )
    return out


def _days_between(start: str, end: str) -> int:
    """
    Calculate the absolute number of days between two date strings.

    Supports flexible parsing (YYYY-MM-DD, YYYY/MM/DD).
    Returns 0 if parsing fails.

    Args:
        start (str): Start date string.
        end (str): End date string.

    Returns:
        int: Absolute difference in days, or 0 on error.
    """
    pass
    if not isinstance(start, str) or not isinstance(end, str):
        return 0

    formats = ["%Y-%m-%d", "%Y/%m/%d"]
    for fmt in formats:
        try:
            start_dt = datetime.strptime(start, fmt)
            end_dt = datetime.strptime(end, fmt)
            return abs((end_dt - start_dt).days)
        except ValueError:
            continue
    return 0


def _validate_param(
    kwargs: dict[str, Any],
    param: str,
    expected_type: type,
    required: bool = True,
    subtype: type = None,
) -> Any:
    """
    Validate and retrieve a parameter from keyword arguments.

    Performs deterministic validation on the presence and type of a parameter,
    with optional subtype checks when the parameter is a list.

    Args:
        kwargs (Dict[str, Any]): Dictionary of keyword arguments to validate.
        param (str): The name of the parameter to validate.
        expected_type (type): Expected top-level type of the parameter (e.g., str, list).
        required (bool, optional): Whether the parameter is required. Defaults to True.
        subtype (type, optional): Expected element type if the parameter is a list.
            For example, subtype=str enforces that all elements in the list are strings.

    Returns:
        Any: The validated parameter value if present and valid, or None if not required.
             On validation failure, returns a standardized error response.
    """
    pass
    value = kwargs.get(param)

    if required and value is None:
        return _response(
            "error", ERROR_MESSAGES["REQUIRED_PARAMETER"].format(param=param)
        )

    if value is not None and not isinstance(value, expected_type):
        return _response(
            "error",
            ERROR_MESSAGES["INVALID_PARAMETER_TYPE"].format(
                param=param, expected_type=expected_type.__name__
            ),
        )

    if subtype and isinstance(value, list):
        for item in value:
            if not isinstance(item, subtype):
                return _response(
                    "error",
                    f"Parameter '{param}' must be a list of {subtype.__name__}.",
                )

    return value


#================================================================
#Repositories Tools
#================================================================


class GetRepositoryMetadataTool(Tool):
    """
    Retrieve deterministic metadata for a specific repository by name.

    This tool searches the dataset for a repository with the given name and
    returns its metadata, augmented with a deterministic `report_date` field.

    Usage:
        - Provide the repository name as input.
        - Returns a JSON response with the repository metadata or an error if not found.

    Input Parameters:
        repo_name (str): The name of the repository to look up.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if found, "error" otherwise.
            - data: Repository metadata with deterministic `report_date`.

    Errors:
        - Returns an error response if `repo_name` is missing or not a string.
        - Returns an error if no repository with the given name exists in the dataset.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        repos = data.get("repositories", [])
        repo_info = next((r for r in repos if r.get("name") == repo_name), None)

        if not repo_info:
            return _response(
                "error",
                ERROR_MESSAGES["NOT_FOUND"].format(
                    entity="Repository", entity_id=repo_name
                ),
                "NOT_FOUND",
            )

        result = {
            **repo_info,
            "report_date": CURRENT_DATE,
        }
        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getRepositoryMetadata",
                "description": "Get deterministic metadata for a repository by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class ListRepositoriesTool(Tool):
    """
    List all repositories with deterministic metadata.

    This tool retrieves all repositories from the dataset and augments each entry
    with a deterministic `report_date` field set to CURRENT_DATE. It does not filter
    by name or other attributes — all repositories present in the dataset are returned.

    Usage:
        - No input parameters are required.
        - Returns metadata for every repository in the dataset.

    Input Parameters:
        None

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: A list of repositories, each enriched with a `report_date` field.
    """

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        repos = data.get("repositories", [])
        result = [{**r, "report_date": CURRENT_DATE} for r in repos]
        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRepositories",
                "description": "List all repositories with deterministic metadata.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class CreateRepositoryTool(Tool):
    """
    Create a new repository deterministically (in-memory only).

    This tool registers a new repository in the dataset with a unique deterministic ID.
    The ID is generated using `_safe_id`, based on the repository name.
    Each repository is also stamped with `created_at`, `updated_at`, and a fixed
    `default_branch` value of "main".

    Usage:
        - Provide the repository name, visibility flag, and optionally a description.
        - If a repository with the same name already exists, an error is returned.

    Input Parameters:
        repo_name (str): The unique name of the repository.
        description (str, optional): A short description of the repository. Defaults to "".
        private (bool): Whether the repository is private.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if created successfully, or "error" otherwise.
            - data: The repository metadata, including a deterministic `repo_id`.

    Errors:
        - Returns an error if `repo_name` or `private` are missing or of the wrong type.
        - Returns an error if a repository with the given name already exists.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, description: str = None, private: bool = False) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            description = _validate_param({"description": description}, "description", str, required=False)
            private = _validate_param({"private": private}, "private", bool)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        repos = data.get("repositories", [])
        if any(r.get("name") == repo_name for r in repos):
            return _response(
                "error",
                ERROR_MESSAGES["ALREADY_EXISTS"].format(
                    entity="Repository", entity_id=repo_name
                ),
                "ALREADY_EXISTS",
            )

        new_repo = {
            "name": repo_name,
            "description": description or "",
            "private": private,
            "created_at": CURRENT_DATE,
            "updated_at": CURRENT_DATE,
            "default_branch": "main",
        }
        new_repo["repo_id"] = _safe_id(new_repo, "repo_id", "REPO_", ["name"])
        repos.append(new_repo)

        return _response("ok", new_repo)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRepository",
                "description": "Create a new repository deterministically (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "description": {"type": "string"},
                        "private": {"type": "boolean"},
                    },
                    "required": ["repo_name", "private"],
                },
            },
        }


class UpdateRepositoryDescriptionTool(Tool):
    """
    Update the description of an existing repository (in-memory only).

    This tool searches for a repository by name and updates its description field.
    The `updated_at` timestamp is refreshed to the CURRENT_DATE to ensure
    deterministic versioning of repository metadata.

    Usage:
        - Provide the repository name and the new description.
        - If the repository is not found, an error response is returned.

    Input Parameters:
        repo_name (str): The unique name of the repository to update.
        description (str): The new description text for the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the update was successful, or "error" otherwise.
            - data: The updated repository metadata, including the refreshed `updated_at` field.

    Errors:
        - Returns an error if `repo_name` or `description` are missing or of the wrong type.
        - Returns an error if the repository with the given name does not exist.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, description: str = None) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            description = _validate_param({"description": description}, "description", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        repos = data.get("repositories", [])
        repo = next((r for r in repos if r.get("name") == repo_name), None)

        if not repo:
            return _response(
                "error",
                ERROR_MESSAGES["NOT_FOUND"].format(
                    entity="Repository", entity_id=repo_name
                ),
            )

        repo["description"] = description
        repo["updated_at"] = CURRENT_DATE
        return _response("ok", repo)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateRepositoryDescription",
                "description": "Update a repository description deterministically (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": ["repo_name", "description"],
                },
            },
        }


class GetRepositoryHealthSummaryTool(Tool):
    """
    Aggregate repository health metrics (issues, PRs, alerts).

    This tool generates a deterministic summary of the health of a repository,
    based on the number of open issues, open pull requests, and open security alerts.
    It provides a quick overview of repository status with an added deterministic
    `report_date` field.

    Usage:
        - Provide the repository name.
        - Returns aggregated counts of open issues, pull requests, and alerts.

    Input Parameters:
        repo_name (str): The unique name of the repository to summarize.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A dictionary with the following keys:
                - repo (str): The repository name.
                - open_issues (int): Number of open issues.
                - open_prs (int): Number of open pull requests.
                - open_alerts (int): Number of open security alerts.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or of the wrong type.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = data.get("issues", [])
        prs = data.get("pull_requests", [])
        alerts = data.get("code_scanning_alerts", [])

        result = {
            "repo": repo_name,
            "open_issues": sum(
                1
                for i in issues
                if i.get("repo") == repo_name and i.get("state") == "open"
            ),
            "open_prs": sum(
                1
                for p in prs
                if p.get("repo") == repo_name and p.get("state") == "open"
            ),
            "open_alerts": sum(
                1
                for a in alerts
                if a.get("repo") == repo_name and a.get("state") == "open"
            ),
            "report_date": CURRENT_DATE,
        }
        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRepositoryHealthSummary",
                "description": "Get a deterministic repository health summary (issues, PRs, alerts).",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


#================================================================
#Commits Tools
#================================================================


class ListCommitsByBranchTool(Tool):
    """
    List commits for a repository branch deterministically.

    This tool retrieves all commits for a given repository branch and augments
    each commit with a deterministic `report_date` field. Author fields are
    normalized with `_normalize_user` to ensure consistent outputs.

    Usage:
        - Provide the repository name and branch name.
        - Returns metadata for all commits matching that repository and branch.

    Input Parameters:
        repo_name (str): The name of the repository.
        branch (str): The branch name within the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A list of commits, each represented as a dictionary with:
                - commit_id (str): The commit SHA identifier.
                - repo (str): The repository name.
                - branch (str): The branch name.
                - message (str): The commit message.
                - author (str): The normalized author identifier.
                - timestamp (str): The commit timestamp.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` or `branch` are missing or of the wrong type.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            branch = _validate_param({"branch": branch}, "branch", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = data.get("commits", [])
        branch_commits = [
            {
                "commit_id": c.get("sha"),
                "repo": repo_name,
                "branch": branch,
                "message": c.get("message"),
                "author": _normalize_user(c.get("author")),
                "timestamp": c.get("timestamp"),
                "report_date": CURRENT_DATE,
            }
            for c in commits
            if c.get("repo") == repo_name and c.get("branch") == branch
        ]
        return _response("ok", branch_commits)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListCommitsByBranch",
                "description": "List commits for a repository branch deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name", "branch"],
                },
            },
        }


class GetCommitMetadataTool(Tool):
    """
    Retrieve deterministic metadata for a commit by SHA.

    This tool searches for a commit within a repository by its SHA identifier and
    returns all associated metadata. The output is augmented with a deterministic
    `report_date` field set to CURRENT_DATE.

    Usage:
        - Provide the repository name and the commit SHA.
        - Returns the commit metadata if found.

    Input Parameters:
        repo_name (str): The name of the repository containing the commit.
        commit_sha (str): The SHA identifier of the commit to retrieve.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the commit is found, or "error" otherwise.
            - data: A dictionary with commit metadata, including:
                - sha (str): The commit SHA identifier.
                - repo (str): The repository name.
                - branch (str): The branch where the commit resides (if available).
                - message (str): The commit message.
                - author (str): The commit author (raw value, not normalized).
                - timestamp (str): The commit timestamp.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` or `commit_sha` are missing or of the wrong type.
        - Returns an error if no commit with the given SHA exists in the repository.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, commit_sha: str) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            commit_sha = _validate_param({"commit_sha": commit_sha}, "commit_sha", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = data.get("commits", [])
        commit = next(
            (
                c
                for c in commits
                if c.get("repo") == repo_name and c.get("sha") == commit_sha
            ),
            None,
        )

        if not commit:
            return _response(
                "error",
                ERROR_MESSAGES["NOT_FOUND"].format(
                    entity="Commit", entity_id=commit_sha
                ),
                "NOT_FOUND",
            )

        result = {**commit, "report_date": CURRENT_DATE}
        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCommitMetadata",
                "description": "Retrieve deterministic metadata for a commit by SHA.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "commit_sha": {"type": "string"},
                    },
                    "required": ["repo_name", "commit_sha"],
                },
            },
        }


class AddCommitToBranchTool(Tool):
    """
    Add a deterministic commit to a repository branch (in-memory only).

    This tool simulates the addition of a new commit to a repository branch.
    Each commit is assigned a deterministic SHA identifier based on the repository,
    branch, and commit sequence number. Metadata fields (`created_at`, `updated_at`,
    `timestamp`) are set to CURRENT_DATE for deterministic outputs.

    Usage:
        - Provide repository name, branch name, commit message, and author.
        - A new commit entry is created unless a commit with the same message already
          exists on the same branch.

    Input Parameters:
        repo_name (str): The name of the repository.
        branch (str): The branch where the commit will be added.
        message (str): The commit message.
        author (str): The author of the commit.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A dictionary representing the created commit, including:
                - sha (str): Deterministic commit SHA (repo + branch + sequence).
                - repo (str): Repository name.
                - branch (str): Branch name.
                - message (str): Commit message.
                - author (str): Normalized author identifier.
                - timestamp (str): Commit timestamp (CURRENT_DATE).
                - created_at (str): Creation date (CURRENT_DATE).
                - updated_at (str): Last update date (CURRENT_DATE).

    Errors:
        - Returns an error if any required parameter is missing or of the wrong type.
        - Returns an error if a commit with the same message already exists on the branch.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, branch: str, message: str, author: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            branch = _validate_param({"branch": branch}, "branch", str)
            message = _validate_param({"message": message}, "message", str)
            author = _validate_param({"author": author}, "author", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = data.get("commits", [])
        if any(
            c.get("repo") == repo_name
            and c.get("message") == message
            and c.get("branch") == branch
            for c in commits
        ):
            return _response(
                "error",
                ERROR_MESSAGES["ALREADY_EXISTS"].format(
                    entity="Commit", entity_id=message
                ),
                "ALREADY_EXISTS",
            )

        new_commit = {
            "sha": _generate_commit_sha(repo_name, branch, len(commits) + 1),
            "repo": repo_name,
            "branch": branch,
            "message": message,
            "author": _normalize_user(author),
            "timestamp": CURRENT_DATE,
            "created_at": CURRENT_DATE,
            "updated_at": CURRENT_DATE,
        }
        commits.append(new_commit)
        return _response("ok", new_commit)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddCommitToBranch",
                "description": "Add a deterministic commit to a branch (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "message": {"type": "string"},
                        "author": {"type": "string"},
                    },
                    "required": ["repo_name", "branch", "message", "author"],
                },
            },
        }


class CountCommitsByAuthorTool(Tool):
    """
    Count commits per author for a repository.

    This tool calculates how many commits each author has made in a given repository.
    Authors are normalized using `_normalize_user` to ensure deterministic identifiers,
    and the result is returned with a deterministic `report_date`.

    Usage:
        - Provide the repository name.
        - Returns a mapping of authors to their commit counts.

    Input Parameters:
        repo_name (str): The name of the repository to analyze.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A dictionary with:
                - repo (str): The repository name.
                - commits_by_author (Dict[str, int]): Mapping of author identifiers to commit counts.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or of the wrong type.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = data.get("commits", [])
        author_counts = {}
        for c in commits:
            if c.get("repo") == repo_name:
                author = _normalize_user(c.get("author"))
                author_counts[author] = author_counts.get(author, 0) + 1

        result = {
            "repo": repo_name,
            "commits_by_author": author_counts,
            "report_date": CURRENT_DATE,
        }
        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CountCommitsByAuthor",
                "description": "Count commits per author for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class ListCommitsByDateRangeTool(Tool):
    """
    List commits for a repository within a deterministic date range.

    This tool retrieves all commits in a given repository that fall within a
    specified inclusive date range. Each commit is augmented with a deterministic
    `report_date` field. Authors are normalized using `_normalize_user`.

    Usage:
        - Provide the repository name, start date, and end date.
        - Dates must be provided in ISO 8601 format (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS).
        - Returns metadata for all commits whose timestamps fall within the range.

    Input Parameters:
        repo_name (str): The name of the repository.
        start_date (str): The start date of the range (inclusive).
        end_date (str): The end date of the range (inclusive).

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A list of commits, each represented as a dictionary with:
                - commit_id (str): The commit SHA identifier.
                - repo (str): The repository name.
                - message (str): The commit message.
                - author (str): The normalized author identifier.
                - timestamp (str): The commit timestamp.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name`, `start_date`, or `end_date` are missing or invalid types.
        - Returns an error if no commits match the specified date range.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, start_date: str, end_date: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            start_date = _validate_param({"start_date": start_date}, "start_date", str)
            end_date = _validate_param({"end_date": end_date}, "end_date", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = data.get("commits", [])
        filtered = [
            {
                "commit_id": c.get("sha"),
                "repo": repo_name,
                "message": c.get("message"),
                "author": _normalize_user(c.get("author")),
                "timestamp": c.get("timestamp"),
                "report_date": CURRENT_DATE,
            }
            for c in commits
            if c.get("repo") == repo_name
            and start_date <= c.get("timestamp", "") <= end_date
        ]
        return _response("ok", filtered)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListCommitsByDateRange",
                "description": "List commits for a repository between a start and end date (deterministic).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["repo_name", "start_date", "end_date"],
                },
            },
        }


#================================================================
#Issues Tools
#================================================================


class GetOpenIssuesTool(Tool):
    """
    Retrieve all open issues for a repository deterministically.

    This tool lists issues in the dataset that are marked as "open" for a given
    repository. Each issue is returned with a deterministic `issue_id` generated
    by `_safe_id`, normalized labels, and a `report_date`.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if issues were found, or "error" otherwise.
            - data: A list of open issues with metadata, including:
                - issue_id (str): Deterministic unique issue ID.
                - title (str): The issue title.
                - state (str): The issue state ("open").
                - assignees (List[str]): List of normalized assignee identifiers.
                - labels (List[str]): List of labels (normalized to lowercase).
                - created_at (str): Creation timestamp.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = data.get("issues", [])
        open_issues = [
            {
                "issue_id": _safe_id(
                    i, "issue_id", f"ISSUE_{repo_name}_", ["title", "body"]
                ),
                "title": i.get("title"),
                "state": i.get("state"),
                "assignees": i.get("assignees", []),
                "labels": [lbl.lower() for lbl in i.get("labels", [])],
                "created_at": i.get("created_at"),
                "report_date": CURRENT_DATE,
            }
            for i in issues
            if i.get("repo") == repo_name and i.get("state") == "open"
        ]
        return _response("ok", open_issues)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOpenIssues",
                "description": "List all open issues for a repository deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class GetClosedIssuesTool(Tool):
    """
    Retrieve all closed issues for a repository deterministically.

    This tool lists issues in the dataset that are marked as "closed" for a given
    repository. Each issue is returned with a deterministic `issue_id` generated
    by `_safe_id`, normalized labels, and a `report_date`.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if issues were found, or "error" otherwise.
            - data: A list of closed issues with metadata, including:
                - issue_id (str): Deterministic unique issue ID.
                - title (str): The issue title.
                - state (str): The issue state ("closed").
                - assignees (List[str]): List of normalized assignee identifiers.
                - labels (List[str]): List of labels (normalized to lowercase).
                - created_at (str): Creation timestamp.
                - closed_at (str): Closing timestamp.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = data.get("issues", [])
        closed_issues = [
            {
                "issue_id": _safe_id(
                    i, "issue_id", f"ISSUE_{repo_name}_", ["title", "body"]
                ),
                "title": i.get("title"),
                "labels": [lbl.lower() for lbl in i.get("labels", [])],
                "state": i.get("state"),
                "closed_at": i.get("closed_at") or CURRENT_DATE,
                "report_date": CURRENT_DATE,
            }
            for i in issues
            if i.get("repo") == repo_name and i.get("state") == "closed"
        ]
        return _response("ok", closed_issues)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetClosedIssues",
                "description": "List all closed issues for a repository deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class CreateIssueTool(Tool):
    """
    Create a new issue deterministically (in-memory only).

    This tool simulates the creation of a new issue in a repository.
    IDs are generated using `_safe_id`, and metadata such as `created_at`
    and `updated_at` are stamped with CURRENT_DATE.

    Input Parameters:
        repo_name (str): The name of the repository.
        title (str): The issue title.
        body (str): The issue description or body text.
        labels (List[str], optional): Labels for the issue (normalized to lowercase).
        assignees (List[str], optional): List of assignee identifiers.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if created successfully, or "error" otherwise.
            - data: Metadata of the created issue, including deterministic `issue_id`.

    Errors:
        - Returns an error if required parameters are missing or invalid.
        - Returns an error if an issue with the same title already exists.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        repo_name: str,
        title: str,
        body: str,
        labels: list[str] = None,
        assignees: list[str] = None
    ) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            title = _validate_param({"title": title}, "title", str)
            body = _validate_param({"body": body}, "body", str)
            labels = (
                _validate_param({"labels": labels}, "labels", list, required=False, subtype=str)
                or []
            )
            assignees = (
                _validate_param({"assignees": assignees}, "assignees", list, required=False, subtype=str)
                or []
            )
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = data.get("issues", [])
        if any(i.get("repo") == repo_name and i.get("title") == title for i in issues):
            return _response(
                "error",
                ERROR_MESSAGES["ALREADY_EXISTS"].format(
                    entity="Issue", entity_id=title
                ),
                "ALREADY_EXISTS",
            )

        new_number = len(issues) + 1
        new_issue = {
            "repo": repo_name,
            "number": new_number,
            "title": title,
            "body": body,
            "state": "open",
            "labels": [lbl.lower() for lbl in labels],
            "assignees": [_normalize_user(a) for a in assignees],
            "created_at": CURRENT_DATE,
            "updated_at": CURRENT_DATE,
        }
        new_issue["issue_id"] = _safe_id(
            new_issue, "issue_id", f"ISSUE_{repo_name}_", ["title", "body"]
        )
        issues.append(new_issue)
        return _response("ok", new_issue)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateIssue",
                "description": "Create a deterministic issue (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "labels": {"type": "array", "items": {"type": "string"}},
                        "assignees": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["repo_name", "title", "body"],
                },
            },
        }


class CloseIssueTool(Tool):
    """
    Close an existing issue deterministically (in-memory only).

    This tool changes the state of a specified issue to "closed" and
    stamps `closed_at` and `updated_at` fields with CURRENT_DATE.

    Input Parameters:
        repo_name (str): The name of the repository.
        issue_id (str): Deterministic ID of the issue to close.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if closed successfully, or "error" otherwise.
            - data: Updated issue metadata.

    Errors:
        - Returns an error if parameters are missing or invalid.
        - Returns an error if the issue does not exist in the repository.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, issue_number: int) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            issue_number = _validate_param({"issue_number": issue_number}, "issue_number", int)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = data.get("issues", [])
        issue = next(
            (
                i
                for i in issues
                if i.get("repo") == repo_name and i.get("number") == issue_number
            ),
            None,
        )

        if not issue:
            return _response(
                "error",
                ERROR_MESSAGES["NOT_FOUND"].format(
                    entity="Issue", entity_id=issue_number
                ),
                "NOT_FOUND",
            )

        issue["state"] = "closed"
        issue["closed_at"] = CURRENT_DATE
        issue["updated_at"] = CURRENT_DATE
        return _response("ok", issue)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CloseIssue",
                "description": "Close an existing issue deterministically (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "issue_number"],
                },
            },
        }


class AssignIssueTool(Tool):
    """
    Assign one or more users to an existing issue (in-memory only).

    This tool updates the `assignees` field of a specified issue.
    Assignee identifiers are normalized via `_normalize_user`.
    The `updated_at` field is refreshed deterministically.

    Input Parameters:
        repo_name (str): The name of the repository.
        issue_id (str): Deterministic ID of the issue.
        assignees (List[str]): List of users to assign to the issue.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if assignment successful, or "error" otherwise.
            - data: Updated issue metadata with new assignees.

    Errors:
        - Returns an error if required parameters are missing or invalid.
        - Returns an error if the issue does not exist.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, issue_number: int, assignees: list[str] = None) -> str:
        if assignees is None:
            assignees = []
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            issue_number = _validate_param({"issue_number": issue_number}, "issue_number", int)
            assignees = (
                _validate_param({"assignees": assignees}, "assignees", list, required=False, subtype=str)
                or []
            )
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = data.get("issues", [])
        issue = next(
            (
                i
                for i in issues
                if i.get("repo") == repo_name and i.get("number") == issue_number
            ),
            None,
        )

        if not issue:
            return _response(
                "error",
                ERROR_MESSAGES["NOT_FOUND"].format(
                    entity="Issue", entity_id=issue_number
                ),
                "NOT_FOUND",
            )

        issue["assignees"] = [_normalize_user(a) for a in assignees]
        issue["updated_at"] = CURRENT_DATE
        return _response("ok", issue)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignIssue",
                "description": "Assign users to an issue deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                        "assignees": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["repo_name", "issue_number", "assignees"],
                },
            },
        }


class ListIssuesByLabelTool(Tool):
    """
    List issues in a repository filtered by label.

    This tool retrieves all issues in a repository that contain a given label.
    Labels are normalized to lowercase to ensure deterministic matching.

    Input Parameters:
        repo_name (str): The name of the repository.
        label (str): The label to filter issues by.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: List of issues with the specified label, including:
                - issue_id (str): Deterministic unique issue ID.
                - title (str): The issue title.
                - state (str): The issue state.
                - assignees (List[str]): Normalized assignee identifiers.
                - labels (List[str]): Normalized labels.
                - created_at (str): Creation date.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if parameters are missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, label: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            label = _validate_param({"label": label}, "label", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = data.get("issues", [])
        labeled = [
            {
                "issue_id": _safe_id(
                    i, "issue_id", f"ISSUE_{repo_name}_", ["title", "body"]
                ),
                "title": i.get("title"),
                "labels": [lbl.lower() for lbl in i.get("labels", [])],
                "state": i.get("state"),
                "report_date": CURRENT_DATE,
            }
            for i in issues
            if i.get("repo") == repo_name
            and label.lower() in [lbl.lower() for lbl in i.get("labels", [])]
        ]
        return _response("ok", labeled)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListIssuesByLabel",
                "description": "Retrieve issues by label for a repository deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "label": {"type": "string"},
                    },
                    "required": ["repo_name", "label"],
                },
            },
        }


class GetIssueAgingReportTool(Tool):
    """
    Generate a deterministic aging report for issues in a repository.

    This tool calculates how many days each issue has been open based on its
    `created_at` date compared to CURRENT_DATE. It provides insights into
    long-standing or unresolved issues.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: List of issues with their aging information, including:
                - issue_id (str): Deterministic issue identifier.
                - title (str): Issue title.
                - state (str): Current issue state.
                - created_at (str): Issue creation date.
                - days_open (int): Number of days the issue has been open.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = data.get("issues", [])
        aging = [
            {
                "issue_id": _safe_id(
                    i, "issue_id", f"ISSUE_{repo_name}_", ["title", "body"]
                ),
                "title": i.get("title"),
                "state": i.get("state"),
                "created_at": i.get("created_at"),
                "days_open": (
                    _days_between(i.get("created_at", CURRENT_DATE), CURRENT_DATE)
                    if i.get("state") == "open"
                    else 0
                ),
                "report_date": CURRENT_DATE,
            }
            for i in issues
            if i.get("repo") == repo_name
        ]
        return _response("ok", aging)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetIssueAgingReport",
                "description": "Generate deterministic report of how long issues have been open.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


#================================================================
#Pull Requests Tools
#================================================================


class ListPullRequestsTool(Tool):
    """
    List all pull requests for a repository deterministically.

    This tool retrieves all pull requests for a repository.
    Each pull request is returned with a deterministic `pr_id`
    (via `_safe_id`) and includes a `report_date`.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: A list of pull requests with metadata, including:
                - pr_id (str): Deterministic unique pull request ID.
                - title (str): Pull request title.
                - state (str): Current state ("open", "closed", or "merged").
                - created_at (str): PR creation date.
                - updated_at (str): PR last update date.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, state: str = None) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = data.get("pull_requests", [])
        repo_prs = [
            {
                "pr_id": _safe_id(
                    pr,
                    "pr_id",
                    f"PR_{repo_name}_",
                    ["title", "head_branch", "base_branch"],
                ),
                "title": pr.get("title"),
                "state": pr.get("state"),
                "created_at": pr.get("created_at"),
                "report_date": CURRENT_DATE,
            }
            for pr in prs
            if pr.get("repo") == repo_name
            and (state is None or pr.get("state") == state)
        ]
        return _response("ok", repo_prs)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListPullRequests",
                "description": "List pull requests for a repository (optionally filter by state).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "state": {"type": "string"},
                    },
                    "required": ["repo_name"],
                },
            },
        }


class GetPullRequestMetadataTool(Tool):
    """
    Retrieve deterministic metadata for a pull request by ID.

    This tool searches for a pull request by its deterministic ID (`pr_id`)
    and returns its metadata, augmented with a `report_date`.

    Input Parameters:
        repo_name (str): The name of the repository.
        pr_id (str): Deterministic ID of the pull request.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if found, or "error" otherwise.
            - data: A dictionary with pull request metadata, including deterministic `pr_id`.

    Errors:
        - Returns an error if parameters are missing or invalid.
        - Returns an error if no pull request with the given ID exists.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, pr_number: int) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            pr_number = _validate_param({"pr_number": pr_number}, "pr_number", int)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = data.get("pull_requests", [])
        pr = next(
            (
                p
                for p in prs
                if p.get("repo") == repo_name and p.get("number") == pr_number
            ),
            None,
        )

        if not pr:
            return _response(
                "error",
                ERROR_MESSAGES["NOT_FOUND"].format(
                    entity="Pull Request", entity_id=pr_number
                ),
                "NOT_FOUND",
            )

        result = {
            **pr,
            "pr_id": _safe_id(
                pr, "pr_id", f"PR_{repo_name}_", ["title", "head_branch", "base_branch"]
            ),
            "report_date": CURRENT_DATE,
        }
        if "author" in result:
            result["author"] = _normalize_user(result["author"])
        if "reviewers" in result:
            result["reviewers"] = [
                _normalize_user(r) for r in result.get("reviewers", [])
            ]

        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPullRequestMetadata",
                "description": "Retrieve deterministic metadata for a pull request by number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "pr_number"],
                },
            },
        }


class OpenPullRequestTool(Tool):
    """
    Open a new pull request deterministically (in-memory only).

    This tool simulates the creation of a new pull request in a repository.
    IDs are generated using `_safe_id` based on the title and branches.
    The PR state defaults to "open", and metadata is stamped with CURRENT_DATE.

    Input Parameters:
        repo_name (str): The name of the repository.
        title (str): The pull request title.
        head_branch (str): The branch with proposed changes.
        base_branch (str): The branch to merge changes into.
        author (str): The user opening the pull request.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if created successfully, or "error" otherwise.
            - data: Metadata of the created pull request, including deterministic `pr_id`.

    Errors:
        - Returns an error if required parameters are missing or invalid.
        - Returns an error if a pull request with the same title already exists for the same branches.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        repo_name: str,
        title: str,
        body: str,
        head_branch: str,
        base_branch: str
,
    author: Any = None,
    ) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            title = _validate_param({"title": title}, "title", str)
            body = _validate_param({"body": body}, "body", str)
            head_branch = _validate_param({"head_branch": head_branch}, "head_branch", str)
            base_branch = _validate_param({"base_branch": base_branch}, "base_branch", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = data.get("pull_requests", [])
        new_number = len(prs) + 1
        new_pr = {
            "repo": repo_name,
            "number": new_number,
            "title": title,
            "body": body,
            "head_branch": head_branch,
            "base_branch": base_branch,
            "state": "open",
            "created_at": CURRENT_DATE,
        }
        new_pr["pr_id"] = _safe_id(
            new_pr, "pr_id", f"PR_{repo_name}_", ["title", "head_branch", "base_branch"]
        )
        prs.append(new_pr)
        return _response("ok", new_pr)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "OpenPullRequest",
                "description": "Open a new pull request deterministically (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "head_branch": {"type": "string"},
                        "base_branch": {"type": "string"},
                    },
                    "required": [
                        "repo_name",
                        "title",
                        "body",
                        "head_branch",
                        "base_branch",
                    ],
                },
            },
        }


class ClosePullRequestTool(Tool):
    """
    Close an existing pull request deterministically (in-memory only).

    This tool updates the state of a pull request from "open" to "closed".
    The `updated_at` timestamp is refreshed with CURRENT_DATE to ensure
    deterministic outputs.

    Input Parameters:
        repo_name (str): The name of the repository.
        pr_id (str): Deterministic ID of the pull request to close.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the pull request was closed successfully, or "error" otherwise.
            - data: Updated pull request metadata, including new state and `updated_at`.

    Errors:
        - Returns an error if `repo_name` or `pr_id` are missing or invalid.
        - Returns an error if the specified pull request does not exist in the dataset.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, pr_id: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            pr_id = _validate_param({"pr_id": pr_id}, "pr_id", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = data.get("pull_requests", [])
        pr = next(
            (
                p
                for p in prs
                if p.get("repo") == repo_name
                and _safe_id(
                    p,
                    "pr_id",
                    f"PR_{repo_name}_",
                    ["title", "head_branch", "base_branch"],
                )
                == pr_id
            ),
            None,
        )

        if not pr:
            return _response(
                "error",
                ERROR_MESSAGES["NOT_FOUND"].format(
                    entity="Pull Request", entity_id=pr_id
                ),
                "NOT_FOUND",
            )

        pr["state"] = "closed"
        pr["updated_at"] = CURRENT_DATE
        return _response("ok", pr)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "closePullRequest",
                "description": "Close a pull request deterministically (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_id": {"type": "string"},
                    },
                    "required": ["repo_name", "pr_id"],
                },
            },
        }


class MergePullRequestTool(Tool):
    """
    Merge an existing pull request deterministically (in-memory only).

    This tool changes the state of a pull request to "merged".
    Metadata is updated with `updated_at` set to CURRENT_DATE.

    Input Parameters:
        repo_name (str): The name of the repository.
        pr_id (str): Deterministic ID of the pull request to merge.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the PR was merged successfully, or "error" otherwise.
            - data: Updated pull request metadata with new state.

    Errors:
        - Returns an error if parameters are missing or invalid.
        - Returns an error if the specified pull request does not exist.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, pr_number: int) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            pr_number = _validate_param({"pr_number": pr_number}, "pr_number", int)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = data.get("pull_requests", [])
        pr = next(
            (
                p
                for p in prs
                if p.get("repo") == repo_name and p.get("number") == pr_number
            ),
            None,
        )

        if not pr:
            return _response(
                "error",
                ERROR_MESSAGES["NOT_FOUND"].format(
                    entity="Pull Request", entity_id=pr_number
                ),
                "NOT_FOUND",
            )

        pr["state"] = "merged"
        pr["merged_at"] = CURRENT_DATE
        pr["updated_at"] = CURRENT_DATE
        return _response("ok", pr)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MergePullRequest",
                "description": "Merge a pull request deterministically (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "pr_number"],
                },
            },
        }


class RequestPullRequestReviewTool(Tool):
    """
    Request reviews for a pull request deterministically (in-memory only).

    This tool appends one or more reviewers to a pull request.
    Reviewers are normalized with `_normalize_user`.
    The `updated_at` field is refreshed deterministically.

    Input Parameters:
        repo_name (str): The name of the repository.
        pr_id (str): Deterministic ID of the pull request.
        reviewers (List[str]): List of reviewers to assign.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if reviewers were assigned successfully, or "error" otherwise.
            - data: Updated pull request metadata with reviewer list.

    Errors:
        - Returns an error if required parameters are missing or invalid.
        - Returns an error if the pull request does not exist.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, pr_number: int, reviewers: list[str] = None) -> str:
        if reviewers is None:
            reviewers = []
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            pr_number = _validate_param({"pr_number": pr_number}, "pr_number", int)
            reviewers = (
                _validate_param({"reviewers": reviewers}, "reviewers", list, required=False, subtype=str)
                or []
            )
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = data.get("pull_requests", [])
        pr = next(
            (
                p
                for p in prs
                if p.get("repo") == repo_name and p.get("number") == pr_number
            ),
            None,
        )

        if not pr:
            return _response(
                "error",
                ERROR_MESSAGES["NOT_FOUND"].format(
                    entity="Pull Request", entity_id=pr_number
                ),
                "NOT_FOUND",
            )

        pr["reviewers"] = [_normalize_user(r) for r in reviewers]
        pr["updated_at"] = CURRENT_DATE
        return _response("ok", pr)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RequestPullRequestReview",
                "description": "Assign reviewers to a pull request deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "reviewers": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["repo_name", "pr_number", "reviewers"],
                },
            },
        }


class LinkPullRequestToIssueTool(Tool):
    """
    Link a pull request to an existing issue (in-memory only).

    This tool associates a pull request with an issue in the same repository,
    typically used to indicate that the PR addresses or resolves the issue.
    The `updated_at` timestamp is refreshed deterministically.

    Input Parameters:
        repo_name (str): The name of the repository.
        pr_id (str): Deterministic ID of the pull request to link.
        issue_id (str): Deterministic ID of the issue to link.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the link was created successfully, or "error" otherwise.
            - data: Updated pull request metadata, including a reference to the linked issue.

    Errors:
        - Returns an error if any required parameter is missing or invalid.
        - Returns an error if the pull request or issue does not exist in the repository.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, pr_number: int, issue_number: int) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            pr_number = _validate_param({"pr_number": pr_number}, "pr_number", int)
            issue_number = _validate_param({"issue_number": issue_number}, "issue_number", int)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = data.get("pull_requests", [])
        pr = next(
            (
                p
                for p in prs
                if p.get("repo") == repo_name and p.get("number") == pr_number
            ),
            None,
        )

        if not pr:
            return _response(
                "error",
                ERROR_MESSAGES["NOT_FOUND"].format(
                    entity="Pull Request", entity_id=pr_number
                ),
                "NOT_FOUND",
            )

        pr.setdefault("linked_issues", []).append(issue_number)
        pr["updated_at"] = CURRENT_DATE
        return _response("ok", pr)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkPullRequestToIssue",
                "description": "Link a pull request to an issue deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "issue_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "pr_number", "issue_number"],
                },
            },
        }


class GetPullRequestMergeTimeReportTool(Tool):
    """
    Generate a deterministic report of pull request merge times.

    This tool calculates how long pull requests remained open before being merged,
    by comparing their `created_at` and `updated_at` timestamps.
    Results provide insights into repository efficiency for reviewing and merging PRs.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: A list of merged pull requests with:
                - pr_id (str): Deterministic pull request ID.
                - title (str): The pull request title.
                - created_at (str): The PR creation timestamp.
                - merged_at (str): The PR merge timestamp.
                - merge_duration_days (int): Number of days between creation and merge.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
        - Returns an error if no merged pull requests are found in the repository.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = data.get("pull_requests", [])
        merged_prs = [
            p for p in prs if p.get("repo") == repo_name and p.get("state") == "merged"
        ]

        merge_times = []
        for pr in merged_prs:
            created = pr.get("created_at")
            merged = pr.get("merged_at")
            if created and merged:
                merge_times.append(_days_between(created, merged))

        average_merge_time = (
            int(sum(merge_times) / len(merge_times)) if merge_times else 0
        )

        report = {
            "repo": repo_name,
            "merged_pr_count": len(merged_prs),
            "average_merge_time": average_merge_time,
            "report_date": CURRENT_DATE,
        }

        return _response("ok", report)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPullRequestMergeTimeReport",
                "description": "Calculate deterministic average time-to-merge for pull requests.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


#================================================================
#Security Alerts Tools
#================================================================


class GetOpenSecurityAlertsTool(Tool):
    """
    Retrieve all open security alerts for a repository deterministically.

    This tool lists all code scanning alerts with state "open" for the given repository.
    Each alert is assigned a deterministic `alert_id` via `_safe_id`, severity is normalized
    to lowercase, and the result includes a `report_date`.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if alerts were found, or "error" otherwise.
            - data: A list of open alerts with metadata, including:
                - alert_id (str): Deterministic unique alert ID.
                - severity (str): Alert severity (normalized to lowercase).
                - state (str): The alert state ("open").
                - description (str): Alert description.
                - file (str): Affected file path.
                - branch (str): Branch where the issue was detected.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        alerts = data.get("code_scanning_alerts", [])
        repo_alerts = [
            {
                "alert_id": _safe_id(
                    a, "alert_id", f"ALERT_{repo_name}_", ["description", "file"]
                ),
                "severity": (a.get("severity") or "unknown").lower(),
                "state": a.get("state"),
                "description": a.get("description"),
                "file": a.get("file"),
                "branch": a.get("branch"),
                "report_date": CURRENT_DATE,
            }
            for a in alerts
            if a.get("repo") == repo_name and a.get("state") == "open"
        ]
        return _response("ok", repo_alerts)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOpenSecurityAlerts",
                "description": "List all open security alerts for a repository deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class GetResolvedSecurityAlertsTool(Tool):
    """
    Retrieve all resolved security alerts for a repository deterministically.

    This tool lists all code scanning alerts with state "resolved" for the given repository.
    Each alert is assigned a deterministic `alert_id` via `_safe_id`, severity is normalized
    to lowercase, and the result includes a `report_date`. If `resolved_at` is missing,
    it is set to CURRENT_DATE.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if alerts were found, or "error" otherwise.
            - data: A list of resolved alerts with metadata, including:
                - alert_id (str): Deterministic unique alert ID.
                - severity (str): Alert severity (normalized to lowercase).
                - state (str): The alert state ("resolved").
                - description (str): Alert description.
                - file (str): Affected file path.
                - branch (str): Branch where the issue was detected.
                - resolved_at (str): Resolution timestamp (existing or CURRENT_DATE).
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        alerts = data.get("code_scanning_alerts", [])
        resolved = [
            {
                "alert_id": _safe_id(
                    a, "alert_id", f"ALERT_{repo_name}_", ["description", "file"]
                ),
                "severity": (a.get("severity") or "unknown").lower(),
                "state": a.get("state"),
                "resolved_at": a.get("resolved_at") or CURRENT_DATE,
                "description": a.get("description"),
            }
            for a in alerts
            if a.get("repo") == repo_name and a.get("state") in ["fixed", "dismissed"]
        ]
        return _response("ok", resolved)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetResolvedSecurityAlerts",
                "description": "List all resolved security alerts for a repository deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class CreateSecurityAlertTool(Tool):
    """
    Create a new security alert deterministically (in-memory only).

    This tool simulates the creation of a new code scanning alert in a repository.
    IDs are generated with `_safe_id` using description and file. Severity is
    normalized to lowercase, and metadata is stamped with CURRENT_DATE.

    Input Parameters:
        repo_name (str): The name of the repository.
        description (str): Description of the security issue.
        file (str): The file path affected by the issue.
        branch (str): The branch where the issue was found.
        severity (str): Severity of the alert (e.g., "low", "medium", "high").

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if created successfully, or "error" otherwise.
            - data: Metadata of the created security alert, including deterministic `alert_id`.

    Errors:
        - Returns an error if required parameters are missing or invalid.
        - Returns an error if a similar alert already exists in the repository.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        repo_name: str,
        severity: str,
        description: str,
        file: str,
        branch: str
    ) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            severity = _validate_param({"severity": severity}, "severity", str)
            description = _validate_param({"description": description}, "description", str)
            file = _validate_param({"file": file}, "file", str)
            branch = _validate_param({"branch": branch}, "branch", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        alerts = data.get("code_scanning_alerts", [])
        if any(
            a.get("repo") == repo_name and a.get("description") == description
            for a in alerts
        ):
            return _response(
                "error",
                ERROR_MESSAGES["ALREADY_EXISTS"].format(
                    entity="SecurityAlert", entity_id=description
                ),
                "ALREADY_EXISTS",
            )

        new_number = len(alerts) + 1
        new_alert = {
            "repo": repo_name,
            "number": new_number,
            "severity": severity,
            "state": "open",
            "description": description,
            "file": file,
            "branch": branch,
            "created_at": CURRENT_DATE,
            "updated_at": CURRENT_DATE,
        }
        new_alert["alert_id"] = _safe_id(
            new_alert, "alert_id", f"ALERT_{repo_name}_", ["description", "file"]
        )
        alerts.append(new_alert)
        return _response("ok", new_alert)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSecurityAlert",
                "description": "Create a new deterministic security alert (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "severity": {"type": "string"},
                        "description": {"type": "string"},
                        "file": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": [
                        "repo_name",
                        "severity",
                        "description",
                        "file",
                        "branch",
                    ],
                },
            },
        }


class FixSecurityAlertTool(Tool):
    """
    Mark an existing security alert as resolved (in-memory only).

    This tool updates the state of an alert from "open" to "resolved".
    The `resolved_at` and `updated_at` timestamps are set deterministically
    to CURRENT_DATE if not already present.

    Input Parameters:
        repo_name (str): The name of the repository.
        alert_id (str): Deterministic ID of the security alert to resolve.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the alert was resolved successfully, or "error" otherwise.
            - data: Updated alert metadata, including state, `resolved_at`, and `updated_at`.

    Errors:
        - Returns an error if parameters are missing or invalid.
        - Returns an error if the alert does not exist in the repository.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, alert_number: int = None) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            alert_number = _validate_param({"alert_number": alert_number}, "alert_number", int)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        alerts = data.get("code_scanning_alerts", [])
        alert = next(
            (
                a
                for a in alerts
                if a.get("repo") == repo_name and a.get("number") == alert_number
            ),
            None,
        )

        if not alert:
            return _response(
                "error",
                ERROR_MESSAGES["NOT_FOUND"].format(
                    entity="Alert", entity_id=alert_number
                ),
                "NOT_FOUND",
            )

        alert["state"] = "fixed"
        alert["resolved_at"] = CURRENT_DATE
        alert["updated_at"] = CURRENT_DATE
        return _response("ok", alert)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FixSecurityAlert",
                "description": "Mark a security alert as fixed deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "alert_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "alert_number"],
                },
            },
        }


class ListAlertsBySeverityTool(Tool):
    """
    List security alerts for a repository filtered by severity.

    This tool retrieves all alerts for a repository with a given severity level.
    Severity values are normalized to lowercase for deterministic filtering.
    Each alert is returned with a deterministic `alert_id` via `_safe_id`.

    Input Parameters:
        repo_name (str): The name of the repository.
        severity (str): Severity level to filter by (e.g., "low", "medium", "high").

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if alerts were found, or "error" otherwise.
            - data: A list of alerts with metadata, including:
                - alert_id (str): Deterministic unique alert ID.
                - severity (str): Normalized severity.
                - state (str): Current state of the alert.
                - description (str): Alert description.
                - file (str): Affected file.
                - branch (str): Branch where the issue was detected.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if parameters are missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, severity: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            severity = _validate_param({"severity": severity}, "severity", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        alerts = data.get("code_scanning_alerts", [])
        filtered = [
            {
                "alert_id": _safe_id(
                    a, "alert_id", f"ALERT_{repo_name}_", ["description", "file"]
                ),
                "severity": (a.get("severity") or "unknown").lower(),
                "state": a.get("state"),
                "description": a.get("description"),
                "report_date": CURRENT_DATE,
            }
            for a in alerts
            if a.get("repo") == repo_name
            and (a.get("severity") or "").lower() == severity.lower()
        ]
        return _response("ok", filtered)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAlertsBySeverity",
                "description": "List security alerts for a repository filtered by severity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "severity": {"type": "string"},
                    },
                    "required": ["repo_name", "severity"],
                },
            },
        }


class GetRepositoryRiskScoreTool(Tool):
    """
    Calculate a deterministic security risk score for a repository.

    This tool analyzes all open security alerts for a repository and
    computes a risk score based on the number and severity of alerts.
    Higher severity alerts contribute more weight to the risk score.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if calculated successfully, or "error" otherwise.
            - data: A dictionary with:
                - repo (str): Repository name.
                - open_alerts (int): Count of open alerts.
                - severity_breakdown (Dict[str, int]): Count of alerts per severity (normalized).
                - risk_score (int): Deterministic numeric risk score.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        alerts = data.get("code_scanning_alerts", [])
        open_alerts = [
            a for a in alerts if a.get("repo") == repo_name and a.get("state") == "open"
        ]

        score = sum(
            {"critical": 5, "high": 3, "medium": 2, "low": 1}.get(
                a.get("severity", "low"), 1
            )
            for a in open_alerts
        )

        result = {
            "repo": repo_name,
            "open_alerts_count": len(open_alerts),
            "risk_score": score,
            "report_date": CURRENT_DATE,
        }
        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRepositoryRiskScore",
                "description": "Calculate deterministic risk score for a repository based on open alerts.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


#================================================================
#Terminal Events & Releases Tools
#================================================================


class GetDeploymentStatusTool(Tool):
    """
    Retrieve deployment status deterministically for a repository.

    Deployment states must reflect terminal log events
    (e.g., React dashboard dark mode deployed, Flutter finance app released).

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok"
            - data: {
                "repo": repo_name,
                "last_deployment": str,
                "deployment_date": str,
                "status": str ("success", "failed", "pending"),
                "report_date": str
            }
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        deploys = data.get("deployments", [])
        repo_deploys = [d for d in deploys if d.get("repo") == repo_name]

        if not repo_deploys:
            return _response(
                "error",
                ERROR_MESSAGES["NO_DATA_FOUND"].format(
                    entity=f"Deployments for {repo_name}"
                ),
                "NOT_FOUND",
            )

        latest = max(repo_deploys, key=lambda d: d.get("deployment_date", ""))
        result = {**latest, "report_date": CURRENT_DATE}
        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getDeploymentStatus",
                "description": "Get latest deterministic deployment status for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class ListTerminalLogsTool(Tool):
    """
    List terminal log events deterministically.

    This tool retrieves all recorded terminal log events from the dataset.
    Each event is augmented with a deterministic `report_date` field set to CURRENT_DATE.

    Input Parameters:
        None

    Returns:
        str: JSON-formatted response containing:
            - status: "ok".
            - data: A list of terminal events with their original metadata plus:
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - None. Returns an empty list if no terminal events exist.
    """

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        events = data.get("terminal", [])
        deterministic_events = [{**e, "report_date": CURRENT_DATE} for e in events]
        return _response("ok", deterministic_events)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listTerminalEvents",
                "description": "List timeline events from terminal logs deterministically.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class GetReleasesByRepositoryTool(Tool):
    """
    List all releases for a repository deterministically.

    This tool retrieves all releases associated with a given repository.
    Each release is assigned a deterministic `release_id` via `_safe_id` and
    includes a `report_date`.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if releases were found, or "error" otherwise.
            - data: A list of releases with metadata, including:
                - release_id (str): Deterministic unique release ID.
                - repo (str): Repository name.
                - version (str): Release version string.
                - description (str): Release description.
                - created_at (str): Creation timestamp.
                - updated_at (str): Last update timestamp.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        releases = data.get("releases", [])
        filtered = [
            {
                "release_id": _safe_id(r, "release_id", "REL_", ["repo", "version"]),
                "repo": repo_name,
                "version": r.get("version"),
                "description": r.get("description"),
                "created_at": r.get("created_at"),
                "report_date": CURRENT_DATE,
            }
            for r in releases
            if r.get("repo") == repo_name
        ]
        return _response("ok", filtered)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReleasesByRepository",
                "description": "List all releases for a repository deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class CreateReleaseTool(Tool):
    """
    Create a new release deterministically (in-memory only).

    This tool simulates the creation of a new release in a repository.
    IDs are generated via `_safe_id` using repository name and version.
    Metadata is stamped with CURRENT_DATE for deterministic behavior.

    Input Parameters:
        repo_name (str): The name of the repository.
        version (str): Version identifier for the release.
        description (str): Description of the release contents.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the release was created successfully, or "error" otherwise.
            - data: Metadata of the created release, including deterministic `release_id`.

    Errors:
        - Returns an error if required parameters are missing or invalid.
        - Returns an error if a release with the same version already exists for the repository.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, version: str, description: str,
    name: Any = None,
    ) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            version = _validate_param({"version": version}, "version", str)
            description = _validate_param({"description": description}, "description", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        releases = data.get("releases", [])
        if any(
            r.get("repo") == repo_name and r.get("version") == version for r in releases
        ):
            return _response(
                "error",
                ERROR_MESSAGES["ALREADY_EXISTS"].format(
                    entity="Release", entity_id=version
                ),
                "ALREADY_EXISTS",
            )

        new_release = {
            "repo": repo_name,
            "version": version,
            "description": description,
            "created_at": CURRENT_DATE,
            "updated_at": CURRENT_DATE,
        }
        new_release["release_id"] = _safe_id(
            new_release, "release_id", "REL_", ["repo", "version"]
        )
        releases.append(new_release)
        return _response("ok", new_release)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRelease",
                "description": "Create a new deterministic release (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "version": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": ["repo_name", "version", "description"],
                },
            },
        }


class RegisterDeployEventTool(Tool):
    """
    Register a new deterministic deploy event (in-memory only).

    This tool logs a deploy event for a repository in a specific environment.
    A deterministic `event_id` is generated via `_safe_id`, based on repository,
    environment, and date. The event is stamped with CURRENT_DATE.

    Input Parameters:
        repo_name (str): The name of the repository.
        environment (str): The deployment environment (e.g., "staging", "production").

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the deploy event was registered successfully, or "error" otherwise.
            - data: Metadata of the created deploy event, including deterministic `event_id`.

    Errors:
        - Returns an error if parameters are missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, environment: str = None) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            environment = _validate_param({"environment": environment}, "environment", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        events = data.get("terminal", [])

        new_event = {
            "repo": repo_name,
            "environment": environment,
            "type": "deploy",
            "date": CURRENT_DATE,
        }
        new_event["event_id"] = _safe_id(
            new_event, "event_id", "DEPLOY_", ["repo", "environment", "date"]
        )
        events.append(new_event)
        return _response("ok", new_event)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterDeployEvent",
                "description": "Register a deterministic deploy event (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "environment": {"type": "string"},
                    },
                    "required": ["repo_name", "environment"],
                },
            },
        }


class GetDeploymentFrequencyReportTool(Tool):
    """
    Generate a deterministic deployment frequency report.

    This tool calculates the number of deploy events for a repository within a
    deterministic time window (e.g., daily, weekly, monthly). It provides insights
    into how frequently deployments occur in different environments.

    Input Parameters:
        repo_name (str): The name of the repository.
        period (str): The aggregation period for frequency ("daily", "weekly", "monthly").

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if calculated successfully, or "error" otherwise.
            - data: A dictionary with:
                - repo (str): The repository name.
                - period (str): The selected aggregation period.
                - deploy_counts (Dict[str, int]): Number of deploys per environment.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` or `period` is missing or invalid.
        - Returns an error if no deploy events exist for the repository.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        events = data.get("terminal", [])
        deploys = [
            d
            for d in events
            if d.get("repo") == repo_name and d.get("type") == "deploy"
        ]
        deploys = sorted(deploys, key=lambda d: (d.get("date"), d.get("event_id")))

        deploy_dates = sorted([d.get("date") for d in deploys if d.get("date")])

        intervals = []
        for i in range(1, len(deploy_dates)):
            intervals.append(_days_between(deploy_dates[i - 1], deploy_dates[i]))

        average_interval = int(sum(intervals) / len(intervals)) if intervals else 0

        report = {
            "repo": repo_name,
            "deploy_count": len(deploys),
            "average_interval_days": average_interval,
            "deploy_events": [
                {
                    "event_id": d["event_id"],
                    "date": d["date"],
                    "environment": d["environment"],
                }
                for d in deploys
            ],
            "report_date": CURRENT_DATE,
        }
        return _response("ok", report)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDeploymentFrequencyReport",
                "description": "Get deterministic deployment frequency stats for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


#================================================================
#Cross-Entity / Analytics Tools
#================================================================


class GetCrossEntityReportTool(Tool):
    """
    Generate a deterministic cross-entity report consolidating issues, PRs, commits, alerts, and deployments.

    This tool links entities (Issues ↔ PRs ↔ Commits ↔ Alerts ↔ Deploys) into a single summary.

    Input Parameters:
        repo_name (str): The repository name.

    Returns:
        str: JSON response containing:
            - status: "ok"
            - data: {
                "repo": str,
                "open_issues": int,
                "merged_prs": int,
                "recent_commits": int (last 30 days),
                "open_alerts": int,
                "last_deployment": str,
                "report_date": str
            }
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        issues = data.get("issues", [])
        prs = data.get("pull_requests", [])
        commits = data.get("commits", [])
        alerts = data.get("code_scanning_alerts", [])
        deploys = data.get("deployments", [])

        result = {
            "repo": repo_name,
            "open_issues": sum(
                1
                for i in issues
                if i.get("repo") == repo_name and i.get("state") == "open"
            ),
            "merged_prs": sum(
                1
                for p in prs
                if p.get("repo") == repo_name and p.get("state") == "merged"
            ),
            "recent_commits": sum(
                1
                for c in commits
                if c.get("repo") == repo_name
                and _days_between(c.get("timestamp", CURRENT_DATE), CURRENT_DATE) <= 30
            ),
            "open_alerts": sum(
                1
                for a in alerts
                if a.get("repo") == repo_name and a.get("state") == "open"
            ),
            "last_deployment": max(
                (
                    d.get("deployment_date")
                    for d in deploys
                    if d.get("repo") == repo_name
                ),
                default="none",
            ),
            "report_date": CURRENT_DATE,
        }
        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrossEntityReport",
                "description": "Generate deterministic cross-entity report (issues, PRs, commits, alerts, deploys).",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class MapCommitsToPullRequestsTool(Tool):
    """
    Map commits to their associated pull requests deterministically.

    This tool searches for commits in a repository and determines which pull requests
    they belong to, based on commit SHA associations. It provides traceability from
    commits to the PRs that included them.

    Input Parameters:
        repo_name (str): The name of the repository.
        commit_shas (List[str]): A list of commit SHA identifiers to map.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A mapping of commit SHAs to pull request IDs.

    Errors:
        - Returns an error if `repo_name` or `commit_shas` are missing or invalid.
        - Returns an error if no associations are found for the given commits.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = data.get("commits", [])
        prs = data.get("pull_requests", [])

        mapping = []
        for pr in prs:
            if pr.get("repo") == repo_name:
                pr_commits = [
                    c
                    for c in commits
                    if c.get("repo") == repo_name
                    and c.get("branch") == pr.get("head_branch")
                ]
                mapping.append(
                    {
                        "pr_id": _safe_id(
                            pr,
                            "pr_id",
                            f"PR_{repo_name}_",
                            ["title", "head_branch", "base_branch"],
                        ),
                        "commit_ids": [c.get("sha") for c in pr_commits],
                        "report_date": CURRENT_DATE,
                    }
                )

        return _response("ok", mapping)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MapCommitsToPullRequests",
                "description": "Map commits deterministically to their pull requests.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class MapPullRequestsToIssuesTool(Tool):
    """
    Map pull requests to their linked issues deterministically.

    This tool retrieves all pull requests in a repository and identifies any linked issues.
    It provides traceability from pull requests to the issues they are meant to resolve.

    Input Parameters:
        repo_name (str): The name of the repository.
        pr_ids (List[str]): A list of pull request IDs to map.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A mapping of pull request IDs to linked issue IDs.

    Errors:
        - Returns an error if `repo_name` or `pr_ids` are missing or invalid.
        - Returns an error if no links exist for the given pull requests.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = data.get("pull_requests", [])

        mapping = [
            {
                "issue_id": _safe_id(
                    pr, "issue_id", f"ISSUE_{repo_name}_", ["title", "body"]
                ),
                "pr_id": _safe_id(
                    pr,
                    "pr_id",
                    f"PR_{repo_name}_",
                    ["title", "head_branch", "base_branch"],
                ),
                "linked_issues": pr.get("linked_issues", []),
                "report_date": CURRENT_DATE,
            }
            for pr in prs
            if pr.get("repo") == repo_name
        ]
        return _response("ok", mapping)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "mapPullRequestsToIssues",
                "description": "Map pull requests deterministically to their linked issues.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class GetRepositoryActivityDashboardTool(Tool):
    """
    Generate a deterministic activity dashboard for a repository.

    This tool aggregates key activity metrics for a repository, including commits,
    pull requests, issues, and alerts. It provides a holistic view of repository health
    and activity trends, normalized for deterministic outputs.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: A dictionary with aggregated metrics:
                - total_commits (int): Total commits in the repository.
                - open_prs (int): Number of open pull requests.
                - merged_prs (int): Number of merged pull requests.
                - open_issues (int): Number of open issues.
                - closed_issues (int): Number of closed issues.
                - open_alerts (int): Number of open security alerts.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = data.get("commits", [])
        issues = data.get("issues", [])
        prs = data.get("pull_requests", [])
        alerts = data.get("code_scanning_alerts", [])

        dashboard = {
            "repo": repo_name,
            "commits_count": sum(1 for c in commits if c.get("repo") == repo_name),
            "open_issues": sum(
                1
                for i in issues
                if i.get("repo") == repo_name and i.get("state") == "open"
            ),
            "open_prs": sum(
                1
                for p in prs
                if p.get("repo") == repo_name and p.get("state") == "open"
            ),
            "open_alerts_by_severity": {
                sev: sum(
                    1
                    for a in alerts
                    if a.get("repo") == repo_name
                    and a.get("state") == "open"
                    and (a.get("severity") or "unknown").lower() == sev
                )
                for sev in ["critical", "high", "medium", "low", "unknown"]
            },
            "open_alerts": sum(
                1
                for a in alerts
                if a.get("repo") == repo_name and a.get("state") == "open"
            ),
            "report_date": CURRENT_DATE,
        }
        return _response("ok", dashboard)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRepositoryActivityDashboard",
                "description": "Summarize repository activity (commits, issues, PRs, alerts).",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class GetTeamContributionStatsTool(Tool):
    """
    Generate deterministic contribution statistics for a team.

    This tool aggregates commit, pull request, and issue contributions across a repository,
    grouped by team members. Author identifiers are normalized via `_normalize_user`.
    Labels and severity values are normalized for consistency.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: Contribution statistics, including:
                - commits_by_author (Dict[str, int]): Commits per author.
                - prs_by_author (Dict[str, int]): Pull requests per author.
                - issues_by_author (Dict[str, int]): Issues created per author.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        commits = data.get("commits", [])
        prs = data.get("pull_requests", [])
        issues = data.get("issues", [])

        stats = {}
        for c in commits:
            if c.get("repo") == repo_name:
                author = _normalize_user(c.get("author"))
                stats.setdefault(author, {"commits": 0, "prs": 0, "issues": 0})
                stats[author]["commits"] += 1
        for p in prs:
            if p.get("repo") == repo_name:
                author = _normalize_user(p.get("author"))
                stats.setdefault(author, {"commits": 0, "prs": 0, "issues": 0})
                stats[author]["prs"] += 1
        for i in issues:
            if i.get("repo") == repo_name:
                for a in [_normalize_user(a) for a in i.get("assignees", [])]:
                    stats.setdefault(a, {"commits": 0, "prs": 0, "issues": 0})
                    stats[a]["issues"] += 1

        result = {"repo": repo_name, "team_stats": stats, "report_date": CURRENT_DATE}
        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamContributionStats",
                "description": "Calculate contributions (commits, PRs, issues) per user deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class GetHotspotRepositoriesTool(Tool):
    """
    Identify hotspot repositories based on activity.

    This tool analyzes all repositories and ranks them based on activity, such as
    commit frequency, open pull requests, and unresolved alerts. It helps identify
    repositories requiring attention.

    Input Parameters:
        None

    Returns:
        str: JSON-formatted response containing:
            - status: "ok".
            - data: A list of repositories with their aggregated activity scores, including:
                - repo (str): Repository name.
                - activity_score (int): Deterministic numeric score based on activity.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - None. Returns an empty list if no repositories exist.
    """

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        issues = data.get("issues", [])
        alerts = data.get("code_scanning_alerts", [])

        repo_hotspots = {}
        for i in issues:
            if i.get("state") == "open":
                repo_hotspots[i.get("repo")] = repo_hotspots.get(i.get("repo"), 0) + 1
        for a in alerts:
            if a.get("state") == "open":
                repo_hotspots[a.get("repo")] = repo_hotspots.get(a.get("repo"), 0) + 1

        result = [
            {"repo": r, "open_items": count, "report_date": CURRENT_DATE}
            for r, count in repo_hotspots.items()
        ]
        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getHotspotRepositories",
                "description": "Identify repositories with most open issues and alerts deterministically.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class GenerateEndToEndReportTool(Tool):
    """
    Generate a deterministic end-to-end report for a repository.

    This tool consolidates multiple aspects of repository health into a single
    comprehensive report, including commits, pull requests, issues, alerts,
    releases, and deploy events. It is intended as a holistic snapshot
    for governance and auditing.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: Comprehensive repository report, including:
                - repo (str): Repository name.
                - commit_stats (Dict): Commit activity metrics.
                - pr_stats (Dict): Pull request activity metrics.
                - issue_stats (Dict): Issue activity metrics.
                - alert_stats (Dict): Security alert metrics.
                - release_info (Dict): Latest release metadata.
                - deploy_stats (Dict): Deployment frequency or events.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        pass
        commits = data.get("commits", [])
        issues = data.get("issues", [])
        prs = data.get("pull_requests", [])
        alerts = data.get("code_scanning_alerts", [])
        releases = data.get("releases", [])

        report = {
            "repo": repo_name,
            "commits_count": sum(1 for c in commits if c.get("repo") == repo_name),
            "open_issues": sum(
                1
                for i in issues
                if i.get("repo") == repo_name and i.get("state") == "open"
            ),
            "merged_prs": sum(
                1
                for p in prs
                if p.get("repo") == repo_name and p.get("state") == "merged"
            ),
            "open_alerts": sum(
                1
                for a in alerts
                if a.get("repo") == repo_name and a.get("state") == "open"
            ),
            "releases_count": sum(1 for r in releases if r.get("repo") == repo_name),
            "report_date": CURRENT_DATE,
        }
        return _response("ok", report)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateEndToEndReport",
                "description": "Generate deterministic end-to-end report (issues, PRs, commits, alerts, releases).",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


TOOLS = [
    #Repositories
    GetRepositoryMetadataTool(),
    ListRepositoriesTool(),
    CreateRepositoryTool(),
    UpdateRepositoryDescriptionTool(),
    GetRepositoryHealthSummaryTool(),
    #Commits
    ListCommitsByBranchTool(),
    GetCommitMetadataTool(),
    AddCommitToBranchTool(),
    CountCommitsByAuthorTool(),
    ListCommitsByDateRangeTool(),
    #Issues
    GetOpenIssuesTool(),
    GetClosedIssuesTool(),
    CreateIssueTool(),
    CloseIssueTool(),
    AssignIssueTool(),
    ListIssuesByLabelTool(),
    GetIssueAgingReportTool(),
    #Pull Requests
    ListPullRequestsTool(),
    GetPullRequestMetadataTool(),
    OpenPullRequestTool(),
    ClosePullRequestTool(),
    MergePullRequestTool(),
    RequestPullRequestReviewTool(),
    LinkPullRequestToIssueTool(),
    GetPullRequestMergeTimeReportTool(),
    #Security Alerts
    GetOpenSecurityAlertsTool(),
    GetResolvedSecurityAlertsTool(),
    CreateSecurityAlertTool(),
    FixSecurityAlertTool(),
    ListAlertsBySeverityTool(),
    GetRepositoryRiskScoreTool(),
    #Terminal / Releases
    GetDeploymentStatusTool(),
    ListTerminalLogsTool(),
    GetReleasesByRepositoryTool(),
    CreateReleaseTool(),
    RegisterDeployEventTool(),
    GetDeploymentFrequencyReportTool(),
    #Cross-Entity / Analytics
    GetCrossEntityReportTool(),
    MapCommitsToPullRequestsTool(),
    MapPullRequestsToIssuesTool(),
    GetRepositoryActivityDashboardTool(),
    GetTeamContributionStatsTool(),
    GetHotspotRepositoriesTool(),
    GenerateEndToEndReportTool(),
]


__all__ = [
    "GetRepositoryMetadataTool",
    "ListRepositoriesTool",
    "CreateRepositoryTool",
    "UpdateRepositoryDescriptionTool",
    "GetRepositoryHealthSummaryTool",
    "ListCommitsByBranchTool",
    "GetCommitMetadataTool",
    "AddCommitToBranchTool",
    "CountCommitsByAuthorTool",
    "ListCommitsByDateRangeTool",
    "GetOpenIssuesTool",
    "GetClosedIssuesTool",
    "CreateIssueTool",
    "CloseIssueTool",
    "AssignIssueTool",
    "ListIssuesByLabelTool",
    "GetIssueAgingReportTool",
    "ListPullRequestsTool",
    "GetPullRequestMetadataTool",
    "OpenPullRequestTool",
    "ClosePullRequestTool",
    "MergePullRequestTool",
    "RequestPullRequestReviewTool",
    "LinkPullRequestToIssueTool",
    "GetPullRequestMergeTimeReportTool",
    "GetOpenSecurityAlertsTool",
    "GetResolvedSecurityAlertsTool",
    "CreateSecurityAlertTool",
    "FixSecurityAlertTool",
    "ListAlertsBySeverityTool",
    "GetRepositoryRiskScoreTool",
    "GetDeploymentStatusTool",
    "ListTerminalLogsTool",
    "GetReleasesByRepositoryTool",
    "CreateReleaseTool",
    "RegisterDeployEventTool",
    "GetDeploymentFrequencyReportTool",
    "GetCrossEntityReportTool",
    "MapCommitsToPullRequestsTool",
    "MapPullRequestsToIssuesTool",
    "GetRepositoryActivityDashboardTool",
    "GetTeamContributionStatsTool",
    "GetHotspotRepositoriesTool",
    "GenerateEndToEndReportTool",
    "TOOLS",
]
