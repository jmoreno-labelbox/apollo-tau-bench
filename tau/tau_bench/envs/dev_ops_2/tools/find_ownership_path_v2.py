# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

class FindOwnershipPathV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], contains: str) -> str:
        ownership = _get_table(data, "ownership_map")
        key = (contains or "").lower()
        candidates = [o for o in ownership if key in (o.get("file_path") or "").lower() or key in (o.get("module_or_path") or "").lower()]
        if not candidates:
            return json.dumps({"file_path": None}, indent=2)
        chosen = sorted(candidates, key=lambda x: x.get("id", ""))[0]
        return json.dumps({"file_path": chosen.get("file_path")}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_ownership_path_v2", "description": "Finds an ownership_map file_path containing the given substring (deterministic by id).", "parameters": {"type": "object", "properties": {"contains": {"type": "string"}}, "required": ["contains"]}}}