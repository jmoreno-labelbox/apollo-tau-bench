from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListSiemAlertsTool(Tool):
    """Display SIEM alerts with optional filters."""

    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None, severity: str = None,
    severity_in: Any = None,
    ) -> str:
        alerts = data.get("siem_alerts", [])
        results = []
        for a in alerts:
            if resource_id and a["resource_id"] != resource_id:
                continue
            if severity and a["severity"] != severity:
                continue
            results.append(a)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListSiemAlerts",
                "description": "List SIEM alerts filtered by resource or severity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string"},
                        "severity": {"type": "string"},
                    },
                },
            },
        }
