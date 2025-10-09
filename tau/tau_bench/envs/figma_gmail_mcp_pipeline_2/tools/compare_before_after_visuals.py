from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CompareBeforeAfterVisuals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], before_release_id: str = None, after_release_id: str = None) -> str:
        if not before_release_id or not after_release_id:
            missing = []
            if not before_release_id:
                missing.append("before_release_id")
            if not after_release_id:
                missing.append("after_release_id")
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        release_diffs: list[dict[str, Any]] = data.get("release_diffs", [])
        diff_by_id = {d.get("release_id"): d for d in release_diffs}

        def lineage(rid: str) -> list[str]:
            ids = []
            cur = rid
            seen = set()
            while cur and cur not in seen and cur in diff_by_id:
                ids.append(cur)
                seen.add(cur)
                cur = diff_by_id[cur].get("prior_release_id_nullable")
            ids.reverse()
            return ids

        def artifacts_for_release(rid: str) -> list[str]:
            if rid not in diff_by_id:
                return []
            s = set()
            for lr in lineage(rid):
                d = diff_by_id.get(lr, {})
                for a in d.get("frames_added") or []:
                    s.add(a)
                for u in d.get("frames_updated") or []:
                    s.add(u)
                for r in d.get("frames_removed") or []:
                    if r in s:
                        s.remove(r)
            return sorted(s)

        if before_release_id not in diff_by_id:
            payload = {"error": f"No release_diff for release_id '{before_release_id}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        if after_release_id not in diff_by_id:
            payload = {"error": f"No release_diff for release_id '{after_release_id}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        before_list = artifacts_for_release(before_release_id)
        after_list = set(before_list)
        after_diff = diff_by_id[after_release_id]
        for a in after_diff.get("frames_removed") or []:
            after_list.discard(a)
        for a in after_diff.get("frames_added") or []:
            after_list.add(a)
        for a in after_diff.get("frames_updated") or []:
            after_list.add(a)
        final_after_list = sorted(after_list)
        payload = {
                "before": {"release_id": before_release_id, "artifacts": before_list},
                "after": {
                    "release_id": after_release_id,
                    "artifacts": final_after_list,
                },
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
                "name": "compareBeforeAfterVisuals",
                "description": "Return artifact lists for a before release and an after release, carrying all before artifacts forward unless removed in the after release.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "before_release_id": {"type": "string"},
                        "after_release_id": {"type": "string"},
                    },
                    "required": ["before_release_id", "after_release_id"],
                },
            },
        }
