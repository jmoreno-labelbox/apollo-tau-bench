# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso




def _fixed_now_iso():
    return datetime.utcnow().isoformat() + "Z"

class ModifyAssetRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], request_id, updates) -> str:
        updates = updates or {}
        requests = list(data.get("asset_requests", {}).values())
        for r in requests:
            if r.get("request_id") == request_id:
                r.update(updates)
                r["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_request_id": request_id, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_asset_request",
            "description":"Update an asset request.",
            "parameters":{"type":"object","properties":{"request_id":{"type":"string"},"updates":{"type":"object"}},"required":["request_id","updates"]}
        }}