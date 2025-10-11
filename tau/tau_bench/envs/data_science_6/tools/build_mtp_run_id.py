# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildMtpRunId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], city_slug, end_ts, model_name, start_ts) -> str:
        if not city_slug or not model_name or not start_ts or not end_ts:
            return json.dumps({"error":"Missing city_slug, model_name, start_ts, or end_ts"})
        y0 = start_ts[:10].replace("-","")
        y1 = end_ts[:10].replace("-","")
        return json.dumps({"run_id": f"mt_{city_slug}_{model_name}_{y0}_{y1}_v1"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_mtp_run_id","description":"Builds canonical MTP run_id from city_slug, model_name, and analysis window.","parameters":{"type":"object","properties":{"city_slug":{"type":"string"},"model_name":{"type":"string"},"start_ts":{"type":"string"},"end_ts":{"type":"string"}},"required":["city_slug","model_name","start_ts","end_ts"]}}}
