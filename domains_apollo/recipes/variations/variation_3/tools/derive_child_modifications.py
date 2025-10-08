from tau_bench.envs.tool import Tool
import json
from typing import Any

class DeriveChildModifications(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipe_ids: list[int], ruleset: str) -> str:
        pass
        # Deterministic notes suitable for children
        recipes = _get_table(data, "recipes")
        by_id = {r.get("recipe_id"): r for r in recipes}
        notes = {}
        for rid in recipe_ids or []:
            r = by_id.get(rid)
            base = (r or {}).get("notes") or ""
            note = "Child: low spice, small pieces"
            if "kid" in (base or "").lower() or "child" in (base or "").lower():
                note = base
            notes[str(rid)] = note
        payload = {"child_notes": notes}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deriveChildModifications",
                "description": "Returns a map of recipe_id -> child-friendly note deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "ruleset": {"type": "string"},
                    },
                    "required": ["recipe_ids", "ruleset"],
                },
            },
        }
