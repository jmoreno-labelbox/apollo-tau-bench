# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAlertSummaryPerRepo(Tool):
    """Returns code scanning alert summary (count + severity breakdown) for specified repositories."""

    @staticmethod
    def invoke(data: Dict[str, Any], repo_names = []) -> str:
        if not repo_names:
            return json.dumps({"error": "repo_names is required."}, indent=2)

        alerts = _alerts(data)
        summary = defaultdict(lambda: {"total": 0, "severity_counts": defaultdict(int)})

        for a in alerts:
            repo = a.get("repo_name")
            if repo in repo_names:
                summary[repo]["total"] += 1
                sev = a.get("severity", "Unknown")
                summary[repo]["severity_counts"][sev] += 1

        # Transform nested defaultdicts into standard dicts.
        clean_summary = {
            repo: {
                "total": val["total"],
                "severity_counts": dict(val["severity_counts"])
            } for repo, val in summary.items()
        }

        return json.dumps(clean_summary, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_alert_summary_per_repo",
                "description": "Returns alert summary (total and by severity) for given repo list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_names": {
                            "type": "array",
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["repo_names"]
                }
            }
        }
