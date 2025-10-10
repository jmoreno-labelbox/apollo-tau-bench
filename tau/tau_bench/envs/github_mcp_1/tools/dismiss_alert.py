# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DismissAlert(Tool):
    """
    Dismiss a code scanning alert for a given repository.
    - Sets states[idx] = "dismissed"
    - Sets dismissed_ts_nullables[idx] = get_current_updated_timestamp()
    - Idempotent: if already dismissed, returns current info without changing anything.
    Inputs: owner, repo_name (alias: repo_name), alert_number
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

        # Normalize alert_number
        try:
            alert_number = int(alert_number_raw)
        except Exception:
            return json.dumps({"error": "alert_number must be an integer."}, indent=2)

        # Load alerts DB
        alerts_db = data.get("code_scanning_alerts", [])
        if not isinstance(alerts_db, list):
            return json.dumps(
                {"error": "Invalid DB: expected a list at data['code_scanning_alerts']."},
                indent=2
            )

        # Find repo bucket
        rec = next((r for r in alerts_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps(
                {"error": f"No alerts found for repository '{owner}/{repo_name}'."},
                indent=2
            )

        alert_numbers: List[int] = rec.get("alert_numbers", [])
        if alert_number not in alert_numbers:
            return json.dumps(
                {"error": f"Alert #{alert_number} not found for '{owner}/{repo_name}'."},
                indent=2
            )

        idx = alert_numbers.index(alert_number)

        # Ensure required arrays exist/padded
        rec.setdefault("states", [])
        rec.setdefault("dismissed_ts_nullables", [])
        while len(rec["states"]) <= idx: rec["states"].append("open")
        while len(rec["dismissed_ts_nullables"]) <= idx: rec["dismissed_ts_nullables"].append(None)

        current_state = rec["states"][idx]
        current_dismissed_ts = rec["dismissed_ts_nullables"][idx]

        # Idempotent behavior if already dismissed
        if current_state == "dismissed":
            return json.dumps(
                {
                    "success": f"Alert #{alert_number} is already dismissed for {owner}/{repo_name}.",
                    "repo": f"{owner}/{repo_name}",
                    "alert_number": alert_number,
                    "state": "dismissed",
                    "dismissed_ts": current_dismissed_ts
                },
                indent=2
            )

        # Dismiss the alert
        rec["states"][idx] = "dismissed"
        new_dismissed_ts = get_current_updated_timestamp()
        rec["dismissed_ts_nullables"][idx] = new_dismissed_ts

        add_terminal_message(data, f"Alert #{alert_number} dismissed for {owner}/{repo_name}.", get_current_updated_timestamp())

        return json.dumps(
            {
                "success": f"Alert #{alert_number} dismissed for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "alert_number": alert_number,
                "state": "dismissed",
                "dismissed_ts": new_dismissed_ts
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "dismiss_alert",
                "description": "Dismiss a code scanning alert: sets state='dismissed' and records dismissed timestamp.",
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
