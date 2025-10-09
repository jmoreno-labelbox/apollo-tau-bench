from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAlertDetails(Tool):
    """
    Return all stored details for a code scanning alert identified by
    (owner, repo_name, alert_number).
    """

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo_name: str = None, alert_number: int = None, alertnumber: int = None) -> str:
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
        alerts_db = _convert_db_to_list(data.get("code_scanning_alerts", {}))
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
            "dismissed_ts": get_at("dismissed_ts_nullables"),
        }
        payload = details
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAlertDetails",
                "description": "Fetch full details for a code scanning alert (owner, repo_name, alert_number).",
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
