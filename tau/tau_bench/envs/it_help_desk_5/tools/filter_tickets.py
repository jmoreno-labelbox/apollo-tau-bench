from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FilterTickets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ids: list = None, status: str = None, not_status: str = None) -> str:
        if ids is None:
            ids = []

        if len(ids) == 0 and all([param is None for param in [status, not_status]]):
            payload = {
                "status": "error",
                "description": "Input parameters to search for are required.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        tickets = data.get("tickets")
        temp_tickets = tickets.copy()

        if len(ids) != 0:
            temp_tickets = [
                ticket for ticket in temp_tickets if ticket["ticket_id"] in ids
            ]
        if status is not None:
            temp_tickets = [
                ticket for ticket in temp_tickets if ticket["status"] == status
            ]
        if not_status is not None:
            temp_tickets = [
                ticket for ticket in temp_tickets if ticket["status"] != not_status
            ]
        payload = temp_tickets
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filterTickets",
                "description": "Filters tickets by input criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "An array of ticket ids to search for.",
                        },
                        "status": {
                            "type": "string",
                            "description": "A status to search for.",
                        },
                        "not_status": {
                            "type": "string",
                            "description": "A status to exclude from search results.",
                        },
                    },
                },
            },
        }
