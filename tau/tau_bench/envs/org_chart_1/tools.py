import json
from typing import Any, Dict, List, Set
from domains.dto import Tool

# ---------------------------------------------------------------------------
#  1.  Get a single employee by ID  (READ)
# ---------------------------------------------------------------------------


class get_employee_by_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        employees = data.get("employees", [])
        for e in employees:
            if e["employee_id"] == employee_id:
                return json.dumps(e, indent=2)
        return json.dumps({"error": f"employee_id {employee_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_by_id",
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


# ---------------------------------------------------------------------------
#  2.  Search employees by arbitrary filters  (READ)
# ---------------------------------------------------------------------------


class find_employees(Tool):
    """
    Performs simple AND-style filtering on any top-level employee fields
    (e.g. {"department_id": "DEPT1001", "status": "Active"}).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], filters: Dict[str, Any]) -> str:
        employees = data.get("employees", [])
        hits = [e for e in employees if all(e.get(k) == v for k, v in filters.items())]
        return json.dumps({"count": len(hits), "results": hits}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_employees",
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


# ---------------------------------------------------------------------------
#  3.  Create a new employee record  (WRITE)
# ---------------------------------------------------------------------------


class create_new_employee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee: Dict[str, Any]) -> str:
        new_emp = employee
        if not new_emp:
            return json.dumps({"error": "employee payload required"}, indent=2)

        employees = data.get("employees", [])
        if any(e["employee_id"] == new_emp["employee_id"] for e in employees):
            return json.dumps({"error": "employee_id already exists"}, indent=2)

        employees.append(new_emp)
        data["employees"] = employees
        return json.dumps(
            {"success": f'employee {new_emp["employee_id"]} created'}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_employee",
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


# ---------------------------------------------------------------------------
#  4.  Update mutable employee fields  (WRITE/PATCH)
# ---------------------------------------------------------------------------


class update_employee_record(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, updates: Dict[str, Any]) -> str:
        employees = data.get("employees", [])
        changes = updates

        updated = False
        for e in employees:
            if e["employee_id"] == employee_id:
                e.update(changes)
                updated = True
                break

        if not updated:
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        data["employees"] = employees
        return json.dumps({"success": f"employee {employee_id} updated"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employee_record",
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


# ---------------------------------------------------------------------------
#  5.  Terminate / off-board employee (soft delete)  (WRITE)
# ---------------------------------------------------------------------------


class terminate_employee(Tool):
    """
    Marks an employee as terminated by setting status, termination_date,
    and (optionally) clearing benefit and compensation links.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, termination_date: str) -> str:
        employees = data.get("employees", [])

        for e in employees:
            if e["employee_id"] == employee_id:
                e["status"] = "Terminated"
                e["termination_date"] = termination_date
                data["employees"] = employees
                return json.dumps(
                    {"success": f"employee {employee_id} terminated"}, indent=2
                )

        return json.dumps({"error": f"employee_id {employee_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "terminate_employee",
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


# ---------------------------------------------------------------------------
#  6.  Get department metadata  (READ)
# ---------------------------------------------------------------------------


class get_department_by_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department_id: str) -> str:
        depts = data.get("departments", [])
        for d in depts:
            if d["department_id"] == department_id:
                return json.dumps(d, indent=2)
        return json.dumps(
            {"error": f"department_id {department_id} not found"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_department_by_id",
                "description": "Fetch department details by department_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"department_id": {"type": "string"}},
                    "required": ["department_id"],
                    "additionalProperties": False,
                },
            },
        }


# ---------------------------------------------------------------------------
#  7.  List all departments  (READ)
# ---------------------------------------------------------------------------


class list_departments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        return json.dumps(data.get("departments", []), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_departments",
                "description": "Return every department record.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


# ---------------------------------------------------------------------------
#  8.  Update department head, budget, or description  (WRITE)
# ---------------------------------------------------------------------------


class update_department_record(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], department_id: str, updates: Dict[str, Any]
    ) -> str:
        depts = data.get("departments", [])
        changes = updates

        for d in depts:
            if d["department_id"] == department_id:
                d.update(changes)
                data["departments"] = depts
                return json.dumps(
                    {"success": f"department {department_id} updated"}, indent=2
                )

        return json.dumps(
            {"error": f"department_id {department_id} not found"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_department_record",
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


# ---------------------------------------------------------------------------
#  9.  Get an employee's current compensation  (READ)
# ---------------------------------------------------------------------------


class get_compensation_by_employee_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        comp = data.get("compensation_records", [])
        latest = [c for c in comp if c["employee_id"] == employee_id]
        latest.sort(key=lambda c: c["effective_date"], reverse=True)
        return json.dumps(latest[0] if latest else {"error": "not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_compensation_by_employee_id",
                "description": "Return the most recent compensation record for employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


# ---------------------------------------------------------------------------
# 10.  Upsert compensation (new effective date)  (WRITE)
# ---------------------------------------------------------------------------


class set_compensation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], compensation: Dict[str, Any]) -> str:
        if not compensation:
            return json.dumps({"error": "compensation record required"}, indent=2)
        comp = data.get("compensation_records", [])
        comp = [
            c for c in comp if c["compensation_id"] != compensation["compensation_id"]
        ]
        comp.append(compensation)
        data["compensation_records"] = comp
        return json.dumps(
            {"success": f'compensation {compensation["compensation_id"]} recorded'},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_compensation",
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


# ---------------------------------------------------------------------------
# 11.  Add a performance review  (WRITE)
# ---------------------------------------------------------------------------


class create_performance_review(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], review: Dict[str, Any]) -> str:
        if not review:
            return json.dumps({"error": "review record required"}, indent=2)
        pr = data.get("performance_reviews", [])
        pr.append(review)
        data["performance_reviews"] = pr
        return json.dumps({"success": f'review {review["review_id"]} added'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_performance_review",
                "description": "Append a new performance review record.",
                "parameters": {
                    "type": "object",
                    "properties": {"review": {"type": "object"}},
                    "required": ["review"],
                    "additionalProperties": False,
                },
            },
        }


# ---------------------------------------------------------------------------
# 12.  List reviews for an employee  (READ)
# ---------------------------------------------------------------------------


class get_performance_reviews_by_employee_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        pr = [
            r
            for r in data.get("performance_reviews", [])
            if r["employee_id"] == employee_id
        ]
        return json.dumps(pr, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_performance_reviews_by_employee_id",
                "description": "Return all reviews linked to the employee.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


# ---------------------------------------------------------------------------
# 13.  Request a new leave record  (WRITE)
# ---------------------------------------------------------------------------


class create_leave_record(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], leave: Dict[str, Any]) -> str:
        if not leave:
            return json.dumps({"error": "leave record required"}, indent=2)
        lv = data.get("leave_records", [])
        lv.append(leave)
        data["leave_records"] = lv
        return json.dumps({"success": f'leave {leave["leave_id"]} requested'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_leave_record",
                "description": "Insert a leave request; status should start as 'Pending'.",
                "parameters": {
                    "type": "object",
                    "properties": {"leave": {"type": "object"}},
                    "required": ["leave"],
                    "additionalProperties": False,
                },
            },
        }


# ---------------------------------------------------------------------------
# 14.  Approve / update leave status  (WRITE)
# ---------------------------------------------------------------------------


class update_leave_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], leave_id: str, status: str) -> str:
        lv = data.get("leave_records", [])

        for leave_record in lv:
            if leave_record["leave_id"] == leave_id:
                leave_record["status"] = status
                data["leave_records"] = lv
                return json.dumps(
                    {"success": f"leave {leave_id} set to {status}"}, indent=2
                )

        return json.dumps({"error": f"leave_id {leave_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_leave_status",
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


# ---------------------------------------------------------------------------
# 15.  List leaves for an employee  (READ)
# ---------------------------------------------------------------------------


class list_employee_leaves(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        lv = [
            leave_record
            for leave_record in data.get("leave_records", [])
            if leave_record["employee_id"] == employee_id
        ]
        return json.dumps(lv, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_employee_leaves",
                "description": "Return all leave records for the employee (any status).",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


# ---------------------------------------------------------------------------
# 16.  Add a new benefit plan (e.g., PPO2)  (WRITE)
# ---------------------------------------------------------------------------


class create_benefit_plan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], benefit_plan: Dict[str, Any]) -> str:
        if not benefit_plan:
            return json.dumps({"error": "benefit_plan record required"}, indent=2)
        bp = data.get("benefits_plan", [])
        bp.append(benefit_plan)
        data["benefits_plan"] = bp
        return json.dumps(
            {"success": f'benefit_plan {benefit_plan["benefit_plan_id"]} added'},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_benefit_plan",
                "description": "Create a new benefit plan definition.",
                "parameters": {
                    "type": "object",
                    "properties": {"benefit_plan": {"type": "object"}},
                    "required": ["benefit_plan"],
                    "additionalProperties": False,
                },
            },
        }


# ---------------------------------------------------------------------------
# 17.  Amend attributes of an existing benefit plan  (WRITE)
# ---------------------------------------------------------------------------


class update_benefit_plan(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], benefit_plan_id: str, updates: Dict[str, Any]
    ) -> str:
        bp = data.get("benefits_plan", [])

        for p in bp:
            if p["benefit_plan_id"] == benefit_plan_id:
                p.update(updates)
                data["benefits_plan"] = bp
                return json.dumps(
                    {"success": f"benefit_plan {benefit_plan_id} updated"}, indent=2
                )

        return json.dumps(
            {"error": f"benefit_plan_id {benefit_plan_id} not found"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_benefit_plan",
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


# ---------------------------------------------------------------------------
# 18.  Enroll or remove an employee in a benefit plan list  (WRITE)
# ---------------------------------------------------------------------------


class set_employee_benefits(Tool):
    """
    Overwrites the benefit_plan_ids array for an employee to match exactly the
    list supplied in `benefit_plan_ids`.
    """

    @staticmethod
    def invoke(
        data: Dict[str, Any], employee_id: str, benefit_plan_ids: List[str]
    ) -> str:
        employees = data.get("employees", [])

        for e in employees:
            if e["employee_id"] == employee_id:
                e["benefit_plan_ids"] = benefit_plan_ids
                data["employees"] = employees
                return json.dumps(
                    {"success": f"benefits for {employee_id} updated"}, indent=2
                )

        return json.dumps({"error": f"employee_id {employee_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_employee_benefits",
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


# ---------------------------------------------------------------------------
# 19.  Get unused new employee ID  (READ)
# ---------------------------------------------------------------------------


class get_new_employee_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        employees = data.get("employees", [])
        used_ids = [e["employee_id"] for e in employees]
        for i in range(10000, 100000):
            if f"E{i:05d}" not in used_ids:
                return json.dumps(f"E{i:05d}", indent=2)
        return json.dumps({"error": "no unused employee ID found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_new_employee_id",
                "description": "Return an employee ID that is not currently in use.",
                "parameters": {},
            },
        }


# ---------------------------------------------------------------------------
# 20.  Search position  (READ)
# ---------------------------------------------------------------------------


class search_positions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], title: str) -> str:
        positions = data.get("positions", [])
        hits = [p for p in positions if p["title"] == title]
        return json.dumps(hits, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_positions",
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
    def invoke(data: Dict[str, Any]) -> str:
        compensations = data.get("compensations", [])
        prefix = "COMP"
        start_num = 10000

        if not compensations:
            return json.dumps(f"{prefix}{start_num}", indent=2)

        max_id_num = 0
        for comp in compensations:
            comp_id = comp.get("compensation_id", "")
            if comp_id.startswith(prefix):
                try:
                    num = int(comp_id[len(prefix) :])
                    if num > max_id_num:
                        max_id_num = num
                except (ValueError, TypeError):
                    continue

        next_id = f"{prefix}{max(start_num, max_id_num) + 1}"
        return json.dumps(next_id, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_new_compensation_id",
                "description": "Return a compensation ID that is not currently in use.",
                "parameters": {},
            },
        }


class get_new_review_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        reviews = data.get("reviews", [])
        prefix = "PR"
        start_num = 10000

        if not reviews:
            return json.dumps(f"{prefix}{start_num}", indent=2)

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
        return json.dumps(next_id, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_new_review_id",
                "description": "Return a performance review ID that is not currently in use.",
                "parameters": {},
            },
        }


class get_employee_by_ids_by_region(Tool):
    REGION_MAP: Dict[str, Set[str]] = {
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
            "ES",
            "SE",
        }
    }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        region = kwargs.get("region")
        status_filter = kwargs.get("status", "Active")

        if not region or region not in get_employee_by_ids_by_region.REGION_MAP:
            return json.dumps(
                {"error": f"Invalid or unsupported region: {region}"}, indent=2
            )

        employees = data.get("employees", [])
        target_nationalities = get_employee_by_ids_by_region.REGION_MAP[region]

        found_employees = [
            emp
            for emp in employees
            if emp.get("nationality") in target_nationalities
            and emp.get("status") == status_filter
        ]

        return json.dumps(found_employees, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_by_ids_by_region",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        leaves = data.get("leaves", [])
        prefix = "LV"
        start_num = 10000

        if not leaves:
            return json.dumps(f"{prefix}{start_num}", indent=2)

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
        return json.dumps(f"{prefix}{next_id_num}", indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_new_leave_id",
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
