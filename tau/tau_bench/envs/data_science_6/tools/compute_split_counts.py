# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeSplitCounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        row_count = kwargs.get("row_count")
        test_fraction = kwargs.get("test_fraction")
        try:
            row_count = int(row_count)
            test_fraction = float(test_fraction)
        except Exception:
            return json.dumps({"error":"row_count must be int and test_fraction must be float"})
        if row_count < 0 or not (0 < test_fraction < 1):
            return json.dumps({"error":"Invalid values for row_count or test_fraction"})
        train_index_count = int(row_count * (1 - test_fraction))
        test_index_count = row_count - train_index_count
        return json.dumps({
            "row_count": row_count,
            "test_fraction": test_fraction,
            "train_index_count": train_index_count,
            "test_index_count": test_index_count
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"compute_split_counts",
                "description":"Computes train/test counts given row_count and test_fraction (floor rule).",
                "parameters":{"type":"object","properties":{"row_count":{"type":"integer"},"test_fraction":{"type":"number"}},"required":["row_count","test_fraction"]}
            }
        }
