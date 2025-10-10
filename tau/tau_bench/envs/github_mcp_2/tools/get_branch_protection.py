# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBranchProtection(Tool):
    """Gets protection settings for a branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], branch, repo_name) -> str:
        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        if "branch_protections" not in repo:
            repo["branch_protections"] = [False] * len(repo.get("branches", []))

        # Set up if not present
        if "branch_protection_rules" not in repo:
            repo["branch_protection_rules"] = {}

        protection = repo.get("branch_protections", [{}])[idx]
        rules = repo.get("branch_protection_rules", {})[idx]

        return json.dumps({"protected": protection if protection else "false",
            "rules": rules}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_branch_protection",
                "description": "Gets branch protection rules for a given branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"}
                    },
                    "required": ["repo_name", "branch"]
                }
            }
        }
