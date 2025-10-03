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

class RegisterDeployEventTool(Tool):
    """
    Register a new deterministic deploy event (in-memory only).

    This tool logs a deploy event for a repository in a specific environment.
    A deterministic `event_id` is generated via `_safe_id`, based on repository,
    environment, and date. The event is stamped with CURRENT_DATE.

    Input Parameters:
        repo_name (str): The name of the repository.
        environment (str): The deployment environment (e.g., "staging", "production").

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the deploy event was registered successfully, or "error" otherwise.
            - data: Metadata of the created deploy event, including deterministic `event_id`.

    Errors:
        - Returns an error if parameters are missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, environment: str = None) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            environment = _validate_param({"environment": environment}, "environment", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        events = data.get("terminal", [])

        new_event = {
            "repo": repo_name,
            "environment": environment,
            "type": "deploy",
            "date": CURRENT_DATE,
        }
        new_event["event_id"] = _safe_id(
            new_event, "event_id", "DEPLOY_", ["repo", "environment", "date"]
        )
        events.append(new_event)
        return _response("ok", new_event)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterDeployEvent",
                "description": "Register a deterministic deploy event (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "environment": {"type": "string"},
                    },
                    "required": ["repo_name", "environment"],
                },
            },
        }
