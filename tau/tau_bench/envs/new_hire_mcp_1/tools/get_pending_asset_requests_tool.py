from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPendingAssetRequestsTool(Tool):
    """Fetches asset_requests along with status analysis and associated candidate information for planning fulfillment."""

    @staticmethod
    def invoke(data: dict[str, Any], status_filter: str = None, role_filter: str = None,
    candidate_id: Any = None,
    ) -> str:
        asset_requests = data.get("asset_requests", {}).values()

        # Implement status filter
        if status_filter:
            valid_statuses = {"Pending", "Sent", "Reserved", "Completed"}
            if status_filter not in valid_statuses:
                return _err(
                    f"Invalid status_filter. Valid statuses are: {sorted(list(valid_statuses))}"
                )
            asset_requests = [
                r for r in asset_requests.values() if r.get("status") == status_filter
            ]

        results = []
        candidates_map = {
            str(c.get("candidate_id")): c for c in data.get("candidates", {}).values()
        }

        for request in asset_requests:
            candidate_id = str(request.get("candidate_id"))
            candidate = candidates_map.get(candidate_id)

            if not candidate:
                continue

            # Implement role filter
            if role_filter and candidate.get("role_title") != role_filter:
                continue

            request_copy = request.copy()
            request_copy["candidate"] = {
                "candidate_id": candidate_id,
                "candidate_name": candidate.get("candidate_name"),
                "role_title": candidate.get("role_title"),
                "start_date": candidate.get("start_date"),
            }
            results.append(request_copy)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPendingAssetRequests",
                "description": "Retrieves asset_requests with status analysis and linked candidate information for fulfillment planning.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status_filter": {
                            "type": "string",
                            "description": "Request status ('Pending', 'Sent', 'Reserved', 'Completed')",
                        },
                        "candidate_role_filter": {
                            "type": "string",
                            "description": "Filter by candidate role",
                        },
                    },
                    "required": [],
                },
            },
        }
