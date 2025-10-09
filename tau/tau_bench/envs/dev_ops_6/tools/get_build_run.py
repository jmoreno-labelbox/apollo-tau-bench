from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetBuildRun(Tool):
    """Retrieve a build run using id; can optionally filter by commit_sha."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None, commit_sha: str = None) -> str:
        rid = id
        commit = commit_sha
        rows = _table(data, "build_runs")
        row = next(
            (
                r
                for r in rows
                if rid
                and r.get("id") == rid
                or (commit and r.get("commit_sha") == commit)
            ),
            None,
        )
        return _ok({"build_run": row}) if row else _err("build_run not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getBuildRun",
                "description": "Fetch a build run by id (or commit_sha).",
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
