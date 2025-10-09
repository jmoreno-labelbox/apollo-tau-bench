from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateWorkflow(Tool):
    """
    Establish a new workflow run with deterministic behavior for the provided data.
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
    def invoke(data: dict[str, Any], dag_name: str = None, game_pk: int = None, status: str = None) -> str:
        # Confirm required fields
        missing = [f for f in ["dag_name", "status"] if locals().get(f) is None]
        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        workflows = data.get("workflow_runs", [])
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
            "log_s3_path": log_path,
        }

        workflows.append(new_entry)
        payload = new_entry
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateWorkflow",
                "description": "Create a new workflow run entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dag_name": {"type": "string"},
                        "game_pk": {"type": ["integer", "null"]},
                        "status": {"type": "string"},
                    },
                    "required": ["dag_name", "status"],
                },
            },
        }
