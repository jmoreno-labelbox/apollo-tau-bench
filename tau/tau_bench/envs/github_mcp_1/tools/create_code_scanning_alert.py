from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
    def invoke(
        data: dict[str, Any],
        owner: str = None,
        repo_name: str = None,
        severity: str = None,
        description: str = None,
        ref: str = None,
    ) -> str:
        owner = (owner or "").strip()
        repo_name = (repo_name or "").strip()
        severity_raw = (severity or "").strip()
        description = (description or "").strip()
        ref = (ref or "").strip()

        if not owner or not repo_name or not severity_raw or not description or not ref:
            payload = {
                    "error": "Required: owner, repo_name (or repo_name), severity, description, ref."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Normalize/validate severity
        severity = severity_raw.lower()
        allowed = {"critical", "high", "medium", "low"}
        if severity not in allowed:
            payload = {
                    "error": f"Invalid severity '{severity_raw}'. Use one of: critical, high, medium, low."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Load alerts DB
        alerts_db = _convert_db_to_list(data.get("code_scanning_alerts", {}).values())
        if not isinstance(alerts_db, list):
            payload = {
                    "error": "Invalid DB: expected a list at data['code_scanning_alerts']."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Find or create repo bucket
        rec = next(
            (
                r
                for r in alerts_db
                if r.get("owner") == owner and r.get("repo_name") == repo_name
            ),
            None,
        )
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
                "dismissed_ts_nullables": [],
            }
            alerts_db.append(rec)
            created_bucket = True

        # Ensure arrays exist
        for key in [
            "alert_numbers",
            "severities",
            "states",
            "descriptions",
            "refs",
            "created_ts",
            "dismissed_ts_nullables",
        ]:
            rec.setdefault(key, [])

        # Next alert number (per repo)
        next_alert_number = get_next_alert_number(data)

        # Deterministic timestamp from your environment helper
        new_ts = get_current_timestamp()

        # Append new alert
        rec["alert_numbers"].append(next_alert_number)
        rec["severities"].append(severity)
        rec["states"].append("open")
        rec["descriptions"].append(description)
        rec["refs"].append(ref)
        rec["created_ts"].append(new_ts)
        rec["dismissed_ts_nullables"].append(None)

        add_terminal_message(
            data,
            (
                f"Created new alerts bucket and alert #{next_alert_number}"
                if created_bucket
                else f"Added alert #{next_alert_number} to existing bucket"
            ),
            get_current_timestamp(),
        )
        payload = {
                "success": (
                    f"Created new alerts bucket and alert #{next_alert_number}"
                    if created_bucket
                    else f"Added alert #{next_alert_number} to existing bucket"
                ),
                "repo": f"{owner}/{repo_name}",
                "alert": {
                    "number": next_alert_number,
                    "severity": severity,
                    "state": "open",
                    "description": description,
                    "ref": ref,
                    "created_ts": new_ts,
                    "dismissed_ts": None,
                },
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
                "name": "CreateCodeScanningAlert",
                "description": "Create a new code scanning alert for a repository; creates the repo bucket if missing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name (alias: repo_name).",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Severity: critical, high, medium, or low.",
                        },
                        "description": {
                            "type": "string",
                            "description": "Alert description.",
                        },
                        "ref": {
                            "type": "string",
                            "description": "Git ref (e.g., refs/heads/main).",
                        },
                    },
                    "required": [
                        "owner",
                        "repo_name",
                        "severity",
                        "description",
                        "ref",
                    ],
                },
            },
        }
