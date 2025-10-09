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
