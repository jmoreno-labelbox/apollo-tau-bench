from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateAccessRequest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, resource_id: str = None, requested_role_id: str = None, justification: str = None) -> str:
        requests = data.get("access_requests", [])
        new_id_num = max((int(r["request_id"][3:]) for r in requests), default=0) + 1
        new_request_id = f"AR-{new_id_num:03d}"
        new_request = {
            "request_id": new_request_id,
            "user_id": user_id,
            "resource_id": resource_id,
            "requested_role_id": requested_role_id,
            "justification": justification,
            "status": "PENDING",
            "submitted_at": NOW.strftime(DT_STR_FORMAT),
        }
        requests.append(new_request)
        data["access_requests"] = requests
        payload = new_request
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAccessRequest",
                "description": "Creates a new access request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "requested_role_id": {"type": "string"},
                        "justification": {"type": "string"},
                    },
                    "required": ["user_id", "requested_role_id", "justification"],
                },
            },
        }
