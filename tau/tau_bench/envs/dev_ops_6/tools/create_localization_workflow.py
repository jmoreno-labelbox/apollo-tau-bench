# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateLocalizationWorkflow(Tool):
    """Create a localization_workflow record (deterministic; error on duplicate id)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        table = _table(data, 'localization_workflow')
        wid = kwargs.get('id')
        # --- ISSUE RESOLUTION: Create ID when none is supplied ---
        if not wid:
            wid = f"loc_workflow_{len(table) + 1:04d}"

        if any((w.get('id') == wid for w in table)):
            return _err(f'localization_workflow id {wid} already exists')
        record = {'id': wid, 'pr_number': kwargs.get('pr_number'), 'changed_keys': kwargs.get('changed_keys', []), 'locales_processed': kwargs.get('locales_processed', []), 'bundle_uris': kwargs.get('bundle_uris', {}), 'overflow_issues': kwargs.get('overflow_issues', 0), 'tms_job_id': kwargs.get('tms_job_id'), 'status': kwargs.get('status', 'queued'), 'timestamp': kwargs.get('timestamp', FIXED_TS), 'metadata': kwargs.get('metadata', {})}
        table.append(record)
        return _ok({'localization_workflow': record})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'create_localization_workflow', 'description': 'Create a localization_workflow record (deterministic fields).', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'pr_number': {'type': 'integer'}, 'changed_keys': {'type': 'array', 'items': {'type': 'string'}}, 'locales_processed': {'type': 'array', 'items': {'type': 'string'}}, 'bundle_uris': {'type': 'object'}, 'overflow_issues': {'type': 'integer'}, 'tms_job_id': {'type': 'string'}, 'status': {'type': 'string'}, 'timestamp': {'type': 'string'}, 'metadata': {'type': 'object'}}, 'required': ['pr_number', 'changed_keys']}}}
