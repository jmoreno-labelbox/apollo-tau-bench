from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class LogWorkflowRun(Tool):
    """Add a workflow_runs entry with a consistent log_s3_path and defined timestamps."""

    @staticmethod
    def invoke(
        data, 
        dag_name: str, 
        status: str, 
        start_time_utc: str, 
        end_time_utc: str, 
        log_s3_path: str, 
        game_pk: str = None,
        workflow_name: str = None,
        timestamp_utc: str = None
    ) -> str:
        err = _require_tables(data, ["workflow_runs"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {
                "dag_name": dag_name,
                "status": status,
                "start_time_utc": start_time_utc,
                "end_time_utc": end_time_utc,
                "log_s3_path": log_s3_path,
            },
            ["dag_name", "status", "start_time_utc", "end_time_utc", "log_s3_path"],
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        rows = data["workflow_runs"]
        new_id = _next_id(rows, "run_id")
        row = {
            "run_id": new_id,
            "dag_name": dag_name,
            "game_pk": game_pk,
            "status": status,
            "start_time_utc": start_time_utc,
            "end_time_utc": end_time_utc,
            "log_s3_path": log_s3_path,
        }
        rows.append(row)
        payload = {"run_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "LogWorkflowRun",
                "description": "Creates workflow_runs row with explicit timestamps and log path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dag_name": {"type": "string"},
                        "game_pk": {"type": "integer"},
                        "status": {"type": "string"},
                        "start_time_utc": {"type": "string"},
                        "end_time_utc": {"type": "string"},
                        "log_s3_path": {"type": "string"},
                    },
                    "required": [
                        "dag_name",
                        "status",
                        "start_time_utc",
                        "end_time_utc",
                        "log_s3_path",
                    ],
                },
            },
        }
