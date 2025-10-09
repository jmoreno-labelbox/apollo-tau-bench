from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetOnTimeDeliveryStats(Tool):
    """Utility for computing the average percentage of on-time deliveries for all carriers."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_scacs: list[str] = None) -> str:
        carriers = data.get("carriers", {}).values()
        if not carriers:
            payload = {"average_on_time_delivery": 0.0}
            out = json.dumps(payload, indent=2)
            return out
        if list_of_scacs:
            carriers = [c for c in carriers.values() if c["scac"] in list_of_scacs]
        total = sum(
            c.get("performance_metrics", {}).values().get("on_time_delivery_percentage", 0)
            for c in carriers
        )
        average = total / len(carriers)
        payload = {"average_on_time_delivery": average}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOnTimeDeliveryStats",
                "description": "Calculate average on-time delivery percentage across all carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_scacs": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of carriers to choose from.",
                        }
                    },
                },
            },
        }
