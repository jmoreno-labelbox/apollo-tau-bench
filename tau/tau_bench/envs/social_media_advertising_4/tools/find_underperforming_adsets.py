from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindUnderperformingAdsets(Tool):
    """Identifies ad sets that fall below a specific ROAS threshold."""

    @staticmethod
    def invoke(data: dict[str, Any], roas_threshold: float = None, date: str = None) -> str:
        adsets = []
        for i in data.get("f_insights", []):
            if i.get("date") == date:
                spend, revenue = i.get("spend", 0), i.get("revenue", 0)
                roas = (revenue / spend) if spend > 0 else 0
                if spend > 0 and roas < roas_threshold:
                    adsets.append({"adset_id": i["adset_id"], "roas": round(roas, 2)})
        payload = {"underperforming_adsets": adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindUnderperformingAdsets",
                "description": "Finds all ad sets with a ROAS below a specified threshold for a given day.",
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
