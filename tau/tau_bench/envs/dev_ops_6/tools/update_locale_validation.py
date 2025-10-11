# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _ok(payload: Dict[str, Any]) -> str:
    return json.dumps({'ok': True, **payload}, indent=2)

def _loc_table(db: Dict[str, Any]) -> List[Dict[str, Any]]:
    return db.get('loc_strings') or db.get('loc_strongs') or []

def _err(msg: str) -> str:
    return json.dumps({'ok': False, 'error': msg}, indent=2)

class UpdateLocaleValidation(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], loc_string_id, locale, metadata, string_key, validation_error, validation_status) -> str:
        new_status = validation_status
        loc_rows = _loc_table(data)
        target_row: Optional[Dict[str, Any]] = None
        for row in loc_rows:
            if loc_string_id and row.get('id') == loc_string_id or (string_key and row.get('string_key') == string_key):
                target_row = row
                break
        if not target_row:
            return _err('loc string not found')
        target_row.setdefault('translations', {})
        entry = target_row['translations'].setdefault(locale, {})
        if new_status is not None:
            entry['validation_status'] = new_status
        if validation_error is not None:
            entry['validation_error'] = validation_error
        if metadata is not None:
            entry['metadata'] = metadata
        return _ok({'updated': {'string_key': target_row.get('string_key'), 'locale': locale, 'validation_status': new_status, 'validation_error': validation_error}})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'update_locale_validation', 'description': 'Update locale validation and mirror into translations. Optionally attach CI/linkage metadata.', 'parameters': {'type': 'object', 'properties': {'loc_string_id': {'type': 'string'}, 'string_key': {'type': 'string'}, 'locale': {'type': 'string'}, 'validation_status': {'type': 'string'}, 'validation_error': {'type': 'string'}, 'metadata': {'type': 'object'}}, 'required': ['locale']}}}