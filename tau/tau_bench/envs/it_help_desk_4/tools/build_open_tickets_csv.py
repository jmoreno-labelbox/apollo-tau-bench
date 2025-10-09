from tau_bench.envs.tool import Tool
import json
from typing import Any

class BuildOpenTicketsCSV(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], open_tickets: list) -> str:
        file_path = f"\\\\IT\\Reports\\DailyReports\\{FIXED_NOW.split('T')[0]}\\Open_Tickets.csv"
        payload = {"file_path": file_path, "rows_written": len(open_tickets)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "buildOpenTicketsCsv",
                "description": "Builds and saves the Open_Tickets.csv file from a list of open tickets.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "open_tickets": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["open_tickets"],
                },
            },
        }
