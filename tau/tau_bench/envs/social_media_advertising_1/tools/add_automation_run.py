from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AddAutomationRun(Tool):
    """Inserts a new record into the automation_runs table."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        run_id: str = None,
        run_type: str = None,
        started_at: str = None,
        ended_at: str = None,
        status: str = None,
        input_ref: str = None,
        errors_json: str = None,
        reason: str = None
    ) -> str:
        if not run_id:
            payload = {"error": "run_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not run_type:
            payload = {"error": "run_type is a required parameter."}
            out = json.dumps(payload)
            return out
        if not started_at:
            payload = {"error": "started_at is a required parameter."}
            out = json.dumps(payload)
            return out
        if not ended_at:
            payload = {"error": "ended_at is a required parameter."}
            out = json.dumps(payload)
            return out
        if not status:
            payload = {"error": "status is a required parameter."}
            out = json.dumps(payload)
            return out
        if not input_ref:
            payload = {"error": "input_ref is a required parameter."}
            out = json.dumps(payload)
            return out
        if not errors_json:
            payload = {"error": "errors_json is a required parameter."}
            out = json.dumps(payload)
            return out

        new_automation_run = {
            "run_id": run_id,
            "run_type": run_type,
            "started_at": started_at,
            "ended_at": ended_at,
            "status": status,
            "input_ref": input_ref,
            "errors_json": errors_json,
        }

        if reason:
            new_automation_run["reason"] = reason

        if "automation_runs" not in data:
            data["automation_runs"] = []

        data["automation_runs"].append(new_automation_run)
        payload = {
            "status": "success",
            "message": f"New automation run was added: {new_automation_run}",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddAutomationRun",
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
                        },
                    },
                    "required": [
                        "run_id",
                        "run_type",
                        "started_at",
                        "ended_at",
                        "status",
                        "input_ref",
                        "errors_json",
                    ],
                },
            },
        }
