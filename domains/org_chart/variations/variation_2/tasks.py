from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="res_01",
        instruction="Starting on 2026-05-22, handle the promotion of Emma Rodriguez (E10003) to 'Lead Compliance Officer' (POS4002) at level L.4, which ensures an 8% salary increase. To facilitate her new responsibilities, coordinate the reassignment of Michael Park (E10002) as her direct report. Log a performance evaluation for Amelia under the summary 'Promotion to Lead Compliance Officer.' Retrieve the updated employee information for both to verify.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10003", "updates": {"position_id": "POS4002", "level_id": "L.4", "role_description": "Lead Compliance Officer"}},
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "effective_date": "2026-05-22",
                    "salary_increase_pct": 8,
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Lead Compliance Officer",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10002", "updates": {"manager_id": "E10003"}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10003",
                    "position_id": "POS4002",
                    "level_id": "L.4",
                    "role_description": "Lead Compliance Officer",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                },
                {
                    "employee_id": "E10002",
                    "manager_id": "E10003"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_02",
        instruction="Beginning on 2026-05-25, carry out an equity refresh for Emma Rodriguez (E10003), providing her with an additional $20,000 IND equity. Since this advances her to a new equity tier, alter her role description to 'Principal Engineer', upload her signed 'Equity Grant Agreement' document, and register a performance evaluation with the summary 'Equity refresh and tier promotion.' To acknowledge her manager, Isabella Chen (E10001), for 'Mentorship excellence,' issue a one-time bonus of $1,000. Obtain both updated employee records for confirmation.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10003"}),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "effective_date": "2026-05-25",
                    "equity_increase_amount": 20000,
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Equity refresh and tier promotion.",
                    }
                },
            ),
            Action(name="GetUnusedDocumentId", kwargs={}),
            Action(
                name="AddEmployeeDocument",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10003",
                        "title": "Equity Grant Agreement",
                        "date": "2026-05-25",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "role_description": "Principal Engineer",
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(name="GetUnusedBonusId", kwargs={}),
            Action(
                name="AddBonusPayment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10001",
                        "amount": 1000,
                        "reason": "Mentorship excellence.",
                    }
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10003",
                    "role_description": "Principal Engineer",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                },
                {
                    "employee_id": "E10001"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_03",
        instruction="Handle and authorize a 12-week parental leave for Isabella Chen (E10001) from 2025-08-01 to 2025-10-23. Allocate Emma Rodriguez (E10003) as acting CTO for this period, granting a temporary 5% salary increase. Record a performance assessment for Amelia with the summary 'Acting CTO during S. Nguyen's leave.' To finance these modifications, relocate $50,000 from the Sales department's budget (DEPT1002) to the Engineering department's (DEPT1001). For validation, obtain the updated records for both employees and the Engineering department.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="GetUnusedLeaveId", kwargs={}),
            Action(
                name="RequestLeave",
                kwargs={
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10001",
                        "leave_type": "Parental Leave",
                        "start_date": "2025-08-01",
                        "end_date": "2025-10-23",
                        "status": "Pending",
                    }
                },
            ),
            Action(
                name="UpdateLeaveStatus",
                kwargs={"leave_id": "LV10000", "status": "Approved"},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10003", "updates": {"role_description": "Acting CTO"}},
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-08-01",
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Acting CTO during S. Nguyen's leave.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4950000}},
            ),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7050000}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10001"
                },
                {
                    "employee_id": "E10003",
                    "role_description": "Acting CTO",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "budget": 7050000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_04",
        instruction="Coordinate the termination of Olivia Martinez (E10005), effective 2025-07-01. Adhere to all off-boarding protocols, including resolving her benefits, adjusting her final compensation to zero, and documenting a performance review with the summary 'Termination.' To fill her position, reassign William Liu (E10006) to her former role (POS3010) and modify his role description to 'Senior Financial Analyst.' For validation, acquire both updated employee records.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(
                name="TerminateEmployee",
                kwargs={"employee_id": "E10005", "termination_date": "2025-07-01"},
            ),
            Action(
                name="SetEmployeeBenefits",
                kwargs={"employee_id": "E10005", "benefit_plan_ids": []},
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10005",
                        "base_salary": 0,
                        "bonus_target_pct": 0,
                        "equity_grant": 0,
                        "effective_date": "2025-07-01",
                    }
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10005",
                        "summary": "Termination",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR10000"],
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10006", "updates": {"position_id": "POS3010", "role_description": "Senior Financial Analyst"}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10005",
                    "status": "Terminated",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR10000"]
                },
                {
                    "employee_id": "E10006",
                    "position_id": "POS3010",
                    "role_description": "Senior Financial Analyst"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_05",
        instruction="Starting from 2025-09-01, handle the promotion of Emma Rodriguez (E10003) to the position of Staff Engineer (POS3005) at level L.4, which involves a 10% increase IND her base salary. Record a performance review with the note 'Promotion to Staff Engineer.' To fill her previous role, transfer Michael Park (E10002) to her former position (POS3006). For confirmation, obtain the updated records for both employees.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"position_id": "POS3005", "level_id": "L.4", "role_description": "Staff Engineer"},
                },
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 10,
                    "effective_date": "2025-09-01",
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Staff Engineer",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10002", "updates": {"position_id": "POS3006"}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10003",
                    "position_id": "POS3005",
                    "level_id": "L.4",
                    "role_description": "Staff Engineer",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                },
                {
                    "employee_id": "E10002",
                    "position_id": "POS3006"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_06",
        instruction="Commencing on 2025-08-01, adjust the monthly employee cost for the Medical-PPO plan (BEN4001) to $170. Simultaneously, coordinate the promotion of Isabella Chen (E10001) to 'Lead Engineer' (POS3002) at level L.A, which includes a 10% salary hike. Enroll Adrian Thompson (E99999) IND the revised Medical-PPO plan. Document a performance review for Sophia with the summary 'Promotion to Lead Engineer.' To support the promotion, allocate $50,000 from the HR department's budget (DEPT1003) to the Engineering department's (DEPT1001). For validation, retrieve the updated employee records for both Andrian and Sophia, as well as the updated record for the Engineering department.",
        actions=[
            Action(
                name="UpdateBenefitPlan",
                kwargs={"benefit_plan_id": "BEN4001", "updates": {"employee_cost_monthly": 170}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E99999"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E99999",
                    "updates": {"benefit_plan_ids": ["BEN9999", "BEN4001"]},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10001"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"position_id": "POS3002", "level_id": "L.A"},
                },
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10001",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 10,
                    "effective_date": "2025-08-01",
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Promotion to Lead Engineer",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5001", "PR10000"],
                    },
                },
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1003"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1003", "updates": {"budget": 750000}},
            ),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7050000}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E99999"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E99999",
                    "benefit_plan_ids": ["BEN9999", "BEN4001"]
                },
                {
                    "employee_id": "E10001",
                    "position_id": "POS3002",
                    "level_id": "L.A",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5001", "PR10000"]
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "budget": 7050000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_07",
        instruction="Starting on 2025-06-24, integrate a new HR Business Partner, Sarah Johnson, into the HR department (DEPT1003). Her salary will be $110,000, and she must be enrolled in the benefits (BEN4001, BEN4002). Her supervisor will be Emma Rodriguez (E10003). Record a performance evaluation for Mary with the summary 'New hire onboarding.' To finance the new position, allocate $120,000 from the Sales department's budget (DEPT1002) to HR. For validation, obtain the revised records for Sarah Johnson and the HR department.",
        actions=[
            Action(name="GetUnusedEmployeeId", kwargs={}),
            Action(
                name="CreateEmployee",
                kwargs={
                    "employee": {
                        "employee_id": "E10000",
                        "first_name": "Mary",
                        "last_name": "Smith",
                        "status": "Active",
                        "hire_date": "2025-06-24",
                        "department_id": "DEPT1003",
                        "manager_id": "E10003",
                        "benefit_plan_ids": ["BEN4001", "BEN4002"],
                        "role_description": "HR Business Partner",
                    }
                },
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10000",
                        "base_salary": 110000,
                        "currency": "USD",
                        "effective_date": "2025-06-24",
                    }
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10000",
                        "summary": "New hire onboarding",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10000",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR10000"],
                    },
                },
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1003"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4880000}},
            ),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1003", "updates": {"budget": 920000}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10000"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1003"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10000",
                    "first_name": "Mary",
                    "last_name": "Smith",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR10000"]
                },
                {
                    "department_id": "DEPT1003",
                    "name": "Human Resources",
                    "budget": 920000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_08",
        instruction="As of 2025-10-15, coordinate an internal relocation and promotion for Emma Rodriguez (E10003) to 'Senior Software Engineer' (POS3009) at level L.3 IND the Engineering department (DEPT1001), with a salary increase of 10%. To replace her previous position, move Arjun Patel (E10004) to her former role (POS3006). Document a performance review for Amelia with the summary 'Promotion and transfer to Engineering.' For confirmation, access the updated employee record for Amelia.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "department_id": "DEPT1001",
                        "position_id": "POS3009",
                        "level_id": "L.3",
                        "role_description": "Senior Software Engineer",
                    },
                },
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 10,
                    "effective_date": "2025-10-15",
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion and transfer to Engineering",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10004", "updates": {"position_id": "POS3006"}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10003",
                "department_id": "DEPT1001",
                "position_id": "POS3009",
                "level_id": "L.3",
                "compensation_id": "COMP10000",
                "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_09",
        instruction="Establish a new 'Vision Plan' (BEN4006) utilizing provider 'VSP' with a monthly fee of $15. Enroll all currently active employees IND the Marketing department (DEPT1005). Transfer Michael Park (E10002) to the Marketing department as part of this and enroll him as well. Record a performance review for Emma Rodriguez (E10003), including the summary 'Benefit rollout and new team member.' For verification purposes, obtain the updated records for Amelia, Daniel, and the Marketing department.",
        actions=[
            Action(
                name="AddBenefitPlan",
                kwargs={
                    "benefit_plan": {
                        "benefit_plan_id": "BEN4006",
                        "name": "Vision Plan",
                        "provider": "VSP",
                        "employee_cost_monthly": 15,
                    }
                },
            ),
            Action(
                name="SearchEmployees",
                kwargs={"filters": {"department_id": "DEPT1005", "status": "Active"}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10003",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4004", "BEN4006"],
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10002", "updates": {"department_id": "DEPT1005"}},
            ),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10002",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4006"],
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Benefit rollout and new team member.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"performance_review_ids": ["PR5003", "PR5010", "PR10000"]},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1005"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10003",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4004", "BEN4006"],
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                },
                {
                    "employee_id": "E10002",
                    "department_id": "DEPT1005",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4006"]
                },
                {
                    "department_id": "DEPT1005",
                    "name": "Marketing"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_10",
        instruction="Approve and handle a one-month unpaid sabbatical for Emma Rodriguez (E10003) from 2025-11-01 to 2025-11-30. Designate Arjun Patel (E10004) as acting team lead and grant him a one-time bonus of $2,500 for 'Acting team lead coverage.' Record a performance review for Amelia with the note 'Unpaid sabbatical approved.' To cover the bonus, raise the Engineering department's (DEPT1001) budget by $2,500. For verification, procure the updated employee records for both Amelia and Rahul, along with the modified Engineering department record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetUnusedLeaveId", kwargs={}),
            Action(
                name="RequestLeave",
                kwargs={
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10003",
                        "leave_type": "Sabbatical",
                        "start_date": "2025-11-01",
                        "end_date": "2025-11-30",
                        "status": "Pending",
                    }
                },
            ),
            Action(
                name="UpdateLeaveStatus",
                kwargs={"leave_id": "LV10000", "status": "Approved"},
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Unpaid sabbatical approved",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"performance_review_ids": ["PR5003", "PR5010", "PR10000"]},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10004", "updates": {"role_description": "Acting Team Lead"}},
            ),
            Action(name="GetUnusedBonusId", kwargs={}),
            Action(
                name="AddBonusPayment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10004",
                        "amount": 2500,
                        "reason": "Acting team lead coverage.",
                    }
                },
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7002500}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10003",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                },
                {
                    "employee_id": "E10004",
                    "role_description": "Acting Team Lead"
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "budget": 7002500
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_11",
        instruction="Handle a 30-day Performance Improvement Plan (PIP) initiation for Michael Park (E10002), starting on 2025-11-01, with the summary '30-day Performance Improvement Plan initiated.' and a 'Needs Improvement' rating. As part of the PIP, reassign him to the Marketing department (DEPT1005), upload his signed 'PIP Agreement' document, and generate a new compensation record to adjust his bonus target to 0%. To facilitate this, allocate $10,000 from the Sales department's budget (DEPT1002) to Marketing. For verification purposes, obtain the updated records for Michael Park and the Marketing department.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10002"}),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "period_start": "2025-11-01",
                        "period_end": "2025-11-30",
                        "rating": "Needs Improvement",
                        "summary": "30-day Performance Improvement Plan initiated.",
                    }
                },
            ),
            Action(name="GetUnusedDocumentId", kwargs={}),
            Action(
                name="AddEmployeeDocument",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10002",
                        "title": "PIP Agreement",
                        "date": "2025-11-01",
                    }
                },
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10002",
                        "bonus_target_pct": 0,
                        "base_salary": 210000,
                        "equity_grant": 40000,
                        "currency": "USD",
                        "effective_date": "2025-11-01",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "department_id": "DEPT1005",
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5002", "PR10000"],
                    },
                },
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1005"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4990000}},
            ),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1005", "updates": {"budget": 1610000}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1005"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10002",
                    "department_id": "DEPT1005",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5002", "PR10000"]
                },
                {
                    "department_id": "DEPT1005",
                    "name": "Marketing",
                    "budget": 1610000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_12",
        instruction="Authorize the request for Isabella Chen (E10001) to commence remote work from 'Remote – Seattle', effective 2025-07-24. Update her work location and upload her signed 'Remote Work Agreement', following which confirm the upload. As part of this team restructuring, adjust Michael Park's (E10002) reporting line to have him report directly to Sophia. Record a performance review for Sophia with the summary 'Remote work transition.' For verification, obtain the updated employee records for both.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10001", "updates": {"work_location": "Remote – Seattle"}},
            ),
            Action(name="GetUnusedDocumentId", kwargs={}),
            Action(
                name="AddEmployeeDocument",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10001",
                        "title": "Remote Work Agreement",
                        "date": "2025-07-24",
                    }
                },
            ),
            Action(name="ListEmployeeDocuments", kwargs={"employee_id": "E10001"}),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Remote work transition",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"performance_review_ids": ["PR5001", "PR10000"]},
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10002", "updates": {"manager_id": "E10001"}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10001",
                    "work_location": "Remote – Seattle",
                    "performance_review_ids": ["PR5001", "PR10000"]
                },
                {
                    "employee_id": "E10002",
                    "manager_id": "E10001"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_13",
        instruction="Handle the extension of Isabella Chen's (E10001) parental leave (LV7001) to 2026-02-15 and modify her status to 'On Leave'. Designate Emma Rodriguez (E10003) to act as interim CTO, which includes granting a temporary 5% salary increase starting on the leave commencement date. Log a performance evaluation for Amelia with the summary 'Acting CTO coverage.' For confirmation, access the updated employee record for Amelia.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="ListEmployeeLeaves", kwargs={"employee_id": "E10001"}),
            Action(
                name="UpdateLeaveRecord",
                kwargs={"leave_id": "LV7001", "updates": {"end_date": "2026-02-15"}},
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10001", "updates": {"status": "On Leave"}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10003", "updates": {"role_description": "Acting CTO"}},
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-07-01",
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Acting CTO coverage.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10003",
                "role_description": "Acting CTO",
                "compensation_id": "COMP10000",
                "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_14",
        instruction="Coordinate the promotion of Michael Park (E10002) to Senior Analyst (POS3012) at level L.2, effective 2025-12-01, with a 7% increase IND base salary. Record a new performance review with an 'Exceeds' rating and the summary 'Promoted to Senior Analyst (L.2).' To acknowledge his manager, William Liu (E10006), for this successful promotion, allocate him a one-time bonus of €1,000 for 'Team development.' For confirmation, access both updated employee records.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10002"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"level_id": "L.2", "position_id": "POS3012", "role_description": "Senior Analyst"},
                },
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10002",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 7,
                    "effective_date": "2025-12-01",
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "rating": "Exceeds",
                        "summary": "Promoted to Senior Analyst (L.2).",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5002", "PR10000"],
                    },
                },
            ),
            Action(name="GetUnusedBonusId", kwargs={}),
            Action(
                name="AddBonusPayment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10006",
                        "amount": 1000,
                        "currency": "EUR",
                        "reason": "Team development",
                    }
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10002",
                    "position_id": "POS3012",
                    "level_id": "L.2",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5002", "PR10000"]
                },
                {
                    "employee_id": "E10006"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_15",
        instruction="Starting 2025-12-01, handle the removal of the 'Vision Plan' (BEN4006) from Isabella Chen's (E10001) benefits and ensure a 'Benefit Change Form' is uploaded to her file. To acknowledge her manager, Emma Rodriguez (E10003), for overseeing this transition, coordinate a one-time bonus of $500 for 'Administrative excellence.' Record a performance review for Sophia with the summary 'Benefit change processed.' Adjust the Engineering department's (DEPT1001) budget by $500 to accommodate the bonus. For verification purposes, obtain both the updated employee records and the Engineering department's revised record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003"]},
                },
            ),
            Action(name="GetUnusedDocumentId", kwargs={}),
            Action(
                name="AddEmployeeDocument",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10001",
                        "title": "Benefit Change Form",
                        "date": "2025-12-01",
                    }
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Benefit change processed",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"performance_review_ids": ["PR5001", "PR10000"]},
                },
            ),
            Action(name="GetUnusedBonusId", kwargs={}),
            Action(
                name="AddBonusPayment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10003",
                        "amount": 500,
                        "reason": "Administrative excellence.",
                    }
                },
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7000500}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10001",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003"],
                    "performance_review_ids": ["PR5001", "PR10000"]
                },
                {
                    "employee_id": "E10003"
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "budget": 7000500
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_16",
        instruction="Coordinate and sanction a 5-day bereavement leave for Michael Park (E10002) from 2025-12-10 to 2025-12-14. Assign Arjun Patel (E10004) as the acting manager during Daniel's absence, which involves a temporary 5% salary increment. Register a performance review for Rahul with the summary 'Acting manager coverage.' For verification, acquire the updated employee records for both Daniel and Rahul.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetUnusedLeaveId", kwargs={}),
            Action(
                name="RequestLeave",
                kwargs={
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10002",
                        "leave_type": "Bereavement Leave",
                        "start_date": "2025-12-10",
                        "end_date": "2025-12-14",
                        "status": "Pending",
                    }
                },
            ),
            Action(
                name="UpdateLeaveStatus",
                kwargs={"leave_id": "LV10000", "status": "Approved"},
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10002", "updates": {"manager_id": "E10004"}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10004"}),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10004",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-12-10",
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "summary": "Acting manager coverage",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5004", "PR5009", "PR10000"],
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10002",
                    "manager_id": "E10004"
                },
                {
                    "employee_id": "E10004",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5004", "PR5009", "PR10000"]
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_17",
        instruction="Starting on 2026-01-01, handle a 3% cost-of-living salary increment for Emma Rodriguez (E10003) and record a performance review with the summary 'COLA applied.' Additionally, within the same audit, allocate a one-time bonus of $2,000 to Michael Park (E10002) for 'cross-functional collaboration.' Allocate $15,000 from the HR department's budget (DEPT1003) to the Sales department's (DEPT1002) to facilitate these adjustments. To ensure accuracy, gather the updated employee records for both and the revised Sales department record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10003"}),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 3,
                    "effective_date": "2026-01-01",
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "COLA applied.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                    },
                },
            ),
            Action(name="GetUnusedBonusId", kwargs={}),
            Action(
                name="AddBonusPayment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10002",
                        "amount": 2000,
                        "reason": "cross-functional collaboration",
                    }
                },
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1003"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1002"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1003", "updates": {"budget": 785000}},
            ),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 5015000}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1002"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                },
                {
                    "employee_id": "E10002"
                },
                {
                    "department_id": "DEPT1002",
                    "name": "Sales",
                    "budget": 5015000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_18",
        instruction="Authorize Michael Park's (E10002) request to work remotely from 'Remote – Dallas', effective starting 2025-07-24. Update his work location information and upload his signed 'Remote Work Agreement'. As a component of the remote work package, coordinate a 5% salary increment for him. Record a performance review noting 'Remote work and compensation updated.' For accuracy verification, obtain his updated employee record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10002"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10002", "updates": {"work_location": "Remote – Dallas"}},
            ),
            Action(name="GetUnusedDocumentId", kwargs={}),
            Action(
                name="AddEmployeeDocument",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10002",
                        "title": "Remote Work Agreement",
                        "date": "2025-07-24",
                    }
                },
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10002",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-07-24",
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Remote work and compensation updated.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5002", "PR10000"],
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10002",
                "work_location": "Remote – Dallas",
                "compensation_id": "COMP10000",
                "performance_review_ids": ["PR5002", "PR10000"]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_19",
        instruction="Register Emma Rodriguez (E10003) and Michael Park (E10002) IND the 'Legal Insurance' plan (BEN9999), commencing on 2025-07-24. Record a performance review once for their supervisor, Isabella Chen (E10001), with the commentary 'Benefit enrollment processed for team.' For verification, access the updated employee records for all three.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10003",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4004", "BEN9999"],
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10002",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN9999"],
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Benefit enrollment processed for team.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"performance_review_ids": ["PR5001", "PR10000"]},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10003",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4004", "BEN9999"]
                },
                {
                    "employee_id": "E10002",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN9999"]
                },
                {
                    "employee_id": "E10001",
                    "performance_review_ids": ["PR5001", "PR10000"]
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_20",
        instruction="Starting 2026-01-01, handle a compensation adjustment for Isabella Chen (E10001), creating a new entry to set her bonus target at 25%. Record a performance review with the summary 'Bonus target adjusted.' To acknowledge her superior, grant a one-time bonus of $5,000 to Emma Rodriguez (E10003) for 'Leadership excellence.' For verification, access the updated employee records for both.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10001"}),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10001",
                        "bonus_target_pct": 25,
                        "base_salary": 325000,
                        "equity_grant": 75000,
                        "currency": "USD",
                        "effective_date": "2026-01-01",
                    }
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Bonus target adjusted",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5001", "PR10000"],
                    },
                },
            ),
            Action(name="GetUnusedBonusId", kwargs={}),
            Action(
                name="AddBonusPayment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10003",
                        "amount": 5000,
                        "reason": "Leadership excellence.",
                    }
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10001",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5001", ""PR10000"]
                },
                {
                    "employee_id": "E10003"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_21",
        instruction="Handle the early return of Sophia Nguyen (E10001) from parental leave (LV7001) on 2025-08-31 by updating her leave record to 'Taken' and changing her status to 'Active'. For successful team management during her leave, coordinate a 5% salary raise for her manager, Amelia Garcia (E10003), and log a performance review with the summary 'Team management bonus.' For confirmation, access Amelia's updated employee record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(
                name="UpdateLeaveRecord",
                kwargs={"leave_id": "LV7001", "updates": {"end_date": "2025-08-31", "status": "Taken"}},
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10001", "updates": {"status": "Active"}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10003"}),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-08-31",
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Team management bonus.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10003",
                "compensation_id": "COMP10000",
                "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_22",
        instruction="Carry out an equity refresh grant for Michael Park (E10002) to take effect on 2026-01-15. Increase his equity grant by $10,000. To document this, log a performance review note with the summary 'Equity refresh of $10,000 granted.' For verification, retrieve his most recent updated compensation record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10002"}),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10002",
                    "compensation_id": "COMP10000",
                    "effective_date": "2026-01-15",
                    "equity_increase_amount": 10000,
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Equity refresh of $10,000 granted.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5002", "PR10000"],
                    },
                },
            ),
            Action(name="GetCompensation", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            {
                "compensation_id": "COMP10000",
                "employee_id": "E10002",
                "base_salary": 210000,
                "currency": "USD",
                "bonus_target_pct": 25,
                "equity_grant": 50000,
                "effective_date": "2026-01-15"
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_23",
        instruction="Starting on 2026-01-01, handle the processing and approval of a 6-month sabbatical for Emma Rodriguez (E10003). IND accordance with policy, generate a new compensation record to adjust her bonus target to 0% during this period. Assign Michael Park (E10002) as acting manager by modifying his role description. Record a performance review for Amelia with the note 'Sabbatical leave.' To finance this temporary arrangement, allocate $15,000 from the Sales department's budget (DEPT1002) to the Engineering department's account (DEPT1001). Confirm by retrieving both refined employee records and the updated Engineering department record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10003"}),
            Action(name="GetUnusedLeaveId", kwargs={}),
            Action(
                name="RequestLeave",
                kwargs={
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10003",
                        "leave_type": "Sabbatical",
                        "start_date": "2026-01-01",
                        "end_date": "2026-06-30",
                        "status": "Pending",
                    }
                },
            ),
            Action(
                name="UpdateLeaveStatus",
                kwargs={"leave_id": "LV10000", "status": "Approved"},
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "bonus_target_pct": 0,
                        "base_salary": 145000,
                        "equity_grant": 15000,
                        "currency": "USD",
                        "effective_date": "2026-01-01",
                    }
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Sabbatical leave",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10002", "updates": {"role_description": "Acting Manager"}},
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4985000}},
            ),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7015000}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                },
                {
                    "employee_id": "E10002",
                    "role_description": "Acting Manager"
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "budget": 7015000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_24",
        instruction="Coordinate a data audit on previous leave for Emma Rodriguez (E10003) and Arjun Patel (E10004), effective as of 2025-07-01. Specifically for Amelia, since her parental leave (LV6001) is finalized but still labeled 'Scheduled', update this to 'Taken'. Next, implement a 5% salary increase for her and record a performance review with the summary 'Completed leave and performance cycle.' For Rahul, provide a one-time bonus of $1,500 citing 'Data audit completion bonus.' as his vacation (LV6002) is already marked as 'Taken' correctly. To support these initiatives, shift $10,000 from the Sales department's budget (DEPT1002) to the Marketing department's account (DEPT1005). Ensure by retrieving the revised employee records for both individuals and the updated department record for Marketing.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateLeaveRecord",
                kwargs={"leave_id": "LV6001", "updates": {"status": "Taken"}},
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-07-01",
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Completed leave and performance cycle.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"compensation_id": "COMP10000", "performance_review_ids": ["PR5003", "PR5010", "PR10000"]},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(name="GetUnusedBonusId", kwargs={}),
            Action(
                name="AddBonusPayment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10004",
                        "amount": 1500,
                        "reason": "Data audit completion bonus.",
                    }
                },
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1005"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4990000}},
            ),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1005", "updates": {"budget": 1610000}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1005"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                },
                {
                    "employee_id": "E10004"
                },
                {
                    "department_id": "DEPT1005",
                    "name": "Marketing",
                    "budget": 1610000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_25",
        instruction="Initiate a promotion for Arjun Patel (E10004) to Senior Front-end Engineer (POS3006), which corresponds to a level L.3 position, effective 2026-04-01. This promotion entails a 15% increase IND base salary, resulting IND a new compensation record. Record a performance review with the summary 'Promoted to Senior Front-end Engineer (L.3).' to note the change. To confirm, access his updated employee record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10004"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {"level_id": "L.3", "position_id": "POS3006"},
                },
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10004",
                        "base_salary": 135700,
                        "currency": "USD",
                        "equity_grant": 8000,
                        "effective_date": "2026-04-01",
                    }
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "period_start": "2026-04-01",
                        "period_end": "2026-04-01",
                        "rating": None,
                        "summary": "Promoted to Senior Front-end Engineer (L.3).",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5004", "PR5009", "PR10000"],
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
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
                    "hire_date": "2022-02-14",
                    "termination_date": null,
                    "status": "Active",
                    "position_id": "POS3006",
                    "department_id": "DEPT1001",
                    "level_id": "L.3",
                    "manager_id": "E10003",
                    "work_location": "Remote – Mumbai",
                    "work_email": "arjun.patel@example.com",
                    "work_phone": "+91-80-5550-1122",
                    "compensation_id": "COMP10000",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4003"
                    ],
                    "performance_review_ids": [
                        "PR5004",
                        "PR5009",
                        "PR10000"
                    ],
                    "skills": [
                        "Go",
                        "Kubernetes",
                        "CI/CD"
                    ],
                    "role_description": "Backend Engineer focusing on micro-services.",
                    "notes": "Visa sponsored (H-1B)."
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_26",
        instruction="Coordinate a compensation audit for Michael Park (E10002), effective 2025-07-15. Confirm if his base salary is under $140,000 (target: $145,000) or if his bonus target falls below 15% (target: 17%). Document the audit by logging a performance review. For verification purposes, obtain his complete list of performance reviews.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10002"}),
            Action(
                name="ConditionalCompensationCheckAndUpdate",
                kwargs={
                    "employee_id": "E10002",
                    "compensation_id": "COMP2002",
                    "effective_date": "2025-07-15",
                    "salary_threshold": 140000,
                    "target_salary": 145000,
                    "bonus_threshold": 15,
                    "target_bonus": 17,
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "period_start": "2025-07-15",
                        "period_end": "2025-07-15",
                        "rating": None,
                        "summary": None,
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"performance_review_ids": ["PR5002", "PR10000"]},
                },
            ),
            Action(name="ListPerformanceReviews", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
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
                },
                {
                    "review_id": "PR10000",
                    "employee_id": "E10002",
                    "period_start": "2025-07-15",
                    "period_end": "2025-07-15",
                    "rating": null,
                    "summary": null
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_27",
        instruction="Handle and approve a 6-week medical leave for Arjun Patel (E10004) covering the period from 2025-08-01 to 2025-09-12, and upload his 'Medical Certificate' dated 2025-07-24. Assign Michael Park (E10002) as the acting project lead during Singh's absence and log a review for him with the summary 'Acting project lead during R. Singh's leave.' To allocate funds, transfer $15,000 from the Engineering department's budget (DEPT1001) to the Sales department's (DEPT1002). For verification purposes, retrieve the updated records for both departments.",
        actions=[
            Action(name="GetUnusedLeaveId", kwargs={}),
            Action(
                name="RequestLeave",
                kwargs={
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10004",
                        "leave_type": "Medical Leave",
                        "start_date": "2025-08-01",
                        "end_date": "2025-09-12",
                        "status": "Pending",
                    }
                },
            ),
            Action(
                name="UpdateLeaveStatus",
                kwargs={"leave_id": "LV10000", "status": "Approved"},
            ),
            Action(name="GetUnusedDocumentId", kwargs={}),
            Action(
                name="AddEmployeeDocument",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10004",
                        "doc_type": "Medical Certificate",
                        "title": "Medical Certificate",
                        "date": "2025-07-24",
                    }
                },
            ),
            Action(name="ListEmployeeDocuments", kwargs={"employee_id": "E10004"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10002", "updates": {"role_description": "Acting project lead"}},
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "period_start": "2025-08-01",
                        "period_end": "2025-09-12",
                        "rating": None,
                        "summary": "Acting project lead during R. Singh's leave.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"performance_review_ids": ["PR5002", "PR10000"]},
                },
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1002"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 6985000}},
            ),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 5015000}},
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1002"}),
        ],
        outputs=[
            """
            [
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "head_id": "E10001",
                    "location": "Seattle HQ",
                    "budget": 6985000,
                    "description": "Responsible for all product development and technical operations."
                },
                {
                    "department_id": "DEPT1002",
                    "name": "Sales",
                    "head_id": "E10012",
                    "location": "Boston Office",
                    "budget": 5015000,
                    "description": "Owns revenue generation and customer relationships."
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_28",
        instruction="As of 2025-09-01, coordinate an internal transfer for Elena Rodriguez (E10005) to the Marketing department (DEPT1005) with her new supervisor, Marcus Chen (E10006). This transfer involves a salary raise to €78,000. Log a performance review with the summary 'Internal transfer and salary adjustment.' To provide funding, increase the Marketing budget by €10,000. For verification, obtain her updated employee record and the Marketing department record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10005"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10005", "updates": {"department_id": "DEPT1005", "manager_id": "E10006"}},
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10005",
                        "base_salary": 78000,
                        "bonus_target_pct": 5,
                        "equity_grant": 2000,
                        "currency": "EUR",
                        "effective_date": "2025-09-01",
                    }
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10005",
                        "summary": "Internal transfer and salary adjustment",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR10000"],
                    },
                },
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1005"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1005", "updates": {"budget": 1610000}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1005"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10005",
                    "department_id": "DEPT1005",
                    "manager_id": "E10006",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR10000"]
                },
                {
                    "department_id": "DEPT1005",
                    "name": "Marketing",
                    "budget": 1610000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_29",
        instruction="Handle a 60-day Performance Improvement Plan (PIP) for Rahul Singh (E10004), commencing 2025-10-01, with the summary 'PIP Initiated.' and a 'Needs Improvement' rating. Upload his signed 'PIP Agreement' document. As per policy, create a fresh compensation record to adjust his bonus target to 0%. To support the PIP process, transfer $10,000 from the Sales department's budget (DEPT1002) to Engineering (DEPT1001). For verification, retrieve the updated records for Rahul and the Engineering department.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10004"}),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "period_start": "2025-10-01",
                        "period_end": "2025-11-30",
                        "rating": "Needs Improvement",
                        "summary": "PIP Initiated.",
                    }
                },
            ),
            Action(name="GetUnusedDocumentId", kwargs={}),
            Action(
                name="AddEmployeeDocument",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10004",
                        "title": "PIP Agreement",
                        "date": "2025-10-01",
                    }
                },
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10004",
                        "bonus_target_pct": 0,
                        "base_salary": 118000,
                        "equity_grant": 8000,
                        "currency": "USD",
                        "effective_date": "2025-10-01",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5004", "PR5009", "PR10000"],
                    },
                },
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4990000}},
            ),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7010000}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10004",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5004", "PR5009", "PR10000"]
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "budget": 7010000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_30",
        instruction="Coordinate a benefit audit for William Liu (E10006), effective 2025-07-24. Enroll him IND the Legal Insurance plan (BEN9999) and ensure he is enrolled in the 401(k) plan (BEN4003). Update his role description to 'Senior Product Manager, Finance Liaison'. Record a performance review with the summary 'Benefit audit completed.' As a reward for the successful audit, issue a one-time bonus of $1,000 to his manager, Isabella Chen (E10001), for 'Managerial oversight.' To fund this, increase the Engineering department's (DEPT1001) budget by $1,000. For verification, retrieve the updated employee records for both Marcus and Sophia, and the updated Engineering department record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
            Action(
                name="AddEmployeeBenefitsConditionally",
                kwargs={
                    "employee_id": "E10006",
                    "benefit_plan_ids": ["BEN4003", "BEN9999"],
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10006", "updates": {"role_description": "Senior Product Manager, Finance Liaison"}},
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10006",
                        "summary": "Benefit audit completed.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {"performance_review_ids": ["PR5011", "PR10000"]},
                },
            ),
            Action(name="GetUnusedBonusId", kwargs={}),
            Action(
                name="AddBonusPayment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10001",
                        "amount": 1000,
                        "reason": "Managerial oversight.",
                    }
                },
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7001000}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10006",
                    "role_description": "Senior Product Manager, Finance Liaison",
                    "performance_review_ids": ["PR5011", "PR10000"]
                },
                {
                    "employee_id": "E10001"
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "budget": 7001000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_31",
        instruction="Handle the voluntary departure of Elena Rodriguez (E10005), taking effect on 2025-12-15. As part of her exit compensation, she should receive a pro-rated performance bonus (ID BON1001) of €2,500 with the reason 'Pro-rated bonus.'. Update her benefits: terminate all current plans but ensure her enrollment in the vested Legal Insurance plan (BEN9999). Record a final performance review (ID PR5024) with a 'Meets' rating and the summary 'Voluntary termination.' to document the situation. For verification purposes, access her updated employee record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(
                name="TerminateEmployee",
                kwargs={"employee_id": "E10005", "termination_date": "2025-12-15"},
            ),
            Action(
                name="AddBonusPayment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON1001",
                        "employee_id": "E10005",
                        "amount": 2500,
                        "currency": "EUR",
                        "payment_date": "2025-12-15",
                        "reason": "Pro-rated bonus.",
                    }
                },
            ),
            Action(
                name="SetEmployeeBenefits",
                kwargs={"employee_id": "E10005", "benefit_plan_ids": ["BEN9999"]},
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR5024",
                        "employee_id": "E10005",
                        "period_start": "2025-12-15",
                        "period_end": "2025-12-15",
                        "rating": "Meets",
                        "summary": "Voluntary termination.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {"performance_review_ids": ["PR5024"]},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
        ],
        outputs=[
            """
            [
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
                    "termination_date": "2025-12-15",
                    "status": "Terminated",
                    "position_id": "POS3010",
                    "department_id": "DEPT1004",
                    "level_id": "L.1",
                    "manager_id": "E10011",
                    "work_location": "Barcelona Office",
                    "work_email": "olivia.martinez@example.com",
                    "work_phone": "+34-91-555-0200",
                    "compensation_id": "COMP2005",
                    "benefit_plan_ids": [
                      "BEN9999"
                    ],
                    "performance_review_ids": [
                     "PR5024"
                    ],
                    "skills": [
                        "Financial Modeling",
                        "SQL",
                        "Excel"
                    ],
                    "role_description": "Junior Financial Analyst supporting quarterly forecasts.",
                    "notes": "Recent graduate—ESADE Business School."
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_32",
        instruction="Initiate the onboarding of a new Senior Backend Engineer, Sarah Johnson, with a start date of 2025-08-15, for the Engineering department (DEPT1001). Her compensation package includes a $145,000 salary, 15% bonus, and $25,000 equity grant. Upon joining, Sarah will take on the role of manager for Rahul Singh (E10004). Record a performance review for Rahul with the summary 'Manager updated.' To finance the new position, allocate $175,000 from the Sales budget (DEPT1002) to Engineering. For verification, obtain the updated records for both the employees and the Engineering department.",
        actions=[
            Action(name="GetUnusedEmployeeId", kwargs={}),
            Action(
                name="CreateEmployee",
                kwargs={
                    "employee": {
                        "employee_id": "E10000",
                        "first_name": "Sarah",
                        "last_name": "Johnson",
                        "status": "Active",
                        "hire_date": "2025-08-15",
                        "department_id": "DEPT1001",
                        "role_description": "Senior Backend Engineer",
                    }
                },
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10000",
                        "base_salary": 145000,
                        "bonus_target_pct": 15,
                        "equity_grant": 25000,
                        "currency": "USD",
                        "effective_date": "2025-08-15",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10000",
                    "updates": {"compensation_id": "COMP10000"},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10004", "updates": {"manager_id": "E10000"}},
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "summary": "Manager updated",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {"performance_review_ids": ["PR5004", "PR5009", "PR10000"]},
                },
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4825000}},
            ),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7175000}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10000"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10000",
                    "first_name": "Sarah",
                    "last_name": "Johnson",
                    "compensation_id": "COMP10000"
                },
                {
                    "employee_id": "E10004",
                    "manager_id": "E10000",
                    "performance_review_ids": ["PR5004", "PR5009", "PR10000"]
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "budget": 7175000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_33",
        instruction="Announce the launch of a new initiative, 'Project Titan,' starting from 2025-11-01. Firstly, promote Amelia Garcia (E10003) to the position 'Lead Engineer, Project Titan' (POS4001), classified as level L.5. This role adjustment encompasses a 12% salary hike and an added $30,000 equity grant. Document this by generating a fresh compensation record and recording a performance review with the note 'Promotion to Lead Engineer, Project Titan.' Subsequently, reassign Rahul Singh (E10004) to fill Amelia's former role (POS3006) within the Marketing department (DEPT1005). Reallocate funds by reducing the Marketing department's budget by $250,000 and bolstering the Engineering department's (DEPT1001) budget equivalent to this reduction. IND addition, prefix 'HIRING FREEZE: Q4 2025.' to the Marketing department's description. For confirmation, retrieve the revised employee records for both Amelia Garcia and Rahul Singh, alongside the updated department record for Engineering.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10003", "updates": {"position_id": "POS4001", "level_id": "L.5", "role_description": "Lead Engineer, Project Titan"}},
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 162400,
                        "equity_grant": 45000,
                        "currency": "USD",
                        "bonus_target_pct": 15,
                        "effective_date": "2025-11-01",
                    }
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Lead Engineer, Project Titan.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10004", "updates": {"position_id": "POS3006", "department_id": "DEPT1005"}},
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1005"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1005", "updates": {"budget": 1350000, "description": "HIRING FREEZE: Q4 2025. Drives brand awareness and demand generation."}},
            ),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7250000}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10003",
                    "position_id": "POS4001",
                    "level_id": "L.5",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                },
                {
                    "employee_id": "E10004",
                    "position_id": "POS3006",
                    "department_id": "DEPT1005"
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "budget": 7250000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_34",
        instruction="Prolong Amelia Garcia's (E10003) parental leave (LV6001) through 2025-03-01 and upload her 'Medical Certificate' dated 2025-07-01. Record a review for her with the note 'Parental leave extended.' To acknowledge Michael Park (E10002) for taking over her responsibilities, designate him as 'Acting Team Lead' by updating his role description and award him a one-time bonus of $1,500 for 'Leave coverage bonus.' For validation, retrieve both updated employee records.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateLeaveRecord",
                kwargs={"leave_id": "LV6001", "updates": {"end_date": "2025-03-01"}},
            ),
            Action(name="GetUnusedDocumentId", kwargs={}),
            Action(
                name="AddEmployeeDocument",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10003",
                        "title": "Medical Certificate",
                        "date": "2025-07-01",
                    }
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Parental leave extended.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"performance_review_ids": ["PR5003", "PR5010", "PR10000"]},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10002", "updates": {"role_description": "Acting Team Lead"}},
            ),
            Action(name="GetUnusedBonusId", kwargs={}),
            Action(
                name="AddBonusPayment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10002",
                        "amount": 1500,
                        "reason": "Leave coverage bonus",
                    }
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10003",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                },
                {
                    "employee_id": "E10002",
                    "role_description": "Acting Team Lead"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_35",
        instruction="Starting from 2025-10-15, handle the promotion of William Liu (E10006) to Director (level L.5) with a revised base salary of €85,000 and a bonus target of 18%. With this transition, assign him as the new head of the Finance department (DEPT1004). To facilitate this, transfer €150,000 from the budget of the Marketing department (DEPT1005) to Finance. Lastly, enter a single performance review for Marcus with the summary 'Promotion to Director and Head of Finance.' To confirm, fetch the updated records for William Liu and the two affected departments.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10006"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10006", "updates": {"level_id": "L.5", "role_description": "Director", "position_id": None}},
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10006",
                        "base_salary": 85000,
                        "bonus_target_pct": 18,
                        "equity_grant": 5000,
                        "currency": "EUR",
                        "effective_date": "2025-10-15",
                    }
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10006",
                        "summary": "Promotion to Director and Head of Finance",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5011", "PR10000"],
                    },
                },
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1005"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1004"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1005", "updates": {"budget": 1450000}},
            ),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1004", "updates": {"budget": 1350000, "head_id": "E10006"}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1005"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1004"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10006",
                    "level_id": "L.5",
                    "role_description": "Director",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5011", "PR10000"]
                },
                {
                    "department_id": "DEPT1005",
                    "name": "Marketing",
                    "budget": 1450000
                },
                {
                    "department_id": "DEPT1004",
                    "name": "Finance",
                    "head_id": "E10006",
                    "budget": 1350000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_36",
        instruction="Starting from 2025-09-01, handle the re-hire of former employee, Adrian Thompson (E99999), as a 'Senior Backend Engineer' (POS3009) at level L.3 within the Engineering department (DEPT1001). His updated compensation comprises a base salary of $130,000 and a bonus target of 15%; assign his benefits to the standard package (BEN4001, BEN4002, BEN4003) and upload his 'Re-hire Packet' document. Upon commencement, Andrian will take on the role of manager for Michael Park (E10002). As a result, advance Daniel to 'Senior Analyst' (POS3012), adjust his salary with a 5% increase, and record a performance review with the summary 'Promotion to Senior Analyst'. To finance these changes, shift $150,000 from the Sales department budget (DEPT1002) to that of the Engineering department's (DEPT1001). For confirmation, acquire the updated employee records for both Andrian and Daniel, alongside the revised department record for Engineering.",
        actions=[
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E99999",
                    "updates": {
                        "status": "Active",
                        "hire_date": "2025-09-01",
                        "termination_date": None,
                        "position_id": "POS3009",
                        "department_id": "DEPT1001",
                        "level_id": "L.3",
                        "role_description": "Senior Backend Engineer",
                    },
                },
            ),
            Action(name="GetUnusedCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E99999",
                        "base_salary": 130000,
                        "bonus_target_pct": 15,
                        "currency": "USD",
                        "effective_date": "2025-09-01",
                    }
                },
            ),
            Action(
                name="SetEmployeeBenefits",
                kwargs={"employee_id": "E99999", "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003"]},
            ),
            Action(name="GetUnusedDocumentId", kwargs={}),
            Action(
                name="AddEmployeeDocument",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E99999",
                        "title": "Re-hire Packet",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E99999", "updates": {"compensation_id": "COMP10000"}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10002"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10002", "updates": {"manager_id": "E99999", "position_id": "POS3012"}},
            ),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10002",
                    "compensation_id": "COMP2002",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-09-01",
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Promotion to Senior Analyst",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10002", "updates": {"performance_review_ids": ["PR5002", "PR10000"]}},
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4850000}},
            ),
            Action(
                name="UpdateDepartment",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7150000}},
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E99999"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E99999",
                    "status": "Active",
                    "position_id": "POS3009",
                    "level_id": "L.3",
                    "compensation_id": "COMP10000"
                },
                {
                    "employee_id": "E10002",
                    "manager_id": "E99999",
                    "position_id": "POS3012",
                    "performance_review_ids": ["PR5002", "PR10000"]
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "budget": 7150000
                }
            ]
            """
        ],
    )
,
    Task(
        annotator="0",
        user_id="res_37",
        instruction="Authorize the request for Rahul Singh (E10004) to continue his work permanently from his present remote location in Bangalore, starting 2025-12-01. Modify his work location to reflect the standardized entry 'Remote - Mumbai' and upload his 'Remote Work Agreement' document. Additionally, record a performance review note with the summary 'Permanent remote work approved.' to log the adjustment. To verify, obtain his updated employee record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {"work_location": "Remote - Bangalore"},
                },
            ),
            Action(name="GetUnusedDocumentId", kwargs={}),
            Action(
                name="AddEmployeeDocument",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10004",
                        "doc_type": "Remote Work Agreement",
                        "title": "Remote Work Agreement",
                        "date": "2025-12-01",
                    }
                },
            ),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "period_start": "2025-12-01",
                        "period_end": "2025-12-01",
                        "rating": None,
                        "summary": "Permanent remote work approved.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {
                        "performance_review_ids": ["PR5004", "PR5009", "PR10000"]
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
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
                    "hire_date": "2022-02-14",
                    "termination_date": null,
                    "status": "Active",
                    "position_id": "POS3007",
                    "department_id": "DEPT1001",
                    "level_id": "L.2",
                    "manager_id": "E10003",
                    "work_location": "Remote - Mumbai",
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
                        "PR10000"
                    ],
                    "skills": [
                        "Go",
                        "Kubernetes",
                        "CI/CD"
                    ],
                    "role_description": "Backend Engineer focusing on micro-services.",
                    "notes": "Visa sponsored (H-1B)."
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_38",
        instruction="Handle the annual performance evaluation for Amelia Garcia (E10003), effective 2025-07-24. Her performance rating is 'Exceeds', making her eligible for a one-time performance bonus of $8,500 with the reason 'Annual performance bonus.' and an 8% merit-based salary raise. Record these changes by creating a new performance review with the summary 'Annual review completed.'. For verification, obtain her updated employee record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensation", kwargs={"employee_id": "E10003"}),
            Action(name="GetUnusedReviewId", kwargs={}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "period_start": "2024-07-24",
                        "period_end": "2025-07-24",
                        "rating": "Exceeds",
                        "summary": "Annual review completed.",
                    }
                },
            ),
            Action(name="GetUnusedBonusId", kwargs={}),
            Action(
                name="AddBonusPayment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10003",
                        "amount": 8500,
                        "currency": "USD",
                        "payment_date": "2025-07-24",
                        "reason": "Annual performance bonus.",
                    }
                },
            ),
            Action(
                name="IncreaseEmployeeCompensation",
                kwargs={
                    "employee_id": "E10003",
                    "salary_increase_pct": 8,
                    "compensation_id": "COMP2003",
                    "effective_date": "2025-07-24",
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"performance_review_ids": ["PR5003", "PR5010", "PR10000"]},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            [
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
                        "PR10000"
                    ],
                    "skills": [
                        "TypeScript",
                        "React",
                        "Accessibility"
                    ],
                    "role_description": "Senior Front-end Engineer on the web platform team.",
                    "notes": "On parental leave 2024-11-01 → 2025-02-01."
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_39",
        instruction="Handle an emergency family leave for Marcus Chen (E10006). This leave spans 2 weeks, beginning retroactively from 2025-07-20 and concluding on 2025-08-03. Document and authorize the request using leave ID LV8006. Since the leave is presently active, adjust his employment status to 'On Leave'. Attach the 'Emergency Leave Request' form (doc ID E10006-001) under the title 'Emergency Leave Form'. Record a review note (ID PR5032) with the summary 'Emergency leave processed.' for documentation. To verify, access his updated employee record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
            Action(
                name="RequestLeave",
                kwargs={
                    "leave": {
                        "leave_id": "LV8006",
                        "employee_id": "E10006",
                        "leave_type": "Emergency Family Leave",
                        "start_date": "2025-07-20",
                        "end_date": "2025-08-03",
                        "status": "Pending",
                    }
                },
            ),
            Action(
                name="UpdateLeaveStatus",
                kwargs={"leave_id": "LV8006", "status": "Approved"},
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10006", "updates": {"status": "On Leave"}},
            ),
            Action(
                name="AddEmployeeDocument",
                kwargs={
                    "document": {
                        "doc_id": "E10006-001",
                        "employee_id": "E10006",
                        "doc_type": "Emergency Leave",
                        "title": "Emergency Leave Form",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR5032",
                        "employee_id": "E10006",
                        "period_start": "2025-07-20",
                        "period_end": "2025-08-03",
                        "rating": None,
                        "summary": "Emergency leave processed.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {"performance_review_ids": ["PR5011", "PR5032"]},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
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
                    "status": "On Leave",
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
                        "PR5032"
                    ],
                    "skills": [
                        "Product Strategy",
                        "User Research",
                        "Data Analytics"
                    ],
                    "role_description": "Senior Product Manager leading the analytics platform initiatives.",
                    "notes": "Previously led successful product launches at major tech companies."
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_40",
        instruction="Coordinate a compensation audit for Daniel Kim (E10002), starting 2025-12-01. The audit compares his salary against a $150,000 minimum (target: $152,000) and his bonus target against a 20% minimum (target: 20%). The audit also incorporates an unconditional equity grant increase of $5,000. Establish a new compensation record with ID COMP5008. Record a review note (ID PR5033) with the summary 'Compensation audit completed.' to document the audit's outcomes. For verification, obtain his latest compensation record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(
                name="ConditionalCompensationCheckAndUpdate",
                kwargs={
                    "employee_id": "E10002",
                    "compensation_id": "COMP5008",
                    "effective_date": "2025-12-01",
                    "salary_threshold": 150000,
                    "target_salary": 152000,
                    "bonus_threshold": 20,
                    "target_bonus": 20,
                    "equity_increase_amount": 5000,
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR5033",
                        "employee_id": "E10002",
                        "period_start": "2025-12-01",
                        "period_end": "2025-12-01",
                        "rating": None,
                        "summary": "Compensation audit completed.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"performance_review_ids": ["PR5002", "PR5033"]},
                },
            ),
            Action(name="GetCompensation", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            [
                {
                    "compensation_id": "COMP5008",
                    "employee_id": "E10002",
                    "base_salary": 210000,
                    "currency": "USD",
                    "bonus_target_pct": 25,
                    "equity_grant": 45000,
                    "effective_date": "2025-12-01"
                }
            ]
            """
        ],
    ),
]
