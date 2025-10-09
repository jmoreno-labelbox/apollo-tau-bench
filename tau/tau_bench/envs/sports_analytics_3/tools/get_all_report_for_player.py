from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAllReportForPlayer(Tool):
    """
    Retrieve all development reports associated with a specific player_id.
    Results are sorted deterministically by week_of_date in descending order, then dev_report_id in ascending order.
    """

    @staticmethod
    def invoke(data: dict[str, Any], player_id: str = None) -> str:
        #1) Confirm validity
        if player_id is None:
            payload = {"error": "Missing required field: player_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        reports: list[dict[str, Any]] = data.get("player_dev_reports", {}).values()

        #3) Filter and arrange
        matching = [r for r in reports.values() if r.get("player_id") == player_id]

        if not matching:
            payload = {"error": f"No reports found for player_id {player_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = matching
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAllReportForPlayer",
                "description": "Fetch all development reports for the specified player_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to retrieve reports for.",
                        }
                    },
                    "required": ["player_id"],
                },
            },
        }
