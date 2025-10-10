# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAssetRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        fields = kwargs.get("fields", {})
        rows = _ensure_list(data, "asset_requests")
        row = _find_by_key(rows, "request_id", request_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"request_id": request_id, "updated": True, "fields": fields}, indent=2)
        return json.dumps({"request_id": request_id, "updated": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_asset_request",
                                                 "description": "Update existing asset_requests row. No-op if not found.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"request_id": {"type": "string"},
                                                                               "fields": {"type": "object"}},
                                                                "required": ["request_id", "fields"]}}}
