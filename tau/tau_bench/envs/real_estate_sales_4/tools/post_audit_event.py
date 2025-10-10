# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PostAuditEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], action, actor_id, entity_id, entity_type, metadata_json) -> str:
        
        if not all([actor_id, action, entity_type, entity_id]):
            return json.dumps({
                "error": "actor_id, action, entity_type, and entity_id are required"
            }, indent=2)
        
        audit_event = {
            "audit_id": 501,
            "actor_id": actor_id,
            "action": action,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "metadata": metadata_json,
            "timestamp": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps({
            "success": True,
            "audit_id": 501,
            "message": f"Audit event recorded: {action}",
            "audit_event": audit_event
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "post_audit_event",
                "description": "Record an audit event for tracking system actions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {
                            "type": "integer",
                            "description": "ID of the user performing the action"
                        },
                        "action": {
                            "type": "string",
                            "description": "Action being performed"
                        },
                        "entity_type": {
                            "type": "string",
                            "description": "Type of entity being acted upon"
                        },
                        "entity_id": {
                            "type": "integer",
                            "description": "ID of the entity being acted upon"
                        },
                        "metadata_json": {
                            "type": "object",
                            "description": "Additional metadata about the action"
                        }
                    },
                    "required": ["actor_id", "action", "entity_type", "entity_id"]
                }
            }
        }
