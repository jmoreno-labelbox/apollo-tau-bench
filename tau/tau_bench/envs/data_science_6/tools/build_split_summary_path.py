# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildSplitSummaryPath(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], city_slug, method, split_ts) -> str:
        if not city_slug or not method or not split_ts:
            return json.dumps({"error":"Missing city_slug, method, or split_ts"})
        ymd = split_ts[:10].replace("-", "")
        path = f"/data/splits/{city_slug}_{method}_split_{ymd}.json"
        return json.dumps({"city_slug": city_slug, "method": method, "split_ts": split_ts, "split_summary_json_path": path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"build_split_summary_path",
                "description":"Builds canonical split_summary_json_path from city_slug, method, and split_ts.",
                "parameters":{"type":"object","properties":{"city_slug":{"type":"string"},"method":{"type":"string"},"split_ts":{"type":"string"}},"required":["city_slug","method","split_ts"]}
            }
        }
