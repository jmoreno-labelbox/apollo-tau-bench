# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddSchedulerRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Logs a scheduler run event.
        """
        new_run = {
            "run_id": kwargs.get("run_id"),
            "task_name": kwargs.get("task_name"),
            "run_date": kwargs["run_date"],
            "status": kwargs.get("status"),
            "notes": kwargs.get("notes", "")
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
                    "required": ["run_date",],
                },
            },
        }
