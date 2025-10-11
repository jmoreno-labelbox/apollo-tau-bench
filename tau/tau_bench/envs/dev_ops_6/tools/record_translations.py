# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _table(db: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return db.get(name, [])

def _ok(payload: Dict[str, Any]) -> str:
    return json.dumps({'ok': True, **payload}, indent=2)

def _loc_table(db: Dict[str, Any]) -> List[Dict[str, Any]]:
    return db.get('loc_strings') or db.get('loc_strongs') or []

class RecordTranslations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], entries = [], reflect_in_loc = True) -> str:
        reflect = bool(reflect_in_loc)
        translations = _table(data, 'translations')
        loc_rows = _loc_table(data)
        ALLOWED = {'loc_string_id', 'string_key', 'locale', 'target_string', 'metadata'}

        added = 0
        for e_in in entries:
            e = {k: v for k, v in e_in.items() if k in ALLOWED}
            eid = f"translation_{len(translations) + 1:04d}"
            e['id'] = eid
            if any(t.get('id') == eid for t in translations):
                continue

            translations.append(e)
            added += 1

            if reflect:
                lsid = e.get('loc_string_id')
                skey = e.get('string_key')
                locale = e.get('locale')
                target = e.get('target_string')
                for row in loc_rows:
                    if (lsid and row.get('id') == lsid) or (skey and row.get('string_key') == skey):
                        row.setdefault('translations', {})
                        loc_entry = row['translations'].setdefault(locale, {})
                        loc_entry['translation'] = target
                        loc_entry['status'] = loc_entry.get('status', 'translated')
                        loc_entry['validation_status'] = loc_entry.get('validation_status', 'pending')
                        if e.get('metadata') is not None:
                            loc_entry['metadata'] = e['metadata']
                        break
        return _ok({'added_count': added})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'record_translations',
                'description': 'Append translation entries and (optionally) reflect into loc_strings. Mirrors per-entry metadata when provided.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'entries': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'loc_string_id': {'type': 'string'},
                                    'string_key': {'type': 'string'},
                                    'locale': {'type': 'string'},
                                    'target_string': {'type': 'string'},
                                    'metadata': {'type': 'object'}
                                },
                                'required': ['locale', 'target_string']
                            }
                        },
                        'reflect_in_loc': {'type': 'boolean'}
                    },
                    'required': ['entries']
                }
            }
        }