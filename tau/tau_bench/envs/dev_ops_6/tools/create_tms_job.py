# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateTmsJob(Tool):
    """Create a minimal TMS job entry (deterministic; error on duplicate id)."""

    @staticmethod
    def invoke(data: Dict[str, Any], due_date, id, assigned_reviewers = [], assigned_translators = [], created_at = FIXED_TS, job_name = f'tms_job_{jid}', job_type = 'translation', metadata = {}, priority = 'medium', source_locale = 'en', target_locales = [], tms_project_id = 'proj_001', total_segments = 0) -> str:
        jobs = _table(data, 'tms_jobs')
        jid = id
        if not jid:
            jid = f"tms_job_{len(jobs) + 1:04d}"
        
        if any((j.get('id') == jid for j in jobs)):
            return _err(f'TMS job id {jid} already exists')
        job = {'id': jid, 'tms_project_id': tms_project_id, 'job_name': job_name, 'job_type': job_type, 'status': 'queued', 'created_at': created_at, 'started_at': None, 'completed_at': None, 'total_segments': total_segments, 'completed_segments': 0, 'assigned_translators': assigned_translators, 'assigned_reviewers': assigned_reviewers, 'source_locale': source_locale, 'target_locales': target_locales, 'priority': priority, 'due_date': due_date, 'metadata': metadata}
        jobs.append(job)
        return _ok({'tms_job': job})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'create_tms_job', 'description': 'Create a queued TMS job with deterministic fields.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'tms_project_id': {'type': 'string'}, 'job_name': {'type': 'string'}, 'job_type': {'type': 'string'}, 'source_locale': {'type': 'string'}, 'target_locales': {'type': 'array', 'items': {'type': 'string'}}, 'priority': {'type': 'string'}, 'due_date': {'type': 'string'}, 'total_segments': {'type': 'integer'}, 'assigned_translators': {'type': 'array', 'items': {'type': 'string'}}, 'assigned_reviewers': {'type': 'array', 'items': {'type': 'string'}}, 'metadata': {'type': 'object'}}, 'required': ['source_locale', 'target_locales']}}}
