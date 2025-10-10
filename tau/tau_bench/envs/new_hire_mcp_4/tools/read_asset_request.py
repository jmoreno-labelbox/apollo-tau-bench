# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadAssetRequest(Tool):
    @staticmethod
    def invoke(data, **kwargs) -> str:
        rid = kwargs["request_id"]
        row = next((r for r in list(data.get("asset_requests", {}).values()) if r.get("request_id") == rid), None)
        return json.dumps({"asset_request": row} if row else {"error": f"request_id {rid} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{
            "name":"read_asset_request",
            "parameters":{"type":"object","properties":{"request_id":{"type":"string"}}, "required":["request_id"]}
        }}
