# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCertification(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], due_date, resource_id, reviewer_id) -> str:
        certifications = data.get('certifications', [])
        new_id_num = max((int(c['certification_id'][2:]) for c in certifications), default=0) + 1
        new_cert_id = f"C-{new_id_num:03d}"
        new_cert = {
                "certification_id": new_cert_id,
                "reviewer_id": reviewer_id,
                "resource_id": resource_id,
                "status": "PENDING",
                "due_date": due_date
        }
        certifications.append(new_cert)
        data['certifications'] = certifications
        return json.dumps(new_cert)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_certification",
                        "description": "Creates a new access certification request.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "reviewer_id": {"type": "string"},
                                        "resource_id": {"type": "string"},
                                        "due_date": {"type": "string", "format": "date-time"}
                                },
                                "required": ["reviewer_id", "resource_id", "due_date"]
                        }
                }
        }
