# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateChildModifications(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], recipe_ids: List[int]) -> str:
        notes: Dict[str, str] = {}
        for rid in recipe_ids or []:
            base = (_recipe_by_id(data, int(rid)) or {}).get("notes") or ""
            add = " Child-friendly: mild seasoning; cut to bite-size; soft textures."
            notes[str(int(rid))] = (str(base) + add).strip()
            # Guarantee deterministic write: stamp recipe row with fixed generated-at marker
            rrow = _recipe_by_id(data, int(rid))
            if rrow is not None:
                rrow["child_mod_last_generated_at"] = "2025-01-01T00:00:00"
        return json.dumps({"child_mod_notes": notes})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_child_modifications",
                "description": "Create deterministic child-friendly notes per recipe_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_ids": {"type": "array", "items": {"type": "integer"}}},
                    "required": ["recipe_ids"],
                },
            },
        }
