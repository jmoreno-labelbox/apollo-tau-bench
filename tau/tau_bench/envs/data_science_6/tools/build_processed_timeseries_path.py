# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildProcessedTimeseriesPath(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city_slug = kwargs.get("city_slug")
        if not city_slug:
            return json.dumps({"error":"Missing city_slug"})
        path = f"/data/processed/timeseries_{city_slug}_weather.csv"
        return json.dumps({"city_slug": city_slug, "csv_path": path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"build_processed_timeseries_path",
                "description":"Builds canonical processed timeseries CSV path for a given city_slug.",
                "parameters":{"type":"object","properties":{"city_slug":{"type":"string"}},"required":["city_slug"]}
            }
        }
