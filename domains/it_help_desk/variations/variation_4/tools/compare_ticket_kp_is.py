from tau_bench.envs.tool import Tool
import json
from typing import Any

class CompareTicketKPIs(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], current_kpis: dict[str, Any] = None, previous_kpis: dict[str, Any] = None) -> str:
        delta = {
            "total_open_delta": current_kpis.get("total_open", 0)
            - previous_kpis.get("total_open", 0),
            "p1_open_delta": current_kpis.get("p1_open_count", 0)
            - previous_kpis.get("p1_open_count", 0),
        }
        analysis_summary = f"KPI comparison complete. Open tickets changed by {delta['total_open_delta']}. P1 tickets changed by {delta['p1_open_delta']}."
        payload = {"analysis_summary": analysis_summary, "delta": delta}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CompareTicketKpis",
                "description": "Compares two sets of ticket KPIs to find the delta.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_kpis": {"type": "object"},
                        "previous_kpis": {"type": "object"},
                    },
                    "required": ["current_kpis", "previous_kpis"],
                },
            },
        }
