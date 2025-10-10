# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchCodeTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner, query, repo) -> str:

        if not all([owner, repo, query]):
            return json.dumps({
                "status": "error",
                "message": "Missing required parameters for search_code.",
                "required": ["owner", "repo", "query"]
            }, indent=2)

        repositories = list(data.get('repositories', {}).values())
        repository = next((r for r in repositories if r['repo_name'] == repo and r['owner'] == owner), None)

        if not repository:
            return json.dumps({
                "status": "error",
                "message": f"Repository '{repo}' not found for owner '{owner}'.",
            }, indent=2)

        # Locate code by examining file content.
        found_occurrences = []
        for file_path, file_content in zip(repository.get('file_paths', {}), repository.get('file_contents', {})):
            if query in file_content:
                # The code segment includes the keyword.
                found_occurrences.append({
                    "path": file_path,
                    "line": file_content.count(query), # A basic method to show availability
                    "match": query
                })

        return json.dumps({
            "status": "success",
            "query": query,
            "occurrences": found_occurrences
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_code",
                "description": "Searches for code patterns within the files of a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "The owner of the repository."},
                        "repo": {"type": "string", "description": "The name of the repository."},
                        "query": {"type": "string", "description": "The code pattern to search for."}
                    },
                    "required": ["owner", "repo", "query"],
                },
            },
        }
