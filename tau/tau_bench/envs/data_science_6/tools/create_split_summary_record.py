from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class CreateSplitSummaryRecord(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        method: str = None,
        test_fraction: float = None,
        train_index_count: int = None,
        test_index_count: int = None,
        split_summary_json_path: str = None,
        split_ts: str = None
    ) -> str:
        if method != "time_based":
            payload = {"error": "Only 'time_based' method is supported."}
            out = json.dumps(payload)
            return out
        try:
            test_fraction = float(test_fraction)
            train_index_count = int(train_index_count)
            test_index_count = int(test_index_count)
        except Exception:
            payload = {"error": "Invalid numeric fields."}
            out = json.dumps(payload)
            return out
        if not split_summary_json_path or not isinstance(split_summary_json_path, str):
            payload = {"error": "split_summary_json_path is required."}
            out = json.dumps(payload)
            return out
        if not split_ts or not isinstance(split_ts, str):
            payload = {"error": "split_ts is required (ISO 8601)."}
            out = json.dumps(payload)
            return out

        ds = data.get("dataset_split", [])
        for rec in ds:
            if (
                rec.get("method") == method
                and rec.get("test_fraction") == test_fraction
                and rec.get("train_index_count") == train_index_count
                and rec.get("test_index_count") == test_index_count
                and rec.get("split_summary_json_path") == split_summary_json_path
                and rec.get("split_ts") == split_ts
            ):
                payload = rec
                out = json.dumps(payload)
                return out

        new_rec = {
            "method": method,
            "test_fraction": test_fraction,
            "train_index_count": train_index_count,
            "test_index_count": test_index_count,
            "split_summary_json_path": split_summary_json_path,
            "split_ts": split_ts,
        }
        ds.append(new_rec)
        data["dataset_split"] = ds
        payload = new_rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSplitSummaryRecord",
                "description": "Creates a deterministic split summary record in dataset_split (no extra fields).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "method": {"type": "string", "enum": ["time_based"]},
                        "test_fraction": {"type": "number"},
                        "train_index_count": {"type": "integer"},
                        "test_index_count": {"type": "integer"},
                        "split_summary_json_path": {"type": "string"},
                        "split_ts": {"type": "string"},
                    },
                    "required": [
                        "method",
                        "test_fraction",
                        "train_index_count",
                        "test_index_count",
                        "split_summary_json_path",
                        "split_ts",
                    ],
                },
            },
        }
