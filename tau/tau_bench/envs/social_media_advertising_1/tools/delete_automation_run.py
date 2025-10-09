from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class DeleteAutomationRun(Tool):
    """Removes a record of an automation run."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None) -> str:
        if not run_id:
            payload = {"error": "run_id is a required parameter."}
            out = json.dumps(payload)
            return out

        runs = data.get("automation_runs", [])
        original_count = len(runs)
        data["automation_runs"] = [r for r in runs if r.get("run_id") != run_id]

        if len(data["automation_runs"]) < original_count:
            payload = {
                    "status": "success",
                    "message": f"Automation run with id {run_id} deleted successfully.",
                }
            out = json.dumps(
                payload)
            return out
        else:
            payload = {"error": f"Automation run with ID '{run_id}' not found."}
            out = json.dumps(
                payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteAutomationRun",
                "description": "Deletes an automation run record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {
                            "type": "string",
                            "description": "The unique ID of the automation run to delete.",
                        },
                    },
                    "required": ["run_id"],
                },
            },
        }
