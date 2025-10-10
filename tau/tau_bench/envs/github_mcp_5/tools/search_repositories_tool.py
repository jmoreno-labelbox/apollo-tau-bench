# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        query = kwargs.get("query")

        if not query:
            return json.dumps(
                {
                    "status": "error",
                    "message": "Missing required parameters: 'query'.",
                    "required": ["query"],
                },
                indent=2,
            )

        repos = list(data.get('repositories', {}).values())
        repo = next((c for c in repos if c["repo_name"] == query), None)
        # repo = fetch_data(repos, query)

        if not repo:
            return json.dumps(
                {"status": "success", "exists": False, "message": "Target repo not found"},
                indent=2,
            )
        else:
            # Emulate the logic for verifying documents.
            return json.dumps(
                {"status": "success", "exists": True, "message": "Target repo found"}, indent=2
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_repositories",
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
