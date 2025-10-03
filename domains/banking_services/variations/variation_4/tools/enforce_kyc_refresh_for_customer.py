from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class EnforceKYCRefreshForCustomer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({'error': 'customer_id is required'})

        customers = load_json('customers.json')
        updated = False

        for c in customers:
            if c['customer_id'] == customer_id:
                # Ensure 'compliance' dict exists
                compliance = c.setdefault('compliance', {})
                # Always set 'kyc_status' to 'Refresh Required'
                compliance['kyc_status'] = 'Refresh Required'
                updated = True
                break

        if not updated:
            return json.dumps({'error': 'Customer not found or KYC enforcement not supported.'})

        return json.dumps({
            'success': True,
            'customer_id': customer_id,
            'new_kyc_status': 'Refresh Required'
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'enforceKycRefreshForCustomer',
                'description': 'Sets kyc_status to "Refresh Required" for a given customer.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {
                            'type': 'string',
                            'description': 'Customer ID'
                        }
                    },
                    'required': ['customer_id']
                }
            }
        }
