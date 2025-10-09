from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class DeleteAllocation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], allocation_id: str = None) -> str:
        if not allocation_id:
            payload = {"error": "allocation_id is required"}
            out = json.dumps(payload)
            return out

        allocations = data.get("allocations", [])

        for i, allocation in enumerate(allocations):
            if allocation.get("allocation_id") == allocation_id:
                removed_allocation = allocations.pop(i)
                payload = {"success": True, "removed_allocation": removed_allocation}
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
                "name": "DeleteAllocation",
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
