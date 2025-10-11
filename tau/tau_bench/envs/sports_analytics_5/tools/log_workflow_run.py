# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables








def _require_tables(data: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [t for t in required if t not in data or data.get(t) is None]
    if missing:
        return f"Missing required table(s): {', '.join(missing)}"
    return None

def _next_id(rows: List[Dict[str, Any]], key: str) -> int:
    max_id = 0
    for r in rows:
        try:
            max_id = max(max_id, int(r.get(key, 0)))
        except Exception:
            pass
    return max_id + 1

def _check_required(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return f"Missing required argument(s): {', '.join(missing)}"
    return None

class LogWorkflowRun(Tool):
    """Insert workflow_runs row with deterministic log_s3_path and explicit timestamps."""
    @staticmethod
    def invoke(data, dag_name, end_time_utc, game_pk, log_s3_path, start_time_utc, status)->str:
        err = _require_tables(data, ["workflow_runs"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["dag_name","status","start_time_utc","end_time_utc","log_s3_path"])
        if need:
            return json.dumps({"error": need}, indent=2)
        rows = data["workflow_runs"]
        new_id = _next_id(rows, "run_id")
        row = {
            "run_id": new_id,
            "dag_name": dag_name,
            "game_pk": game_pk,
            "status": status,
            "start_time_utc": start_time_utc,
            "end_time_utc": end_time_utc,
            "log_s3_path": log_s3_path
        }
        rows.append(row)
        return json.dumps({"run_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"log_workflow_run","description":"Creates workflow_runs row with explicit timestamps and log path.","parameters":{"type":"object","properties":{"dag_name":{"type":"string"},"game_pk":{"type":"integer"},"status":{"type":"string"},"start_time_utc":{"type":"string"},"end_time_utc":{"type":"string"},"log_s3_path":{"type":"string"}},"required":["dag_name","status","start_time_utc","end_time_utc","log_s3_path"]}}}