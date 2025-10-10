# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSupplierInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get('supplier_id')
        product_id = kwargs.get('product_id')

        if not supplier_id and not product_id:
            return json.dumps({'error': 'Either supplier_id or product_id is required'})

        suppliers = data['suppliers']

        if supplier_id:
            supplier = next((s for s in suppliers if s['supplier_id'] == supplier_id), None)
            if not supplier:
                return json.dumps({'error': 'Supplier not found'})
            return json.dumps(supplier, indent=2)

        if product_id:
            suppliers_for_product = []
            for supplier in suppliers:
                if product_id in supplier['products']:
                    suppliers_for_product.append({
                        'supplier_id': supplier['supplier_id'],
                        'name': supplier['name'],
                        'contact_info': supplier['contact_info']
                    })
            return json.dumps(suppliers_for_product, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_supplier_info',
                'description': 'Get supplier information by supplier ID or find suppliers for a specific product.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'supplier_id': {'type': 'string', 'description': 'Supplier ID to look up'},
                        'product_id': {'type': 'string', 'description': 'Product ID to find suppliers for'}
                    }
                }
            }
        }
