# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogWorkflowRun(Tool):
    """Insert workflow_runs row with deterministic log_s3_path and explicit timestamps."""
    @staticmethod
    def invoke(data, **kwargs)->str:
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
            "dag_name": kwargs.get("dag_name"),
            "game_pk": kwargs.get("game_pk"),
            "status": kwargs.get("status"),
            "start_time_utc": kwargs.get("start_time_utc"),
            "end_time_utc": kwargs.get("end_time_utc"),
            "log_s3_path": kwargs.get("log_s3_path")
        }
        rows.append(row)
        return json.dumps({"run_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"log_workflow_run","description":"Creates workflow_runs row with explicit timestamps and log path.","parameters":{"type":"object","properties":{"dag_name":{"type":"string"},"game_pk":{"type":"integer"},"status":{"type":"string"},"start_time_utc":{"type":"string"},"end_time_utc":{"type":"string"},"log_s3_path":{"type":"string"}},"required":["dag_name","status","start_time_utc","end_time_utc","log_s3_path"]}}}
