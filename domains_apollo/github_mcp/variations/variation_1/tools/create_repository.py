from tau_bench.envs.tool import Tool
import json
from typing import Any

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
    def invoke(
        data: dict[str, Any],
        owner: str = "",
        repo_name: str = "",
        description: str = None,
        private_flag: bool = False,
        auto_init_flag: bool = False
    ) -> str:
        pass
        owner = owner.strip()
        repo_name = repo_name.strip()

        if not owner or not repo_name:
            payload = {"error": "Both 'owner' and 'repo_name' are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        repos = data.get("repositories", [])

        # Normalize description to the nullable field name used in the DB
        description_nullable = description if description is not None else None

        # Collision handling: if (owner, repo_name) exists, try single '_v2' suffix
        def _exists(o: str, n: str) -> bool:
            pass
            return any(r.get("owner") == o and r.get("repo_name") == n for r in repos)

        if _exists(owner, repo_name):
            candidate = f"{repo_name}_v2"
            if _exists(owner, candidate):
                payload = {
                        "error": f"Repository '{owner}/{repo_name}' exists and '{candidate}' also exists."
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
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
        file_paths = []
        file_contents = []

        # Per-branch aligned structures
        branch_files = [[]]
        branch_contents = [[]]

        if auto_init_flag:
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
            "auto_init_flag": bool(auto_init_flag),
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

        add_terminal_message(
            data, f"Repository '{owner}/{repo_name}' created.", get_current_timestamp()
        )
        payload = {
                "success": f"Repository '{owner}/{repo_name}' created.",
                "repository": {
                    "owner": owner,
                    "repo_name": repo_name,
                    "default_branch": default_branch,
                    "branch_shas": branch_shas,
                    "created_ts": created_ts,
                    "updated_ts": updated_ts,
                    "file_paths": file_paths,
                    "file_contents": file_contents,
                },
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
                "name": "createRepository",
                "description": "Creates a new repository with default branch 'main', a deterministic branch SHA, and deterministic timestamps. If name exists, appends '_v2'. If autoinit_flag is true, seeds README.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "Repository owner (account/team).",
                        },
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name to create (may be suffixed with '_v2' if taken).",
                        },
                        "description": {
                            "type": "string",
                            "nullable": True,
                            "description": "Optional description of the repository.",
                        },
                        "private_flag": {
                            "type": "boolean",
                            "description": "Whether the repo is private.",
                        },
                        "autoinit_flag": {
                            "type": "boolean",
                            "description": "If true, adds README to file paths/contents and to the main branch.",
                        },
                    },
                    "required": [
                        "owner",
                        "repo_name",
                        "private_flag",
                        "auto_init_flag",
                    ],
                },
            },
        }
