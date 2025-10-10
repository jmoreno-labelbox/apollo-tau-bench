from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetJobIdByTitle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], job_title: str) -> str:
        _job_titleL = job_title or ''.lower()
        pass
        postings = data.get("job_postings", {}).values()
        # Utilize a case-insensitive partial match for reliability
        posting = next(
            (p for p in postings.values() if job_title.lower() in p.get("title", "").lower()),
            None,
        )
        if posting:
            payload = {"job_id": posting["job_id"]}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Job posting with title containing '{job_title}' not found"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetJobIdByTitle",
                "description": "Find a job ID by its title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_title": {
                            "type": "string",
                            "description": "The title of the job to find.",
                        }
                    },
                    "required": ["job_title"],
                },
            },
        }
