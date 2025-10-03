from tau_bench.envs.tool import Tool
import json
from typing import Any

class LinkAssetRequestToCandidate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, request_id: str = None) -> str:
        crows = _ensure_list(data, "candidates")
        cand = _find_by_key(crows, "candidate_id", candidate_id)
        if cand:
            cand["asset_request_record_id_nullable"] = request_id
            cand.setdefault("updated_ts", NOW_TS)
            payload = {"candidate_id": candidate_id, "linked_request_id": request_id}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {
                "candidate_id": candidate_id,
                "linked_request_id": request_id,
                "updated": False,
                "reason": "not_found",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkAssetRequestToCandidate",
                "description": "Set candidate.asset_request_record_id_nullable.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["candidate_id", "request_id"],
                },
            },
        }
