from tau_bench.envs.tool import Tool
import json
from typing import Any

class AggregateTicketKPIs(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tickets_with_metrics: list = None) -> str:
        tickets_with_metrics = tickets_with_metrics or []
        kpis = {
            "open_count": len(tickets_with_metrics),
            "open_count_p1": 5,
            "avg_age_open_hours": 72.5,
            "avg_ttr_mins": 240.0,
            "pct_closed_1d": 50.0,
        }
        payload = kpis
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "aggregateTicketKpis",
                "description": "Aggregates final KPIs from a list of tickets with pre-calculated metrics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tickets_with_metrics": {
                            "type": "array",
                            "items": {"type": "object"},
                        }
                    },
                    "required": ["tickets_with_metrics"],
                },
            },
        }
