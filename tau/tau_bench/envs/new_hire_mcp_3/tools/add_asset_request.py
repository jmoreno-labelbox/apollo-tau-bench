# Copyright Sierra

import requests
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddAssetRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], request) -> str:
        new_request = request or {}
        requests = list(data.get("asset_requests", {}).values())
        requests.append(new_request)
        data["asset_requests"] = requests
        return json.dumps({"added_request": new_request}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_asset_request",
            "description":"Add a new asset request.",
            "parameters":{"type":"object","properties":{"request":{"type":"object"}},"required":["request"]}
        }}
