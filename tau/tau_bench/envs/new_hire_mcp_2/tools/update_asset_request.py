from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateAssetRequest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], request_id: str, fields: dict = {}) -> str:
        rows = _ensure_list(data, "asset_requests")
        row = _find_by_key(rows, "request_id", request_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            row.setdefault("updated_ts", NOW_TS)
            payload = {"request_id": request_id, "updated": True, "fields": fields}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"request_id": request_id, "updated": False, "reason": "not_found"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAssetRequest",
                "description": "Update existing asset_requests row. No-op if not found.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "fields": {"type": "object"},
                    },
                    "required": ["request_id", "fields"],
                },
            },
        }
