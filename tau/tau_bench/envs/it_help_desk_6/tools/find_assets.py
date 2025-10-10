# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindAssets(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        asset_type: Optional[str] = None,
        status: Optional[str] = None,
        model: Optional[str] = None,
        assigned_to: Optional[str] = None,
        mdm_enrolled: Optional[bool] = None,
    ) -> str:
        results = []
        for a in data["it_assets"]:
            if asset_type and a["asset_type"] != asset_type:
                continue
            if status and a["status"] != status:
                continue
            if model and a["model"] != model:
                continue
            if assigned_to is not None and a.get("assigned_to") != assigned_to:
                continue
            if mdm_enrolled is not None and a.get("mdm_enrolled") != mdm_enrolled:
                continue
            results.append(a)
        return json.dumps({"status": "ok", "assets": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_assets",
                "description": "Find assets filtered by type, status, model, owner, or MDM enrolled flag.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_type": {"type": "string"},
                        "status": {"type": "string"},
                        "model": {"type": "string"},
                        "assigned_to": {"type": "string"},
                        "mdm_enrolled": {"type": "boolean"},
                    },
                    "required": [],
                },
            },
        }
