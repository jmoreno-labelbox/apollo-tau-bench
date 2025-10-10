# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListActiveLoansWithBalances(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        if not customer_id:
            return json.dumps({'error': 'customer_id is required'})
        loans = load_json('loans.json')
        filtered = [l for l in loans if l['customer_id'] == customer_id and l['status'] == 'Active']
        result = [
            {
                'loan_id': l['loan_id'],
                'loan_type': l['loan_type'],
                'current_balance': l['current_balance'],
                'account_id': l['account_id']
            }
            for l in filtered
        ]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'list_active_loans_with_balances',
                'description': 'Returns all active loans and their current outstanding balances.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'}
                    },
                    'required': ['customer_id']
                }
            }
        }
