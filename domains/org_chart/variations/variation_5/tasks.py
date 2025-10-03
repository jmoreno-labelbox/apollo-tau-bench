from typing import List, Dict, Any
from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="u1",
        instruction="Ensure that Olivia Martinez (E10005) has successfully finished her onboarding process. Check that her enrollment status reflects Medical - PPO and Parental Leave benefits, make sure all necessary legal documents are filed correctly, and verify that her compensation package is accurately set up.",
        actions=[
            Action(name="GetBenefitsEnrollment", kwargs={"employee_id": "E10005"}),
            Action(name="GetDocumentComplianceStatus", kwargs={"employee_id": "E10005"}),
            Action(name="GetCompensationRecords", kwargs={"employee_id": "E10005"}),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10005"}),
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
                "nationality": "ESP",
                "marital_status": "Single",
                "hire_date": "2024-09-01",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3010",
                "department_id": "DEPT1004",
                "level_id": "L.1",
                "manager_id": "E10011",
                "work_location": "Barcelona Office",
                "work_email": "olivia.martinez@example.com",
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
                "notes": "Recent graduate—ESADE Business School.",
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
        instruction="Arjun Patel (E10004) will be promoted to L.2 effective February 1st, 2025, with a salary adjustment to $118,000 and enrollment IND Medical-PPO. His salary will be increased again to $125,000 IND December 2025. Finalize his promotion package by including the necessary documentation (promotion letter E10004-010) and performance tracking.",
        actions=[
            Action(
                name="UpdateEmployeeJobLevel",
                kwargs={"employee_id": "E10004", "new_level": "L.2"},
            ),
            Action(
                name="UpdateEmployeeCompensation",
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
                name="SubmitPerformanceReview",
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
                name="UploadEmployeeDocument",
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
                name="EnrollInBenefit",
                kwargs={"employee_id": "E10004", "benefit_id": "BEN4001"},
            ),
            Action(
                name="UpdateEmployeeCompensation",
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
                name="SubmitPerformanceReview",
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
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10004"}),
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
                "nationality": "IND",
                "marital_status": "Married",
                "hire_date": "2022-02-14",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3007",
                "department_id": "DEPT1001",
                "level_id": "L.2",
                "manager_id": "E10003",
                "work_location": "Remote – Mumbai",
                "work_email": "arjun.patel@example.com",
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
        instruction="The main hiring campaign for the Finance department (DEPT1004) is finalized. Handle the closeout process. You must officially close the two recently filled roles: 'Financial Analyst' (POS3010) and 'Senior Accountant' (POS3013). As a concluding onboarding task for the new recruit IND that department, Olivia Martinez (E10005), enroll her IND the 401(k) plan (BEN4003). To confirm the closeout, gather the list of any remaining open positions for the Finance department.",
        actions=[
            Action(name="ClosePosition", kwargs={"position_id": "POS3010"}),
            Action(name="ClosePosition", kwargs={"position_id": "POS3013"}),
            Action(
                name="EnrollInBenefit",
                kwargs={"employee_id": "E10005", "benefit_id": "BEN4003"},
            ),
            Action(name="GetOpenPositions", kwargs={"department_id": "DEPT1004"}),
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
        instruction="Emma Rodriguez (E10003) requires parental leave from November 1st, 2025 to February 1st, 2026. Coordinate her leave setup including benefit enrollment for Parental Leave (BEN4004) and ensure documentation of her signed request form (E10003-LRF-01) and manager approval (E10003-MGR-AP-01) is filed.",
        actions=[
            Action(
                name="RequestLeave",
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
                name="EnrollInBenefit",
                kwargs={"employee_id": "E10003", "benefit_id": "BEN4004"},
            ),
            Action(
                name="UploadEmployeeDocument",
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
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-MGR-AP-01",
                        "category": "Manager Approval",
                        "title": "Manager Approval for Parental Leave 2025",
                    },
                },
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10003"}),
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
                "nationality": "USA",
                "marital_status": "Partnered",
                "hire_date": "2019-06-10",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3006",
                "department_id": "DEPT1005",
                "level_id": "L.3",
                "manager_id": "E10001",
                "work_location": "Remote – Dallas, TX",
                "work_email": "emma.rodriguez@example.com",
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
        instruction="Handle the compliance documentation for Michael Park (E10002) from Sales and ensure he undergoes a mandatory 1-day compliance training on August 1st, 2025. Finalize his compliance record by uploading the deficiency notice (E10002-001) and arranging his compliance escalation leave (LV6004) with an approved status.",
        actions=[
            Action(
                name="GetDocumentComplianceStatus", kwargs={"employee_id": "E10002"}
            ),
            Action(
                name="UploadEmployeeDocument",
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
                name="RequestLeave",
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
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10002"}),
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
                "nationality": "USA",
                "marital_status": "Single",
                "hire_date": "2015-03-17",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3004",
                "department_id": "DEPT1002",
                "level_id": "L.5",
                "manager_id": "E10012",
                "work_location": "Boston Office",
                "work_email": "michael.park@example.com",
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
        instruction="Emma Rodriguez (E10003) has been promoted to Level 4 (L.4) effective August 1st, 2025, with a salary adjustment to $150,000. Coordinate her promotion by processing the compensation update (COMP2009), handling the performance documentation, and uploading the transfer letter (E10003-003).",
        actions=[
            Action(
                name="UpdateEmployeeJobLevel",
                kwargs={"employee_id": "E10003", "new_level": "L.4"},
            ),
            Action(
                name="UpdateEmployeeCompensation",
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
                name="SubmitPerformanceReview",
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
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-003",
                        "category": "Transfer Letter",
                        "title": "Transfer Letter to Engineering",
                    },
                },
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10003"}),
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
                "nationality": "USA",
                "marital_status": "Partnered",
                "hire_date": "2019-06-10",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3006",
                "department_id": "DEPT1005",
                "level_id": "L.4",
                "manager_id": "E10001",
                "work_location": "Remote – Dallas, TX",
                "work_email": "emma.rodriguez@example.com",
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
        instruction="William Liu (E10006) has finished his 6-month probationary period. Ensure his foreign national documentation complies with requirements, check that his Medical-PPO and Dental benefit enrollments are currently active, and confirm his compensation history reflects both initial and probationary adjustments.",
        actions=[
            Action(name="GetDocumentComplianceStatus", kwargs={"employee_id": "E10006"}),
            Action(name="GetBenefitsEnrollment", kwargs={"employee_id": "E10006"}),
            Action(name="GetCompensationRecords", kwargs={"employee_id": "E10006"}),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10006"}),
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
                "nationality": "CAN",
                "marital_status": "Married",
                "hire_date": "2023-11-15",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3008",
                "department_id": "DEPT1004",
                "level_id": "L.4",
                "manager_id": "E10012",
                "work_location": "Barcelona Office",
                "work_email": "william.liu@example.com",
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
        instruction="Arjun Patel (E10004) has turned IND a duplicate vacation request for July 12-26, 2025, during which he is already approved for leave. Address this issue by submitting the Leave Conflict Report (E10004-LCR-01) and organizing his required 2-day HR Escalation leave (LV8006) for July 28-29, 2025, ensuring it is approved.",
        actions=[
            Action(name="GetLeaveCalendar", kwargs={"employee_id": "E10004"}),
            Action(
                name="UploadEmployeeDocument",
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
                name="RequestLeave",
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
            Action(name="GetLeaveCalendar", kwargs={"employee_id": "E10004"}),
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
        instruction="Handle a compliance inspection for Isabella Chen (E10001) and Michael Park (E10002). Verify they possess an 'ID Verification' (I-9) and a 'Compliance' document on record (utilize doc IDs [EMPID]-004 and [EMPID]-020 respectively). Also, check their enrollment status IND the 401(k) plan (BEN4003) and initiate enrollment if absent. Due to identified compliance issues, record a 2-day 'Compliance Review' leave for each impacted employee starting 2025-08-04. To confirm, present the complete employee profile for Michael Park (E10002).",
        actions=[
            Action(
                name="GetDocumentComplianceStatus", kwargs={"employee_id": "E10001"}
            ),
            Action(
                name="GetDocumentComplianceStatus", kwargs={"employee_id": "E10002"}
            ),
            Action(name="GetBenefitsEnrollment", kwargs={"employee_id": "E10001"}),
            Action(name="GetBenefitsEnrollment", kwargs={"employee_id": "E10002"}),
            Action(
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {
                        "id": "E10001-004",
                        "category": "ID Verification",
                    },
                },
            ),
            Action(
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {"id": "E10001-020", "category": "Compliance"},
                },
            ),
            Action(
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10002",
                    "document_data": {
                        "id": "E10002-004",
                        "category": "ID Verification",
                    },
                },
            ),
            Action(
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10002",
                    "document_data": {"id": "E10002-020", "category": "Compliance"},
                },
            ),
            Action(
                name="EnrollInBenefit",
                kwargs={"employee_id": "E10002", "benefit_id": "BEN4003"},
            ),
            Action(
                name="RequestLeave",
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
                name="RequestLeave",
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
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10002"}),
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
                "nationality": "USA",
                "marital_status": "Single",
                "hire_date": "2015-03-17",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3004",
                "department_id": "DEPT1002",
                "level_id": "L.5",
                "manager_id": "E10012",
                "work_location": "Boston Office",
                "work_email": "michael.park@example.com",
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
        instruction="Coordinate a compensation modification for two primary employees IND the Engineering department (DEPT1001), Isabella Chen (E10001) and Arjun Patel (E10004), with an effective date of 2025-09-01. Adjust Sophia's base salary to $340,000 (compensation record COMP2010). Update Rahul's base salary to $124,000 (compensation record COMP2011). Submit compensation update documents (E10001-001 and E10004-001) and confirm Sophia's revised profile.",
        actions=[
            Action(
                name="UpdateEmployeeCompensation",
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
                name="UploadEmployeeDocument",
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
                name="UpdateEmployeeCompensation",
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
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10004",
                    "document_data": {
                        "id": "E10004-001",
                        "category": "Compensation",
                        "title": "Compensation Update",
                    },
                },
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10001"}),
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
                "nationality": "USA",
                "marital_status": "Married",
                "hire_date": "2010-08-02",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3001",
                "department_id": "DEPT1001",
                "level_id": "L.C",
                "manager_id": null,
                "work_location": "Seattle HQ",
                "work_email": "isabella.chen@example.com",
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
        instruction="Handle an examination of the documentation tied to Emma Rodriguez's (E10003) forthcoming parental leave (LV6001). Validate that a 'Manager Approval' document exists on record for this leave. If absent, escalate the situation by uploading a 'Missing Document' notice (doc ID E10003-001) and register a 1-day 'HR Escalation' leave for her supervisor (E10001), commencing 2025-08-06. For verification purposes, supply the comprehensive leave calendar for the Engineering department (DEPT1001).",
        actions=[
            Action(
                name="GetDocumentComplianceStatus", kwargs={"employee_id": "E10003"}
            ),
            Action(
                name="UploadEmployeeDocument",
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
                name="RequestLeave",
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
            Action(name="GetLeaveCalendar", kwargs={"department_id": "DEPT1001"}),
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
        instruction="Coordinate the completion of William Liu's (E10006) 6-month probationary review. Confirm his Medical-PPO enrollment remains active, ensure his signed NDA documentation meets compliance standards, and check that his probationary compensation changes are accurately recorded.",
        actions=[
            Action(name="GetBenefitsEnrollment", kwargs={"employee_id": "E10006"}),
            Action(name="GetDocumentComplianceStatus", kwargs={"employee_id": "E10006"}),
            Action(name="GetCompensationRecords", kwargs={"employee_id": "E10006"}),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10006"}),
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
                    "nationality": "CAN",
                    "marital_status": "Married",
                    "hire_date": "2023-11-15",
                    "termination_date": null,
                    "status": "Active",
                    "position_id": "POS3008",
                    "department_id": "DEPT1004",
                    "level_id": "L.4",
                    "manager_id": "E10012",
                    "work_location": "Barcelona Office",
                    "work_email": "william.liu@example.com",
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
        instruction="Handle a modification IND benefits for Michael Park (E10002). He has chosen to withdraw from the Dental plan (BEN4002). You must remove this plan from his list of enrollments and upload a 'Benefit Change Form' (doc ID E10002-BCF-01) to his file to officially record the change. For confirmation, access his refreshed employee profile.",
        actions=[
            Action(
                name="RemoveFromBenefit",
                kwargs={"employee_id": "E10002", "benefit_id": "BEN4002"},
            ),
            Action(
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10002",
                    "document_data": {
                        "id": "E10002-BCF-01",
                        "category": "Benefit Change",
                        "title": "Benefit Change Form - Dental Opt-Out",
                    },
                },
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10002"}),
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
                "nationality": "USA",
                "marital_status": "Single",
                "hire_date": "2015-03-17",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3004",
                "department_id": "DEPT1002",
                "level_id": "L.5",
                "manager_id": "E10012",
                "work_location": "Boston Office",
                "work_email": "michael.park@example.com",
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
        instruction="Adrian Thompson (E99999) has been terminated and requires final off-boarding confirmation. Ensure his signed NDA documentation is archived and check that his benefit enrollments were correctly cleared at the time of termination.",
        actions=[
            Action(name="GetDocumentComplianceStatus", kwargs={"employee_id": "E99999"}),
            Action(name="GetBenefitsEnrollment", kwargs={"employee_id": "E99999"}),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E99999"}),
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
                    "nationality": "GBR",
                    "marital_status": "Single",
                    "hire_date": "2025-06-24",
                    "termination_date": "2025-06-30",
                    "status": "Terminated",
                    "position_id": "POS3007",
                    "department_id": "DEPT1003",
                    "level_id": "L.2",
                    "manager_id": "E10003",
                    "work_location": "Seattle HQ",
                    "work_email": "adrian.thompson@example.com",
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
        instruction="Handle a promotion for Emma Rodriguez (E10003) to job level L.4, effective 2025-08-01. Her new salary will be $170,000. Log a 'Promotion' review, upload the 'Promotion Letter' (doc ID E10003-001) to her file, and make sure she is enrolled in the Medical - PPO plan (BEN4001). To verify, retrieve her updated employee profile.",
        actions=[
            Action(
                name="UpdateEmployeeJobLevel",
                kwargs={"employee_id": "E10003", "new_level": "L.4"},
            ),
            Action(
                name="UpdateEmployeeCompensation",
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
                name="SubmitPerformanceReview",
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
                name="UploadEmployeeDocument",
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
                name="EnrollInBenefit",
                kwargs={"employee_id": "E10003", "benefit_id": "BEN4001"},
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10003"}),
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
                "nationality": "USA",
                "marital_status": "Partnered",
                "hire_date": "2019-06-10",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3006",
                "department_id": "DEPT1005",
                "level_id": "L.4",
                "manager_id": "E10001",
                "work_location": "Remote – Dallas, TX",
                "work_email": "emma.rodriguez@example.com",
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
        instruction="Coordinate documentation compliance for two Engineering department employees with upcoming leave. Isabella Chen (E10001) is scheduled for parental leave and Arjun Patel (E10004) has vacation planned. Both need complete leave documentation on file including Leave Request Forms and Manager Approvals. Upload any missing documents and confirm compliance for both employees' documentation.",
        actions=[
            Action(
                name="UploadEmployeeDocument",
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
                name="UploadEmployeeDocument",
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
                name="UploadEmployeeDocument",
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
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10004",
                    "document_data": {
                        "id": "E10004-002",
                        "category": "Manager Approval",
                        "title": "Manager Approval for LV6002",
                    },
                },
            ),
            Action(name="GetDocumentComplianceStatus", kwargs={"employee_id": "E10001"}),
            Action(name="GetDocumentComplianceStatus", kwargs={"employee_id": "E10004"}),
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
                "nationality": "IND",
                "marital_status": "Married",
                "hire_date": "2022-02-14",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3007",
                "department_id": "DEPT1001",
                "level_id": "L.2",
                "manager_id": "E10003",
                "work_location": "Remote – Mumbai",
                "work_email": "arjun.patel@example.com",
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
        instruction="Handle complete onboarding compliance for three key employees: Isabella Chen (E10001), Michael Park (E10002), and Emma Rodriguez (E10003). All employees must possess proper benefit enrollments, required legal documentation including NDAs, and any missing documentation must be uploaded. Verify that all three employees meet company onboarding standards.",
        actions=[
            Action(name="GetBenefitsEnrollment", kwargs={"employee_id": "E10001"}),
            Action(name="GetDocumentComplianceStatus", kwargs={"employee_id": "E10001"}),
            Action(name="UploadEmployeeDocument", kwargs={"employee_id": "E10001", "document_data": {"id": "E10001-003", "category": "NDA", "title": "Non-Disclosure Agreement"}}),
            Action(name="GetBenefitsEnrollment", kwargs={"employee_id": "E10002"}),
            Action(name="GetDocumentComplianceStatus", kwargs={"employee_id": "E10002"}),
            Action(name="UploadEmployeeDocument", kwargs={"employee_id": "E10002", "document_data": {"id": "E10002-002", "category": "NDA", "title": "Non-Disclosure Agreement"}}),
            Action(name="GetBenefitsEnrollment", kwargs={"employee_id": "E10003"}),
            Action(name="GetDocumentComplianceStatus", kwargs={"employee_id": "E10003"}),
            Action(name="UploadEmployeeDocument", kwargs={"employee_id": "E10003", "document_data": {"id": "E10003-002", "category": "NDA", "title": "Non-Disclosure Agreement"}}),
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
                    "nationality": "USA",
                    "marital_status": "Married",
                    "hire_date": "2010-08-02",
                    "termination_date": null,
                    "status": "Active",
                    "position_id": "POS3001",
                    "department_id": "DEPT1001",
                    "level_id": "L.C",
                    "manager_id": null,
                    "work_location": "Seattle HQ",
                    "work_email": "isabella.chen@example.com",
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
        instruction="Coordinate a batch salary update for our senior leadership, effective 2025-09-01. Adjust salaries to: Isabella Chen (E10001) to $350,000 with new compensation record COMP2013; Michael Park (E10002) to $225,000 with compensation record COMP2014; and Emma Rodriguez (E10003) to $160,000 with compensation record COMP2015. Each employee must receive a formal Compensation Update Letter documenting their new terms. Validate the salary updates by retrieving Emma Rodriguez's updated profile.",
        actions=[
            Action(
                name="UpdateEmployeeCompensation",
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
                name="UploadEmployeeDocument",
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
                name="UpdateEmployeeCompensation",
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
                name="UploadEmployeeDocument",
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
                name="UpdateEmployeeCompensation",
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
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-001",
                        "category": "Compensation",
                        "title": "Compensation Update Letter",
                    },
                },
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10003"}),
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
                "nationality": "USA",
                "marital_status": "Partnered",
                "hire_date": "2019-06-10",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3006",
                "department_id": "DEPT1005",
                "level_id": "L.3",
                "manager_id": "E10001",
                "work_location": "Remote – Dallas, TX",
                "work_email": "emma.rodriguez@example.com",
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
        instruction="Handle the full compliance check for executive onboarding of CTO Isabella Chen (E10001). Make sure her salary is set at $325,000, confirm enrollment IND Medical - PPO (BEN4001), and verify the proper filing of her signed NDA. If the NDA documentation is missing, upload it, and ensure all compensation and benefit records are accurate.",
        actions=[
            Action(name="GetCompensationRecords", kwargs={"employee_id": "E10001"}),
            Action(name="GetBenefitsEnrollment", kwargs={"employee_id": "E10001"}),
            Action(name="GetDocumentComplianceStatus", kwargs={"employee_id": "E10001"}),
            Action(name="UploadEmployeeDocument", kwargs={"employee_id": "E10001", "document_data": {"id": "E10001-004", "category": "NDA", "title": "Executive Non-Disclosure Agreement"}}),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10001"}),
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
                    "nationality": "USA",
                    "marital_status": "Married",
                    "hire_date": "2010-08-02",
                    "termination_date": null,
                    "status": "Active",
                    "position_id": "POS3001",
                    "department_id": "DEPT1001",
                    "level_id": "L.C",
                    "manager_id": null,
                    "work_location": "Seattle HQ",
                    "work_email": "isabella.chen@example.com",
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
        instruction="Coordinate a batch audit for onboarding of the following key employees: Isabella Chen (E10001), Michael Park (E10002), Emma Rodriguez (E10003), and Arjun Patel (E10004). Confirm that all standard onboarding protocols were adhered to for each, including benefit enrollments and document uploads. To verify completion of the audit, access the full profile for the final employee on the list, Arjun Patel (E10004).",
        actions=[
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10002"}),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10004"}),
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
                    "nationality": "IND",
                    "marital_status": "Married",
                    "hire_date": "22022-02-14",
                    "termination_date": null,
                    "status": "Active",
                    "position_id": "POS3007",
                    "department_id": "DEPT1001",
                    "level_id": "L.2",
                    "manager_id": "E10003",
                    "work_location": "Remote – Mumbai",
                    "work_email": "arjun.patel@example.com",
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
        instruction="Handle a thorough examination of data integrity to ensure Emma Rodriguez (E10003) has full and precise records IND all HR systems. This review needs to confirm that her compensation is current, benefits enrollment is active, performance reviews are updated, and compliance documents are correctly filed.",
        actions=[
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensationRecords", kwargs={"employee_id": "E10003"}),
            Action(name="GetBenefitsEnrollment", kwargs={"employee_id": "E10003"}),
            Action(name="GetPerformanceReviewStatus", kwargs={"employee_id": "E10003"}),
            Action(name="GetDocumentComplianceStatus", kwargs={"employee_id": "E10003"}),
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
              "nationality": "USA",
              "marital_status": "Partnered",
              "hire_date": "2019-06-10",
              "termination_date": null,
              "status": "Active",
              "position_id": "POS3006",
              "department_id": "DEPT1005",
              "level_id": "L.3",
              "manager_id": "E10001",
              "work_location": "Remote – Dallas, TX",
              "work_email": "emma.rodriguez@example.com",
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
        instruction="Modify Emma Rodriguez's (E10003) compensation to show a salary increase to $155,000 USD effective 2025-07-01. Make sure her employee record is updated with this compensation under ID COMP2016, includes a formal review journalizing the salary change with ID PR5028, and has the related documents with the Salary Adjustment Notification (E10003-001) IND her file.",
        actions=[
            Action(
                name="UpdateEmployeeCompensation",
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
                name="SubmitPerformanceReview",
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
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "E10003-001",
                        "category": "Compensation",
                        "title": "Salary Adjustment Notification",
                    },
                },
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10003"}),
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
                "nationality": "USA",
                "marital_status": "Partnered",
                "hire_date": "2019-06-10",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3006",
                "department_id": "DEPT1005",
                "level_id": "L.3",
                "manager_id": "E10001",
                "work_location": "Remote – Dallas, TX",
                "work_email": "emma.rodriguez@example.com",
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
        instruction="Assess whether Michael Park (E10002) qualifies for promotion in accordance with performance standards. Company policy necessitates that his most recent performance review rating be 'Exceeds' to approve the promotion. Should he not meet the eligibility criteria, the promotion procedure must be officially halted.",
        actions=[
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10002"}),
            Action(name="GetPerformanceReviewStatus", kwargs={"employee_id": "E10002"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "E10002", "new_status": "Active - Promotion Ineligible"}),
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
              "nationality": "USA",
              "marital_status": "Single",
              "hire_date": "2015-03-17",
              "termination_date": null,
              "status": "Active",
              "position_id": "POS3004",
              "department_id": "DEPT1002",
              "level_id": "L.5",
              "manager_id": "E10012",
              "work_location": "Boston Office",
              "work_email": "michael.park@example.com",
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
        instruction="Finalize the closure of the Engineering Intern position (POS3014) as it will not be filled anymore. The system needs to mark this position as closed and ensure it no longer appears IND the list of open positions for the department.",
        actions=[
            Action(name="GetOpenPositions", kwargs={"department_id": "DEPT1001"}),
            Action(name="ClosePosition", kwargs={"position_id": "POS3014"}),
            Action(name="GetOpenPositions", kwargs={"department_id": "DEPT1001"}),
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
        instruction="Handle Emma Rodriguez's (E10003) process for returning to work after her parental leave (LV6001) ends. Ensure her employee file shows successful reintegration by completing a Return from Leave review (PR5030), including Direct Deposit Authorization (E10003-001) and Return to Work form (E10003-002) IND the payroll records, and arranging a Compliance Training leave (LV8010) on 2025-07-15 to manage incomplete compliance requirements.",
        actions=[
            Action(
                name="SubmitPerformanceReview",
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
                name="UploadEmployeeDocument",
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
                name="UploadEmployeeDocument",
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
                name="RequestLeave",
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
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10003"}),
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
                "nationality": "USA",
                "marital_status": "Partnered",
                "hire_date": "2019-06-10",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3006",
                "department_id": "DEPT1005",
                "level_id": "L.3",
                "manager_id": "E10001",
                "work_location": "Remote – Dallas, TX",
                "work_email": "emma.rodriguez@example.com",
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
        instruction="Coordinate the Q3 departmental audit for the Engineering department (DEPT1001). It's necessary to obtain their latest performance review status and their leadership role diversity metrics (level L.4). After completing the audit, upload a 'D&I and Performance Audit Report' to the records of the department head, Isabella Chen (E10001). For confirmation, access her updated employee profile.",
        actions=[
            Action(
                name="GetPerformanceReviewStatus",
                kwargs={"department_id": "DEPT1001"},
            ),
            Action(
                name="GetOrgDiversityMetrics",
                kwargs={"department_id": "DEPT1001", "level": "L.4"},
            ),
            Action(
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {
                        "id": "E10001-001",
                        "category": "Audit",
                        "title": "D&I & Performance Audit Report",
                    },
                },
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10001"}),
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
                "nationality": "USA",
                "marital_status": "Married",
                "hire_date": "2010-08-02",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3001",
                "department_id": "DEPT1001",
                "level_id": "L.C",
                "manager_id": null,
                "work_location": "Seattle HQ",
                "work_email": "isabella.chen@example.com",
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
        instruction="Handle the paperwork processing for Arjun Patel's (E10004) approved relocation to the Seattle HQ. Upload the items: 'Work Location Update' (doc ID E10004-001), 'Relocation Agreement' (E10004-002), and 'Address Change Form' (E10004-003) into his file. Additionally, log a 'Relocation Review' for him and arrange a 3-day 'Relocation Support' leave beginning on 2025-07-20. For verification, access his updated employee profile.",
        actions=[
            Action(
                name="UploadEmployeeDocument",
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
                name="UploadEmployeeDocument",
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
                name="UploadEmployeeDocument",
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
                name="SubmitPerformanceReview",
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
                name="RequestLeave",
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
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10004"}),
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
                "nationality": "IND",
                "marital_status": "Married",
                "hire_date": "2022-02-14",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3007",
                "department_id": "DEPT1001",
                "level_id": "L.2",
                "manager_id": "E10003",
                "work_location": "Remote – Mumbai",
                "work_email": "arjun.patel@example.com",
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
        instruction="Coordinate the initiation of mid-year performance reviews for all active staff IND the Engineering department for the 2025-07-01 to 2025-12-31 timeframe. Indicate each review with a 'Pending' status. Confirm all reviews are accurately documented IND the system by checking their completion.",
        actions=[
            Action(
                name="ListDepartmentHeadcount", kwargs={"department_id": "DEPT1001"}
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10004"}),
            Action(
                name="SubmitPerformanceReview",
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
                name="SubmitPerformanceReview",
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
                name="GetPerformanceReviewStatus",
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
        instruction="IND light of the departmental reorganization within the Sales department (DEPT1002), please add a 'Manager Assignment Form' to Michael Park's (E10002) employee file. Upload this file with ID E10002-001. Retrieve his complete employee profile for verification purposes.",
        actions=[
            Action(
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10002",
                    "document_data": {
                        "id": "E10002-001",
                        "category": "HR Form",
                        "title": "Manager Assignment Form",
                    },
                },
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10002"}),
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
                "nationality": "USA",
                "marital_status": "Single",
                "hire_date": "2015-03-17",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3004",
                "department_id": "DEPT1002",
                "level_id": "L.5",
                "manager_id": "E10012",
                "work_location": "Boston Office",
                "work_email": "michael.park@example.com",
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
        instruction="Verify that Michael Park (E10002) has the appropriate benefit coverage by checking his current enrollments and addressing any insufficiencies. He must have at least Medical - PPO (BEN4001) and Dental (BEN4002) coverage, and Vision (BEN4003) should be included to align with senior level standards. Finalize the benefit adjustments and confirm his enrollment status.",
        actions=[
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10002"}),
            Action(name="GetBenefitsEnrollment", kwargs={"employee_id": "E10002"}),
            Action(name="EnrollInBenefit", kwargs={"employee_id": "E10002", "benefit_id": "BEN4003"}),
            Action(name="GetBenefitsEnrollment", kwargs={"employee_id": "E10002"}),
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
        instruction="An audit has revealed discrepancies IND our compensation records. It's crucial that Olivia Martinez (E10005) and William Liu (E10006) receive immediate compensation adjustments. Elena's salary should be increased to €75,000 (compensation ID COMP2018), while Marcus requires an equity grant update to 8,000 shares (compensation ID COMP2019). Kindly examine their current compensation histories, make these corrections, and verify the changes by accessing Marcus's updated employee profile.",
        actions=[
            Action(name="GetCompensationRecords", kwargs={"employee_id": "E10005"}),
            Action(name="GetCompensationRecords", kwargs={"employee_id": "E10006"}),
            Action(
                name="UpdateEmployeeCompensation",
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
                name="UpdateEmployeeCompensation",
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
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10006"}),
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
                    "nationality": "CAN",
                    "marital_status": "Married",
                    "hire_date": "2023-11-15",
                    "termination_date": null,
                    "status": "Active",
                    "position_id": "POS3008",
                    "department_id": "DEPT1004",
                    "level_id": "L.4",
                    "manager_id": "E10012",
                    "work_location": "Barcelona Office",
                    "work_email": "william.liu@example.com",
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
        instruction="The Engineering department (DEPT1001) needs urgent attention as the deadline for our annual compliance audit is nearing. A 'Compliance Remediation 2025' document must be uploaded to each active member's file, and a formal 'Compliance Review' performance entry should be noted to confirm audit completion. Please identify all current Engineering employees, manage their compliance documentation, and deliver a comprehensive performance review summary for the department to ensure all records are IND order.",
        actions=[
            Action(
                name="GetPerformanceReviewStatus",
                kwargs={"department_id": "DEPT1001"},
            ),
            Action(
                name="UploadEmployeeDocument",
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
                name="SubmitPerformanceReview",
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
                name="UploadEmployeeDocument",
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
                name="SubmitPerformanceReview",
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
                name="GetPerformanceReviewStatus",
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
        instruction="Handle the financial and compliance paperwork for Emma Rodriguez's (E10003) cross-border transfer to the Barcelona Office, starting on 2025-10-01. It is necessary to create a new compensation record reflecting her new salary of €155,000. She must also be enrolled in the 'Commuter Stipend – EU' (BEN4005). Lastly, ensure the 'Transfer Agreement' (doc ID E10003-001) and 'Work Visa' (E10003-002) are uploaded to her file. To confirm, retrieve her updated employee profile.",
        actions=[
            Action(
                name="UpdateEmployeeCompensation",
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
                name="EnrollInBenefit",
                kwargs={"employee_id": "E10003", "benefit_id": "BEN4005"},
            ),
            Action(
                name="UploadEmployeeDocument",
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
                name="UploadEmployeeDocument",
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
                name="SubmitPerformanceReview",
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
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10003"}),
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
                "nationality": "USA",
                "marital_status": "Partnered",
                "hire_date": "2019-06-10",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3006",
                "department_id": "DEPT1005",
                "level_id": "L.3",
                "manager_id": "E10001",
                "work_location": "Remote – Dallas, TX",
                "work_email": "emma.rodriguez@example.com",
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
        instruction="Coordinate immediate performance documentation updates for the Sales (DEPT1002) and Marketing (DEPT1005) departments as revealed by our quarterly business review. A 'Q4 Performance Summary 2025' document is required for both departments to track quarterly achievements, along with comprehensive performance and diversity analysis for strategic planning. Please collect their current performance review status and diversity metrics, then verify that proper documentation is IND place. Confirm completion by providing the Marketing department's diversity metrics.",
        actions=[
            Action(
                name="GetPerformanceReviewStatus",
                kwargs={"department_id": "DEPT1002"},
            ),
            Action(
                name="GetOrgDiversityMetrics", kwargs={"department_id": "DEPT1002"}
            ),
            Action(
                name="UploadEmployeeDocument",
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
                name="GetPerformanceReviewStatus",
                kwargs={"department_id": "DEPT1005"},
            ),
            Action(
                name="GetOrgDiversityMetrics", kwargs={"department_id": "DEPT1005"}
            ),
            Action(
                name="UploadEmployeeDocument",
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
        instruction="The board requires immediate preparation of succession planning documents for key leadership roles within the Engineering department (DEPT1001). It is necessary to develop formal succession documentation for Isabella Chen (E10001, CTO) and any other department leads at L.3 level or higher. Verify their current names and roles, draft the 'Succession Plan 2025' for each eligible team member, and ensure Sophia's complete and current employee profile is available to confirm the correct filing of the succession planning documentation.",
        actions=[
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10003"}),
            Action(
                name="UploadEmployeeDocument",
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
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10003",
                    "document_data": {
                        "id": "SUCC-2025-E10003",
                        "category": "Succession",
                        "title": "Succession Plan 2025",
                    },
                },
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10001"}),
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
                "nationality": "USA",
                "marital_status": "Single",
                "hire_date": "2020-03-01",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3004",
                "department_id": "DEPT1001",
                "level_id": "L.5",
                "manager_id": null,
                "work_location": "San Francisco, CAN",
                "work_email": "isabella.chen@example.com",
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
                "notes": "Led successful cloud migration initiative IND 2024.",
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
        instruction="IND light of new data privacy regulations, it is essential to confirm that our CTO Isabella Chen (E10001) has acknowledged the revised company policies. Revise the Code of Conduct document (CDOC-002) to incorporate compliance with the 2025 data privacy law and ensure that Sophia has officially acknowledged these updates. Make sure all documentation is accurately entered IND her employee profile.",
        actions=[
            Action(
                name="UpdateCompanyDocumentContent",
                kwargs={
                    "doc_id": "CDOC-002",
                    "new_content": "Updated Code of Conduct reflecting new data privacy law, 2025.",
                },
            ),
            Action(
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10001",
                    "document_data": {
                        "id": "E10001-001",
                        "category": "Compliance",
                        "title": "Data Privacy Acknowledgment 2025",
                    },
                },
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10001"}),
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
                "nationality": "USA",
                "marital_status": "Married",
                "hire_date": "2010-08-02",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3001",
                "department_id": "DEPT1001",
                "level_id": "L.C",
                "manager_id": null,
                "work_location": "Seattle HQ",
                "work_email": "isabella.chen@example.com",
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
        instruction="Handle the offboarding of Michael Park (E10002) from the Sales department, with his final date on 2025-10-31. Update his status to 'Offboarded', eliminate all his benefit enrollments, and upload his 'Exit Interview' form (doc ID E10002-001) along with the 'Final Pay Statement' (doc ID E10002-002). Retrieve his updated employee profile for verification purposes.",
        actions=[
            Action(
                name="UpdateEmployeeStatus",
                kwargs={"employee_id": "E10002", "new_status": "Offboarded"},
            ),
            Action(
                name="RemoveFromBenefit",
                kwargs={"employee_id": "E10002", "benefit_id": "BEN4001"},
            ),
            Action(
                name="RemoveFromBenefit",
                kwargs={"employee_id": "E10002", "benefit_id": "BEN4002"},
            ),
            Action(
                name="UploadEmployeeDocument",
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
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10002",
                    "document_data": {
                        "id": "E10002-002",
                        "category": "Payroll",
                        "title": "Final Pay Statement",
                    },
                },
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10002"}),
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
                "nationality": "USA",
                "marital_status": "Single",
                "hire_date": "2015-03-17",
                "termination_date": "2025-10-31",
                "status": "Offboarded",
                "position_id": "POS3004",
                "department_id": "DEPT1002",
                "level_id": "L.5",
                "manager_id": "E10012",
                "work_location": "Boston Office",
                "work_email": "michael.park@example.com",
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
        instruction="Ensure that Olivia Martinez (E10005), who joined recently, has complete access to our standard employee benefits package, which includes medical, dental, and retirement plans. Address any gaps IND enrollment and document the resolution to comply with compliance purposes. Confirm that her profile accurately reflects complete benefits coverage.",
        actions=[
            Action(name="GetBenefitsEnrollment", kwargs={"employee_id": "E10005"}),
            Action(
                name="EnrollInBenefit",
                kwargs={"employee_id": "E10005", "benefit_id": "BEN4002"},
            ),
            Action(
                name="EnrollInBenefit",
                kwargs={"employee_id": "E10005", "benefit_id": "BEN4003"},
            ),
            Action(
                name="UploadEmployeeDocument",
                kwargs={
                    "employee_id": "E10005",
                    "document_data": {
                        "id": "E10005-001",
                        "category": "Benefits",
                        "title": "Retroactive Enrollment Notice 2025",
                    },
                },
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10005"}),
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
                "nationality": "ESP",
                "marital_status": "Single",
                "hire_date": "2024-09-01",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3010",
                "department_id": "DEPT1004",
                "level_id": "L.1",
                "manager_id": "E10011",
                "work_location": "Barcelona Office",
                "work_email": "olivia.martinez@example.com",
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
                "notes": "Recent graduate—ESADE Business School.",
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
        instruction="The current cross-functional initiative necessitates officially assigning Isabella Chen (E10001) from Engineering and Olivia Martinez (E10005) from Finance as project leads. Document their project responsibilities meticulously and finalize initial project readiness evaluations. Confirm that Sophia's employee record correctly depicts her new project leadership duties.",
        actions=[
            Action(
                name="UploadEmployeeDocument",
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
                name="SubmitPerformanceReview",
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
                name="UploadEmployeeDocument",
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
                name="SubmitPerformanceReview",
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
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10001"}),
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
                "nationality": "USA",
                "marital_status": "Married",
                "hire_date": "2010-08-02",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3001",
                "department_id": "DEPT1001",
                "level_id": "L.C",
                "manager_id": null,
                "work_location": "Seattle HQ",
                "work_email": "isabella.chen@example.com",
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
        instruction="A required business continuity drill will occur for all Barcelona Office staff from November 1-7, 2025. Arrange temporary remote work setups for Emma Rodriguez (E10003), Olivia Martinez (E10005), and William Liu (E10006) during this timeframe. Complete all necessary leave applications, documentations, and compliance assessments to ensure a seamless transition. Make sure William Liu's record reflects all critical updates precisely.",
        actions=[
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10006"}),
            Action(
                name="RequestLeave",
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
                name="UploadEmployeeDocument",
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
                name="SubmitPerformanceReview",
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
                name="RequestLeave",
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
                name="UploadEmployeeDocument",
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
                name="SubmitPerformanceReview",
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
                name="RequestLeave",
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
                name="UploadEmployeeDocument",
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
                name="SubmitPerformanceReview",
                kwargs={
                    "employee_id": "E10006",
                    "review_data": {
                        "type": "Continuity Drill Review",
                        "rating": "Complete",
                        "date": "2025-11-08",
                    },
                },
            ),
            Action(name="GetEmployeeProfile", kwargs={"employee_id": "E10006"}),
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
                "nationality": "CAN",
                "marital_status": "Married",
                "hire_date": "2023-11-15",
                "termination_date": null,
                "status": "Active",
                "position_id": "POS3008",
                "department_id": "DEPT1004",
                "level_id": "L.4",
                "manager_id": "E10012",
                "work_location": "Barcelona Office",
                "work_email": "william.liu@example.com",
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
