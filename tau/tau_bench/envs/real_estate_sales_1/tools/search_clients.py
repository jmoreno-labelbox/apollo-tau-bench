# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchClients(Tool):
    """Search for clients by name or other criteria."""
    
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        clients = list(data.get('client_preferences', {}).values())
        if not clients:
            return json.dumps({"error": "No client data available"}, indent=2)
        
        results = []
        name_query = kwargs.get('name', '').lower()
        client_id = kwargs.get('client_id')
        
        for client in clients:
            if client_id and client.get('client_id') != client_id:
                continue
            if name_query and name_query not in client.get('name', '').lower():
                continue
            
            results.append(client)
        
        return json.dumps(results, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_clients",
                "description": "Search for clients by name or ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Client name to search for (partial match)"
                        },
                        "client_id": {
                            "type": "string",
                            "description": "Specific client ID"
                        }
                    },
                    "required": []
                }
            }
        }
