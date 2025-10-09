from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindAssets(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_type: str | None = None,
        status: str | None = None,
        model: str | None = None,
        assigned_to: str | None = None,
        mdm_enrolled: bool | None = None,
    ) -> str:
        results = []
        for a in data["it_assets"].values():
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
        payload = {"status": "ok", "assets": results}
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAssets",
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
