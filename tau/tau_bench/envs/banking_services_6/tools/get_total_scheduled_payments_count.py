from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetTotalScheduledPaymentsCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("scheduled_payments", []))
        return json.dumps({"total_scheduled_payments": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalScheduledPaymentsCount",
                        "description": "Returns the current total number of scheduled payments in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }
