# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchPitchData(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], time_window, pitcher_ids = []) -> str:
        return json.dumps({"performance_data_df": f"df_{'_'.join(pitcher_ids)}_{time_window}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "fetch_pitch_data", "description": "Fetches event-level pitch data.", "parameters": {"type": "object", "properties": {"pitcher_ids": {"type": "array", "items": {"type": "string"}}, "time_window": {"type": "string"}}, "required": ["pitcher_ids", "time_window"]}}}
