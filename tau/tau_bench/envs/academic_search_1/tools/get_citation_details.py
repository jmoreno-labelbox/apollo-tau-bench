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

class GetCitationDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], citation_id: Any = None) -> str:
        citation_id = citation_id
        if not citation_id:
            payload = {"error": "citation_id is required."}
            out = json.dumps(payload)
            return out

        for citation in data.get("citations", {}).values():
            if citation.get("reference_id") == citation_id:
                payload = citation
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Citation with ID '{citation_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCitationDetails",
                "description": "Retrieves the full details for a single citation by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "citation_id": {
                            "type": "string",
                            "description": "The unique ID of the citation to retrieve.",
                        }
                    },
                    "required": ["citation_id"],
                },
            },
        }
