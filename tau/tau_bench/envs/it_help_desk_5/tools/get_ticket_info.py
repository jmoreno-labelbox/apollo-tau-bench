from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetTicketInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None) -> str:
        if ticket_id is None:
            payload = {"status": "error", "description": "The ticket_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        tickets = data.get("tickets")

        for ticket in tickets.values():
            if ticket["ticket_id"] == ticket_id:
                payload = ticket
                out = json.dumps(payload, indent=2)
                return out
        payload = {"status": "error", "description": "The ticket was not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTicketInfo",
                "description": "Gets info for a ticket based on ticket_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "The id of the ticket to search for.",
                        },
                    },
                    "required": ["ticket_id"],
                },
            },
        }
