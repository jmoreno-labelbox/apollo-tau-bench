from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetMonthlyAuditBySnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], snapshot_id: str) -> str:
        """
        Returns row_ids of monthly expenses for a given snapshot_id.
        """
        records = [me["row_id"] for me in data.get("monthly_expenses", {}).values() if me["snapshot_id"] == snapshot_id]
        return json.dumps(records)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMonthlyAuditBySnapshot",
                "description": "Retrieve all monthly expense row_ids tied to a dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string", "description": "Snapshot ID to filter monthly expenses"}
                    },
                    "required": ["snapshot_id"],
                },
            },
        }
