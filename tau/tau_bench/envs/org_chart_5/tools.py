import json
from typing import Any, Dict, List
from domains.dto import Tool
from collections import Counter


#  Helper function
def find_employee(employees: List[Dict[str, Any]], employee_id: str) -> Dict[str, Any]:
    """Helper to find a single employee by ID."""
    for e in employees:
        if e.get("employee_id") == employee_id:
            return e
    return None


class get_employee_profile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        employee = find_employee(data.get("employees", []), employee_id)
        if not employee:
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        profile = employee.copy()
        profile["compensation_history"] = [
            c
            for c in data.get("compensation_records", [])
            if c.get("employee_id") == employee_id
        ]
        profile["performance_reviews"] = [
            r
            for r in data.get("performance_reviews", [])
            if r.get("employee_id") == employee_id
        ]
        profile["leave_records"] = [
            l
            for l in data.get("leave_records", [])
            if l.get("employee_id") == employee_id
        ]
        for doc_record in data.get("employee_documents", {}).get(
            "employee_documents", []
        ):
            if doc_record.get("employee_id") == employee_id:
                profile["documents"] = doc_record.get("documents", [])
                break
        return json.dumps(profile, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_profile",
                "description": "Retrieve a comprehensive profile for an employee, including job, compensation, reviews, and documents.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }


class create_employee_from_offer_letter(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        offer_doc_id = kwargs.get("offer_doc_id")
        employee_id = kwargs.get("employee_id")
        if not offer_doc_id or not employee_id:
            return json.dumps(
                {"error": "offer_doc_id and employee_id are required"}, indent=2
            )
        if find_employee(data.get("employees", []), employee_id):
            return json.dumps(
                {"error": f"employee_id {employee_id} already exists"}, indent=2
            )

        new_employee = {
            "employee_id": employee_id,
            "first_name": "New",
            "last_name": "Hire",
            "status": "Active",
            "notes": f"Created from offer doc {offer_doc_id}",
        }
        data.get("employees", []).append(new_employee)
        return json.dumps(
            {
                "success": f"Employee {employee_id} created from offer letter {offer_doc_id}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_employee_from_offer_letter",
                "description": "Creates a new employee record based on an offer letter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "offer_doc_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                    },
                    "required": ["offer_doc_id", "employee_id"],
                },
            },
        }


class list_department_headcount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department_id = kwargs.get("department_id")
        headcount = len(
            [
                e
                for e in data.get("employees", [])
                if e.get("department_id") == department_id
                and e.get("status") == "Active"
            ]
        )
        return json.dumps(
            {"department_id": department_id, "active_headcount": headcount}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_department_headcount",
                "description": "Return current headcount of active employees for a department.",
                "parameters": {
                    "type": "object",
                    "properties": {"department_id": {"type": "string"}},
                    "required": ["department_id"],
                },
            },
        }


class update_employee_compensation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        new_comp = kwargs.get("new_comp")
        if not find_employee(data.get("employees", []), employee_id):
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        new_comp_record = new_comp.copy()
        new_comp_record["employee_id"] = employee_id
        if "compensation_id" not in new_comp_record:
            return json.dumps(
                {"error": "new_comp payload must include a unique compensation_id"},
                indent=2,
            )

        data.get("compensation_records", []).append(new_comp_record)
        return json.dumps(
            {
                "success": f"Compensation record {new_comp_record['compensation_id']} added for {employee_id}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employee_compensation",
                "description": "Adds a new compensation record for an employee, preserving history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "new_comp": {
                            "type": "object",
                            "description": "New compensation details including a unique compensation_id",
                        },
                    },
                    "required": ["employee_id", "new_comp"],
                },
            },
        }


class get_performance_review_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department_id = kwargs.get("department_id")
        employee_id = kwargs.get("employee_id")
        reviews = data.get("performance_reviews", [])

        if employee_id:
            results = [r for r in reviews if r.get("employee_id") == employee_id]
        elif department_id:
            dept_employees = {
                e["employee_id"]
                for e in data.get("employees", [])
                if e.get("department_id") == department_id
            }
            results = [r for r in reviews if r.get("employee_id") in dept_employees]
        else:
            return json.dumps(
                {"error": "Either employee_id or department_id is required"}, indent=2
            )
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_performance_review_status",
                "description": "List performance reviews for a department or an individual employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                    },
                },
            },
        }


class submit_performance_review(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        review_data = kwargs.get("review_data")
        employee = find_employee(data.get("employees", []), employee_id)
        if not employee:
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        new_review = review_data.copy()
        new_review["employee_id"] = employee_id
        if "review_id" not in new_review:
            new_review["review_id"] = (
                f"PR_NEW_{len(data.get('performance_reviews', [])) + 1}"
            )

        data.get("performance_reviews", []).append(new_review)

        if "performance_review_ids" not in employee:
            employee["performance_review_ids"] = []
        if new_review["review_id"] not in employee["performance_review_ids"]:
            employee["performance_review_ids"].append(new_review["review_id"])

        return json.dumps(
            {
                "success": f"Performance review {new_review['review_id']} submitted for {employee_id}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "submit_performance_review",
                "description": "Submit a new performance review for an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "review_data": {
                            "type": "object",
                            "description": "Details including review_id, type, rating, date",
                        },
                    },
                    "required": ["employee_id", "review_data"],
                },
            },
        }


class get_leave_calendar(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department_id = kwargs.get("department_id")
        employee_id = kwargs.get("employee_id")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")

        if not department_id and not employee_id:
            return json.dumps(
                {"error": "department_id or employee_id is required"}, indent=2
            )

        results = data.get("leave_records", [])

        if department_id:
            dept_employees = {
                e["employee_id"]
                for e in data.get("employees", [])
                if e.get("department_id") == department_id
            }
            results = [r for r in results if r.get("employee_id") in dept_employees]

        if employee_id:
            results = [r for r in results if r.get("employee_id") == employee_id]

        if start_date:
            results = [r for r in results if r.get("end_date", "") >= start_date]

        if end_date:
            results = [r for r in results if r.get("start_date", "") <= end_date]

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_leave_calendar",
                "description": "Retrieve leave records for a department or employee, optionally within a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "start_date": {"type": "string", "description": "YYYY-MM-DD"},
                        "end_date": {"type": "string", "description": "YYYY-MM-DD"},
                    },
                },
            },
        }


class request_leave(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        leave_data = kwargs.get("leave_data")
        if not find_employee(data.get("employees", []), employee_id):
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        new_leave = leave_data.copy()
        new_leave["employee_id"] = employee_id
        if "leave_id" not in new_leave:
            new_leave["leave_id"] = f"LV_NEW_{len(data.get('leave_records', [])) + 1}"

        data.get("leave_records", []).append(new_leave)
        return json.dumps(
            {"success": f"Leave {new_leave['leave_id']} requested for {employee_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "request_leave",
                "description": "Submit a new leave request for an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "leave_data": {
                            "type": "object",
                            "description": "Details including a unique leave_id",
                        },
                    },
                    "required": ["employee_id", "leave_data"],
                },
            },
        }


class get_benefits_enrollment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        department_id = kwargs.get("department_id")

        if employee_id:
            employee = find_employee(data.get("employees", []), employee_id)
            if not employee:
                return json.dumps(
                    {"error": f"employee_id {employee_id} not found"}, indent=2
                )
            return json.dumps(employee.get("benefit_plan_ids", []), indent=2)

        if department_id:
            dept_employees = [
                e
                for e in data.get("employees", [])
                if e.get("department_id") == department_id
            ]
            all_benefits = {
                plan_id
                for emp in dept_employees
                for plan_id in emp.get("benefit_plan_ids", [])
            }
            return json.dumps(list(all_benefits), indent=2)

        return json.dumps(
            {"error": "employee_id or department_id is required"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_benefits_enrollment",
                "description": "List benefits enrollment status for an employee or department.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "department_id": {"type": "string"},
                    },
                },
            },
        }


class enroll_in_benefit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        benefit_id = kwargs.get("benefit_id")
        employee = find_employee(data.get("employees", []), employee_id)
        if not employee:
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        if "benefit_plan_ids" not in employee:
            employee["benefit_plan_ids"] = []

        if benefit_id not in employee["benefit_plan_ids"]:
            employee["benefit_plan_ids"].append(benefit_id)
            return json.dumps(
                {"success": f"Employee {employee_id} enrolled in benefit {benefit_id}"},
                indent=2,
            )
        else:
            return json.dumps(
                {
                    "success": f"Employee {employee_id} was already enrolled in benefit {benefit_id}"
                },
                indent=2,
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "enroll_in_benefit",
                "description": "Enroll an employee in a specific benefit plan (non-destructive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "benefit_id": {"type": "string"},
                    },
                    "required": ["employee_id", "benefit_id"],
                },
            },
        }


class remove_from_benefit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        benefit_id = kwargs.get("benefit_id")
        employee = find_employee(data.get("employees", []), employee_id)
        if not employee:
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        if (
            "benefit_plan_ids" in employee
            and benefit_id in employee["benefit_plan_ids"]
        ):
            employee["benefit_plan_ids"].remove(benefit_id)
            return json.dumps(
                {
                    "success": f"Employee {employee_id} removed from benefit {benefit_id}"
                },
                indent=2,
            )
        else:
            return json.dumps(
                {
                    "success": f"Employee {employee_id} was not enrolled in benefit {benefit_id}"
                },
                indent=2,
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_from_benefit",
                "description": "Remove an employee from a specific benefit plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "benefit_id": {"type": "string"},
                    },
                    "required": ["employee_id", "benefit_id"],
                },
            },
        }


class get_document_compliance_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        emp_doc_record = next(
            (
                d
                for d in data.get("employee_documents", {}).get(
                    "employee_documents", []
                )
                if d.get("employee_id") == employee_id
            ),
            None,
        )
        if not emp_doc_record:
            return json.dumps(
                {"employee_id": employee_id, "status": "No documents on file"}, indent=2
            )

        docs = emp_doc_record.get("documents", [])
        doc_categories = {doc.get("category") for doc in docs}

        status = {
            "employee_id": employee_id,
            "has_nda": "NDA" in doc_categories,
            "has_id_verification": "ID Verification" in doc_categories,
            "document_count": len(docs),
        }
        return json.dumps(status, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_document_compliance_status",
                "description": "Check if an employee has key required documents like an NDA and ID verification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "department_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class upload_employee_document(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        document_data = kwargs.get("document_data")
        main_container = data.get("employee_documents", {}).get(
            "employee_documents", []
        )

        emp_doc_record = next(
            (
                d
                for d in data.get("employee_documents", {}).get(
                    "employee_documents", []
                )
                if d.get("employee_id") == employee_id
            ),
            None,
        )
        if not emp_doc_record:
            employee = find_employee(data.get("employees", []), employee_id)
            employee_name = (
                f"{employee.get('first_name')} {employee.get('last_name')}"
                if employee
                else "Unknown"
            )

            emp_doc_record = {
                "employee_id": employee_id,
                "name": employee_name,
                "documents": [],
            }
            main_container.append(emp_doc_record)

        emp_doc_record["documents"].append(document_data)
        return json.dumps({"success": f"Document uploaded for {employee_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upload_employee_document",
                "description": "Upload or attach a new document to an employee's record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "document_data": {
                            "type": "object",
                            "description": "Document metadata and content",
                        },
                    },
                    "required": ["employee_id", "document_data"],
                },
            },
        }


class get_org_diversity_metrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department_id = kwargs.get("department_id")
        level = kwargs.get("level")

        employees_to_scan = data.get("employees", [])
        if department_id:
            employees_to_scan = [
                e for e in employees_to_scan if e.get("department_id") == department_id
            ]
        if level:
            employees_to_scan = [
                e for e in employees_to_scan if e.get("level_id") == level
            ]

        gender_counts = Counter(e.get("gender") for e in employees_to_scan)
        ethnicity_counts = Counter(e.get("ethnicity_code") for e in employees_to_scan)

        metrics = {
            "filter_department": department_id,
            "filter_level": level,
            "total_employees_in_filter": len(employees_to_scan),
            "gender_distribution": dict(gender_counts),
            "ethnicity_distribution": dict(ethnicity_counts),
        }
        return json.dumps(metrics, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_org_diversity_metrics",
                "description": "Return diversity metrics (gender, ethnicity) by department, level, or company-wide.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {"type": "string"},
                        "level": {"type": "string"},
                    },
                },
            },
        }


class update_employee_job_level(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        new_level = kwargs.get("new_level")
        employee = find_employee(data.get("employees", []), employee_id)
        if not employee:
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        employee["level_id"] = new_level
        return json.dumps(
            {"success": f"Job level for {employee_id} updated to {new_level}"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employee_job_level",
                "description": "Change an employee's job level ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "new_level": {"type": "string"},
                    },
                    "required": ["employee_id", "new_level"],
                },
            },
        }


class get_open_positions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department_id = kwargs.get("department_id")
        level = kwargs.get("level")

        filled_position_ids = {
            e.get("position_id")
            for e in data.get("employees", [])
            if e.get("status") == "Active"
        }
        all_positions = data.get("positions", [])

        open_positions = [
            p for p in all_positions if p.get("position_id") not in filled_position_ids
        ]

        if department_id:
            open_positions = [
                p for p in open_positions if p.get("department_id") == department_id
            ]
        if level:
            open_positions = [p for p in open_positions if p.get("level_id") == level]

        return json.dumps(open_positions, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_open_positions",
                "description": "List all open positions not currently filled by an active employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {"type": "string"},
                        "level": {"type": "string"},
                    },
                },
            },
        }


class close_position(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        position_id = kwargs.get("position_id")
        positions = data.get("positions", [])
        position_to_close = next(
            (p for p in positions if p.get("position_id") == position_id), None
        )

        if position_to_close:
            positions.remove(position_to_close)
            return json.dumps(
                {"success": f"Position {position_id} has been closed and removed."},
                indent=2,
            )
        else:
            return json.dumps({"error": f"Position {position_id} not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "close_position",
                "description": "Mark a position as closed by removing it from the list of available positions.",
                "parameters": {
                    "type": "object",
                    "properties": {"position_id": {"type": "string"}},
                    "required": ["position_id"],
                },
            },
        }


class update_company_document_content(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        doc_id = kwargs.get("doc_id")
        new_content = kwargs.get("new_content")

        all_docs = data.get("company_doc", {}).get("company_documents", [])
        doc_to_update = next((d for d in all_docs if d.get("id") == doc_id), None)

        if doc_to_update:
            doc_to_update["content"] = new_content
            doc_to_update["last_updated"] = "2025-06-24"
            return json.dumps(
                {"success": f"Content for document '{doc_id}' updated successfully."},
                indent=2,
            )
        else:
            return json.dumps(
                {"error": f"Company document with ID '{doc_id}' not found."}, indent=2
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_company_document_content",
                "description": "Updates the full text content of an existing company-wide document.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "doc_id": {"type": "string"},
                        "new_content": {"type": "string"},
                    },
                    "required": ["doc_id", "new_content"],
                },
            },
        }


class get_compensation_records(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        if not find_employee(data.get("employees", []), employee_id):
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        records = [
            c
            for c in data.get("compensation_records", [])
            if c.get("employee_id") == employee_id
        ]
        return json.dumps(records, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_compensation_records",
                "description": "Retrieve all historical compensation records for an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }


class update_employee_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        new_status = kwargs.get("new_status")
        employee = find_employee(data.get("employees", []), employee_id)
        if not employee:
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        employee["status"] = new_status
        if new_status.lower() == "terminated":
            employee["termination_date"] = "2025-06-24"  # Using our standard "today"
        return json.dumps(
            {"success": f"Employee {employee_id} status updated to {new_status}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employee_status",
                "description": "Update an employee's current status (e.g., 'Active', 'On Leave', 'Terminated').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["employee_id", "new_status"],
                },
            },
        }


TOOLS = [
    get_employee_profile(),
    create_employee_from_offer_letter(),
    list_department_headcount(),
    update_employee_compensation(),
    get_performance_review_status(),
    submit_performance_review(),
    get_leave_calendar(),
    request_leave(),
    get_benefits_enrollment(),
    enroll_in_benefit(),
    remove_from_benefit(),
    get_document_compliance_status(),
    upload_employee_document(),
    get_org_diversity_metrics(),
    update_employee_job_level(),
    get_open_positions(),
    close_position(),
    update_company_document_content(),
    get_compensation_records(),
    update_employee_status(),
]
