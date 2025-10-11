# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
    def invoke(data: Dict[str, Any], auto_init_flag = False, description = None, owner = "", private_flag = False, repo_name = "") -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        autoinit_flag = auto_init_flag

        if not owner or not repo_name:
            return json.dumps(
                {"error": "Both 'owner' and 'repo_name' are required."},
                indent=2
            )


        repos = list(data.get("repositories", {}).values())



        # Standardize the description to match the nullable field name utilized in the database.
        description_nullable = description if description is not None else None

        # Collision management: if (owner, repo_name) is found, attempt a '_v2' suffix.
        def _exists(o: str, n: str) -> bool:
            return any(r.get("owner") == o and r.get("repo_name") == n for r in repos)

        if _exists(owner, repo_name):
            candidate = f"{repo_name}_v2"
            if _exists(owner, candidate):
                return json.dumps(
                    {"error": f"Repository '{owner}/{repo_name}' exists and '{candidate}' also exists."},
                    indent=2
                )
            repo_name = candidate  # unique deterministic suffix

        # Fixed timestamps
        created_ts = get_current_timestamp()
        updated_ts = created_ts  # initialize as equal upon instantiation

        # Predefined values
        default_branch = "main"
        branches = ["main"]

        # Deterministic SHA for 'main' function
        main_sha = get_next_branch_sha(data)
        branch_shas = [main_sha]

        # Automatically initialize the file structure for the entire repository.
        file_paths= []
        file_contents= []

        # Structures aligned for each branch
        branch_files = [[]]
        branch_contents = [[]]

        if autoinit_flag:
            readme_content = f"# {repo_name}\n\nInitial commit."
            file_paths = ["README.md"]
            file_contents = [readme_content]
            branch_files = [file_paths.copy()]
            branch_contents = [file_contents.copy()]

        # Create the new repository entry according to the current schema.
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

        # Append in a deterministic manner at the end.
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
