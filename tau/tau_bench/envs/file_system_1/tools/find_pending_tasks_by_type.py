# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindPendingTasksByType(Tool):
    """Finds all pending tasks of a specified type (e.g., 'archive', 'file_check')."""
    @staticmethod
    def invoke(data: Dict[str, Any], task_type) -> str:
        pending_tasks = []
        if task_type == 'archive':
            db = data.get('archive_instructions', [])
            pending_tasks = [t for t in db if t.get('status') == 'pending']
        elif task_type == 'file_check':
            db = data.get('file_check_db', [])
            pending_tasks = [t for t in db if not t.get('completed')]
        elif task_type == 'file_organization':
            db = data.get('file_lists', [])
            op_ids = {f['operation_id'] for f in db if f.get('status') == 'pending'}
            all_ops = data.get('directories', [])
            pending_tasks = [op for op in all_ops if op['operation_id'] in op_ids]

        return json.dumps({"pending_tasks": pending_tasks, "count": len(pending_tasks)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_pending_tasks_by_type", "description": "Scans the databases for all tasks of a specific type that are in a 'pending' state.", "parameters": {"type": "object", "properties": {"task_type": {"type": "string", "enum": ["archive", "file_check", "file_organization"]}}, "required": ["task_type"]}}}
