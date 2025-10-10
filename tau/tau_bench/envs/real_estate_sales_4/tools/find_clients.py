# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindClients(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], client_id, name = '') -> str:
        clients = data.get('client_preferences', [])
        if not clients:
            return json.dumps({"error": "No client data available"}, indent=2)
        
        results = []
        name_query = name.lower()
        
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
                "name": "find_clients",
                "description": "Find clients by name or ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Client name to find for (partial match)"
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
