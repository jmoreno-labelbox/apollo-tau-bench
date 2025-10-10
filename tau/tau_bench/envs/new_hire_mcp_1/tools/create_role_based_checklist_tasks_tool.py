# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateRoleBasedChecklistTasksTool(Tool):
    """Inserts multiple checklist_items records based on the roles of one or more candidates."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        candidate_ids = kwargs.get("candidate_ids")

        ids_to_process = []
        if candidate_ids:
            ids_to_process.extend(candidate_ids)
        if candidate_id:
            ids_to_process.append(candidate_id)

        if not ids_to_process:
            return _err("candidate_id or candidate_ids is required.")

        candidates_map = {str(c.get("candidate_id")): c for c in data.get("candidates", [])}
        checklist_items = data.setdefault("checklist_items", [])
        all_created_tasks = []

        for cid in ids_to_process:
            candidate = candidates_map.get(cid)
            if not candidate:
                if len(ids_to_process) == 1:
                    return _err(f"Candidate '{cid}' not found.", code="not_found")
                continue

            start_date_str = candidate.get("start_date")
            if not start_date_str:
                if len(ids_to_process) == 1:
                    return _err("Candidate start_date is required for due date calculation.")
                continue

            start_date = datetime.fromisoformat(start_date_str)
            role_title = candidate.get("role_title", "").replace(" ", "")

            task_list = ROLE_CHECKLIST_MAP.get(role_title, [])
            if not task_list:
                for key, value in ROLE_CHECKLIST_MAP.items():
                    if role_title.lower() in key.lower().replace(" ", ""):
                        task_list = value
                        break

            if not task_list:
                if len(ids_to_process) == 1:
                    return _err(f"No task template found for role '{candidate.get('role_title', '')}'.")
                continue

            created_tasks = []
            for task in task_list:
                due_date = start_date + timedelta(days=task["due_days"])
                new_task = {
                    "item_id": _next_str_id(checklist_items, "item_id", "ITEM-"),
                    "candidate_id": cid,
                    "task_name": task["task_name"],
                    "status": "Pending",
                    "due_date": due_date.strftime("%Y-%m-%d"),
                    "created_ts": HARD_TS,
                    "updated_ts": HARD_TS,
                    "reminder_sent_flag": False,
                    "reminder_email_message_id_nullable": None
                }
                checklist_items.append(new_task)
                created_tasks.append(new_task)
            all_created_tasks.extend(created_tasks)

        return json.dumps(all_created_tasks, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_role_based_checklist_tasks",
                "description": "Inserts multiple checklist_items records based on the roles of one or more candidates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "A single target candidate identifier."},
                        "candidate_ids": {"type": "array", "items": {"type": "string"}, "description": "A list of target candidate identifiers."}
                    },
                },
            },
        }
