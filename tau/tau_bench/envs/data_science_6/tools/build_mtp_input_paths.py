# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildMtpInputPaths(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], features_csv_path, merged_timeseries_path, split_summary_json_path) -> str:
        if not merged_timeseries_path or not features_csv_path or not split_summary_json_path:
            return json.dumps({"error":"Missing merged_timeseries_path, features_csv_path, or split_summary_json_path"})
        return json.dumps({"input_paths":[merged_timeseries_path, features_csv_path, split_summary_json_path]})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_mtp_input_paths","description":"Builds input_paths array for MTP.","parameters":{"type":"object","properties":{"merged_timeseries_path":{"type":"string"},"features_csv_path":{"type":"string"},"split_summary_json_path":{"type":"string"}},"required":["merged_timeseries_path","features_csv_path","split_summary_json_path"]}}}
