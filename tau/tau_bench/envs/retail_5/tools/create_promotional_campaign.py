# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import generate_unique_id


class CreatePromotionalCampaign(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], campaign_name, target_category, discount_percentage = 10) -> str:

        if not campaign_name or not target_category:
            return json.dumps({'error': 'campaign_name and target_category are required'})

        if 'active_campaigns' not in data:
            data['active_campaigns'] = []

        campaign_id = f"CAMP_{generate_unique_id()}"

        new_campaign = {
            'campaign_id': campaign_id,
            'campaign_name': campaign_name,
            'target_category': target_category,
            'discount_percentage': discount_percentage,
            'created_at': get_current_timestamp()
        }

        data['active_campaigns'].append(new_campaign)

        return json.dumps({
            'success': True,
            'campaign_id': campaign_id,
            'message': f"Campaign '{campaign_name}' created and is now active."
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'create_promotional_campaign',
                'description': 'Create and save a promotional campaign for specific product categories.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'campaign_name': {'type': 'string', 'description': 'Name of the promotional campaign'},
                        'target_category': {'type': 'string', 'description': 'Product category to target'},
                        'discount_percentage': {'type': 'number', 'description': 'Discount percentage', 'default': 10}
                    },
                    'required': ['campaign_name', 'target_category']
                }
            }
        }
