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

class GetTmsJob(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], id) -> str:
        jid = id
        rows = _table(data, 'tms_jobs')
        row = next((r for r in rows if r.get('id') == jid), None)
        return _ok({'tms_job': row}) if row else _err('tms_job not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_tms_job', 'description': 'Fetch TMS job by id.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}}, 'required': ['id']}}}