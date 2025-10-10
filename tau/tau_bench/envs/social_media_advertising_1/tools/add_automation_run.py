# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddAutomationRun(Tool):
    """Adds a new entry to the automation_runs table."""

    @staticmethod
    def invoke(data: Dict[str, Any], ended_at, errors_json, input_ref, reason, run_id, run_type, started_at, status) -> str:
        
        if not run_id:
            return json.dumps({"error": "run_id is a required parameter."})
        if not run_type:
            return json.dumps({"error": "run_type is a required parameter."})
        if not started_at:
            return json.dumps({"error": "started_at is a required parameter."})
        if not ended_at:
            return json.dumps({"error": "ended_at is a required parameter."})
        if not status:
            return json.dumps({"error": "status is a required parameter."})
        if not input_ref:
            return json.dumps({"error": "input_ref is a required parameter."})
        if not errors_json:
            return json.dumps({"error": "errors_json is a required parameter."})

        new_automation_run = {
            "run_id": run_id,
            "run_type": run_type,
            "started_at": started_at,
            "ended_at": ended_at,
            "status": status,
            "input_ref": input_ref,
            "errors_json": errors_json
        }
        
        if reason:
            new_automation_run["reason"] = reason
            
        if "automation_runs" not in data:
            data["automation_runs"] = []
            
        data['automation_runs'].append(new_automation_run)

        return json.dumps(
            {
                "status": "success",
                "message": f"New automation run was added: {new_automation_run}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_automation_run",
                "description": "Adds a new entry to the automation_runs table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {
                            "type": "string",
                            "description": "The unique ID of the automation run.",
                        },
                        "run_type": {
                            "type": "string",
                            "description": "The type of automation run.",
                        },
                        "started_at": {
                            "type": "string",
                            "description": "The start timestamp (ISO format).",
                        },
                        "ended_at": {
                            "type": "string",
                            "description": "The end timestamp (ISO format).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the run.",
                        },
                        "input_ref": {
                            "type": "string",
                            "description": "The input reference for the run.",
                        },
                        "errors_json": {
                            "type": "string",
                            "description": "JSON string of any errors.",
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the automation run.",
                        }
                    },
                    "required": ["run_id", "run_type", "started_at", "ended_at", "status", "input_ref", "errors_json"],
                },
            },
        }
