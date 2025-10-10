# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAllocation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        allocation_id = kwargs.get("allocation_id")
        hours_per_week = kwargs.get("hours_per_week")
        end_date = kwargs.get("end_date")

        if not allocation_id:
            return json.dumps({"error": "allocation_id is required"})

        allocations = data.get("allocations", [])
        for allocation in allocations:
            if allocation.get("allocation_id") == allocation_id:
                if hours_per_week is not None:
                    allocation["hours_per_week"] = hours_per_week
                if end_date is not None:
                    allocation["end_date"] = end_date
                return json.dumps({"success": True, "allocation": allocation})

        return json.dumps({"error": f"Allocation with ID '{allocation_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_allocation",
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
