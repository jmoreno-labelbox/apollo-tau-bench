# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAlertSeverityDistribution(Tool):
    """Returns global severity counts across all code scanning alerts."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alerts = _alerts(data)
        counter = Counter(a.get("severity", "Unknown") for a in alerts)
        return json.dumps(dict(counter), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_alert_severity_distribution",
                "description": "Returns global severity count distribution across all alerts.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
