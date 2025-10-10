# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetJobApplications(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        job_id = kwargs.get("job_id")
        apps = [
            app
            for app in data.get("job_applications", [])
            if app.get("job_id") == job_id
        ]
        return json.dumps(apps, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_job_applications",
                "description": "Returns all applications for a given job ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {
                            "type": "string",
                            "description": "Job ID to fetch applications for",
                        }
                    },
                    "required": ["job_id"],
                },
            },
        }
