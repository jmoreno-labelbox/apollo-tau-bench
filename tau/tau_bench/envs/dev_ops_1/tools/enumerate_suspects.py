# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EnumerateSuspects(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], failing_sha: str, last_green_sha: Optional[str] = None) -> str:
        commits = _get_table(data, "commits")
        source_changes = _get_table(data, "source_changes")
        ownership = _get_table(data, "ownership_map")
        # Deterministic window: in the absence of last_green_sha, utilize the latest alternative change in the same branch/repo as a substitute.
        candidate_refs = [failing_sha]
        if last_green_sha:
            candidate_refs.append(last_green_sha)
        candidate = [c for c in source_changes if c.get("commit_sha") in candidate_refs]
        suspects = []
        for ch in candidate:
            files = ch.get("files_changed") or []
            owners = []
            for f in files:
                owner = next((o.get("team_id") for o in ownership if o.get("file_path") and str(o.get("file_path")) in str(f)), None)
                if owner and owner not in owners:
                    owners.append(owner)
            suspects.append({"ref": ch.get("commit_sha"), "author": ch.get("author"), "files": files, "owners": owners})
        return json.dumps({"suspects": suspects}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "enumerate_suspects", "description": "Enumerates suspect changes deterministically from source_changes and ownership_map.", "parameters": {"type": "object", "properties": {"failing_sha": {"type": "string"}, "last_green_sha": {"type": "string"}}, "required": ["failing_sha"]}}}
