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
