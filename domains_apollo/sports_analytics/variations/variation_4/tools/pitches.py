from tau_bench.envs.tool import Tool
import json
from typing import Any

class Pitches(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], pitcher_ids: list[str] = None, time_window: str = None,
    team_id: Any = None,
    game_pk: Any = None,
    ) -> str:
        if pitcher_ids is None:
            pitcher_ids = []
        payload = {"performance_data_df": f"df_{'_'.join(pitcher_ids)}_{time_window}"}
        out = json.dumps(
            payload, indent=2,
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
                "name": "getPitch",
                "description": "Collects event-level pitch data.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitcher_ids": {"type": "array", "items": {"type": "string"}},
                        "time_window": {"type": "string"},
                    },
                    "required": ["pitcher_ids", "time_window"],
                },
            },
        }
