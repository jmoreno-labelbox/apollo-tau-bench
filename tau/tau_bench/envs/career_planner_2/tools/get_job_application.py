from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetJobApplication(Tool):
    """Retrieve a job application record using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], application_id: str = None) -> str:
        aid = application_id
        for a in data.get("job_applications", {}).values():
            if a.get("application_id") == aid:
                payload = a
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Application not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetJobApplication",
                "description": "Get job application.",
                "parameters": {
                    "type": "object",
                    "properties": {"application_id": {"type": "string"}},
                    "required": ["application_id"],
                },
            },
        }
