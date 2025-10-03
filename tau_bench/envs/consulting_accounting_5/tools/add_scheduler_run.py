from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class AddSchedulerRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str = None, task_name: str = None, run_date: str = None, status: str = None, notes: str = "", note: str = None) -> str:
        """
        Logs a scheduler run event.
        """
        # Accept either 'note' or 'notes' parameter
        if note is not None:
            notes = note
        new_run = {
            "run_id": run_id,
            "task_name": task_name,
            "run_date": run_date,
            "status": status,
            "notes": notes
        }
        data["scheduler_runs"].append(new_run)
        return json.dumps(new_run["run_id"])
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddSchedulerRun",
                "description": "Log a new scheduler run event into scheduler_runs.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "task_name": {"type": "string"},
                        "run_date": {"type": "string"},
                        "status": {"type": "string"},
                        "notes": {"type": "string"}
                    },
                    "required": ["run_date"],
                },
            },
        }
