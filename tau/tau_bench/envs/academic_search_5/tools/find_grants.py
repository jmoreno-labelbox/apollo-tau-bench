from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindGrants(Tool):
    """
    Utility for locating funding sources based on different criteria, or obtaining details of a specific source by its ID.
    """

    @staticmethod
    def invoke(data: dict[str, Any], funding_source_id: Any = None, focus_area: Any = None, status: Any = None, min_grant_amount: Any = None, source_name: Any = None) -> str:
        funding_source_id = funding_source_id
        focus_area = focus_area
        status = status
        min_grant_amount = min_grant_amount

        sources = data.get("funding_sources", {}).values()

        if funding_source_id:
            for source in sources.values():
                if source.get("funding_source_id") == funding_source_id:
                    payload = source
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Funding source with ID '{funding_source_id}' not found."}
            out = json.dumps(
                payload)
            return out

        results = []
        for source in sources.values():
            area_match = (
                not focus_area
                or focus_area.lower() in source.get("focus_area", "").lower()
            )
            status_match = (
                not status or status.lower() == source.get("status", "").lower()
            )
            amount_match = not min_grant_amount or source.get("grant_amount", 0) >= int(
                min_grant_amount
            )

            if area_match and status_match and amount_match:
                results.append(source)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindGrants",
                "description": "Searches for funding sources by criteria (focus area, status, amount), or retrieves a single source by its specific ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "funding_source_id": {
                            "type": "string",
                            "description": "The specific ID of the funding source to retrieve.",
                        },
                        "focus_area": {
                            "type": "string",
                            "description": "The research area the funding supports (e.g., 'AI').",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the grant (e.g., 'available').",
                        },
                        "min_grant_amount": {
                            "type": "integer",
                            "description": "The minimum amount of funding required.",
                        },
                    },
                },
            },
        }
