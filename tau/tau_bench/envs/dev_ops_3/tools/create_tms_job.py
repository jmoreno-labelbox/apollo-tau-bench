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

class create_tms_job(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id: str, job_name: str, source_locale: str, target_locales: List[str], string_keys: List[str]) -> str:
        tms_jobs = data.get("tms_jobs", [])
        existing_ids = [job['id'] for job in tms_jobs]
        new_id = _get_next_id("tms_job", existing_ids)

        new_job = {
            "id": new_id,
            "tms_project_id": project_id,
            "job_name": job_name,
            "job_type": "translation",
            "status": "pending",
            "created_at": FIXED_TIMESTAMP,
            "started_at": None,
            "completed_at": None,
            "total_segments": len(string_keys) * len(target_locales),
            "completed_segments": 0,
            "assigned_translators": [],
            "assigned_reviewers": [],
            "source_locale": source_locale,
            "target_locales": target_locales,
            "priority": "medium",
            "due_date": None,
            "metadata": { "string_keys": string_keys }
        }

        tms_jobs.append(new_job)
        data["tms_jobs"] = tms_jobs
        return json.dumps({"success": f"Created TMS job '{new_id}'.", "tms_job_id": new_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "create_tms_job", "description": "Creates a new job in the Translation Management System (TMS).", "parameters": { "type": "object", "properties": { "project_id": { "type": "string" }, "job_name": { "type": "string" }, "source_locale": { "type": "string" }, "target_locales": { "type": "array", "items": { "type": "string" } }, "string_keys": { "type": "array", "items": { "type": "string" } } }, "required": ["project_id", "job_name", "source_locale", "target_locales", "string_keys"] } } }