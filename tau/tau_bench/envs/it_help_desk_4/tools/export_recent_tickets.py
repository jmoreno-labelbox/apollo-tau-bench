from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ExportRecentTickets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], days: int = 30) -> str:
        tickets = data.get("tickets", {}).values()
        report_path = f"\\\\IT\\Reports\\DailyReports\\{FIXED_NOW.split('T')[0]}\\Tickets_Export.csv"
        payload = {"export_path": report_path, "ticket_count": len(tickets)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportRecentTickets",
                "description": "Exports all tickets updated in the last N days to a CSV file.",
                "parameters": {
                    "type": "object",
                    "properties": {"days": {"type": "integer"}},
                    "required": ["days"],
                },
            },
        }
