# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFileContentsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get('owner')
        repo = kwargs.get('repo')
        path = kwargs.get('path')
        ref = kwargs.get('ref', 'main') # Default to main branch

        if not all([owner, repo, path]):
            return json.dumps({
                "status": "error",
                "message": "Missing required parameters for get_file_contents.",
                "required": ["owner", "repo", "path"]
            }, indent=2)

        repositories = list(data.get('repositories', {}).values())
        repository = next((r for r in repositories if r['repo_name'] == repo and r['owner'] == owner), None)

        if not repository:
            return json.dumps({
                "status": "error",
                "message": f"Repository '{repo}' not found for owner '{owner}'.",
            }, indent=2)

        if path in repository.get('file_contents', {}):
            return json.dumps({
                "status": "success",
                "content": repository['file_contents'][path],
                "path": path,
                "commit_sha": repository.get('commits', [{}])[-1].get('commit_shas', [''])[0] if repository.get('commits') else ''
            }, indent=2)
        else:
            return json.dumps({
                "status": "error",
                "message": f"File '{path}' not found in repository '{repo}'.",
            }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_file_contents",
                "description": "Gets the content of a file in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "The owner of the repository."},
                        "repo": {"type": "string", "description": "The name of the repository."},
                        "path": {"type": "string", "description": "The path of the file."},
                        "ref": {"type": "string", "description": "The branch or commit SHA to get the file from."}
                    },
                    "required": ["owner", "repo", "path"],
                },
            },
        }
