# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            environment = _validate_param(kwargs, "environment", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        events = data.get("terminal", [])

        new_event = {
            "repo": repo_name,
            "environment": environment,
            "type": "deploy",
            "date": CURRENT_DATE,
        }
        new_event["event_id"] = _safe_id(new_event, "event_id", "DEPLOY_", ["repo", "environment", "date"])
        events.append(new_event)
        return _response("ok", new_event)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "register_deploy_event",
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
