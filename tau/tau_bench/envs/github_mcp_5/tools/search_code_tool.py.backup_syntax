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

        repositories = data.get("repositories", {}).values()
        repository = next(
            (r for r in repositories.values() if r["repo_name"] == repo and r["owner"] == owner),
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
            repository.get("file_paths", {}).values()), repository.get("file_contents", {}).values()
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
