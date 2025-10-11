# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
