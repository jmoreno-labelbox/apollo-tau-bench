from tau_bench.envs.tool import Tool
import json
from typing import Any

class GenerateChildModifications(Tool):
    """Provide notes for each recipe_id regarding child-friendly modifications (mild spice, bite-sized)."""

    @staticmethod
    def invoke(data: dict[str, Any], recipe_ids_json: str = "[]") -> str:
        ids = _parse_json_list_ids(recipe_ids_json)
        notes: dict[str, str] = {}
        for rid in ids:
            base = (_recipe_by_id(data, rid) or {}).get("notes") or ""
            add = " Child-friendly: mild seasoning; cut to bite-size; soft textures."
            notes[str(rid)] = (str(base) + add).strip()
        return _json_dump({"child_mod_notes": notes})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateChildModifications",
                "description": "Create deterministic child-friendly notes for recipes.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_ids_json": {"type": "string"}},
                    "required": ["recipe_ids_json"],
                },
            },
        }
