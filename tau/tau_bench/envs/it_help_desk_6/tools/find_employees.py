# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_all(collection: List[Dict[str, Any]], **filters: Any) -> List[Dict[str, Any]]:
    results = []
    for row in collection:
        ok = True
        for k, v in filters.items():
            if v is None:
                continue
            if isinstance(v, list):
                if row.get(k) not in v:
                    ok = False
                    break
            else:
                if row.get(k) != v:
                    ok = False
                    break
        if ok:
            results.append(row)
    return results

class FindEmployees(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        department: Optional[str] = None,
        job_title: Optional[str] = None,
        status: Optional[str] = None,
        manager_id: Optional[str] = None,
    ) -> str:
        results = _find_all(
            data["employees"],
            department=department,
            job_title=job_title,
            status=status,
            manager_id=manager_id,
        )
        return json.dumps({"status": "ok", "employees": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_employees",
                "description": "Find employees filtered by department, job_title, status, and/or manager_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {"type": "string"},
                        "job_title": {"type": "string"},
                        "status": {"type": "string"},
                        "manager_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }