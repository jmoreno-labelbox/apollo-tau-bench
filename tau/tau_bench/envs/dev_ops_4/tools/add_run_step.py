# Copyright © Sierra

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
    def invoke(data, ended_at, name, run_id, started_at, status, step_id):
        step = {
            "id": step_id,
            "name": name,
            "status": status,
            "started_at": started_at,
            "ended_at": ended_at,
        }
        runs = list(data.get("build_runs", {}).values())
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        steps = run.get("steps") or []
        steps.append(step)
        run["steps"] = steps
        return json.dumps({"run": run}, indent=2)
