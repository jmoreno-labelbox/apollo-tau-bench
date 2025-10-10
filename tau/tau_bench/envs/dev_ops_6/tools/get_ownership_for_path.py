# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOwnershipForPath(Tool):
    """Fetch ownership entry for a given file_path."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        path = kwargs.get('file_path')
        rows = _table(data, 'ownership_map')
        row = next((r for r in rows if r.get('file_path') == path), None)
        return _ok({'ownership': row}) if row else _err('ownership not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_ownership_for_path', 'description': 'Fetch ownership record by file_path.', 'parameters': {'type': 'object', 'properties': {'file_path': {'type': 'string'}}, 'required': ['file_path']}}}
