# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateBenchAssignment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        start_date = kwargs.get("start_date")
        skills = kwargs.get("skills", [])
        availability = kwargs.get("availability", "immediate")
        preferred_projects = kwargs.get("preferred_projects", [])

        if not all([employee_id, start_date]):
            return json.dumps({"error": "employee_id and start_date are required"})

        bench_resources = data.get("bench_resources", [])
        allocations = data.get("allocations", [])

        employee_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("employee_id") == employee_id
            and alloc.get("status") == "active"
        ]

        from datetime import datetime

        bench_start = datetime.strptime(start_date, "%Y-%m-%d")

        active_allocations_during_bench = []
        for alloc in employee_allocations:
            end_date = alloc.get("end_date")
            if end_date:
                alloc_end = datetime.strptime(end_date, "%Y-%m-%d")
                if alloc_end >= bench_start:
                    active_allocations_during_bench.append(alloc)
            else:

                active_allocations_during_bench.append(alloc)

        total_allocated_hours = sum(
            alloc.get("hours_per_week", 0) for alloc in active_allocations_during_bench
        )
        is_actually_available = total_allocated_hours == 0

        bench_id = f"bench_{uuid.uuid4().hex[:8]}"

        new_assignment = {
            "bench_id": bench_id,
            "employee_id": employee_id,
            "start_date": start_date,
            "skills": skills,
            "availability": availability,
            "preferred_projects": preferred_projects,
            "status": "active",
            "current_allocated_hours": total_allocated_hours,
            "fully_available": is_actually_available,
        }

        bench_resources.append(new_assignment)

        available_resources = len(
            [
                r
                for r in bench_resources
                if r.get("status") == "active" and r.get("fully_available", True)
            ]
        )

        partially_available = len(
            [
                r
                for r in bench_resources
                if r.get("status") == "active" and not r.get("fully_available", True)
            ]
        )

        return json.dumps(
            {
                "success": True,
                "bench_assignment": "created",
                "available_resources": available_resources,
                "partially_available_resources": partially_available,
                "assignment_details": new_assignment,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_bench_assignment",
                "description": "Assign an employee to the bench",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date on bench (YYYY-MM-DD)",
                        },
                        "skills": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee skills",
                        },
                        "availability": {
                            "type": "string",
                            "description": "Availability status",
                        },
                        "preferred_projects": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Preferred project types",
                        },
                    },
                    "required": ["employee_id", "start_date"],
                },
            },
        }
