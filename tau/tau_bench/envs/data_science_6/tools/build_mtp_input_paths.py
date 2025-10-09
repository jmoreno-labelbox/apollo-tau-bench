from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class BuildMtpInputPaths(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], merged_timeseries_path: str = None, features_csv_path: str = None, split_summary_json_path: str = None) -> str:
        if (
            not merged_timeseries_path
            or not features_csv_path
            or not split_summary_json_path
        ):
            payload = {
                    "error": "Missing merged_timeseries_path, features_csv_path, or split_summary_json_path"
                }
            out = json.dumps(
                payload)
            return out
        payload = {
                "input_paths": [
                    merged_timeseries_path,
                    features_csv_path,
                    split_summary_json_path,
                ]
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildMtpInputPaths",
                "description": "Builds input_paths array for MTP.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "merged_timeseries_path": {"type": "string"},
                        "features_csv_path": {"type": "string"},
                        "split_summary_json_path": {"type": "string"},
                    },
                    "required": [
                        "merged_timeseries_path",
                        "features_csv_path",
                        "split_summary_json_path",
                    ],
                },
            },
        }
