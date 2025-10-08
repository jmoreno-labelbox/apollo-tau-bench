from tau_bench.envs.tool import Tool
import json
from typing import Any

class DismissAlert(Tool):
    """
    Dismiss a code scanning alert for a given repository.
    - Sets states[idx] = "dismissed"
    - Sets dismissed_ts_nullables[idx] = get_current_updated_timestamp()
    - Idempotent: if already dismissed, returns current info without changing anything.
    Inputs: owner, repo_name (alias: repo_name), alert_number
    """

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo_name: str = None, alert_number: Any = None, alertnumber: Any = None,
    dismiss_reason: Any = None,
    ) -> str:
        owner = (owner or "").strip()
        repo_name = (repo_name or repo_name or "").strip()
        alert_number_raw = alert_number if alert_number is not None else alertnumber

        if not owner or not repo_name or alert_number_raw is None:
            payload = {"error": "Required: owner, repo_name (or repo_name), alert_number."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Normalize alert_number
        try:
            alert_number = int(alert_number_raw)
        except Exception:
            payload = {"error": "alert_number must be an integer."}
            out = json.dumps(payload, indent=2)
            return out

        # Load alerts DB
        alerts_db = data.get("code_scanning_alerts", [])
        if not isinstance(alerts_db, list):
            payload = {
                    "error": "Invalid DB: expected a list at data['code_scanning_alerts']."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Find repo bucket
        rec = next(
            (
                r
                for r in alerts_db
                if r.get("owner") == owner and r.get("repo_name") == repo_name
            ),
            None,
        )
        if rec is None:
            payload = {"error": f"No alerts found for repository '{owner}/{repo_name}'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        alert_numbers: list[int] = rec.get("alert_numbers", [])
        if alert_number not in alert_numbers:
            payload = {
                    "error": f"Alert #{alert_number} not found for '{owner}/{repo_name}'."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        idx = alert_numbers.index(alert_number)

        # Ensure required arrays exist/padded
        rec.setdefault("states", [])
        rec.setdefault("dismissed_ts_nullables", [])
        while len(rec["states"]) <= idx:
            rec["states"].append("open")
        while len(rec["dismissed_ts_nullables"]) <= idx:
            rec["dismissed_ts_nullables"].append(None)

        current_state = rec["states"][idx]
        current_dismissed_ts = rec["dismissed_ts_nullables"][idx]

        # Idempotent behavior if already dismissed
        if current_state == "dismissed":
            payload = {
                    "success": f"Alert #{alert_number} is already dismissed for {owner}/{repo_name}.",
                    "repo": f"{owner}/{repo_name}",
                    "alert_number": alert_number,
                    "state": "dismissed",
                    "dismissed_ts": current_dismissed_ts,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Dismiss the alert
        rec["states"][idx] = "dismissed"
        new_dismissed_ts = get_current_updated_timestamp()
        rec["dismissed_ts_nullables"][idx] = new_dismissed_ts

        add_terminal_message(
            data,
            f"Alert #{alert_number} dismissed for {owner}/{repo_name}.",
            get_current_updated_timestamp(),
        )
        payload = {
                "success": f"Alert #{alert_number} dismissed for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "alert_number": alert_number,
                "state": "dismissed",
                "dismissed_ts": new_dismissed_ts,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DismissAlert",
                "description": "Dismiss a code scanning alert: sets state='dismissed' and records dismissed timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name (alias: repo_name).",
                        },
                        "alert_number": {
                            "type": "integer",
                            "description": "Alert number within the repository.",
                        },
                    },
                    "required": ["owner", "repo_name", "alert_number"],
                },
            },
        }
