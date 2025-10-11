# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _table(db: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return db.get(name, [])

def _ok(payload: Dict[str, Any]) -> str:
    return json.dumps({'ok': True, **payload}, indent=2)

def _err(msg: str) -> str:
    return json.dumps({'ok': False, 'error': msg}, indent=2)

class CreateLocalizationWorkflow(Tool):
    """Create a localization_workflow record (deterministic; error on duplicate id)."""

    @staticmethod
    def invoke(data: Dict[str, Any], id, pr_number, tms_job_id, bundle_uris = {}, changed_keys = [], locales_processed = [], metadata = {}, overflow_issues = 0, status = 'queued', timestamp = FIXED_TS) -> str:
        table = _table(data, 'localization_workflow')
        wid = id
        # --- ISSUE RESOLUTION: Create ID when none is supplied ---
        if not wid:
            wid = f"loc_workflow_{len(table) + 1:04d}"

        if any((w.get('id') == wid for w in table)):
            return _err(f'localization_workflow id {wid} already exists')
        record = {'id': wid, 'pr_number': pr_number, 'changed_keys': changed_keys, 'locales_processed': locales_processed, 'bundle_uris': bundle_uris, 'overflow_issues': overflow_issues, 'tms_job_id': tms_job_id, 'status': status, 'timestamp': timestamp, 'metadata': metadata}
        table.append(record)
        return _ok({'localization_workflow': record})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'create_localization_workflow', 'description': 'Create a localization_workflow record (deterministic fields).', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'pr_number': {'type': 'integer'}, 'changed_keys': {'type': 'array', 'items': {'type': 'string'}}, 'locales_processed': {'type': 'array', 'items': {'type': 'string'}}, 'bundle_uris': {'type': 'object'}, 'overflow_issues': {'type': 'integer'}, 'tms_job_id': {'type': 'string'}, 'status': {'type': 'string'}, 'timestamp': {'type': 'string'}, 'metadata': {'type': 'object'}}, 'required': ['pr_number', 'changed_keys']}}}