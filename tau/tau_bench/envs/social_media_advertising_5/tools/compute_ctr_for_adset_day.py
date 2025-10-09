from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any

class ComputeCtrForAdsetDay(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        for i in data.get("f_insights", []):
            if i.get("adset_id") == adset_id and i.get("date") == date:
                imp = i.get("impressions", 0)
                clk = i.get("clicks", 0)
                ctr = round(clk / imp, 4) if imp > 0 else 0
                payload = {"adset_id": adset_id, "date": date, "ctr": ctr}
                out = json.dumps(payload)
                return out
        payload = {"error": "ctr_not_available"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeCtrForAdsetDay",
                "description": "Computes CTR for one day.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["adset_id", "date"],
                },
            },
        }
