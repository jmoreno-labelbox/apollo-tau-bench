from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class run_git_bisect(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], failing_commit_sha: str, last_known_good_commit_sha: str
    ) -> str:
        pass
        bisect_results = data.get("bisect_results", [])
        for result in bisect_results:
            if (
                result.get("first_bad_commit") == failing_commit_sha
                and result.get("last_good_commit") == last_known_good_commit_sha
            ):
                payload = result
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Bisect result not found for the given commit range."}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RunGitBisect",
                "description": "Performs a git bisect to find the commit that introduced a failure.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "failing_commit_sha": {"type": "string"},
                        "last_known_good_commit_sha": {"type": "string"},
                    },
                    "required": ["failing_commit_sha", "last_known_good_commit_sha"],
                },
            },
        }
