# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Pitches(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pitcher_ids = kwargs.get("pitcher_ids", [])
        time_window = kwargs.get("time_window")
        # return outcome
        return json.dumps({"performance_data_df": f"df_{'_'.join(pitcher_ids)}_{time_window}"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # output result
        return {"type": "function", "function": {"name": "getPitch", "description": "Collects event-level pitch data.", "parameters": {"type": "object", "properties": {"pitcher_ids": {"type": "array", "items": {"type": "string"}}, "time_window": {"type": "string"}}, "required": ["pitcher_ids", "time_window"]}}}
