# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerAccountsByType(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        account_type = kwargs.get('account_type')
        if not customer_id or not account_type:
            return json.dumps({'error': 'customer_id and account_type are required'})
        accounts = load_json('accounts.json')
        filtered = [a for a in accounts if a['customer_id'] == customer_id and a['account_type'].lower() == account_type.lower()]
        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_customer_accounts_by_type',
                'description': 'Returns a customer\'s accounts filtered by account type (e.g., "Savings").',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'},
                        'account_type': {'type': 'string', 'description': 'Account type (e.g., Savings, Checking, Credit Card, etc.)'}
                    },
                    'required': ['customer_id', 'account_type']
                }
            }
        }
