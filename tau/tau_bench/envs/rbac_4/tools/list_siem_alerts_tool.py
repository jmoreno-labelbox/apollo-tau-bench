# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListSiemAlertsTool(Tool):
    """List SIEM alerts with optional filtering."""

    @staticmethod
    def invoke(data: Dict[str, Any], resource_id, severity) -> str:
        res_id = resource_id
        sev = severity
        alerts = data.get("siem_alerts", [])
        results = []
        for a in alerts:
            if res_id and a["resource_id"] != res_id:
                continue
            if sev and a["severity"] != sev:
                continue
            results.append(a)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_siem_alerts",
                "description": "List SIEM alerts filtered by resource or severity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string"},
                        "severity": {"type": "string"}
                    }
                }
            }
        }
