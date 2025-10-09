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

class ListRepositoriesTool(Tool):
    """
    List all repositories with deterministic metadata.

    This tool retrieves all repositories from the dataset and augments each entry
    with a deterministic `report_date` field set to CURRENT_DATE. It does not filter
    by name or other attributes — all repositories present in the dataset are returned.

    Usage:
        - No input parameters are required.
        - Returns metadata for every repository in the dataset.

    Input Parameters:
        None

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: A list of repositories, each enriched with a `report_date` field.
    """

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        repos = data.get("repositories", [])
        result = [{**r, "report_date": CURRENT_DATE} for r in repos]
        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRepositories",
                "description": "List all repositories with deterministic metadata.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
