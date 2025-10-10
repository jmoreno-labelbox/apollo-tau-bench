from typing import List, Dict, Any
from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="u1",
        instruction="We need to confirm Elena Rodriguez (E10005) successfully completed her onboarding process. Verify her enrollment status shows Medical - PPO and Parental Leave benefits, confirm all required legal documents are properly filed, and validate her compensation package is correctly established.",
        actions=[
            Action(name="get_benefits_enrollment", kwargs={"employee_id": "E10005"}),
            Action(name="get_document_compliance_status", kwargs={"employee_id": "E10005"}),
            Action(name="get_compensation_records", kwargs={"employee_id": "E10005"}),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10005"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10005",
                "first_name": "Elena",
                "last_name": "Rodriguez",
                "preferred_name": "Elena",
                "date_of_birth": "1995-01-30",
                "gender": "Female",
                "ethnicity_code": "H",
                "nationality": "ES",
                "marital_status": "Single",
                "hire_date": "2024-09-01",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3010",
                "department_id": "DEPT1004",
                "level_id": "L.1",
                "manager_id": "E10011",
                "work_location": "Madrid Office",
                "work_email": "elena.rodriguez@example.com",
                "work_phone": "+34-91-555-0200",
                "compensation_id": "COMP2005",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4005"
                ],
                "performance_review_ids": [],
                "skills": [
                    "Financial Modeling",
                    "SQL",
                    "Excel"
                ],
                "role_description": "Junior Financial Analyst supporting quarterly forecasts.",
                "notes": "Recent graduate—IE Business School.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2005",
                        "employee_id": "E10005",
                        "base_salary": 72000,
                        "currency": "EUR",
                        "bonus_target_pct": 5,
                        "equity_grant": 2000,
                        "effective_date": "2024-09-01"
                    }
                ],
                "performance_reviews": [],
                "leave_records": [],
                "documents": []
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u2",
        instruction="Rahul Singh (E10004) has earned a promotion to L.2 effective February 1st, 2025, with a salary adjustment to $118,000 and Medical-PPO enrollment. He'll receive another salary increase to $125,000 in December 2025. Complete his promotion package including documentation (promotion letter E10004-010) and performance tracking.",
        actions=[
            Action(
                name="update_employee_job_level",
                kwargs={"employee_id": "E10004", "new_level": "L.2"},
            ),
            Action(
                name="update_employee_compensation",
                kwargs={
                    "employee_id": "E10004",
                    "new_comp": {
                        "compensation_id": "COMP2007",
                        "base_salary": 118000,
                        "currency": "USD",
                        "effective_date": "2025-02-01",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10004",
                    "review_data": {
                        "review_id": "PR5012",
                        "type": "Promotion",
                        "rating": "Meets",
                        "date": "2025-02-01",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10004",
                    "document_data": {
                        "id": "E10004-010",
                        "category": "Promotion Letter",
                        "title": "Promotion Letter L.2",
                    },
                },
            ),
            Action(
                name="enroll_in_benefit",
                kwargs={"employee_id": "E10004", "benefit_id": "BEN4001"},
            ),
            Action(
                name="update_employee_compensation",
                kwargs={
                    "employee_id": "E10004",
                    "new_comp": {
                        "compensation_id": "COMP2008",
                        "base_salary": 125000,
                        "currency": "USD",
                        "effective_date": "2025-12-01",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10004",
                    "review_data": {
                        "review_id": "PR5013",
                        "type": "Annual",
                        "rating": "Exceeds",
                        "date": "2025-12-01",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10004"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10004",
                "first_name": "Rahul",
                "last_name": "Singh",
                "preferred_name": "Rahul",
                "date_of_birth": "1988-05-02",
                "gender": "Male",
                "ethnicity_code": "A",
                "nationality": "IN",
                "marital_status": "Married",
                "hire_date": "2022-02-14",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3007",
                "department_id": "DEPT1001",
                "level_id": "L.2",
                "manager_id": "E10003",
                "work_location": "Remote – Bangalore",
                "work_email": "rahul.singh@example.com",
                "work_phone": "+91-80-5550-1122",
                "compensation_id": "COMP2004",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4003"
                ],
                "performance_review_ids": [
                    "PR5004",
                    "PR5009",
                    "PR5012",
                    "PR5013"
                ],
                "skills": [
                    "Go",
                    "Kubernetes",
                    "CI/CD"
                ],
                "role_description": "Backend Engineer focusing on micro-services.",
                "notes": "Visa sponsored (H-1B).",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2004",
                        "employee_id": "E10004",
                        "base_salary": 118000,
                        "currency": "USD",
                        "bonus_target_pct": 10,
                        "equity_grant": 8000,
                        "effective_date": "2022-02-14"
                    },
                    {
                        "compensation_id": "COMP2007",
                        "base_salary": 118000,
                        "currency": "USD",
                        "effective_date": "2025-02-01",
                        "employee_id": "E10004"
                    },
                    {
                        "compensation_id": "COMP2008",
                        "base_salary": 125000,
                        "currency": "USD",
                        "effective_date": "2025-12-01",
                        "employee_id": "E10004"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5004",
                        "employee_id": "E10004",
                        "period_start": "2023-01-01",
                        "period_end": "2023-12-31",
                        "rating": "Meets",
                        "manager_id": "E10003",
                        "summary": "Solid contributor; needs mentorship on architecture."
                    },
                    {
                        "review_id": "PR5009",
                        "employee_id": "E10004",
                        "period_start": "2024-01-01",
                        "period_end": "2024-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10003",
                        "summary": "Exceeds performance"
                    },
                    {
                        "review_id": "PR5012",
                        "type": "Promotion",
                        "rating": "Meets",
                        "date": "2025-02-01",
                        "employee_id": "E10004"
                    },
                    {
                        "review_id": "PR5013",
                        "type": "Annual",
                        "rating": "Exceeds",
                        "date": "2025-12-01",
                        "employee_id": "E10004"
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV6002",
                        "employee_id": "E10004",
                        "leave_type": "Vacation",
                        "start_date": "2025-07-12",
                        "end_date": "2025-07-26",
                        "status": "Taken"
                    }
                ],
                "documents": [
                    {
                        "id": "E10004-010",
                        "category": "Promotion Letter",
                        "title": "Promotion Letter L.2"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u3",
        instruction="The main hiring push for the Finance department (DEPT1004) is complete. Process the closeout. You'll need to formally close the two recently filled positions: 'Financial Analyst' (POS3010) and 'Senior Accountant' (POS3013). As a final onboarding step for the new hire in that department, Elena Rodriguez (E10005), enroll her in the 401(k) plan (BEN4003). To verify the closeout, retrieve the list of any remaining open positions for the Finance department.",
        actions=[
            Action(name="close_position", kwargs={"position_id": "POS3010"}),
            Action(name="close_position", kwargs={"position_id": "POS3013"}),
            Action(
                name="enroll_in_benefit",
                kwargs={"employee_id": "E10005", "benefit_id": "BEN4003"},
            ),
            Action(name="get_open_positions", kwargs={"department_id": "DEPT1004"}),
        ],
        outputs=[
            """
            []
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u4",
        instruction="Amelia Garcia (E10003) needs parental leave from November 1st, 2025 to February 1st, 2026. Complete her leave setup including benefit enrollment for Parental Leave (BEN4004) and document filing for her signed request form (E10003-LRF-01) and manager approval (E10003-MGR-AP-01).",
        actions=[
            Action(
                name="request_leave",
                kwargs={
                    "employee_id": "E10003",
                    "leave_data": {
                        "leave_id": "LV6003",
                        "type": "Parental",
                        "start_date": "2025-11-01",
                        "end_date": "2026-02-01",
                        "status": "Approved",
                    },
                },
            ),
            Action(
                name="enroll_in_benefit",
                kwargs={"employee_id": "E10003", "benefit_id": "BEN4004"},
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-LRF-01",
                        "category": "Leave Request Form",
                        "title": "Parental Leave Request Form 2025",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-MGR-AP-01",
                        "category": "Manager Approval",
                        "title": "Manager Approval for Parental Leave 2025",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10003",
                "first_name": "Amelia",
                "last_name": "Garcia",
                "preferred_name": "Amy",
                "date_of_birth": "1990-11-22",
                "gender": "Female",
                "ethnicity_code": "H",
                "nationality": "US",
                "marital_status": "Partnered",
                "hire_date": "2019-06-10",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3006",
                "department_id": "DEPT1005",
                "level_id": "L.3",
                "manager_id": "E10001",
                "work_location": "Remote – Austin, TX",
                "work_email": "amelia.garcia@example.com",
                "work_phone": "+1-737-555-0188",
                "compensation_id": "COMP2003",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4003",
                    "BEN4004"
                ],
                "performance_review_ids": [
                    "PR5003",
                    "PR5010"
                ],
                "skills": [
                    "TypeScript",
                    "React",
                    "Accessibility"
                ],
                "role_description": "Senior Front-end Engineer on the web platform team.",
                "notes": "On parental leave 2024-11-01 → 2025-02-01.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2003",
                        "employee_id": "E10003",
                        "base_salary": 145000,
                        "currency": "USD",
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "effective_date": "2024-07-01"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5003",
                        "employee_id": "E10003",
                        "period_start": "2023-07-01",
                        "period_end": "2023-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10001",
                        "summary": "Led UI redesign improving conversion by 10%."
                    },
                    {
                        "review_id": "PR5010",
                        "employee_id": "E10003",
                        "period_start": "2024-01-01",
                        "period_end": "2024-06-30",
                        "rating": "Pending",
                        "manager_id": "E10001",
                        "summary": "On leave; review deferred."
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV6001",
                        "employee_id": "E10003",
                        "leave_type": "Parental",
                        "start_date": "2024-11-01",
                        "end_date": "2025-02-01",
                        "status": "Scheduled"
                    },
                    {
                        "leave_id": "LV6003",
                        "type": "Parental",
                        "start_date": "2025-11-01",
                        "end_date": "2026-02-01",
                        "status": "Approved",
                        "employee_id": "E10003"
                    }
                ],
                "documents": [
                    {
                        "id": "E10003-LRF-01",
                        "category": "Leave Request Form",
                        "title": "Parental Leave Request Form 2025"
                    },
                    {
                        "id": "E10003-MGR-AP-01",
                        "category": "Manager Approval",
                        "title": "Manager Approval for Parental Leave 2025"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u5",
        instruction="Daniel Kim (E10002) from Sales needs compliance documentation and a mandatory 1-day compliance training period on August 1st, 2025. Complete his compliance record by uploading the deficiency notice (E10002-001) and scheduling his compliance escalation leave (LV6004) with approved status.",
        actions=[
            Action(
                name="get_document_compliance_status", kwargs={"employee_id": "E10002"}
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10002",
                    "document_data": {
                        "id": "E10002-001",
                        "category": "Compliance",
                        "title": "Compliance Deficiency Notice",
                    },
                },
            ),
            Action(
                name="request_leave",
                kwargs={
                    "employee_id": "E10002",
                    "leave_data": {
                        "leave_id": "LV6004",
                        "type": "Compliance Escalation",
                        "start_date": "2025-08-01",
                        "end_date": "2025-08-01",
                        "status": "Approved",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10002",
                "first_name": "Daniel",
                "last_name": "Kim",
                "preferred_name": "Dan",
                "date_of_birth": "1982-09-04",
                "gender": "Male",
                "ethnicity_code": "A",
                "nationality": "US",
                "marital_status": "Single",
                "hire_date": "2015-03-17",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3004",
                "department_id": "DEPT1002",
                "level_id": "L.5",
                "manager_id": "E10012",
                "work_location": "New York Office",
                "work_email": "dan.kim@example.com",
                "work_phone": "+1-212-555-0144",
                "compensation_id": "COMP2002",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4002"
                ],
                "performance_review_ids": [
                    "PR5002"
                ],
                "skills": [
                    "Sales Strategy",
                    "CRM",
                    "Negotiation"
                ],
                "role_description": "Regional VP of Sales for the Eastern territory.",
                "notes": "High performer—President's Club 2023.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2002",
                        "employee_id": "E10002",
                        "base_salary": 210000,
                        "currency": "USD",
                        "bonus_target_pct": 25,
                        "equity_grant": 40000,
                        "effective_date": "2024-04-01"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5002",
                        "employee_id": "E10002",
                        "period_start": "2024-01-01",
                        "period_end": "2024-03-31",
                        "rating": "Meets",
                        "manager_id": "E10012",
                        "summary": "On track to hit Q2 quota."
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV6004",
                        "type": "Compliance Escalation",
                        "start_date": "2025-08-01",
                        "end_date": "2025-08-01",
                        "status": "Approved",
                        "employee_id": "E10002"
                    }
                ],
                "documents": [
                    {
                        "id": "E10002-001",
                        "category": "Compliance",
                        "title": "Compliance Deficiency Notice"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u6",
        instruction="Amelia Garcia (E10003) has earned a promotion to Level 4 (L.4) effective August 1st, 2025, with a salary increase to $150,000. Process her promotion including the compensation update (COMP2009), performance documentation, and transfer letter (E10003-003) upload.",
        actions=[
            Action(
                name="update_employee_job_level",
                kwargs={"employee_id": "E10003", "new_level": "L.4"},
            ),
            Action(
                name="update_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "new_comp": {
                        "compensation_id": "COMP2009",
                        "base_salary": 150000,
                        "currency": "USD",
                        "effective_date": "2025-08-01",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10003",
                    "review_data": {
                        "review_id": "PR5014",
                        "type": "Transfer",
                        "rating": None,
                        "date": "2025-08-01",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-003",
                        "category": "Transfer Letter",
                        "title": "Transfer Letter to Engineering",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10003",
                "first_name": "Amelia",
                "last_name": "Garcia",
                "preferred_name": "Amy",
                "date_of_birth": "1990-11-22",
                "gender": "Female",
                "ethnicity_code": "H",
                "nationality": "US",
                "marital_status": "Partnered",
                "hire_date": "2019-06-10",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3006",
                "department_id": "DEPT1005",
                "level_id": "L.4",
                "manager_id": "E10001",
                "work_location": "Remote – Austin, TX",
                "work_email": "amelia.garcia@example.com",
                "work_phone": "+1-737-555-0188",
                "compensation_id": "COMP2003",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4003",
                    "BEN4004"
                ],
                "performance_review_ids": [
                    "PR5003",
                    "PR5010",
                    "PR5014"
                ],
                "skills": [
                    "TypeScript",
                    "React",
                    "Accessibility"
                ],
                "role_description": "Senior Front-end Engineer on the web platform team.",
                "notes": "On parental leave 2024-11-01 → 2025-02-01.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2003",
                        "employee_id": "E10003",
                        "base_salary": 145000,
                        "currency": "USD",
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "effective_date": "2024-07-01"
                    },
                    {
                        "compensation_id": "COMP2009",
                        "base_salary": 150000,
                        "currency": "USD",
                        "effective_date": "2025-08-01",
                        "employee_id": "E10003"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5003",
                        "employee_id": "E10003",
                        "period_start": "2023-07-01",
                        "period_end": "2023-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10001",
                        "summary": "Led UI redesign improving conversion by 10%."
                    },
                    {
                        "review_id": "PR5010",
                        "employee_id": "E10003",
                        "period_start": "2024-01-01",
                        "period_end": "2024-06-30",
                        "rating": "Pending",
                        "manager_id": "E10001",
                        "summary": "On leave; review deferred."
                    },
                    {
                        "review_id": "PR5014",
                        "type": "Transfer",
                        "rating": null,
                        "date": "2025-08-01",
                        "employee_id": "E10003"
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV6001",
                        "employee_id": "E10003",
                        "leave_type": "Parental",
                        "start_date": "2024-11-01",
                        "end_date": "2025-02-01",
                        "status": "Scheduled"
                    }
                ],
                "documents": [
                    {
                        "id": "E10003-003",
                        "category": "Transfer Letter",
                        "title": "Transfer Letter to Engineering"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u7",
        instruction="Marcus Chen (E10006) completed his 6-month probationary period. Verify his foreign national documentation is compliant, confirm his Medical-PPO and Dental benefit enrollments are active, and validate his compensation history includes both initial and probationary updates.",
        actions=[
            Action(name="get_document_compliance_status", kwargs={"employee_id": "E10006"}),
            Action(name="get_benefits_enrollment", kwargs={"employee_id": "E10006"}),
            Action(name="get_compensation_records", kwargs={"employee_id": "E10006"}),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10006"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10006",
                "first_name": "Marcus",
                "last_name": "Chen",
                "preferred_name": "Marcus",
                "date_of_birth": "1991-08-12",
                "gender": "Male",
                "ethnicity_code": "A",
                "nationality": "CA",
                "marital_status": "Married",
                "hire_date": "2023-11-15",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3008",
                "department_id": "DEPT1004",
                "level_id": "L.4",
                "manager_id": "E10012",
                "work_location": "Madrid Office",
                "work_email": "marcus.chen@example.com",
                "work_phone": "+1-604-555-0166",
                "compensation_id": "COMP2006",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4002",
                    "BEN4003"
                ],
                "performance_review_ids": [

                ],
                "skills": [
                    "Product Strategy",
                    "User Research",
                    "Data Analytics"
                ],
                "role_description": "Senior Product Manager leading the analytics platform initiatives.",
                "notes": "Previously led successful product launches at major tech companies.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2006",
                        "employee_id": "E10006",
                        "base_salary": 60000,
                        "currency": "EUR",
                        "bonus_target_pct": 5,
                        "equity_grant": 5000,
                        "effective_date": "2024-09-01"
                    }
                ],
                "performance_reviews": [],
                "leave_records": [],
                "documents": []
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u8",
        instruction="Rahul Singh (E10004) has submitted a duplicate vacation request for July 12-26, 2025, when he's already scheduled for leave. Escalate this conflict by uploading the Leave Conflict Report (E10004-LCR-01) and scheduling his mandatory 2-day HR Escalation leave (LV8006) from July 28-29, 2025, with approved status.",
        actions=[
            Action(name="get_leave_calendar", kwargs={"employee_id": "E10004"}),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10004",
                    "document_data": {
                        "id": "E10004-LCR-01",
                        "category": "Leave Conflict",
                        "title": "Leave Conflict Report",
                    },
                },
            ),
            Action(
                name="request_leave",
                kwargs={
                    "employee_id": "E10004",
                    "leave_data": {
                        "leave_id": "LV8006",
                        "type": "HR Escalation",
                        "start_date": "2025-07-28",
                        "end_date": "2025-07-29",
                        "status": "Approved",
                    },
                },
            ),
            Action(name="get_leave_calendar", kwargs={"employee_id": "E10004"}),
        ],
        outputs=[
            """
            [
                {
                    "leave_id": "LV6002",
                    "employee_id": "E10004",
                    "leave_type": "Vacation",
                    "start_date": "2025-07-12",
                    "end_date": "2025-07-26",
                    "status": "Taken"
                },
                {
                    "leave_id": "LV8006",
                    "type": "HR Escalation",
                    "start_date": "2025-07-28",
                    "end_date": "2025-07-29",
                    "status": "Approved",
                    "employee_id": "E10004"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u9",
        instruction="Conduct a compliance audit for Sophia Nguyen (E10001) and Daniel Kim (E10002). For both, ensure they have an 'ID Verification' (I-9) and a 'Compliance' document on file (use doc IDs [EMPID]-004 and [EMPID]-020 respectively). Also, verify that they are enrolled in the 401(k) plan (BEN4003) and enroll them if they are not. Since compliance issues were found, log a 2-day 'Compliance Review' leave for each affected employee starting 2025-08-04. To verify, provide the full employee profile for Daniel Kim (E10002).",
        actions=[
            Action(
                name="get_document_compliance_status", kwargs={"employee_id": "E10001"}
            ),
            Action(
                name="get_document_compliance_status", kwargs={"employee_id": "E10002"}
            ),
            Action(name="get_benefits_enrollment", kwargs={"employee_id": "E10001"}),
            Action(name="get_benefits_enrollment", kwargs={"employee_id": "E10002"}),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {
                        "id": "E10001-004",
                        "category": "ID Verification",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {"id": "E10001-020", "category": "Compliance"},
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10002",
                    "document_data": {
                        "id": "E10002-004",
                        "category": "ID Verification",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10002",
                    "document_data": {"id": "E10002-020", "category": "Compliance"},
                },
            ),
            Action(
                name="enroll_in_benefit",
                kwargs={"employee_id": "E10002", "benefit_id": "BEN4003"},
            ),
            Action(
                name="request_leave",
                kwargs={
                    "employee_id": "E10001",
                    "leave_data": {
                        "leave_id": "LV8007",
                        "type": "Compliance Review",
                        "start_date": "2025-08-04",
                        "end_date": "2025-08-05",
                    },
                },
            ),
            Action(
                name="request_leave",
                kwargs={
                    "employee_id": "E10002",
                    "leave_data": {
                        "leave_id": "LV8008",
                        "type": "Compliance Review",
                        "start_date": "2025-08-04",
                        "end_date": "2025-08-05",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10002",
                "first_name": "Daniel",
                "last_name": "Kim",
                "preferred_name": "Dan",
                "date_of_birth": "1982-09-04",
                "gender": "Male",
                "ethnicity_code": "A",
                "nationality": "US",
                "marital_status": "Single",
                "hire_date": "2015-03-17",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3004",
                "department_id": "DEPT1002",
                "level_id": "L.5",
                "manager_id": "E10012",
                "work_location": "New York Office",
                "work_email": "dan.kim@example.com",
                "work_phone": "+1-212-555-0144",
                "compensation_id": "COMP2002",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4002",
                    "BEN4003"
                ],
                "performance_review_ids": [

                ],
                "skills": [
                    "Sales Strategy",
                    "CRM",
                    "Negotiation"
                ],
                "role_description": "Regional VP of Sales for the Eastern territory.",
                "notes": "High performer—President's Club 2023.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2002",
                        "employee_id": "E10002",
                        "base_salary": 210000,
                        "currency": "USD",
                        "bonus_target_pct": 25,
                        "equity_grant": 40000,
                        "effective_date": "2024-04-01"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5002",
                        "employee_id": "E10002",
                        "period_start": "2024-01-01",
                        "period_end": "2024-03-31",
                        "rating": "Meets",
                        "manager_id": "E10012",
                        "summary": "On track to hit Q2 quota."
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV8008",
                        "type": "Compliance Review",
                        "start_date": "2025-08-04",
                        "end_date": "2025-08-05",
                        "employee_id": "E10002"
                    }
                ],
                "documents": [
                    {
                        "id": "E10002-004",
                        "category": "ID Verification"
                    },
                    {
                        "id": "E10002-020",
                        "category": "Compliance"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u10",
        instruction="Process a compensation update for two key employees in the Engineering department (DEPT1001), Sophia Nguyen (E10001) and Rahul Singh (E10004), effective 2025-09-01. Sophia's new base salary is $340,000 (compensation record COMP2010). Rahul's new base salary is $124,000 (compensation record COMP2011). Upload compensation update documents (E10001-001 and E10004-001) and verify Sophia's updated profile.",
        actions=[
            Action(
                name="update_employee_compensation",
                kwargs={
                    "employee_id": "E10001",
                    "new_comp": {
                        "compensation_id": "COMP2010",
                        "base_salary": 340000,
                        "currency": "USD",
                        "effective_date": "2025-09-01",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {
                        "id": "E10001-001",
                        "category": "Compensation",
                        "title": "Compensation Update",
                    },
                },
            ),
            Action(
                name="update_employee_compensation",
                kwargs={
                    "employee_id": "E10004",
                    "new_comp": {
                        "compensation_id": "COMP2011",
                        "base_salary": 124000,
                        "currency": "USD",
                        "effective_date": "2025-09-01",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10004",
                    "document_data": {
                        "id": "E10004-001",
                        "category": "Compensation",
                        "title": "Compensation Update",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10001",
                "first_name": "Sophia",
                "last_name": "Nguyen",
                "preferred_name": "Sophia",
                "date_of_birth": "1978-02-16",
                "gender": "Female",
                "ethnicity_code": "W",
                "nationality": "US",
                "marital_status": "Married",
                "hire_date": "2010-08-02",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3001",
                "department_id": "DEPT1001",
                "level_id": "L.C",
                "manager_id": null,
                "work_location": "San Francisco HQ",
                "work_email": "sophia.nguyen@example.com",
                "work_phone": "+1-415-555-0100",
                "compensation_id": "COMP2010",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4002",
                    "BEN4003"
                ],
                "performance_review_ids": [
                    "PR5001",
                    "PR5009"
                ],
                "skills": [
                    "Leadership",
                    "Cloud Architecture",
                    "Python"
                ],
                "role_description": "Chief Technology Officer overseeing all engineering functions.",
                "notes": "Founder-level equity grant.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2001",
                        "employee_id": "E10001",
                        "base_salary": 325000,
                        "currency": "USD",
                        "bonus_target_pct": 30,
                        "equity_grant": 75000,
                        "effective_date": "2025-01-01"
                    },
                    {
                        "compensation_id": "COMP2010",
                        "base_salary": 340000,
                        "currency": "USD",
                        "effective_date": "2025-09-01",
                        "employee_id": "E10001"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5001",
                        "employee_id": "E10001",
                        "period_start": "2024-01-01",
                        "period_end": "2024-12-31",
                        "rating": "Exceeds",
                        "manager_id": "null",
                        "summary": "Delivered cloud migration ahead of schedule."
                    },
                    {
                        "review_id": "PR5009",
                        "employee_id": "E10001",
                        "period_start": "2024-01-01",
                        "period_end": "2024-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10003",
                        "summary": "Exceeds performance"
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV7001",
                        "employee_id": "E10001",
                        "leave_type": "Parental",
                        "start_date": "2025-07-01",
                        "end_date": "2026-02-01",
                        "status": "Scheduled"
                    }
                ],
                "documents": [
                    {
                        "id": "E10001-001",
                        "category": "Compensation",
                        "title": "Compensation Update"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u11",
        instruction="Conduct an audit of the documentation for Amelia Garcia's (E10003) upcoming parental leave (LV6001). You need to verify that a 'Manager Approval' document is on file for this leave. If it is missing, you must escalate the issue by uploading a 'Missing Document' notice (doc ID E10003-001) and logging a 1-day 'HR Escalation' leave for her manager (E10001), effective 2025-08-06. For verification, provide the full leave calendar for the Engineering department (DEPT1001).",
        actions=[
            Action(
                name="get_document_compliance_status", kwargs={"employee_id": "E10003"}
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-001",
                        "category": "Compliance",
                        "title": "Missing Document Notice: Manager Approval for LV6001",
                    },
                },
            ),
            Action(
                name="request_leave",
                kwargs={
                    "employee_id": "E10001",
                    "leave_data": {
                        "leave_id": "LV8009",
                        "type": "HR Escalation",
                        "start_date": "2025-08-06",
                        "end_date": "2025-08-06",
                        "status": "Approved",
                    },
                },
            ),
            Action(name="get_leave_calendar", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "leave_id": "LV6001",
                    "employee_id": "E10003",
                    "leave_type": "Parental",
                    "start_date": "2024-11-01",
                    "end_date": "2025-02-01",
                    "status": "Scheduled"
                },
                {
                    "leave_id": "LV6002",
                    "employee_id": "E10004",
                    "leave_type": "Vacation",
                    "start_date": "2025-07-12",
                    "end_date": "2025-07-26",
                    "status": "Taken"
                },
                {
                    "leave_id": "LV7001",
                    "employee_id": "E10001",
                    "leave_type": "Parental",
                    "start_date": "2025-07-01",
                    "end_date": "2026-02-01",
                    "status": "Scheduled"
                },
                {
                    "leave_id": "LV8009",
                    "employee_id": "E10001",
                    "type": "HR Escalation",
                    "start_date": "2025-08-06",
                    "end_date": "2025-08-06",
                    "status": "Approved",
                },
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u12",
        instruction="Marcus Chen (E10006) needs his 6-month probationary review completed. Verify his Medical-PPO enrollment is active, confirm his signed NDA documentation is compliant, and validate his probationary compensation adjustments are properly recorded.",
        actions=[
            Action(name="get_benefits_enrollment", kwargs={"employee_id": "E10006"}),
            Action(name="get_document_compliance_status", kwargs={"employee_id": "E10006"}),
            Action(name="get_compensation_records", kwargs={"employee_id": "E10006"}),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10006"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10006",
                    "first_name": "Marcus",
                    "last_name": "Chen",
                    "preferred_name": "Marcus",
                    "date_of_birth": "1991-08-12",
                    "gender": "Male",
                    "ethnicity_code": "A",
                    "nationality": "CA",
                    "marital_status": "Married",
                    "hire_date": "2023-11-15",
                    "termination_date": null,
                    "status": "Active",
                    "position_id": "POS3008",
                    "department_id": "DEPT1004",
                    "level_id": "L.4",
                    "manager_id": "E10012",
                    "work_location": "Madrid Office",
                    "work_email": "marcus.chen@example.com",
                    "work_phone": "+1-604-555-0166",
                    "compensation_id": "COMP2006",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN4003"
                    ],
                    "performance_review_ids": [
                        "PR5011"
                    ],
                    "skills": [
                        "Product Strategy",
                        "User Research",
                        "Data Analytics"
                    ],
                    "role_description": "Senior Product Manager leading the analytics platform initiatives.",
                    "notes": "Previously led successful product launches at major tech companies.",
                    "compensation_history": [
                        {
                            "compensation_id": "COMP2006",
                            "employee_id": "E10006",
                            "base_salary": 60000,
                            "currency": "EUR",
                            "bonus_target_pct": 5,
                            "equity_grant": 5000,
                            "effective_date": "2024-09-01"
                        }
                    ],
                    "performance_reviews": [],
                    "leave_records": [],
                    "documents": []
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u13",
        instruction="Process a benefits change for Daniel Kim (E10002). He has elected to opt out of the Dental plan (BEN4002). You'll need to remove this plan from his enrollments and upload a 'Benefit Change Form' (doc ID E10002-BCF-01) to his file to document the change. For verification, retrieve his updated employee profile.",
        actions=[
            Action(
                name="remove_from_benefit",
                kwargs={"employee_id": "E10002", "benefit_id": "BEN4002"},
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10002",
                    "document_data": {
                        "id": "E10002-BCF-01",
                        "category": "Benefit Change",
                        "title": "Benefit Change Form - Dental Opt-Out",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10002",
                "first_name": "Daniel",
                "last_name": "Kim",
                "preferred_name": "Dan",
                "date_of_birth": "1982-09-04",
                "gender": "Male",
                "ethnicity_code": "A",
                "nationality": "US",
                "marital_status": "Single",
                "hire_date": "2015-03-17",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3004",
                "department_id": "DEPT1002",
                "level_id": "L.5",
                "manager_id": "E10012",
                "work_location": "New York Office",
                "work_email": "dan.kim@example.com",
                "work_phone": "+1-212-555-0144",
                "compensation_id": "COMP2002",
                "benefit_plan_ids": [
                    "BEN4001"
                ],
                "performance_review_ids": [
                    "PR5002"
                ],
                "skills": [
                    "Sales Strategy",
                    "CRM",
                    "Negotiation"
                ],
                "role_description": "Regional VP of Sales for the Eastern territory.",
                "notes": "High performer—President's Club 2023.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2002",
                        "employee_id": "E10002",
                        "base_salary": 210000,
                        "currency": "USD",
                        "bonus_target_pct": 25,
                        "equity_grant": 40000,
                        "effective_date": "2024-04-01"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5002",
                        "employee_id": "E10002",
                        "period_start": "2024-01-01",
                        "period_end": "2024-03-31",
                        "rating": "Meets",
                        "manager_id": "E10012",
                        "summary": "On track to hit Q2 quota."
                    }
                ],
                "leave_records": [],
                "documents": [
                    {
                        "id": "E10002-BCF-01",
                        "category": "Benefit Change",
                        "title": "Benefit Change Form - Dental Opt-Out"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u14",
        instruction="Andrian Roberts (E99999) has been terminated and needs final off-boarding verification. Confirm his signed NDA documentation is on file and validate his benefit enrollments were properly cleared during termination.",
        actions=[
            Action(name="get_document_compliance_status", kwargs={"employee_id": "E99999"}),
            Action(name="get_benefits_enrollment", kwargs={"employee_id": "E99999"}),
            Action(name="get_employee_profile", kwargs={"employee_id": "E99999"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E99999",
                    "first_name": "Andrian",
                    "last_name": "Roberts",
                    "preferred_name": "Andrian",
                    "date_of_birth": "1992-07-15",
                    "gender": "Male",
                    "ethnicity_code": "W",
                    "nationality": "UK",
                    "marital_status": "Single",
                    "hire_date": "2025-06-24",
                    "termination_date": "2025-06-30",
                    "status": "Terminated",
                    "position_id": "POS3007",
                    "department_id": "DEPT1003",
                    "level_id": "L.2",
                    "manager_id": "E10003",
                    "work_location": "San Francisco HQ",
                    "work_email": "andrian.roberts@example.com",
                    "work_phone": "+1-415-555-0199",
                    "compensation_id": "COMP2999",
                    "benefit_plan_ids": [

                    ],
                    "performance_review_ids": [],
                    "skills": [
                        "Go",
                        "Kubernetes"
                    ],
                    "role_description": "Backend Engineer (contract-to-hire).",
                    "notes": "",
                    "compensation_history": [
                        {
                            "compensation_id": "COMP9999",
                            "employee_id": "E99999",
                            "base_salary": 120000,
                            "currency": "USD",
                            "bonus_target_pct": 12,
                            "equity_grant": 9000,
                            "effective_date": "2025-06-24"
                        }
                    ],
                    "performance_reviews": [],
                    "leave_records": [
                        {
                            "leave_id": "LV9999",
                            "employee_id": "E99999",
                            "leave_type": "Sabbatical",
                            "start_date": "2025-09-01",
                            "end_date": "2025-12-01",
                            "status": "Pending"
                        }
                    ],
                    "documents": []
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u15",
        instruction="Process a promotion for Amelia Garcia (E10003) to job level L.4, effective 2025-08-01. Her new salary will be $170,000. You'll need to log a 'Promotion' review, upload the 'Promotion Letter' (doc ID E10003-001) to her file, and ensure she is enrolled in the Medical - PPO plan (BEN4001). For verification, retrieve her updated employee profile.",
        actions=[
            Action(
                name="update_employee_job_level",
                kwargs={"employee_id": "E10003", "new_level": "L.4"},
            ),
            Action(
                name="update_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "new_comp": {
                        "compensation_id": "COMP2012",
                        "base_salary": 170000,
                        "currency": "USD",
                        "effective_date": "2025-08-01",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10003",
                    "review_data": {
                        "review_id": "PR5026",
                        "type": "Promotion",
                        "rating": "Exceeds",
                        "date": "2025-08-01",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-001",
                        "category": "Promotion",
                        "title": "Promotion Letter to L.4",
                    },
                },
            ),
            Action(
                name="enroll_in_benefit",
                kwargs={"employee_id": "E10003", "benefit_id": "BEN4001"},
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10003",
                "first_name": "Amelia",
                "last_name": "Garcia",
                "preferred_name": "Amy",
                "date_of_birth": "1990-11-22",
                "gender": "Female",
                "ethnicity_code": "H",
                "nationality": "US",
                "marital_status": "Partnered",
                "hire_date": "2019-06-10",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3006",
                "department_id": "DEPT1005",
                "level_id": "L.4",
                "manager_id": "E10001",
                "work_location": "Remote – Austin, TX",
                "work_email": "amelia.garcia@example.com",
                "work_phone": "+1-737-555-0188",
                "compensation_id": "COMP2003",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4003",
                    "BEN4004"
                ],
                "performance_review_ids": [
                    "PR5003",
                    "PR5010",
                    "PR5026"
                ],
                "skills": [
                    "TypeScript",
                    "React",
                    "Accessibility"
                ],
                "role_description": "Senior Front-end Engineer on the web platform team.",
                "notes": "On parental leave 2024-11-01 → 2025-02-01.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2003",
                        "employee_id": "E10003",
                        "base_salary": 145000,
                        "currency": "USD",
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "effective_date": "2024-07-01"
                    },
                    {
                        "compensation_id": "COMP2012",
                        "base_salary": 170000,
                        "currency": "USD",
                        "effective_date": "2025-08-01",
                        "employee_id": "E10003"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5003",
                        "employee_id": "E10003",
                        "period_start": "2023-07-01",
                        "period_end": "2023-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10001",
                        "summary": "Led UI redesign improving conversion by 10%."
                    },
                    {
                        "review_id": "PR5010",
                        "employee_id": "E10003",
                        "period_start": "2024-01-01",
                        "period_end": "2024-06-30",
                        "rating": "Pending",
                        "manager_id": "E10001",
                        "summary": "On leave; review deferred."
                    },
                    {
                        "review_id": "PR5026",
                        "type": "Promotion",
                        "rating": "Exceeds",
                        "date": "2025-08-01",
                        "employee_id": "E10003"
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV6001",
                        "employee_id": "E10003",
                        "leave_type": "Parental",
                        "start_date": "2024-11-01",
                        "end_date": "2025-02-01",
                        "status": "Scheduled"
                    }
                ],
                "documents": [
                    {
                        "id": "E10003-001",
                        "category": "Promotion",
                        "title": "Promotion Letter to L.4"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u16",
        instruction="Ensure documentation compliance for two Engineering department employees with upcoming leave. Sophia Nguyen (E10001) has parental leave scheduled and Rahul Singh (E10004) has vacation scheduled. Both must have complete leave documentation on file including Leave Request Forms and Manager Approvals. Upload any missing documentation and confirm both employees have proper documentation compliance.",
        actions=[
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {
                        "id": "E10001-001",
                        "category": "Leave Request Form",
                        "title": "Leave Request Form for LV7001",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {
                        "id": "E10001-002",
                        "category": "Manager Approval",
                        "title": "Manager Approval for LV7001",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10004",
                    "document_data": {
                        "id": "E10004-001",
                        "category": "Leave Request Form",
                        "title": "Leave Request Form for LV6002",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10004",
                    "document_data": {
                        "id": "E10004-002",
                        "category": "Manager Approval",
                        "title": "Manager Approval for LV6002",
                    },
                },
            ),
            Action(name="get_document_compliance_status", kwargs={"employee_id": "E10001"}),
            Action(name="get_document_compliance_status", kwargs={"employee_id": "E10004"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10004",
                "first_name": "Rahul",
                "last_name": "Singh",
                "preferred_name": "Rahul",
                "date_of_birth": "1988-05-02",
                "gender": "Male",
                "ethnicity_code": "A",
                "nationality": "IN",
                "marital_status": "Married",
                "hire_date": "2022-02-14",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3007",
                "department_id": "DEPT1001",
                "level_id": "L.2",
                "manager_id": "E10003",
                "work_location": "Remote – Bangalore",
                "work_email": "rahul.singh@example.com",
                "work_phone": "+91-80-5550-1122",
                "compensation_id": "COMP2004",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4003"
                ],
                "performance_review_ids": [
                    "PR5004",
                    "PR5009"
                ],
                "skills": [
                    "Go",
                    "Kubernetes",
                    "CI/CD"
                ],
                "role_description": "Backend Engineer focusing on micro-services.",
                "notes": "Visa sponsored (H-1B).",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2004",
                        "employee_id": "E10004",
                        "base_salary": 118000,
                        "currency": "USD",
                        "bonus_target_pct": 10,
                        "equity_grant": 8000,
                        "effective_date": "2022-02-14"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5004",
                        "employee_id": "E10004",
                        "period_start": "2023-01-01",
                        "period_end": "2023-12-31",
                        "rating": "Meets",
                        "manager_id": "E10003",
                        "summary": "Solid contributor; needs mentorship on architecture."
                    },
                    {
                        "review_id": "PR5009",
                        "employee_id": "E10004",
                        "period_start": "2024-01-01",
                        "period_end": "2024-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10003",
                        "summary": "Exceeds performance"
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV6002",
                        "employee_id": "E10004",
                        "leave_type": "Vacation",
                        "start_date": "2025-07-12",
                        "end_date": "2025-07-26",
                        "status": "Taken"
                    }
                ],
                "documents": [
                    {
                        "id": "E10004-001",
                        "category": "Leave Request Form",
                        "title": "Leave Request Form for LV6002"
                    },
                    {
                        "id": "E10004-002",
                        "category": "Manager Approval",
                        "title": "Manager Approval for LV6002"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u17",
        instruction="Ensure complete onboarding compliance for three key employees: Sophia Nguyen (E10001), Daniel Kim (E10002), and Amelia Garcia (E10003). All employees must have proper benefit enrollments, required legal documentation including NDAs, and any missing documentation must be uploaded. Confirm all three employees meet company onboarding standards.",
        actions=[
            Action(name="get_benefits_enrollment", kwargs={"employee_id": "E10001"}),
            Action(name="get_document_compliance_status", kwargs={"employee_id": "E10001"}),
            Action(name="upload_employee_document", kwargs={"employee_id": "E10001", "document_data": {"id": "E10001-003", "category": "NDA", "title": "Non-Disclosure Agreement"}}),
            Action(name="get_benefits_enrollment", kwargs={"employee_id": "E10002"}),
            Action(name="get_document_compliance_status", kwargs={"employee_id": "E10002"}),
            Action(name="upload_employee_document", kwargs={"employee_id": "E10002", "document_data": {"id": "E10002-002", "category": "NDA", "title": "Non-Disclosure Agreement"}}),
            Action(name="get_benefits_enrollment", kwargs={"employee_id": "E10003"}),
            Action(name="get_document_compliance_status", kwargs={"employee_id": "E10003"}),
            Action(name="upload_employee_document", kwargs={"employee_id": "E10003", "document_data": {"id": "E10003-002", "category": "NDA", "title": "Non-Disclosure Agreement"}}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10001",
                    "first_name": "Sophia",
                    "last_name": "Nguyen",
                    "preferred_name": "Sophia",
                    "date_of_birth": "1978-02-16",
                    "gender": "Female",
                    "ethnicity_code": "W",
                    "nationality": "US",
                    "marital_status": "Married",
                    "hire_date": "2010-08-02",
                    "termination_date": null,
                    "status": "Active",
                    "position_id": "POS3001",
                    "department_id": "DEPT1001",
                    "level_id": "L.C",
                    "manager_id": null,
                    "work_location": "San Francisco HQ",
                    "work_email": "sophia.nguyen@example.com",
                    "work_phone": "+1-415-555-0100",
                    "compensation_id": "COMP2001",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN4003"
                    ],
                    "performance_review_ids": [
                        "PR5001",
                        "PR5009"
                    ],
                    "skills": [
                        "Leadership",
                        "Cloud Architecture",
                        "Python"
                    ],
                    "role_description": "Chief Technology Officer overseeing all engineering functions.",
                    "notes": "Founder-level equity grant.",
                    "compensation_history": [
                        {
                            "compensation_id": "COMP2001",
                            "employee_id": "E10001",
                            "base_salary": 325000,
                            "currency": "USD",
                            "bonus_target_pct": 30,
                            "equity_grant": 75000,
                            "effective_date": "2025-01-01"
                        }
                    ],
                    "performance_reviews": [
                        {
                            "review_id": "PR5001",
                            "employee_id": "E10001",
                            "period_start": "2024-01-01",
                            "period_end": "2024-12-31",
                            "rating": "Exceeds",
                            "manager_id": "null",
                            "summary": "Delivered cloud migration ahead of schedule."
                        },
                        {
                            "review_id": "PR5009",
                            "employee_id": "E10001",
                            "period_start": "2024-01-01",
                            "period_end": "2024-12-31",
                            "rating": "Exceeds",
                            "manager_id": "E10003",
                            "summary": "Exceeds performance"
                        }
                    ],
                    "leave_records": [
                        {
                            "leave_id": "LV7001",
                            "employee_id": "E10001",
                            "leave_type": "Parental",
                            "start_date": "2025-07-01",
                            "end_date": "2026-02-01",
                            "status": "Scheduled"
                        }
                    ],
                    "documents": []
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u18",
        instruction="Process a batch salary update for our senior leadership, effective 2025-09-01. Update salaries to: Sophia Nguyen (E10001) to $350,000 with new compensation record COMP2013; Daniel Kim (E10002) to $225,000 with compensation record COMP2014; and Amelia Garcia (E10003) to $160,000 with compensation record COMP2015. Each employee must receive a formal Compensation Update Letter documenting their new terms. Confirm the salary updates by retrieving Amelia Garcia's updated profile.",
        actions=[
            Action(
                name="update_employee_compensation",
                kwargs={
                    "employee_id": "E10001",
                    "new_comp": {
                        "compensation_id": "COMP2013",
                        "base_salary": 350000,
                        "currency": "USD",
                        "effective_date": "2025-09-01",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {
                        "id": "E10001-001",
                        "category": "Compensation",
                        "title": "Compensation Update Letter",
                    },
                },
            ),
            Action(
                name="update_employee_compensation",
                kwargs={
                    "employee_id": "E10002",
                    "new_comp": {
                        "compensation_id": "COMP2014",
                        "base_salary": 225000,
                        "currency": "USD",
                        "effective_date": "2025-09-01",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10002",
                    "document_data": {
                        "id": "E10002-001",
                        "category": "Compensation",
                        "title": "Compensation Update Letter",
                    },
                },
            ),
            Action(
                name="update_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "new_comp": {
                        "compensation_id": "COMP2015",
                        "base_salary": 160000,
                        "currency": "USD",
                        "effective_date": "2025-09-01",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-001",
                        "category": "Compensation",
                        "title": "Compensation Update Letter",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
           {
                "employee_id": "E10003",
                "first_name": "Amelia",
                "last_name": "Garcia",
                "preferred_name": "Amy",
                "date_of_birth": "1990-11-22",
                "gender": "Female",
                "ethnicity_code": "H",
                "nationality": "US",
                "marital_status": "Partnered",
                "hire_date": "2019-06-10",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3006",
                "department_id": "DEPT1005",
                "level_id": "L.3",
                "manager_id": "E10001",
                "work_location": "Remote – Austin, TX",
                "work_email": "amelia.garcia@example.com",
                "work_phone": "+1-737-555-0188",
                "compensation_id": "COMP2003",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4003",
                    "BEN4004"
                ],
                "performance_review_ids": [
                    "PR5003",
                    "PR5010"
                ],
                "skills": [
                    "TypeScript",
                    "React",
                    "Accessibility"
                ],
                "role_description": "Senior Front-end Engineer on the web platform team.",
                "notes": "On parental leave 2024-11-01 → 2025-02-01.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2003",
                        "employee_id": "E10003",
                        "base_salary": 145000,
                        "currency": "USD",
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "effective_date": "2024-07-01"
                    },
                    {
                        "compensation_id": "COMP2015",
                        "base_salary": 160000,
                        "currency": "USD",
                        "effective_date": "2025-09-01",
                        "employee_id": "E10003"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5003",
                        "employee_id": "E10003",
                        "period_start": "2023-07-01",
                        "period_end": "2023-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10001",
                        "summary": "Led UI redesign improving conversion by 10%."
                    },
                    {
                        "review_id": "PR5010",
                        "employee_id": "E10003",
                        "period_start": "2024-01-01",
                        "period_end": "2024-06-30",
                        "rating": "Pending",
                        "manager_id": "E10001",
                        "summary": "On leave; review deferred."
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV6001",
                        "employee_id": "E10003",
                        "leave_type": "Parental",
                        "start_date": "2024-11-01",
                        "end_date": "2025-02-01",
                        "status": "Scheduled"
                    }
                ],
                "documents": [
                    {
                        "id": "E10003-001",
                        "category": "Compensation",
                        "title": "Compensation Update Letter"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u19",
        instruction="Ensure complete executive onboarding compliance for CTO Sophia Nguyen (E10001). Verify her salary is correctly set at $325,000, confirm she is enrolled in Medical - PPO (BEN4001), and ensure her signed NDA is properly filed. Upload her NDA documentation if missing and verify all compensation and benefit records are accurate.",
        actions=[
            Action(name="get_compensation_records", kwargs={"employee_id": "E10001"}),
            Action(name="get_benefits_enrollment", kwargs={"employee_id": "E10001"}),
            Action(name="get_document_compliance_status", kwargs={"employee_id": "E10001"}),
            Action(name="upload_employee_document", kwargs={"employee_id": "E10001", "document_data": {"id": "E10001-004", "category": "NDA", "title": "Executive Non-Disclosure Agreement"}}),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10001",
                    "first_name": "Sophia",
                    "last_name": "Nguyen",
                    "preferred_name": "Sophia",
                    "date_of_birth": "1978-02-16",
                    "gender": "Female",
                    "ethnicity_code": "W",
                    "nationality": "US",
                    "marital_status": "Married",
                    "hire_date": "2010-08-02",
                    "termination_date": null,
                    "status": "Active",
                    "position_id": "POS3001",
                    "department_id": "DEPT1001",
                    "level_id": "L.C",
                    "manager_id": null,
                    "work_location": "San Francisco HQ",
                    "work_email": "sophia.nguyen@example.com",
                    "work_phone": "+1-415-555-0100",
                    "compensation_id": "COMP2001",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN4003"
                    ],
                    "performance_review_ids": [
                        "PR5001",
                        "PR5009"
                    ],
                    "skills": [
                        "Leadership",
                        "Cloud Architecture",
                        "Python"
                    ],
                    "role_description": "Chief Technology Officer overseeing all engineering functions.",
                    "notes": "Founder-level equity grant.",
                    "compensation_history": [
                        {
                            "compensation_id": "COMP2001",
                            "employee_id": "E10001",
                            "base_salary": 325000,
                            "currency": "USD",
                            "bonus_target_pct": 30,
                            "equity_grant": 75000,
                            "effective_date": "2025-01-01"
                        }
                    ],
                    "performance_reviews": [
                        {
                            "review_id": "PR5001",
                            "employee_id": "E10001",
                            "period_start": "2024-01-01",
                            "period_end": "2024-12-31",
                            "rating": "Exceeds",
                            "manager_id": "null",
                            "summary": "Delivered cloud migration ahead of schedule."
                        },
                        {
                            "review_id": "PR5009",
                            "employee_id": "E10001",
                            "period_start": "2024-01-01",
                            "period_end": "2024-12-31",
                            "rating": "Exceeds",
                            "manager_id": "E10003",
                            "summary": "Exceeds performance"
                        }
                    ],
                    "leave_records": [
                        {
                            "leave_id": "LV7001",
                            "employee_id": "E10001",
                            "leave_type": "Parental",
                            "start_date": "2025-07-01",
                            "end_date": "2026-02-01",
                            "status": "Scheduled"
                        }
                    ],
                    "documents": []
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u20",
        instruction="Perform a batch onboarding audit for four key employees: Sophia Nguyen (E10001), Daniel Kim (E10002), Amelia Garcia (E10003), and Rahul Singh (E10004). You need to verify that all standard onboarding procedures were followed for each of them, including benefit enrollments and document uploads. To confirm the audit has been performed, retrieve the full employee profile for the last person on the list, Rahul Singh (E10004).",
        actions=[
            Action(name="get_employee_profile", kwargs={"employee_id": "E10001"}),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10002"}),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10003"}),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10004"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10004",
                    "first_name": "Rahul",
                    "last_name": "Singh",
                    "preferred_name": "Rahul",
                    "date_of_birth": "1988-05-02",
                    "gender": "Male",
                    "ethnicity_code": "A",
                    "nationality": "IN",
                    "marital_status": "Married",
                    "hire_date": "22022-02-14",
                    "termination_date": null,
                    "status": "Active",
                    "position_id": "POS3007",
                    "department_id": "DEPT1001",
                    "level_id": "L.2",
                    "manager_id": "E10003",
                    "work_location": "Remote – Bangalore",
                    "work_email": "rahul.singh@example.com",
                    "work_phone": "+91-80-5550-1122",
                    "compensation_id": "COMP2004",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4003"
                    ],
                    "performance_review_ids": [
                        "PR5004",
                        "PR5009"
                    ],
                    "skills": [
                        "Go",
                        "Kubernetes",
                        "CI/CD"
                    ],
                    "role_description": "Backend Engineer focusing on micro-services.",
                    "notes": "Visa sponsored (H-1B).",
                    "compensation_history": [
                        {
                            "compensation_id": "COMP2004",
                            "employee_id": "E10004",
                            "base_salary": 118000,
                            "currency": "USD",
                            "bonus_target_pct": 10,
                            "equity_grant": 8000,
                            "effective_date": "2022-02-14"
                        }
                    ],
                    "performance_reviews": [
                        {
                            "review_id": "PR5004",
                            "employee_id": "E10004",
                            "period_start": "2023-01-01",
                            "period_end": "2023-12-31",
                            "rating": "Meets",
                            "manager_id": "E10003",
                            "summary": "Solid contributor; needs mentorship on architecture."
                        },
                        {
                            "review_id": "PR5009",
                            "employee_id": "E10004",
                            "period_start": "2024-01-01",
                            "period_end": "2024-12-31",
                            "rating": "Exceeds",
                            "manager_id": "E10003",
                            "summary": "Exceeds performance"
                        }
                    ],
                    "leave_records": [
                        {
                            "leave_id": "LV6002",
                            "employee_id": "E10004",
                            "leave_type": "Vacation",
                            "start_date": "2025-07-12",
                            "end_date": "2025-07-26",
                            "status": "Taken"
                        }
                    ],
                    "documents": []
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u21",
        instruction="Conduct a comprehensive data integrity audit to verify Amelia Garcia (E10003) has complete and accurate records across all HR systems. The audit must confirm her compensation is current, benefits enrollment is active, performance reviews are up-to-date, and compliance documents are properly filed.",
        actions=[
            Action(name="get_employee_profile", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation_records", kwargs={"employee_id": "E10003"}),
            Action(name="get_benefits_enrollment", kwargs={"employee_id": "E10003"}),
            Action(name="get_performance_review_status", kwargs={"employee_id": "E10003"}),
            Action(name="get_document_compliance_status", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            {
              "employee_id": "E10003",
              "first_name": "Amelia",
              "last_name": "Garcia",
              "preferred_name": "Amy",
              "date_of_birth": "1990-11-22",
              "gender": "Female",
              "ethnicity_code": "H",
              "nationality": "US",
              "marital_status": "Partnered",
              "hire_date": "2019-06-10",
              "termination_date": null,
              "status": "Active",
              "position_id": "POS3006",
              "department_id": "DEPT1005",
              "level_id": "L.3",
              "manager_id": "E10001",
              "work_location": "Remote – Austin, TX",
              "work_email": "amelia.garcia@example.com",
              "work_phone": "+1-737-555-0188",
              "compensation_id": "COMP2003",
              "benefit_plan_ids": [
                "BEN4001",
                "BEN4003",
                "BEN4004"
              ],
              "performance_review_ids": [
                "PR5003",
                "PR5010"
              ],
              "skills": [
                "TypeScript",
                "React",
                "Accessibility"
              ],
              "role_description": "Senior Front-end Engineer on the web platform team.",
              "notes": "On parental leave 2024-11-01 → 2025-02-01.",
              "compensation_history": [
                {
                  "compensation_id": "COMP2003",
                  "employee_id": "E10003",
                  "base_salary": 145000,
                  "currency": "USD",
                  "bonus_target_pct": 15,
                  "equity_grant": 15000,
                  "effective_date": "2024-07-01"
                }
              ],
              "performance_reviews": [
                {
                  "review_id": "PR5003",
                  "employee_id": "E10003",
                  "period_start": "2023-07-01",
                  "period_end": "2023-12-31",
                  "rating": "Exceeds",
                  "manager_id": "E10001",
                  "summary": "Led UI redesign improving conversion by 10%."
                },
                {
                  "review_id": "PR5010",
                  "employee_id": "E10003",
                  "period_start": "2024-01-01",
                  "period_end": "2024-06-30",
                  "rating": "Pending",
                  "manager_id": "E10001",
                  "summary": "On leave; review deferred."
                }
              ],
              "leave_records": [
                {
                  "leave_id": "LV6001",
                  "employee_id": "E10003",
                  "leave_type": "Parental",
                  "start_date": "2024-11-01",
                  "end_date": "2025-02-01",
                  "status": "Scheduled"
                }
              ],
              "documents": []
            }
            """,
            """
            [
              {
                "compensation_id": "COMP2003",
                "employee_id": "E10003",
                "base_salary": 145000,
                "currency": "USD",
                "bonus_target_pct": 15,
                "equity_grant": 15000,
                "effective_date": "2024-07-01"
              }
            ]
            """,
            """
            [
              "BEN4001",
              "BEN4003",
              "BEN4004"
            ]
            """,
            """
            [
              {
                "review_id": "PR5003",
                "employee_id": "E10003",
                "period_start": "2023-07-01",
                "period_end": "2023-12-31",
                "rating": "Exceeds",
                "manager_id": "E10001",
                "summary": "Led UI redesign improving conversion by 10%."
              },
              {
                "review_id": "PR5010",
                "employee_id": "E10003",
                "period_start": "2024-01-01",
                "period_end": "2024-06-30",
                "rating": "Pending",
                "manager_id": "E10001",
                "summary": "On leave; review deferred."
              }
            ]
            """,
            """
            {
              "employee_id": "E10003",
              "status": "No documents on file"
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u22",
        instruction="Update Amelia Garcia's (E10003) compensation to reflect a salary increase to $155,000 USD effective 2025-07-01. Ensure her employee record shows the updated compensation with ID COMP2016, includes a formal review documenting the salary adjustment with ID PR5028, and has proper documentation with the Salary Adjustment Notification (E10003-001) in her file.",
        actions=[
            Action(
                name="update_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "new_comp": {
                        "compensation_id": "COMP2016",
                        "base_salary": 155000,
                        "currency": "USD",
                        "effective_date": "2025-07-01",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10003",
                    "review_data": {
                        "review_id": "PR5028",
                        "type": "Salary Adjustment",
                        "rating": "Approved",
                        "date": "2025-07-01",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-001",
                        "category": "Compensation",
                        "title": "Salary Adjustment Notification",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10003",
                "first_name": "Amelia",
                "last_name": "Garcia",
                "preferred_name": "Amy",
                "date_of_birth": "1990-11-22",
                "gender": "Female",
                "ethnicity_code": "H",
                "nationality": "US",
                "marital_status": "Partnered",
                "hire_date": "2019-06-10",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3006",
                "department_id": "DEPT1005",
                "level_id": "L.3",
                "manager_id": "E10001",
                "work_location": "Remote – Austin, TX",
                "work_email": "amelia.garcia@example.com",
                "work_phone": "+1-737-555-0188",
                "compensation_id": "COMP2003",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4003",
                    "BEN4004"
                ],
                "performance_review_ids": [
                    "PR5003",
                    "PR5010",
                    "PR5028"
                ],
                "skills": [
                    "TypeScript",
                    "React",
                    "Accessibility"
                ],
                "role_description": "Senior Front-end Engineer on the web platform team.",
                "notes": "On parental leave 2024-11-01 → 2025-02-01.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2003",
                        "employee_id": "E10003",
                        "base_salary": 145000,
                        "currency": "USD",
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "effective_date": "2024-07-01"
                    },
                    {
                        "compensation_id": "COMP2016",
                        "base_salary": 155000,
                        "currency": "USD",
                        "effective_date": "2025-07-01",
                        "employee_id": "E10003"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5003",
                        "employee_id": "E10003",
                        "period_start": "2023-07-01",
                        "period_end": "2023-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10001",
                        "summary": "Led UI redesign improving conversion by 10%."
                    },
                    {
                        "review_id": "PR5010",
                        "employee_id": "E10003",
                        "period_start": "2024-01-01",
                        "period_end": "2024-06-30",
                        "rating": "Pending",
                        "manager_id": "E10001",
                        "summary": "On leave; review deferred."
                    },
                    {
                        "review_id": "PR5028",
                        "type": "Salary Adjustment",
                        "rating": "Approved",
                        "date": "2025-07-01",
                        "employee_id": "E10003"
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV6001",
                        "employee_id": "E10003",
                        "leave_type": "Parental",
                        "start_date": "2024-11-01",
                        "end_date": "2025-02-01",
                        "status": "Scheduled"
                    }
                ],
                "documents": [
                    {
                        "id": "E10003-001",
                        "category": "Compensation",
                        "title": "Salary Adjustment Notification"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u23",
        instruction="Determine Daniel Kim's (E10002) eligibility for promotion based on performance standards. Company policy requires his latest performance review rating to be 'Exceeds' for promotion approval. If eligibility criteria are not met, the promotion process must be formally halted.",
        actions=[
            Action(name="get_employee_profile", kwargs={"employee_id": "E10002"}),
            Action(name="get_performance_review_status", kwargs={"employee_id": "E10002"}),
            Action(name="update_employee_status", kwargs={"employee_id": "E10002", "new_status": "Active - Promotion Ineligible"}),
        ],
        outputs=[
            """
            {
              "employee_id": "E10002",
              "first_name": "Daniel",
              "last_name": "Kim",
              "preferred_name": "Dan",
              "date_of_birth": "1982-09-04",
              "gender": "Male",
              "ethnicity_code": "A",
              "nationality": "US",
              "marital_status": "Single",
              "hire_date": "2015-03-17",
              "termination_date": null,
              "status": "Active",
              "position_id": "POS3004",
              "department_id": "DEPT1002",
              "level_id": "L.5",
              "manager_id": "E10012",
              "work_location": "New York Office",
              "work_email": "dan.kim@example.com",
              "work_phone": "+1‑212‑555‑0144",
              "compensation_id": "COMP2002",
              "benefit_plan_ids": [
                "BEN4001",
                "BEN4002"
              ],
              "performance_review_ids": [
                "PR5002"
              ],
              "skills": [
                "Sales Strategy",
                "CRM",
                "Negotiation"
              ],
              "role_description": "Regional VP of Sales for the Eastern territory.",
              "notes": "High performer—President's Club 2023."
            }
            """,
            """
            [
              {
                "review_id": "PR5002",
                "employee_id": "E10002",
                "period_start": "2024-01-01",
                "period_end": "2024-03-31",
                "rating": "Meets",
                "manager_id": "E10012",
                "summary": "On track to hit Q2 quota."
              }
            ]
            """,
            """
            {
              "success": "Employee E10002 status updated to Active - Promotion Ineligible"
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u24",
        instruction="Close the Engineering Intern position (POS3014) that will no longer be filled. The system must reflect this position as closed and no longer appear in the department's open positions list.",
        actions=[
            Action(name="get_open_positions", kwargs={"department_id": "DEPT1001"}),
            Action(name="close_position", kwargs={"position_id": "POS3014"}),
            Action(name="get_open_positions", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
              {
                "position_id": "POS3014",
                "title": "Engineering Intern",
                "department_id": "DEPT1001",
                "status": "Open"
              }
            ]
            """,
            """
            {
              "success": "Position POS3014 closed successfully"
            }
            """,
            """
            []
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u25",
        instruction="Complete Amelia Garcia's (E10003) return to work process following the conclusion of her parental leave (LV6001). Her employee record must reflect successful reintegration with a Return from Leave review (PR5030), proper payroll documentation including Direct Deposit Authorization (E10003-001) and Return to Work form (E10003-002), and a scheduled Compliance Training leave (LV8010) for 2025-07-15 to address missing compliance documents.",
        actions=[
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10003",
                    "review_data": {
                        "review_id": "PR5030",
                        "type": "Return from Leave",
                        "rating": "Positive",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-001",
                        "category": "Payroll",
                        "title": "Direct Deposit Authorization",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-002",
                        "category": "HR Form",
                        "title": "Return to Work Document",
                    },
                },
            ),
            Action(
                name="request_leave",
                kwargs={
                    "employee_id": "E10003",
                    "leave_data": {
                        "leave_id": "LV8010",
                        "type": "Compliance Training",
                        "start_date": "2025-07-15",
                        "end_date": "2025-07-15",
                        "status": "Approved",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10003",
                "first_name": "Amelia",
                "last_name": "Garcia",
                "preferred_name": "Amy",
                "date_of_birth": "1990-11-22",
                "gender": "Female",
                "ethnicity_code": "H",
                "nationality": "US",
                "marital_status": "Partnered",
                "hire_date": "2019-06-10",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3006",
                "department_id": "DEPT1005",
                "level_id": "L.3",
                "manager_id": "E10001",
                "work_location": "Remote – Austin, TX",
                "work_email": "amelia.garcia@example.com",
                "work_phone": "+1-737-555-0188",
                "compensation_id": "COMP2003",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4003",
                    "BEN4004"
                ],
                "performance_review_ids": [
                    "PR5003",
                    "PR5010",
                    "PR5030"
                ],
                "skills": [
                    "TypeScript",
                    "React",
                    "Accessibility"
                ],
                "role_description": "Senior Front-end Engineer on the web platform team.",
                "notes": "On parental leave 2024-11-01 → 2025-02-01.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2003",
                        "employee_id": "E10003",
                        "base_salary": 145000,
                        "currency": "USD",
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "effective_date": "2024-07-01"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5003",
                        "employee_id": "E10003",
                        "period_start": "2023-07-01",
                        "period_end": "2023-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10001",
                        "summary": "Led UI redesign improving conversion by 10%."
                    },
                    {
                        "review_id": "PR5010",
                        "employee_id": "E10003",
                        "period_start": "2024-01-01",
                        "period_end": "2024-06-30",
                        "rating": "Pending",
                        "manager_id": "E10001",
                        "summary": "On leave; review deferred."
                    },
                    {
                        "review_id": "PR5030",
                        "type": "Return from Leave",
                        "rating": "Positive",
                        "employee_id": "E10003"
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV6001",
                        "employee_id": "E10003",
                        "leave_type": "Parental",
                        "start_date": "2024-11-01",
                        "end_date": "2025-02-01",
                        "status": "Scheduled"
                    },
                    {
                        "leave_id": "LV8010",
                        "type": "Compliance Training",
                        "start_date": "2025-07-15",
                        "end_date": "2025-07-15",
                        "status": "Approved",
                        "employee_id": "E10003"
                    }
                ],
                "documents": [
                    {
                        "id": "E10003-001",
                        "category": "Payroll",
                        "title": "Direct Deposit Authorization"
                    },
                    {
                        "id": "E10003-002",
                        "category": "HR Form",
                        "title": "Return to Work Document"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u26",
        instruction="Conduct the Q3 departmental audit for the Engineering department (DEPT1001). You need to retrieve their latest performance review status and their diversity metrics for leadership roles (level L.4). Following the audit, you must upload a 'D&I and Performance Audit Report' to the file of the department head, Sophia Nguyen (E10001). For verification, retrieve her updated employee profile.",
        actions=[
            Action(
                name="get_performance_review_status",
                kwargs={"department_id": "DEPT1001"},
            ),
            Action(
                name="get_org_diversity_metrics",
                kwargs={"department_id": "DEPT1001", "level": "L.4"},
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {
                        "id": "E10001-001",
                        "category": "Audit",
                        "title": "D&I & Performance Audit Report",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10001",
                "first_name": "Sophia",
                "last_name": "Nguyen",
                "preferred_name": "Sophia",
                "date_of_birth": "1978-02-16",
                "gender": "Female",
                "ethnicity_code": "W",
                "nationality": "US",
                "marital_status": "Married",
                "hire_date": "2010-08-02",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3001",
                "department_id": "DEPT1001",
                "level_id": "L.C",
                "manager_id": null,
                "work_location": "San Francisco HQ",
                "work_email": "sophia.nguyen@example.com",
                "work_phone": "+1-415-555-0100",
                "compensation_id": "COMP2001",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4002",
                    "BEN4003"
                ],
                "performance_review_ids": [
                    "PR5001",
                    "PR5009"
                ],
                "skills": [
                    "Leadership",
                    "Cloud Architecture",
                    "Python"
                ],
                "role_description": "Chief Technology Officer overseeing all engineering functions.",
                "notes": "Founder-level equity grant.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2001",
                        "employee_id": "E10001",
                        "base_salary": 325000,
                        "currency": "USD",
                        "bonus_target_pct": 30,
                        "equity_grant": 75000,
                        "effective_date": "2025-01-01"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5001",
                        "employee_id": "E10001",
                        "period_start": "2024-01-01",
                        "period_end": "2024-12-31",
                        "rating": "Exceeds",
                        "manager_id": "null",
                        "summary": "Delivered cloud migration ahead of schedule."
                    },
                    {
                        "review_id": "PR5009",
                        "employee_id": "E10001",
                        "period_start": "2024-01-01",
                        "period_end": "2024-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10003",
                        "summary": "Exceeds performance"
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV7001",
                        "employee_id": "E10001",
                        "leave_type": "Parental",
                        "start_date": "2025-07-01",
                        "end_date": "2026-02-01",
                        "status": "Scheduled"
                    }
                ],
                "documents": [
                    {
                        "id": "E10001-001",
                        "category": "Audit",
                        "title": "D&I & Performance Audit Report"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u27",
        instruction="We need to process the paperwork for Rahul Singh's (E10004) approved relocation to the San Francisco HQ. Upload the following documents to his file: 'Work Location Update' (doc ID E10004-001), 'Relocation Agreement' (E10004-002), and 'Address Change Form' (E10004-003). Also, log a 'Relocation Review' for him and schedule a 3-day 'Relocation Support' leave starting 2025-07-20. To verify, retrieve his updated employee profile.",
        actions=[
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10004",
                    "document_data": {
                        "id": "E10004-001",
                        "category": "HR Form",
                        "title": "Work Location Update",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10004",
                    "document_data": {
                        "id": "E10004-002",
                        "category": "HR Agreement",
                        "title": "Relocation Agreement",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10004",
                    "document_data": {
                        "id": "E10004-003",
                        "category": "HR Form",
                        "title": "Address Change Form",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10004",
                    "review_data": {
                        "review_id": "PR5031",
                        "type": "Relocation Review",
                        "rating": "Approved",
                        "date": "2025-06-24",
                    },
                },
            ),
            Action(
                name="request_leave",
                kwargs={
                    "employee_id": "E10004",
                    "leave_data": {
                        "leave_id": "LV8011",
                        "type": "Relocation Support",
                        "start_date": "2025-07-20",
                        "end_date": "2025-07-22",
                        "status": "Approved",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10004"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10004",
                "first_name": "Rahul",
                "last_name": "Singh",
                "preferred_name": "Rahul",
                "date_of_birth": "1988-05-02",
                "gender": "Male",
                "ethnicity_code": "A",
                "nationality": "IN",
                "marital_status": "Married",
                "hire_date": "2022-02-14",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3007",
                "department_id": "DEPT1001",
                "level_id": "L.2",
                "manager_id": "E10003",
                "work_location": "Remote – Bangalore",
                "work_email": "rahul.singh@example.com",
                "work_phone": "+91-80-5550-1122",
                "compensation_id": "COMP2004",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4003"
                ],
                "performance_review_ids": [
                    "PR5004",
                    "PR5009",
                    "PR5031"
                ],
                "skills": [
                    "Go",
                    "Kubernetes",
                    "CI/CD"
                ],
                "role_description": "Backend Engineer focusing on micro-services.",
                "notes": "Visa sponsored (H-1B).",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2004",
                        "employee_id": "E10004",
                        "base_salary": 118000,
                        "currency": "USD",
                        "bonus_target_pct": 10,
                        "equity_grant": 8000,
                        "effective_date": "2022-02-14"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5004",
                        "employee_id": "E10004",
                        "period_start": "2023-01-01",
                        "period_end": "2023-12-31",
                        "rating": "Meets",
                        "manager_id": "E10003",
                        "summary": "Solid contributor; needs mentorship on architecture."
                    },
                    {
                        "review_id": "PR5009",
                        "employee_id": "E10004",
                        "period_start": "2024-01-01",
                        "period_end": "2024-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10003",
                        "summary": "Exceeds performance"
                    },
                    {
                        "review_id": "PR5031",
                        "type": "Relocation Review",
                        "rating": "Approved",
                        "date": "2025-06-24",
                        "employee_id": "E10004"
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV6002",
                        "employee_id": "E10004",
                        "leave_type": "Vacation",
                        "start_date": "2025-07-12",
                        "end_date": "2025-07-26",
                        "status": "Taken"
                    },
                    {
                        "leave_id": "LV8011",
                        "type": "Relocation Support",
                        "start_date": "2025-07-20",
                        "end_date": "2025-07-22",
                        "status": "Approved",
                        "employee_id": "E10004"
                    }
                ],
                "documents": [
                    {
                        "id": "E10004-001",
                        "category": "HR Form",
                        "title": "Work Location Update"
                    },
                    {
                        "id": "E10004-002",
                        "category": "HR Agreement",
                        "title": "Relocation Agreement"
                    },
                    {
                        "id": "E10004-003",
                        "category": "HR Form",
                        "title": "Address Change Form"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u28",
        instruction="Ensure all active Engineering department staff have mid-year performance reviews initiated for the 2025-07-01 to 2025-12-31 period. Each review should be marked as 'Pending' status. Confirm completion by verifying all department reviews are properly recorded in the system.",
        actions=[
            Action(
                name="list_department_headcount", kwargs={"department_id": "DEPT1001"}
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10001"}),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10004"}),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10001",
                    "review_data": {
                        "review_id": "PR5032",
                        "type": "Mid-Year Review",
                        "rating": "Pending",
                        "period_start": "2025-07-01",
                        "period_end": "2025-12-31",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10004",
                    "review_data": {
                        "review_id": "PR5034",
                        "type": "Mid-Year Review",
                        "rating": "Pending",
                        "period_start": "2025-07-01",
                        "period_end": "2025-12-31",
                    },
                },
            ),
            Action(
                name="get_performance_review_status",
                kwargs={"department_id": "DEPT1001"},
            ),
        ],
        outputs=[
            """
            [
                {
                    "review_id": "PR5001",
                    "employee_id": "E10001",
                    "period_start": "2024-01-01",
                    "period_end": "2024-12-31",
                    "rating": "Exceeds",
                    "manager_id": "null",
                    "summary": "Delivered cloud migration ahead of schedule."
                },
                {
                    "review_id": "PR5009",
                    "employee_id": "E10001",
                    "period_start": "2024-01-01",
                    "period_end": "2024-12-31",
                    "rating": "Exceeds",
                    "manager_id": "E10003",
                    "summary": "Exceeds performance"
                },
                {
                    "review_id": "PR5032",
                    "type": "Mid-Year Review",
                    "rating": "Pending",
                    "period_start": "2025-07-01",
                    "period_end": "2025-12-31",
                    "employee_id": "E10001"
                },
                {
                    "review_id": "PR5004",
                    "employee_id": "E10004",
                    "period_start": "2023-01-01",
                    "period_end": "2023-12-31",
                    "rating": "Meets",
                    "manager_id": "E10003",
                    "summary": "Solid contributor; needs mentorship on architecture."
                },
                {
                    "review_id": "PR5009",
                    "employee_id": "E10004",
                    "period_start": "2024-01-01",
                    "period_end": "2024-12-31",
                    "rating": "Exceeds",
                    "manager_id": "E10003",
                    "summary": "Exceeds performance"
                },
                {
                    "review_id": "PR5034",
                    "type": "Mid-Year Review",
                    "rating": "Pending",
                    "period_start": "2025-07-01",
                    "period_end": "2025-12-31",
                    "employee_id": "E10004"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u29",
        instruction="As part of a departmental reorganization in the Sales department (DEPT1002), a 'Manager Assignment Form' needs to be added to Daniel Kim's (E10002) employee file. Upload this document with ID E10002-001. For verification, retrieve his full employee profile.",
        actions=[
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10002",
                    "document_data": {
                        "id": "E10002-001",
                        "category": "HR Form",
                        "title": "Manager Assignment Form",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10002",
                "first_name": "Daniel",
                "last_name": "Kim",
                "preferred_name": "Dan",
                "date_of_birth": "1982-09-04",
                "gender": "Male",
                "ethnicity_code": "A",
                "nationality": "US",
                "marital_status": "Single",
                "hire_date": "2015-03-17",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3004",
                "department_id": "DEPT1002",
                "level_id": "L.5",
                "manager_id": "E10012",
                "work_location": "New York Office",
                "work_email": "dan.kim@example.com",
                "work_phone": "+1-212-555-0144",
                "compensation_id": "COMP2002",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4002"
                ],
                "performance_review_ids": [

                ],
                "skills": [
                    "Sales Strategy",
                    "CRM",
                    "Negotiation"
                ],
                "role_description": "Regional VP of Sales for the Eastern territory.",
                "notes": "High performer—President's Club 2023.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2002",
                        "employee_id": "E10002",
                        "base_salary": 210000,
                        "currency": "USD",
                        "bonus_target_pct": 25,
                        "equity_grant": 40000,
                        "effective_date": "2024-04-01"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5002",
                        "employee_id": "E10002",
                        "period_start": "2024-01-01",
                        "period_end": "2024-03-31",
                        "rating": "Meets",
                        "manager_id": "E10012",
                        "summary": "On track to hit Q2 quota."
                    }
                ],
                "leave_records": [],
                "documents": [
                    {
                        "id": "E10002-001",
                        "category": "HR Form",
                        "title": "Manager Assignment Form"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u30",
        instruction="Ensure Daniel Kim (E10002) has proper benefit coverage by verifying his current enrollments and correcting any gaps. He should have Medical - PPO (BEN4001) and Dental (BEN4002) as minimum coverage, but needs Vision (BEN4003) added to match senior level standards. Complete the benefit optimization and confirm the final enrollment status.",
        actions=[
            Action(name="get_employee_profile", kwargs={"employee_id": "E10002"}),
            Action(name="get_benefits_enrollment", kwargs={"employee_id": "E10002"}),
            Action(name="enroll_in_benefit", kwargs={"employee_id": "E10002", "benefit_id": "BEN4003"}),
            Action(name="get_benefits_enrollment", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10002",
                    "benefit_enrollments": [
                        {
                            "benefit_id": "BEN4001",
                            "plan_name": "Medical - PPO",
                            "enrollment_date": "2015-03-17",
                            "status": "Active"
                        },
                        {
                            "benefit_id": "BEN4002",
                            "plan_name": "Dental",
                            "enrollment_date": "2015-03-17",
                            "status": "Active"
                        },
                        {
                            "benefit_id": "BEN4003",
                            "plan_name": "Vision",
                            "enrollment_date": "2025-01-15",
                            "status": "Active"
                        }
                    ]
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u31",
        instruction="We've discovered inconsistencies in our compensation records during an audit. Elena Rodriguez (E10005) and Marcus Chen (E10006) both need compensation adjustments effective immediately. Elena should receive a salary increase to €75,000 (compensation ID COMP2018), and Marcus needs his equity grant updated to 8,000 shares (compensation ID COMP2019). Please review their current compensation histories, implement these corrections, and confirm the changes by retrieving Marcus's updated employee profile.",
        actions=[
            Action(name="get_compensation_records", kwargs={"employee_id": "E10005"}),
            Action(name="get_compensation_records", kwargs={"employee_id": "E10006"}),
            Action(
                name="update_employee_compensation",
                kwargs={
                    "employee_id": "E10005",
                    "new_comp": {
                        "compensation_id": "COMP2018",
                        "base_salary": 75000,
                        "currency": "EUR",
                        "effective_date": "2025-06-24",
                    },
                },
            ),
            Action(
                name="update_employee_compensation",
                kwargs={
                    "employee_id": "E10006",
                    "new_comp": {
                        "compensation_id": "COMP2019",
                        "base_salary": 60000,
                        "currency": "EUR",
                        "bonus_target_pct": 5,
                        "equity_grant": 8000,
                        "effective_date": "2025-06-24",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10006"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10006",
                    "first_name": "Marcus",
                    "last_name": "Chen",
                    "preferred_name": "Marcus",
                    "date_of_birth": "1991-08-12",
                    "gender": "Male",
                    "ethnicity_code": "A",
                    "nationality": "CA",
                    "marital_status": "Married",
                    "hire_date": "2023-11-15",
                    "termination_date": null,
                    "status": "Active",
                    "position_id": "POS3008",
                    "department_id": "DEPT1004",
                    "level_id": "L.4",
                    "manager_id": "E10012",
                    "work_location": "Madrid Office",
                    "work_email": "marcus.chen@example.com",
                    "work_phone": "+1-604-555-0166",
                    "compensation_id": "COMP2006",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN4003"
                    ],
                    "performance_review_ids": [

                    ],
                    "skills": [
                        "Product Strategy",
                        "User Research",
                        "Data Analytics"
                    ],
                    "role_description": "Senior Product Manager leading the analytics platform initiatives.",
                    "notes": "Previously led successful product launches at major tech companies.",
                    "compensation_history": [
                        {
                            "compensation_id": "COMP2006",
                            "employee_id": "E10006",
                            "base_salary": 60000,
                            "currency": "EUR",
                            "bonus_target_pct": 5,
                            "equity_grant": 5000,
                            "effective_date": "2024-09-01"
                        },
                        {
                            "compensation_id": "COMP2019",
                            "base_salary": 60000,
                            "currency": "EUR",
                            "bonus_target_pct": 5,
                            "equity_grant": 8000,
                            "effective_date": "2025-06-24",
                            "employee_id": "E10006"
                        }
                    ],
                    "performance_reviews": [],
                    "leave_records": [],
                    "documents": []
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u32",
        instruction="Our annual compliance audit deadline is approaching and the Engineering department (DEPT1001) needs immediate attention. Each active team member requires a 'Compliance Remediation 2025' document uploaded to their file and a formal 'Compliance Review' performance entry to document audit completion. Please identify all active Engineering employees, process their compliance documentation, and provide a comprehensive performance review summary for the department to confirm everything is properly recorded.",
        actions=[
            Action(
                name="get_performance_review_status",
                kwargs={"department_id": "DEPT1001"},
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {
                        "id": "COMP-2025-E10001",
                        "category": "Compliance",
                        "title": "Compliance Remediation 2025",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10001",
                    "review_data": {
                        "review_id": "PR5035",
                        "type": "Compliance Review",
                        "rating": "Complete",
                        "date": "2025-06-24",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "COMP-2025-E10003",
                        "category": "Compliance",
                        "title": "Compliance Remediation 2025",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10003",
                    "review_data": {
                        "review_id": "PR5036",
                        "type": "Compliance Review",
                        "rating": "Complete",
                        "date": "2025-06-24",
                    },
                },
            ),
            Action(
                name="get_performance_review_status",
                kwargs={"department_id": "DEPT1001"},
            ),
        ],
        outputs=[
            """
            [
                {
                    "review_id": "PR5001",
                    "employee_id": "E10001",
                    "period_start": "2024-01-01",
                    "period_end": "2024-12-31",
                    "rating": "Exceeds",
                    "manager_id": "null",
                    "summary": "Delivered cloud migration ahead of schedule."
                },
                {
                    "review_id": "PR5009",
                    "employee_id": "E10001",
                    "period_start": "2024-01-01",
                    "period_end": "2024-12-31",
                    "rating": "Exceeds",
                    "manager_id": "E10003",
                    "summary": "Exceeds performance"
                },
                {
                    "review_id": "PR5035",
                    "type": "Compliance Review",
                    "rating": "Complete",
                    "date": "2025-06-24",
                    "employee_id": "E10001"
                },
                {
                    "review_id": "PR5003",
                    "employee_id": "E10003",
                    "period_start": "2023-07-01",
                    "period_end": "2023-12-31",
                    "rating": "Exceeds",
                    "manager_id": "E10001",
                    "summary": "Led UI redesign improving conversion by 10%."
                },
                {
                    "review_id": "PR5010",
                    "employee_id": "E10003",
                    "period_start": "2024-01-01",
                    "period_end": "2024-06-30",
                    "rating": "Pending",
                    "manager_id": "E10001",
                    "summary": "On leave; review deferred."
                },
                {
                    "review_id": "PR5036",
                    "type": "Compliance Review",
                    "rating": "Complete",
                    "date": "2025-06-24",
                    "employee_id": "E10003"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u33",
        instruction="Process the financial and compliance paperwork for Amelia Garcia's (E10003) cross-border transfer to the Madrid Office, effective 2025-10-01. You'll need to create a new compensation record for her new salary of €155,000. She also needs to be enrolled in the 'Commuter Stipend – EU' (BEN4005). Finally, please upload her 'Transfer Agreement' (doc ID E10003-001) and 'Work Visa' (E10003-002) to her file. To verify, retrieve her updated employee profile.",
        actions=[
            Action(
                name="update_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "new_comp": {
                        "compensation_id": "COMP2017",
                        "base_salary": 155000,
                        "currency": "EUR",
                        "effective_date": "2025-10-01",
                    },
                },
            ),
            Action(
                name="enroll_in_benefit",
                kwargs={"employee_id": "E10003", "benefit_id": "BEN4005"},
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-001",
                        "category": "Transfer",
                        "title": "Transfer Agreement",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-002",
                        "category": "Compliance",
                        "title": "Work Visa",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10003",
                    "review_data": {
                        "review_id": "PR5038",
                        "type": "Transfer Review",
                        "rating": "Pending",
                        "date": "2025-10-01",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10003",
                "first_name": "Amelia",
                "last_name": "Garcia",
                "preferred_name": "Amy",
                "date_of_birth": "1990-11-22",
                "gender": "Female",
                "ethnicity_code": "H",
                "nationality": "US",
                "marital_status": "Partnered",
                "hire_date": "2019-06-10",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3006",
                "department_id": "DEPT1005",
                "level_id": "L.3",
                "manager_id": "E10001",
                "work_location": "Remote – Austin, TX",
                "work_email": "amelia.garcia@example.com",
                "work_phone": "+1-737-555-0188",
                "compensation_id": "COMP2003",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4003",
                    "BEN4004",
                    "BEN4005"
                ],
                "performance_review_ids": [
                    "PR5003",
                    "PR5010",
                    "PR5038"
                ],
                "skills": [
                    "TypeScript",
                    "React",
                    "Accessibility"
                ],
                "role_description": "Senior Front-end Engineer on the web platform team.",
                "notes": "On parental leave 2024-11-01 → 2025-02-01.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2003",
                        "employee_id": "E10003",
                        "base_salary": 145000,
                        "currency": "USD",
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "effective_date": "2024-07-01"
                    },
                    {
                        "compensation_id": "COMP2017",
                        "base_salary": 155000,
                        "currency": "EUR",
                        "effective_date": "2025-10-01",
                        "employee_id": "E10003"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5003",
                        "employee_id": "E10003",
                        "period_start": "2023-07-01",
                        "period_end": "2023-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10001",
                        "summary": "Led UI redesign improving conversion by 10%."
                    },
                    {
                        "review_id": "PR5010",
                        "employee_id": "E10003",
                        "period_start": "2024-01-01",
                        "period_end": "2024-06-30",
                        "rating": "Pending",
                        "manager_id": "E10001",
                        "summary": "On leave; review deferred."
                    },
                    {
                        "review_id": "PR5038",
                        "type": "Transfer Review",
                        "rating": "Pending",
                        "date": "2025-10-01",
                        "employee_id": "E10003"
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV6001",
                        "employee_id": "E10003",
                        "leave_type": "Parental",
                        "start_date": "2024-11-01",
                        "end_date": "2025-02-01",
                        "status": "Scheduled"
                    }
                ],
                "documents": [
                    {
                        "id": "E10003-001",
                        "category": "Transfer",
                        "title": "Transfer Agreement"
                    },
                    {
                        "id": "E10003-002",
                        "category": "Compliance",
                        "title": "Work Visa"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u34",
        instruction="Our quarterly business review revealed that the Sales (DEPT1002) and Marketing (DEPT1005) departments need immediate performance documentation updates. Both departments require a 'Q4 Performance Summary 2025' document uploaded to track quarterly achievements, and we need comprehensive performance and diversity analysis for strategic planning. Please gather their current performance review status and diversity metrics, then ensure proper documentation is in place. Confirm completion by providing the Marketing department's diversity metrics.",
        actions=[
            Action(
                name="get_performance_review_status",
                kwargs={"department_id": "DEPT1002"},
            ),
            Action(
                name="get_org_diversity_metrics", kwargs={"department_id": "DEPT1002"}
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10002",
                    "document_data": {
                        "id": "Q4-PERF-DEPT1002-2025",
                        "category": "Performance",
                        "title": "Q4 Performance Summary 2025 - Sales Department",
                    },
                },
            ),
            Action(
                name="get_performance_review_status",
                kwargs={"department_id": "DEPT1005"},
            ),
            Action(
                name="get_org_diversity_metrics", kwargs={"department_id": "DEPT1005"}
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "Q4-PERF-DEPT1005-2025",
                        "category": "Performance",
                        "title": "Q4 Performance Summary 2025 - Marketing Department",
                    },
                },
            ),
        ],
        outputs=[
            """
            [
                {
                    "filter_department": "DEPT1005",
                    "filter_level": null,
                    "total_employees_in_filter": 1,
                    "gender_distribution": {
                        "Female": 1
                    },
                    "ethnicity_distribution": {
                        "H": 1
                    }
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u35",
        instruction="Our board has mandated immediate succession planning documentation for key Engineering department (DEPT1001) leadership roles. We need formal succession planning documents prepared for Sophia Nguyen (E10001, CTO) and any other department leads at L.3 level or above. Please confirm their current identities and roles, create the required 'Succession Plan 2025' documentation for each qualified team member, and provide Sophia's complete updated employee profile to verify the succession planning documentation is properly filed.",
        actions=[
            Action(name="get_employee_profile", kwargs={"employee_id": "E10001"}),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10003"}),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {
                        "id": "SUCC-2025-E10001",
                        "category": "Succession",
                        "title": "Succession Plan 2025",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "SUCC-2025-E10003",
                        "category": "Succession",
                        "title": "Succession Plan 2025",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10001",
                "first_name": "Sophia",
                "last_name": "Nguyen",
                "preferred_name": "Sophia",
                "date_of_birth": "1985-03-15",
                "gender": "Female",
                "ethnicity_code": "A",
                "nationality": "US",
                "marital_status": "Single",
                "hire_date": "2020-03-01",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3004",
                "department_id": "DEPT1001",
                "level_id": "L.5",
                "manager_id": null,
                "work_location": "San Francisco, CA",
                "work_email": "sophia.nguyen@example.com",
                "work_phone": "+1-415-555-0123",
                "compensation_id": "COMP2001",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4002",
                    "BEN4003"
                ],
                "performance_review_ids": [
                    "PR5001",
                    "PR5009"
                ],
                "skills": [
                    "System Architecture",
                    "Cloud Infrastructure",
                    "Team Leadership"
                ],
                "role_description": "Chief Technology Officer responsible for overall technical strategy and engineering leadership.",
                "notes": "Led successful cloud migration initiative in 2024.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2001",
                        "employee_id": "E10001",
                        "base_salary": 180000,
                        "currency": "USD",
                        "bonus_target_pct": 25,
                        "equity_grant": 25000,
                        "effective_date": "2024-01-01"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5001",
                        "employee_id": "E10001",
                        "period_start": "2024-01-01",
                        "period_end": "2024-12-31",
                        "rating": "Exceeds",
                        "manager_id": null,
                        "summary": "Delivered cloud migration ahead of schedule."
                    }
                ],
                "leave_records": [],
                "documents": [
                    {
                        "id": "SUCC-2025-E10001",
                        "category": "Succession",
                        "title": "Succession Plan 2025"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u36",
        instruction="Due to new data privacy regulations, we need to ensure our CTO Sophia Nguyen (E10001) has acknowledged the updated company policies. Update the Code of Conduct document (CDOC-002) to reflect compliance with the 2025 data privacy law and confirm that Sophia has formally acknowledged these changes. Verify all documentation is properly recorded in her employee profile.",
        actions=[
            Action(
                name="update_company_document_content",
                kwargs={
                    "doc_id": "CDOC-002",
                    "new_content": "Updated Code of Conduct reflecting new data privacy law, 2025.",
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {
                        "id": "E10001-001",
                        "category": "Compliance",
                        "title": "Data Privacy Acknowledgment 2025",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10001",
                "first_name": "Sophia",
                "last_name": "Nguyen",
                "preferred_name": "Sophia",
                "date_of_birth": "1978-02-16",
                "gender": "Female",
                "ethnicity_code": "W",
                "nationality": "US",
                "marital_status": "Married",
                "hire_date": "2010-08-02",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3001",
                "department_id": "DEPT1001",
                "level_id": "L.C",
                "manager_id": null,
                "work_location": "San Francisco HQ",
                "work_email": "sophia.nguyen@example.com",
                "work_phone": "+1-415-555-0100",
                "compensation_id": "COMP2001",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4002",
                    "BEN4003"
                ],
                "performance_review_ids": [
                    "PR5001",
                    "PR5009"
                ],
                "skills": [
                    "Leadership",
                    "Cloud Architecture",
                    "Python"
                ],
                "role_description": "Chief Technology Officer overseeing all engineering functions.",
                "notes": "Founder-level equity grant.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2001",
                        "employee_id": "E10001",
                        "base_salary": 325000,
                        "currency": "USD",
                        "bonus_target_pct": 30,
                        "equity_grant": 75000,
                        "effective_date": "2025-01-01"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5001",
                        "employee_id": "E10001",
                        "period_start": "2024-01-01",
                        "period_end": "2024-12-31",
                        "rating": "Exceeds",
                        "manager_id": "null",
                        "summary": "Delivered cloud migration ahead of schedule."
                    },
                    {
                        "review_id": "PR5009",
                        "employee_id": "E10001",
                        "period_start": "2024-01-01",
                        "period_end": "2024-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10003",
                        "summary": "Exceeds performance"
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV7001",
                        "employee_id": "E10001",
                        "leave_type": "Parental",
                        "start_date": "2025-07-01",
                        "end_date": "2026-02-01",
                        "status": "Scheduled"
                    }
                ],
                "documents": [
                    {
                        "id": "E10001-001",
                        "category": "Compliance",
                        "title": "Data Privacy Acknowledgment 2025"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u37",
        instruction="Process the offboarding for Daniel Kim (E10002) from the Sales department, with a final date of 2025-10-31. You need to update his status to 'Offboarded', remove all his benefit enrollments, and upload his 'Exit Interview' form (doc ID E10002-001) and 'Final Pay Statement' (doc ID E10002-002). For verification, retrieve his updated employee profile.",
        actions=[
            Action(
                name="update_employee_status",
                kwargs={"employee_id": "E10002", "new_status": "Offboarded"},
            ),
            Action(
                name="remove_from_benefit",
                kwargs={"employee_id": "E10002", "benefit_id": "BEN4001"},
            ),
            Action(
                name="remove_from_benefit",
                kwargs={"employee_id": "E10002", "benefit_id": "BEN4002"},
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10002",
                    "document_data": {
                        "id": "E10002-001",
                        "category": "Exit",
                        "title": "Exit Interview",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10002",
                    "document_data": {
                        "id": "E10002-002",
                        "category": "Payroll",
                        "title": "Final Pay Statement",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10002",
                "first_name": "Daniel",
                "last_name": "Kim",
                "preferred_name": "Dan",
                "date_of_birth": "1982-09-04",
                "gender": "Male",
                "ethnicity_code": "A",
                "nationality": "US",
                "marital_status": "Single",
                "hire_date": "2015-03-17",
                "termination_date": "2025-10-31",
                "status": "Offboarded",
                "position_id": "POS3004",
                "department_id": "DEPT1002",
                "level_id": "L.5",
                "manager_id": "E10012",
                "work_location": "New York Office",
                "work_email": "dan.kim@example.com",
                "work_phone": "+1-212-555-0144",
                "compensation_id": "COMP2002",
                "benefit_plan_ids": [],
                "performance_review_ids": [
                 "PR5002"
                ],
                "skills": [
                    "Sales Strategy",
                    "CRM",
                    "Negotiation"
                ],
                "role_description": "Regional VP of Sales for the Eastern territory.",
                "notes": "High performer—President's Club 2023.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2002",
                        "employee_id": "E10002",
                        "base_salary": 210000,
                        "currency": "USD",
                        "bonus_target_pct": 25,
                        "equity_grant": 40000,
                        "effective_date": "2024-04-01"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5002",
                        "employee_id": "E10002",
                        "period_start": "2024-01-01",
                        "period_end": "2024-03-31",
                        "rating": "Meets",
                        "manager_id": "E10012",
                        "summary": "On track to hit Q2 quota."
                    }
                ],
                "leave_records": [],
                "documents": [
                    {
                        "id": "E10002-001",
                        "category": "Exit",
                        "title": "Exit Interview"
                    },
                    {
                        "id": "E10002-002",
                        "category": "Payroll",
                        "title": "Final Pay Statement"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u38",
        instruction="Elena Rodriguez (E10005) recently joined and may not have complete benefits coverage. Ensure she has access to our standard employee benefits package including medical, dental, and retirement plans. Address any enrollment gaps and document the resolution for compliance purposes. Confirm her profile reflects complete benefits coverage.",
        actions=[
            Action(name="get_benefits_enrollment", kwargs={"employee_id": "E10005"}),
            Action(
                name="enroll_in_benefit",
                kwargs={"employee_id": "E10005", "benefit_id": "BEN4002"},
            ),
            Action(
                name="enroll_in_benefit",
                kwargs={"employee_id": "E10005", "benefit_id": "BEN4003"},
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10005",
                    "document_data": {
                        "id": "E10005-001",
                        "category": "Benefits",
                        "title": "Retroactive Enrollment Notice 2025",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10005"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10005",
                "first_name": "Elena",
                "last_name": "Rodriguez",
                "preferred_name": "Elena",
                "date_of_birth": "1995-01-30",
                "gender": "Female",
                "ethnicity_code": "H",
                "nationality": "ES",
                "marital_status": "Single",
                "hire_date": "2024-09-01",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3010",
                "department_id": "DEPT1004",
                "level_id": "L.1",
                "manager_id": "E10011",
                "work_location": "Madrid Office",
                "work_email": "elena.rodriguez@example.com",
                "work_phone": "+34-91-555-0200",
                "compensation_id": "COMP2005",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4005",
                    "BEN4002",
                    "BEN4003"
                ],
                "performance_review_ids": [],
                "skills": [
                    "Financial Modeling",
                    "SQL",
                    "Excel"
                ],
                "role_description": "Junior Financial Analyst supporting quarterly forecasts.",
                "notes": "Recent graduate—IE Business School.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2005",
                        "employee_id": "E10005",
                        "base_salary": 72000,
                        "currency": "EUR",
                        "bonus_target_pct": 5,
                        "equity_grant": 2000,
                        "effective_date": "2024-09-01"
                    }
                ],
                "performance_reviews": [],
                "leave_records": [],
                "documents": [
                    {
                        "id": "E10005-001",
                        "category": "Benefits",
                        "title": "Retroactive Enrollment Notice 2025"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u39",
        instruction="Our new cross-functional initiative requires formal assignment of project leads Sophia Nguyen (E10001) from Engineering and Elena Rodriguez (E10005) from Finance. Ensure proper documentation of their project responsibilities and complete initial project readiness assessments. Verify that Sophia's employee record accurately reflects her new project leadership role.",
        actions=[
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {
                        "id": "E10001-001",
                        "category": "Project",
                        "title": "Project Assignment Letter 2025",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10001",
                    "review_data": {
                        "review_id": "PR5039",
                        "type": "Project Launch Review",
                        "rating": "Complete",
                        "date": "2025-06-24",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10005",
                    "document_data": {
                        "id": "E10005-001",
                        "category": "Project",
                        "title": "Project Assignment Letter 2025",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10005",
                    "review_data": {
                        "review_id": "PR5040",
                        "type": "Project Launch Review",
                        "rating": "Complete",
                        "date": "2025-06-24",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10001",
                "first_name": "Sophia",
                "last_name": "Nguyen",
                "preferred_name": "Sophia",
                "date_of_birth": "1978-02-16",
                "gender": "Female",
                "ethnicity_code": "W",
                "nationality": "US",
                "marital_status": "Married",
                "hire_date": "2010-08-02",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3001",
                "department_id": "DEPT1001",
                "level_id": "L.C",
                "manager_id": null,
                "work_location": "San Francisco HQ",
                "work_email": "sophia.nguyen@example.com",
                "work_phone": "+1-415-555-0100",
                "compensation_id": "COMP2001",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4002",
                    "BEN4003"
                ],
                "performance_review_ids": [
                    "PR5001",
                    "PR5009",
                    "PR5039"
                ],
                "skills": [
                    "Leadership",
                    "Cloud Architecture",
                    "Python"
                ],
                "role_description": "Chief Technology Officer overseeing all engineering functions.",
                "notes": "Founder-level equity grant.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2001",
                        "employee_id": "E10001",
                        "base_salary": 325000,
                        "currency": "USD",
                        "bonus_target_pct": 30,
                        "equity_grant": 75000,
                        "effective_date": "2025-01-01"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR5001",
                        "employee_id": "E10001",
                        "period_start": "2024-01-01",
                        "period_end": "2024-12-31",
                        "rating": "Exceeds",
                        "manager_id": "null",
                        "summary": "Delivered cloud migration ahead of schedule."
                    },
                    {
                        "review_id": "PR5009",
                        "employee_id": "E10001",
                        "period_start": "2024-01-01",
                        "period_end": "2024-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10003",
                        "summary": "Exceeds performance"
                    },
                    {
                        "review_id": "PR5039",
                        "type": "Project Launch Review",
                        "rating": "Complete",
                        "date": "2025-06-24",
                        "employee_id": "E10001"
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV7001",
                        "employee_id": "E10001",
                        "leave_type": "Parental",
                        "start_date": "2025-07-01",
                        "end_date": "2026-02-01",
                        "status": "Scheduled"
                    }
                ],
                "documents": [
                    {
                        "id": "E10001-001",
                        "category": "Project",
                        "title": "Project Assignment Letter 2025"
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="u40",
        instruction="A mandatory business continuity drill is being conducted for all Madrid Office staff from November 1-7, 2025. Prepare Amelia Garcia (E10003), Elena Rodriguez (E10005), and Marcus Chen (E10006) for temporary remote work arrangements during this period. Ensure all necessary leave requests, documentation, and compliance reviews are completed for a smooth transition. Verify that Marcus Chen's record accurately reflects all required changes.",
        actions=[
            Action(name="get_employee_profile", kwargs={"employee_id": "E10006"}),
            Action(
                name="request_leave",
                kwargs={
                    "employee_id": "E10003",
                    "leave_data": {
                        "type": "Business Continuity",
                        "start_date": "2025-11-01",
                        "end_date": "2025-11-07",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-RWA",
                        "category": "HR Form",
                        "title": "Remote Work Agreement",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10003",
                    "review_data": {
                        "type": "Continuity Drill Review",
                        "rating": "Complete",
                        "date": "2025-11-08",
                    },
                },
            ),
            Action(
                name="request_leave",
                kwargs={
                    "employee_id": "E10005",
                    "leave_data": {
                        "type": "Business Continuity",
                        "start_date": "2025-11-01",
                        "end_date": "2025-11-07",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10005",
                    "document_data": {
                        "id": "E10005-RWA",
                        "category": "HR Form",
                        "title": "Remote Work Agreement",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10005",
                    "review_data": {
                        "type": "Continuity Drill Review",
                        "rating": "Complete",
                        "date": "2025-11-08",
                    },
                },
            ),
            Action(
                name="request_leave",
                kwargs={
                    "employee_id": "E10006",
                    "leave_data": {
                        "type": "Business Continuity",
                        "start_date": "2025-11-01",
                        "end_date": "2025-11-07",
                    },
                },
            ),
            Action(
                name="upload_employee_document",
                kwargs={
                    "employee_id": "E10006",
                    "document_data": {
                        "id": "E10006-RWA",
                        "category": "HR Form",
                        "title": "Remote Work Agreement",
                    },
                },
            ),
            Action(
                name="submit_performance_review",
                kwargs={
                    "employee_id": "E10006",
                    "review_data": {
                        "type": "Continuity Drill Review",
                        "rating": "Complete",
                        "date": "2025-11-08",
                    },
                },
            ),
            Action(name="get_employee_profile", kwargs={"employee_id": "E10006"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10006",
                "first_name": "Marcus",
                "last_name": "Chen",
                "preferred_name": "Marcus",
                "date_of_birth": "1991-08-12",
                "gender": "Male",
                "ethnicity_code": "A",
                "nationality": "CA",
                "marital_status": "Married",
                "hire_date": "2023-11-15",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3008",
                "department_id": "DEPT1004",
                "level_id": "L.4",
                "manager_id": "E10012",
                "work_location": "Madrid Office",
                "work_email": "marcus.chen@example.com",
                "work_phone": "+1-604-555-0166",
                "compensation_id": "COMP2006",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4002",
                    "BEN4003"
                ],
                "performance_review_ids": [
                    "PR5011",
                    "PR5043"
                ],
                "skills": [
                    "Product Strategy",
                    "User Research",
                    "Data Analytics"
                ],
                "role_description": "Senior Product Manager leading the analytics platform initiatives.",
                "notes": "Previously led successful product launches at major tech companies.",
                "compensation_history": [
                    {
                        "compensation_id": "COMP2006",
                        "employee_id": "E10006",
                        "base_salary": 60000,
                        "currency": "EUR",
                        "bonus_target_pct": 5,
                        "equity_grant": 5000,
                        "effective_date": "2024-09-01"
                    }
                ],
                "performance_reviews": [
                    {
                        "review_id": "PR_NEW_1",
                        "type": "Continuity Drill Review",
                        "rating": "Complete",
                        "date": "2025-11-08",
                        "employee_id": "E10006"
                    }
                ],
                "leave_records": [
                    {
                        "leave_id": "LV_NEW_1",
                        "type": "Business Continuity",
                        "start_date": "2025-11-01",
                        "end_date": "2025-11-07",
                        "employee_id": "E10006"
                    }
                ],
                "documents": [
                    {
                        "id": "E10006-RWA",
                        "category": "HR Form",
                        "title": "Remote Work Agreement"
                    }
                ]
            }
            """
        ],
    ),
]
