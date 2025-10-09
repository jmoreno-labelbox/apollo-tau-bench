from tau_bench.envs.tool import Tool
import json
from itertools import islice
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RetrieveMortgageProfile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None) -> str:
        profiles = (
            data.get("mortgage_profiles") or data.get("mortage_profiles") or []
        )  # error tolerance
        prof = next((m for m in profiles if m.get("client_id") == client_id), None)
        if not prof:
            payload = {"error": f"No mortgage profile for client_id={client_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = prof
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RetrieveMortgageProfile",
                "description": "Fetch the mortgage profile for a client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }
