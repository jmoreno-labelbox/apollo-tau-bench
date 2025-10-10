# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateApplicationStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        app_id = kwargs.get("application_id")
        new_status = kwargs.get("new_status")
        for app in data.get("job_applications", []):
            if app["application_id"] == app_id:
                app["status"] = new_status
                app["last_updated"] = datetime.now().isoformat()
                return f"{app_id} {new_status}"
        return "Application not found"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_application_status",
                "description": "Updates the status of a job application.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "application_id": {
                            "type": "string",
                            "description": "Application to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status label",
                        },
                    },
                    "required": ["application_id", "new_status"],
                },
            },
        }
