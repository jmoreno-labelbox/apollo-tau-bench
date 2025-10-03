from tau_bench.envs.tool import Tool
import json
from typing import Any

class CalculateTicketKPIs(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], export_path: str) -> str:
        if "Tickets_Export.csv" not in export_path:
            payload = {"error": "Invalid export path provided."}
            out = json.dumps(payload, indent=2)
            return out
        kpis = {
            "total_open": 46,
            "avg_age_open_hours": 23.5,
            "avg_ttr_mins": 1440,
            "pct_closed_1d": 60.0,
            "p1_open_count": 5,
        }
        payload = kpis
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTicketKpis",
                "description": "Calculates standard service desk KPIs from a ticket export CSV.",
                "parameters": {
                    "type": "object",
                    "properties": {"export_path": {"type": "string"}},
                    "required": ["export_path"],
                },
            },
        }
