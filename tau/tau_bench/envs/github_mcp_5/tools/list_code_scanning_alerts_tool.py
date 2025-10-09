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

class ListCodeScanningAlertsTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None) -> str:
        if not all([owner, repo]):
            payload = {
                    "status": "error",
                    "message": "Missing required parameters for list_code_scanning_alerts.",
                    "required": ["owner", "repo"],
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

        alerts = data.get("code_scanning_alerts", {}).values()
        repo_alerts = [
            alert
            for alert in alerts.values() if alert["owner"] == owner and alert["repo_name"] == repo
        ]
        payload = {"status": "success", "alerts": repo_alerts}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listCodeScanningAlerts",
                "description": "Lists code scanning alerts for a repository.",
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
                    },
                    "required": ["owner", "repo"],
                },
            },
        }
