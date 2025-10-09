from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetReleaseDiffSummaryTool(Tool):
    """Summarize a release difference: counts of added, updated, and removed frames."""

    @staticmethod
    def invoke(data: dict[str, Any], release_id: str = None) -> str:
        release_id = _require_str(release_id, "release_id")
        if not release_id:
            payload = {"error": "release_id is required"}
            out = json.dumps(payload)
            return out

        diffs = data.get("release_diffs", {}).values()
        adds = updates = removes = 0
        for d in diffs.values():
            if d.get("release_id") != release_id:
                continue
            t = d.get("change_type")
            if t == "ADDED":
                adds += 1
            elif t == "UPDATED":
                updates += 1
            elif t == "REMOVED":
                removes += 1
        payload = {
                "release_id": release_id,
                "added": adds,
                "updated": updates,
                "removed": removes,
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
                "name": "GetReleaseDiffSummary",
                "description": "Return counts of ADDED/UPDATED/REMOVED items for a release.",
                "parameters": {
                    "type": "object",
                    "properties": {"release_id": {"type": "string"}},
                    "required": ["release_id"],
                },
            },
        }
