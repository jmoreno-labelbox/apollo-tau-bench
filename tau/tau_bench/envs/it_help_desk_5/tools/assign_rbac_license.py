# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignRBACLicense(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        license_id = kwargs.get('license_id')
        job_title = kwargs.get('job_title')

        if license_id is None or job_title is None:
            return json.dumps({'status': 'error', 'description': 'The license_id and job_title fields are required.'}, indent=2)

        group_map = data.get('rbac_group_map')

        for group in group_map:
            if group['job_title'] == job_title:
                group['default_license_bundle'].append(license_id)

                return json.dumps(group['default_license_bundle'])
        return json.dumps({'status': 'error', 'description': 'The job title could not be found with an rbac group association.'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'assign_rbac_license',
                'description': 'Assigns a license to be default in the rbac_group_map for a job_title.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'license_id': {'type': 'string', 'description': 'The id of the license to add.'},
                        'job_title': {'type': 'string', 'description': 'The job title to assign the license to.'}
                    },
                    'required': ['license_id', 'job_title']
                }
            }
        }
