import json
import uuid
from datetime import datetime
from typing import Any, Dict, List

from domains.dto import Tool


class SearchEmployees(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        required_skills = kwargs.get("skills")
        min_skill_matches = kwargs.get("min_skill_matches", 1)
        department = kwargs.get("department")
        role = kwargs.get("role")
        role_contains = kwargs.get("role_contains")
        role_disregard = kwargs.get("role_disregard")
        clearance = kwargs.get("clearance")
        utilization_below = kwargs.get("utilization_below")
        utilization_above = kwargs.get("utilization_above")
        min_proficiency = kwargs.get("min_proficiency", 0)
        min_available_hours = kwargs.get("min_available_hours")
        disregard_employees = kwargs.get("disregard_employee_ids", [])


        employees = data.get("employees", [])
        results = []

        for employee in employees:

            if name and name.lower() not in employee.get("name", "").lower():
                continue

            if department and employee.get("department") != department:
                continue

            if role and employee.get("role") != role:
                continue

            if employee.get("employee_id") in disregard_employees:
                continue

            if (
                role_contains
                and role_contains.lower() not in employee.get("role", "").lower()
            ):
                continue

            if (
                role_disregard
                and role_disregard.lower() in employee.get("role", "").lower()
            ):
                continue

            if clearance and employee.get("clearance") != clearance:
                continue

            if required_skills:
                employee_skills = employee.get("skills", [])
                skills_matches = {
                    info["skill"] for info in employee_skills
                    if info["skill"] in required_skills and info.get("proficiency", 0) >= min_proficiency
                }
                if len(skills_matches) < min_skill_matches:
                    continue

            if utilization_below:
                current_util = employee.get("current_utilization", 0)
                if current_util > utilization_below:
                    continue

            if utilization_above is not None:
                current_util = employee.get("current_utilization", 0)
                if current_util <= utilization_above:
                    continue

            if min_available_hours:
                available_hours = (employee.get("max_hours_per_week", 0) *
                                   (100 - employee.get("current_utilization", 0)) / 100)
                if available_hours < min_available_hours:
                    continue

            results.append(employee)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_employees",
                "description": "Search for employees by name, skill, department, role, security clearance, or utilization levels",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Employee name to search for",
                        },
                        "skill": {
                            "type": "string",
                            "description": "Skill name to filter by",
                        },
                        "department": {
                            "type": "string",
                            "description": "Department to filter by",
                        },
                        "role": {
                            "type": "string",
                            "description": "Exact role to filter by",
                        },
                        "role_contains": {
                            "type": "string",
                            "description": "Partial role match",
                        },
                        "clearance": {
                            "type": "string",
                            "description": "Security clearance level",
                        },
                        "utilization_below": {
                            "type": "number",
                            "description": "Find employees with utilization below this value",
                        },
                        "utilization_above": {
                            "type": "number",
                            "description": "Find employees with utilization above this value",
                        },
                        "min_proficiency": {
                            "type": "number",
                            "description": "Minimum skill proficiency level",
                        },
                    },
                },
            },
        }


class GetEmployeeAllocations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        if not employee_id:
            return json.dumps({"error": "employee_id is required"})

        allocations = data.get("allocations", [])
        employee_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("employee_id") == employee_id
            and alloc.get("status") == "active"
        ]

        return json.dumps(employee_allocations, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_allocations",
                "description": "Get all active allocations for a specific employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        }
                    },
                    "required": ["employee_id"],
                },
            },
        }


class GetProjectDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        if not project_id:
            return json.dumps({"error": "project_id is required"})

        projects = data.get("projects", [])
        allocations = data.get("allocations", [])
        allocated_hours = sum(
            allocation["hours_per_week"] for allocation in allocations if allocation["project_id"] == project_id
        )
        for project in projects:
            if project.get("project_id") == project_id:
                data = project.copy()
                data["allocated_hours"] = allocated_hours
                return json.dumps(data, indent=2)

        return json.dumps({"error": f"Project with ID '{project_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_project_details",
                "description": "Get details of a specific project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        }
                    },
                    "required": ["project_id"],
                },
            },
        }


class UpdateAllocation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        allocation_id = kwargs.get("allocation_id")
        hours_per_week = kwargs.get("hours_per_week")
        end_date = kwargs.get("end_date")

        if not allocation_id:
            return json.dumps({"error": "allocation_id is required"})

        allocations = data.get("allocations", [])
        for allocation in allocations:
            if allocation.get("allocation_id") == allocation_id:
                if hours_per_week is not None:
                    allocation["hours_per_week"] = hours_per_week
                if end_date is not None:
                    allocation["end_date"] = end_date
                return json.dumps({"success": True, "allocation": allocation})

        return json.dumps({"error": f"Allocation with ID '{allocation_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_allocation",
                "description": "Update an existing allocation's hours or end date",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "allocation_id": {
                            "type": "string",
                            "description": "The allocation ID to update",
                        },
                        "hours_per_week": {
                            "type": "number",
                            "description": "New hours per week",
                        },
                        "end_date": {"type": "string", "description": "New end date"},
                    },
                    "required": ["allocation_id"],
                },
            },
        }


class CalculateEmployeeUtilization(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        if not employee_id:
            return json.dumps({"error": "employee_id is required"})

        allocations = data.get("allocations", [])
        employee_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("employee_id") == employee_id
            and alloc.get("status") == "active"
        ]

        total_hours = sum(
            alloc.get("hours_per_week", 0) for alloc in employee_allocations
        )
        utilization_percentage = (total_hours / 40) * 100

        return json.dumps(
            {
                "employee_id": employee_id,
                "total_hours": total_hours,
                "utilization_percentage": round(utilization_percentage, 1),
                "allocations_count": len(employee_allocations),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_employee_utilization",
                "description": "Calculate the utilization percentage for an employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        }
                    },
                    "required": ["employee_id"],
                },
            },
        }


class UpdateUtilizationLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        new_utilization = kwargs.get("new_utilization")

        if not all([employee_id, new_utilization is not None]):
            return json.dumps({"error": "employee_id and new_utilization are required"})

        utilization_logs = data.get("utilization_logs", [])

        log_entry = {
            "log_id": f"log_{uuid.uuid4().hex[:8]}",
            "employee_id": employee_id,
            "utilization": new_utilization,
            "timestamp": datetime.now().isoformat(),
        }

        utilization_logs.append(log_entry)

        employees = data.get("employees", [])
        for employee in employees:
            if employee.get("employee_id") == employee_id:
                employee["current_utilization"] = new_utilization
                break

        return json.dumps({"success": True, "log_entry": log_entry})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_utilization_log",
                "description": "Log utilization changes for an employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "new_utilization": {
                            "type": "number",
                            "description": "New utilization percentage",
                        },
                    },
                    "required": ["employee_id", "new_utilization"],
                },
            },
        }


class UpdateEmployeesUtilization(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:

        employee_ids = kwargs.get("employee_ids", [])

        if not employee_ids:
            return json.dumps({"error": "employee_ids is required"})

        employees = data.get("employees", [])
        employee_info = {
            info["employee_id"]: {"index": i, "max_hours_per_week": info["max_hours_per_week"]}
            for i, info in enumerate(employees)
        }

        allocations = data.get("allocations", [])

        utilization_per_employee = {}
        for allocation in allocations:
            employee_id = allocation.get("employee_id")
            if employee_id not in employee_ids:
                continue
            project_id = allocation.get("project_id")
            hours = allocation.get("hours_per_week")
            if employee_id in utilization_per_employee:
                utilization_per_employee[employee_id]["project_allocations"] += [
                    {
                        "project_id": project_id,
                        "hours": hours
                    },
                ]
                utilization_per_employee[employee_id]["total_hours"] += hours
                utilization_per_employee[employee_id]["utilization_percentage"] = int(
                    utilization_per_employee[employee_id]["total_hours"] * 100 /
                    employee_info[employee_id]["max_hours_per_week"]
                )
            else:
                utilization_per_employee[employee_id] = {
                    "log_id": f"log_{uuid.uuid4().hex[:8]}",
                    "employee_id": employee_id,
                    "week": "current",
                    "project_allocations": [
                        {
                            "project_id": project_id,
                            "hours": hours
                        },
                    ],
                    "total_hours": hours,
                    "utilization_percentage": int(hours * 100/ employee_info[employee_id]["max_hours_per_week"]),
                }

        new_utilization_logs = []
        for employee_id, utilization_info in utilization_per_employee.items():
            if employee_id not in employee_ids:
                continue
            new_utilization_logs.append(utilization_info)
            employees[employee_info[employee_id]["index"]]["current_utilization"] = (
                utilization_info)["utilization_percentage"]

        data["utilization_logs"] = new_utilization_logs


        return json.dumps({"success": True, "utilization_logs": new_utilization_logs})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employees_utilization",
                "description": "Update utilization log and employees current utilization with information "
                               "from allocations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_ids": {
                            "type": "list",
                            "description": "List of employee IDs",
                        }
                    },
                    "required": ["employee_ids"],
                },
            },
        }


class SearchProjects(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        needs_resources = kwargs.get("needs_resources")

        projects = data.get("projects", [])
        results = []

        for project in projects:
            match = True

            if name and name.lower() not in project.get("name", "").lower():
                match = False

            if needs_resources is not None:
                if needs_resources and not project.get("needs_resources", False):
                    match = False
                elif not needs_resources and project.get("needs_resources", True):
                    match = False

            if match:
                results.append(project)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_projects",
                "description": "Search for projects by name or resource needs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Project name to search for",
                        },
                        "needs_resources": {
                            "type": "boolean",
                            "description": "Filter by projects needing resources",
                        },
                    },
                },
            },
        }


class CalculateEmployeeAvailability(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        if not employee_id:
            return json.dumps({"error": "employee_id is required"})

        allocations = data.get("allocations", [])
        employee_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("employee_id") == employee_id
            and alloc.get("status") == "active"
        ]

        total_allocated = sum(
            alloc.get("hours_per_week", 0) for alloc in employee_allocations
        )
        available_hours = max(0, 40 - total_allocated)

        return json.dumps(
            {
                "employee_id": employee_id,
                "total_allocated_hours": total_allocated,
                "available_hours": available_hours,
                "availability_percentage": round((available_hours / 40) * 100, 1),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_employee_availability",
                "description": "Calculate available hours for an employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        }
                    },
                    "required": ["employee_id"],
                },
            },
        }


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


class CreateAllocation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        project_id = kwargs.get("project_id")
        hours_per_week = kwargs.get("hours_per_week", 0)
        role = kwargs.get("role")
        start_date = kwargs.get("start_date", "")
        end_date = kwargs.get("end_date", "")
        status = kwargs.get("status", "active")
        cross_department = kwargs.get("cross_department", False)

        if not all([employee_id, project_id, role]):
            return json.dumps(
                {
                    "error": "employee_id, project_id, hours_per_week, and role are required"
                }
            )

        allocations = data.get("allocations", [])
        projects = data.get("projects", [])
        skill_requirements = data.get("skill_requirements", [])

        is_temporary = any(
            term in role.lower()
            for term in ["consultant", "emergency", "temporary", "interim"]
        )

        project = next((p for p in projects if p.get("project_id") == project_id), None)

        skill_gap_filled = 0
        if project:

            project_requirements = next(
                (
                    req
                    for req in skill_requirements
                    if req.get("project_id") == project_id
                ),
                None,
            )

            if project_requirements:

                current_allocations = [
                    alloc
                    for alloc in allocations
                    if alloc.get("project_id") == project_id
                    and alloc.get("status") == "active"
                ]
                current_hours = sum(
                    alloc.get("hours_per_week", 0) for alloc in current_allocations
                )

                total_hours_needed = sum(
                    skill.get("hours_needed", 0)
                    for skill in project_requirements.get("required_skills", [])
                )

                previous_gap = max(0, total_hours_needed - current_hours)
                new_gap = max(0, total_hours_needed - (current_hours + hours_per_week))
                skill_gap_filled = previous_gap - new_gap

        allocation_id = kwargs.get("allocation_id") or f"alloc_{uuid.uuid4().hex[:8]}"

        new_allocation = {
            "allocation_id": allocation_id,
            "employee_id": employee_id,
            "project_id": project_id,
            "hours_per_week": hours_per_week,
            "role": role,
            "start_date": start_date,
            "end_date": end_date,
            "status": status,
            "cross_department": cross_department,
        }

        allocations.append(new_allocation)

        result = {
            "success": True,
            "allocation": new_allocation,
            "is_temporary": is_temporary,
        }

        if is_temporary:
            result["temporary_coverage"] = hours_per_week

        if skill_gap_filled > 0:
            result["skill_gap_filled"] = skill_gap_filled

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_allocation",
                "description": "Create a new resource allocation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "allocation_id": {
                            "type": "string",
                            "description": "Optional custom allocation ID",
                        },
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        },
                        "hours_per_week": {
                            "type": "number",
                            "description": "Hours allocated per week",
                        },
                        "role": {
                            "type": "string",
                            "description": "Role in the project",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date (YYYY-MM-DD)",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date (YYYY-MM-DD)",
                        },
                        "status": {
                            "type": "string",
                            "description": "Status: active, completed, cancelled",
                        },
                        "cross_department": {
                            "type": "boolean",
                            "description": "Is this a cross-department allocation",
                        },
                    },
                    "required": ["employee_id", "project_id", "hours_per_week", "role"],
                },
            },
        }


class UpdateRequestStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        status = kwargs.get("status")
        assigned_employees = kwargs.get("assigned_employees", [])
        allocated_hours = kwargs.get("allocated_hours", 0)

        if not all([request_id, status]):
            return json.dumps({"error": "request_id and status are required"})

        resource_requests = data.get("resource_requests", [])

        for request in resource_requests:
            if request.get("request_id") == request_id:
                request["status"] = status
                request["assigned_employees"] = assigned_employees
                request["allocated_hours"] = allocated_hours

                result = {"success": True, "request": request}
                if status == "partially_fulfilled":
                    hours_needed = request.get("hours_needed", 0)
                    skill_gap = hours_needed - allocated_hours
                    result["skill_gap"] = skill_gap

                return json.dumps(result)

        return json.dumps({"error": f"Request with ID '{request_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_request_status",
                "description": "Update the status of a resource request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The request ID",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status: pending, partially_fulfilled, fulfilled, cancelled",
                        },
                        "assigned_employees": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of assigned employee IDs",
                        },
                        "allocated_hours": {
                            "type": "number",
                            "description": "Total hours allocated",
                        },
                    },
                    "required": ["request_id", "status"],
                },
            },
        }


class UpdateDepartmentCapacity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department = kwargs.get("department")
        employee_id = kwargs.get("employee_id")
        hours_allocated = kwargs.get("hours_allocated")
        cross_department_project = kwargs.get("cross_department_project")

        if not all([department, employee_id, hours_allocated is not None]):
            return json.dumps(
                {"error": "department, employee_id, and hours_allocated are required"}
            )

        departments = data.get("departments", [])

        for dept in departments:
            if dept.get("department_name") == department:
                if "capacity_changes" not in dept:
                    dept["capacity_changes"] = []

                change_entry = {
                    "employee_id": employee_id,
                    "hours_allocated": hours_allocated,
                    "cross_department_project": cross_department_project,
                    "timestamp": datetime.now().isoformat(),
                }

                dept["capacity_changes"].append(change_entry)

                return json.dumps({"success": True, "department": dept})

        return json.dumps({"error": f"Department '{department}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_department_capacity",
                "description": "Update department capacity when allocations change",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "description": "Department name",
                        },
                        "employee_id": {"type": "string", "description": "Employee ID"},
                        "hours_allocated": {
                            "type": "number",
                            "description": "Hours allocated",
                        },
                        "cross_department_project": {
                            "type": "string",
                            "description": "Cross-department project ID",
                        },
                    },
                    "required": ["department", "employee_id", "hours_allocated"],
                },
            },
        }


class GetDepartmentCapacity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department = kwargs.get("department")
        if not department:
            return json.dumps({"error": "department is required"})

        employees = data.get("employees", [])
        allocations = data.get("allocations", [])

        dept_employees = [
            emp for emp in employees if emp.get("department") == department
        ]

        total_capacity = len(dept_employees) * 40
        total_allocated = 0

        for employee in dept_employees:
            emp_allocations = [
                alloc
                for alloc in allocations
                if alloc.get("employee_id") == employee.get("employee_id")
                and alloc.get("status") == "active"
            ]
            total_allocated += sum(
                alloc.get("hours_per_week", 0) for alloc in emp_allocations
            )

        available_capacity = total_capacity - total_allocated
        utilization_percentage = (
            (total_allocated / total_capacity * 100) if total_capacity > 0 else 0
        )

        return json.dumps(
            {
                "department": department,
                "total_employees": len(dept_employees),
                "total_capacity": total_capacity,
                "total_allocated": total_allocated,
                "available_capacity": available_capacity,
                "utilization_percentage": round(utilization_percentage, 1),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_department_capacity",
                "description": "Get current capacity information for a department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "description": "Department name",
                        }
                    },
                    "required": ["department"],
                },
            },
        }


class GetTeamDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_name = kwargs.get("team_name")
        team_id = kwargs.get("team_id")

        if not team_name and not team_id:
            return json.dumps({"error": "Either team_name or team_id is required"})

        teams = data.get("teams", [])

        for team in teams:
            if (team_id and team.get("team_id") == team_id) or (
                team_name and team.get("team_name") == team_name
            ):
                return json.dumps(team, indent=2)

        return json.dumps({"error": f"Team not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_details",
                "description": "Get details of a specific team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_name": {"type": "string", "description": "Team name"},
                        "team_id": {"type": "string", "description": "Team ID"},
                    },
                },
            },
        }


class UpdateProjectStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        status = kwargs.get("status")

        if not all([project_id, status]):
            return json.dumps({"error": "project_id and status are required"})

        projects = data.get("projects", [])

        for project in projects:
            if project.get("project_id") == project_id:
                project["status"] = status
                return json.dumps({"success": True, "project": project})

        return json.dumps({"error": f"Project with ID '{project_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_project_status",
                "description": "Update the status of a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status: active, completed, cancelled, on-hold",
                        },
                    },
                    "required": ["project_id", "status"],
                },
            },
        }


class UpdateProjectRequiredHours(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        required_hours = kwargs.get("required_hours")

        if not all([project_id, required_hours]):
            return json.dumps({"error": "project_id and required hours are required"})

        projects = data.get("projects", [])

        for project in projects:
            if project.get("project_id") == project_id:
                project["required_hours_per_week"] = required_hours
                return json.dumps({"success": True, "project": project})

        return json.dumps({"error": f"Project with ID '{project_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_project_required_hours",
                "description": "Update the hours per week required by a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        },
                        "required_hours": {
                            "type": "int",
                            "description": "Hours per week required by the project",
                        },
                    },
                    "required": ["project_id", "required_hours"],
                },
            },
        }


class GetProjectAllocations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        if not project_id:
            return json.dumps({"error": "project_id is required"})

        allocations = data.get("allocations", [])
        project_allocations = [
            alloc for alloc in allocations if alloc.get("project_id") == project_id
        ]

        return json.dumps(project_allocations, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_project_allocations",
                "description": "Get all allocations for a specific project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        }
                    },
                    "required": ["project_id"],
                },
            },
        }


class GetEmployeeDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        if not employee_id:
            return json.dumps({"error": "employee_id is required"})

        employees = data.get("employees", [])
        for employee in employees:
            if employee.get("employee_id") == employee_id:
                return json.dumps(employee, indent=2)

        return json.dumps({"error": f"Employee with ID '{employee_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_details",
                "description": "Get details of a specific employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        }
                    },
                    "required": ["employee_id"],
                },
            },
        }


class DeleteAllocation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        allocation_id = kwargs.get("allocation_id")
        if not allocation_id:
            return json.dumps({"error": "allocation_id is required"})

        allocations = data.get("allocations", [])

        for i, allocation in enumerate(allocations):
            if allocation.get("allocation_id") == allocation_id:
                removed_allocation = allocations.pop(i)
                return json.dumps(
                    {"success": True, "removed_allocation": removed_allocation}
                )

        return json.dumps({"error": f"Allocation with ID '{allocation_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_allocation",
                "description": "Remove an allocation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "allocation_id": {
                            "type": "string",
                            "description": "The allocation ID to delete",
                        }
                    },
                    "required": ["allocation_id"],
                },
            },
        }


class SearchAllocations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        end_date_before = kwargs.get("end_date_before")
        status = kwargs.get("status")
        allocation_id = kwargs.get("allocation_id")

        allocations = data.get("allocations", [])
        results = []

        for allocation in allocations:
            match = True

            if end_date_before and allocation.get("end_date"):
                if allocation.get("end_date") >= end_date_before:
                    match = False

            if status and allocation.get("status") != status:
                match = False

            if allocation_id and allocation.get("allocation_id") != allocation_id:
                match = False

            if match:
                results.append(allocation)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_allocations",
                "description": "Search allocations by end date, status, or allocation_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "end_date_before": {
                            "type": "string",
                            "description": "Find allocations ending before this date (YYYY-MM-DD)",
                        },
                        "status": {
                            "type": "string",
                            "description": "Status to filter by",
                        },
                        "allocation_id": {
                            "type": "string",
                            "description": "allocation_id of the allocation to get",
                        },
                    },
                },
            },
        }


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


class UpdateEmployeeStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        status = kwargs.get("status")
        available_from = kwargs.get("available_from")

        if not all([employee_id, status]):
            return json.dumps({"error": "employee_id and status are required"})

        employees = data.get("employees", [])

        for employee in employees:
            if employee.get("employee_id") == employee_id:
                employee["status"] = status
                if available_from:
                    employee["available_from"] = available_from
                return json.dumps({"success": True, "employee": employee})

        return json.dumps({"error": f"Employee with ID '{employee_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employee_status",
                "description": "Update employee status",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status: active, bench, leave",
                        },
                        "available_from": {
                            "type": "string",
                            "description": "Date when employee becomes available",
                        },
                    },
                    "required": ["employee_id", "status"],
                },
            },
        }


class UpdateEmployeesDepartment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        department = kwargs.get("department")

        if not all([employee_id, department]):
            return json.dumps({"error": "employee_id and department are required"})

        employees = data.get("employees", [])

        for employee in employees:
            if employee.get("employee_id") == employee_id:
                employee["department"] = department
                return json.dumps({"success": True, "employee": employee})

        return json.dumps({"error": f"Employee with ID '{employee_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employees_department",
                "description": "Update employee department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "department": {
                            "type": "string",
                            "description": "New department",
                        },
                    },
                    "required": ["employee_id", "department"],
                },
            },
        }


class UpdateTeamsDepartment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("team_id")
        department = kwargs.get("department")

        if not all([team_id, department]):
            return json.dumps({"error": "team_id and department are required"})

        teams = data.get("teams", [])

        for team in teams:
            if team.get("team_id") == team_id:
                team["department"] = department
                return json.dumps({"success": True, "team": team})

        return json.dumps({"error": f"Employee with ID '{team_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_teams_department",
                "description": "Update team department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {
                            "type": "string",
                            "description": "The team ID",
                        },
                        "department": {
                            "type": "string",
                            "description": "New department",
                        },
                    },
                    "required": ["team_id", "department"],
                },
            },
        }


class CheckAllocationDuration(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        project_id = kwargs.get("project_id")

        if not all([employee_id, project_id]):
            return json.dumps({"error": "employee_id and project_id are required"})

        allocations = data.get("allocations", [])

        for allocation in allocations:
            if (
                allocation.get("employee_id") == employee_id
                and allocation.get("project_id") == project_id
            ):
                start_date = datetime.fromisoformat(allocation.get("start_date"))
                duration_days = (datetime.now() - start_date).days
                duration_months = duration_days / 30

                return json.dumps(
                    {
                        "employee_id": employee_id,
                        "project_id": project_id,
                        "start_date": allocation.get("start_date"),
                        "duration_days": duration_days,
                        "duration_months": round(duration_months, 1),
                    }
                )

        return json.dumps({"error": "Allocation not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_allocation_duration",
                "description": "Check how long an employee has been allocated to a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        },
                    },
                    "required": ["employee_id", "project_id"],
                },
            },
        }


class CreateRotationSchedule(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        from_project = kwargs.get("from_project")
        to_project = kwargs.get("to_project")
        rotation_date = kwargs.get("rotation_date")
        hours_to_rotate = kwargs.get("hours_to_rotate")
        holiday_coverage = kwargs.get("holiday_coverage", "false")
        skill_development_rotation = kwargs.get("skill_development_rotation", "false")

        if not all(
            [employee_id, from_project, to_project, rotation_date, hours_to_rotate]
        ):
            return json.dumps({"error": "The fields employee_id, from_project, to_project, rotation_date, hours_to_rotate are required"})

        rotation_schedules = data.get("rotation_schedules", [])
        allocations = data.get("allocations", [])
        projects = data.get("projects", [])

        from_project_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("project_id") == from_project
            and alloc.get("status") == "active"
        ]

        employee_from_allocation = next(
            (
                alloc
                for alloc in from_project_allocations
                if alloc.get("employee_id") == employee_id
            ),
            None,
        )

        if not employee_from_allocation:
            return json.dumps(
                {"error": f"Employee {employee_id} not found on project {from_project}"}
            )

        from_project_data = next(
            (p for p in projects if p.get("project_id") == from_project), None
        )
        if from_project_data:
            required_hours = from_project_data.get("required_hours_per_week", 0)
            current_total_hours = sum(
                alloc.get("hours_per_week", 0) for alloc in from_project_allocations
            )
            hours_after_rotation = current_total_hours - hours_to_rotate

            coverage_percentage = (
                (hours_after_rotation / required_hours * 100)
                if required_hours > 0
                else 0
            )
            other_team_members = len(from_project_allocations) - 1

            if holiday_coverage.lower() == "true":

                coverage_maintained = (
                    hours_after_rotation >= required_hours * 0.3
                    or other_team_members > 0
                    or hours_to_rotate <= 25
                )
            else:
                coverage_maintained = coverage_percentage >= 80 or (
                    other_team_members > 0
                    and hours_after_rotation >= required_hours * 0.5
                )
        else:

            if holiday_coverage.lower() == "true":
                coverage_maintained = True
            else:
                coverage_maintained = (
                    len(from_project_allocations) > 1 or hours_to_rotate < 20
                )

        rotation_id = f"rot_{uuid.uuid4().hex[:8]}"

        new_rotation = {
            "rotation_id": rotation_id,
            "employee_id": employee_id,
            "from_project": from_project,
            "to_project": to_project,
            "rotation_date": rotation_date,
            "hours_to_rotate": hours_to_rotate,
            "holiday_coverage": holiday_coverage,
            "skill_development_rotation": skill_development_rotation,
            "status": "scheduled",
        }

        rotation_schedules.append(new_rotation)

        existing_rotations = [
            rot
            for rot in rotation_schedules
            if rot.get("status") == "scheduled"
            and skill_development_rotation.lower() == "true"
        ]

        developers_in_rotation = len(existing_rotations)
        skill_development_hours = hours_to_rotate

        return json.dumps(
            {
                "success": True,
                "rotation": new_rotation,
                "rotation_created": True,
                "coverage_maintained": coverage_maintained,
                "developers_in_rotation": developers_in_rotation,
                "skill_development_hours": skill_development_hours,
                "coverage_details": {
                    "from_project_allocations": len(from_project_allocations),
                    "other_team_members": other_team_members
                    if "other_team_members" in locals()
                    else 0,
                    "coverage_percentage": round(coverage_percentage, 1)
                    if "coverage_percentage" in locals()
                    else 0,
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_rotation_schedule",
                "description": "Create a rotation schedule for an employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "from_project": {
                            "type": "string",
                            "description": "Current project ID",
                        },
                        "to_project": {
                            "type": "string",
                            "description": "New project ID",
                        },
                        "rotation_date": {
                            "type": "string",
                            "description": "Date of rotation (YYYY-MM-DD)",
                        },
                        "hours_to_rotate": {
                            "type": "number",
                            "description": "Hours to rotate",
                        },
                        "holiday_coverage": {
                            "type": "bool",
                            "description": "Flag if the rotation is holiday coverage",
                        },
                        "skill_development_rotation": {
                            "type": "bool",
                            "description": "Flag if the rotation is skill development rotation",
                        },
                    },
                    "required": [
                        "employee_id",
                        "from_project",
                        "to_project",
                        "rotation_date",
                        "hours_to_rotate",
                    ],
                },
            },
        }


class GetDepartmentTeams(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department = kwargs.get("department")
        if not department:
            return json.dumps({"error": "department is required"})

        teams = data.get("teams", [])
        dept_teams = [team for team in teams if team.get("department") == department]

        return json.dumps(dept_teams, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_department_teams",
                "description": "Get all teams in a department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "description": "Department name",
                        }
                    },
                    "required": ["department"],
                },
            },
        }


class GetTeamUtilization(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("team_id")
        if not team_id:
            return json.dumps({"error": "team_id is required"})

        teams = data.get("teams", [])
        allocations = data.get("allocations", [])

        team = None
        for t in teams:
            if t.get("team_id") == team_id:
                team = t
                break

        if not team:
            return json.dumps({"error": f"Team with ID '{team_id}' not found"})

        team_members = team.get("members", [])
        total_capacity = len(team_members) * 40
        total_allocated = 0
        member_utilizations = []

        for member_id in team_members:
            member_allocations = [
                alloc
                for alloc in allocations
                if alloc.get("employee_id") == member_id
                and alloc.get("status") == "active"
            ]
            member_hours = sum(
                alloc.get("hours_per_week", 0) for alloc in member_allocations
            )
            total_allocated += member_hours
            member_utilizations.append(
                {
                    "employee_id": member_id,
                    "hours": member_hours,
                    "utilization": round((member_hours / 40) * 100, 1),
                }
            )

        team_utilization = (
            (total_allocated / total_capacity * 100) if total_capacity > 0 else 0
        )

        return json.dumps(
            {
                "team_id": team_id,
                "team_name": team.get("team_name"),
                "total_capacity": total_capacity,
                "total_allocated": total_allocated,
                "team_utilization": round(team_utilization, 1),
                "member_utilizations": member_utilizations,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_utilization",
                "description": "Get utilization metrics for a team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string", "description": "The team ID"}
                    },
                    "required": ["team_id"],
                },
            },
        }


class CalculateDepartmentUtilization(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department = kwargs.get("department")
        if not department:
            return json.dumps({"error": "department is required"})

        result = GetDepartmentCapacity.invoke(data, department=department)
        dept_data = json.loads(result)

        return json.dumps(
            {
                "department": department,
                "dept_utilization": dept_data.get("utilization_percentage", 0),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_department_utilization",
                "description": "Calculate overall department utilization",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "description": "Department name",
                        }
                    },
                    "required": ["department"],
                },
            },
        }


class CreateTeam(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_name = kwargs.get("team_name")
        project_id = kwargs.get("project_id")
        team_members = kwargs.get("team_members", [])

        if not all([team_name, project_id]):
            return json.dumps({"error": "team_name and project_id are required"})

        teams = data.get("teams", [])
        projects = data.get("projects", [])
        allocations = data.get("allocations", [])

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        if not project:
            return json.dumps({"error": f"Project {project_id} not found"})

        project_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("project_id") == project_id and alloc.get("status") == "active"
        ]

        total_allocated_hours = sum(
            alloc.get("hours_per_week", 0) for alloc in project_allocations
        )
        required_hours = project.get("required_hours_per_week", 0)

        staffing_percentage = (
            (total_allocated_hours / required_hours * 100) if required_hours > 0 else 0
        )
        project_staffed = staffing_percentage >= 80

        team_formed = True
        members_on_project = 0
        for member_id in team_members:
            member_allocation = next(
                (
                    alloc
                    for alloc in project_allocations
                    if alloc.get("employee_id") == member_id
                ),
                None,
            )
            if member_allocation:
                members_on_project += 1
            else:
                team_formed = False

        team_id = kwargs.get("team_id") or f"team_{uuid.uuid4().hex[:8]}"

        new_team = {
            "team_id": team_id,
            "team_name": team_name,
            "project_id": project_id,
            "members": team_members,
            "created_date": datetime.now().isoformat(),
            "status": "active",
        }

        teams.append(new_team)

        return json.dumps(
            {
                "success": True,
                "team": new_team,
                "team_formed": team_formed,
                "project_staffed": project_staffed,
                "staffing_details": {
                    "allocated_hours": total_allocated_hours,
                    "required_hours": required_hours,
                    "staffing_percentage": round(staffing_percentage, 1),
                    "members_on_project": members_on_project,
                    "total_members": len(team_members),
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_team",
                "description": "Create a new team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_name": {"type": "string", "description": "Team name"},
                        "project_id": {
                            "type": "string",
                            "description": "Associated project ID",
                        },
                        "team_members": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs",
                        },
                        "team_id": {
                            "type": "string",
                            "description": "Optional custom team ID",
                        },
                    },
                    "required": ["team_name", "project_id"],
                },
            },
        }


class CreateProject(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_name = kwargs.get("project_name")
        department = kwargs.get("department")
        status = kwargs.get("status", "active")
        priority = kwargs.get("priority", "low")
        required_hours_per_week = kwargs.get("required_hours_per_week")
        need_resources = kwargs.get("need_resources", "true")
        start_date = kwargs.get("start_date", "to be defined")
        end_date = kwargs.get("end_date", "to be defined")
        project_id = kwargs.get("project_id", f"project_{uuid.uuid4().hex[:8]}")

        if not all([project_name, department, required_hours_per_week]):
            return json.dumps({"error": "project_name, required_hours_per_week and department are required parameters"})

        projects = data.get("projects", [])

        new_project = {
            "project_id": project_id,
            "project_name": project_name,
            "department": department,
            "status": status,
            "priority": priority,
            "required_hours_per_week": required_hours_per_week,
            "need_resources": need_resources,
            "start_date": start_date,
            "end_date": end_date,
        }

        projects.append(new_project)

        return json.dumps(
            {
                "success": True,
                "project_id": project_id,
                "name": project_name,
                "department": department,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_project",
                "description": "Create a new project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Project name"},
                        "project_id": {
                            "type": "string",
                            "description": "ID for the project",
                        },
                        "priority": {
                            "type": "str",
                            "description": "Project's priority",
                        },
                        "status": {
                            "type": "string",
                            "description": "Project's priority",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Project's start date",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "Project's end date",
                        },
                        "required_hours_per_week": {
                            "type": "int",
                            "description": "Project's required allocation hours per week",
                        },
                        "department": {
                            "type": "string",
                            "description": "Project's department",
                        },
                        "needs_resources": {
                            "type": "bool",
                            "description": "Indicates if the project need more allocation",
                        },
                    },
                    "required": ["project_name", "department", "required_hours_per_week"],
                },
            },
        }


class CreateDepartment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department_name = kwargs.get("name")
        department_id = kwargs.get("department_id", f"conflict_{uuid.uuid4().hex[:8]}")
        head_id = kwargs.get("head_id")

        if not all([department_name, head_id]):
            return json.dumps({"error": "department_name and head_id are required parameters"})

        departments = data.get("departments", [])

        new_department = {
            "department_id": department_id,
            "department_name": department_name,
            "head_id": head_id,
            "total_capacity_hours": 800,
            "allocated_hours": 680,
            "available_hours": 120,
            "employee_count": 20,
            "avg_utilization": 85
        }

        departments.append(new_department)

        return json.dumps(
            {
                "success": True,
                "department_id": department_id,
                "name": department_name,
                "head_id": head_id,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_department",
                "description": "Create a new department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Department name"},
                        "department_id": {
                            "type": "string",
                            "description": "ID for the department",
                        },
                        "head_id": {
                            "type": "string",
                            "description": "Employee ID for the department head",
                        },
                    },
                    "required": ["name", "head_id"],
                },
            },
        }


class UpdateDepartmentsUtilization(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:

        departments = data.get("departments", [])
        employees = data.get("employees", [])
        allocations = data.get("allocations", [])
        employee_info = {}
        department_info = {}
        for employee in employees:
            department = employee["department"]
            employee_info[employee["employee_id"]] = department
            if department in department_info:
                department_info[department]["total_capacity_hours"] += employee["max_hours_per_week"]
                department_info[department]["employee_count"] += 1
            else:
                department_info[department] = {
                    "total_capacity_hours": employee["max_hours_per_week"],
                    "employee_count": 1
                }

        for allocation in allocations:
            employee_id = allocation["employee_id"]
            department = employee_info.get(employee_id)
            if department in department_info:
                if "allocated_hours" in department_info[department]:
                    department_info[department]["allocated_hours"] += allocation["hours_per_week"]
                else:
                    department_info[department]["allocated_hours"] = allocation["hours_per_week"]
            else:
                department_info[department] = {"allocated_hours": allocation["hours_per_week"]}

        for department in departments:
            department_name = department["department_name"]
            if department_name in department_info:
                department["total_capacity_hours"] = department_info.get(department_name, {}).get("total_capacity_hours", 0)
                department["allocated_hours"] = department_info.get(department_name, {}).get("allocated_hours", 0)
                department["employee_count"] = department_info.get(department_name, {}).get("employee_count", 0)
                department["available_hours"] = department["total_capacity_hours"] - department["allocated_hours"]
                department["avg_utilization"] = department["allocated_hours"] / department["employee_count"]

        return json.dumps({"success": True, })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_departments_utilization",
                "description": "Update departments main metrics",
                "parameters": {},
            },
        }


class DeleteDepartment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department_name = kwargs.get("name")

        if not all([department_name]):
            return json.dumps({"error": "department_name is a required parameters"})

        departments = data.get("departments", [])

        for i, department in enumerate(departments):
            if department.get("department_name") == department_name:
                departments.pop(i)
                return json.dumps({"success": True})

        return json.dumps(
            {
                "error": "Department name '{}' does not exist".format(department_name),
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_department",
                "description": "Delete a department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Department name"},
                    },
                    "required": ["name"],
                },
            },
        }


class GetDepartmentDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")

        if not name:
            return json.dumps({"error": "name is a required parameter"})

        departments = data.get("departments", [])

        for department in departments:
            if department.get("department_name") == name:
                return json.dumps({"success": True, "details": department})

        return json.dumps(
            {
                "error": "name or department is not found",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_department_details",
                "description": "Get department details",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Name of the department",
                        },
                    },
                    "required": ["name"],
                },
            },
        }


class AnalyzeAllocationEfficiency(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        projects = kwargs.get("projects", [])
        check_partial_allocations = kwargs.get("check_partial_allocations", False)
        check_skill_mismatch = kwargs.get("check_skill_mismatch", False)

        allocations = data.get("allocations", [])
        employees = data.get("employees", [])
        projects_data = data.get("projects", [])

        partial_allocations_found = 0
        skill_mismatches_found = 0
        recommendations = []

        if check_partial_allocations:

            employee_allocations = {}
            for alloc in allocations:
                if (
                    alloc.get("project_id") in projects
                    and alloc.get("status") == "active"
                ):
                    emp_id = alloc.get("employee_id")
                    if emp_id not in employee_allocations:
                        employee_allocations[emp_id] = []
                    employee_allocations[emp_id].append(alloc)

            for emp_id, emp_allocations in employee_allocations.items():
                for alloc in emp_allocations:
                    if alloc.get("hours_per_week", 0) < 20:
                        partial_allocations_found += 1

            if partial_allocations_found > 0:
                recommendations.append("Consider consolidating partial allocations")

        if check_skill_mismatch:

            for alloc in allocations:
                if (
                    alloc.get("project_id") in projects
                    and alloc.get("status") == "active"
                ):
                    emp_id = alloc.get("employee_id")
                    employee = next(
                        (e for e in employees if e.get("employee_id") == emp_id), None
                    )

                    if employee:
                        role = employee.get("role", "").lower()
                        project = next(
                            (
                                p
                                for p in projects_data
                                if p.get("project_id") == alloc.get("project_id")
                            ),
                            None,
                        )

                        if ("senior" in role or "architect" in role) and project:
                            if (
                                project.get("priority") == "medium"
                                or project.get("priority") == "low"
                            ):
                                skill_mismatches_found += 1

            if skill_mismatches_found > 0:
                recommendations.append("Review skill assignments")

        return json.dumps(
            {
                "projects_analyzed": len(projects),
                "partial_allocations_found": partial_allocations_found,
                "skill_mismatches_found": skill_mismatches_found,
                "recommendations": recommendations,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyze_allocation_efficiency",
                "description": "Analyze allocation efficiency across projects",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "projects": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of project IDs to analyze",
                        },
                        "check_partial_allocations": {
                            "type": "boolean",
                            "description": "Check for partial allocations",
                        },
                        "check_skill_mismatch": {
                            "type": "boolean",
                            "description": "Check for skill mismatches",
                        },
                    },
                    "required": ["projects"],
                },
            },
        }


class ConsolidateAllocations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        from_projects = kwargs.get("from_projects", [])
        to_project = kwargs.get("to_project")
        total_hours = kwargs.get("total_hours")

        return json.dumps(
            {
                "success": True,
                "consolidation": {
                    "employee_id": employee_id,
                    "from_projects": from_projects,
                    "to_project": to_project,
                    "total_hours": total_hours,
                    "status": "completed",
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "consolidate_allocations",
                "description": "Consolidate multiple partial allocations into one",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "from_projects": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of project IDs to consolidate from",
                        },
                        "to_project": {
                            "type": "string",
                            "description": "Target project ID",
                        },
                        "total_hours": {
                            "type": "number",
                            "description": "Total hours to allocate",
                        },
                    },
                    "required": [
                        "employee_id",
                        "from_projects",
                        "to_project",
                        "total_hours",
                    ],
                },
            },
        }


class ReassignJuniorWork(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        from_employee = kwargs.get("from_employee")
        to_employee = kwargs.get("to_employee")
        project_id = kwargs.get("project_id")
        hours = kwargs.get("hours")

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


class CalculateOptimizationMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        projects = kwargs.get("projects", [])
        metric_type = kwargs.get("metric_type", "efficiency_gain")

        allocations = data.get("allocations", [])
        employees = data.get("employees", [])
        projects_data = data.get("projects", [])

        total_allocated_hours = 0
        total_required_hours = 0
        overallocated_employees = 0
        underutilized_employees = 0
        skill_mismatches = 0
        partial_allocations = 0

        project_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("project_id") in projects and alloc.get("status") == "active"
        ]

        for alloc in project_allocations:
            total_allocated_hours += alloc.get("hours_per_week", 0)

            if alloc.get("hours_per_week", 0) < 20:
                partial_allocations += 1

        for proj_id in projects:
            project = next(
                (p for p in projects_data if p.get("project_id") == proj_id), None
            )
            if project:
                total_required_hours += project.get("required_hours_per_week", 0)

        employee_hours = {}
        for alloc in allocations:
            if alloc.get("status") == "active":
                emp_id = alloc.get("employee_id")
                if emp_id not in employee_hours:
                    employee_hours[emp_id] = 0
                employee_hours[emp_id] += alloc.get("hours_per_week", 0)

        for emp_id, hours in employee_hours.items():
            utilization = (hours / 40) * 100
            if utilization > 100:
                overallocated_employees += 1
            elif utilization < 70:
                underutilized_employees += 1

        for alloc in project_allocations:
            emp_id = alloc.get("employee_id")
            employee = next(
                (e for e in employees if e.get("employee_id") == emp_id), None
            )
            project = next(
                (
                    p
                    for p in projects_data
                    if p.get("project_id") == alloc.get("project_id")
                ),
                None,
            )

            if employee and project:
                role = employee.get("role", "").lower()
                if ("senior" in role or "architect" in role) and project.get(
                    "priority"
                ) in ["low", "medium"]:
                    skill_mismatches += 1

        allocation_efficiency = (
            (total_allocated_hours / total_required_hours * 100)
            if total_required_hours > 0
            else 0
        )

        potential_improvements = (
            (overallocated_employees * 5)
            + (underutilized_employees * 3)
            + (skill_mismatches * 2)
            + (partial_allocations * 1)
        )

        efficiency_gain = min(potential_improvements, 30)

        optimization_complete = efficiency_gain < 5

        return json.dumps(
            {
                "projects_analyzed": len(projects),
                "metric_type": metric_type,
                "efficiency_gain": efficiency_gain,
                "optimization_complete": optimization_complete,
                "metrics": {
                    "allocation_efficiency": round(allocation_efficiency, 1),
                    "overallocated_employees": overallocated_employees,
                    "underutilized_employees": underutilized_employees,
                    "skill_mismatches": skill_mismatches,
                    "partial_allocations": partial_allocations,
                    "total_allocated_hours": total_allocated_hours,
                    "total_required_hours": total_required_hours,
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_optimization_metrics",
                "description": "Calculate optimization metrics for projects",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "projects": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of project IDs",
                        },
                        "metric_type": {
                            "type": "string",
                            "description": "Type of metric to calculate",
                        },
                    },
                    "required": ["projects"],
                },
            },
        }


class CreateResourceConflict(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        competing_projects = kwargs.get("competing_projects", [])
        conflict_type = kwargs.get("conflict_type", "allocation")
        resolution = kwargs.get("resolution", "")

        if not all([employee_id, competing_projects]):
            return json.dumps(
                {"error": "employee_id and competing_projects are required"}
            )

        resource_conflicts = data.get("resource_conflicts", [])

        conflict_id = f"conflict_{uuid.uuid4().hex[:8]}"

        new_conflict = {
            "conflict_id": conflict_id,
            "employee_id": employee_id,
            "competing_projects": competing_projects,
            "conflict_type": conflict_type,
            "resolution": resolution,
            "created_date": datetime.now().isoformat(),
            "status": "resolved" if resolution else "pending",
        }

        resource_conflicts.append(new_conflict)

        return json.dumps({"success": True, "conflict": new_conflict})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_resource_conflict",
                "description": "Create a record of resource conflict when multiple projects compete for the same employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "competing_projects": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of competing project IDs",
                        },
                        "conflict_type": {
                            "type": "string",
                            "description": "Type of conflict",
                        },
                        "resolution": {
                            "type": "string",
                            "description": "How the conflict was resolved",
                        },
                    },
                    "required": ["employee_id", "competing_projects"],
                },
            },
        }


class CompareProjectPriorities(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id_1 = kwargs.get("project_id_1")
        project_id_2 = kwargs.get("project_id_2")

        if not all([project_id_1, project_id_2]):
            return json.dumps({"error": "project_id_1 and project_id_2 are required"})

        projects = data.get("projects", [])

        project_1 = None
        project_2 = None

        for project in projects:
            if project.get("project_id") == project_id_1:
                project_1 = project
            elif project.get("project_id") == project_id_2:
                project_2 = project

        if not project_1 or not project_2:
            return json.dumps({"error": "One or both projects not found"})

        priority_1 = project_1.get("priority", 3)
        priority_2 = project_2.get("priority", 3)

        if priority_1 < priority_2:
            higher_priority = project_id_1
            lower_priority = project_id_2
        elif priority_2 < priority_1:
            higher_priority = project_id_2
            lower_priority = project_id_1
        else:
            higher_priority = project_id_1
            lower_priority = project_id_2

        return json.dumps(
            {
                "higher_priority_project": higher_priority,
                "lower_priority_project": lower_priority,
                "priority_values": {project_id_1: priority_1, project_id_2: priority_2},
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compare_project_priorities",
                "description": "Compare priorities of two projects to determine which has higher priority",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id_1": {
                            "type": "string",
                            "description": "First project ID",
                        },
                        "project_id_2": {
                            "type": "string",
                            "description": "Second project ID",
                        },
                    },
                    "required": ["project_id_1", "project_id_2"],
                },
            },
        }


class SummarizeWorkloadRebalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hours_transferred = kwargs.get("hours_transferred", 0)
        from_employee = kwargs.get("from_employee")
        to_employee = kwargs.get("to_employee")

        if not all([hours_transferred, from_employee, to_employee]):
            return json.dumps(
                {
                    "error": "hours_transferred, from_employee, and to_employee are required"
                }
            )

        return json.dumps(
            {
                "workload_balanced": True,
                "rebalanced": True,
                "hours_transferred": hours_transferred,
                "from_employee": from_employee,
                "to_employee": to_employee,
                "status": "completed",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_workload_rebalance",
                "description": "Generate a summary of workload rebalancing operations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hours_transferred": {
                            "type": "number",
                            "description": "Number of hours transferred",
                        },
                        "from_employee": {
                            "type": "string",
                            "description": "Employee ID who had hours reduced",
                        },
                        "to_employee": {
                            "type": "string",
                            "description": "Employee ID who received additional hours",
                        },
                    },
                    "required": ["hours_transferred", "from_employee", "to_employee"],
                },
            },
        }


class SummarizeReallocation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        reallocated_employees = kwargs.get("reallocated_employees", [])
        cancelled_project_id = kwargs.get("cancelled_project_id")
        new_projects = kwargs.get("new_projects", [])

        if not all([reallocated_employees, cancelled_project_id]):
            return json.dumps(
                {"error": "reallocated_employees and cancelled_project_id are required"}
            )

        reallocated_count = len(reallocated_employees)

        all_resources_assigned = len(new_projects) >= reallocated_count

        return json.dumps(
            {
                "reallocated_count": reallocated_count,
                "all_resources_assigned": all_resources_assigned,
                "cancelled_project": cancelled_project_id,
                "reallocated_employees": reallocated_employees,
                "new_projects": new_projects,
                "summary": f"Successfully reallocated {reallocated_count} employees from cancelled project {cancelled_project_id}",
                "status": "completed",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_reallocation",
                "description": "Generate a summary of employee reallocation after project cancellation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reallocated_employees": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs that were reallocated",
                        },
                        "cancelled_project_id": {
                            "type": "string",
                            "description": "ID of the cancelled project",
                        },
                        "new_projects": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of new project IDs where employees were assigned",
                        },
                    },
                    "required": ["reallocated_employees", "cancelled_project_id"],
                },
            },
        }


class SummarizeOptimizationResults(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        optimization_actions = kwargs.get("optimization_actions", [])
        employees_optimized = kwargs.get("employees_optimized", [])

        utilization_optimized = (
            len(optimization_actions) > 0 or len(employees_optimized) > 0
        )
        resources_balanced = utilization_optimized

        return json.dumps(
            {
                "utilization_optimized": utilization_optimized,
                "resources_balanced": resources_balanced,
                "optimization_summary": {
                    "actions_performed": optimization_actions,
                    "employees_affected": employees_optimized,
                    "status": "completed"
                    if utilization_optimized
                    else "no_optimization_needed",
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_optimization_results",
                "description": "Generate a summary of resource utilization optimization results",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "optimization_actions": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of optimization actions performed",
                        },
                        "employees_optimized": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs that were optimized",
                        },
                    },
                },
            },
        }


class SummarizeTeamExpansion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        new_team_members = kwargs.get("new_team_members", [])
        additional_hours = kwargs.get("additional_hours", 0)
        existing_hours = kwargs.get("existing_hours", 0)

        if not all([project_id, new_team_members, additional_hours is not None]):
            return json.dumps(
                {
                    "error": "project_id, new_team_members, and additional_hours are required"
                }
            )

        total_hours = existing_hours + additional_hours

        return json.dumps(
            {
                "project_id": project_id,
                "new_team_members": new_team_members,
                "additional_hours": additional_hours,
                "total_hours": total_hours,
                "expansion_summary": {
                    "members_added": len(new_team_members),
                    "hours_added": additional_hours,
                    "final_allocation": total_hours,
                    "status": "completed",
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_team_expansion",
                "description": "Generate a summary of team expansion operations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID that was expanded",
                        },
                        "new_team_members": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs added to the team",
                        },
                        "additional_hours": {
                            "type": "number",
                            "description": "Total additional hours allocated",
                        },
                        "existing_hours": {
                            "type": "number",
                            "description": "Existing hours before expansion",
                        },
                    },
                    "required": ["project_id", "new_team_members", "additional_hours"],
                },
            },
        }


class SummarizeProjectConsolidation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        consolidated_to = kwargs.get("consolidated_to")
        total_hours = kwargs.get("total_hours")
        team_size = kwargs.get("team_size")
        consolidated_projects = kwargs.get("consolidated_projects", [])

        if not all([consolidated_to, total_hours is not None, team_size is not None]):
            return json.dumps(
                {"error": "consolidated_to, total_hours, and team_size are required"}
            )

        return json.dumps(
            {
                "consolidated_to": consolidated_to,
                "total_hours": total_hours,
                "team_size": team_size,
                "consolidation_summary": {
                    "target_project": consolidated_to,
                    "final_team_size": team_size,
                    "total_allocated_hours": total_hours,
                    "consolidated_projects": consolidated_projects,
                    "status": "completed",
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_project_consolidation",
                "description": "Generate a summary of project consolidation operations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "consolidated_to": {
                            "type": "string",
                            "description": "The target project ID where teams were consolidated",
                        },
                        "total_hours": {
                            "type": "number",
                            "description": "Total hours allocated to the consolidated project",
                        },
                        "team_size": {
                            "type": "number",
                            "description": "Final team size after consolidation",
                        },
                        "consolidated_projects": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of project IDs that were consolidated",
                        },
                    },
                    "required": ["consolidated_to", "total_hours", "team_size"],
                },
            },
        }


class ValidateComplianceStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        required_clearance = kwargs.get("required_clearance", "secret")

        if not project_id:
            return json.dumps({"error": "project_id is required"})

        allocations = data.get("allocations", [])
        employees = data.get("employees", [])

        project_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("project_id") == project_id and alloc.get("status") == "active"
        ]

        cleared_resources = 0
        compliance_violations = []

        for allocation in project_allocations:
            employee_id = allocation.get("employee_id")

            employee = None
            for emp in employees:
                if emp.get("employee_id") == employee_id:
                    employee = emp
                    break

            if employee:
                employee_clearance = employee.get("clearance")
                if employee_clearance == required_clearance:
                    cleared_resources += 1
                else:
                    compliance_violations.append(
                        {
                            "employee_id": employee_id,
                            "required_clearance": required_clearance,
                            "actual_clearance": employee_clearance,
                        }
                    )

        compliance_achieved = len(compliance_violations) == 0

        return json.dumps(
            {
                "project_id": project_id,
                "required_clearance": required_clearance,
                "compliance_achieved": compliance_achieved,
                "cleared_resources": cleared_resources,
                "total_allocations": len(project_allocations),
                "compliance_violations": compliance_violations,
                "validation_summary": {
                    "status": "compliant" if compliance_achieved else "non_compliant",
                    "cleared_count": cleared_resources,
                    "violation_count": len(compliance_violations),
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_compliance_status",
                "description": "Validate security clearance compliance for a project and return compliance status",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID to validate",
                        },
                        "required_clearance": {
                            "type": "string",
                            "description": "Required security clearance level (default: secret)",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }


class SummarizeDepartmentMerger(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        merged_departments = kwargs.get("merged_departments", [])
        new_department_name = kwargs.get("new_department_name")
        teams_consolidated = kwargs.get("teams_consolidated", [])
        final_utilization = kwargs.get("final_utilization")
        employees_affected = kwargs.get("employees_affected", [])

        if not all([merged_departments, new_department_name]):
            return json.dumps(
                {"error": "merged_departments and new_department_name are required"}
            )

        if final_utilization is None and employees_affected:
            employees = data.get("employees", [])
            total_hours = 0
            total_capacity = 0

            for emp_id in employees_affected:
                for employee in employees:
                    if employee.get("employee_id") == emp_id:
                        total_capacity += 40
                        total_hours += (
                            employee.get("current_utilization", 0) / 100
                        ) * 40
                        break

            if total_capacity > 0:
                final_utilization = round((total_hours / total_capacity) * 100, 1)

        return json.dumps(
            {
                "merged_department_utilization": final_utilization,
                "teams_consolidated": len(teams_consolidated),
                "merger_summary": {
                    "departments_merged": merged_departments,
                    "new_department": new_department_name,
                    "teams_affected": teams_consolidated,
                    "employees_in_new_dept": len(employees_affected),
                    "status": "completed",
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_department_merger",
                "description": "Generate a summary of department merger operations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "merged_departments": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of department names that were merged",
                        },
                        "new_department_name": {
                            "type": "string",
                            "description": "Name of the new merged department",
                        },
                        "teams_consolidated": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of team IDs that were consolidated",
                        },
                        "final_utilization": {
                            "type": "number",
                            "description": "Final utilization percentage of merged department",
                        },
                        "employees_affected": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs in the merged department",
                        },
                    },
                    "required": ["merged_departments", "new_department_name"],
                },
            },
        }


class SummarizeProjectPhaseMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")

        if not project_id:
            return json.dumps({"error": "project_id is required"})

        allocations = data.get("allocations", [])
        employees = data.get("employees", [])

        project_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("project_id") == project_id and alloc.get("status") == "active"
        ]

        dev_hours = 0
        qa_hours = 0

        dev_keywords = [
            "developer",
            "dev",
            "architect",
            "engineer",
            "programmer",
            "coder",
        ]
        qa_keywords = ["qa", "test", "quality", "tester"]

        for allocation in project_allocations:
            employee_id = allocation.get("employee_id")
            role = allocation.get("role", "").lower()
            hours = allocation.get("hours_per_week", 0)

            employee = next(
                (emp for emp in employees if emp.get("employee_id") == employee_id),
                None,
            )

            is_dev_role = False
            is_qa_role = False

            for keyword in dev_keywords:
                if keyword in role and "qa" not in role and "test" not in role:
                    is_dev_role = True
                    break

            for keyword in qa_keywords:
                if keyword in role:
                    is_qa_role = True
                    break

            if not is_dev_role and not is_qa_role and employee:
                emp_role = employee.get("role", "").lower()
                emp_dept = employee.get("department", "").lower()

                for keyword in dev_keywords:
                    if (
                        keyword in emp_role
                        and "qa" not in emp_role
                        and "test" not in emp_role
                    ):
                        is_dev_role = True
                        break

                for keyword in qa_keywords:
                    if keyword in emp_role or keyword in emp_dept:
                        is_qa_role = True
                        break

                if emp_dept == "engineering" and not is_qa_role:
                    is_dev_role = True
                elif emp_dept == "qa":
                    is_qa_role = True

            if is_dev_role:
                dev_hours += hours
            elif is_qa_role:
                qa_hours += hours

        return json.dumps(
            {
                "project_id": project_id,
                "dev_hours": dev_hours,
                "qa_hours": qa_hours,
                "total_allocations": len(project_allocations),
                "phase_transition_summary": {
                    "development_hours": dev_hours,
                    "qa_testing_hours": qa_hours,
                    "status": "calculated",
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_project_phase_metrics",
                "description": "Calculate and summarize development and QA hours for a project phase transition",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID to analyze",
                        }
                    },
                    "required": ["project_id"],
                },
            },
        }


class SummarizeHybridWorkAllocation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")

        if not project_id:
            return json.dumps({"error": "project_id is required"})

        allocations = data.get("allocations", [])
        employees = data.get("employees", [])

        project_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("project_id") == project_id and alloc.get("status") == "active"
        ]

        total_hours = 0
        onsite_hours = 0
        remote_work_maintained = True

        for allocation in project_allocations:
            employee_id = allocation.get("employee_id")
            hours = allocation.get("hours_per_week", 0)
            role = allocation.get("role", "").lower()

            total_hours += hours

            employee = next(
                (emp for emp in employees if emp.get("employee_id") == employee_id),
                None,
            )

            if employee:
                work_location_preference = employee.get(
                    "work_location_preference", "remote"
                )
                can_work_onsite = employee.get("can_work_onsite", True)

                is_onsite_allocation = False

                if "onsite" in role:
                    is_onsite_allocation = True

                    if work_location_preference == "remote" and not can_work_onsite:
                        remote_work_maintained = False
                elif work_location_preference == "onsite":
                    is_onsite_allocation = True
                elif work_location_preference == "hybrid":

                    is_onsite_allocation = True
                    onsite_hours += hours * 0.5
                    continue

                if is_onsite_allocation:
                    onsite_hours += hours

        onsite_percentage = (
            round((onsite_hours / total_hours * 100)) if total_hours > 0 else 0
        )

        return json.dumps(
            {
                "project_id": project_id,
                "onsite_percentage": onsite_percentage,
                "remote_work_maintained": remote_work_maintained,
                "total_hours": total_hours,
                "onsite_hours": onsite_hours,
                "hybrid_work_summary": {
                    "total_project_hours": total_hours,
                    "onsite_hours": onsite_hours,
                    "onsite_percentage": onsite_percentage,
                    "remote_agreements_respected": remote_work_maintained,
                    "status": "calculated",
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_hybrid_work_allocation",
                "description": "Calculate and summarize onsite vs remote work allocation percentages for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID to analyze",
                        }
                    },
                    "required": ["project_id"],
                },
            },
        }


TOOLS = [
    SearchEmployees(),
    GetEmployeeAllocations(),
    GetProjectDetails(),
    UpdateAllocation(),
    CalculateEmployeeUtilization(),
    UpdateUtilizationLog(),
    UpdateEmployeesUtilization(),
    SearchProjects(),
    CalculateEmployeeAvailability(),
    CreateResourceRequest(),
    CreateAllocation(),
    CreateProject(),
    CreateDepartment(),
    UpdateDepartmentsUtilization(),
    DeleteDepartment(),
    GetDepartmentDetails(),
    UpdateRequestStatus(),
    UpdateDepartmentCapacity(),
    GetDepartmentCapacity(),
    GetTeamDetails(),
    UpdateProjectStatus(),
    UpdateProjectRequiredHours(),
    GetProjectAllocations(),
    GetEmployeeDetails(),
    DeleteAllocation(),
    SearchAllocations(),
    CreateBenchAssignment(),
    UpdateEmployeeStatus(),
    UpdateEmployeesDepartment(),
    UpdateTeamsDepartment(),
    CheckAllocationDuration(),
    CreateRotationSchedule(),
    GetDepartmentTeams(),
    GetTeamUtilization(),
    CalculateDepartmentUtilization(),
    CreateTeam(),
    AnalyzeAllocationEfficiency(),
    ConsolidateAllocations(),
    ReassignJuniorWork(),
    CalculateOptimizationMetrics(),
    CreateResourceConflict(),
    CompareProjectPriorities(),
    SummarizeWorkloadRebalance(),
    SummarizeReallocation(),
    SummarizeOptimizationResults(),
    SummarizeTeamExpansion(),
    SummarizeProjectConsolidation(),
    ValidateComplianceStatus(),
    SummarizeDepartmentMerger(),
    SummarizeProjectPhaseMetrics(),
    SummarizeHybridWorkAllocation(),
]
