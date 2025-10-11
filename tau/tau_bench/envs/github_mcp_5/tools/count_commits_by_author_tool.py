# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = list(data.get("commits", {}).values())
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
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "count_commits_by_author",
                "description": "Count commits per author for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
