from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateScoutingReport(Tool):
    """
    Establish a new scouting report.

    Required inputs (exact names):
      - report_type (string)
      - game_pk (int)
      - created_at (string, 'YYYY-MM-DD HH:MM:SS')
      - s3_pdf_path (string)
      - gslides_link (string)
      - core_narrative_text (string)

    Behavior:
      - report_id is auto-generated: max existing + 1 (starting at 1).
    """

    @staticmethod
    def invoke(data: dict[str, Any], report_type: str = None, game_pk: Any = None, core_narrative_text: str = None) -> str:
        #1) Confirm validity
        missing = []
        if not isinstance(report_type, str) or report_type == "":
            missing.append("report_type")
        if game_pk is None:
            missing.append("game_pk")
        if not isinstance(core_narrative_text, str) or core_narrative_text == "":
            missing.append("core_narrative_text")

        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        reports: list[dict[str, Any]] = data.get("scouting_reports", {}).values()

        #3) Create a new id
        new_id = get_next_scouting_report_id(data)

        #4) Add
        new_row = {
            "report_id": new_id,
            "report_type": report_type,
            "game_pk": game_pk,
            "created_at": get_today_date(),
            "s3_pdf_path": f"s3://reports/scouting/{new_id}.pdf",
            "gslides_link": f"https://docs.google.com/presentation/d/{new_id}",
            "core_narrative_text": core_narrative_text,
        }
        reports.append(new_row)
        payload = new_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        props = {
            "report_type": {
                "type": "string",
                "description": "e.g., 'Pre-Game', 'Post-Game', 'Opponent Analysis', 'Series Summary', 'Player Focus'",
            },
            "game_pk": {
                "type": "integer",
                "description": "Game primary key this report is about.",
            },
            "core_narrative_text": {
                "type": "string",
                "description": "Main narrative text for the report.",
            },
        }
        return {
            "type": "function",
            "function": {
                "name": "CreateScoutingReport",
                "description": "Create a new scouting report; report_id auto-generated (max existing + 1).",
                "parameters": {
                    "type": "object",
                    "properties": props,
                    "required": list(props.keys()),
                },
            },
        }
