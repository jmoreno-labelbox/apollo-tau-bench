from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateWorkflowStage(Tool):
    """Revise the status of the HR workflow stage."""

    @staticmethod
    def invoke(data: dict[str, Any], workflow_id: str = None, stage: str = None, status: str = None) -> str:
        wid = workflow_id
        stg = stage
        st = status
        for wf in data.get("hr_workflows", []):
            if wf.get("workflow_id") == wid:
                for s in wf.get("workflow_stages", []):
                    if s.get("stage") == stg:
                        s["status"] = st
                        s["date"] = datetime.utcnow().date().isoformat()
                        payload = {"success": f"{stg} -> {st}"}
                        out = json.dumps(payload, indent=2)
                        return out
        payload = {"error": "Not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateWorkflowStage",
                "description": "Update stage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "workflow_id": {"type": "string"},
                        "stage": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["workflow_id", "stage", "status"],
                },
            },
        }
