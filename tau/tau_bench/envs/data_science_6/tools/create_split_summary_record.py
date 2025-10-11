# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateSplitSummaryRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], method, split_summary_json_path, split_ts, test_fraction, test_index_count, train_index_count) -> str:

        if method != "time_based":
            return json.dumps({"error": "Only 'time_based' method is supported."})
        try:
            test_fraction = float(test_fraction)
            train_index_count = int(train_index_count)
            test_index_count = int(test_index_count)
        except Exception:
            return json.dumps({"error":"Invalid numeric fields."})
        if not split_summary_json_path or not isinstance(split_summary_json_path, str):
            return json.dumps({"error": "split_summary_json_path is required."})
        if not split_ts or not isinstance(split_ts, str):
            return json.dumps({"error": "split_ts is required (ISO 8601)."})

        ds = data.get("dataset_split", [])
        for rec in ds:
            if (rec.get("method") == method and
                rec.get("test_fraction") == test_fraction and
                rec.get("train_index_count") == train_index_count and
                rec.get("test_index_count") == test_index_count and
                rec.get("split_summary_json_path") == split_summary_json_path and
                rec.get("split_ts") == split_ts):
                return json.dumps(rec)

        new_rec = {
            "method": method,
            "test_fraction": test_fraction,
            "train_index_count": train_index_count,
            "test_index_count": test_index_count,
            "split_summary_json_path": split_summary_json_path,
            "split_ts": split_ts
        }
        ds.append(new_rec)
        data["dataset_split"] = ds
        return json.dumps(new_rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"create_split_summary_record",
                "description":"Creates a deterministic split summary record in dataset_split (no extra fields).",
                "parameters":{
                    "type":"object",
                    "properties":{
                        "method":{"type":"string","enum":["time_based"]},
                        "test_fraction":{"type":"number"},
                        "train_index_count":{"type":"integer"},
                        "test_index_count":{"type":"integer"},
                        "split_summary_json_path":{"type":"string"},
                        "split_ts":{"type":"string"}
                    },
                    "required":["method","test_fraction","train_index_count","test_index_count","split_summary_json_path","split_ts"]
                }
            }
        }
