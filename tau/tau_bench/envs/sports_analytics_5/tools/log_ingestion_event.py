# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class LogIngestionEvent(Tool):
    """Append ingestion_logs row."""
    @staticmethod
    def invoke(data, records_ingested, source_name, status_code, request_timestamp_utc = _now_utc_iso())->str:
        err = _require_tables(data, ["ingestion_logs"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["source_name","status_code","records_ingested"])
        if need:
            return json.dumps({"error": need}, indent=2)
        rows = data["ingestion_logs"]
        new_id = _next_id(rows, "ingestion_id")
        row = {
            "ingestion_id": new_id,
            "source_name": source_name,
            "request_timestamp_utc": request_timestamp_utc,
            "status_code": status_code,
            "records_ingested": records_ingested
        }
        rows.append(row)
        return json.dumps({"ingestion_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"log_ingestion_event","description":"Creates ingestion_logs row for observability.","parameters":{"type":"object","properties":{"source_name":{"type":"string"},"status_code":{"type":"integer"},"records_ingested":{"type":"integer"},"request_timestamp_utc":{"type":"string"}},"required":["source_name","status_code","records_ingested"]}}}
