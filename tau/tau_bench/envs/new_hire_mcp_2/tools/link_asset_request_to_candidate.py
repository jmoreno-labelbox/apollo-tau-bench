# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _find_by_key(rows: List[Dict[str, Any]], key: str, val: Any) -> Dict[str, Any]:
    for r in rows:
        if r.get(key) == val:
            return r
    return None

def _ensure_list(d: Dict[str, Any], key: str) -> List[Any]:
    if key not in d or not isinstance(d[key], list):
        d[key] = []
    return d[key]

class LinkAssetRequestToCandidate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, request_id) -> str:
        crows = _ensure_list(data, "candidates")
        cand = _find_by_key(crows, "candidate_id", candidate_id)
        if cand:
            cand["asset_request_record_id_nullable"] = request_id
            cand.setdefault("updated_ts", NOW_TS)
            return json.dumps({"candidate_id": candidate_id, "linked_request_id": request_id}, indent=2)
        return json.dumps(
            {"candidate_id": candidate_id, "linked_request_id": request_id, "updated": False, "reason": "not_found"},
            indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "link_asset_request_to_candidate",
                                                 "description": "Set candidate.asset_request_record_id_nullable.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"candidate_id": {"type": "string"},
                                                                               "request_id": {"type": "string"}},
                                                                "required": ["candidate_id", "request_id"]}}}