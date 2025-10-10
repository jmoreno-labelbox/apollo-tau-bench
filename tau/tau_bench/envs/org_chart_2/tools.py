import json
from typing import Any, Dict, List, Optional
from domains.dto import Tool

# ---------------------------------------------------------------------------
#  1.  Get a single employee by ID  (READ)
# ---------------------------------------------------------------------------


class get_employee(Tool):
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
                "name": "get_employee",
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


class search_employees(Tool):
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
                "name": "search_employees",
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


class create_employee(Tool):
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
                "name": "create_employee",
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


class update_employee(Tool):
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
                "name": "update_employee",
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


class get_department(Tool):
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
                "name": "get_department",
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


class update_department(Tool):
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
                "name": "update_department",
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


class get_compensation(Tool):
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
                "name": "get_compensation",
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


class add_performance_review(Tool):
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
                "name": "add_performance_review",
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


class list_performance_reviews(Tool):
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
                "name": "list_performance_reviews",
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


class request_leave(Tool):
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
                "name": "request_leave",
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


class add_benefit_plan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], benefit_plan: Dict[str, Any]) -> str:
        if not benefit_plan:
            return json.dumps({"error": "benefit_plan record required"}, indent=2)
        bp = data.get("benefit_plans", [])
        bp.append(benefit_plan)
        data["benefit_plans"] = bp
        return json.dumps(
            {"success": f'benefit_plan {benefit_plan["benefit_plan_id"]} added'},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_benefit_plan",
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


class get_unused_employee_id(Tool):
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
                "name": "get_unused_employee_id",
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


# ---------------------------------------------------------------------------
#  21.  Add a leave record for an employee  (WRITE)
# ---------------------------------------------------------------------------


class add_leave_record(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], leave: Dict[str, Any]) -> str:
        leave_records = data.setdefault("leave_records", [])
        leave_records.append(leave)
        return json.dumps(leave, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_leave_record",
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


# ---------------------------------------------------------------------------
#  22.  List leave records for an employee  (READ)
# ---------------------------------------------------------------------------


class list_leave_records(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        leave_records = data.get("leave_records", [])
        hits = [lr for lr in leave_records if lr.get("employee_id") == employee_id]
        return json.dumps({"count": len(hits), "results": hits}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_leave_records",
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


# ---------------------------------------------------------------------------
# 23.  Patch any field(s) on an existing leave record  (WRITE)
# ---------------------------------------------------------------------------


class update_leave_record(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], leave_id: str, updates: Dict[str, Any]) -> str:
        records = data.get("leave_records", [])
        for rec in records:
            if rec["leave_id"] == leave_id:
                rec.update(updates)
                data["leave_records"] = records
                return json.dumps({"success": f"leave {leave_id} updated"}, indent=2)
        return json.dumps({"error": f"leave_id {leave_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_leave_record",
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


# ---------------------------------------------------------------------------
# 24.  Add / list employee documents – use canonical nested structure
# ---------------------------------------------------------------------------


class add_employee_document(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], document: Dict[str, Any]) -> str:
        container = data.setdefault("employee_documents", [])
        target = next(
            (e for e in container if e["employee_id"] == document["employee_id"]), None
        )
        if target is None:
            target = {
                "employee_id": document["employee_id"],
                "name": "",
                "documents": [],
            }
            container.append(target)

        target["documents"].append(document)
        return json.dumps(
            {"success": f'doc {document.get("doc_id") or document.get("id")} added'},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_employee_document",
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
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        container = data.get("employee_documents", [])
        target = next((e for e in container if e["employee_id"] == employee_id), None)
        docs = target["documents"] if target else []
        return json.dumps({"count": len(docs), "results": docs}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_employee_documents",
                "description": "Return the documents array for the specified employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }


# ---------------------------------------------------------------------------
# 25.  Add a bonus payment record  (WRITE)
# ---------------------------------------------------------------------------


class add_bonus_payment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], bonus: Dict[str, Any]) -> str:
        bonuses = data.setdefault("bonus_payments", [])
        bonuses.append(bonus)
        return json.dumps(bonus, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_bonus_payment",
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


# ---------------------------------------------------------------------------
# 26.  List bonus payments for an employee  (READ)
# ---------------------------------------------------------------------------


class list_bonus_payments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        bonuses = data.get("bonus_payments", [])
        hits = [b for b in bonuses if b.get("employee_id") == employee_id]
        return json.dumps({"count": len(hits), "results": hits}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_bonus_payments",
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


# ---------------------------------------------------------------------------
# 27.  Add employee benefits conditionally  (WRITE)
# ---------------------------------------------------------------------------


class add_employee_benefits_conditionally(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], employee_id: str, benefit_plan_ids: List[str]
    ) -> str:
        # Get current employee benefits
        employees = data.get("employees", [])
        employee = next((e for e in employees if e["employee_id"] == employee_id), None)

        if not employee:
            return json.dumps({"error": f"Employee {employee_id} not found"}, indent=2)

        current_benefits = set(employee.get("benefit_plan_ids", []))
        new_benefits = set(benefit_plan_ids)

        # Only add benefits that aren't already present
        benefits_to_add = new_benefits - current_benefits
        final_benefits = list(current_benefits | new_benefits)

        # Update employee benefits
        employee["benefit_plan_ids"] = final_benefits

        return json.dumps(
            {
                "success": f"Benefits updated for employee {employee_id}",
                "current_benefits": list(current_benefits),
                "requested_benefits": benefit_plan_ids,
                "benefits_actually_added": list(benefits_to_add),
                "final_benefits": final_benefits,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_employee_benefits_conditionally",
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


# ---------------------------------------------------------------------------
# 28.  Increase employee compensation by percentage  (WRITE)
# ---------------------------------------------------------------------------


class increase_employee_compensation(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        employee_id: str,
        compensation_id: str,
        effective_date: str,
        salary_increase_pct: Optional[float] = None,
        equity_increase_amount: Optional[int] = None,
    ) -> str:

        comp_records = data.get("compensation_records", [])
        # Get current compensation
        current_comp_list = [c for c in comp_records if c["employee_id"] == employee_id]
        if not current_comp_list:
            return json.dumps(
                {
                    "error": f"No compensation record found for employee_id {employee_id}"
                },
                indent=2,
            )

        current_comp_list.sort(key=lambda c: c["effective_date"], reverse=True)
        current_comp = current_comp_list[0]

        # Start with current values
        new_comp = current_comp.copy()

        # Update with new required values
        new_comp["compensation_id"] = compensation_id
        new_comp["effective_date"] = effective_date

        # Calculate new salary if applicable
        if salary_increase_pct is not None:
            new_comp["base_salary"] = int(
                current_comp["base_salary"] * (1 + salary_increase_pct / 100)
            )

        # Calculate new equity if applicable
        if equity_increase_amount is not None:
            new_comp["equity_grant"] = (
                current_comp["equity_grant"] + equity_increase_amount
            )

        # Add the new record, preserving history
        comp_records.append(new_comp)
        data["compensation_records"] = comp_records
        return json.dumps(
            {
                "success": f"New compensation record {compensation_id} created for {employee_id}",
                "new_compensation": new_comp,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "increase_employee_compensation",
                "description": "Increase salary by a percentage and/or equity by a fixed amount, creating a new compensation record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "compensation_id": {"type": "string"},
                        "effective_date": {"type": "string"},
                        "salary_increase_pct": {"type": "number"},
                        "equity_increase_amount": {"type": "integer"},
                    },
                    "required": ["employee_id", "compensation_id", "effective_date"],
                },
            },
        }


# ---------------------------------------------------------------------------
# 29.  Conditional compensation check and update  (WRITE)
# ---------------------------------------------------------------------------


class conditional_compensation_check_and_update(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        employee_id: str,
        compensation_id: str,
        effective_date: str,
        salary_threshold: Optional[float] = None,
        target_salary: Optional[float] = None,
        bonus_threshold: Optional[float] = None,
        target_bonus: Optional[float] = None,
        equity_increase_amount: Optional[float] = None,
    ) -> str:
        # Get current compensation
        comp = data.get("compensation_records", [])
        current = [c for c in comp if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            return json.dumps(
                {"error": "No current compensation found for employee"}, indent=2
            )

        latest = current[0]
        changes_made = []

        # Start with current values
        new_salary = latest["base_salary"]
        new_bonus = latest["bonus_target_pct"]
        new_equity = latest["equity_grant"]

        # Check salary condition
        if salary_threshold is not None and target_salary is not None:
            if latest["base_salary"] < salary_threshold:
                new_salary = target_salary
                changes_made.append(
                    f"salary increased from ${latest['base_salary']:,} to ${target_salary:,}"
                )
            else:
                changes_made.append(
                    f"salary ${latest['base_salary']:,} already above threshold ${salary_threshold:,}"
                )

        # Check bonus condition
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

        # Handle equity increase
        if equity_increase_amount is not None:
            new_equity = latest["equity_grant"] + equity_increase_amount
            changes_made.append(
                f"equity increased by ${equity_increase_amount:,} from ${latest['equity_grant']:,} to ${new_equity:,}"
            )

        # Create new compensation record
        new_comp = {
            "compensation_id": compensation_id,
            "employee_id": employee_id,
            "base_salary": new_salary,
            "currency": latest["currency"],
            "bonus_target_pct": new_bonus,
            "equity_grant": new_equity,
            "effective_date": effective_date,
        }

        # Remove old record with same ID if exists and add new one
        comp = [c for c in comp if c["compensation_id"] != compensation_id]
        comp.append(new_comp)
        data["compensation_records"] = comp

        return json.dumps(
            {
                "success": f"Compensation audit completed for {employee_id}",
                "changes": changes_made,
                "new_compensation": new_comp,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "conditional_compensation_check_and_update",
                "description": "Check employee compensation against thresholds and update only if below thresholds, with equity adjustment.",
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
                        "equity_increase_amount": {
                            "type": "number",
                            "description": "Fixed amount to add to equity grant",
                        },
                    },
                    "required": ["employee_id", "compensation_id", "effective_date"],
                    "additionalProperties": False,
                },
            },
        }


class get_unused_document_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        documents = data.get("documents", [])
        prefix = "DOC"
        start_num = 10000

        if not documents:
            return json.dumps(f"{prefix}{start_num}", indent=2)

        max_id_num = 0
        for doc in documents:
            doc_id = doc.get("doc_id", "")
            if doc_id.startswith(prefix):
                try:
                    num = int(doc_id[len(prefix):])
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
                "name": "get_unused_document_id",
                "description": "Return a document ID that is not currently in use.",
                "parameters": {},
            },
        }


class get_unused_review_id(Tool):
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
                "name": "get_unused_review_id",
                "description": "Return a performance review ID that is not currently in use.",
                "parameters": {},
            },
        }



class list_compensations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        all_compensations = data.get("compensation_records", [])
        history = [
            comp for comp in all_compensations
            if comp.get("employee_id") == employee_id
        ]
        if not history:
            return json.dumps({"count": 0, "results": []}, indent=2)
        history.sort(key=lambda c: c.get("effective_date", ""), reverse=True)
        return json.dumps({"count": len(history), "results": history}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_compensations",
                "description": "Return an employee's full compensation history, sorted from most to least recent.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The ID of the employee."
                        }
                    },
                    "required": ["employee_id"],
                },
            },
        }


class get_unused_leave_id(Tool):
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
                "name": "get_unused_leave_id",
                "description": "Return a leave ID that is not currently in use.",
                "parameters": {},
            },
        }


class get_unused_compensation_id(Tool):
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
                "name": "get_unused_compensation_id",
                "description": "Return a compensation ID that is not currently in use.",
                "parameters": {},
            },
        }


class get_unused_bonus_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        bonuses = data.get("bonuses", [])
        prefix = "BON"
        start_num = 10000

        if not bonuses:
            return json.dumps(f"{prefix}{start_num}", indent=2)

        max_id_num = 0
        for bonus in bonuses:
            bonus_id = bonus.get("bonus_id", "")
            if bonus_id.startswith(prefix):
                try:
                    num = int(bonus_id[len(prefix):])
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
                "name": "get_unused_bonus_id",
                "description": "Return a bonus payment ID that is not currently in use.",
                "parameters": {},
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
    conditional_compensation_check_and_update(),
    get_unused_document_id(),
    get_unused_review_id(),
    list_compensations(),
    get_unused_leave_id(),
    get_unused_compensation_id(),
    get_unused_bonus_id(),
]
