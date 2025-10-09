import json
from typing import Any

from tau_bench.envs.tool import Tool

#---------------------------------------------------------------------------
#1.  Retrieve an individual employee using their ID  (READ)
#---------------------------------------------------------------------------




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class get_employee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        employees = data.get("employees", {}).values()
        for e in employees.values():
            if e["employee_id"] == employee_id:
                payload = e
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"employee_id {employee_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
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


#---------------------------------------------------------------------------
#2.  Find employees using various filters  (READ)
#---------------------------------------------------------------------------


class search_employees(Tool):
    """
    Executes straightforward AND-style filtering on any top-level employee attributes
    (e.g. {"department_id": "DEPT1001", "status": "Active"}).
    """

    @staticmethod
    def invoke(data: dict[str, Any], filters: dict[str, Any]) -> str:
        employees = data.get("employees", {}).values()
        hits = [e for e in employees.values() if all(e.get(k) == v for k, v in filters.items())]
        payload = {"count": len(hits), "results": hits}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchEmployees",
                "description": "Return employees' full records that match ALL supplied attribute/value pairs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "object",
                            "description": "Key/value pairs to filter on (case-sensitive match)",
                        }
                    },
                    "required": ["filters"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#3.  Establish a new employee entry  (WRITE)
#---------------------------------------------------------------------------


class create_employee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee: dict[str, Any]) -> str:
        new_emp = employee
        if not new_emp:
            payload = {"error": "employee payload required"}
            out = json.dumps(payload, indent=2)
            return out

        employees = data.get("employees", {}).values()
        if any(e["employee_id"] == new_emp["employee_id"] for e in employees.values()):
            payload = {"error": "employee_id already exists"}
            out = json.dumps(payload, indent=2)
            return out

        data["employees"][employee_id] = new_emp
        data["employees"] = employees
        payload = {"success": f'employee {new_emp["employee_id"]} created'}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createEmployee",
                "description": "Insert a completely new employee record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee": {
                            "type": "object",
                            "description": "Full employee JSON object conforming to employees.json schema",
                        }
                    },
                    "required": ["employee"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#4.  Modify changeable employee attributes  (WRITE/PATCH)
#---------------------------------------------------------------------------


class update_employee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str, updates: dict[str, Any]) -> str:
        employees = data.get("employees", {}).values()
        changes = updates

        updated = False
        for e in employees.values():
            if e["employee_id"] == employee_id:
                e.update(changes)
                updated = True
                break

        if not updated:
            payload = {"error": f"employee_id {employee_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        data["employees"] = employees
        payload = {"success": f"employee {employee_id} updated"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmployee",
                "description": "Patch one or more fields on an existing employee record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "updates": {
                            "type": "object",
                            "description": "Dictionary of field:value pairs to update",
                        },
                    },
                    "required": ["employee_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#5.  End or off-board an employee (soft delete)  (WRITE)
#---------------------------------------------------------------------------


class terminate_employee(Tool):
    """
    Designates an employee as terminated by updating status, termination_date,
    and (if desired) removing benefit and compensation associations.
    """

    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str, termination_date: str) -> str:
        employees = data.get("employees", {}).values()

        for e in employees.values():
            if e["employee_id"] == employee_id:
                e["status"] = "Terminated"
                e["termination_date"] = termination_date
                data["employees"] = employees
                payload = {"success": f"employee {employee_id} terminated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"employee_id {employee_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TerminateEmployee",
                "description": "Soft-delete: flag employee as Terminated and record final day.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "termination_date": {
                            "type": "string",
                            "description": "ISO-8601 date of last employment (YYYY-MM-DD)",
                        },
                    },
                    "required": ["employee_id", "termination_date"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#6.  Retrieve metadata for departments  (READ)
#---------------------------------------------------------------------------


class get_department(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_id: str) -> str:
        depts = data.get("departments", {}).values()
        for d in depts.values():
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
        return {
            "type": "function",
            "function": {
                "name": "GetDepartment",
                "description": "Fetch department details by department_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"department_id": {"type": "string"}},
                    "required": ["department_id"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#7.  Display all departments  (READ)
#---------------------------------------------------------------------------


class list_departments(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], departments: list = None) -> str:
        payload = departments if departments is not None else []
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listDepartments",
                "description": "Return every department record.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


#---------------------------------------------------------------------------
#8.  Revise department head, budget, or description  (WRITE)
#---------------------------------------------------------------------------


class update_department(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], department_id: str, updates: dict[str, Any]
    ) -> str:
        depts = data.get("departments", {}).values()
        changes = updates

        for d in depts.values():
            if d["department_id"] == department_id:
                d.update(changes)
                data["departments"] = depts
                payload = {"success": f"department {department_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"department_id {department_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
        pass
        depts = data.get("departments", {}).values()
        changes = updates

        for d in depts.values():
            if d["department_id"] == department_id:
                d.update(changes)
                data["departments"] = depts
                payload = {"success": f"department {department_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"department_id {department_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateDepartment",
                "description": "Patch mutable department attributes (head_id, budget …).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["department_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#9.  Retrieve the current compensation of an employee  (READ)
#---------------------------------------------------------------------------


class get_compensation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        comp = data.get("compensation_records", {}).values()
        latest = [c for c in comp.values() if c["employee_id"] == employee_id]
        latest.sort(key=lambda c: c["effective_date"], reverse=True)
        payload = latest[0] if latest else {"error": "not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCompensation",
                "description": "Return the most recent compensation record for employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#10.  Upsert compensation with a new effective date  (WRITE)
#---------------------------------------------------------------------------


class set_compensation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], compensation: dict[str, Any]) -> str:
        if not compensation:
            payload = {"error": "compensation record required"}
            out = json.dumps(payload, indent=2)
            return out
        comp = data.get("compensation_records", {}).values()
        comp = [
            c for c in comp.values() if c["compensation_id"] != compensation["compensation_id"]
        ]
        data["compensation_records"][compensation["compensation_record_id"]] = compensation
        data["compensation_records"] = comp
        payload = {"success": f'compensation {compensation["compensation_id"]} recorded'}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetCompensation",
                "description": "Insert a new compensation record with all necessary fields (overwrites prior record if compensation_id already exists).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "compensation": {
                            "type": "object",
                            "description": "Full compensation object",
                        }
                    },
                    "required": ["compensation"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#11.  Insert a performance review  (WRITE)
#---------------------------------------------------------------------------


class add_performance_review(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], review: dict[str, Any]) -> str:
        if not review:
            payload = {"error": "review record required"}
            out = json.dumps(payload, indent=2)
            return out
        pr = data.get("performance_reviews", {}).values()
        data["performance_reviews"][review["performance_review_id"]] = review
        data["performance_reviews"] = pr
        payload = {"success": f'review {review["review_id"]} added'}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddPerformanceReview",
                "description": "Append a new performance review record.",
                "parameters": {
                    "type": "object",
                    "properties": {"review": {"type": "object"}},
                    "required": ["review"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#12.  Display reviews associated with an employee  (READ)
#---------------------------------------------------------------------------


class list_performance_reviews(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        pr = [
            r
            for r in data.get("performance_reviews", {}).values()
            if r["employee_id"] == employee_id
        ]
        payload = pr
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListPerformanceReviews",
                "description": "Return all reviews linked to the employee.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#13.  Submit a request for a new leave record  (WRITE)
#---------------------------------------------------------------------------


class request_leave(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], leave: dict[str, Any]) -> str:
        if not leave:
            payload = {"error": "leave record required"}
            out = json.dumps(payload, indent=2)
            return out
        lv = data.get("leave_records", {}).values()
        data["leave_records"][leave["leave_record_id"]] = leave
        data["leave_records"] = lv
        payload = {"success": f'leave {leave["leave_id"]} requested'}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RequestLeave",
                "description": "Insert a leave request; status should start as 'Pending'.",
                "parameters": {
                    "type": "object",
                    "properties": {"leave": {"type": "object"}},
                    "required": ["leave"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#14.  Approve or modify leave status  (WRITE)
#---------------------------------------------------------------------------


class update_leave_status(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], leave_id: str, status: str) -> str:
        lv = data.get("leave_records", {}).values()

        for leave_record in lv.values():
            if leave_record["leave_id"] == leave_id:
                leave_record["status"] = status
                data["leave_records"] = lv
                payload = {"success": f"leave {leave_id} set to {status}"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"leave_id {leave_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateLeaveStatus",
                "description": "Change status of an existing leave record (e.g., Approved, Denied).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "leave_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["leave_id", "status"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#15.  Display leave records for an employee  (READ)
#---------------------------------------------------------------------------


class list_employee_leaves(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        lv = [
            leave_record
            for leave_record in data.get("leave_records", {}).values()
            if leave_record["employee_id"] == employee_id
        ]
        payload = lv
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listEmployeeLeaves",
                "description": "Return all leave records for the employee (any status).",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#16.  Introduce a new benefit plan (e.g., PPO2)  (WRITE)
#---------------------------------------------------------------------------


class add_benefit_plan(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], benefit_plan: dict[str, Any]) -> str:
        if not benefit_plan:
            payload = {"error": "benefit_plan record required"}
            out = json.dumps(payload, indent=2)
            return out
        bp = data.get("benefit_plans", {}).values()
        data["benefit_plans"][benefit_plan_id] = benefit_plan
        data["benefit_plans"] = bp
        payload = {"success": f'benefit_plan {benefit_plan["benefit_plan_id"]} added'}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddBenefitPlan",
                "description": "Create a new benefit plan definition.",
                "parameters": {
                    "type": "object",
                    "properties": {"benefit_plan": {"type": "object"}},
                    "required": ["benefit_plan"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#17.  Modify the attributes of a current benefit plan  (WRITE)
#---------------------------------------------------------------------------


class update_benefit_plan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], benefit_plan_id: str, updates: dict[str, Any]
    ) -> str:
        bp = data.get("benefit_plans", {}).values()

        for p in bp.values():
            if p["benefit_plan_id"] == benefit_plan_id:
                p.update(updates)
                data["benefit_plans"] = bp
                payload = {"success": f"benefit_plan {benefit_plan_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"benefit_plan_id {benefit_plan_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
        pass
        bp = data.get("benefit_plans", {}).values()

        for p in bp.values():
            if p["benefit_plan_id"] == benefit_plan_id:
                p.update(updates)
                data["benefit_plans"] = bp
                payload = {"success": f"benefit_plan {benefit_plan_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"benefit_plan_id {benefit_plan_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateBenefitPlan",
                "description": "Patch fields of an existing benefit plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "benefit_plan_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["benefit_plan_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#18.  Add or remove an employee from a benefit plan list  (WRITE)
#---------------------------------------------------------------------------


class set_employee_benefits(Tool):
    """
    Replaces the benefit_plan_ids array for an employee to precisely align with the
    list provided in `benefit_plan_ids`.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], employee_id: str, benefit_plan_ids: list[str]
    ) -> str:
        employees = data.get("employees", {}).values()

        for e in employees.values():
            if e["employee_id"] == employee_id:
                e["benefit_plan_ids"] = benefit_plan_ids
                data["employees"] = employees
                payload = {"success": f"benefits for {employee_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"employee_id {employee_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
        pass
        employees = data.get("employees", {}).values()

        for e in employees.values():
            if e["employee_id"] == employee_id:
                e["benefit_plan_ids"] = benefit_plan_ids
                data["employees"] = employees
                payload = {"success": f"benefits for {employee_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"employee_id {employee_id} not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetEmployeeBenefits",
                "description": "Replace an employee's benefit_plan_ids array with the supplied list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "benefit_plan_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Array of benefit_plan_id values",
                        },
                    },
                    "required": ["employee_id", "benefit_plan_ids"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#19.  Retrieve an available new employee ID  (READ)
#---------------------------------------------------------------------------


class get_unused_employee_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employees: list[dict[str, Any]] = None) -> str:
        employees = employees if employees is not None else data.get("employees", {}).values()
        used_ids = [e["employee_id"] for e in employees.values()]
        for i in range(10000, 100000):
            if f"E{i:05d}" not in used_ids:
                payload = f"E{i:05d}"
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "no unused employee ID found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUnusedEmployeeId",
                "description": "Return an employee ID that is not currently in use.",
                "parameters": {},
            },
        }


#---------------------------------------------------------------------------
#20.  Look up a position  (READ)
#---------------------------------------------------------------------------


class search_positions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], title: str) -> str:
        positions = data.get("positions", {}).values()
        hits = [p for p in positions.values() if p["title"] == title]
        payload = hits
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchPositions",
                "description": "Return all positions that match the title. If no match, return an empty list.",
                "parameters": {
                    "type": "object",
                    "properties": {"title": {"type": "string"}},
                    "required": ["title"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#21.  Create a leave record for an employee  (WRITE)
#---------------------------------------------------------------------------


class add_leave_record(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], leave: dict[str, Any]) -> str:
        leave_records = data.setdefault("leave_records", [])
        leave_data["leave_records"][leave["leave_record_id"]] = leave
        payload = leave
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddLeaveRecord",
                "description": "Insert a new leave record into leave_records for the specified employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "leave": {
                            "type": "object",
                            "description": "Complete leave record object including leave_id, employee_id, leave_type, start_date, end_date, status, and notes.",
                        }
                    },
                    "required": ["leave"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#22.  Display leave records associated with an employee  (READ)
#---------------------------------------------------------------------------


class list_leave_records(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        leave_records = data.get("leave_records", {}).values()
        hits = [lr for lr in leave_records.values() if lr.get("employee_id") == employee_id]
        payload = {"count": len(hits), "results": hits}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListLeaveRecords",
                "description": "Return all leave records for a given employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Unique ID of the employee whose leave records are requested",
                        }
                    },
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#23.  Update any field(s) in an existing leave record  (WRITE)
#---------------------------------------------------------------------------


class update_leave_record(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], leave_id: str, updates: dict[str, Any]) -> str:
        records = data.get("leave_records", {}).values()
        for rec in records.values():
            if rec["leave_id"] == leave_id:
                rec.update(updates)
                data["leave_records"] = records
                payload = {"success": f"leave {leave_id} updated"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"leave_id {leave_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateLeaveRecord",
                "description": "Patch one or more fields (end_date, status, notes …) on an existing leave record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "leave_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["leave_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#24.  Add or list employee documents – utilize a canonical nested format
#---------------------------------------------------------------------------


class add_employee_document(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], document: dict[str, Any]) -> str:
        container = data.setdefault("employee_documents", [])
        target = next(
            (e for e in container.values() if e["employee_id"] == document["employee_id"]), None
        )
        if target is None:
            target = {
                "employee_id": document["employee_id"],
                "name": "",
                "documents": [],
            }
            data["employee_documents"][target["employee_document_id"]] = target

        target["documents"].append(document)
        payload = {"success": f'doc {document.get("doc_id") or document.get("id")} added'}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddEmployeeDocument",
                "description": "Attach a document object to the employee_documents nested list.",
                "parameters": {
                    "type": "object",
                    "properties": {"document": {"type": "object"}},
                    "required": ["document"],
                    "additionalProperties": False,
                },
            },
        }


class list_employee_documents(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        container = data.get("employee_documents", {}).values()
        target = next((e for e in container.values() if e["employee_id"] == employee_id), None)
        docs = target["documents"] if target else []
        payload = {"count": len(docs), "results": docs}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListEmployeeDocuments",
                "description": "Return the documents array for the specified employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#25.  Insert a bonus payment record  (WRITE)
#---------------------------------------------------------------------------


class add_bonus_payment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], bonus: dict[str, Any]) -> str:
        bonuses = data.setdefault("bonus_payments", [])
        data["bonus_payments"][bonus["bonus_payment_id"]] = bonus
        payload = bonus
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddBonusPayment",
                "description": "Insert a one-time bonus payment record for an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "bonus": {
                            "type": "object",
                            "description": "Complete bonus payment object including bonus_id, employee_id, amount, currency, payment_date, and reason.",
                        }
                    },
                    "required": ["bonus"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#26.  Display bonus payments for an employee  (READ)
#---------------------------------------------------------------------------


class list_bonus_payments(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        bonuses = data.get("bonus_payments", {}).values()
        hits = [b for b in bonuses.values() if b.get("employee_id") == employee_id]
        payload = {"count": len(hits), "results": hits}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListBonusPayments",
                "description": "Return all bonus payments for a given employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Unique ID of the employee whose bonus payments are requested",
                        }
                    },
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#27.  Conditionally add benefits for employees  (WRITE)
#---------------------------------------------------------------------------


class add_employee_benefits_conditionally(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], employee_id: str, benefit_plan_ids: list[str]
    ) -> str:
        # Retrieve the current benefits for employees
        employees = data.get("employees", {}).values()
        employee = next((e for e in employees.values() if e["employee_id"] == employee_id), None)

        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        current_benefits = set(employee.get("benefit_plan_ids", []))
        new_benefits = set(benefit_plan_ids)

        # Add only those benefits that are not currently included
        benefits_to_add = new_benefits - current_benefits
        final_benefits = list(current_benefits | new_benefits)

        # Revise employee benefits
        employee["benefit_plan_ids"] = final_benefits
        payload = {
            "success": f"Benefits updated for employee {employee_id}",
            "current_benefits": list(current_benefits),
            "requested_benefits": benefit_plan_ids,
            "benefits_actually_added": list(benefits_to_add),
            "final_benefits": final_benefits,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        #Retrieve the current benefits for employees
        employees = data.get("employees", {}).values()
        employee = next((e for e in employees.values() if e["employee_id"] == employee_id), None)

        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        current_benefits = set(employee.get("benefit_plan_ids", []))
        new_benefits = set(benefit_plan_ids)

        #Add only those benefits that are not currently included
        benefits_to_add = new_benefits - current_benefits
        final_benefits = list(current_benefits | new_benefits)

        #Revise employee benefits
        employee["benefit_plan_ids"] = final_benefits
        payload = {
                "success": f"Benefits updated for employee {employee_id}",
                "current_benefits": list(current_benefits),
                "requested_benefits": benefit_plan_ids,
                "benefits_actually_added": list(benefits_to_add),
                "final_benefits": final_benefits,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addEmployeeBenefitsConditionally",
                "description": "Add benefit plans to an employee, but only if they don't already have them. Returns details about what was actually added.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Unique ID of the employee",
                        },
                        "benefit_plan_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of benefit plan IDs to add (only new ones will be added)",
                        },
                    },
                    "required": ["employee_id", "benefit_plan_ids"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#28.  Raise employee compensation by a percentage  (WRITE)
#---------------------------------------------------------------------------


class increase_employee_compensation(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        compensation_id: str,
        effective_date: str,
        salary_increase_pct: float | None = None,
        bonus_increase_pct: float | None = None,
        equity_increase_amount: float | None = None
    ) -> str:
        # Retrieve the current compensation
        comp = data.get("compensation_records", {}).values()
        current = [c for c in comp.values() if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            payload = {"error": "No current compensation found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest = current[0]

        # Compute new values
        new_salary = latest["base_salary"]
        new_bonus = latest["bonus_target_pct"]
        new_equity = latest["equity_grant"]

        if salary_increase_pct:
            new_salary = round(latest["base_salary"] * (1 + salary_increase_pct / 100))

        if bonus_increase_pct:
            new_bonus = latest["bonus_target_pct"] + bonus_increase_pct

        if equity_increase_amount:
            new_equity = latest["equity_grant"] + equity_increase_amount

        # Generate a new compensation record
        new_comp = {
            "compensation_id": compensation_id,
            "employee_id": employee_id,
            "base_salary": new_salary,
            "currency": latest["currency"],
            "bonus_target_pct": new_bonus,
            "equity_grant": new_equity,
            "effective_date": effective_date,
        }

        # Delete the old record with the same ID if it exists and insert the new one
        comp = [c for c in comp.values() if c["compensation_id"] != compensation_id]
        data["compensation_records"][new_comp["compensation_record_id"]] = new_comp
        data["compensation_records"] = comp
        payload = {
            "success": f"Compensation increased for {employee_id}",
            "new_compensation": new_comp,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        #Retrieve the current compensation
        comp = data.get("compensation_records", {}).values()
        current = [c for c in comp.values() if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            payload = {"error": "No current compensation found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest = current[0]

        #Compute new values
        new_salary = latest["base_salary"]
        new_bonus = latest["bonus_target_pct"]
        new_equity = latest["equity_grant"]

        if salary_increase_pct:
            new_salary = round(latest["base_salary"] * (1 + salary_increase_pct / 100))

        if bonus_increase_pct:
            new_bonus = latest["bonus_target_pct"] + bonus_increase_pct

        if equity_increase_amount:
            new_equity = latest["equity_grant"] + equity_increase_amount

        #Generate a new compensation record
        new_comp = {
            "compensation_id": compensation_id,
            "employee_id": employee_id,
            "base_salary": new_salary,
            "currency": latest["currency"],
            "bonus_target_pct": new_bonus,
            "equity_grant": new_equity,
            "effective_date": effective_date,
        }

        #Delete the old record with the same ID if it exists and insert the new one
        comp = [c for c in comp.values() if c["compensation_id"] != compensation_id]
        data["compensation_records"][new_comp["compensation_record_id"]] = new_comp
        data["compensation_records"] = comp
        payload = {
                "success": f"Compensation increased for {employee_id}",
                "new_compensation": new_comp,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "IncreaseEmployeeCompensation",
                "description": "Increase employee compensation by percentage or fixed amount based on current values.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "compensation_id": {
                            "type": "string",
                            "description": "New compensation record ID",
                        },
                        "effective_date": {
                            "type": "string",
                            "description": "Effective date for the increase (YYYY-MM-DD)",
                        },
                        "salary_increase_pct": {
                            "type": "number",
                            "description": "Percentage to increase base salary (optional)",
                        },
                        "bonus_increase_pct": {
                            "type": "number",
                            "description": "Percentage points to increase bonus target (optional)",
                        },
                        "equity_increase_amount": {
                            "type": "number",
                            "description": "Fixed amount to add to equity grant (optional)",
                        },
                    },
                    "required": ["employee_id", "compensation_id", "effective_date"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#29.  Modify leave records based on status  (WRITE)
#---------------------------------------------------------------------------


class update_leave_records_by_status(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        current_status: str,
        new_status: str,
        notes: str = ""
    ) -> str:
        leave_records = data.get("leave_records", {}).values()
        updated_count = 0

        for record in leave_records.values():
            if (
                record.get("employee_id") == employee_id
                and record.get("status") == current_status
            ):
                record["status"] = new_status
                if notes:
                    record["notes"] = f"{record.get('notes', '')} {notes}".strip()
                updated_count += 1

        data["leave_records"] = leave_records
        payload = {
            "success": f"Updated {updated_count} leave records from {current_status} to {new_status} for employee {employee_id}"
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        leave_records = data.get("leave_records", {}).values()
        updated_count = 0

        for record in leave_records.values():
            if (
                record.get("employee_id") == employee_id
                and record.get("status") == current_status
            ):
                record["status"] = new_status
                if notes:
                    record["notes"] = f"{record.get('notes', '')} {notes}".strip()
                updated_count += 1

        data["leave_records"] = leave_records
        payload = {
                "success": f"Updated {updated_count} leave records from {current_status} to {new_status} for employee {employee_id}"
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateLeaveRecordsByStatus",
                "description": "Update all leave records for an employee that match a specific status to a new status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "current_status": {
                            "type": "string",
                            "description": "Current status to match (e.g., 'Pending')",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status to set (e.g., 'Approved', 'Cancelled')",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes to append",
                        },
                    },
                    "required": ["employee_id", "current_status", "new_status"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#30.  Increase compensation based on conditions  (WRITE)
#---------------------------------------------------------------------------


class conditional_compensation_increase(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        compensation_id: str,
        effective_date: str,
        condition: str,
        new_bonus_target_pct: float | None = None,
        new_salary: float | None = None,
        new_equity: float | None = None
    ) -> str:
        # Retrieve the current compensation
        comp = data.get("compensation_records", {}).values()
        current = [c for c in comp.values() if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            payload = {"error": "No current compensation found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest = current[0]

        # Analyze and assess the condition
        should_update = False
        if "bonus_target_pct < 18" in condition:
            should_update = latest["bonus_target_pct"] < 18
        elif "base_salary < 75000" in condition:
            should_update = latest["base_salary"] < 75000
        # Include additional conditions as required

        if not should_update:
            payload = {
                    "success": f"Condition '{condition}' not met, no compensation change for {employee_id}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Generate a new compensation record with the revised values
        new_comp = {
            "compensation_id": compensation_id,
            "employee_id": employee_id,
            "base_salary": (
                new_salary if new_salary is not None else latest["base_salary"]
            ),
            "currency": latest["currency"],
            "bonus_target_pct": (
                new_bonus_target_pct
                if new_bonus_target_pct is not None
                else latest["bonus_target_pct"]
            ),
            "equity_grant": (
                new_equity if new_equity is not None else latest["equity_grant"]
            ),
            "effective_date": effective_date,
        }

        # Delete the previous record with the same ID if it exists and insert the new one
        comp = [c for c in comp.values() if c["compensation_id"] != compensation_id]
        data["compensation_records"][new_comp["compensation_record_id"]] = new_comp
        data["compensation_records"] = comp
        payload = {
                "success": f"Compensation updated for {employee_id} based on condition '{condition}'",
                "new_compensation": new_comp,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        #Retrieve the current compensation
        comp = data.get("compensation_records", {}).values()
        current = [c for c in comp.values() if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            payload = {"error": "No current compensation found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest = current[0]

        #Analyze and assess the condition
        should_update = False
        if "bonus_target_pct < 18" in condition:
            should_update = latest["bonus_target_pct"] < 18
        elif "base_salary < 75000" in condition:
            should_update = latest["base_salary"] < 75000
        #Include additional conditions as required

        if not should_update:
            payload = {
                    "success": f"Condition '{condition}' not met, no compensation change for {employee_id}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Generate a new compensation record with the revised values
        new_comp = {
            "compensation_id": compensation_id,
            "employee_id": employee_id,
            "base_salary": (
                new_salary if new_salary is not None else latest["base_salary"]
            ),
            "currency": latest["currency"],
            "bonus_target_pct": (
                new_bonus_target_pct
                if new_bonus_target_pct is not None
                else latest["bonus_target_pct"]
            ),
            "equity_grant": (
                new_equity if new_equity is not None else latest["equity_grant"]
            ),
            "effective_date": effective_date,
        }

        #Delete the previous record with the same ID if it exists and insert the new one
        comp = [c for c in comp.values() if c["compensation_id"] != compensation_id]
        data["compensation_records"][new_comp["compensation_record_id"]] = new_comp
        data["compensation_records"] = comp
        payload = {
                "success": f"Compensation updated for {employee_id} based on condition '{condition}'",
                "new_compensation": new_comp,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConditionalCompensationIncrease",
                "description": "Update employee compensation only if a specified condition is met.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "compensation_id": {"type": "string"},
                        "effective_date": {
                            "type": "string",
                            "description": "Effective date (YYYY-MM-DD)",
                        },
                        "condition": {
                            "type": "string",
                            "description": "Condition to check (e.g., 'bonus_target_pct < 18')",
                        },
                        "new_bonus_target_pct": {
                            "type": "number",
                            "description": "New bonus target percentage (optional)",
                        },
                        "new_salary": {
                            "type": "number",
                            "description": "New base salary (optional)",
                        },
                        "new_equity": {
                            "type": "number",
                            "description": "New equity grant (optional)",
                        },
                    },
                    "required": [
                        "employee_id",
                        "compensation_id",
                        "effective_date",
                        "condition",
                    ],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#31.  Insert employee benefit if it is absent  (WRITE)
#---------------------------------------------------------------------------


class add_employee_benefit_if_missing(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        benefit_plan_id: str,
        current_benefit_plan_ids: list[str]
    ) -> str:
        employees = data.get("employees", {}).values()
        employee = next((e for e in employees.values() if e["employee_id"] == employee_id), None)

        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        current_benefits = set(employee.get("benefit_plan_ids", []))

        if benefit_plan_id in current_benefits:
            payload = {
                "success": f"Employee {employee_id} already has benefit {benefit_plan_id}, no change needed"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Insert the benefit that is missing
        new_benefits = list(current_benefits)
        new_benefits.append(benefit_plan_id)
        employee["benefit_plan_ids"] = new_benefits
        payload = {
            "success": f"Benefit {benefit_plan_id} added to employee {employee_id}",
            "previous_benefits": list(current_benefits),
            "new_benefits": new_benefits,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        employees = data.get("employees", {}).values()
        employee = next((e for e in employees.values() if e["employee_id"] == employee_id), None)

        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        current_benefits = set(employee.get("benefit_plan_ids", []))

        if benefit_plan_id in current_benefits:
            payload = {
                    "success": f"Employee {employee_id} already has benefit {benefit_plan_id}, no change needed"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Insert the benefit that is missing
        new_benefits = list(current_benefits)
        new_benefits.append(benefit_plan_id)
        employee["benefit_plan_ids"] = new_benefits
        payload = {
                "success": f"Benefit {benefit_plan_id} added to employee {employee_id}",
                "previous_benefits": list(current_benefits),
                "new_benefits": new_benefits,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddEmployeeBenefitIfMissing",
                "description": "Add a benefit plan to an employee only if they don't already have it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "benefit_plan_id": {
                            "type": "string",
                            "description": "Benefit plan ID to add",
                        },
                        "current_benefit_plan_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Known current benefit plan IDs (for reference)",
                        },
                    },
                    "required": [
                        "employee_id",
                        "benefit_plan_id",
                        "current_benefit_plan_ids",
                    ],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#32.  Verify and update compensation based on conditions  (WRITE)
#---------------------------------------------------------------------------


class conditional_compensation_check_and_update(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        compensation_id: str,
        effective_date: str,
        salary_threshold: float | None = None,
        target_salary: float | None = None,
        bonus_threshold: float | None = None,
        target_bonus: float | None = None
    ) -> str:
        # Retrieve the current compensation
        comp = data.get("compensation_records", {}).values()
        current = [c for c in comp.values() if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            payload = {"error": "No current compensation found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest = current[0]
        changes_made = []

        # Begin with the existing values
        new_salary = latest["base_salary"]
        new_bonus = latest["bonus_target_pct"]

        # Evaluate the salary condition
        if salary_threshold is not None and target_salary is not None:
            if latest["base_salary"] < salary_threshold:
                new_salary = target_salary
                changes_made.append(
                    f"salary increased from {latest['base_salary']} to {target_salary}"
                )
            else:
                changes_made.append(
                    f"salary {latest['base_salary']} already above threshold {salary_threshold}"
                )

        # Evaluate the bonus condition
        if bonus_threshold is not None and target_bonus is not None:
            if latest["bonus_target_pct"] < bonus_threshold:
                new_bonus = target_bonus
                changes_made.append(
                    f"bonus increased from {latest['bonus_target_pct']}% to {target_bonus}%"
                )
            else:
                changes_made.append(
                    f"bonus {latest['bonus_target_pct']}% already above threshold {bonus_threshold}%"
                )

        # Generate a new record only if modifications occurred
        if (
            new_salary != latest["base_salary"]
            or new_bonus != latest["bonus_target_pct"]
        ):
            new_comp = {
                "compensation_id": compensation_id,
                "employee_id": employee_id,
                "base_salary": new_salary,
                "currency": latest["currency"],
                "bonus_target_pct": new_bonus,
                "equity_grant": latest["equity_grant"],
                "effective_date": effective_date,
            }

            # Delete the previous record with the same ID if it exists and insert the new one
            comp = [c for c in comp.values() if c["compensation_id"] != compensation_id]
            data["compensation_records"][new_comp["compensation_record_id"]] = new_comp
            data["compensation_records"] = comp
            payload = {
                    "success": f"Compensation updated for {employee_id}",
                    "changes": changes_made,
                    "new_compensation": new_comp,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                    "success": f"No compensation changes needed for {employee_id}",
                    "analysis": changes_made,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        pass
        #Retrieve the current compensation
        comp = data.get("compensation_records", {}).values()
        current = [c for c in comp.values() if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            payload = {"error": "No current compensation found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest = current[0]
        changes_made = []

        #Begin with the existing values
        new_salary = latest["base_salary"]
        new_bonus = latest["bonus_target_pct"]

        #Evaluate the salary condition
        if salary_threshold is not None and target_salary is not None:
            if latest["base_salary"] < salary_threshold:
                new_salary = target_salary
                changes_made.append(
                    f"salary increased from {latest['base_salary']} to {target_salary}"
                )
            else:
                changes_made.append(
                    f"salary {latest['base_salary']} already above threshold {salary_threshold}"
                )

        #Evaluate the bonus condition
        if bonus_threshold is not None and target_bonus is not None:
            if latest["bonus_target_pct"] < bonus_threshold:
                new_bonus = target_bonus
                changes_made.append(
                    f"bonus increased from {latest['bonus_target_pct']}% to {target_bonus}%"
                )
            else:
                changes_made.append(
                    f"bonus {latest['bonus_target_pct']}% already above threshold {bonus_threshold}%"
                )

        #Generate a new record only if modifications occurred
        if (
            new_salary != latest["base_salary"]
            or new_bonus != latest["bonus_target_pct"]
        ):
            new_comp = {
                "compensation_id": compensation_id,
                "employee_id": employee_id,
                "base_salary": new_salary,
                "currency": latest["currency"],
                "bonus_target_pct": new_bonus,
                "equity_grant": latest["equity_grant"],
                "effective_date": effective_date,
            }

            #Delete the previous record with the same ID if it exists and insert the new one
            comp = [c for c in comp.values() if c["compensation_id"] != compensation_id]
            data["compensation_records"][new_comp["compensation_record_id"]] = new_comp
            data["compensation_records"] = comp
            payload = {
                    "success": f"Compensation updated for {employee_id}",
                    "changes": changes_made,
                    "new_compensation": new_comp,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                    "success": f"No compensation changes needed for {employee_id}",
                    "analysis": changes_made,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConditionalCompensationCheckAndUpdate",
                "description": "Check employee compensation against thresholds and update only if below thresholds.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "compensation_id": {"type": "string"},
                        "effective_date": {
                            "type": "string",
                            "description": "Effective date (YYYY-MM-DD)",
                        },
                        "salary_threshold": {
                            "type": "number",
                            "description": "Minimum salary threshold to check against",
                        },
                        "target_salary": {
                            "type": "number",
                            "description": "Target salary if below threshold",
                        },
                        "bonus_threshold": {
                            "type": "number",
                            "description": "Minimum bonus percentage threshold to check against",
                        },
                        "target_bonus": {
                            "type": "number",
                            "description": "Target bonus percentage if below threshold",
                        },
                    },
                    "required": ["employee_id", "compensation_id", "effective_date"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#33.  Update employee level conditionally based on performance  (WRITE)
#---------------------------------------------------------------------------


class conditional_level_update(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], employee_id: str, required_rating: str, new_level: str
    ) -> str:
        # Retrieve performance reviews
        reviews = data.get("performance_reviews", {}).values()
        employee_reviews = [r for r in reviews.values() if r["employee_id"] == employee_id]
        employee_reviews.sort(key=lambda r: r["period_end"], reverse=True)

        if not employee_reviews:
            payload = {"error": "No performance reviews found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest_review = employee_reviews[0]
        current_rating = latest_review.get("rating", "")

        if current_rating == required_rating:
            # Revise the level
            employees = data.get("employees", {}).values()
            for e in employees.values():
                if e["employee_id"] == employee_id:
                    old_level = e.get("level_id", "")
                    e["level_id"] = new_level
                    data["employees"] = employees
                    payload = {
                        "success": f"Employee {employee_id} level updated from {old_level} to {new_level}",
                        "condition_met": f"Performance rating '{current_rating}' matches required '{required_rating}'",
                    }
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        else:
            payload = {
                "success": f"Level update skipped for employee {employee_id}",
                "condition_not_met": f"Performance rating '{current_rating}' does not match required '{required_rating}'",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        pass
        #Retrieve performance reviews
        reviews = data.get("performance_reviews", {}).values()
        employee_reviews = [r for r in reviews.values() if r["employee_id"] == employee_id]
        employee_reviews.sort(key=lambda r: r["period_end"], reverse=True)

        if not employee_reviews:
            payload = {"error": "No performance reviews found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest_review = employee_reviews[0]
        current_rating = latest_review.get("rating", "")

        if current_rating == required_rating:
            #Revise the level
            employees = data.get("employees", {}).values()
            for e in employees.values():
                if e["employee_id"] == employee_id:
                    old_level = e.get("level_id", "")
                    e["level_id"] = new_level
                    data["employees"] = employees
                    payload = {
                            "success": f"Employee {employee_id} level updated from {old_level} to {new_level}",
                            "condition_met": f"Performance rating '{current_rating}' matches required '{required_rating}'",
                        }
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        else:
            payload = {
                    "success": f"Level update skipped for employee {employee_id}",
                    "condition_not_met": f"Performance rating '{current_rating}' does not match required '{required_rating}'",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConditionalLevelUpdate",
                "description": "Update employee level only if their latest performance rating matches the required rating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "required_rating": {
                            "type": "string",
                            "description": "Required performance rating (e.g., 'Exceeds')",
                        },
                        "new_level": {
                            "type": "string",
                            "description": "New level to assign if condition is met",
                        },
                    },
                    "required": ["employee_id", "required_rating", "new_level"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#34.  Maintain benefits conditionally based on equity  (WRITE)
#---------------------------------------------------------------------------


class conditional_benefit_maintenance(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        equity_threshold: float,
        maintain_benefits: list[str],
        reduced_benefits: list[str]
    ) -> str:
        # Retrieve the current compensation
        comp = data.get("compensation_records", {}).values()
        current = [c for c in comp.values() if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            payload = {"error": "No current compensation found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest = current[0]
        current_equity = latest.get("equity_grant", 0)

        employees = data.get("employees", {}).values()
        employee = next((e for e in employees.values() if e["employee_id"] == employee_id), None)

        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        if current_equity > equity_threshold:
            # Ensure full benefits are maintained
            employee["benefit_plan_ids"] = maintain_benefits
            action_taken = "Benefits maintained due to high equity"
            final_benefits = maintain_benefits
        else:
            # Diminish benefits while on leave
            employee["benefit_plan_ids"] = reduced_benefits
            action_taken = "Benefits reduced during leave due to lower equity"
            final_benefits = reduced_benefits

        data["employees"] = employees
        payload = {
                "success": f"Benefit maintenance decision made for employee {employee_id}",
                "equity_amount": current_equity,
                "equity_threshold": equity_threshold,
                "condition_met": current_equity > equity_threshold,
                "action_taken": action_taken,
                "final_benefits": final_benefits,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        #Retrieve the current compensation
        comp = data.get("compensation_records", {}).values()
        current = [c for c in comp.values() if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            payload = {"error": "No current compensation found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest = current[0]
        current_equity = latest.get("equity_grant", 0)

        employees = data.get("employees", {}).values()
        employee = next((e for e in employees.values() if e["employee_id"] == employee_id), None)

        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        if current_equity > equity_threshold:
            #Ensure full benefits are maintained
            employee["benefit_plan_ids"] = maintain_benefits
            action_taken = "Benefits maintained due to high equity"
            final_benefits = maintain_benefits
        else:
            #Diminish benefits while on leave
            employee["benefit_plan_ids"] = reduced_benefits
            action_taken = "Benefits reduced during leave due to lower equity"
            final_benefits = reduced_benefits

        data["employees"] = employees
        payload = {
                "success": f"Benefit maintenance decision made for employee {employee_id}",
                "equity_amount": current_equity,
                "equity_threshold": equity_threshold,
                "condition_met": current_equity > equity_threshold,
                "action_taken": action_taken,
                "final_benefits": final_benefits,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConditionalBenefitMaintenance",
                "description": "Maintain or reduce employee benefits based on equity threshold during leave.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "equity_threshold": {
                            "type": "number",
                            "description": "Equity threshold for benefit maintenance",
                        },
                        "maintain_benefits": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Benefits to maintain if equity is above threshold",
                        },
                        "reduced_benefits": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Reduced benefits if equity is below threshold",
                        },
                    },
                    "required": [
                        "employee_id",
                        "equity_threshold",
                        "maintain_benefits",
                        "reduced_benefits",
                    ],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#35.  Adjust sabbatical compensation conditionally based on level  (WRITE)
#---------------------------------------------------------------------------


class conditional_sabbatical_compensation(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        level_threshold: str,
        paid_leave_type: str,
        unpaid_leave_type: str
    ) -> str:
        employees = data.get("employees", {}).values()
        employee = next((e for e in employees.values() if e["employee_id"] == employee_id), None)

        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        current_level = employee.get("level_id", "")

        # Basic level comparison (assuming L.1, L.2, L.3, L.4, L.5 structure)
        def level_to_number(level_str):
            try:
                return float(level_str.replace("L.", ""))
            except:
                return 0

        current_level_num = level_to_number(current_level)
        threshold_level_num = level_to_number(level_threshold)

        if current_level_num >= threshold_level_num:
            # Keep full compensation during paid sabbatical
            leave_type = paid_leave_type
            compensation_maintained = True
            action_taken = f"Paid sabbatical approved - level {current_level} meets threshold {level_threshold}"
        else:
            # Diminish compensation during unpaid sabbatical
            leave_type = unpaid_leave_type
            compensation_maintained = False
            action_taken = f"Unpaid sabbatical approved - level {current_level} below threshold {level_threshold}"

        payload = {
            "success": f"Sabbatical compensation decision made for employee {employee_id}",
            "current_level": current_level,
            "level_threshold": level_threshold,
            "condition_met": current_level_num >= threshold_level_num,
            "leave_type": leave_type,
            "compensation_maintained": compensation_maintained,
            "action_taken": action_taken,
        }
        out = json.dumps(payload, indent=2)
        return out
        pass
        employees = data.get("employees", {}).values()
        employee = next((e for e in employees.values() if e["employee_id"] == employee_id), None)

        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        current_level = employee.get("level_id", "")

        #Basic level comparison (assuming L.1, L.2, L.3, L.4, L.5 structure)
        def level_to_number(level_str):
            pass
            try:
                return float(level_str.replace("L.", ""))
            except:
                return 0

        current_level_num = level_to_number(current_level)
        threshold_level_num = level_to_number(level_threshold)

        if current_level_num >= threshold_level_num:
            #Keep full compensation during paid sabbatical
            leave_type = paid_leave_type
            compensation_maintained = True
            action_taken = f"Paid sabbatical approved - level {current_level} meets threshold {level_threshold}"
        else:
            #Diminish compensation during unpaid sabbatical
            leave_type = unpaid_leave_type
            compensation_maintained = False
            action_taken = f"Unpaid sabbatical approved - level {current_level} below threshold {level_threshold}"
        payload = {
                "success": f"Sabbatical compensation decision made for employee {employee_id}",
                "current_level": current_level,
                "level_threshold": level_threshold,
                "condition_met": current_level_num >= threshold_level_num,
                "leave_type": leave_type,
                "compensation_maintained": compensation_maintained,
                "action_taken": action_taken,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConditionalSabbaticalCompensation",
                "description": "Determine sabbatical compensation based on employee level threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "level_threshold": {
                            "type": "string",
                            "description": "Minimum level for paid sabbatical (e.g., 'L.3')",
                        },
                        "paid_leave_type": {
                            "type": "string",
                            "description": "Leave type if level meets threshold",
                        },
                        "unpaid_leave_type": {
                            "type": "string",
                            "description": "Leave type if level below threshold",
                        },
                    },
                    "required": [
                        "employee_id",
                        "level_threshold",
                        "paid_leave_type",
                        "unpaid_leave_type",
                    ],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#36.  Normalize bonus target to default conditionally  (WRITE)
#---------------------------------------------------------------------------


class conditional_bonus_target_normalization(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        compensation_id: str,
        effective_date: str,
        target_bonus_pct: float
    ) -> str:
        # Retrieve the current compensation
        comp = data.get("compensation_records", {}).values()
        current = [c for c in comp.values() if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            payload = {"error": "No current compensation found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest = current[0]
        current_bonus = latest.get("bonus_target_pct", 0)

        if current_bonus < target_bonus_pct:
            # Revise bonus target to align with default
            new_comp = {
                "compensation_id": compensation_id,
                "employee_id": employee_id,
                "base_salary": latest["base_salary"],
                "currency": latest["currency"],
                "bonus_target_pct": target_bonus_pct,
                "equity_grant": latest["equity_grant"],
                "effective_date": effective_date,
            }

            # Delete the previous record with the same ID if it exists and insert the new one
            comp = [c for c in comp.values() if c["compensation_id"] != compensation_id]
            data["compensation_records"][new_comp["compensation_record_id"]] = new_comp
            data["compensation_records"] = comp
            payload = {
                "success": f"Bonus target normalized for employee {employee_id}",
                "previous_bonus": current_bonus,
                "new_bonus": target_bonus_pct,
                "action_taken": f"Bonus increased from {current_bonus}% to {target_bonus_pct}%",
                "new_compensation": new_comp,
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                "success": f"Bonus target normalization skipped for employee {employee_id}",
                "current_bonus": current_bonus,
                "target_bonus": target_bonus_pct,
                "action_taken": f"Bonus {current_bonus}% already at or above target {target_bonus_pct}%",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        pass
        #Retrieve the current compensation
        comp = data.get("compensation_records", {}).values()
        current = [c for c in comp.values() if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            payload = {"error": "No current compensation found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest = current[0]
        current_bonus = latest.get("bonus_target_pct", 0)

        if current_bonus < target_bonus_pct:
            #Revise bonus target to align with default
            new_comp = {
                "compensation_id": compensation_id,
                "employee_id": employee_id,
                "base_salary": latest["base_salary"],
                "currency": latest["currency"],
                "bonus_target_pct": target_bonus_pct,
                "equity_grant": latest["equity_grant"],
                "effective_date": effective_date,
            }

            #Delete the previous record with the same ID if it exists and insert the new one
            comp = [c for c in comp.values() if c["compensation_id"] != compensation_id]
            data["compensation_records"][new_comp["compensation_record_id"]] = new_comp
            data["compensation_records"] = comp
            payload = {
                    "success": f"Bonus target normalized for employee {employee_id}",
                    "previous_bonus": current_bonus,
                    "new_bonus": target_bonus_pct,
                    "action_taken": f"Bonus increased from {current_bonus}% to {target_bonus_pct}%",
                    "new_compensation": new_comp,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                    "success": f"Bonus target normalization skipped for employee {employee_id}",
                    "current_bonus": current_bonus,
                    "target_bonus": target_bonus_pct,
                    "action_taken": f"Bonus {current_bonus}% already at or above target {target_bonus_pct}%",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConditionalBonusTargetNormalization",
                "description": "Normalize employee bonus target to default level only if current bonus is below target.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "compensation_id": {"type": "string"},
                        "effective_date": {
                            "type": "string",
                            "description": "Effective date (YYYY-MM-DD)",
                        },
                        "target_bonus_pct": {
                            "type": "number",
                            "description": "Target bonus percentage for normalization",
                        },
                    },
                    "required": [
                        "employee_id",
                        "compensation_id",
                        "effective_date",
                        "target_bonus_pct",
                    ],
                    "additionalProperties": False,
                },
            },
        }


TOOLS = [
    get_employee(),
    search_employees(),
    create_employee(),
    update_employee(),
    terminate_employee(),
    get_department(),
    list_departments(),
    update_department(),
    get_compensation(),
    set_compensation(),
    add_performance_review(),
    list_performance_reviews(),
    request_leave(),
    update_leave_status(),
    list_employee_leaves(),
    add_benefit_plan(),
    update_benefit_plan(),
    set_employee_benefits(),
    get_unused_employee_id(),
    search_positions(),
    add_leave_record(),
    list_leave_records(),
    update_leave_record(),
    add_employee_document(),
    list_employee_documents(),
    add_bonus_payment(),
    list_bonus_payments(),
    add_employee_benefits_conditionally(),
    increase_employee_compensation(),
    update_leave_records_by_status(),
    conditional_compensation_increase(),
    add_employee_benefit_if_missing(),
    conditional_compensation_check_and_update(),
    conditional_level_update(),
    conditional_benefit_maintenance(),
    conditional_sabbatical_compensation(),
    conditional_bonus_target_normalization(),
]
