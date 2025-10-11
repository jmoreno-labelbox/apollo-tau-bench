# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_next_id(prefix: str, existing_ids: List[str]) -> str:
    """
    Generates the next sequential ID by finding the max existing ID for a given prefix.
    This is more robust than assuming the list is sorted.
    """
    max_id_num = 0
    for item_id in existing_ids:
        if item_id.startswith(prefix):
            try:
                num_part = int(item_id.split('_')[-1])
                if num_part > max_id_num:
                    max_id_num = num_part
            except (ValueError, IndexError):
                continue

    if max_id_num == 0:
        if not any(s.startswith(prefix) for s in existing_ids):
             return f"{prefix}_001"

    return f"{prefix}_{max_id_num + 1:03d}"

class create_compliance_record(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id: str, compliance_type: str, requirement: str, status: str, details: str, assignee_id: str) -> str:
        compliance_records = data.get("compliance", [])
        existing_ids = [item['id'] for item in compliance_records]
        new_id = _get_next_id("compliance", existing_ids)

        new_record = {
            "id": new_id,
            "project_id": project_id,
            "compliance_type": compliance_type,
            "requirement": requirement,
            "status": status,
            "details": details,
            "due_date": None,
            "assigned_to": assignee_id,
            "created_at": FIXED_TIMESTAMP
        }

        compliance_records.append(new_record)
        data["compliance"] = compliance_records
        return json.dumps({"success": f"Created compliance record '{new_id}'.", "compliance_id": new_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "create_compliance_record", "description": "Creates a new compliance record.", "parameters": { "type": "object", "properties": { "project_id": { "type": "string" }, "compliance_type": { "type": "string" }, "requirement": { "type": "string" }, "status": { "type": "string" }, "details": { "type": "string" }, "assignee_id": { "type": "string" } }, "required": ["project_id", "compliance_type", "requirement", "status", "details", "assignee_id"] } } }