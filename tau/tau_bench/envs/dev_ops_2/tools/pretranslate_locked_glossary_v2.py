# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PretranslateLockedGlossaryV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], locales: List[str], keys: List[str], glossary_lock: bool = True, context_uris: Optional[Dict[str, str]] = None) -> str:
        # Deterministic stub: record pretranslation intent with stable output URIs per locale
        localization_workflow = _get_table(data, "localization_workflow")
        outputs: Dict[str, Any] = {"locales": locales, "keys": keys, "glossary_lock": glossary_lock, "context_uris": context_uris or {}, "pretranslate_uris": {}}
        for loc in locales:
            uri = f"artifact://pretranslate/{loc}-{len(keys)}"
            outputs["pretranslate_uris"][loc] = uri
            localization_workflow.append({"step": "pretranslate", "locale": loc, "keys": keys, "uri": uri, "glossary_lock": glossary_lock, "context_uris": context_uris or {}})
        return json.dumps(outputs, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "pretranslate_locked_glossary_v2", "description": "Pre-translate keys with locked glossary and capture context URIs; returns deterministic URIs per locale.", "parameters": {"type": "object", "properties": {"locales": {"type": "array", "items": {"type": "string"}}, "keys": {"type": "array", "items": {"type": "string"}}, "glossary_lock": {"type": "boolean"}, "context_uris": {"type": "object"}}, "required": ["locales", "keys"]}}}
