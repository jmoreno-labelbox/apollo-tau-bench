from tau_bench.envs.tool import Tool
import json
from typing import Any

class ProposeAndValidateSubstitutions(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        recipe_id: int,
        household_id: int,
        preserve_section: bool = True,
        require_peanut_free: bool = True,
        prefer_pantry_staples: bool = True
    ) -> str:
        # Initially, suggest deterministic substitutions
        proposed = json.loads(
            ProposeSubstitutionsForRecipe.invoke(
                data,
                recipe_id=recipe_id,
                household_id=household_id,
                preserve_section=preserve_section,
                require_peanut_free=require_peanut_free,
                prefer_pantry_staples=prefer_pantry_staples,
            )
        ).get("substitutions", [])
        # Subsequently, verify those substitutions based on integrity rules
        validated = json.loads(
            ValidateRecipeSubstitutions.invoke(
                data,
                recipe_id=recipe_id,
                household_id=household_id,
                substitutions=proposed,
                require_peanut_free=require_peanut_free,
                preserve_section=preserve_section,
            )
        )
        payload = {
            "valid": bool(validated.get("valid")),
            "validated_substitutions": validated.get("validated_substitutions", []),
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        #Initially, suggest deterministic substitutions
        proposed = json.loads(
            ProposeSubstitutionsForRecipe.invoke(
                data,
                recipe_id=recipe_id,
                household_id=household_id,
                preserve_section=preserve_section,
                require_peanut_free=require_peanut_free,
                prefer_pantry_staples=prefer_pantry_staples,
            )
        ).get("substitutions", [])
        #Subsequently, verify those substitutions based on integrity rules
        validated = json.loads(
            ValidateRecipeSubstitutions.invoke(
                data,
                recipe_id=recipe_id,
                household_id=household_id,
                substitutions=proposed,
                require_peanut_free=require_peanut_free,
                preserve_section=preserve_section,
            )
        )
        payload = {
                "valid": bool(validated.get("valid")),
                "validated_substitutions": validated.get("validated_substitutions", []),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProposeAndValidateSubstitutions",
                "description": "Proposes substitutions for a recipe and validates them in one deterministic step.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {"type": "integer"},
                        "household_id": {"type": "integer"},
                        "preserve_section": {"type": "boolean"},
                        "require_peanut_free": {"type": "boolean"},
                        "prefer_pantry_staples": {"type": "boolean"},
                    },
                    "required": ["recipe_id", "household_id"],
                },
            },
        }
