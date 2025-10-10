# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateFixProposal(Tool):
    """Creates a fix proposal for a build run."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        fix_proposals = data.get("fix_proposals", [])
        new_id_num = max([int(p["id"].split("_")[1]) for p in fix_proposals], default=0) + 1
        new_id = f"fix_{new_id_num:03d}"
        
        new_proposal = {
            "id": new_id,
            "build_run_id": kwargs.get("build_run_id"),
            "bisect_result_id": kwargs.get("bisect_result_id"),
            "repo": kwargs.get("repo"),
            "branch": kwargs.get("branch"),
            "created_at": "2025-01-28T00:00:00Z",
            "status": "draft",
            "fix_type": kwargs.get("fix_type"),
            "title": kwargs.get("title"),
            "description": kwargs.get("description"),
        }
        fix_proposals.append(new_proposal)
        return json.dumps(new_proposal)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_fix_proposal",
                "description": "Creates a fix proposal for a build run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "build_run_id": {"type": "string"},
                        "bisect_result_id": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"},
                        "fix_type": {"type": "string"},
                        "title": {"type": "string"},
                        "description": {"type": "string"}
                    },
                    "required": ["build_run_id", "bisect_result_id", "repo", "branch", "fix_type", "title", "description"],
                },
            },
        }
