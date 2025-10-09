from tau_bench.envs.tool import Tool
import json
from typing import Any

class EnumerateSuspects(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], failing_sha: str, last_green_sha: str | None = None
    ) -> str:
        _get_table(data, "commits")
        source_changes = _get_table(data, "source_changes")
        ownership = _get_table(data, "ownership_map")
        candidate_refs = [failing_sha]
        if last_green_sha:
            candidate_refs.append(last_green_sha)
        candidate = [c for c in source_changes.values() if c.get("commit_sha") in candidate_refs]
        suspects = []
        for ch in candidate:
            files = ch.get("files_changed") or []
            owners = []
            for f in files:
                owner = next(
                    (
                        o.get("team_id")
                        for o in ownership
                        if o.get("file_path") and str(o.get("file_path")) in str(f)
                    ),
                    None,
                )
                if owner and owner not in owners:
                    owners.append(owner)
            suspects.append(
                {
                    "ref": ch.get("commit_sha"),
                    "author": ch.get("author"),
                    "files": files,
                    "owners": owners,
                }
            )
        payload = {"suspects": suspects}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnumerateSuspects",
                "description": "Enumerates suspect changes deterministically from source_changes and ownership_map.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "failing_sha": {"type": "string"},
                        "last_green_sha": {"type": "string"},
                    },
                    "required": ["failing_sha"],
                },
            },
        }
