# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateWorkflow(Tool):
    """
    Create a new workflow run with deterministic behavior for provided data.
    Inputs:
      - dag_name (str)    : DAG name
      - game_pk (int)     : Game PK (nullable)
      - status (str)      : Initial status
      - end_time_utc (str): End time in UTC (YYYY-MM-DD HH:MM:SS)
      - log_s3_path (str) : Optional log path, defaults to None
    Output:
      - Created workflow run object
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        dag_name = kwargs.get("dag_name")
        game_pk = kwargs.get("game_pk") or None
        status = kwargs.get("status")
        

        # Validate required fields
        missing = [f for f in ["dag_name", "status"] if kwargs.get(f) is None]
        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        workflows = list(data.get("workflow_runs", {}).values())
        run_id = get_next_workflow_run_id(data)
        start_time = get_log_start_timestamp()
        end_time = get_log_end_timestamp()
        log_path = f"s3://logs/workflows/{run_id}.log"

        new_entry = {
            "run_id": run_id,
            "dag_name": dag_name,
            "game_pk": game_pk,
            "status": status,
            "start_time_utc": start_time,
            "end_time_utc": end_time,
            "log_s3_path": log_path
        }

        workflows.append(new_entry)
        return json.dumps(new_entry, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_workflow",
                "description": "Create a new workflow run entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dag_name": {"type": "string"},
                        "game_pk": {"type": ["integer", "null"]},
                        "status": {"type": "string"},
                    },
                    "required": ["dag_name", "status"]
                }
            }
        }
