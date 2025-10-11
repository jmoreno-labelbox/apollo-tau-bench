# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _fixed_ts(ts: Optional[str]) -> str:
    return ts or "2025-09-01T00:00:00Z"

class AllocateFirstAvailableAsset(Tool):
    @staticmethod
    def invoke(db: Dict[str, Any], request_id, updated_ts) -> str:
        rid = request_id
        req = next((r for r in db.get("asset_requests", []) if r.get("request_id") == rid), None)
        if not req:
            return json.dumps({"error": f"request_id {rid} not found"}, indent=2)
        cand_id = req.get("candidate_id"); a_type = req.get("asset_type")
        inv = db.get("inventory_assets", [])
        def is_free(row):
            st = (row.get("status") or "").lower()
            return (row.get("asset_type") == a_type) and (row.get("assigned_candidate_id_nullable") in (None, "")) and (st in ("available","avail","free"))
        free = sorted([r for r in inv if is_free(r)], key=lambda r: (r.get("asset_tag") or ""))
        if not free:
            return json.dumps({"request_id": rid, "candidate_id": cand_id, "asset_type": a_type, "asset_tag": None, "status": "none_available"}, indent=2)
        chosen = free[0]
        chosen["assigned_candidate_id_nullable"] = cand_id
        chosen["status"] = "allocated"
        for c in db.get("candidates", []):
            if c.get("candidate_id") == cand_id:
                c["allocated_asset_tag_nullable"] = chosen.get("asset_tag")
                break
        req["updated_ts"] = _fixed_ts(updated_ts)
        return json.dumps({
            "request_id": rid,
            "candidate_id": cand_id,
            "asset_type": a_type,
            "asset_tag": chosen.get("asset_tag"),
            "status": "allocated"
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"allocate_first_available_asset",
            "description":"Allocate the first available inventory asset for an existing request_id, and mirror the tag onto the candidate.",
            "parameters":{"type":"object","properties":{"request_id":{"type":"string"}, "updated_ts":{"type":"string"}}, "required":["request_id"]}
        }}