from tau_bench.envs.tool import Tool
import calendar
import json
import os
import random
import uuid
from datetime import datetime, timezone
from typing import Any
import hashlib
from datetime import datetime



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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

        repositories = data.get("repositories", {}).values()
        repository = next(
            (r for r in repositories.values() if r["repo_name"] == repo and r["owner"] == owner),
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
