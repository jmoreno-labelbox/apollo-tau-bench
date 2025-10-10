# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_application(Tool):
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
            return json.dumps(
                {
                    "success": f"Application {application_id} updated for candidate {candidate_id}"
                },
                indent=2,
            )
        else:
            return json.dumps({"error": "Application not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "update_application",
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
