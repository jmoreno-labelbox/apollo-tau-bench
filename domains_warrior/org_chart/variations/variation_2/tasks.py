from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="res_01",
        instruction="Effective 2026-05-22, promote Amelia Garcia (E10003) to 'Lead Compliance Officer' (POS4002) at level L.4, which includes an 8% salary increase. To support her new role, reassign Daniel Kim (E10002) to be her direct report. Log a performance review for Amelia with the summary 'Promotion to Lead Compliance Officer.' For verification, retrieve the updated employee records for both.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10003", "updates": {"position_id": "POS4002", "level_id": "L.4", "role_description": "Lead Compliance Officer"}},
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "effective_date": "2026-05-22",
                    "salary_increase_pct": 8,
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Lead Compliance Officer",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10002", "updates": {"manager_id": "E10003"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
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
        instruction="Effective 2026-05-25, process an equity refresh for Amelia Garcia (E10003), granting her an additional $20,000 in equity. As this puts her in a new equity tier, update her role description to 'Principal Engineer', upload her signed 'Equity Grant Agreement' document, and log a performance review with the summary 'Equity refresh and tier promotion.' To recognize her manager, Sophia Nguyen (E10001), for 'Mentorship excellence,' issue her a one-time bonus of $1,000. For verification, retrieve both updated employee records.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "effective_date": "2026-05-25",
                    "equity_increase_amount": 20000,
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Equity refresh and tier promotion.",
                    }
                },
            ),
            Action(name="get_unused_document_id", kwargs={}),
            Action(
                name="add_employee_document",
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
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "role_description": "Principal Engineer",
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(name="get_unused_bonus_id", kwargs={}),
            Action(
                name="add_bonus_payment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10001",
                        "amount": 1000,
                        "reason": "Mentorship excellence.",
                    }
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
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
        instruction="Process and approve a 12-week parental leave for Sophia Nguyen (E10001) from 2025-08-01 to 2025-10-23. Appoint Amelia Garcia (E10003) as acting CTO for the duration, which includes a temporary 5% salary increase. Log a performance review for Amelia with the summary 'Acting CTO during S. Nguyen's leave.' To fund these changes, transfer $50,000 from the Sales department's budget (DEPT1002) to the Engineering department's (DEPT1001). For verification, retrieve the updated records for both employees and the Engineering department.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="get_unused_leave_id", kwargs={}),
            Action(
                name="request_leave",
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
                name="update_leave_status",
                kwargs={"leave_id": "LV10000", "status": "Approved"},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10003", "updates": {"role_description": "Acting CTO"}},
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-08-01",
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Acting CTO during S. Nguyen's leave.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1002"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4950000}},
            ),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7050000}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
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
        instruction="Process the termination of Elena Rodriguez (E10005), effective 2025-07-01. Follow all off-boarding procedures, including clearing her benefits, zeroing out her final compensation, and logging a performance review with the summary 'Termination.' To backfill her role, transfer Marcus Chen (E10006) to her previous position (POS3010) and update his role description to 'Senior Financial Analyst.' For verification, retrieve both updated employee records.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10005"}),
            Action(
                name="terminate_employee",
                kwargs={"employee_id": "E10005", "termination_date": "2025-07-01"},
            ),
            Action(
                name="set_employee_benefits",
                kwargs={"employee_id": "E10005", "benefit_plan_ids": []},
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="set_compensation",
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
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10005",
                        "summary": "Termination",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR10000"],
                    },
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10006"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10006", "updates": {"position_id": "POS3010", "role_description": "Senior Financial Analyst"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10005"}),
            Action(name="get_employee", kwargs={"employee_id": "E10006"}),
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
        instruction="Effective 2025-09-01, promote Amelia Garcia (E10003) to Staff Engineer (POS3005) at level L.4, which includes a 10% base salary increase. Log a performance review with the summary 'Promotion to Staff Engineer.' To backfill her previous role, transfer Daniel Kim (E10002) to her old position (POS3006). For verification, retrieve the updated records for both employees.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"position_id": "POS3005", "level_id": "L.4", "role_description": "Staff Engineer"},
                },
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 10,
                    "effective_date": "2025-09-01",
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Staff Engineer",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10002", "updates": {"position_id": "POS3006"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
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
        instruction="Effective 2025-08-01, increase the monthly employee cost for the Medical-PPO plan (BEN4001) to $170. Concurrently, promote Sophia Nguyen (E10001) to 'Lead Engineer' (POS3002) at level L.A, which includes a 10% salary increase. Enroll Andrian Roberts (E99999) in the updated Medical-PPO plan. Log a performance review for Sophia with the summary 'Promotion to Lead Engineer.' To fund the promotion, transfer $50,000 from the HR department's budget (DEPT1003) to the Engineering department's (DEPT1001). For verification, retrieve the updated employee records for both Andrian and Sophia, and the updated Engineering department record.",
        actions=[
            Action(
                name="update_benefit_plan",
                kwargs={"benefit_plan_id": "BEN4001", "updates": {"employee_cost_monthly": 170}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E99999"}),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E99999",
                    "updates": {"benefit_plan_ids": ["BEN9999", "BEN4001"]},
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10001"}),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"position_id": "POS3002", "level_id": "L.A"},
                },
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10001",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 10,
                    "effective_date": "2025-08-01",
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Promotion to Lead Engineer",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5001", "PR10000"],
                    },
                },
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1003"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1003", "updates": {"budget": 750000}},
            ),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7050000}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E99999"}),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
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
        instruction="Effective 2025-06-24, onboard a new HR Business Partner, Mary Smith, into the HR department (DEPT1003). Her compensation is a $110,000 salary, and she should be enrolled in benefits (BEN4001, BEN4002). Her manager will be Amelia Garcia (E10003). Log a performance review for Mary with the summary 'New hire onboarding.' To fund the new role, transfer $120,000 from the Sales department's budget (DEPT1002) to HR. For verification, retrieve the updated records for Mary Smith and the HR department.",
        actions=[
            Action(name="get_unused_employee_id", kwargs={}),
            Action(
                name="create_employee",
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
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="set_compensation",
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
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10000",
                        "summary": "New hire onboarding",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10000",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR10000"],
                    },
                },
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1002"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1003"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4880000}},
            ),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1003", "updates": {"budget": 920000}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10000"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1003"}),
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
        instruction="Effective 2025-10-15, process an internal transfer and promotion for Amelia Garcia (E10003) to 'Senior Software Engineer' (POS3009) at level L.3 in the Engineering department (DEPT1001), with a 10% salary increase. To backfill her old role, transfer Rahul Singh (E10004) to her previous position (POS3006). Log a performance review for Amelia with the summary 'Promotion and transfer to Engineering.' For verification, retrieve the updated employee record for Amelia.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
            Action(
                name="update_employee",
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
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 10,
                    "effective_date": "2025-10-15",
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion and transfer to Engineering",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10004", "updates": {"position_id": "POS3006"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
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
        instruction="Create a new 'Vision Plan' (BEN4006) with provider 'VSP' and a $15 monthly cost. Enroll all active employees in the Marketing department (DEPT1005). As part of this, transfer Daniel Kim (E10002) to the Marketing department and enroll him as well. Log a performance review for Amelia Garcia (E10003), with the summary 'Benefit rollout and new team member.' For verification, retrieve the updated records for Amelia, Daniel, and the Marketing department.",
        actions=[
            Action(
                name="add_benefit_plan",
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
                name="search_employees",
                kwargs={"filters": {"department_id": "DEPT1005", "status": "Active"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(
                name="set_employee_benefits",
                kwargs={
                    "employee_id": "E10003",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4004", "BEN4006"],
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10002", "updates": {"department_id": "DEPT1005"}},
            ),
            Action(
                name="set_employee_benefits",
                kwargs={
                    "employee_id": "E10002",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4006"],
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Benefit rollout and new team member.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"performance_review_ids": ["PR5003", "PR5010", "PR10000"]},
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1005"}),
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
        instruction="Process and approve a one-month unpaid sabbatical for Amelia Garcia (E10003) from 2025-11-01 to 2025-11-30. Appoint Rahul Singh (E10004) as acting team lead and issue him a one-time bonus of $2,500 for 'Acting team lead coverage.' Log a performance review for Amelia with the summary 'Unpaid sabbatical approved.' To fund the bonus, increase the Engineering department's (DEPT1001) budget by $2,500. For verification, retrieve the updated employee records for both Amelia and Rahul, and the updated Engineering department record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_unused_leave_id", kwargs={}),
            Action(
                name="request_leave",
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
                name="update_leave_status",
                kwargs={"leave_id": "LV10000", "status": "Approved"},
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Unpaid sabbatical approved",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"performance_review_ids": ["PR5003", "PR5010", "PR10000"]},
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10004", "updates": {"role_description": "Acting Team Lead"}},
            ),
            Action(name="get_unused_bonus_id", kwargs={}),
            Action(
                name="add_bonus_payment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10004",
                        "amount": 2500,
                        "reason": "Acting team lead coverage.",
                    }
                },
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7002500}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
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
        instruction="Initiate a 30-day Performance Improvement Plan (PIP) for Daniel Kim (E10002), starting on 2025-11-01, with the summary '30-day Performance Improvement Plan initiated.' and a 'Needs Improvement' rating. As part of the PIP, transfer him to the Marketing department (DEPT1005), upload his signed 'PIP Agreement' document, and create a new compensation record to set his bonus target to 0%. To support this, transfer $10,000 from the Sales department's budget (DEPT1002) to Marketing. For verification, retrieve the updated records for Daniel Kim and the Marketing department.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10002"}),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
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
            Action(name="get_unused_document_id", kwargs={}),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10002",
                        "title": "PIP Agreement",
                        "date": "2025-11-01",
                    }
                },
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="set_compensation",
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
                name="update_employee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "department_id": "DEPT1005",
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5002", "PR10000"],
                    },
                },
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1002"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1005"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4990000}},
            ),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1005", "updates": {"budget": 1610000}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1005"}),
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
        instruction="Approve the request for Sophia Nguyen (E10001) to work remotely from 'Remote – Seattle', effective 2025-07-24. Update her work location and upload her signed 'Remote Work Agreement', then verify the upload. As part of this team restructuring, reassign Daniel Kim (E10002) to report directly to Sophia. Log a performance review for Sophia with the summary 'Remote work transition.' For verification, retrieve the updated employee records for both.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10001", "updates": {"work_location": "Remote – Seattle"}},
            ),
            Action(name="get_unused_document_id", kwargs={}),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10001",
                        "title": "Remote Work Agreement",
                        "date": "2025-07-24",
                    }
                },
            ),
            Action(name="list_employee_documents", kwargs={"employee_id": "E10001"}),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Remote work transition",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"performance_review_ids": ["PR5001", "PR10000"]},
                },
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10002", "updates": {"manager_id": "E10001"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
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
        instruction="Extend Sophia Nguyen's (E10001) parental leave (LV7001) to 2026-02-15 and update her status to 'On Leave'. Appoint Amelia Garcia (E10003) as acting CTO, which includes a temporary 5% salary increase effective on the leave start date. Log a performance review for Amelia with the summary 'Acting CTO coverage.' For verification, retrieve the updated employee record for Amelia.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="list_employee_leaves", kwargs={"employee_id": "E10001"}),
            Action(
                name="update_leave_record",
                kwargs={"leave_id": "LV7001", "updates": {"end_date": "2026-02-15"}},
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10001", "updates": {"status": "On Leave"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10003", "updates": {"role_description": "Acting CTO"}},
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-07-01",
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Acting CTO coverage.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
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
        instruction="Promote Daniel Kim (E10002) to Senior Analyst (POS3012) at level L.2, effective 2025-12-01, which includes a 7% base salary increase. Log a new performance review with an 'Exceeds' rating and the summary 'Promoted to Senior Analyst (L.2).' To recognize his manager, Marcus Chen (E10006), for this successful promotion, issue him a one-time bonus of €1,000 for 'Team development.' For verification, retrieve both updated employee records.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10002"}),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"level_id": "L.2", "position_id": "POS3012", "role_description": "Senior Analyst"},
                },
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10002",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 7,
                    "effective_date": "2025-12-01",
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
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
                name="update_employee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5002", "PR10000"],
                    },
                },
            ),
            Action(name="get_unused_bonus_id", kwargs={}),
            Action(
                name="add_bonus_payment",
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
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_employee", kwargs={"employee_id": "E10006"}),
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
        instruction="Effective 2025-12-01, remove the 'Vision Plan' (BEN4006) from Sophia Nguyen's (E10001) benefits and upload a 'Benefit Change Form' to her file. To recognize her manager, Amelia Garcia (E10003), for handling this transition, issue her a one-time bonus of $500 for 'Administrative excellence.' Log a performance review for Sophia with the summary 'Benefit change processed.' To fund the bonus, increase the Engineering department's (DEPT1001) budget by $500. For verification, retrieve both updated employee records and the updated Engineering department record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003"]},
                },
            ),
            Action(name="get_unused_document_id", kwargs={}),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10001",
                        "title": "Benefit Change Form",
                        "date": "2025-12-01",
                    }
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Benefit change processed",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"performance_review_ids": ["PR5001", "PR10000"]},
                },
            ),
            Action(name="get_unused_bonus_id", kwargs={}),
            Action(
                name="add_bonus_payment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10003",
                        "amount": 500,
                        "reason": "Administrative excellence.",
                    }
                },
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7000500}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
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
        instruction="Process and approve a 5-day bereavement leave for Daniel Kim (E10002) from 2025-12-10 to 2025-12-14. Appoint Rahul Singh (E10004) as acting manager for Daniel during the leave, which includes a temporary 5% salary increase. Log a performance review for Rahul with the summary 'Acting manager coverage.' For verification, retrieve the updated employee records for both Daniel and Rahul.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_unused_leave_id", kwargs={}),
            Action(
                name="request_leave",
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
                name="update_leave_status",
                kwargs={"leave_id": "LV10000", "status": "Approved"},
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10002", "updates": {"manager_id": "E10004"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10004"}),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10004",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-12-10",
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "summary": "Acting manager coverage",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5004", "PR5009", "PR10000"],
                    },
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
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
        instruction="Effective 2026-01-01, process a 3% cost-of-living salary increase for Amelia Garcia (E10003) and log a performance review with the summary 'COLA applied.' As part of the same audit, issue a one-time bonus of $2,000 to Daniel Kim (E10002) for 'cross-functional collaboration.' To fund these changes, transfer $15,000 from the HR department's budget (DEPT1003) to the Sales department's (DEPT1002). For verification, retrieve the updated employee records for both and the updated Sales department record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 3,
                    "effective_date": "2026-01-01",
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "COLA applied.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"]
                    },
                },
            ),
            Action(name="get_unused_bonus_id", kwargs={}),
            Action(
                name="add_bonus_payment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10002",
                        "amount": 2000,
                        "reason": "cross-functional collaboration",
                    }
                },
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1003"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1002"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1003", "updates": {"budget": 785000}},
            ),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 5015000}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1002"}),
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
        instruction="Approve the request for Daniel Kim (E10002) to work remotely from 'Remote – Austin', effective 2025-07-24. Update his work location and upload his signed 'Remote Work Agreement'. As part of the remote work package, process a 5% salary increase for him. Log a performance review with the summary 'Remote work and compensation updated.' For verification, retrieve his updated employee record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10002"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10002", "updates": {"work_location": "Remote – Austin"}},
            ),
            Action(name="get_unused_document_id", kwargs={}),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10002",
                        "title": "Remote Work Agreement",
                        "date": "2025-07-24",
                    }
                },
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10002",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-07-24",
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Remote work and compensation updated.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5002", "PR10000"],
                    },
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            {
                "employee_id": "E10002",
                "work_location": "Remote – Austin",
                "compensation_id": "COMP10000",
                "performance_review_ids": ["PR5002", "PR10000"]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_19",
        instruction="Enroll Amelia Garcia (E10003) and Daniel Kim (E10002) in the 'Legal Insurance' plan (BEN9999), effective 2025-07-24. Log a single performance review for their manager, Sophia Nguyen (E10001), with the summary 'Benefit enrollment processed for team.' For verification, retrieve the updated employee records for all three.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(
                name="set_employee_benefits",
                kwargs={
                    "employee_id": "E10003",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4004", "BEN9999"],
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(
                name="set_employee_benefits",
                kwargs={
                    "employee_id": "E10002",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN9999"],
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Benefit enrollment processed for team.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"performance_review_ids": ["PR5001", "PR10000"]},
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
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
        instruction="Effective 2026-01-01, process a compensation adjustment for Sophia Nguyen (E10001), creating a new record to set her bonus target to 25%. Log a performance review with the summary 'Bonus target adjusted.' To recognize her manager, issue a one-time bonus of $5,000 to Amelia Garcia (E10003) for 'Leadership excellence.' For verification, retrieve the updated employee records for both.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10001"}),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="set_compensation",
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
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Bonus target adjusted",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5001", "PR10000"],
                    },
                },
            ),
            Action(name="get_unused_bonus_id", kwargs={}),
            Action(
                name="add_bonus_payment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10003",
                        "amount": 5000,
                        "reason": "Leadership excellence.",
                    }
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
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
        instruction="Sophia Nguyen (E10001) is returning from parental leave (LV7001) early on 2025-08-31. Update her leave record to 'Taken' and her status to 'Active'. As a reward for successful team management during the leave, process a 5% salary increase for her manager, Amelia Garcia (E10003), and log a performance review with the summary 'Team management bonus.' For verification, retrieve Amelia's updated employee record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(
                name="update_leave_record",
                kwargs={"leave_id": "LV7001", "updates": {"end_date": "2025-08-31", "status": "Taken"}},
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10001", "updates": {"status": "Active"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-08-31",
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Team management bonus.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
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
        instruction="Process an equity refresh grant for Daniel Kim (E10002), effective 2026-01-15. His equity grant should be increased by $10,000. Log a performance review note with the summary 'Equity refresh of $10,000 granted.' to document this. For verification, retrieve his new, most recent compensation record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10002"}),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10002",
                    "compensation_id": "COMP10000",
                    "effective_date": "2026-01-15",
                    "equity_increase_amount": 10000,
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Equity refresh of $10,000 granted.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5002", "PR10000"],
                    },
                },
            ),
            Action(name="get_compensation", kwargs={"employee_id": "E10002"}),
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
        instruction="Effective 2026-01-01, process and approve a 6-month sabbatical for Amelia Garcia (E10003). Per policy, create a new compensation record to set her bonus target to 0% for the duration. Appoint Daniel Kim (E10002) as acting manager by updating his role description. Log a performance review for Amelia with the summary 'Sabbatical leave.' To fund this temporary change, transfer $15,000 from the Sales department's budget (DEPT1002) to the Engineering department's (DEPT1001). For verification, retrieve both updated employee records and the updated Engineering department record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
            Action(name="get_unused_leave_id", kwargs={}),
            Action(
                name="request_leave",
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
                name="update_leave_status",
                kwargs={"leave_id": "LV10000", "status": "Approved"},
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="set_compensation",
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
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Sabbatical leave",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10002", "updates": {"role_description": "Acting Manager"}},
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1002"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4985000}},
            ),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7015000}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
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
        instruction="Perform a data audit on past leave for Amelia Garcia (E10003) and Rahul Singh (E10004), effective 2025-07-01. For Amelia, her parental leave (LV6001) is complete but still marked 'Scheduled'; update its status to 'Taken'. Then, process a 5% salary increase for her and log a performance review with the summary 'Completed leave and performance cycle.' For Rahul, issue him a one-time bonus of $1,500 with the reason 'Data audit completion bonus.' since his vacation (LV6002) is already correctly marked as 'Taken'. To fund these changes, transfer $10,000 from the Sales department's budget (DEPT1002) to the Marketing department's (DEPT1005). For verification, retrieve the updated employee records for both employees and the updated department record for Marketing.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
            Action(
                name="update_leave_record",
                kwargs={"leave_id": "LV6001", "updates": {"status": "Taken"}},
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-07-01",
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Completed leave and performance cycle.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"compensation_id": "COMP10000", "performance_review_ids": ["PR5003", "PR5010", "PR10000"]},
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(name="get_unused_bonus_id", kwargs={}),
            Action(
                name="add_bonus_payment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10004",
                        "amount": 1500,
                        "reason": "Data audit completion bonus.",
                    }
                },
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1002"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1005"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4990000}},
            ),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1005", "updates": {"budget": 1610000}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1005"}),
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
        instruction="Process a promotion for Rahul Singh (E10004) to Senior Front-end Engineer (POS3006), which is a level L.3 role, effective 2026-04-01. This promotion includes a 15% base salary increase, creating a new compensation record. Log a performance review with the summary 'Promoted to Senior Front-end Engineer (L.3).' to document the change. For verification, retrieve his updated employee record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10004"}),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {"level_id": "L.3", "position_id": "POS3006"},
                },
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="set_compensation",
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
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
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
                name="update_employee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5004", "PR5009", "PR10000"],
                    },
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
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
                    "hire_date": "2022-02-14",
                    "termination_date": null,
                    "status": "Active",
                    "position_id": "POS3006",
                    "department_id": "DEPT1001",
                    "level_id": "L.3",
                    "manager_id": "E10003",
                    "work_location": "Remote – Bangalore",
                    "work_email": "rahul.singh@example.com",
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
        instruction="Perform a compensation audit for Daniel Kim (E10002), effective 2025-07-15. Check if his base salary is below $140,000 (target: $145,000) or if his bonus target is below 15% (target: 17%). Log a performance review to document that the audit was performed. For verification, retrieve his full list of performance reviews.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10002"}),
            Action(
                name="conditional_compensation_check_and_update",
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
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
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
                name="update_employee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"performance_review_ids": ["PR5002", "PR10000"]},
                },
            ),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10002"}),
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
        instruction="Process and approve a 6-week medical leave for Rahul Singh (E10004) from 2025-08-01 to 2025-09-12, and upload his 'Medical Certificate' dated 2025-07-24. Appoint Daniel Kim (E10002) as acting project lead during the leave and log a review for him with the summary 'Acting project lead during R. Singh's leave.' To fund this, transfer $15,000 from the Engineering department's budget (DEPT1001) to the Sales department's (DEPT1002). For verification, retrieve the updated records for both departments.",
        actions=[
            Action(name="get_unused_leave_id", kwargs={}),
            Action(
                name="request_leave",
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
                name="update_leave_status",
                kwargs={"leave_id": "LV10000", "status": "Approved"},
            ),
            Action(name="get_unused_document_id", kwargs={}),
            Action(
                name="add_employee_document",
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
            Action(name="list_employee_documents", kwargs={"employee_id": "E10004"}),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10002", "updates": {"role_description": "Acting project lead"}},
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
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
                name="update_employee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"performance_review_ids": ["PR5002", "PR10000"]},
                },
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1002"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 6985000}},
            ),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 5015000}},
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1002"}),
        ],
        outputs=[
            """
            [
                {
                    "department_id": "DEPT1001",
                    "name": "Engineering",
                    "head_id": "E10001",
                    "location": "San Francisco HQ",
                    "budget": 6985000,
                    "description": "Responsible for all product development and technical operations."
                },
                {
                    "department_id": "DEPT1002",
                    "name": "Sales",
                    "head_id": "E10012",
                    "location": "New York Office",
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
        instruction="Effective 2025-09-01, process an internal transfer for Elena Rodriguez (E10005) to the Marketing department (DEPT1005) under her new manager, Marcus Chen (E10006). This transfer includes a salary increase to €78,000. Log a performance review with the summary 'Internal transfer and salary adjustment.' To fund this, increase the Marketing budget by €10,000. For verification, retrieve her updated employee record and the Marketing department record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10005"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10005"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10005", "updates": {"department_id": "DEPT1005", "manager_id": "E10006"}},
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="set_compensation",
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
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10005",
                        "summary": "Internal transfer and salary adjustment",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR10000"],
                    },
                },
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1005"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1005", "updates": {"budget": 1610000}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10005"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1005"}),
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
        instruction="Initiate a 60-day Performance Improvement Plan (PIP) for Rahul Singh (E10004), starting 2025-10-01, with the summary 'PIP Initiated.' and a 'Needs Improvement' rating. Upload his signed 'PIP Agreement' document. Per policy, create a new compensation record to set his bonus target to 0%. To fund the PIP process, transfer $10,000 from the Sales department's budget (DEPT1002) to Engineering (DEPT1001). For verification, retrieve the updated records for Rahul and the Engineering department.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10004"}),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
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
            Action(name="get_unused_document_id", kwargs={}),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10004",
                        "title": "PIP Agreement",
                        "date": "2025-10-01",
                    }
                },
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="set_compensation",
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
                name="update_employee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5004", "PR5009", "PR10000"],
                    },
                },
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1002"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4990000}},
            ),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7010000}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
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
        instruction="Perform a benefit audit for Marcus Chen (E10006), effective 2025-07-24. Enroll him in the Legal Insurance plan (BEN9999) and ensure he is enrolled in the 401(k) plan (BEN4003). Update his role description to 'Senior Product Manager, Finance Liaison'. Log a performance review with the summary 'Benefit audit completed.' As a reward for the successful audit, issue a one-time bonus of $1,000 to his manager, Sophia Nguyen (E10001), for 'Managerial oversight.' To fund this, increase the Engineering department's (DEPT1001) budget by $1,000. For verification, retrieve the updated employee records for both Marcus and Sophia, and the updated Engineering department record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10006"}),
            Action(
                name="add_employee_benefits_conditionally",
                kwargs={
                    "employee_id": "E10006",
                    "benefit_plan_ids": ["BEN4003", "BEN9999"],
                },
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10006", "updates": {"role_description": "Senior Product Manager, Finance Liaison"}},
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10006",
                        "summary": "Benefit audit completed.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {"performance_review_ids": ["PR5011", "PR10000"]},
                },
            ),
            Action(name="get_unused_bonus_id", kwargs={}),
            Action(
                name="add_bonus_payment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10001",
                        "amount": 1000,
                        "reason": "Managerial oversight.",
                    }
                },
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7001000}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10006"}),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
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
        instruction="Process the voluntary termination for Elena Rodriguez (E10005), effective 2025-12-15. As part of her exit package, she is to receive a pro-rated performance bonus (ID BON1001) of €2,500 with the reason 'Pro-rated bonus.'. Her benefits should be updated: cancel all current plans but enroll her in the vested Legal Insurance plan (BEN9999). Log a final performance review (ID PR5024) with a 'Meets' rating and the summary 'Voluntary termination.' to document the event. For verification, retrieve her updated employee record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10005"}),
            Action(
                name="terminate_employee",
                kwargs={"employee_id": "E10005", "termination_date": "2025-12-15"},
            ),
            Action(
                name="add_bonus_payment",
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
                name="set_employee_benefits",
                kwargs={"employee_id": "E10005", "benefit_plan_ids": ["BEN9999"]},
            ),
            Action(
                name="add_performance_review",
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
                name="update_employee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {"performance_review_ids": ["PR5024"]},
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10005"}),
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
                    "nationality": "ES",
                    "marital_status": "Single",
                    "hire_date": "2024-09-01",
                    "termination_date": "2025-12-15",
                    "status": "Terminated",
                    "position_id": "POS3010",
                    "department_id": "DEPT1004",
                    "level_id": "L.1",
                    "manager_id": "E10011",
                    "work_location": "Madrid Office",
                    "work_email": "elena.rodriguez@example.com",
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
                    "notes": "Recent graduate—IE Business School."
                }
            ]
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_32",
        instruction="Onboard a new Senior Backend Engineer, Sarah Johnson, effective 2025-08-15, into the Engineering department (DEPT1001). Her compensation is a $145,000 salary, 15% bonus, and $25,000 equity grant. Upon starting, Sarah will become the new manager for Rahul Singh (E10004). Log a performance review for Rahul with the summary 'Manager updated.' To fund the new role, transfer $175,000 from the Sales budget (DEPT1002) to Engineering. For verification, retrieve the updated records for both employees and the Engineering department.",
        actions=[
            Action(name="get_unused_employee_id", kwargs={}),
            Action(
                name="create_employee",
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
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="set_compensation",
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
                name="update_employee",
                kwargs={
                    "employee_id": "E10000",
                    "updates": {"compensation_id": "COMP10000"},
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10004", "updates": {"manager_id": "E10000"}},
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "summary": "Manager updated",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {"performance_review_ids": ["PR5004", "PR5009", "PR10000"]},
                },
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1002"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4825000}},
            ),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7175000}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10000"}),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
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
        instruction="A new initiative, 'Project Titan,' is being launched, effective 2025-11-01. First, promote Amelia Garcia (E10003) to 'Lead Engineer, Project Titan' (POS4001), a level L.5 role. This includes a 12% salary increase and an additional $30,000 equity grant. To document this, create a new compensation record and log a performance review with the summary 'Promotion to Lead Engineer, Project Titan.' Next, transfer Rahul Singh (E10004) to backfill Amelia's previous role (POS3006) in the Marketing department (DEPT1005). To fund the project, decrease the Marketing department's budget by $250,000 and increase the Engineering department's (DEPT1001) budget by the same amount. Also, prepend 'HIRING FREEZE: Q4 2025.' to the Marketing department's description. For verification, retrieve the updated employee records for both Amelia Garcia and Rahul Singh, and the updated department record for Engineering.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10003", "updates": {"position_id": "POS4001", "level_id": "L.5", "role_description": "Lead Engineer, Project Titan"}},
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="set_compensation",
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
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Lead Engineer, Project Titan.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5003", "PR5010", "PR10000"],
                    },
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10004", "updates": {"position_id": "POS3006", "department_id": "DEPT1005"}},
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1005"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1005", "updates": {"budget": 1350000, "description": "HIRING FREEZE: Q4 2025. Drives brand awareness and demand generation."}},
            ),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7250000}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
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
        instruction="Extend Amelia Garcia's (E10003) parental leave (LV6001) to 2025-03-01 and upload her 'Medical Certificate' with the date of 2025-07-01. Log a review for her with the summary 'Parental leave extended.' To recognize Daniel Kim (E10002) for covering her duties, appoint him as 'Acting Team Lead' by updating his role description and issue him a one-time bonus of $1,500 with the reason 'Leave coverage bonus.' For verification, retrieve both updated employee records.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(
                name="update_leave_record",
                kwargs={"leave_id": "LV6001", "updates": {"end_date": "2025-03-01"}},
            ),
            Action(name="get_unused_document_id", kwargs={}),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10003",
                        "title": "Medical Certificate",
                        "date": "2025-07-01",
                    }
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Parental leave extended.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"performance_review_ids": ["PR5003", "PR5010", "PR10000"]},
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10002", "updates": {"role_description": "Acting Team Lead"}},
            ),
            Action(name="get_unused_bonus_id", kwargs={}),
            Action(
                name="add_bonus_payment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10002",
                        "amount": 1500,
                        "reason": "Leave coverage bonus",
                    }
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
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
        instruction="Effective 2025-10-15, process the promotion of Marcus Chen (E10006) to Director (level L.5) with a new base salary of €85,000 and an 18% bonus target. As part of this change, make him the new head of the Finance department (DEPT1004). To fund this, transfer €150,000 from the Marketing department's budget (DEPT1005) to Finance. Finally, log a single performance review for Marcus with the summary 'Promotion to Director and Head of Finance.' For verification, retrieve the updated records for Marcus Chen and both affected departments.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10006"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10006"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10006", "updates": {"level_id": "L.5", "role_description": "Director", "position_id": None}},
            ),
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="set_compensation",
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
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10006",
                        "summary": "Promotion to Director and Head of Finance",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": ["PR5011", "PR10000"],
                    },
                },
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1005"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1004"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1005", "updates": {"budget": 1450000}},
            ),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1004", "updates": {"budget": 1350000, "head_id": "E10006"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10006"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1005"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1004"}),
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
        instruction="Effective 2025-09-01, process the re-hire of a former employee, Andrian Roberts (E99999), as a 'Senior Backend Engineer' (POS3009) at level L.3 in the Engineering department (DEPT1001). His new compensation is a $130,000 base salary and 15% bonus target; set his benefits to the standard package (BEN4001, BEN4002, BEN4003) and upload his 'Re-hire Packet' document. Upon starting, Andrian will become the new manager for Daniel Kim (E10002). Consequently, promote Daniel to 'Senior Analyst' (POS3012), give him a 5% salary increase, and log a performance review with the summary 'Promotion to Senior Analyst'. To fund these changes, transfer $150,000 from the Sales department budget (DEPT1002) to the Engineering department's (DEPT1001). For verification, retrieve the updated employee records for both Andrian and Daniel, and the updated department record for Engineering.",
        actions=[
            Action(
                name="update_employee",
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
            Action(name="get_unused_compensation_id", kwargs={}),
            Action(
                name="set_compensation",
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
                name="set_employee_benefits",
                kwargs={"employee_id": "E99999", "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003"]},
            ),
            Action(name="get_unused_document_id", kwargs={}),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E99999",
                        "title": "Re-hire Packet",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E99999", "updates": {"compensation_id": "COMP10000"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10002"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10002", "updates": {"manager_id": "E99999", "position_id": "POS3012"}},
            ),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10002",
                    "compensation_id": "COMP2002",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-09-01",
                },
            ),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Promotion to Senior Analyst",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10002", "updates": {"performance_review_ids": ["PR5002", "PR10000"]}},
            ),
            Action(name="get_department", kwargs={"department_id": "DEPT1002"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1002", "updates": {"budget": 4850000}},
            ),
            Action(
                name="update_department",
                kwargs={"department_id": "DEPT1001", "updates": {"budget": 7150000}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E99999"}),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
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
        instruction="Approve the request for Rahul Singh (E10004) to work permanently from his current remote location in Bangalore, effective 2025-12-01. Update his work location to the standardized format 'Remote - Bangalore' and upload his 'Remote Work Agreement' document. Also log a performance review note with the summary 'Permanent remote work approved.' to document the change. For verification, retrieve his updated employee record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {"work_location": "Remote - Bangalore"},
                },
            ),
            Action(name="get_unused_document_id", kwargs={}),
            Action(
                name="add_employee_document",
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
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
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
                name="update_employee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {
                        "performance_review_ids": ["PR5004", "PR5009", "PR10000"]
                    },
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
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
                    "hire_date": "2022-02-14",
                    "termination_date": null,
                    "status": "Active",
                    "position_id": "POS3007",
                    "department_id": "DEPT1001",
                    "level_id": "L.2",
                    "manager_id": "E10003",
                    "work_location": "Remote - Bangalore",
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
        instruction="Process the annual performance review for Amelia Garcia (E10003), effective 2025-07-24. Her performance rating is 'Exceeds'. This qualifies her for a one-time performance bonus of $8,500 with the reason 'Annual performance bonus.' and an 8% merit-based salary increase. Document these changes by creating a new performance review with the summary 'Annual review completed.'. For verification, retrieve her updated employee record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
            Action(name="get_unused_review_id", kwargs={}),
            Action(
                name="add_performance_review",
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
            Action(name="get_unused_bonus_id", kwargs={}),
            Action(
                name="add_bonus_payment",
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
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "salary_increase_pct": 8,
                    "compensation_id": "COMP2003",
                    "effective_date": "2025-07-24",
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"performance_review_ids": ["PR5003", "PR5010", "PR10000"]},
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
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
        instruction="Process an emergency family leave for Marcus Chen (E10006). The leave is for 2 weeks, starting retroactively from 2025-07-20 and ending 2025-08-03. Log and approve the request using leave ID LV8006. As the leave is currently active, update his employment status to 'On Leave'. Upload the 'Emergency Leave Request' form (doc ID E10006-001) with the title 'Emergency Leave Form'. Log a review note (ID PR5032) with the summary 'Emergency leave processed.' to document this. For verification, retrieve his updated employee record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10006"}),
            Action(
                name="request_leave",
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
                name="update_leave_status",
                kwargs={"leave_id": "LV8006", "status": "Approved"},
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10006", "updates": {"status": "On Leave"}},
            ),
            Action(
                name="add_employee_document",
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
                name="add_performance_review",
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
                name="update_employee",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {"performance_review_ids": ["PR5011", "PR5032"]},
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10006"}),
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
                    "status": "On Leave",
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
        instruction="Conduct a compensation audit for Daniel Kim (E10002), effective 2025-12-01. The audit checks his salary against a $150,000 floor (target: $152,000) and his bonus target against a 20% floor (target: 20%). The audit also includes an unconditional equity grant increase of $5,000. Create a new compensation record with ID COMP5008. Log a review note (ID PR5033) with the summary 'Compensation audit completed.' to document the audit's findings. For verification, retrieve his new, most recent compensation record.",
        actions=[
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(
                name="conditional_compensation_check_and_update",
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
                name="add_performance_review",
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
                name="update_employee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"performance_review_ids": ["PR5002", "PR5033"]},
                },
            ),
            Action(name="get_compensation", kwargs={"employee_id": "E10002"}),
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
