# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateApplicationStatus(Tool):
    """Set a new status on a job application."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("application_id")
        st = kwargs.get("status")
        for a in data.get("job_applications", []):
            if a.get("application_id") == aid:
                a["status"] = st
                a["last_updated"] = datetime.utcnow().date().isoformat()
                return json.dumps({"success": f"{aid} status {st}"}, indent=2)
        return json.dumps({"error": "Application not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_application_status",
                "description": "Update app status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "application_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["application_id", "status"],
                },
            },
        }
