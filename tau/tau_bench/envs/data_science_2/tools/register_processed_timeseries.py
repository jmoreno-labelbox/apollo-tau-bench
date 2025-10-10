# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RegisterProcessedTimeseries(Tool):
    """
    Appends a processed_timeseries record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        req = {"csv_path", "columns", "row_count", "min_timestamp", "max_timestamp", "file_hash_sha256", "created_ts"}
        if not req.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        data.setdefault("processed_timeseries", []).append(record)
        return json.dumps({"status": "inserted", "csv_path": record.get("csv_path")})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "register_processed_timeseries",
                "description": "Appends a processed_timeseries record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }
