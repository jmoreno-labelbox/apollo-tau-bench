# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ScheduleOpenHouse(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], date, end_time, property_id, start_time) -> str:
        
        if not all([property_id, date, start_time, end_time]):
            return json.dumps({
                "error": "property_id, date, start_time, and end_time are required"
            }, indent=2)
        
        listings = list(list(list(data.get('listings', {}).values())) if isinstance(data.get('listings'), dict) else data.get('listings', []))
        property_exists = any(l.get('property_id') == property_id for l in listings)
        
        if not property_exists:
            return json.dumps({
                "error": f"Property {property_id} not found in listings"
            }, indent=2)
        
        open_house = {
            "property_id": property_id,
            "date": date,
            "start_time": start_time,
            "end_time": end_time,
            "status": "scheduled",
            "created_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps({
            "success": True,
            "message": f"Open house scheduled for property {property_id}",
            "open_house": open_house
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_open_house",
                "description": "Schedule an open house event for a property",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {
                            "type": "string",
                            "description": "Property ID to schedule open house for"
                        },
                        "date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format"
                        },
                        "start_time": {
                            "type": "string",
                            "description": "Start time in HH:MM format"
                        },
                        "end_time": {
                            "type": "string",
                            "description": "End time in HH:MM format"
                        }
                    },
                    "required": ["property_id", "date", "start_time", "end_time"]
                }
            }
        }
