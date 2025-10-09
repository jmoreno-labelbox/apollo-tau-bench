from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateHrWorkflow(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], workflow_id: str, updates: dict[str, Any]) -> str:
        wf = next(
            (
                w
                for w in data.get("hr_workflows", [])
                if w["workflow_id"] == workflow_id
            ),
            None,
        )
        if not wf:
            payload = {"error": "workflow not found"}
            out = json.dumps(payload)
            return out

        if "notes_append" in updates:
            wf["notes"] = wf.get("notes", "") + " " + updates.pop("notes_append")

        wf.update(updates)
        payload = {"success": f"workflow {workflow_id} updated"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateHrWorkflow",
                "description": "Update fields of an existing HR workflow record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "workflow_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["workflow_id", "updates"],
                },
            },
        }
