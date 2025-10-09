from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindUnderperformingAdsets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], roas_threshold: float, date: str) -> str:
        out = []
        for i in data.get("f_insights", []):
            if i.get("date") == date:
                spend = i.get("spend", 0)
                revenue = i.get("revenue", 0)
                roas = (revenue / spend) if spend > 0 else 0
                if spend > 0 and roas < roas_threshold:
                    out.append({"adset_id": i.get("adset_id"), "roas": round(roas, 2)})
        payload = {"underperforming_adsets": out}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindUnderperformingAdsets",
                "description": "Finds ad sets below a ROAS threshold for a day.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "roas_threshold": {"type": "number"},
                        "date": {"type": "string"},
                    },
                    "required": ["roas_threshold", "date"],
                },
            },
        }
