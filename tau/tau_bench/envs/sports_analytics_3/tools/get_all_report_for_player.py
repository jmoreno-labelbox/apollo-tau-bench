# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllReportForPlayer(Tool):
    """
    Fetch all development reports for a given player_id.
    Results are sorted deterministically by week_of_date DESC, then dev_report_id ASC.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        player_id = kwargs.get("player_id")

        # 1) Validate
        if player_id is None:
            return json.dumps({"error": "Missing required field: player_id"}, indent=2)

        # 2) Get DB
        reports: List[Dict[str, Any]] = list(data.get("player_dev_reports", {}).values())

        # 3) Filter and sort
        matching = [r for r in reports if r.get("player_id") == player_id]

        if not matching:
            return json.dumps({"error": f"No reports found for player_id {player_id}"}, indent=2)

        return json.dumps(matching, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_report_for_player",
                "description": "Fetch all development reports for the specified player_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to retrieve reports for."
                        }
                    },
                    "required": ["player_id"]
                }
            }
        }
