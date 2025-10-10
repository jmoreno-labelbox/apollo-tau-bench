# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerTotalBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        if not customer_id:
            return json.dumps({'error': 'customer_id is required'})

        accounts = load_json('accounts.json')
        customer_accounts = [a for a in accounts if a['customer_id'] == customer_id]

        if not customer_accounts:
            return json.dumps({'error': 'No accounts found for this customer.'})

        total_balance = sum(a.get('balance', 0) for a in customer_accounts)

        return json.dumps({
            'customer_id': customer_id,
            'total_balance': total_balance,
            'account_count': len(customer_accounts)
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_customer_total_balance',
                'description': 'Calculates the total balance of a customer across all their accounts.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'The ID of the customer.'}
                    },
                    'required': ['customer_id']
                }
            }
        }
