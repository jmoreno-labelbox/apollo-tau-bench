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

class GetSourceChange(Tool):
    """Fetch a source change by commit_sha or id."""

    @staticmethod
    def invoke(data: Dict[str, Any], commit_sha, id) -> str:
        cid = id
        sha = commit_sha
        rows = _table(data, 'source_changes')
        row = next((r for r in rows if cid and r.get('id') == cid or (sha and r.get('commit_sha') == sha)), None)
        return _ok({'source_change': row}) if row else _err('source_change not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_source_change', 'description': 'Fetch a source change by commit_sha (or id).', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'commit_sha': {'type': 'string'}}, 'required': []}}}