from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateAllocation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], allocation_id: str = None, hours_per_week: int = None, end_date: str = None) -> str:
        if not allocation_id:
            payload = {"error": "allocation_id is required"}
            out = json.dumps(payload)
            return out

        allocations = data.get("allocations", [])
        for allocation in allocations:
            if allocation.get("allocation_id") == allocation_id:
                if hours_per_week is not None:
                    allocation["hours_per_week"] = hours_per_week
                if end_date is not None:
                    allocation["end_date"] = end_date
                payload = {"success": True, "allocation": allocation}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Allocation with ID '{allocation_id}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAllocation",
                "description": "Update an existing allocation's hours or end date",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "allocation_id": {
                            "type": "string",
                            "description": "The allocation ID to update",
                        },
                        "hours_per_week": {
                            "type": "number",
                            "description": "New hours per week",
                        },
                        "end_date": {"type": "string", "description": "New end date"},
                    },
                    "required": ["allocation_id"],
                },
            },
        }
