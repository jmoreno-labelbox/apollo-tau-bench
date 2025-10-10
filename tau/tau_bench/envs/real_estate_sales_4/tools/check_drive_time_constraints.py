# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckDriveTimeConstraints(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_ids = kwargs.get('property_ids')
        max_minutes = kwargs.get('max_minutes', 30)
        
        if not property_ids:
            return json.dumps({
                "error": "property_ids is required"
            }, indent=2)
        
        feasible = len(property_ids) <= 4
        
        result = {
            "feasible": feasible,
            "property_count": len(property_ids),
            "max_minutes_per_hop": max_minutes,
            "estimated_total_time": len(property_ids) * 25,
            "properties_checked": property_ids
        }
        
        return json.dumps(result, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_drive_time_constraints",
                "description": "Check if properties can be visited within time constraints",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of property IDs to check"
                        },
                        "max_minutes": {
                            "type": "integer",
                            "description": "Maximum minutes allowed between stops"
                        }
                    },
                    "required": ["property_ids"]
                }
            }
        }
