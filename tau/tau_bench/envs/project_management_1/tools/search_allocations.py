# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchAllocations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        end_date_before = kwargs.get("end_date_before")
        status = kwargs.get("status")
        allocation_id = kwargs.get("allocation_id")

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

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_allocations",
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
