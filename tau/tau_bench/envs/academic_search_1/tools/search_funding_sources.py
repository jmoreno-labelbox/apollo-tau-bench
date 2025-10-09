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

class SearchFundingSources(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], source_name: Any = None, focus_area: Any = None, status: Any = None, funding_source_id: Any = None) -> str:
        sources = data.get("funding_sources", [])

        if not source_name and not focus_area and not status and not funding_source_id:
            payload = sources
            out = json.dumps(payload, indent=2)
            return out

        results = [
            s
            for s in sources
            if (
                not source_name
                or source_name.lower() in s.get("source_name", "").lower()
            )
            and (
                not focus_area or s.get("focus_area", "").lower() == focus_area.lower()
            )
            and (not status or s.get("status", "").lower() == status.lower())
            and (not funding_source_id or s.get("sponsor_id") == funding_source_id)
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchFundingSources",
                "description": "Searches for funding sources by name, focus area, status, or funding source ID. If no parameters are provided, it returns all sources.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {
                            "type": "string",
                            "description": "The name of the funding source to search for.",
                        },
                        "focus_area": {
                            "type": "string",
                            "description": "The focus area of the funding source (e.g., 'AI', 'Biomedicine').",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the funding source (e.g., 'available', 'depleted').",
                        },
                        "funding_source_id": {
                            "type": "string",
                            "description": "The ID of the funding source to search for.",
                        },
                    },
                },
            },
        }
