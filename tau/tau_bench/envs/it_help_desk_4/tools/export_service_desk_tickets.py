from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ExportServiceDeskTickets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], start_date: str = None, end_date: str = None, export_path: str = None) -> str:
        tickets = data.get("tickets", [])
        payload = {
                "export_path": export_path,
                "ticket_count": len(tickets),
                "start_date": start_date,
                "end_date": end_date,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "exportServiceDeskTickets",
                "description": "Export service desk tickets within a date range to CSV.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "export_path": {"type": "string"},
                    },
                    "required": ["start_date", "end_date", "export_path"],
                },
            },
        }
