# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LicenseRequiresRenewal(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], num_days) -> str:
        if num_days is None:
            return json.dumps({'status': 'error', 'reason': 'The num_days field is required.'}, indent=2)

        inventory = data.get('license_inventory')
        licenses = []

        dt_now = datetime.fromisoformat(FIXED_NOW)

        for license in inventory:
            dt_audit = datetime.fromisoformat(license['last_audit_at'])
            if (dt_now - dt_audit).days > num_days:
                licenses.append(license['license_id'])

        return json.dumps(licenses, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'license_requires_renewal',
                'description': 'Returns the license_id of any license audited over num_days ago.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'num_days': {'type': 'string', 'description': 'The number of days to filter by.'},
                    },
                    'required': ['num_days']
                }
            }
        }
