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

        commits = data.get("commits", {}).values()
        commit = next(
            (
                c
                for c in commits.values() if c.get("repo") == repo_name and c.get("sha") == commit_sha
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
