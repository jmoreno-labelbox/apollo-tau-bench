# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_applications(Tool):
    @staticmethod
    def invoke(data, candidate_id: str) -> str:
        apps = [
            app
            for app in data.get("job_applications", [])
            if app.get("candidate_id") == candidate_id
        ]
        return json.dumps({"applications": apps}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_applications",
                "description": "List all job applications for a given candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }
