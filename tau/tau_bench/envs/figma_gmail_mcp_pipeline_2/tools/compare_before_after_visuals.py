# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CompareBeforeAfterVisuals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], after_release_id, before_release_id) -> str:
        if not before_release_id or not after_release_id:
            missing = []
            if not before_release_id:
                missing.append("before_release_id")
            if not after_release_id:
                missing.append("after_release_id")
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        release_diffs: List[Dict[str, Any]] = list(data.get("release_diffs", {}).values())
        diff_by_id = {d.get("release_id"): d for d in release_diffs}

        def lineage(rid: str) -> List[str]:
            ids = []
            cur = rid
            seen = set()
            while cur and cur not in seen and cur in diff_by_id:
                ids.append(cur)
                seen.add(cur)
                cur = diff_by_id[cur].get("prior_release_id_nullable")
            ids.reverse()
            return ids

        def artifacts_for_release(rid: str) -> List[str]:
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
            return json.dumps({"error": f"No release_diff for release_id '{before_release_id}'"}, indent=2)
        if after_release_id not in diff_by_id:
            return json.dumps({"error": f"No release_diff for release_id '{after_release_id}'"}, indent=2)

        before_list = artifacts_for_release(before_release_id)
        after_list = set(before_list)
        after_diff = diff_by_id[after_release_id]
        for a in (after_diff.get("frames_removed") or []):
            after_list.discard(a)
        for a in (after_diff.get("frames_added") or []):
            after_list.add(a)
        for a in (after_diff.get("frames_updated") or []):
            after_list.add(a)
        final_after_list = sorted(after_list)

        return json.dumps(
            {
                "before": {"release_id": before_release_id, "artifacts": before_list},
                "after": {"release_id": after_release_id, "artifacts": final_after_list}
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compare_before_after_visuals",
                "description": "Return artifact lists for a before release and an after release, carrying all before artifacts forward unless removed in the after release.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "before_release_id": {"type": "string"},
                        "after_release_id": {"type": "string"}
                    },
                    "required": ["before_release_id", "after_release_id"]
                }
            }
        }
