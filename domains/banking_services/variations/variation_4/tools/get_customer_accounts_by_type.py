from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class GetCustomerAccountsByType(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, account_type: str = None) -> str:
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
                'name': 'getCustomerAccountsByType',
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
