# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateRepositoryNameTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        target_name = kwargs.get("target_name")
        repo_already_exists = kwargs.get("repo_already_exists")

        if not target_name:
            return json.dumps(
                {
                    "status": "error",
                    "message": "Missing required parameters: 'target_name'.",
                    "required": ["target_name"],
                },
                indent=2,
            )

        if repo_already_exists:
            new_target_name = target_name + "_v2"
            repos = list(data.get('repositories', {}).values())
            repo = next((c for c in repos if c["repo_name"] == new_target_name), None)
            # repo = fetch_data(repos, new_target_name)

            if not repo:
                return json.dumps(
                    {"status": "success", "target_name": new_target_name, "message": "Target repo name updated"},
                    indent=2,
                )
            else:
                # Emulate the logic for verifying documents.
                return json.dumps(
                    {"status": "error", "message": f"New Target repo name {new_target_name} already exists in the database."}, indent=2
                )
        else:
            return json.dumps(
                {"status": "success", "target_name": target_name, "message": "Target repo name unchanged"},
                indent=2,
            )


    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "update_repository_name",
                "description": "Updates the name of the target repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_name": {
                            "type": "string",
                            "description": "Repository name to search in the database.",
                        },
                        "repo_already_exists": {
                            "type": "boolean",
                            "description": "Does the repository already exist in the database?",
                        },
                    },
                    "required": ["target_name", "repo_already_exists"],
                },
            },
        }
