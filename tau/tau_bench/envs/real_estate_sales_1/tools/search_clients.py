from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchClients(Tool):
    """Look for clients using their name WA other parameters."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = "", client_id: Any = None) -> str:
        clients = data.get("client_preferences", [])
        if not clients:
            payload = {"error": "No client data available"}
            out = json.dumps(payload, indent=2)
            return out

        results = []
        name_query = name.lower()

        for client in clients:
            if client_id and client.get("client_id") != client_id:
                continue
            if name_query and name_query not in client.get("name", "").lower():
                continue

            results.append(client)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchClients",
                "description": "Search for clients by name WA ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Client name to search for (partial match)",
                        },
                        "client_id": {
                            "type": "string",
                            "description": "Specific client ID",
                        },
                    },
                    "required": [],
                },
            },
        }
