from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateNewReport(Tool):
    """
    Establish a new player development report.
    Required inputs (exact names):
      - player_id (int)
      - week_of_date (string, YYYY-MM-DD)
      - created_at (string, 'YYYY-MM-DD HH:MM:SS')
      - s3_pdf_path (string)
    Behavior:
      - dev_report_id is auto-generated: max existing + 1 (starts at 1).
    """

    @staticmethod
    def invoke(data: dict[str, Any], player_id: str = None, week_of_date: str = None) -> str:
        #1) Confirm required inputs
        missing = []
        if player_id is None:
            missing.append("player_id")
        if not isinstance(week_of_date, str) or week_of_date == "":
            missing.append("week_of_date")

        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        reports: list[dict[str, Any]] = data.get("player_dev_reports", [])

        new_id = get_next_dev_report_goal_id(data)

        #4) Construct and add the row
        new_row = {
            "dev_report_id": new_id,
            "player_id": player_id,
            "week_of_date": week_of_date,
            "created_at": get_current_timestamp(),
            "s3_pdf_path": f"s3://reports/development/{new_id}.pdf",
        }
        reports.append(new_row)
        payload = new_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewReport",
                "description": "Create a new player development report. dev_report_id auto-generated (max existing + 1).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Player ID the report belongs to.",
                        },
                        "week_of_date": {
                            "type": "string",
                            "description": "Week-of date in YYYY-MM-DD.",
                        },
                    },
                    "required": ["player_id", "week_of_date"],
                },
            },
        }
