# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFvpTimestamps(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        return json.dumps({"started_ts": "2024-03-17T10:20:00Z", "finished_ts_nullable": "2024-03-17T10:25:00Z"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_fvp_timestamps","description":"Returns canonical started_ts and finished_ts_nullable for FVP.","parameters":{"type":"object","properties":{}}}}
