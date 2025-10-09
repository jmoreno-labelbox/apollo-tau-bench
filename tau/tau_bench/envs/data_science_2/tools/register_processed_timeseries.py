from tau_bench.envs.tool import Tool
import json
from typing import Any

class RegisterProcessedTimeseries(Tool):
    """Adds a processed_timeseries record."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        csv_path: str = None,
        columns: list[str] = None,
        row_count: int = None,
        min_timestamp: str = None,
        max_timestamp: str = None,
        file_hash_sha256: str = None,
        created_ts: str = None
    ) -> str:
        req = {
            "csv_path",
            "columns",
            "row_count",
            "min_timestamp",
            "max_timestamp",
            "file_hash_sha256",
            "created_ts",
        }
        record = {
            "csv_path": csv_path,
            "columns": columns,
            "row_count": row_count,
            "min_timestamp": min_timestamp,
            "max_timestamp": max_timestamp,
            "file_hash_sha256": file_hash_sha256,
            "created_ts": created_ts,
        }
        if not req.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        data.setdefault("processed_timeseries", []).append(record)
        payload = {"status": "inserted", "csv_path": csv_path}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "registerProcessedTimeseries",
                "description": "Appends a processed_timeseries record.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }
