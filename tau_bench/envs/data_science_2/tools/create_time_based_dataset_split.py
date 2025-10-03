from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateTimeBasedDatasetSplit(Tool):
    """Generates a dataset_split record from processed_timeseries row_count using a deterministic floor split."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        processed_csv_path: str,
        test_fraction: float,
        split_summary_json_path: str,
        split_ts: str,
    ) -> str:
        pts = data.get("processed_timeseries", [])
        row = None
        for r in pts:
            if r.get("csv_path") == processed_csv_path:
                row = r
                break
        if not row:
            payload = {
                "error": "processed_timeseries not found",
                "csv_path": processed_csv_path,
            }
            out = json.dumps(payload)
            return out
        total = int(row.get("row_count", 0))
        if test_fraction < 0 or test_fraction > 1:
            payload = {"error": "invalid test_fraction"}
            out = json.dumps(payload)
            return out
        test_count = int(total * test_fraction)
        train_count = total - test_count
        rec = {
            "method": "time_based",
            "test_fraction": test_fraction,
            "train_index_count": train_count,
            "test_index_count": test_count,
            "split_summary_json_path": split_summary_json_path,
            "split_ts": split_ts,
        }
        data.setdefault("dataset_split", []).append(rec)
        payload = {"status": "inserted", "record": rec}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTimeBasedDatasetSplit",
                "description": "Creates a dataset_split record from processed_timeseries row_count using floor(test_fraction*rows).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "processed_csv_path": {"type": "string"},
                        "test_fraction": {"type": "number"},
                        "split_summary_json_path": {"type": "string"},
                        "split_ts": {"type": "string"},
                    },
                    "required": [
                        "processed_csv_path",
                        "test_fraction",
                        "split_summary_json_path",
                        "split_ts",
                    ],
                },
            },
        }
