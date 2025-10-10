# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildMergedTimeseriesPath(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city_slug = kwargs.get("city_slug")
        start_ts = kwargs.get("start_ts")
        end_ts = kwargs.get("end_ts")
        if not city_slug or not start_ts or not end_ts:
            return json.dumps({"error":"Missing city_slug, start_ts, end_ts"})
        y0 = start_ts[:10].replace("-","")
        y1 = end_ts[:10].replace("-","")
        return json.dumps({"merged_timeseries_path": f"/processed_data/merged_timeseries_{city_slug}_{y0}_{y1}.csv"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_merged_timeseries_path","description":"Builds canonical merged timeseries path from city_slug and analysis window.","parameters":{"type":"object","properties":{"city_slug":{"type":"string"},"start_ts":{"type":"string"},"end_ts":{"type":"string"}},"required":["city_slug","start_ts","end_ts"]}}}
