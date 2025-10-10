# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPendingAssetRequestsTool(Tool):
    """Retrieves asset_requests with status analysis and linked candidate information for fulfillment planning."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_role_filter, status_filter) -> str:
        role_filter = candidate_role_filter

        asset_requests = data.get("asset_requests", [])

        # Implement status filter
        if status_filter:
            valid_statuses = {"Pending", "Sent", "Reserved", "Completed"}
            if status_filter not in valid_statuses:
                 return _err(f"Invalid status_filter. Valid statuses are: {sorted(list(valid_statuses))}")
            asset_requests = [r for r in asset_requests if r.get("status") == status_filter]

        results = []
        candidates_map = {str(c.get("candidate_id")): c for c in data.get("candidates", [])}

        for request in asset_requests:
            candidate_id = str(request.get("candidate_id"))
            candidate = candidates_map.get(candidate_id)

            if not candidate:
                continue

            # Implement role-based filtering.
            if role_filter and candidate.get("role_title") != role_filter:
                continue

            request_copy = request.copy()
            request_copy["candidate"] = {
                "candidate_id": candidate_id,
                "candidate_name": candidate.get("candidate_name"),
                "role_title": candidate.get("role_title"),
                "start_date": candidate.get("start_date")
            }
            results.append(request_copy)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pending_asset_requests",
                "description": "Retrieves asset_requests with status analysis and linked candidate information for fulfillment planning.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status_filter": {"type": "string", "description": "Request status ('Pending', 'Sent', 'Reserved', 'Completed')"},
                        "candidate_role_filter": {"type": "string", "description": "Filter by candidate role"}
                    },
                    "required": [],
                },
            },
        }
