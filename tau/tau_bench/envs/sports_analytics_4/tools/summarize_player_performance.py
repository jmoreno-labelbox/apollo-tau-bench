# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SummarizePlayerPerformance(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], player_id) -> str:
        games = data.get("games", [])
        stats = [g for g in games if player_id in g.get("player_stats", {})]
        summary = {
            "player_id": player_id,
            "games_played": len(stats),
            "avg_batting_avg": sum(s["player_stats"][player_id].get("batting_avg", 0) for s in stats) / max(len(stats), 1),
            "avg_ops": sum(s["player_stats"][player_id].get("ops", 0) for s in stats) / max(len(stats), 1),
        }
        # return output
        return json.dumps(summary, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return output
        return {
            "type": "function",
            "function": {
                "name": "summarize_player_performance",
                "description": "Creates an aggregated summary of a player's recent performance over available games.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {"type": "integer"}
                    },
                    "required": ["player_id"]
                }
            }
        }
