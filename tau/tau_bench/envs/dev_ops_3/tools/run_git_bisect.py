# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class run_git_bisect(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], failing_commit_sha: str, last_known_good_commit_sha: str) -> str:
        bisect_results = data.get("bisect_results", [])
        for result in bisect_results:
            if result.get("first_bad_commit") == failing_commit_sha and result.get("last_good_commit") == last_known_good_commit_sha:
                return json.dumps(result, indent=2)
        return json.dumps({"error": "Bisect result not found for the given commit range."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "run_git_bisect", "description": "Performs a git bisect to find the commit that introduced a failure.", "parameters": { "type": "object", "properties": { "failing_commit_sha": { "type": "string" }, "last_known_good_commit_sha": { "type": "string" } }, "required": ["failing_commit_sha", "last_known_good_commit_sha"] } } }
