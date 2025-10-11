# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _table(db: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return db.get(name, [])

def _ok(payload: Dict[str, Any]) -> str:
    return json.dumps({'ok': True, **payload}, indent=2)

def _err(msg: str) -> str:
    return json.dumps({'ok': False, 'error': msg}, indent=2)

class GetOwnershipForPath(Tool):
    """Fetch ownership entry for a given file_path."""

    @staticmethod
    def invoke(data: Dict[str, Any], file_path) -> str:
        path = file_path
        rows = _table(data, 'ownership_map')
        row = next((r for r in rows if r.get('file_path') == path), None)
        return _ok({'ownership': row}) if row else _err('ownership not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_ownership_for_path', 'description': 'Fetch ownership record by file_path.', 'parameters': {'type': 'object', 'properties': {'file_path': {'type': 'string'}}, 'required': ['file_path']}}}