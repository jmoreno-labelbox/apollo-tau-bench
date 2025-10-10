# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCodeScanningAlertsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner, repo) -> str:

        if not all([owner, repo]):
            return json.dumps({
                "status": "error",
                "message": "Missing required parameters for list_code_scanning_alerts.",
                "required": ["owner", "repo"]
            }, indent=2)

        repositories = list(data.get('repositories', {}).values())
        repository = next((r for r in repositories if r['repo_name'] == repo and r['owner'] == owner), None)

        if not repository:
            return json.dumps({
                "status": "error",
                "message": f"Repository '{repo}' not found for owner '{owner}'.",
            }, indent=2)

        alerts = data.get('code_scanning_alerts', [])
        repo_alerts = [alert for alert in alerts if alert['owner'] == owner and alert['repo_name'] == repo]

        return json.dumps({
            "status": "success",
            "alerts": repo_alerts
        }, indent=2)



    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_code_scanning_alerts",
                "description": "Lists code scanning alerts for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "The owner of the repository."},
                        "repo": {"type": "string", "description": "The name of the repository."}
                    },
                    "required": ["owner", "repo"],
                },
            },
        }
