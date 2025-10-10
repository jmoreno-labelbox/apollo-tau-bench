# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
