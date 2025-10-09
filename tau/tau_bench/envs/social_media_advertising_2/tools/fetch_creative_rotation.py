from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FetchCreativeRotation(Tool):
    """Provide creative rotation records filtered by adset_id or rotation_id from the database snapshot.

    The output rows include: old_ad_id, new_ad_id, rotated_at, rationale.
    If neither adset_id nor rotation_id is supplied, returns 'none'.
    """

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, rotation_id: str = None) -> str:
        if not adset_id and not rotation_id:
            payload = "no rotation"
            out = json.dumps(payload)
            return out

        rows = []
        for r in data.get("creative_rotations", []):
            if rotation_id and str(r.get("rotation_id")) == str(rotation_id):
                rows.append(r)
            elif adset_id and str(r.get("adset_id")) == str(adset_id):
                rows.append(r)

        results = []
        for r in rows:
            results.append(
                {
                    "old_ad_id": r.get("old_ad_id"),
                    "new_ad_id": r.get("new_ad_id"),
                    "rotated_at": r.get("rotated_at") or r.get("date"),
                    "rationale": r.get("rationale"),
                }
            )

        results.sort(
            key=lambda x: (
                x.get("rotated_at") or "",
                str(x.get("old_ad_id") or ""),
                str(x.get("new_ad_id") or ""),
            )
        )
        payload = results
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchCreativeRotation",
                "description": "Fetch creative rotation rows (old_ad_id, new_ad_id, rotated_at, rationale) by adset_id or rotation_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "rotation_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
