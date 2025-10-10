# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MonitorPlayerFatigue(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        player_id = kwargs.get("player_id")
        workloads = data.get("player_workload", [])
        workload = next((w for w in workloads if w.get("player_id") == player_id), {})
        fatigue_score = (workload.get("innings_pitched", 0) * 0.5 + workload.get("pitches_thrown", 0) * 0.1)
        # return result
        return json.dumps({"player_id": player_id, "fatigue_score": fatigue_score}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {
            "type": "function",
            "function": {
                "name": "monitor_player_fatigue",
                "description": "Calculates a deterministic fatigue score for a pitcher based on innings and pitches thrown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {"type": "integer"}
                    },
                    "required": ["player_id"]
                }
            }
        }
