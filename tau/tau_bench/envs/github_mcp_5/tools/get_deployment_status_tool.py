# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        repo_name = _validate_param(kwargs, "repo_name", str)
        deploys = list(data.get("deployments", {}).values())
        repo_deploys = [d for d in deploys if d.get("repo") == repo_name]

        if not repo_deploys:
            return _response(
                "error",
                ERROR_MESSAGES["NO_DATA_FOUND"].format(entity=f"Deployments for {repo_name}"),
                "NOT_FOUND"
            )

        latest = max(repo_deploys, key=lambda d: d.get("deployment_date", ""))
        result = {**latest, "report_date": CURRENT_DATE}
        return _response("ok", result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_deployment_status",
                "description": "Get latest deterministic deployment status for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
