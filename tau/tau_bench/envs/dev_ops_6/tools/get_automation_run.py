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

class GetAutomationRun(Tool):
    """Fetch an automation run by id."""

    @staticmethod
    def invoke(data: Dict[str, Any], id) -> str:
        aid = id
        rows = _table(data, 'automation_runs')
        row = next((r for r in rows if r.get('id') == aid), None)
        return _ok({'automation_run': row}) if row else _err('automation_run not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_automation_run', 'description': 'Fetch an automation run by id.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}}, 'required': ['id']}}}