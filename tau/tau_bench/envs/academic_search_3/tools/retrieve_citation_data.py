from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RetrieveCitationData(Tool):
    """Utility for retrieving complete details of a particular citation."""

    @staticmethod
    def invoke(data: dict[str, Any], citation_id: Any = None) -> str:
        for citation in data.get("citations", []):
            if citation.get("citation_id") == citation_id:
                payload = citation
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Citation with ID {citation_id} not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RetrieveCitationData",
                "description": "Retrieves the full details of a specific citation by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "citation_id": {
                            "type": "string",
                            "description": "The unique ID of the citation.",
                        }
                    },
                    "required": ["citation_id"],
                },
            },
        }
