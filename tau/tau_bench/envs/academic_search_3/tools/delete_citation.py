from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class DeleteCitation(Tool):
    """Utility for removing a citation record."""

    @staticmethod
    def invoke(data: dict[str, Any], citation_id: Any = None) -> str:
        citations = data.get("citations", [])
        original_count = len(citations)
        data["citations"] = [
            c for c in citations if c.get("citation_id") != citation_id
        ]
        if len(data["citations"]) < original_count:
            payload = {
                "status": "success",
                "citation_id": citation_id,
                "message": "Citation deleted.",
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": f"Citation with ID {citation_id} not found."}
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteCitation",
                "description": "Deletes a specific citation record by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "citation_id": {
                            "type": "string",
                            "description": "The unique ID of the citation to delete.",
                        }
                    },
                    "required": ["citation_id"],
                },
            },
        }
