from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListJobPostings(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role: str) -> str:
        postings = [
            jp
            for jp in data.get("job_postings", {}).values()
            if jp.get("title", "").find(role) != -1
        ]
        payload = {"job_postings": postings}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listJobPostings",
                "description": "List all job postings for a given role.",
                "parameters": {
                    "type": "object",
                    "properties": {"role": {"type": "string"}},
                    "required": ["role"],
                },
            },
        }
