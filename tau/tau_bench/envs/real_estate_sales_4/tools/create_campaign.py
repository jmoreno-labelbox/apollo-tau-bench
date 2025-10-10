# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCampaign(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get('name')
        campaign_type = kwargs.get('type')
        created_by = kwargs.get('created_by')
        
        if not all([name, campaign_type, created_by]):
            return json.dumps({
                "error": "name, type, and created_by are required"
            }, indent=2)
        
        campaign = {
            "campaign_id": 101,
            "name": name,
            "type": campaign_type,
            "created_by": created_by,
            "status": "active",
            "created_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps({
            "success": True,
            "campaign_id": 101,
            "campaign": campaign
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_campaign",
                "description": "Create a marketing campaign for client outreach",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Campaign name"
                        },
                        "type": {
                            "type": "string",
                            "description": "Campaign type (likely_buyer, general_update, etc.)"
                        },
                        "created_by": {
                            "type": "integer",
                            "description": "Broker ID creating the campaign"
                        }
                    },
                    "required": ["name", "type", "created_by"]
                }
            }
        }
