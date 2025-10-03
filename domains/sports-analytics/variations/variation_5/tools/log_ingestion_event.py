from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class LogIngestionEvent(Tool):
    """Add an entry to ingestion_logs."""

    @staticmethod
    def invoke(data, source_name: str, status_code: int, records_ingested: int, request_timestamp_utc: str = None, ingested_at_utc: str = None, timestamp_utc: str = None, message: str = None, game_pk: Any = None) -> str:
        err = _require_tables(data, ["ingestion_logs"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {"source_name": source_name, "status_code": status_code, "records_ingested": records_ingested},
            ["source_name", "status_code", "records_ingested"]
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        rows = data["ingestion_logs"]
        new_id = _next_id(rows, "ingestion_id")
        # Use ingested_at_utc if provided, otherwise request_timestamp_utc, otherwise current time
        timestamp = ingested_at_utc or request_timestamp_utc or _now_utc_iso()
        row = {
            "ingestion_id": new_id,
            "source_name": source_name,
            "request_timestamp_utc": timestamp,
            "status_code": status_code,
            "records_ingested": records_ingested,
        }
        rows.append(row)
        payload = {"ingestion_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "LogIngestionEvent",
                "description": "Creates ingestion_logs row for observability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {"type": "string"},
                        "status_code": {"type": "integer"},
                        "records_ingested": {"type": "integer"},
                        "request_timestamp_utc": {"type": "string"},
                    },
                    "required": ["source_name", "status_code", "records_ingested"],
                },
            },
        }
