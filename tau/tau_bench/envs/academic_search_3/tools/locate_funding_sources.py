from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LocateFundingSources(Tool):
    """Utility for identifying funding sources based on research area and availability."""

    @staticmethod
    def invoke(data: dict[str, Any], area: str = None, status: str = None, funding_source_id: str = None, source_name: str = None) -> str:
        sources = data.get("funding_sources", [])
        results = []
        area = area.lower() if area else ""
        status = status.lower() if status else ""
        source_name = source_name.lower() if source_name else ""

        for s in sources:
            match_area = not area or area in s.get("focus_area", "").lower()
            match_status = not status or status == s.get("status", "").lower()
            match_id = not funding_source_id or funding_source_id == s.get("sponsor_id")
            match_name = not source_name or source_name in s.get("source_name", "").lower()

            if match_area and match_status and match_id and match_name:
                results.append(s)
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LocateFundingSources",
                "description": "Locates funding sources by research area, availability, funding source ID, or source name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "area": {
                            "type": "string",
                            "description": "The research area (e.g., 'AI', 'Medical Research').",
                        },
                        "status": {
                            "type": "string",
                            "description": "The availability status of the grant (e.g., 'available').",
                        },
                        "funding_source_id": {
                            "type": "string",
                            "description": "The ID of the funding source to search for.",
                        },
                        "source_name": {
                            "type": "string",
                            "description": "The name of the funding source to search for.",
                        },
                    },
                    "required": [],
                },
            },
        }
