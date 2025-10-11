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

class GetLocalizationWorkflow(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], id) -> str:
        wid = id
        rows = _table(data, 'localization_workflow')
        row = next((r for r in rows if r.get('id') == wid), None)
        return _ok({'localization_workflow': row}) if row else _err('localization_workflow not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_localization_workflow', 'description': 'Fetch localization_workflow by id.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}}, 'required': ['id']}}}