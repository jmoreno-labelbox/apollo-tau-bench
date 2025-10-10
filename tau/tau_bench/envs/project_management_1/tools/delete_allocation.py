# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteAllocation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], allocation_id) -> str:
        if not allocation_id:
            return json.dumps({"error": "allocation_id is required"})

        allocations = data.get("allocations", [])

        for i, allocation in enumerate(allocations):
            if allocation.get("allocation_id") == allocation_id:
                removed_allocation = allocations.pop(i)
                return json.dumps(
                    {"success": True, "removed_allocation": removed_allocation}
                )

        return json.dumps({"error": f"Allocation with ID '{allocation_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_allocation",
                "description": "Remove an allocation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "allocation_id": {
                            "type": "string",
                            "description": "The allocation ID to delete",
                        }
                    },
                    "required": ["allocation_id"],
                },
            },
        }
