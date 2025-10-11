# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

class ResolveOwnerFromMap(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], module_or_path: str) -> str:
        ownership = _get_table(data, "ownership_map")
        # Handle both 'module_or_path' and 'file_path' keys in the dataset; return the corresponding team_id in a consistent manner.
        match = next((o for o in ownership if o.get("module_or_path") == module_or_path or o.get("file_path") == module_or_path), None)
        owner_team = (match or {}).get("owner_team") or (match or {}).get("team_id")
        return json.dumps({"owner_team": owner_team}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "resolve_owner_from_map", "description": "Resolves owner team deterministically from ownership_map.", "parameters": {"type": "object", "properties": {"module_or_path": {"type": "string"}}, "required": ["module_or_path"]}}}