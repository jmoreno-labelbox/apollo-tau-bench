from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class GetAlertSeverityDistribution(Tool):
    """Provides overall severity counts for all code scanning alerts."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        alerts = _alerts(data)
        counter = Counter(a.get("severity", "Unknown") for a in alerts)
        payload = dict(counter)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAlertSeverityDistribution",
                "description": "Returns global severity count distribution across all alerts.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
