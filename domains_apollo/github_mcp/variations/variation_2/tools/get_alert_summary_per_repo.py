from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class GetAlertSummaryPerRepo(Tool):
    """Provides a summary of code scanning alerts (count and severity breakdown) for the specified repositories."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_names: list[str] = None, repo_name: Any = None) -> str:
        if not repo_names:
            payload = {"error": "repo_names is required."}
            out = json.dumps(payload, indent=2)
            return out

        alerts = _alerts(data)
        summary = defaultdict(lambda: {"total": 0, "severity_counts": defaultdict(int)})

        for a in alerts:
            repo = a.get("repo_name")
            if repo in repo_names:
                summary[repo]["total"] += 1
                sev = a.get("severity", "Unknown")
                summary[repo]["severity_counts"][sev] += 1

        # Transform nested defaultdicts into standard dictionaries
        clean_summary = {
            repo: {
                "total": val["total"],
                "severity_counts": dict(val["severity_counts"]),
            }
            for repo, val in summary.items()
        }
        payload = clean_summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getAlertSummaryPerRepo",
                "description": "Returns alert summary (total and by severity) for given repo list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_names": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["repo_names"],
                },
            },
        }
