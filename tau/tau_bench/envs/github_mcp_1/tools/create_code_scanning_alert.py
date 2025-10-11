# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCodeScanningAlert(Tool):
    """
    Create a new code scanning alert for a repository in the code_scanning_alerts DB.
    - Inputs: owner, repo_name (alias: repo_name), severity, description, ref
    - Behavior:
        * If (owner, repo_name) bucket does NOT exist: create a new record and add alert #1.
        * Else: append a new alert with next alert_number = max(existing)+1.
    - Fields:
        * state: "open"
        * created_ts: get_current_updated_timestamp()
        * dismissed_ts_nullables: null
    """

    @staticmethod
    def invoke(data: Dict[str, Any], owner, repo_name, severity, description, ref) -> str:
        owner = (owner or "").strip()
        repo_name = (repo_name or repo_name or "").strip()
        severity_raw = (severity or "").strip()
        description = (description or "").strip()
        ref = (ref or "").strip()

        if not owner or not repo_name or not severity_raw or not description or not ref:
            return json.dumps(
                {"error": "Required: owner, repo_name (or repo_name), severity, description, ref."},
                indent=2
            )

        # Standardize/verify severity
        severity = severity_raw.lower()
        allowed = {"critical", "high", "medium", "low"}
        if severity not in allowed:
            return json.dumps(
                {"error": f"Invalid severity '{severity_raw}'. Use one of: critical, high, medium, low."},
                indent=2
            )

        # Initialize alerts database.
        alerts_db = data.get("code_scanning_alerts", [])
        if not isinstance(alerts_db, list):
            return json.dumps(
                {"error": "Invalid DB: expected a list at data['code_scanning_alerts']."},
                indent=2
            )

        # Locate or establish a repository bucket.
        rec = next((r for r in alerts_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        created_bucket = False
        if rec is None:
            rec = {
                "owner": owner,
                "repo_name": repo_name,
                "alert_numbers": [],
                "severities": [],
                "states": [],
                "descriptions": [],
                "refs": [],
                "created_ts": [],
                "dismissed_ts_nullables": []
            }
            alerts_db.append(rec)
            created_bucket = True

        # Verify the presence of arrays.
        for key in ["alert_numbers","severities","states","descriptions","refs","created_ts","dismissed_ts_nullables"]:
            rec.setdefault(key, [])

        # Subsequent alert identifier (for each repository)
        next_alert_number = get_next_alert_number(data)

        # Environment helper for obtaining a deterministic timestamp.
        new_ts = get_current_timestamp()

        # Add a new notification.
        rec["alert_numbers"].append(next_alert_number)
        rec["severities"].append(severity)
        rec["states"].append("open")
        rec["descriptions"].append(description)
        rec["refs"].append(ref)
        rec["created_ts"].append(new_ts)
        rec["dismissed_ts_nullables"].append(None)

add_terminal_message(data, f"Created new alerts bucket and alert #{next_alert_number}" if created_bucket else f"Alert #{next_alert_number} added to existing bucket", get_current_timestamp())

return json.dumps(
            {
                "success": (
f"Created new alerts bucket and alert # {subsequent_alert_number}"
                    if created_bucket else
f"Added alert # {next_alert_number} to the current bucket."
                ),
                "repo": f"{owner}/{repo_name}",
                "alert": {
                    "number": next_alert_number,
                    "severity": severity,
                    "state": "open",
                    "description": description,
                    "ref": ref,
                    "created_ts": new_ts,
                    "dismissed_ts": None
                }
            },
            indent=2
        )

@staticmethod
def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_code_scanning_alert",
                "description": "Create a new code scanning alert for a repository; creates the repo bucket if missing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: repo_name)."},
                        "severity": {"type": "string", "description": "Severity: critical, high, medium, or low."},
                        "description": {"type": "string", "description": "Alert description."},
                        "ref": {"type": "string", "description": "Git ref (e.g., refs/heads/main)."}
                    },
                    "required": ["owner", "repo_name", "severity", "description", "ref"]
                }
            }
        }