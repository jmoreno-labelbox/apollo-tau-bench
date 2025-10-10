# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_job_postings(Tool):
    @staticmethod
    def invoke(data, role: str) -> str:
        postings = [
            jp
            for jp in data.get("job_postings", [])
            if jp.get("title", "").find(role) != -1
        ]
        return json.dumps({"job_postings": postings}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_job_postings",
                "description": "List all job postings for a given role.",
                "parameters": {
                    "type": "object",
                    "properties": {"role": {"type": "string"}},
                    "required": ["role"],
                },
            },
        }
