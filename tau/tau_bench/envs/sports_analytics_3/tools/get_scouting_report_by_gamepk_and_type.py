from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetScoutingReportByGamepkAndType(Tool):
    """
    Retrieve scouting reports using game_pk, with optional filtering by report_type.

    Inputs (exact names):
      - game_pk (int)       [required]
      - report_type (str)   [optional] exact, case-sensitive

    Behavior:
      - If report_type is provided, return only exact matches.
      - If not provided, return all reports for the game.
      - Deterministic ordering: created_at in ascending order, then report_id in ascending order.
    """

    @staticmethod
    def invoke(data: dict[str, Any], game_pk: int = None, report_type: str = None) -> str:
        #1) Confirm validity
        if game_pk is None:
            payload = {"error": "Missing required field: game_pk"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        reports: list[dict[str, Any]] = data.get("scouting_reports", {}).values()

        #3) Apply filter
        matches = [r for r in reports.values() if r.get("game_pk") == game_pk]
        if report_type is not None:
            matches = [r for r in matches.values() if r.get("report_type") == report_type]

        if not matches:
            if report_type is None:
                payload = {"error": f"No scouting reports found for game_pk {game_pk}"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            payload = {
                    "error": f"No scouting reports found for game_pk {game_pk} with type '{report_type}'"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #4) Sort in a deterministic manner
        matches.sort(
            key=lambda r: (r.get("created_at", ""), int(r.get("report_id", 0)))
        )
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getScoutingReportByGamepkAndType",
                "description": "Fetch scouting reports for a game; optionally filter by exact report_type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Game primary key.",
                        },
                        "report_type": {
                            "type": "string",
                            "description": "Optional exact report type (case-sensitive).",
                        },
                    },
                    "required": ["game_pk"],
                },
            },
        }
