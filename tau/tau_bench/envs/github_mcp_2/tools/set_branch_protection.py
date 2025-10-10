# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetBranchProtection(Tool):
    """Sets branch protection rules for a given branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo = _find_repo_record(data, kwargs.get("repo_name"))
        idx = _branch_index(repo, kwargs.get("branch"))
        protection = kwargs.get("protected")
        rules = kwargs.get("rules")

        # Set up if not present
        if "branch_protections" not in repo:
            repo["branch_protections"] = [False] * len(repo.get("branches", []))
        repo["branch_protections"][idx] = protection

        # Set up if not present
        if "branch_protection_rules" not in repo:
            repo["branch_protection_rules"] = {}

        repo["branch_protection_rules"][idx] = rules
        return json.dumps({
            "message": "Branch protection enabled." if protection else "Branch protection disabled.",
            "repo_name": repo["repo_name"],
            "branch": kwargs.get("branch"),
            "protected": protection if protection else "false",
            "rules": rules
        }, indent=2)


    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_branch_protection",
                "description": "Sets protection rules for a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "protected": {"type": "string"},
                        "rules": {"type": "object", "description": "Protection rule dictionary"}
                    },
                    "required": ["repo_name", "branch", "rules", "protected"]
                }
            }
        }
