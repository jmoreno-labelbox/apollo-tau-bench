from tau_bench.envs.tool import Tool
import json
from typing import Any

class CalculateServiceDeskKPIs(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], input_path: str = None, metrics: Any = None, output_path: str = None) -> str:
        kpis = {
            "total_open": 46,
            "avg_age_open_hours": 23.5,
            "avg_ttr_mins": 1440,
            "pct_closed_1d": 60.0,
            "p1_open_count": 5,
        }
        payload = {"kpis": kpis, "output_path": output_path}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculateServiceDeskKpis",
                "description": "Calculate service desk KPIs from ticket data.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "input_path": {"type": "string"},
                        "metrics": {"type": "array", "items": {"type": "string"}},
                        "output_path": {"type": "string"},
                    },
                    "required": ["input_path", "metrics", "output_path"],
                },
            },
        }
