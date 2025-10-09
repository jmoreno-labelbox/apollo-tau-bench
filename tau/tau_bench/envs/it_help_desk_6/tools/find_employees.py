from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindEmployees(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        department: str | None = None,
        job_title: str | None = None,
        status: str | None = None,
        manager_id: str | None = None,
    ) -> str:
        pass
        results = _find_all(
            data["employees"],
            department=department,
            job_title=job_title,
            status=status,
            manager_id=manager_id,
        )
        payload = {"status": "ok", "employees": results}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindEmployees",
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
