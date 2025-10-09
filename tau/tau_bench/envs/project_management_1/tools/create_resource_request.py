from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateResourceRequest(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        skill_required: str,
        hours_needed: int,
        urgency: str = "normal",
        department: str = None,
        request_id: str = None
    ) -> str:
        if not all([project_id, skill_required, hours_needed]):
            payload = {"error": "project_id, skill_required, and hours_needed are required"}
            out = json.dumps(payload)
            return out

        resource_requests = data.get("resource_requests", [])
        allocations = data.get("allocations", [])
        employees = data.get("employees", [])

        qualified_employees = []
        for emp in employees:
            if department and emp.get("department") != department:
                continue
            for skill in emp.get("skills", []):
                if skill.get("skill") == skill_required:
                    qualified_employees.append(emp)
                    break

        total_available_hours = 0
        for emp in qualified_employees:
            emp_id = emp.get("employee_id")
            emp_allocations = [
                alloc
                for alloc in allocations
                if alloc.get("employee_id") == emp_id
                and alloc.get("status") == "active"
            ]
            allocated_hours = sum(
                alloc.get("hours_per_week", 0) for alloc in emp_allocations
            )
            available_hours = max(0, 40 - allocated_hours)
            total_available_hours += available_hours

        skill_gap_identified = total_available_hours < hours_needed
        skill_gap_hours = max(0, hours_needed - total_available_hours)

        request_id = request_id or f"req_{uuid.uuid4().hex[:8]}"

        new_request = {
            "request_id": request_id,
            "project_id": project_id,
            "skill_required": skill_required,
            "hours_needed": hours_needed,
            "urgency": urgency,
            "department": department,
            "status": "pending",
            "created_date": datetime.now().isoformat(),
            "assigned_employees": [],
            "allocated_hours": 0,
        }

        resource_requests.append(new_request)
        payload = {
            "success": True,
            "request": new_request,
            "skill_gap_identified": skill_gap_identified,
            "skill_gap_hours": skill_gap_hours,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateResourceRequest",
                "description": "Create a new resource request for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        },
                        "skill_required": {
                            "type": "string",
                            "description": "Required skill",
                        },
                        "hours_needed": {
                            "type": "number",
                            "description": "Hours needed per week",
                        },
                        "urgency": {
                            "type": "string",
                            "description": "Urgency level: normal, urgent",
                        },
                        "department": {
                            "type": "string",
                            "description": "Requesting department",
                        },
                        "request_id": {
                            "type": "string",
                            "description": "Optional custom request ID",
                        },
                    },
                    "required": ["project_id", "skill_required", "hours_needed"],
                },
            },
        }
