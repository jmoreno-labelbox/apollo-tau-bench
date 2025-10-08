from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="res_01",
        instruction="Effective 2025-07-01, promote Emma Rodriguez (E10003) to 'Senior Front-end Engineer' (POS3006) at level L.4, which includes a 5% salary increase. To support her new role, transfer Michael Park (E10002) to her department (DEPT1005), making Amelia his new manager. Log a performance review for Amelia with the summary 'Promotion to Senior Engineer.' For verification, retrieve the updated records for both employees.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10003", "updates": {"position_id": "POS3006", "level_id": "L.4", "role_description": "Senior Front-end Engineer"}},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 152250,
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "currency": "USD",
                        "effective_date": "2025-07-01",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Senior Engineer",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10002", "updates": {"department_id": "DEPT1005", "manager_id": "E10003"}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10003",
                    "position_id": "POS3006",
                    "level_id": "L.4",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                },
                {
                    "employee_id": "E10002",
                    "department_id": "DEPT1005",
                    "manager_id": "E10003"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_02",
        instruction="Process the transfer of Michael Park (E10002) to the 'Boston Office', effective 2025-07-24. His new manager will be Isabella Chen (E10001). As part of this transfer, also enroll him IND the 'Legal Insurance' plan (BEN9999). A performance review note (ID PR5013) must be logged with the summary 'Relocation to Boston; enrolled in Legal Insurance.' to document these changes. For verification, retrieve his updated employee record.",
        actions=[
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "work_location": "Boston Office",
                        "manager_id": "E10001",
                    },
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10002",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN9999"],
                },
            ),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR5013",
                        "employee_id": "E10002",
                        "period_start": "2025-07-24",
                        "period_end": "2025-07-24",
                        "rating": None,
                        "summary": "Relocation to Boston; enrolled in Legal Insurance.",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"performance_review_ids": ["PR5002", "PR5013"]},
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
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
                "manager_id": "E10001",
                "work_location": "Boston Office",
                "work_email": "michael.park@example.com",
                "work_phone": "+1-212-555-0144",
                "compensation_id": "COMP2002",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4002",
                    "BEN9999"
                ],
                "performance_review_ids": [
                    "PR5002",
                    "PR5013"
                ],
                "skills": [
                    "Sales Strategy",
                    "CRM",
                    "Negotiation"
                ],
                "role_description": "Regional VP of Sales for the Eastern territory.",
                "notes": "High performer—President's Club 2023."
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_03",
        instruction="You need to onboard a new Marketing Intern, Jane Doe, into the Marketing department (DEPT1005), effective 2025-06-24. Her salary will be €45,000. For her benefits, she'll get a new 'Intern Medical' plan, so set up that plan first: it's plan ID BEN10000, from Blue Shield, with 80% employer coverage and a €50 monthly employee cost. Once she's IND the system, you'll also need to raise the Marketing department's budget by €50,000 for her role. After that's taken care of, please pull up Jane's new employee record for verification.",
        actions=[
            Action(
                name="CreateBenefitPlan",
                kwargs={
                    "benefit_plan": {
                        "benefit_plan_id": "BEN10000",
                        "name": "Intern Medical",
                        "provider": "Blue Shield",
                        "employer_coverage_pct": 80,
                        "employee_cost_monthly": 50,
                    }
                },
            ),
            Action(name="GetNewEmployeeId", kwargs={}),
            Action(
                name="CreateNewEmployee",
                kwargs={
                    "employee": {
                        "employee_id": "E10000",
                        "first_name": "Jane",
                        "last_name": "Doe",
                        "status": "Active",
                        "hire_date": "2025-06-24",
                        "department_id": "DEPT1005",
                        "work_email": None,
                        "compensation_id": None,
                        "benefit_plan_ids": ["BEN10000"],
                        "performance_review_ids": [],
                        "role_description": "Marketing Intern",
                    }
                },
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10000",
                        "base_salary": 45000,
                        "currency": "EUR",
                        "effective_date": "2025-06-24",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10000",
                    "updates": {"compensation_id": "COMP10000"},
                },
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1005"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1005", "updates": {"budget": 1650000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10000"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10000",
                "first_name": "Jane",
                "last_name": "Doe",
                "preferred_name": null,
                "date_of_birth": null,
                "gender": null,
                "ethnicity_code": null,
                "nationality": null,
                "marital_status": null,
                "hire_date": "2025-06-24",
                "termination_date": null,
                "status": "Active",
                "position_id": null,
                "department_id": "DEPT1005",
                "level_id": null,
                "manager_id": null,
                "work_location": null,
                "work_email": null,
                "work_phone": null,
                "compensation_id": "COMP10000",
                "benefit_plan_ids": [
                    "BEN10000"
                ],
                "performance_review_ids": [],
                "skills": [],
                "role_description": "Marketing Intern",
                "notes": null
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_04",
        instruction="Process the termination of Olivia Martinez (E10005), effective 2025-07-01. Follow all off-boarding procedures, including clearing her benefits, zeroing out her final compensation, and logging a performance review with the summary 'Termination.' To backfill her role, transfer William Liu (E10006) to her previous position (POS3010). For verification, retrieve the updated records for both employees.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10005"}),
            Action(
                name="TerminateEmployee",
                kwargs={"employee_id": "E10005", "termination_date": "2025-07-01"},
            ),
            Action(
                name="SetEmployeeBenefits",
                kwargs={"employee_id": "E10005", "benefit_plan_ids": []},
            ),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP_FINAL_E10005",
                        "employee_id": "E10005",
                        "base_salary": 0,
                        "bonus_target_pct": 0,
                        "equity_grant": 0,
                        "effective_date": "2025-07-01",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10005",
                        "summary": "Termination",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP_FINAL_E10005",
                        "performance_review_ids": ["PR10000"],
                    },
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10006"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10006", "updates": {"position_id": "POS3010"}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10005"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10006"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10005",
                    "status": "Terminated",
                    "compensation_id": "COMP_FINAL_E10005",
                    "performance_review_ids": ["PR10000"]
                },
                {
                    "employee_id": "E10006",
                    "position_id": "POS3010"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_05",
        instruction="Process and approve a vacation for Arjun Patel (E10004) from 2025-08-15 to 2025-08-30. Appoint Michael Park (E10002) as acting team lead, which includes a temporary 10% salary increase, effective 2025-08-15. Log a performance review for Daniel with the summary 'Acting team lead assignment and vacation coverage.' To fund the salary increase, transfer $5,000 from the Sales department (DEPT1002) to Engineering (DEPT1001). For verification, retrieve the updated records for both employees and the Engineering department.",
        actions=[
            Action(name="GetNewLeaveId", kwargs={}),
            Action(
                name="CreateLeaveRecord",
                kwargs={
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10004",
                        "leave_type": "Vacation",
                        "start_date": "2025-08-15",
                        "end_date": "2025-08-30",
                        "status": "Pending",
                    }
                },
            ),
            Action(
                name="UpdateLeaveStatus",
                kwargs={"leave_id": "LV10000", "status": "Approved"},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10002"}),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10002",
                        "base_salary": 231000,
                        "bonus_target_pct": 25,
                        "equity_grant": 40000,
                        "currency": "USD",
                        "effective_date": "2025-08-15",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Acting team lead assignment and vacation coverage",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "role_description": "Acting Team Lead",
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5002", "PR10000"],
                    },
                },
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4995000}},
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7005000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10004"
                },
                {
                    "employee_id": "E10002",
                    "role_description": "Acting Team Lead",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5002", "PR10000"]
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "budget": 7005000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_06",
        instruction="Effective 2025-08-01, increase the monthly employee cost for the Medical-PPO plan (BEN4001) to $170. Concurrently, promote Isabella Chen (E10001) to 'Lead Engineer' (POS3002) at level L.A, which includes a 10% salary increase, and log a performance review with the summary 'Promotion to Lead Engineer.' Enroll Adrian Thompson (E99999) IND the updated Medical-PPO plan. To fund the promotion, transfer $50,000 from the HR department's budget (DEPT1003) to the Engineering department's (DEPT1001). For verification, retrieve the updated employee records for both Andrian and Sophia, and the updated Engineering department record.",
        actions=[
            Action(
                name="UpdateBenefitPlan",
                kwargs={"benefit_plan_id": "BEN4001", "updates": {"employee_cost_monthly": 170}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E99999"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E99999",
                    "benefit_plan_ids": ["BEN9999", "BEN4001"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10001"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"position_id": "POS3002", "level_id": "L.A"},
                },
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10001",
                        "base_salary": 357500,
                        "bonus_target_pct": 30,
                        "equity_grant": 75000,
                        "currency": "USD",
                        "effective_date": "2025-08-01",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Promotion to Lead Engineer",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5001", "PR10000"],
                    },
                },
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1003"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1003", "updates": {"budget": 750000}},
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7050000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E99999"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
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
        instruction="Effective 2025-06-24, onboard a new HR Business Partner, Sarah Johnson, into the HR department (DEPT1003). Her compensation is a $110,000 salary, and she should be enrolled in benefits (BEN4001, BEN4002). Her manager will be Emma Rodriguez (E10003). Log a performance review for Mary with the summary 'New hire onboarding.' To fund the new role, transfer $120,000 from the Sales budget (DEPT1002) to HR. For verification, retrieve the updated records for Sarah Johnson and the HR department.",
        actions=[
            Action(name="GetNewEmployeeId", kwargs={}),
            Action(
                name="CreateNewEmployee",
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
            Action(name="GetNewCompensationId", kwargs={}),
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
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10000",
                        "summary": "New hire onboarding",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10000",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR10000"],
                    },
                },
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1003"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4880000}},
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1003", "updates": {"budget": 920000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10000"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1003"}),
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
        instruction="Effective 2025-06-24, promote Arjun Patel (E10004) to 'Senior Engineer' (POS3006) at level L.3, which includes a 10% salary increase. To backfill his role, transfer Michael Park (E10002) to Rahul's previous department (DEPT1001) and manager (E10003). Log a performance review for Rahul with the summary 'Promotion to Senior Engineer'. To fund the promotion, transfer $50,000 from the Sales department's budget (DEPT1002) to Engineering (DEPT1001). For verification, retrieve the updated records for both employees and the Engineering department.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10004"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10004", "updates": {"position_id": "POS3006", "level_id": "L.3", "role_description": "Senior Engineer"}},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10004",
                        "base_salary": 129800,
                        "bonus_target_pct": 10,
                        "equity_grant": 8000,
                        "currency": "USD",
                        "effective_date": "2025-06-24",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "summary": "Promotion to Senior Engineer",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5004", "PR5009", "PR10000"],
                    },
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10002", "updates": {"department_id": "DEPT1001", "manager_id": "E10003"}},
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4950000}},
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7050000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10004",
                    "position_id": "POS3006",
                    "level_id": "L.3",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5004", "PR5009", "PR10000"]
                },
                {
                    "employee_id": "E10002",
                    "department_id": "DEPT1001",
                    "manager_id": "E10003"
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
        user_id="res_09",
        instruction="Effective 2025-08-01, increase the monthly employee cost for the Medical-PPO plan (BEN4001) to $170. Concurrently, promote Isabella Chen (E10001) to 'Lead Engineer' (POS3002) at level L.A, which includes a 10% salary increase, and log a performance review with the summary 'Promotion to Lead Engineer.' Enroll Adrian Thompson (E99999) IND the updated Medical-PPO plan. To fund the promotion, transfer $50,000 from the HR department's budget (DEPT1003) to the Engineering department's (DEPT1001). For verification, retrieve the updated employee records for both Andrian and Sophia, and the updated Engineering department record.",
        actions=[
            Action(
                name="UpdateBenefitPlan",
                kwargs={"benefit_plan_id": "BEN4001", "updates": {"employee_cost_monthly": 170}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E99999"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E99999",
                    "benefit_plan_ids": ["BEN9999", "BEN4001"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10001"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"position_id": "POS3002", "level_id": "L.A"},
                },
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10001",
                        "base_salary": 357500,
                        "bonus_target_pct": 30,
                        "equity_grant": 75000,
                        "currency": "USD",
                        "effective_date": "2025-08-01",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Promotion to Lead Engineer",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5001", "PR10000"],
                    },
                },
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1003"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1003", "updates": {"budget": 750000}},
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7050000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E99999"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
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
        user_id="res_10",
        instruction="Effective 2025-07-15, process the termination of Olivia Martinez (E10005). Follow all off-boarding procedures, including clearing her benefits, zeroing out her final compensation, and logging a performance review with the summary 'Termination.' To backfill her role, transfer William Liu (E10006) to her previous position (POS3010). For verification, retrieve the updated record for William Liu.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10005"}),
            Action(
                name="TerminateEmployee",
                kwargs={"employee_id": "E10005", "termination_date": "2025-07-15"},
            ),
            Action(
                name="SetEmployeeBenefits",
                kwargs={"employee_id": "E10005", "benefit_plan_ids": []},
            ),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP_FINAL_E10005",
                        "employee_id": "E10005",
                        "base_salary": 0,
                        "bonus_target_pct": 0,
                        "equity_grant": 0,
                        "effective_date": "2025-07-15",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10005",
                        "summary": "Termination",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP_FINAL_E10005",
                        "performance_review_ids": ["PR10000"],
                    },
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10006", "updates": {"position_id": "POS3010"}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10006"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10006",
                "first_name": "Marcus",
                "last_name": "Chen",
                "position_id": "POS3010"
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_11",
        instruction="Effective 2025-07-01, restructure the Sales department (DEPT1002). Promote Michael Park (E10002) to 'Regional VP' (POS3004) with a 15% salary increase and log a performance review with the summary 'Promotion to Regional VP.' To support him, transfer Arjun Patel (E10004) to the Sales department, making Daniel his new manager. Increase the Sales department budget by $200,000. For verification, retrieve the updated records for both employees and the Sales department.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10002"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10002", "updates": {"position_id": "POS3004", "role_description": "Regional VP"}},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10002",
                        "base_salary": 241500,
                        "bonus_target_pct": 25,
                        "equity_grant": 40000,
                        "currency": "USD",
                        "effective_date": "2025-07-01",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Promotion to Regional VP",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5002", "PR10000"],
                    },
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10004", "updates": {"department_id": "DEPT1002", "manager_id": "E10002"}},
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1002"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 5200000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1002"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10002",
                    "position_id": "POS3004",
                    "role_description": "Regional VP",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5002", "PR10000"]
                },
                {
                    "employee_id": "E10004",
                    "department_id": "DEPT1002",
                    "manager_id": "E10002"
                },
                {
                    "department_id": "DEPT1002",
                    "name": "Sales",
                    "budget": 5200000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_12",
        instruction="Effective 2025-08-01, promote Emma Rodriguez (E10003) to 'Senior Engineer' (POS3005) at level L.4 IND the Engineering department (DEPT1001), which includes a 10% salary increase. To support the team, transfer Michael Park (E10002) to the Engineering department, making Amelia his new manager. Log a performance review for Amelia with the summary 'Promotion to Senior Engineer.' To fund the promotion, transfer $75,000 from the Sales department's budget (DEPT1002) to Engineering. For verification, retrieve the updated records for both employees and both departments.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10003", "updates": {"department_id": "DEPT1001", "position_id": "POS3005", "level_id": "L.4", "role_description": "Senior Engineer"}},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 159500,
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "currency": "USD",
                        "effective_date": "2025-08-01",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Senior Engineer",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10002", "updates": {"department_id": "DEPT1001", "manager_id": "E10003"}},
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4925000}},
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7075000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1002"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10003",
                    "department_id": "DEPT1001",
                    "position_id": "POS3005",
                    "level_id": "L.4",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                },
                {
                    "employee_id": "E10002",
                    "department_id": "DEPT1001",
                    "manager_id": "E10003"
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "budget": 7075000
                },
                {
                    "department_id": "DEPT1002",
                    "name": "Sales",
                    "budget": 4925000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_13",
        instruction="Effective 2025-07-01, increase the Sales department's (DEPT1002) budget by $250,000. Use this to promote Michael Park (E10002) to 'Senior Sales Executive' (POS3005) at level L.5, which includes a 10% salary increase. To provide support, transfer Arjun Patel (E10004) to the Sales department, making Daniel his new manager. Log a performance review for Daniel with the summary 'Promotion to Senior Sales Executive.' For verification, retrieve the updated records for both employees and the Sales department.",
        actions=[
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1002"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 5250000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10002"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10002", "updates": {"position_id": "POS3005", "level_id": "L.5", "role_description": "Senior Sales Executive"}},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10002",
                        "base_salary": 231000,
                        "bonus_target_pct": 25,
                        "equity_grant": 40000,
                        "currency": "USD",
                        "effective_date": "2025-07-01",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Promotion to Senior Sales Executive",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5002", "PR10000"],
                    },
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10004", "updates": {"department_id": "DEPT1002", "manager_id": "E10002"}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1002"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10002",
                    "position_id": "POS3005",
                    "level_id": "L.5",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5002", "PR10000"]
                },
                {
                    "employee_id": "E10004",
                    "department_id": "DEPT1002",
                    "manager_id": "E10002"
                },
                {
                    "department_id": "DEPT1002",
                    "name": "Sales",
                    "budget": 5250000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_14",
        instruction="Effective 2025-10-01, process and approve a parental leave for Isabella Chen (E10001) until 2026-02-01. Appoint Emma Rodriguez (E10003) as acting CTO (POS4001) at level L.5 to cover the leave, which includes a temporary 8% salary increase. Log a performance review for Amelia with the summary 'Acting CTO assignment.' To fund this, transfer $50,000 from the Sales department's budget (DEPT1002) to Engineering (DEPT1001). For verification, retrieve the updated records for both employees and the Engineering department.",
        actions=[
            Action(name="GetNewLeaveId", kwargs={}),
            Action(
                name="CreateLeaveRecord",
                kwargs={
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10001",
                        "leave_type": "Parental",
                        "start_date": "2025-10-01",
                        "end_date": "2026-02-01",
                        "status": "Pending",
                    }
                },
            ),
            Action(
                name="UpdateLeaveStatus",
                kwargs={"leave_id": "LV10000", "status": "Approved"},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10003", "updates": {"position_id": "POS4001", "level_id": "L.5", "role_description": "Acting CTO"}},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 156600,
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "currency": "USD",
                        "effective_date": "2025-10-01",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Acting CTO assignment",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4950000}},
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7050000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10001"
                },
                {
                    "employee_id": "E10003",
                    "position_id": "POS4001",
                    "level_id": "L.5",
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
        user_id="res_15",
        instruction="Onboard a new hire, Sofia Hernandez, as a 'Junior Marketing Analyst' (POS3010) IND the Marketing department (DEPT1005), effective 2025-06-24. Her salary is €68,000 with a 5% bonus. Log a 'New hire onboarding' review for her. As part of the onboarding, update her manager William Liu's (E10006) role description to 'Senior Product Manager & Team Lead'. To fund the new role, increase the Marketing budget by €100,000. For verification, retrieve the updated records for both employees and the Marketing department.",
        actions=[
            Action(name="GetNewEmployeeId", kwargs={}),
            Action(
                name="CreateNewEmployee",
                kwargs={
                    "employee": {
                        "employee_id": "E10000",
                        "first_name": "Maria",
                        "last_name": "Lopez",
                        "status": "Active",
                        "hire_date": "2025-06-24",
                        "position_id": "POS3010",
                        "department_id": "DEPT1005",
                        "manager_id": "E10006",
                        "role_description": "Junior Marketing Analyst",
                    }
                },
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10000",
                        "base_salary": 68000,
                        "bonus_target_pct": 5,
                        "currency": "EUR",
                        "effective_date": "2025-06-24",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10000",
                        "summary": "New hire onboarding",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10000",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR10000"],
                    },
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10006"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10006", "updates": {"role_description": "Senior Product Manager & Team Lead"}},
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1005"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1005", "updates": {"budget": 1700000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10000"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10006"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1005"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10000",
                    "first_name": "Maria",
                    "last_name": "Lopez",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR10000"]
                },
                {
                    "employee_id": "E10006",
                    "role_description": "Senior Product Manager & Team Lead"
                },
                {
                    "department_id": "DEPT1005",
                    "name": "Marketing",
                    "budget": 1700000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_16",
        instruction="Arjun Patel's (E10004) recent vacation (leave ID LV6002) has concluded. Update the status of this leave record to 'Taken' to reflect that it's completed. As he has now returned, process his pending promotion to 'Senior Backend Engineer' (POS3009) at level L.3, effective 2025-07-27. This includes a 12% salary increase. Log a performance review with the summary 'Promotion to Senior Engineer.' To fund the raise, transfer $20,000 from the HR budget (DEPT1003) to Engineering (DEPT1001). For verification, retrieve his updated employee record, leave history, and the Engineering department record.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10004"}),
            Action(
                name="UpdateLeaveStatus",
                kwargs={"leave_id": "LV6002", "status": "Taken"},
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10004", "updates": {"position_id": "POS3009", "level_id": "L.3", "role_description": "Senior Backend Engineer"}},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10004",
                        "base_salary": 132160,
                        "bonus_target_pct": 10,
                        "equity_grant": 8000,
                        "currency": "USD",
                        "effective_date": "2025-07-27",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "summary": "Promotion to Senior Engineer",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5004", "PR5009", "PR10000"],
                    },
                },
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1003"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1003", "updates": {"budget": 780000}},
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7020000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(name="ListEmployeeLeaves", kwargs={"employee_id": "E10004"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10004",
                    "position_id": "POS3009",
                    "level_id": "L.3",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5004", "PR5009", "PR10000"]
                },
                [
                    {
                        "leave_id": "LV6002",
                        "status": "Taken"
                    }
                ],
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "budget": 7020000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_17",
        instruction="Standardize the records for Arjun Patel (E10004), effective 2025-07-01, by updating his work location to 'Remote – Mumbai'. As part of this, promote his manager, Emma Rodriguez (E10003), to 'Lead Engineer' (POS3005) with a 5% salary increase. Log a performance review for Amelia with the summary 'Promotion to Lead Engineer.' For verification, retrieve the updated records for both employees.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10004", "updates": {"work_location": "Remote – Mumbai"}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10003", "updates": {"position_id": "POS3005", "role_description": "Lead Engineer"}},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 152250,
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "currency": "USD",
                        "effective_date": "2025-07-01",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Lead Engineer",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            # --- Final Verification ---
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10004",
                    "work_location": "Remote – Mumbai"
                },
                {
                    "employee_id": "E10003",
                    "position_id": "POS3005",
                    "role_description": "Lead Engineer",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_18",
        instruction="Effective 2025-07-24, transfer Michael Park (E10002) to the Marketing department (DEPT1005). As part of this move, enroll him IND the 'Commuter Stipend - EU' plan (BEN4005). Log a performance review with the summary 'Transfer and benefit update.' For verification, retrieve his updated employee record.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10002", "updates": {"department_id": "DEPT1005"}},
            ),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10002",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4005"],
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Transfer and benefit update",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"performance_review_ids": ["PR5002", "PR10000"]},
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10002",
                "department_id": "DEPT1005",
                "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4005"],
                "performance_review_ids": ["PR5002", "PR10000"]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_19",
        instruction="Effective 2025-06-24, process a leadership change. Promote Isabella Chen (E10001) to CEO (POS4000) with a new $400,000 base salary, 35% bonus, and 90,000 equity grant. Appoint Emma Rodriguez (E10003) as the new head of the Engineering department (DEPT1001). Log a performance review for Sophia with the summary 'Promotion to CEO.' For verification, retrieve the updated records for both employees and the Engineering department.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10001"}),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10001",
                        "base_salary": 400000,
                        "bonus_target_pct": 35,
                        "equity_grant": 90000,
                        "currency": "USD",
                        "effective_date": "2025-06-24",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Promotion to CEO",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "position_id": "POS4000",
                        "role_description": "Chief Executive Officer",
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5001", "PR10000"],
                    },
                },
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1001", "updates": {"head_id": "E10003"}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10001",
                    "position_id": "POS4000",
                    "role_description": "Chief Executive Officer",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5001", "PR10000"]
                },
                {
                    "employee_id": "E10003"
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "head_id": "E10003"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_20",
        instruction="Process a departmental reorganization, effective 2025-06-24. The Finance department (DEPT1004) is being merged into the Human Resources department (DEPT1003). Transfer all active employees from Finance to HR. William Liu (E10006) will be the new head of the combined HR department. Zero out the old Finance budget and set the new HR budget to $2,000,000. Log a performance review for Marcus to document the transition. For verification, provide an updated roster of all active employees IND the HR department.",
        actions=[
            Action(
                name="FindEmployees",
                kwargs={"filters": {"department_id": "DEPT1004", "status": "Active"}},
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {"department_id": "DEPT1003", "manager_id": "E10006"},
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {"department_id": "DEPT1003"},
                },
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={
                    "department_id": "DEPT1004",
                    "updates": {"budget": 0, "head_id": None},
                },
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={
                    "department_id": "DEPT1003",
                    "updates": {"budget": 2000000, "head_id": "E10006"},
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10006",
                        "period_start": "2025-06-24",
                        "period_end": "2025-06-24",
                        "rating": None,
                        "summary": None,
                    }
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10006"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {"performance_review_ids": ["PR5011", "PR10000"]},
                },
            ),
            Action(
                name="FindEmployees",
                kwargs={"filters": {"department_id": "DEPT1003", "status": "Active"}},
            ),
        ],
        outputs=[
            """
            {
                "count": 2,
                "results": [
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
                        "department_id": "DEPT1003",
                        "level_id": "L.1",
                        "manager_id": "E10006",
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
                        "notes": "Recent graduate—ESADE Business School."
                    },
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
                        "department_id": "DEPT1003",
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
                            "PR10000"
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
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_21",
        instruction="Effective 2025-06-24, process an equity refresh for Michael Park (E10002), increasing his equity grant by $15,000 and updating his role description to 'Senior Sales Executive'. Log a performance review with the summary 'Equity refresh and title change.' To fund this, increase the Sales department (DEPT1002) budget by $15,000. As part of the same process, append the note 'Q3 compensation audit complete.' to the HR department's (DEPT1003) description. For verification, retrieve the updated records for Michael Park and both departments.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10002"}),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10002",
                        "equity_grant": 55000,
                        "base_salary": 210000,
                        "bonus_target_pct": 25,
                        "currency": "USD",
                        "effective_date": "2025-06-24",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10002", "updates": {"role_description": "Senior Sales Executive"}},
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Equity refresh and title change",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5002", "PR10000"],
                    },
                },
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1002"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 5015000}},
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1003"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1003", "updates": {"description": "Manages recruitment, retention, and employee well-being. Q3 compensation audit complete."}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1003"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10002",
                    "role_description": "Senior Sales Executive",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5002", "PR10000"]
                },
                {
                    "department_id": "DEPT1002",
                    "name": "Sales",
                    "budget": 5015000
                },
                {
                    "department_id": "DEPT1003",
                    "name": "Human Resources",
                    "description": "Manages recruitment, retention, and employee well-being. Q3 compensation audit complete."
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_22",
        instruction="The company is launching a new Employee Assistance Program (EAP). Create the new benefit plan IND the system using ID BEN10002, with 'ComPsych' as the provider and 100% employer coverage. Once the plan exists, you need to enroll every currently active employee. To verify the rollout, provide the updated employee record for Isabella Chen (E10001).",
        actions=[
            Action(
                name="CreateBenefitPlan",
                kwargs={
                    "benefit_plan": {
                        "benefit_plan_id": "BEN10002",
                        "name": "Employee Assistance Program",
                        "provider": "ComPsych",
                        "employer_coverage_pct": 100,
                    }
                },
            ),
            Action(name="FindEmployees", kwargs={"filters": {"status": "Active"}}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10001",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003", "BEN10002"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10002",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN10002"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10003",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4004", "BEN10002"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10004",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN10002"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10005"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10005",
                    "benefit_plan_ids": ["BEN4001", "BEN4005", "BEN10002"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10006"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10006",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003", "BEN10002"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
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
                    "BEN4003",
                    "BEN10002"
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
                "notes": "Founder-level equity grant."
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_23",
        instruction="Process a paid sabbatical for Emma Rodriguez (E10003) from 2026-01-01 to 2026-07-01, and it should be logged and immediately approved. Per policy, an employee's bonus is set to 0% during a sabbatical, so you need to create a new compensation record reflecting this change, effective on the leave start date. Pull up her new compensation record.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10003"}),
            Action(name="GetNewLeaveId", kwargs={}),
            Action(
                name="CreateLeaveRecord",
                kwargs={
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10003",
                        "leave_type": "Sabbatical",
                        "start_date": "2026-01-01",
                        "end_date": "2026-07-01",
                        "status": "Pending",
                    }
                },
            ),
            Action(
                name="UpdateLeaveStatus",
                kwargs={"leave_id": "LV10000", "status": "Approved"},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 145000,
                        "currency": "USD",
                        "bonus_target_pct": 0,
                        "equity_grant": 15000,
                        "effective_date": "2026-01-01",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                    },
                },
            ),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            [
                {
                    "compensation_id": "COMP10000",
                    "employee_id": "E10003",
                    "base_salary": 145000,
                    "currency": "USD",
                    "bonus_target_pct": 0,
                    "equity_grant": 15000,
                    "effective_date": "2026-01-01"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_24",
        instruction="Rehire Olivia Martinez (E10005) as Senior Accountant (POS3013) IND the finance department on 2025-09-01 with a €85,000 salary. Update her status to 'Active', set her benefits to Medical-PPO (BEN4001) & Dental (BEN4002), and log a rehiring review with the summary 'Re-hire processing.'. As her manager, William Liu (E10006), will now oversee re-hires, update his role description to 'Senior Product Manager, Team Lead'. For verification, retrieve both updated employee records.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10005"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "status": "Active",
                        "hire_date": "2025-09-01",
                        "termination_date": None,
                        "position_id": "POS3013",
                        "role_description": "Senior Accountant",
                    },
                },
            ),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10005",
                    "benefit_plan_ids": ["BEN4001", "BEN4002"],
                },
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10005",
                        "base_salary": 85000,
                        "currency": "EUR",
                        "effective_date": "2025-09-01",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10005",
                        "summary": "Re-hire processing.",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR10000"],
                    },
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10006", "updates": {"role_description": "Senior Product Manager, Team Lead"}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10005"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10006"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10005",
                    "status": "Active",
                    "hire_date": "2025-09-01",
                    "position_id": "POS3013",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR10000"]
                },
                {
                    "employee_id": "E10006",
                    "role_description": "Senior Product Manager, Team Lead"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_25",
        instruction="Due to budget cuts effective 2025-06-24, reduce the Marketing (DEPT1005) budget by €300,000 and prepend 'HIRING FREEZE: H2 2025.' to its description. As part of this, transfer William Liu (E10006) to the Finance department (DEPT1004) and promote him to 'Senior Financial Analyst' (POS3010), which includes a 5% salary increase. Log a performance review with the summary 'Transfer and promotion due to restructuring.' For verification, retrieve the updated records for Marcus and the Marketing department.",
        actions=[
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1005"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={
                    "department_id": "DEPT1005",
                    "updates": {
                        "budget": 1300000,
                        "description": "HIRING FREEZE: H2 2025. Drives brand awareness and demand generation.",
                    },
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10006"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10006"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10006", "updates": {"department_id": "DEPT1004", "position_id": "POS3010", "role_description": "Senior Financial Analyst"}},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10006",
                        "base_salary": 63000,
                        "bonus_target_pct": 5,
                        "equity_grant": 5000,
                        "currency": "EUR",
                        "effective_date": "2025-06-24",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10006",
                        "summary": "Transfer and promotion due to restructuring",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5011", "PR10000"],
                    },
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10006"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1005"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10006",
                    "department_id": "DEPT1004",
                    "position_id": "POS3010",
                    "role_description": "Senior Financial Analyst",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5011", "PR10000"]
                },
                {
                    "department_id": "DEPT1005",
                    "name": "Marketing",
                    "budget": 1300000,
                    "description": "HIRING FREEZE: H2 2025. Drives brand awareness and demand generation."
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_26",
        instruction="Effective 2025-06-30, process the termination of Adrian Thompson (E99999). Follow all off-boarding procedures, including clearing his benefits, zeroing out his final compensation, and logging a performance review with the summary 'Termination.' To backfill his duties, update Michael Park's (E10002) role description to 'Interim Team Lead.' For verification, retrieve the updated records for both employees.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E99999"}),
            Action(
                name="TerminateEmployee",
                kwargs={"employee_id": "E99999", "termination_date": "2025-06-30"},
            ),
            Action(
                name="SetEmployeeBenefits",
                kwargs={"employee_id": "E99999", "benefit_plan_ids": []},
            ),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP_FINAL_E99999",
                        "employee_id": "E99999",
                        "base_salary": 0,
                        "bonus_target_pct": 0,
                        "equity_grant": 0,
                        "effective_date": "2025-06-30",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E99999",
                        "summary": "Termination",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E99999",
                    "updates": {
                        "compensation_id": "COMP_FINAL_E99999",
                        "performance_review_ids": ["PR10000"],
                    },
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10002", "updates": {"role_description": "Interim Team Lead"}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E99999"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E99999",
                    "status": "Terminated",
                    "compensation_id": "COMP_FINAL_E99999",
                    "performance_review_ids": ["PR10000"]
                },
                {
                    "employee_id": "E10002",
                    "role_description": "Interim Team Lead"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_27",
        instruction="We're rolling out the existing Legal Insurance plan (BEN9999) to all active, USA-national employees. Enroll all eligible employees IND this plan. As a separate administrative update, also increase the monthly employee cost of the Dental plan (BEN4002) to $25. To verify, provide an updated list of all active USA-national employees.",
        actions=[
            Action(
                name="UpdateBenefitPlan",
                kwargs={
                    "benefit_plan_id": "BEN4002",
                    "updates": {"employee_cost_monthly": 25},
                },
            ),
            Action(
                name="FindEmployees",
                kwargs={"filters": {"nationality": "USA", "status": "Active"}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10001",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003", "BEN9999"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10002",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN9999"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10003",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4004", "BEN9999"],
                },
            ),
            Action(
                name="FindEmployees",
                kwargs={"filters": {"nationality": "USA", "status": "Active"}},
            ),
        ],
        outputs=[
            """
            {
                "count": 3,
                "results": [
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
                            "BEN4003",
                            "BEN9999"
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
                        "notes": "Founder-level equity grant."
                    },
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
                            "BEN9999"
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
                    },
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
                            "BEN9999"
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
                        "notes": "On parental leave 2024-11-01 → 2025-02-01."
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_28",
        instruction="Create a new 'Tech Allowance' benefit plan with ID BEN10003 and provider 'HR Ops'. Enroll all active staff IND the Engineering department (DEPT1001). Concurrently, promote the department head, Isabella Chen (E10001), to 'Principal Engineer' (POS4001) at level L.D, which includes a 5% salary increase, effective 2025-07-24. Log a performance review for her with the summary 'Promotion and benefit rollout oversight.' For verification, retrieve the updated records for Sophia and the Engineering department.",
        actions=[
            Action(
                name="CreateBenefitPlan",
                kwargs={
                    "benefit_plan": {
                        "benefit_plan_id": "BEN10003",
                        "name": "Tech Allowance",
                        "provider": "HR Ops",
                    }
                },
            ),
            Action(
                name="FindEmployees",
                kwargs={"filters": {"department_id": "DEPT1001", "status": "Active"}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10001",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003", "BEN10003"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10004",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN10003"],
                },
            ),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10001"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10001", "updates": {"position_id": "POS4001", "level_id": "L.D", "role_description": "Principal Engineer"}},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10001",
                        "base_salary": 341250,
                        "bonus_target_pct": 30,
                        "equity_grant": 75000,
                        "currency": "USD",
                        "effective_date": "2025-07-24",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Promotion and benefit rollout oversight",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5001", "PR10000"],
                    },
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10001",
                    "position_id": "POS4001",
                    "level_id": "L.D",
                    "role_description": "Principal Engineer",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5001", "PR10000"]
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_29",
        instruction="Create a new 'Diversity Scholarship' benefit plan with ID BEN10004, provider 'HR D&I', and an annual amount of $2,000. Once created, enroll all active employees with an ethnicity code of either 'H' or 'B'. For each enrolled employee, append the following to their record's notes field: 'Enrolled IND Diversity Scholarship 2025.'. For verification, provide a list of the updated records for all employees who were enrolled.",
        actions=[
            Action(
                name="CreateBenefitPlan",
                kwargs={
                    "benefit_plan": {
                        "benefit_plan_id": "BEN10004",
                        "name": "Diversity Scholarship",
                        "provider": "HR D&I",
                        "annual_amount": 2000,
                    }
                },
            ),
            Action(
                name="FindEmployees",
                kwargs={"filters": {"status": "Active", "ethnicity_code": "H"}},
            ),
            Action(
                name="FindEmployees",
                kwargs={"filters": {"status": "Active", "ethnicity_code": "B"}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10003",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4004", "BEN10004"],
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "notes": "On parental leave 2024-11-01 → 2025-02-01. Enrolled IND Diversity Scholarship 2025."
                    },
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10005"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10005",
                    "benefit_plan_ids": ["BEN4001", "BEN4005", "BEN10004"],
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "notes": "Recent graduate—ESADE Business School. Enrolled IND Diversity Scholarship 2025."
                    },
                },
            ),
            Action(
                name="FindEmployees",
                kwargs={"filters": {"status": "Active", "ethnicity_code": "H"}},
            ),
        ],
        outputs=[
            """
            {
                "count": 2,
                "results": [
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
                            "BEN10004"
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
                        "notes": "On parental leave 2024-11-01 → 2025-02-01. Enrolled IND Diversity Scholarship 2025."
                    },
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
                            "BEN10004"
                        ],
                        "performance_review_ids": [],
                        "skills": [
                            "Financial Modeling",
                            "SQL",
                            "Excel"
                        ],
                        "role_description": "Junior Financial Analyst supporting quarterly forecasts.",
                        "notes": "Recent graduate—ESADE Business School. Enrolled IND Diversity Scholarship 2025."
                    }
                ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_30",
        instruction="Effective 2025-07-01, promote Arjun Patel (E10004) to 'Lead Backend Engineer' (POS3009) at level L.3, which includes an 8% salary increase. To backfill his role, transfer Michael Park (E10002) to Rahul's previous department (DEPT1001) and manager (E10003). Log a performance review for Rahul with the summary 'Promotion to Lead Engineer.' Also, update the description of the Engineering department (DEPT1001) to 'Core product and platform engineering.' For verification, retrieve the updated records for Arjun Patel and the Engineering department.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10004"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10004", "updates": {"position_id": "POS3009", "level_id": "L.3", "role_description": "Lead Backend Engineer"}},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10004",
                        "base_salary": 127440,
                        "bonus_target_pct": 10,
                        "equity_grant": 8000,
                        "currency": "USD",
                        "effective_date": "2025-07-01",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "summary": "Promotion to Lead Engineer",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5004", "PR5009", "PR10000"],
                    },
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10002", "updates": {"department_id": "DEPT1001", "manager_id": "E10003"}},
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1001", "updates": {"description": "Core product and platform engineering."}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10004",
                    "position_id": "POS3009",
                    "level_id": "L.3",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5004", "PR5009", "PR10000"]
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "description": "Core product and platform engineering."
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_31",
        instruction="Onboard a new Engineering Intern, Liam Chen, effective 2025-07-01, into the Engineering department (DEPT1001) with a $35,000 salary. His manager will be Emma Rodriguez (E10003). Log a performance review for Liam with the summary 'New hire onboarding.' To fund the new role, transfer $50,000 from the Sales department (DEPT1002) to Engineering. For verification, retrieve the updated records for Liam Chen and the Engineering department.",
        actions=[
            Action(name="GetNewEmployeeId", kwargs={}),
            Action(
                name="CreateNewEmployee",
                kwargs={
                    "employee": {
                        "employee_id": "E10000",
                        "first_name": "Liam",
                        "last_name": "Chen",
                        "status": "Active",
                        "hire_date": "2025-07-01",
                        "department_id": "DEPT1001",
                        "manager_id": "E10003",
                        "role_description": "Engineering Intern",
                    }
                },
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10000",
                        "base_salary": 35000,
                        "currency": "USD",
                        "effective_date": "2025-07-01",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10000",
                        "summary": "New hire onboarding",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10000",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR10000"],
                    },
                },
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4950000}},
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7050000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10000"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10000",
                    "first_name": "Liam",
                    "last_name": "Chen",
                    "department_id": "DEPT1001",
                    "manager_id": "E10003",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR10000"]
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
        user_id="res_32",
        instruction="Finalize Isabella Chen's (E10001) parental leave (LV7001) by updating its status to 'Approved'. Appoint Emma Rodriguez (E10003) as acting manager. As part of this temporary role, process a 5% salary increase for Amelia, effective on the leave start date of 2025-07-01. Log a performance review for Amelia with the summary 'Acting manager assignment.' For verification, retrieve both updated employee records.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(
                name="UpdateLeaveStatus",
                kwargs={"leave_id": "LV7001", "status": "Approved"},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10003", "updates": {"role_description": "Acting Manager"}},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 152250,
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "currency": "USD",
                        "effective_date": "2025-07-01",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Acting manager assignment",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10001"
                },
                {
                    "employee_id": "E10003",
                    "role_description": "Acting Manager",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_33",
        instruction="As part of a personnel file audit, log a review for Isabella Chen (E10001) with the summary 'Q3 2025 personnel file audit completed.' Concurrently, transfer Michael Park (E10002) to her department (DEPT1001) and make Sophia his new manager. As part of his transfer, process a 5% salary increase for him, effective 2025-07-01. For verification, retrieve both updated employee records.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Q3 2025 personnel file audit completed.",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"performance_review_ids": ["PR5001", "PR10000"]},
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10002"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10002", "updates": {"department_id": "DEPT1001", "manager_id": "E10001"}},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10002",
                        "base_salary": 220500,
                        "bonus_target_pct": 25,
                        "equity_grant": 40000,
                        "currency": "USD",
                        "effective_date": "2025-07-01",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"compensation_id": "COMP10000"},
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10001",
                    "performance_review_ids": ["PR5001", "PR10000"]
                },
                {
                    "employee_id": "E10002",
                    "department_id": "DEPT1001",
                    "manager_id": "E10001",
                    "compensation_id": "COMP10000"
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_34",
        instruction="We're launching a new Employee Stock Purchase Plan (ESPP). Create the benefit plan with ID BEN10005, provider 'Fidelity', and 0% employer coverage. Per the policy, you need to auto-enroll all active employees who are at level L.4 or higher (L.4, L.5, and L.C). Once they are all enrolled, please pull up the employee record for Isabella Chen (E10001) to verify the change.",
        actions=[
            Action(
                name="CreateBenefitPlan",
                kwargs={
                    "benefit_plan": {
                        "benefit_plan_id": "BEN10005",
                        "name": "Employee Stock Purchase Plan",
                        "provider": "Fidelity",
                        "employer_coverage_pct": 0,
                    }
                },
            ),
            Action(
                name="FindEmployees",
                kwargs={"filters": {"level_id": "L.4", "status": "Active"}},
            ),
            Action(
                name="FindEmployees",
                kwargs={"filters": {"level_id": "L.5", "status": "Active"}},
            ),
            Action(
                name="FindEmployees",
                kwargs={"filters": {"level_id": "L.C", "status": "Active"}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10001",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003", "BEN10005"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10002",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN10005"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10006"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10006",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003", "BEN10005"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
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
                    "BEN4003",
                    "BEN10005"
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
                "notes": "Founder-level equity grant."
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_35",
        instruction="Effective 2025-07-24, process a benefits and compensation update for Olivia Martinez (E10005). Discontinue her 'Commuter Stipend - EU' (BEN4005) and enroll her IND two replacement plans: Dental (BEN4002) and Legal Insurance (BEN9999). As part of this update, also process a 5% salary increase. Log a single performance review with the summary 'Benefit and compensation update.' To fund the salary increase, increase the Finance department's (DEPT1004) budget by the exact amount of her raise. For verification, retrieve her updated employee record and the updated Finance department record.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10005"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10005"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10005",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN9999"],
                },
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10005",
                        "base_salary": 75600,
                        "bonus_target_pct": 5,
                        "equity_grant": 2000,
                        "currency": "EUR",
                        "effective_date": "2025-07-24",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10005",
                        "summary": "Benefit and compensation update",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR10000"],
                    },
                },
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1004"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1004", "updates": {"budget": 1203600}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10005"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1004"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10005",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN9999"],
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR10000"]
                },
                {
                    "department_id": "DEPT1004",
                    "name": "Finance",
                    "budget": 1203600
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_36",
        instruction="Effective 2025-07-01, process a 3% cost-of-living adjustment (COLA) for Olivia Martinez (E10005) by creating a new compensation record. Concurrently, promote the Finance department head, William Liu (E10006), to 'Senior Director' (POS4003). Log a single performance review for Marcus with the summary 'Promotion to Senior Director.' Increase the Finance department budget by $50,000 to cover these changes. For verification, retrieve the updated records for both employees and the Finance department.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10005"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10005"}),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10005",
                        "base_salary": 74160,
                        "bonus_target_pct": 5,
                        "equity_grant": 2000,
                        "currency": "EUR",
                        "effective_date": "2025-07-01",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {"compensation_id": "COMP10000"},
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10006"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10006", "updates": {"position_id": "POS4003", "role_description": "Senior Director"}},
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10006",
                        "summary": "Promotion to Senior Director",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {"performance_review_ids": ["PR5011", "PR10000"]},
                },
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1004"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1004", "updates": {"budget": 1250000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10005"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10006"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1004"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10005",
                    "compensation_id": "COMP10000"
                },
                {
                    "employee_id": "E10006",
                    "position_id": "POS4003",
                    "role_description": "Senior Director",
                    "performance_review_ids": ["PR5011", "PR10000"]
                },
                {
                    "department_id": "DEPT1004",
                    "name": "Finance",
                    "budget": 1250000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_37",
        instruction="We're adding a new 'Mental-Health Support' benefit. Create the new plan with ID BEN10006, provider 'Lyra Health', 100 sessions per year, and 100% employer coverage. This benefit should be rolled out to all active employees with USA nationality. To verify the rollout is complete, pull up the updated employee record for Michael Park (E10002).",
        actions=[
            Action(
                name="CreateBenefitPlan",
                kwargs={
                    "benefit_plan": {
                        "benefit_plan_id": "BEN10006",
                        "name": "Mental-Health Support",
                        "provider": "Lyra Health",
                        "sessions_per_year": 100,
                        "employer_coverage_pct": 100,
                    }
                },
            ),
            Action(
                name="FindEmployees",
                kwargs={"filters": {"nationality": "USA", "status": "Active"}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10001",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003", "BEN10006"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10002",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN10006"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10003",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4004", "BEN10006"],
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10002"}),
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
                    "BEN10006"
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
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_38",
        instruction="Effective 2025-07-24, promote Emma Rodriguez (E10003) to a 'Senior Engineer' role (POS3005) at level L.4 and update her role description to 'Senior Engineer'. This promotion includes an 8% salary increase. To backfill her previous role, transfer Arjun Patel (E10004) to her old position (POS3006). Log a performance review for Amelia with the summary 'Promotion to Senior Engineer.' To fund the promotion, transfer $20,000 from the Sales department's budget (DEPT1002) to Engineering (DEPT1001). For verification, retrieve the updated records for both employees and the Engineering department.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10003", "updates": {"position_id": "POS3005", "level_id": "L.4", "role_description": "Senior Engineer"}},
            ),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 156600,
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "currency": "USD",
                        "effective_date": "2025-07-24",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Senior Engineer",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10004", "updates": {"position_id": "POS3006"}},
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1002"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4980000}},
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7020000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10003",
                    "position_id": "POS3005",
                    "level_id": "L.4",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                },
                {
                    "employee_id": "E10004",
                    "position_id": "POS3006"
                },
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "budget": 7020000
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_39",
        instruction="As a performance reward for Isabella Chen (E10001), whose most recent rating was 'Exceeds', increase her bonus target by 10 percentage points, effective 2025-07-01. Log a performance review with the summary 'Exceeds Performance Bonus.' To support her, transfer Arjun Patel (E10004) to her team as a direct report. To fund the bonus, transfer $10,000 from the HR department's budget (DEPT1003) to Engineering (DEPT1001). For verification, retrieve the updated records for both employees and the Engineering department.",
        actions=[
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(name="GetPerformanceReviewsByEmployeeId", kwargs={"employee_id": "E10001"}),
            Action(name="GetCompensationByEmployeeId", kwargs={"employee_id": "E10001"}),
            Action(name="GetNewCompensationId", kwargs={}),
            Action(
                name="SetCompensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10001",
                        "base_salary": 325000,
                        "bonus_target_pct": 40,
                        "equity_grant": 75000,
                        "currency": "USD",
                        "effective_date": "2025-07-01",
                    }
                },
            ),
            Action(name="GetNewReviewId", kwargs={}),
            Action(
                name="CreatePerformanceReview",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Exceeds Performance Bonus",
                    }
                },
            ),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5001", "PR10000"],
                    },
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(
                name="UpdateEmployeeRecord",
                kwargs={"employee_id": "E10004", "updates": {"manager_id": "E10001"}},
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1003"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1003", "updates": {"budget": 790000}},
            ),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7010000}},
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            """
            [
                {
                    "employee_id": "E10001",
                    "compensation_id": "COMP10000",
                    "performance_review_ids": ["PR5001", "PR10000"]
                },
                {
                    "employee_id": "E10004",
                    "manager_id": "E10001"
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
        user_id="res_40",
        instruction="Create a new 'Remote-Work Stipend' benefit plan with ID BEN10007, provider 'HR Ops', and an annual amount of $1,500. Next, enroll all active employees whose work location is either 'Remote – Austin, TX' or 'Remote – Bangalore'. To fund this, increase the budget of each remote employee's respective department by $1,500. For verification, provide an updated list of all departments.",
        actions=[
            Action(
                name="CreateBenefitPlan",
                kwargs={
                    "benefit_plan": {
                        "benefit_plan_id": "BEN10007",
                        "name": "Remote-Work Stipend",
                        "provider": "HR Ops",
                        "annual_amount": 1500,
                    }
                },
            ),
            Action(
                name="FindEmployees",
                kwargs={
                    "filters": {
                        "work_location": "Remote – Austin, TX",
                        "status": "Active",
                    }
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10003"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10003",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4004", "BEN10007"],
                },
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1005"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1005", "updates": {"budget": 1601500}},
            ),
            Action(
                name="FindEmployees",
                kwargs={
                    "filters": {
                        "work_location": "Remote – Bangalore",
                        "status": "Active",
                    }
                },
            ),
            Action(name="GetEmployeeById", kwargs={"employee_id": "E10004"}),
            Action(
                name="SetEmployeeBenefits",
                kwargs={
                    "employee_id": "E10004",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN10007"],
                },
            ),
            Action(name="GetDepartmentById", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="UpdateDepartmentRecord",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7001500}},
            ),
            Action(name="ListDepartments", kwargs={}),
        ],
        outputs=[
            """
            [
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "head_id": "E10001",
                    "location": "Seattle HQ",
                    "budget": 7001500,
                    "description": "Responsible for all product development and technical operations."
                },
                {
                    "department_id": "DEPT1002",
                    "name": "Sales",
                    "head_id": "E10012",
                    "location": "Boston Office",
                    "budget": 5000000,
                    "description": "Owns revenue generation and customer relationships."
                },
                {
                    "department_id": "DEPT1003",
                    "name": "Human Resources",
                    "head_id": "E10009",
                    "location": "Seattle HQ",
                    "budget": 800000,
                    "description": "Manages recruitment, retention, and employee well-being."
                },
                {
                    "department_id": "DEPT1004",
                    "name": "Finance",
                    "head_id": "E10011",
                    "location": "Barcelona Office",
                    "budget": 1200000,
                    "description": "Oversees accounting, compliance, and financial planning."
                },
                {
                    "department_id": "DEPT1005",
                    "name": "Marketing",
                    "head_id": "E10013",
                    "location": "Manchester Office",
                    "budget": 1601500,
                    "description": "Drives brand awareness and demand generation."
                }
            ]
            """
        ],
    ),
]
