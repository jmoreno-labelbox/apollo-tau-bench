# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetJobLicenses(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        job_title = kwargs.get('job_title')

        if job_title is None:
            return json.dumps({'status': 'error', 'reason': 'The job_title parameter is required.'}, indent=2)

        group_data = data.get('rbac_group_map')

        for group in group_data:
            if group['job_title'] == job_title:
                return json.dumps(group['default_license_bundle'], indent=2)
        return json.dumps({'status': 'error', 'reason': 'Unable to find specified job_title.'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_job_licenses',
                'description': 'Gets all default licenses for a specific job title.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'job_title': {'type': 'string', 'description': 'The name of the job.'},
                    },
                    'required': ['job_title']
                }
            }
        }
