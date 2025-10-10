# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateResourceRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        skill_required = kwargs.get("skill_required")
        hours_needed = kwargs.get("hours_needed")
        urgency = kwargs.get("urgency", "normal")
        department = kwargs.get("department")

        if not all([project_id, skill_required, hours_needed]):
            return json.dumps(
                {"error": "project_id, skill_required, and hours_needed are required"}
            )

        resource_requests = data.get("resource_requests", [])
        allocations = data.get("allocations", [])
        employees = list(data.get("employees", {}).values())

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

        request_id = kwargs.get("request_id") or f"req_{uuid.uuid4().hex[:8]}"

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

        return json.dumps(
            {
                "success": True,
                "request": new_request,
                "skill_gap_identified": skill_gap_identified,
                "skill_gap_hours": skill_gap_hours,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_resource_request",
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
