# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRepositoryRiskScoreTool(Tool):
    """
    Calculate a deterministic security risk score for a repository.

    This tool analyzes all open security alerts for a repository and
    computes a risk score based on the number and severity of alerts.
    Higher severity alerts contribute more weight to the risk score.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if calculated successfully, or "error" otherwise.
            - data: A dictionary with:
                - repo (str): Repository name.
                - open_alerts (int): Count of open alerts.
                - severity_breakdown (Dict[str, int]): Count of alerts per severity (normalized).
                - risk_score (int): Deterministic numeric risk score.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        alerts = data.get("code_scanning_alerts", [])
        open_alerts = [a for a in alerts if a.get("repo") == repo_name and a.get("state") == "open"]

        score = sum(
            {"critical": 5, "high": 3, "medium": 2, "low": 1}.get(a.get("severity", "low"), 1)
            for a in open_alerts
        )

        result = {
            "repo": repo_name,
            "open_alerts_count": len(open_alerts),
            "risk_score": score,
            "report_date": CURRENT_DATE,
        }
        return _response("ok", result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repository_risk_score",
                "description": "Calculate deterministic risk score for a repository based on open alerts.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
