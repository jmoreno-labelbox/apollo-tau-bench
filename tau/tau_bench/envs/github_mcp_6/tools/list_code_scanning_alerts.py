from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListCodeScanningAlerts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str, repo: str) -> str:
        """List code scanning alerts for a repo."""
        pass
        alerts_data = data.get("code_scanning_alerts", {}).values()

        for alert_entry in alerts_data.values():
            if alert_entry["owner"] == owner and alert_entry["repo_name"] == repo:
                alerts = []
                for i, alert_num in enumerate(alert_entry["alert_numbers"]):
                    alerts.append(
                        {
                            "number": alert_num,
                            "severity": alert_entry["severities"][i],
                            "state": alert_entry["states"][i],
                            "ref": alert_entry["refs"][i],
                        }
                    )
                payload = {"alerts": alerts}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"alerts": []}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listCodeScanningAlerts",
                "description": "List code scanning alerts for a repo.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                    },
                    "required": ["owner", "repo"],
                },
            },
        }
