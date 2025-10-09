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
        return list(db.values())
    return db

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
