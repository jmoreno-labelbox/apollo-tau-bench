# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateBranchTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get('owner')
        repo = kwargs.get('repo')
        new_branch_name = kwargs.get('branch_name')
        sha = kwargs.get('sha')

        if not all([owner, repo, new_branch_name, sha]):
            return json.dumps({
                "status": "error",
                "message": "Missing required parameters for create_branch.",
                "required": ["owner", "repo", "branch_name", "sha"]
            }, indent=2)

        repositories = list(data.get('repositories', {}).values())
        repository = next((r for r in repositories if r['repo_name'] == repo and r['owner'] == owner), None)

        if not repository:
            return json.dumps({
                "status": "error",
                "message": f"Repository '{repo}' not found for owner '{owner}'.",
            }, indent=2)

        # Simulate creating a branch
        repository.setdefault('branches', []).append({
            "name": new_branch_name,
            "commit_sha": sha
        })
        repository.setdefault('branch_files', []).append([]) # Add empty file list for new branch
        repository.setdefault('branch_contents', []).append([]) # Add empty contents list

        return json.dumps({
            "status": "success",
            "message": f"Branch '{new_branch_name}' created successfully.",
            "ref": f"refs/heads/{new_branch_name}"
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_branch",
                "description": "Creates a new branch in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "The owner of the repository."},
                        "repo": {"type": "string", "description": "The name of the repository."},
                        "branch_name": {"type": "string", "description": "The name of the new branch."},
                        "sha": {"type": "string", "description": "The SHA of the commit to branch from."}
                    },
                    "required": ["owner", "repo", "branch_name", "sha"],
                },
            },
        }
