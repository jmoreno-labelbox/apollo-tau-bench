# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReassignJuniorWork(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], from_employee, hours, project_id, to_employee) -> str:

        params_and_keys = [
            ("from_employee", from_employee),
            ("to_employee", to_employee),
            ("project_id", project_id),
            ("hours", hours)
        ]
        missing_required_params = [key for key, value in params_and_keys if not value]
        if missing_required_params:
            return json.dumps(
                {"error": f"Missing required parameters: {', '.join(missing_required_params)}"}
            )

        allocations: List[Dict] = data.get("allocations", [])
        from_employee_found = False
        to_employee_found = False
        new_allocation = {}
        for i, allocation in enumerate(allocations):
            allocation_employee_id = allocation.get("employee_id")
            allocation_project_id = allocation.get("project_id")
            allocation_info = allocation.get("hours_per_week", 0)
            if allocation_project_id == project_id:
                if allocation_employee_id == from_employee:
                    from_employee_found = True
                    if allocation_info < hours:
                        return json.dumps(
                            {
                                "error": f"The employee {allocation_employee_id} doesn't have enough hours allocated"
                                         f" to transfer for another employee. Hours allocated: {allocation_info}, "
                                         f"Hours to transfer: {hours}."
                            }
                        )
                    new_allocation[i] = {"hours": allocation["hours_per_week"] - hours, "employee_id": from_employee}

                if allocation_employee_id == to_employee:
                    to_employee_found = True
                    new_allocation[i] = {"hours": allocation["hours_per_week"] + hours, "employee_id": to_employee}


        if not from_employee_found:
            return json.dumps(
                {
                    "error": f"The employee {from_employee} doesn't have allocation register "
                             f"in the project {project_id}"
                }
            )
        if not to_employee_found:
            return json.dumps(
                {
                    "error": f"The employee {to_employee} doesn't have allocation register"
                             f" in the project {project_id}"
                }
            )

        for i, allocation_info in new_allocation.items():
            allocations[i]["hours_per_week"] = allocation_info["hours"]
            if allocation_info["hours"] == 0:
                allocations[i]["status"] = "inactive"

        return json.dumps(
            {
                "success": True,
                "reassignment": {
                    "from_employee": from_employee,
                    "to_employee": to_employee,
                    "project_id": project_id,
                    "hours": hours,
                    "status": "completed",
                },
            }
        )


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reassign_junior_work",
                "description": "Reassign work from senior to junior employees",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "from_employee": {
                            "type": "string",
                            "description": "Senior employee ID",
                        },
                        "to_employee": {
                            "type": "string",
                            "description": "Junior employee ID",
                        },
                        "project_id": {"type": "string", "description": "Project ID"},
                        "hours": {"type": "number", "description": "Hours to reassign"},
                    },
                    "required": ["from_employee", "to_employee", "project_id", "hours"],
                },
            },
        }
