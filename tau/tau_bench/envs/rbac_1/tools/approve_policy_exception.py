from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ApprovePolicyException(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None, reviewed_by: str = None) -> str:
        for ex in data.get("policy_exceptions", []):
            if ex.get("exception_id") == exception_id:
                ex["status"] = "ACTIVE"
                ex["reviewed_by"] = reviewed_by
                ex["reviewed_on"] = NOW.strftime(DT_STR_FORMAT)
                payload = ex
                out = json.dumps(payload)
                return out
        payload = {"error": "Policy exception not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApprovePolicyException",
                "description": "Approves a pending policy exception.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string"},
                        "reviewed_by": {"type": "string"},
                    },
                    "required": ["exception_id", "reviewed_by"],
                },
            },
        }
