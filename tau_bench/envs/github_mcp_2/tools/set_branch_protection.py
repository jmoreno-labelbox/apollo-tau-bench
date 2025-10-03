from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class SetBranchProtection(Tool):
    """Establishes branch protection rules for a specified branch."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None, protected: bool = None, rules: dict = None) -> str:
        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        protection = protected

        # Set up if absent
        if "branch_protections" not in repo:
            repo["branch_protections"] = [False] * len(repo.get("branches", []))
        repo["branch_protections"][idx] = protection

        # Set up if absent
        if "branch_protection_rules" not in repo:
            repo["branch_protection_rules"] = {}

        repo["branch_protection_rules"][idx] = rules
        payload = {
            "message": (
                "Branch protection enabled."
                if protection
                else "Branch protection disabled."
            ),
            "repo_name": repo["repo_name"],
            "branch": branch,
            "protected": protection if protection else "false",
            "rules": rules,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SetBranchProtection",
                "description": "Sets protection rules for a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "protected": {"type": "string"},
                        "rules": {
                            "type": "object",
                            "description": "Protection rule dictionary",
                        },
                    },
                    "required": ["repo_name", "branch", "rules", "protected"],
                },
            },
        }
