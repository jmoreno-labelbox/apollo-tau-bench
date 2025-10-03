from tau_bench.envs.tool import Tool
import json
from typing import Any

class FetchPitchData(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        pitcher_ids = kwargs.get("pitcher_ids", [])
        time_window = kwargs.get("time_window")
        payload = {"performance_data_df": f"df_{'_'.join(pitcher_ids)}_{time_window}"}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchPitchData",
                "description": "Fetches event-level pitch data.",
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
