import json
from typing import Any

from domains.dto import Tool


#ACCESS APIS
class get_employee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        employees = data.get("employees", [])
        for e in employees:
            if e["employee_id"] == employee_id:
                payload = e
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"employee_id {employee_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetEmployee",
                "description": "Return the complete employee record including fields first_name, last_name, preferred_name, date_of_birth, gender, ethnicity_code, nationality, marital_status, hire_date, termination_date, status, position_id, department_id, level_id, manager_id, work_location, work_email, work_phone, compensation_id, benefit_plan_ids, performance_review_ids, skills, role_description, notes for the given employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Unique ID of the employee to fetch",
                        }
                    },
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


class get_all_employees(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], department_id: str = None, level_id: str = None
    ) -> str:
        employees = data.get("employees", [])
        filtered = [
            e
            for e in employees
            if (not department_id or e.get("department_id") == department_id)
            and (not level_id or e.get("level_id") == level_id)
        ]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getAllEmployees",
                "description": "Return a list of all employees, optionally filtered by department_id and/or level_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {
                            "type": "string",
                            "description": "Department ID to filter employees",
                        },
                        "level_id": {
                            "type": "string",
                            "description": "Job level ID to filter employees",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class get_department(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_id: str) -> str:
        departments = data.get("departments", [])
        for d in departments:
            if d["department_id"] == department_id:
                payload = d
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"department_id {department_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetDepartment",
                "description": "Return the department record for the given department_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {
                            "type": "string",
                            "description": "Unique ID of the department to fetch",
                        }
                    },
                    "required": ["department_id"],
                    "additionalProperties": False,
                },
            },
        }


class get_departments(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], departments: list = None) -> str:
        if departments is None:
            departments = []
        payload = departments
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getDepartments",
                "description": "Return a list of all departments.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class get_position(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], position_id: str) -> str:
        positions = data.get("positions", [])
        for p in positions:
            if p["position_id"] == position_id:
                payload = p
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"position_id {position_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getPosition",
                "description": "Return the position record for the given position_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "position_id": {
                            "type": "string",
                            "description": "Unique ID of the position to fetch",
                        }
                    },
                    "required": ["position_id"],
                    "additionalProperties": False,
                },
            },
        }


class get_positions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_id: str = None) -> str:
        positions = data.get("positions", [])
        filtered = [
            p
            for p in positions
            if (not department_id or p.get("department_id") == department_id)
        ]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getPositions",
                "description": "Return a list of all positions, optionally filtered by department_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {
                            "type": "string",
                            "description": "Department ID to filter positions",
                        }
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class get_compensation_records(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        records = data.get("compensation_records", [])
        filtered = [r for r in records if r.get("employee_id") == employee_id]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetCompensationRecords",
                "description": "Return all compensation records for the given employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Employee ID to fetch compensation records for",
                        }
                    },
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


class get_performance_reviews(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        reviews = data.get("performance_reviews", [])
        filtered = [r for r in reviews if r.get("employee_id") == employee_id]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetPerformanceReviews",
                "description": "Return all performance reviews for the given employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Employee ID to fetch performance reviews for",
                        }
                    },
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


class get_leave_records(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        records = data.get("leave_records", [])
        filtered = [r for r in records if r.get("employee_id") == employee_id]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetLeaveRecords",
                "description": "Return all leave records for the given employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Employee ID to fetch leave records for",
                        }
                    },
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


#CREATE APIS
class add_employee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        employees = data.setdefault("employees", [])
        employee = {"employee_id": employee_id}
        employees.append(employee)
        payload = {"success": True, "employee_id": employee_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "addEmployee",
                "description": "Add a new employee record. The employee object must contain all required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee": {
                            "type": "object",
                            "description": "Employee record to add",
                        }
                    },
                    "required": ["employee"],
                    "additionalProperties": False,
                },
            },
        }


class update_employee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str, updates: dict) -> str:
        employees = data.get("employees", [])
        for e in employees:
            if e["employee_id"] == employee_id:
                e.update(updates)
                payload = {"success": True, "employee_id": employee_id}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"employee_id {employee_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmployee",
                "description": "Update an existing employee record with the provided updates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Employee ID to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Fields to update IND the employee record",
                        },
                    },
                    "required": ["employee_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }


class delete_employee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        employees = data.get("employees", [])
        for i, e in enumerate(employees):
            if e["employee_id"] == employee_id:
                del employees[i]
                payload = {"success": True, "employee_id": employee_id}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"employee_id {employee_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "deleteEmployee",
                "description": "Delete the employee record for the given employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Employee ID to delete",
                        }
                    },
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


class add_department(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_id: str) -> str:
        departments = data.setdefault("departments", [])
        department = {"department_id": department_id}
        departments.append(department)
        payload = {"success": True, "department_id": department_id}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "addDepartment",
                "description": "Add a new department record. The department object must contain all required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "object",
                            "description": "Department record to add",
                        }
                    },
                    "required": ["department"],
                    "additionalProperties": False,
                },
            },
        }


class add_position(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], position_id: str = None,
    position: Any = None,
    ) -> str:
        positions = data.setdefault("positions", [])
        position = {"position_id": position_id}
        positions.append(position)
        payload = {"success": True, "position_id": position.get("position_id")}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddPosition",
                "description": "Add a new position record. The position object must contain all required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "position": {
                            "type": "object",
                            "description": "Position record to add",
                        }
                    },
                    "required": ["position"],
                    "additionalProperties": False,
                },
            },
        }


class add_compensation_record(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], compensation_record: dict, position: Any = None) -> str:
        records = data.setdefault("compensation_records", [])
        records.append(compensation_record)
        payload = {
                "success": True,
                "compensation_id": compensation_record.get("compensation_id"),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddCompensationRecord",
                "description": "Add a new compensation record. The compensation_record object must contain all required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "compensation_record": {
                            "type": "object",
                            "description": "Compensation record to add",
                        }
                    },
                    "required": ["compensation_record"],
                    "additionalProperties": False,
                },
            },
        }


class add_performance_review(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], performance_review: dict) -> str:
        reviews = data.setdefault("performance_reviews", [])
        reviews.append(performance_review)
        payload = {"success": True, "review_id": performance_review.get("review_id")}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddPerformanceReview",
                "description": "Add a new performance review record. The performance_review object must contain all required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "performance_review": {
                            "type": "object",
                            "description": "Performance review record to add",
                        }
                    },
                    "required": ["performance_review"],
                    "additionalProperties": False,
                },
            },
        }


class add_leave_record(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], leave_record: dict) -> str:
        records = data.setdefault("leave_records", [])
        records.append(leave_record)
        payload = {"success": True, "leave_id": leave_record.get("leave_id")}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddLeaveRecord",
                "description": "Add a new leave record. The leave_record object must contain all required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "leave_record": {
                            "type": "object",
                            "description": "Leave record to add",
                        }
                    },
                    "required": ["leave_record"],
                    "additionalProperties": False,
                },
            },
        }


TOOLS = [
    get_employee(),
    get_all_employees(),
    get_department(),
    get_departments(),
    get_position(),
    get_positions(),
    get_compensation_records(),
    get_performance_reviews(),
    get_leave_records(),
    add_employee(),
    update_employee(),
    delete_employee(),
    add_department(),
    add_position(),
    add_compensation_record(),
    add_performance_review(),
    add_leave_record(),
]