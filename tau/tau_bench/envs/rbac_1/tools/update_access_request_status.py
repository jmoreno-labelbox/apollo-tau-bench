from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateAccessRequestStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, status: str = None, reviewed_by: str = None) -> str:
        for req in data.get("access_requests", {}).values():
            if req.get("request_id") == request_id:
                req["status"] = status
                req["reviewed_by"] = reviewed_by
                req["decision_at"] = NOW.strftime(DT_STR_FORMAT)
                payload = req
                out = json.dumps(payload)
                return out
        payload = {"error": "Access request not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAccessRequestStatus",
                "description": "Updates the status of an access request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "status": {"type": "string"},
                        "reviewed_by": {"type": "string"},
                    },
                    "required": ["request_id", "status", "reviewed_by"],
                },
            },
        }
