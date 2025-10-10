# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePullRequestTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get('owner')
        repo = kwargs.get('repo')
        title = kwargs.get('title')
        body = kwargs.get('body')
        head_branch = kwargs.get('head')
        base_branch = kwargs.get('base', 'main') # Default base branch to 'main'

        if not all([owner, repo, title, body, head_branch, base_branch]):
            return json.dumps({
                "status": "error",
                "message": "Missing required parameters for create_pull_request.",
                "required": ["owner", "repo", "title", "body", "head", "base"]
            }, indent=2)

        repositories = list(data.get('repositories', {}).values())
        repository = next((r for r in repositories if r['repo_name'] == repo and r['owner'] == owner), None)

        if not repository:
            return json.dumps({
                "status": "error",
                "message": f"Repository '{repo}' not found for owner '{owner}'.",
            }, indent=2)

        # Simulate creating a pull request
        pr_number = len(repository.get('pull_requests', [])) + 1
        repository.setdefault('pull_requests', []).append({
            "pr_number": pr_number,
            "owner": owner,
            "repo_name": repo,
            "pr_titles": [title],
            "pr_bodies": [body],
            "pr_states": ["open"],
            "head_branches": [head_branch],
            "base_branches": [base_branch],
            "head_shas": [""], # Placeholder for SHA
            "mergeable_flags": [True],
            "merged_flags": [False],
            "pr_files": [], # This will be populated by get_pull_request_files later
            "pr_comments": [],
            "pr_comment_users": [],
            "reviewers": [],
            "review_states": [],
            "review_events": [],
            "created_ts": [datetime.now(timezone.utc).isoformat()],
            "updated_ts": [datetime.now(timezone.utc).isoformat()]
        })

        return json.dumps({
            "status": "success",
            "message": f"Pull request #{pr_number} created successfully.",
            "pr_number": pr_number
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_pull_request",
                "description": "Creates a pull request from a head branch to a base branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "The owner of the repository."},
                        "repo": {"type": "string", "description": "The name of the repository."},
                        "title": {"type": "string", "description": "The title of the pull request."},
                        "body": {"type": "string", "description": "The body/description of the pull request."},
                        "head": {"type": "string", "description": "The name of the branch where your changes are implemented."},
                        "base": {"type": "string", "description": "The name of the branch you want your changes pulled into."}
                    },
                    "required": ["owner", "repo", "title", "body", "head", "base"],
                },
            },
        }
