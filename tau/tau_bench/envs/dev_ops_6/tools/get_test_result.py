# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTestResult(Tool):
    """Fetch a test result by id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tid = kwargs.get('id')
        rows = _table(data, 'test_results')
        row = next((r for r in rows if r.get('id') == tid), None)
        return _ok({'test_result': row}) if row else _err('test_result not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_test_result', 'description': 'Fetch a test result by id.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}}, 'required': ['id']}}}
