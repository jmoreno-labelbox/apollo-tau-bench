# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetScoutingReportByGamepkAndType(Tool):
    """
    Fetch scouting reports by game_pk, optionally filtering by report_type.

    Inputs (exact names):
      - game_pk (int)       [required]
      - report_type (str)   [optional] exact, case-sensitive

    Behavior:
      - If report_type is provided, return only exact matches.
      - If not provided, return all reports for the game.
      - Deterministic ordering: created_at ASC, then report_id ASC.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")
        report_type = kwargs.get("report_type")

        # 1) Validate
        if game_pk is None:
            return json.dumps({"error": "Missing required field: game_pk"}, indent=2)

        # 2) Get DB
        reports: List[Dict[str, Any]] = list(data.get("scouting_reports", {}).values())

        # 3) Filter
        matches = [r for r in reports if r.get("game_pk") == game_pk]
        if report_type is not None:
            matches = [r for r in matches if r.get("report_type") == report_type]

        if not matches:
            if report_type is None:
                return json.dumps({"error": f"No scouting reports found for game_pk {game_pk}"}, indent=2)
            return json.dumps({"error": f"No scouting reports found for game_pk {game_pk} with type '{report_type}'"}, indent=2)

        # 4) Sort deterministically
        matches.sort(key=lambda r: (r.get("created_at", ""), int(r.get("report_id", 0))))
        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_scouting_report_by_gamepk_and_type",
                "description": "Fetch scouting reports for a game; optionally filter by exact report_type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer", "description": "Game primary key."},
                        "report_type": {"type": "string", "description": "Optional exact report type (case-sensitive)."}
                    },
                    "required": ["game_pk"]
                }
            }
        }
