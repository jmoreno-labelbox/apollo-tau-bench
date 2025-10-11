# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump








def _recipe_by_id(data: Dict[str, Any], recipe_id: int) -> Optional[Dict[str, Any]]:
    return next((r for r in data.get("recipes", []) if int(r.get("recipe_id")) == recipe_id), None)

def _parse_json_list_ids(json_str: str) -> List[int]:
    try:
        arr = json.loads(json_str)
        if isinstance(arr, list):
            return [int(x) for x in arr]
    except Exception:
        pass
    return []

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

class GenerateChildModifications(Tool):
    """Return note per recipe_id for child-friendly changes (mild spice, bite-size)."""
    @staticmethod
    def invoke(data: Dict[str, Any], recipe_ids_json = "[]") -> str:
        ids = _parse_json_list_ids(recipe_ids_json)
        notes: Dict[str, str] = {}
        for rid in ids:
            base = (_recipe_by_id(data, rid) or {}).get("notes") or ""
            add = " Child-friendly: mild seasoning; cut to bite-size; soft textures."
            notes[str(rid)] = (str(base) + add).strip()
        return _json_dump({"child_mod_notes": notes})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"generate_child_modifications",
            "description":"Create deterministic child-friendly notes for recipes.",
            "parameters":{"type":"object","properties":{"recipe_ids_json":{"type":"string"}},"required":["recipe_ids_json"]}
        }}