from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class ListRecentTransactionsByCategory(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        account_ids: list = None,
        group_by: str = 'merchant_name',
        limit: int = 10
    ) -> str:
        if not account_ids:
            return json.dumps({'error': 'account_ids is required'})
        transactions = load_json('transactions.json')
        filtered = [t for t in transactions if t['account_id'] in account_ids]
        filtered.sort(key=lambda t: t['transaction_date'], reverse=True)
        filtered = filtered[:limit]
        grouped = {}
        for t in filtered:
            key = t.get(group_by) or 'Unknown'
            grouped.setdefault(key, []).append(t)
        return json.dumps(grouped, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'listRecentTransactionsByCategory',
                'description': 'Lists recent transactions grouped by merchant or spending category.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_ids': {'type': 'array', 'items': {'type': 'string'}, 'description': 'List of account IDs'},
                        'group_by': {'type': 'string', 'description': 'Group by merchant_name or transaction_type', 'default': 'merchant_name'},
                        'limit': {'type': 'integer', 'description': 'Number of recent transactions to consider', 'default': 10}
                    },
                    'required': ['account_ids']
                }
            }
        }
