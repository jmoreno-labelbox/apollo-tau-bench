# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAssetRequest(Tool):
    """Create or update an asset request for a candidate (idempotent by candidate_id+asset_type)."""
    @staticmethod
    def invoke(db: Dict[str, Any], asset_type, candidate_id, requested_ts, status = "Requested") -> str:
        cand_id = candidate_id
        ts = _fixed_ts(requested_ts)
        reqs = db.setdefault("asset_requests", [])

        row = next((r for r in reqs if r.get("candidate_id") == cand_id and r.get("asset_type") == asset_type), None)
        if row:
            row["status"] = status
            row["updated_ts"] = ts
            return json.dumps({"request_id": row["request_id"], "status": "updated"}, indent=2)

        request_id = _next_seq(reqs, "request_id", "req")
        reqs.append({
            "request_id": request_id,
            "candidate_id": cand_id,
            "asset_type": asset_type,
            "status": status,
            "email_message_id_nullable": None,
            "inventory_checked_flag": False,
            "asset_tag_nullable": None,
            "requested_ts": ts,
            "updated_ts": ts
        })
        return json.dumps({"request_id": request_id, "status": "created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_asset_request",
                "description": "Create or update an asset request for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "asset_type": {"type": "string"},
                        "status": {"type": "string"},
                        "requested_ts": {"type": "string"}
                    },
                    "required": ["candidate_id", "asset_type"]
                }
            }
        }
