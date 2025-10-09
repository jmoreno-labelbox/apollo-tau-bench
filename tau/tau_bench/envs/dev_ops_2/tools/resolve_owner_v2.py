from tau_bench.envs.tool import Tool
import json
from typing import Any

class ResolveOwnerV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], module_or_path: str) -> str:
        pass
        ownership = _get_table(data, "ownership_map")
        match = next(
            (
                o
                for o in ownership
                if o.get("module_or_path") == module_or_path
                or o.get("file_path") == module_or_path
            ),
            None,
        )
        owner_team = (match or {}).get("owner_team") or (match or {}).get("team_id")
        payload = {"owner_team": owner_team}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ResolveOwnerV2",
                "description": "Resolves owner team deterministically from ownership_map.",
                "parameters": {
                    "type": "object",
                    "properties": {"module_or_path": {"type": "string"}},
                    "required": ["module_or_path"],
                },
            },
        }
