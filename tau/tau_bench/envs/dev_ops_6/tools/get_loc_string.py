# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _loc_table(db: Dict[str, Any]) -> List[Dict[str, Any]]:
    return db.get('loc_strings') or db.get('loc_strongs') or []

def _err(msg: str) -> str:
    return json.dumps({'ok': False, 'error': msg}, indent=2)

class GetLocString(Tool):
    """Fetch a localization string row by string_key; optionally include a locale entry."""

    @staticmethod
    def invoke(data: Dict[str, Any], locale, string_key) -> str:
        rows = _loc_table(data)
        for row in rows:
            if row.get('string_key') == string_key:
                if locale:
                    entry = (row.get('translations') or {}).get(locale)
                    return json.dumps({'loc_string': row, 'locale_entry': entry}, indent=2)
                return json.dumps({'loc_string': row}, indent=2)
        return _err(f'string_key not found: {string_key}')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_loc_string', 'description': 'Fetch a loc string by string_key (optionally include a single-locale view).', 'parameters': {'type': 'object', 'properties': {'string_key': {'type': 'string'}, 'locale': {'type': 'string'}}, 'required': ['string_key']}}}