# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAsset(Tool):
    """Fetch an asset by asset_path or id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get('id')
        apath = kwargs.get('asset_path')
        rows = _table(data, 'asset_catalog')
        row = next((r for r in rows if aid and r.get('id') == aid or (apath and r.get('asset_path') == apath)), None)
        return _ok({'asset': row}) if row else _err('asset not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_asset', 'description': 'Fetch an asset by asset_path (or id).', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'asset_path': {'type': 'string'}}, 'required': []}}}
