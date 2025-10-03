from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class SearchAllocations(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], end_date_before: str = None, status: str = None, allocation_id: str = None) -> str:
        allocations = data.get("allocations", [])
        results = []

        for allocation in allocations:
            match = True

            if end_date_before and allocation.get("end_date"):
                if allocation.get("end_date") >= end_date_before:
                    match = False

            if status and allocation.get("status") != status:
                match = False

            if allocation_id and allocation.get("allocation_id") != allocation_id:
                match = False

            if match:
                results.append(allocation)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchAllocations",
                "description": "Search allocations by end date, status, or allocation_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "end_date_before": {
                            "type": "string",
                            "description": "Find allocations ending before this date (YYYY-MM-DD)",
                        },
                        "status": {
                            "type": "string",
                            "description": "Status to filter by",
                        },
                        "allocation_id": {
                            "type": "string",
                            "description": "allocation_id of the allocation to get",
                        },
                    },
                },
            },
        }
