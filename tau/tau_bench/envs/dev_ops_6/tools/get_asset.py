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

class GetAsset(Tool):
    """Fetch an asset by asset_path or id."""

    @staticmethod
    def invoke(data: Dict[str, Any], asset_path, id) -> str:
        aid = id
        apath = asset_path
        rows = _table(data, 'asset_catalog')
        row = next((r for r in rows if aid and r.get('id') == aid or (apath and r.get('asset_path') == apath)), None)
        return _ok({'asset': row}) if row else _err('asset not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_asset', 'description': 'Fetch an asset by asset_path (or id).', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'asset_path': {'type': 'string'}}, 'required': []}}}