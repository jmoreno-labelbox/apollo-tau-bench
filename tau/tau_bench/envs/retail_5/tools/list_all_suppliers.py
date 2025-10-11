# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAllSuppliers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        suppliers = data['suppliers']

        # Provide fundamental supplier details excluding comprehensive inventory data.
        supplier_list = []
        for supplier in suppliers:
            supplier_list.append({
                'supplier_id': supplier['supplier_id'],
                'name': supplier['name'],
                'contact_info': supplier['contact_info'],
                'total_products': len(supplier['products'])
            })

        return json.dumps(supplier_list, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'list_all_suppliers',
                'description': 'Get a list of all suppliers with basic information.',
                'parameters': {
                    'type': 'object',
                    'properties': {}
                }
            }
        }
