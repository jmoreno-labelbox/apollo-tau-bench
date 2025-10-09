from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RemoveAssetRequest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None) -> str:
        requests = data.get("asset_requests", [])
        data["asset_requests"] = [
            r for r in requests if r.get("request_id") != request_id
        ]
        payload = {"removed_request_id": request_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeAssetRequest",
                "description": "Remove an asset request by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"request_id": {"type": "string"}},
                    "required": ["request_id"],
                },
            },
        }
