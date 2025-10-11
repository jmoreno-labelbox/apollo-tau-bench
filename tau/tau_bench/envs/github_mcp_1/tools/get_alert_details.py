# Copyright belongs to Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAlertDetails(Tool):
    """
    Return all stored details for a code scanning alert identified by
    (owner, repo_name, alert_number).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = (kwargs.get("owner") or "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        alert_number_raw = kwargs.get("alert_number", kwargs.get("alertnumber", None))

        if not owner or not repo_name or alert_number_raw is None:
            return json.dumps(
                {"error": "Required: owner, repo_name (or repo_name), alert_number."},
                indent=2
            )

        # Standardize alert_number
        try:
            alert_number = int(alert_number_raw)
        except Exception:
            return json.dumps({"error": "alert_number must be an integer."}, indent=2)

        # Initialize alerts database.
        alerts_db = data.get("code_scanning_alerts", [])
        if not isinstance(alerts_db, list):
            return json.dumps(
                {"error": "Invalid DB: expected a list at data['code_scanning_alerts']."},
                indent=2
            )

        # Locate the repository bucket.
        rec = next((r for r in alerts_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps(
                {"error": f"No alerts found for repository '{owner}/{repo_name}'."},
                indent=2
            )

        alert_numbers: List[int] = rec.get("alert_numbers", [])
        if alert_number not in alert_numbers:
            return json.dumps(
{"error": f"Alert # {alert_number} is missing for '{owner}/{repo_name}'."},
                indent=2
            )

        idx = alert_numbers.index(alert_number)

        def get_at(key: str):
            arr = rec.get(key, [])
            return arr[idx] if idx < len(arr) else None

        details = {
            "owner": owner,
            "repo_name": repo_name,
            "number": alert_number,
            "severity": get_at("severities"),
            "state": get_at("states"),
            "description": get_at("descriptions"),
            "ref": get_at("refs"),
            "created_ts": get_at("created_ts"),
            "dismissed_ts": get_at("dismissed_ts_nullables")
        }

        return json.dumps(details, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_alert_details",
                "description": "Fetch full details for a code scanning alert (owner, repo_name, alert_number).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: repo_name)."},
                        "alert_number": {"type": "integer", "description": "Alert number within the repository."}
                    },
                    "required": ["owner", "repo_name", "alert_number"]
                }
            }
        }