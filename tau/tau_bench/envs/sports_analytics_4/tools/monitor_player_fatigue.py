from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class MonitorPlayerFatigue(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], player_id: str = None) -> str:
        workloads = data.get("player_workload", [])
        workload = next((w for w in workloads if w.get("player_id") == player_id), {})
        fatigue_score = (
            workload.get("innings_pitched", 0) * 0.5
            + workload.get("pitches_thrown", 0) * 0.1
        )
        payload = {"player_id": player_id, "fatigue_score": fatigue_score}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "monitorPlayerFatigue",
                "description": "Calculates a deterministic fatigue score for a pitcher based on innings and pitches thrown.",
                "parameters": {
                    "type": "object",
                    "properties": {"player_id": {"type": "integer"}},
                    "required": ["player_id"],
                },
            },
        }
