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

class GetDeploymentStatusTool(Tool):
    """
    Retrieve deployment status deterministically for a repository.

    Deployment states must reflect terminal log events
    (e.g., React dashboard dark mode deployed, Flutter finance app released).

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok"
            - data: {
                "repo": repo_name,
                "last_deployment": str,
                "deployment_date": str,
                "status": str ("success", "failed", "pending"),
                "report_date": str
            }
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        deploys = data.get("deployments", {}).values()
        repo_deploys = [d for d in deploys.values() if d.get("repo") == repo_name]

        if not repo_deploys:
            return _response(
                "error",
                ERROR_MESSAGES["NO_DATA_FOUND"].format(
                    entity=f"Deployments for {repo_name}"
                ),
                "NOT_FOUND",
            )

        latest = max(repo_deploys, key=lambda d: d.get("deployment_date", ""))
        result = {**latest, "report_date": CURRENT_DATE}
        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getDeploymentStatus",
                "description": "Get latest deterministic deployment status for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
