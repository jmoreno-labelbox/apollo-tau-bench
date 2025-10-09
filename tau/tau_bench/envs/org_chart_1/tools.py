import json
from typing import Any

from tau_bench.envs.tool import Tool

#---------------------------------------------------------------------------
#1.  Retrieve a specific employee using their ID  (READ)
#---------------------------------------------------------------------------


class get_employee_by_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
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
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeById",
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


class find_employees(Tool):
    """
    Executes basic AND-style filtering on any primary employee attributes
    (e.g. {"department_id": "DEPT1001", "status": "Active"}).
    """

    @staticmethod
    def invoke(data: dict[str, Any], filters: dict[str, Any]) -> str:
        employees = data.get("employees", [])
        hits = [e for e in employees if all(e.get(k) == v for k, v in filters.items())]
        payload = {"count": len(hits), "results": hits}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindEmployees",
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
#3.  Add a new employee entry  (WRITE)
#---------------------------------------------------------------------------


class create_new_employee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee: dict[str, Any]) -> str:
        new_emp = employee
        if not new_emp:
            payload = {"error": "employee payload required"}
            out = json.dumps(payload, indent=2)
            return out

        employees = data.get("employees", [])
        if any(e["employee_id"] == new_emp["employee_id"] for e in employees):
            payload = {"error": "employee_id already exists"}
            out = json.dumps(payload, indent=2)
            return out

        employees.append(new_emp)
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
                "name": "CreateNewEmployee",
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


class update_employee_record(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str, updates: dict[str, Any]) -> str:
        employees = data.get("employees", [])
        changes = updates

        updated = False
        for e in employees:
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
                "name": "UpdateEmployeeRecord",
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
#5.  End employment / off-board employee (soft delete)  (WRITE)
#---------------------------------------------------------------------------


class terminate_employee(Tool):
    """
    Designates an employee as terminated by updating status, termination_date,
    and (if desired) removing benefit and compensation associations.
    """

    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str, termination_date: str = None) -> str:
        employees = data.get("employees", [])

        for e in employees:
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
#6.  Retrieve department information  (READ)
#---------------------------------------------------------------------------


class get_department_by_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_id: str = None) -> str:
        depts = data.get("departments", [])
        for d in depts:
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
                "name": "GetDepartmentById",
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
        payload = departments if departments is not None else data.get("departments", [])
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListDepartments",
                "description": "Return every department record.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


#---------------------------------------------------------------------------
#8.  Modify department leader, budget, or details  (WRITE)
#---------------------------------------------------------------------------


class update_department_record(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], department_id: str, updates: dict[str, Any]
    ) -> str:
        depts = data.get("departments", [])
        changes = updates

        for d in depts:
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
        depts = data.get("departments", [])
        changes = updates

        for d in depts:
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
                "name": "UpdateDepartmentRecord",
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
#9.  Retrieve the current salary of an employee  (READ)
#---------------------------------------------------------------------------


class get_compensation_by_employee_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        comp = data.get("compensation_records", [])
        latest = [c for c in comp if c["employee_id"] == employee_id]
        latest.sort(key=lambda c: c["effective_date"], reverse=True)
        payload = latest[0] if latest else {"error": "not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCompensationByEmployeeId",
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
#10.  Insert or update compensation (new effective date)  (WRITE)
#---------------------------------------------------------------------------


class set_compensation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], compensation: dict[str, Any]) -> str:
        if not compensation:
            payload = {"error": "compensation record required"}
            out = json.dumps(payload, indent=2)
            return out
        comp = data.get("compensation_records", [])
        comp = [
            c for c in comp if c["compensation_id"] != compensation["compensation_id"]
        ]
        comp.append(compensation)
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
#11.  Submit a performance evaluation  (WRITE)
#---------------------------------------------------------------------------


class create_performance_review(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], review: dict[str, Any]) -> str:
        if not review:
            payload = {"error": "review record required"}
            out = json.dumps(payload, indent=2)
            return out
        pr = data.get("performance_reviews", [])
        pr.append(review)
        data["performance_reviews"] = pr
        payload = {"success": f'review {review["review_id"]} added'}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePerformanceReview",
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
#12.  Display evaluations for an employee  (READ)
#---------------------------------------------------------------------------


class get_performance_reviews_by_employee_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        pr = [
            r
            for r in data.get("performance_reviews", [])
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
                "name": "GetPerformanceReviewsByEmployeeId",
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


class create_leave_record(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], leave: dict[str, Any]) -> str:
        if not leave:
            payload = {"error": "leave record required"}
            out = json.dumps(payload, indent=2)
            return out
        lv = data.get("leave_records", [])
        lv.append(leave)
        data["leave_records"] = lv
        payload = {"success": f'leave {leave["leave_id"]} requested'}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateLeaveRecord",
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
#14.  Confirm or modify leave status  (WRITE)
#---------------------------------------------------------------------------


class update_leave_status(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], leave_id: str, status: str = None) -> str:
        lv = data.get("leave_records", [])

        for leave_record in lv:
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
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        lv = [
            leave_record
            for leave_record in data.get("leave_records", [])
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
                "name": "ListEmployeeLeaves",
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
#16.  Introduce a new benefits plan (e.g., PPO2)  (WRITE)
#---------------------------------------------------------------------------


class create_benefit_plan(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], benefit_plan: dict[str, Any]) -> str:
        if not benefit_plan:
            payload = {"error": "benefit_plan record required"}
            out = json.dumps(payload, indent=2)
            return out
        bp = data.get("benefits_plan", [])
        bp.append(benefit_plan)
        data["benefits_plan"] = bp
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
                "name": "CreateBenefitPlan",
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
#17.  Modify properties of a current benefits plan  (WRITE)
#---------------------------------------------------------------------------


class update_benefit_plan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], benefit_plan_id: str, updates: dict[str, Any]
    ) -> str:
        bp = data.get("benefits_plan", [])

        for p in bp:
            if p["benefit_plan_id"] == benefit_plan_id:
                p.update(updates)
                data["benefits_plan"] = bp
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
        bp = data.get("benefits_plan", [])

        for p in bp:
            if p["benefit_plan_id"] == benefit_plan_id:
                p.update(updates)
                data["benefits_plan"] = bp
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
                "name": "UpdateBenefitPlan",
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
#18.  Add or remove an employee from a benefits plan list  (WRITE)
#---------------------------------------------------------------------------


class set_employee_benefits(Tool):
    """
    Replaces the benefit_plan_ids array for an employee to precisely align with the
    list provided in `benefit_plan_ids`.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], employee_id: str, benefit_plan_ids: list[str]
     = None) -> str:
        employees = data.get("employees", [])

        for e in employees:
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
        employees = data.get("employees", [])

        for e in employees:
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


class get_new_employee_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        employees = data.get("employees", [])
        used_ids = [e["employee_id"] for e in employees]
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
                "name": "GetNewEmployeeId",
                "description": "Return an employee ID that is not currently in use.",
                "parameters": {},
            },
        }


#---------------------------------------------------------------------------
#20.  Look up position  (READ)
#---------------------------------------------------------------------------


class search_positions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], title: str = None) -> str:
        positions = data.get("positions", [])
        hits = [p for p in positions if p["title"] == title]
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


class get_new_compensation_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], compensations: list[dict[str, Any]] = None) -> str:
        compensations = compensations if compensations is not None else []
        prefix = "COMP"
        start_num = 10000

        if not compensations:
            payload = f"{prefix}{start_num}"
            out = json.dumps(payload, indent=2)
            return out

        max_id_num = 0
        for comp in compensations:
            comp_id = comp.get("compensation_id", "")
            if comp_id.startswith(prefix):
                try:
                    num = int(comp_id[len(prefix):])
                    if num > max_id_num:
                        max_id_num = num
                except (ValueError, TypeError):
                    continue

        next_id = f"{prefix}{max(start_num, max_id_num) + 1}"
        payload = next_id
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNewCompensationId",
                "description": "Return a compensation ID that is not currently in use.",
                "parameters": {},
            },
        }


class get_new_review_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], reviews: list[dict[str, Any]] = None) -> str:
        reviews = reviews if reviews is not None else []
        prefix = "PR"
        start_num = 10000

        if not reviews:
            payload = f"{prefix}{start_num}"
            out = json.dumps(payload, indent=2)
            return out

        max_id_num = 0
        for review in reviews:
            review_id = review.get("review_id", "")
            if review_id.startswith(prefix):
                try:
                    num = int(review_id[len(prefix) :])
                    if num > max_id_num:
                        max_id_num = num
                except (ValueError, TypeError):
                    continue

        next_id = f"{prefix}{max(start_num, max_id_num) + 1}"
        payload = next_id
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNewReviewId",
                "description": "Return a performance review ID that is not currently in use.",
                "parameters": {},
            },
        }


class get_employee_by_ids_by_region(Tool):
    REGION_MAP: dict[str, set[str]] = {
        "EU": {
            "AT",
            "BE",
            "BG",
            "HR",
            "CY",
            "CZ",
            "DK",
            "EE",
            "FI",
            "FR",
            "DE",
            "GR",
            "HU",
            "IE",
            "IT",
            "LV",
            "LT",
            "LU",
            "MT",
            "NL",
            "PL",
            "PT",
            "RO",
            "SK",
            "SI",
            "ESP",
            "SE",
        }
    }

    @staticmethod
    def invoke(data: dict[str, Any], region: str = None, status: str = "Active") -> str:
        if not region or region not in get_employee_by_ids_by_region.REGION_MAP:
            payload = {"error": f"Invalid or unsupported region: {region}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        employees = data.get("employees", [])
        target_nationalities = get_employee_by_ids_by_region.REGION_MAP[region]

        found_employees = [
            emp
            for emp in employees
            if emp.get("nationality") in target_nationalities
            and emp.get("status") == status
        ]
        payload = found_employees
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getEmployeeByIdsByRegion",
                "description": "Retrieves a list of employees belonging to a specific geographical or political region (e.g., EU).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "region": {
                            "type": "string",
                            "description": "The geographical or political region to search for.",
                            "enum": ["EU"],
                        },
                        "status": {
                            "type": "string",
                            "description": "The employment status to filter by. Defaults to 'Active'.",
                        },
                    },
                    "required": ["region"],
                },
            },
        }


class get_new_leave_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        leaves = data.get("leaves", [])
        prefix = "LV"
        start_num = 10000

        if not leaves:
            payload = f"{prefix}{start_num}"
            out = json.dumps(payload, indent=2)
            return out

        max_id_num = 0
        for leave in leaves:
            leave_id = leave.get("leave_id", "")
            if leave_id.startswith(prefix):
                try:
                    num = int(leave_id[len(prefix) :])
                    if num > max_id_num:
                        max_id_num = num
                except (ValueError, TypeError):
                    continue

        next_id_num = max(start_num, max_id_num) + 1
        payload = f"{prefix}{next_id_num}"
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNewLeaveId",
                "description": "Return a leave ID that is not currently in use.",
                "parameters": {},
            },
        }


TOOLS = [
    get_employee_by_id(),
    find_employees(),
    create_new_employee(),
    update_employee_record(),
    terminate_employee(),
    get_department_by_id(),
    list_departments(),
    update_department_record(),
    get_compensation_by_employee_id(),
    set_compensation(),
    create_performance_review(),
    get_performance_reviews_by_employee_id(),
    create_leave_record(),
    update_leave_status(),
    list_employee_leaves(),
    create_benefit_plan(),
    update_benefit_plan(),
    set_employee_benefits(),
    get_new_employee_id(),
    search_positions(),
    get_new_compensation_id(),
    get_new_review_id(),
    get_employee_by_ids_by_region(),
    get_new_leave_id(),
]
