# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump


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
