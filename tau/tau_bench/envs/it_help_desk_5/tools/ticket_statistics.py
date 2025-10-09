from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class TicketStatistics(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        field: str = None,
        stat_type: str = None,
        type: Any = None
    ) -> str:
        if field is None or stat_type is None:
            payload = {
                "status": "error",
                "reason": "The field and type parameters are required.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if field not in [
            "tickets_opened",
            "tickets_closed",
            "closed_within_24h",
            "avg_open_age_hours",
        ]:
            payload = {
                "status": "error",
                "reason": "The specified field could not be found in daily_metrics.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if stat_type not in ["avg", "sum"]:
            payload = {"status": "error", "reason": "Unknown statistic type."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        daily_metrics = data.get("daily_metrics")

        pulled_data = []
        for metrics in daily_metrics.values():
            pulled_data.append(metrics[field])

        if stat_type == "sum":
            payload = {"result": sum(pulled_data)}
            out = json.dumps(payload)
            return out
        elif stat_type == "avg":
            payload = {"result": sum(pulled_data) / len(pulled_data)}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ticketStatistics",
                "description": "Calculates various statistics for ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type": "string",
                            "description": "The field in daily_metrics to target.",
                        },
                        "type": {
                            "type": "string",
                            "description": "The type of statistic to produce.",
                        },
                    },
                    "required": ["field", "type"],
                },
            },
        }
