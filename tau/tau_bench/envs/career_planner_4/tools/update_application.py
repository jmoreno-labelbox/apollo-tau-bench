from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateApplication(Tool):
    @staticmethod
    def invoke(data, candidate_id: str, application_id: str, updates: dict) -> str:
        updated = False
        for app in data.get("job_applications", []):
            if (
                app.get("application_id") == application_id
                and app.get("candidate_id") == candidate_id
            ):
                app.update(updates)
                updated = True
        if updated:
            payload = {
                    "success": f"Application {application_id} updated for candidate {candidate_id}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {"error": "Application not found"}
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateApplication",
                "description": "Update an external job application record with new details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "application_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["candidate_id", "application_id", "updates"],
                },
            },
        }
