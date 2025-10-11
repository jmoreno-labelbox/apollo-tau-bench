# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadNoaaStationSearches(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        rows = list(data.get("noaa_station_searches", {}).values()) or []
        return json.dumps({"rows": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_noaa_station_searches",
            "description": "List prior NOAA station discovery queries/results.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }}
