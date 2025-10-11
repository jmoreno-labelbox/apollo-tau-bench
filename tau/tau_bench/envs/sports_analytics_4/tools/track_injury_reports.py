# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TrackInjuryReports(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], player_id) -> str:
        injuries = data.get("injury_reports", [])
        player_injuries = [i for i in injuries if i.get("player_id") == player_id]
        # return outcome
        return json.dumps({"player_id": player_id, "injury_history": player_injuries}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return output
        return {
            "type": "function",
            "function": {
                "name": "track_injury_reports",
                "description": "Retrieves injury history for a given player from injury_reports.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {"type": "integer"}
                    },
                    "required": ["player_id"]
                }
            }
        }
