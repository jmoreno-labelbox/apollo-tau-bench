# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddRunStep(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "add_run_step",
                "description": "Adds a step entry to a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "step_id": {"type": "string", "description": "Unique step id"},
                        "name": {"type": "string", "description": "Human readable step name"},
                        "status": {"type": "string", "description": "pending|running|completed|failed", "enum": ["pending", "running", "completed", "failed"]},
                        "started_at": {"type": "string", "description": "ISO8601 start time"},
                        "ended_at": {"type": "string", "description": "ISO8601 end time"}
                    },
                    "required": ["run_id", "step_id", "name", "status"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        run_id = kwargs.get("run_id")
        step = {
            "id": kwargs.get("step_id"),
            "name": kwargs.get("name"),
            "status": kwargs.get("status"),
            "started_at": kwargs.get("started_at"),
            "ended_at": kwargs.get("ended_at"),
        }
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        steps = run.get("steps") or []
        steps.append(step)
        run["steps"] = steps
        return json.dumps({"run": run}, indent=2)
