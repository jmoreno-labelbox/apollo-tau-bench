from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetSourceChange(Tool):
    """Retrieve a source change using commit_sha or id."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None, commit_sha: str = None) -> str:
        rows = _table(data, "source_changes")
        row = next(
            (
                r
                for r in rows
                if id and r.get("id") == id or (commit_sha and r.get("commit_sha") == commit_sha)
            ),
            None,
        )
        return _ok({"source_change": row}) if row else _err("source_change not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getSourceChange",
                "description": "Fetch a source change by commit_sha (or id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "commit_sha": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
