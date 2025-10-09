from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class CreateAssetRequest(Tool):
    """Establish or modify an asset request for a candidate (idempotent based on candidate_id+asset_type)."""

    @staticmethod
    def invoke(
        db: dict[str, Any],
        candidate_id: str,
        asset_type: str,
        status: str = "Requested",
        requested_ts: Any = None
    ) -> str:
        cand_id = candidate_id
        asset_type = asset_type
        status = status
        ts = _fixed_ts(requested_ts)
        reqs = db.setdefault("asset_requests", [])

        row = next(
            (
                r
                for r in reqs
                if r.get("candidate_id") == cand_id
                and r.get("asset_type") == asset_type
            ),
            None,
        )
        if row:
            row["status"] = status
            row["updated_ts"] = ts
            payload = {"request_id": row["request_id"], "status": "updated"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        request_id = _next_seq(reqs, "request_id", "req")
        reqs.append(
            {
                "request_id": request_id,
                "candidate_id": cand_id,
                "asset_type": asset_type,
                "status": status,
                "email_message_id_nullable": None,
                "inventory_checked_flag": False,
                "asset_tag_nullable": None,
                "requested_ts": ts,
                "updated_ts": ts,
            }
        )
        payload = {"request_id": request_id, "status": "created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAssetRequest",
                "description": "Create or update an asset request for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "asset_type": {"type": "string"},
                        "status": {"type": "string"},
                        "requested_ts": {"type": "string"},
                    },
                    "required": ["candidate_id", "asset_type"],
                },
            },
        }
