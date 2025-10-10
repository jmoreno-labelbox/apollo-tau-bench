# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveAssetRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        requests = list(data.get("asset_requests", {}).values())
        data["asset_requests"] = [r for r in requests if r.get("request_id") != request_id]
        return json.dumps({"removed_request_id": request_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"remove_asset_request",
            "description":"Remove an asset request by ID.",
            "parameters":{"type":"object","properties":{"request_id":{"type":"string"}},"required":["request_id"]}
        }}
