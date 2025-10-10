# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBranchProtection(Tool):
    """Gets protection settings for a branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo = _find_repo_record(data, kwargs.get("repo_name"))
        idx = _branch_index(repo, kwargs.get("branch"))
        if "branch_protections" not in repo:
            repo["branch_protections"] = [False] * len(repo.get("branches", []))

        # Initialize if missing
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
