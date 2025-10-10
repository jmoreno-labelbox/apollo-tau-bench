# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateResource(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resources = data.get('resources', [])
        new_id_num = max((int(r['resource_id'][4:]) for r in resources), default=0) + 1
        new_resource_id = f"RES-{new_id_num:03d}"
        new_resource = {
                "resource_id": new_resource_id,
                "name": kwargs.get("name"),
                "owner_id": kwargs.get("owner_id"),
                "criticality": kwargs.get("criticality"),
                "compliance_scope": kwargs.get("compliance_scope")
        }
        resources.append(new_resource)
        data['resources'] = resources
        return json.dumps(new_resource)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_resource",
                        "description": "Creates a new resource.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "name": {"type": "string"},
                                        "owner_id": {"type": "string"},
                                        "criticality": {"type": "string"},
                                        "compliance_scope": {"type": "string"}
                                },
                                "required": ["name", "owner_id", "criticality"]
                        }
                }
        }
