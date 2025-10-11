from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os
def _convert_db_to_list(db_data: Any) -> List[Dict]:
    """Convert database data to list of dicts"""
    if isinstance(db_data, list):
        return db_data
    elif isinstance(db_data, dict):
        return [db_data]
    else:
        return []

class ReassignRelationshipManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, relationship_manager_id: str = None) -> str:
        if not customer_id or not relationship_manager_id:
            return json.dumps({'error': 'customer_id and relationship_manager_id are required'})
        customers = load_json('customers.json')
        customers = _convert_db_to_list(customers)
        updated = False
        for c in customers:
            if c['customer_id'] == customer_id:
                if 'bank_relationship' not in c or 'relationship_manager_id' not in c['bank_relationship']:
                    return json.dumps({'error': 'Relationship manager reassignment not supported: no relationship_manager_id field in data.'})
                c['bank_relationship']['relationship_manager_id'] = relationship_manager_id
                updated = True
        if not updated:
            return json.dumps({'error': 'Customer not found or reassignment not supported.'})
        return json.dumps({'success': True, 'customer_id': customer_id, 'relationship_manager_id': relationship_manager_id})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'reassignRelationshipManager',
                'description': 'Updates the assigned relationship manager for a customer (only if field exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'},
                        'relationship_manager_id': {'type': 'string', 'description': 'New Relationship Manager ID'}
                    },
                    'required': ['customer_id', 'relationship_manager_id']
                }
            }
        }