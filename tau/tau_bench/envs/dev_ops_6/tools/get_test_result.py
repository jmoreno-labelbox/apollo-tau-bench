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

class GetTestResult(Tool):
    """Fetch a test result by id."""

    @staticmethod
    def invoke(data: Dict[str, Any], id) -> str:
        tid = id
        rows = _table(data, 'test_results')
        row = next((r for r in rows if r.get('id') == tid), None)
        return _ok({'test_result': row}) if row else _err('test_result not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_test_result', 'description': 'Fetch a test result by id.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}}, 'required': ['id']}}}