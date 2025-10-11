# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSupplierContact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], contact_info, email, phone, supplier_id) -> str:

        if not supplier_id:
            return json.dumps({'error': 'supplier_id is required'})

        suppliers = data['suppliers']
        supplier = next((s for s in suppliers if s['supplier_id'] == supplier_id), None)

        if not supplier:
            return json.dumps({'error': f'Supplier {supplier_id} not found'})

        if contact_info:
            old_contact = supplier['contact_info'].copy()
            supplier['contact_info'] = contact_info
        else:
            if not phone and not email:
                return json.dumps({'error': 'At least one of phone or email is required'})
            old_contact = supplier['contact_info'].copy()

            if phone:
                supplier['contact_info']['phone'] = phone
            if email:
                supplier['contact_info']['email'] = email

        return json.dumps({
            'success': True,
            'supplier_id': supplier_id,
            'old_contact': old_contact,
            'new_contact': supplier['contact_info'],
            'updated_at': get_current_timestamp()
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'update_supplier_contact',
                'description': 'Update contact information for a supplier.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'supplier_id': {'type': 'string', 'description': 'Supplier ID to update'},
                        'phone': {'type': 'string', 'description': 'New phone number'},
                        'email': {'type': 'string', 'description': 'New email address'},
                        'contact_info': {
                            'type': 'object',
                            'description': 'Complete contact information object',
                            'properties': {
                                'phone': {'type': 'string', 'description': 'Phone number'},
                                'email': {'type': 'string', 'description': 'Email address'}
                            }
                        }
                    },
                    'required': ['supplier_id']
                }
            }
        }
