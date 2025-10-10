# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListOpenAlertsForRepo(Tool):
    """
    List open code scanning alerts for a repository.
    - Inputs (required): owner, repo_name (alias: repo_name)
    - Inputs (optional): severity (critical/high/medium/low), ref (e.g., refs/heads/main)
    - Returns a list of open alerts with basic details, sorted by alert number.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = (kwargs.get("owner") or "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        severity_raw = (kwargs.get("severity") or "").strip()
        ref_filter = (kwargs.get("ref") or "").strip()

        if not owner or not repo_name:
            return json.dumps(
                {"error": "Required: owner, repo_name (or repo_name)."},
                indent=2
            )

        # Standardize optional severity levels.
        severity_filter = None
        if severity_raw:
            sev = severity_raw.lower()
            if sev not in {"critical", "high", "medium", "low"}:
                return json.dumps(
                    {"error": "Invalid 'severity'. Use one of: critical, high, medium, low."},
                    indent=2
                )
            severity_filter = sev

        # Initialize alerts database.
        alerts_db = data.get("code_scanning_alerts", [])
        if not isinstance(alerts_db, list):
            return json.dumps(
                {"error": "Invalid DB: expected a list at data['code_scanning_alerts']."},
                indent=2
            )

        # Locate repository bucket
        rec = next((r for r in alerts_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps(
                {"error": f"No alerts found for repository '{owner}/{repo_name}'."},
                indent=2
            )

        alert_numbers: List[int] = rec.get("alert_numbers", [])

        def get_at(key: str, i: int):
            arr = rec.get(key, [])
            return arr[i] if i < len(arr) else None

        # Create a list of active alerts, with an option to filter by severity/reference.
        indexed: List[tuple] = [(num, i) for i, num in enumerate(alert_numbers)]
        indexed.sort(key=lambda t: t[0])

        results: List[Dict[str, Any]] = []
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

            results.append({
                "number": num,
                "severity": sev,
                "state": state,
                "description": get_at("descriptions", idx),
                "ref": alert_ref,
                "created_ts": get_at("created_ts", idx),
                "dismissed_ts": get_at("dismissed_ts_nullables", idx),
            })

        return json.dumps(
            {
                "owner": owner,
                "repo_name": repo_name,
                "count": len(results),
                "alerts": results
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_open_alerts_for_repo",
                "description": "List open code scanning alerts for a repository, optionally filtered by severity and ref.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: repo_name)."},
                        "severity": {
                            "type": "string",
                            "enum": ["critical", "high", "medium", "low"],
                            "description": "Optional severity filter."
                        },
                        "ref": {"type": "string", "description": "Optional Git ref filter (e.g., refs/heads/main)."}
                    },
                    "required": ["owner", "repo_name"]
                }
            }
        }
