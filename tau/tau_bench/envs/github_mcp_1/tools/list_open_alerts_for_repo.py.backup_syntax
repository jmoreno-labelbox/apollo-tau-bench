from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListOpenAlertsForRepo(Tool):
    """
    List open code scanning alerts for a repository.
    - Inputs (required): owner, repo_name (alias: repo_name)
    - Inputs (optional): severity (critical/high/medium/low), ref (e.g., refs/heads/main)
    - Returns a list of open alerts with basic details, sorted by alert number.
    """

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = "", repo_name: str = "", severity: str = "", ref: str = "") -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        severity_raw = severity.strip()
        ref_filter = ref.strip()

        if not owner or not repo_name:
            payload = {"error": "Required: owner, repo_name (or repo_name)."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Normalize optional severity
        severity_filter = None
        if severity_raw:
            sev = severity_raw.lower()
            if sev not in {"critical", "high", "medium", "low"}:
                payload = {
                    "error": "Invalid 'severity'. Use one of: critical, high, medium, low."
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            severity_filter = sev

        # Load alerts DB
        alerts_db = _convert_db_to_list(data.get("code_scanning_alerts", {}).values()
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

        def get_at(key: str, i: int):
            arr = rec.get(key, [])
            return arr[i] if i < len(arr) else None

        # Build list of open alerts, optionally filter by severity/ref
        indexed: list[tuple] = [(num, i) for i, num in enumerate(alert_numbers)]
        indexed.sort(key=lambda t: t[0])

        results: list[dict[str, Any]] = []
        for num, idx in indexed:
            state = get_at("states", idx)
            if state != "open":
                continue

            sev = (get_at("severities", idx) or "").lower()
            alert_ref = get_at("refs", idx) or ""

            if severity_filter and sev != severity_filter:
                continue
            if ref_filter and alert_ref != ref_filter:
                continue

            results.append(
                {
                    "number": num,
                    "severity": sev,
                    "state": state,
                    "description": get_at("descriptions", idx),
                    "ref": alert_ref,
                    "created_ts": get_at("created_ts", idx),
                    "dismissed_ts": get_at("dismissed_ts_nullables", idx),
                }
            )
        payload = {
            "owner": owner,
            "repo_name": repo_name,
            "count": len(results),
            "alerts": results,
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
                "name": "ListOpenAlertsForRepo",
                "description": "List open code scanning alerts for a repository, optionally filtered by severity and ref.",
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
                            "enum": ["critical", "high", "medium", "low"],
                            "description": "Optional severity filter.",
                        },
                        "ref": {
                            "type": "string",
                            "description": "Optional Git ref filter (e.g., refs/heads/main).",
                        },
                    },
                    "required": ["owner", "repo_name"],
                },
            },
        }
