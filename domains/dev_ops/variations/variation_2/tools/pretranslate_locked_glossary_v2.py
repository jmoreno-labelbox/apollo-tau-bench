from tau_bench.envs.tool import Tool
import json
from typing import Any

class PretranslateLockedGlossaryV2(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        locales: list[str],
        keys: list[str],
        glossary_lock: bool = True,
        context_uris: dict[str, str] | None = None,
    ) -> str:
        pass
        #Consistent stub: log pretranslation intent with stable output URIs for each locale
        localization_workflow = _get_table(data, "localization_workflow")
        outputs: dict[str, Any] = {
            "locales": locales,
            "keys": keys,
            "glossary_lock": glossary_lock,
            "context_uris": context_uris or {},
            "pretranslate_uris": {},
        }
        for loc in locales:
            uri = f"artifact://pretranslate/{loc}-{len(keys)}"
            outputs["pretranslate_uris"][loc] = uri
            localization_workflow.append(
                {
                    "step": "pretranslate",
                    "locale": loc,
                    "keys": keys,
                    "uri": uri,
                    "glossary_lock": glossary_lock,
                    "context_uris": context_uris or {},
                }
            )
        payload = outputs
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PretranslateLockedGlossaryV2",
                "description": "Pre-translate keys with locked glossary and capture context URIs; returns deterministic URIs per locale.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "locales": {"type": "array", "items": {"type": "string"}},
                        "keys": {"type": "array", "items": {"type": "string"}},
                        "glossary_lock": {"type": "boolean"},
                        "context_uris": {"type": "object"},
                    },
                    "required": ["locales", "keys"],
                },
            },
        }
