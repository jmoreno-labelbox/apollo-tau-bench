from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="res_01",
        instruction="Remove the Dental Plan (BEN4002) from Daniel Kim's benefits effective immediately and log the update.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Daniel", "last_name": "Kim"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(
                name="set_employee_benefits",
                kwargs={"employee_id": "E10002", "benefit_plan_ids": ["BEN4001"]},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
        ],
        outputs=["Dental Plan BEN4002 removed for Daniel Kim."],
    ),
    Task(
        annotator="0",
        user_id="res_02",
        instruction="Award Sophia Nguyen a $8,000 spot bonus and verify the payout record.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Sophia", "last_name": "Nguyen"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(
                name="add_bonus_payment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON_SophiaNguyen_8000",
                        "employee_id": "E10001",
                        "amount": 8000,
                        "currency": "USD"
                    }
                },
            ),
            Action(name="list_bonus_payments", kwargs={"employee_id": "E10001"}),
        ],
        outputs=["$8,000 spot bonus BON_SophiaNguyen_8000 recorded for Sophia Nguyen."],
    ),
    Task(
        annotator="0",
        user_id="res_03",
        instruction="Update the work location for Amelia Garcia (E10003) to 'Remote - Denver', effective 2025-07-24. Log a performance review note, PR5011, to document this change. For verification, retrieve her updated employee record.",
        actions=[
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"work_location": "Remote - Denver"},
                },
            ),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5011",
                        "employee_id": "E10003",
                        "period_start": "2025-07-24",
                        "period_end": "2025-07-24",
                        "rating": None,
                        "summary": "Work location updated to Remote - Denver.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "performance_review_ids": ["PR5003", "PR5010", "PR5011"]
                    },
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
                    "work_location": "Remote - Denver",
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
                        "PR5011"
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
        user_id="res_04",
        instruction="Log and approve a 10-day jury duty leave for Daniel Kim (E10002), from 2026-06-05 to 2026-06-14. For verification, retrieve his full list of leave records.",
        actions=[
            Action(
                name="request_leave",
                kwargs={
                    "leave": {
                        "leave_id": "LV5001",
                        "employee_id": "E10002",
                        "leave_type": "Jury Duty",
                        "start_date": "2026-06-05",
                        "end_date": "2026-06-14",
                        "status": "Pending",
                        "notes": "10-day jury duty leave.",
                    }
                },
            ),
            Action(
                name="update_leave_status",
                kwargs={"leave_id": "LV5001", "status": "Approved"},
            ),
            Action(name="list_leave_records", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            """
            {
              "count": 1,
              "results": [
                {
                  "leave_id": "LV5001",
                  "employee_id": "E10002",
                  "leave_type": "Jury Duty",
                  "start_date": "2026-06-05",
                  "end_date": "2026-06-14",
                  "status": "Approved",
                  "notes": "10-day jury duty leave."
                }
              ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_05",
        instruction="You want to promote Amelia Garcia from Senior Engineer (L.3) to Staff Engineer (L.4), increase her base salary by 10 %, and log the change.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Amelia", "last_name": "Garcia"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10003", "updates": {"level_id": "L.4"}},
            ),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP2003",  # reuse existing deterministic ID
                    "effective_date": "2024-07-01",  # same as current record
                    "salary_increase_pct": 10,
                },
            ),
            # Verify promotion and compensation update deterministically
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            "Amelia Garcia promoted to L.4 with 10% salary increase."
        ],
    ),
    Task(
        annotator="0",
        user_id="res_06",
        instruction="Grant Sophia Nguyen a $25,000 equity refresh effective 2025-09-01. Create compensation record COMP2008 and performance review PR5015 to log the change.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Sophia", "last_name": "Nguyen"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10001"}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10001",
                    "compensation_id": "COMP2008",
                    "effective_date": "2025-09-01",
                    "equity_increase_amount": 25000,
                },
            ),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5015",
                        "employee_id": "E10001",
                        "period_start": "2025-09-01",
                        "period_end": "2025-09-01"
                    }
                },
            ),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            "Sophia Nguyen equity refresh recorded in compensation COMP2008 and review PR5015."
        ],
    ),
    Task(
        annotator="0",
        user_id="res_07",
        instruction="Rehire Daniel Kim (E10002) effective 2025-10-01 as Financial Analyst (position POS3010) in Finance (DEPT1004) under manager E10011. Create compensation record COMP2009 (base 120000 USD, bonus 10%) and performance review PR5016 to log the event.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Daniel", "last_name": "Kim"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "status": "Active",
                        "hire_date": "2025-10-01",
                        "termination_date": "",
                        "department_id": "DEPT1004",
                        "manager_id": "E10011",
                        "position_id": "POS3010"
                    },
                },
            ),
            Action(
                name="set_compensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP2009",
                        "employee_id": "E10002",
                        "base_salary": 120000,
                        "currency": "USD",
                        "bonus_target_pct": 10,
                        "equity_grant": 0,
                        "effective_date": "2025-10-01",
                    }
                },
            ),
            Action(
                name="set_employee_benefits",
                kwargs={
                    "employee_id": "E10002",
                    "benefit_plan_ids": ["BEN4001", "BEN4002"],
                },
            ),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5016",
                        "employee_id": "E10002",
                        "period_start": "2025-10-01",
                        "period_end": "2025-10-01"
                    }
                },
            ),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            "Daniel Kim rehired with compensation COMP2009; review PR5016 recorded."
        ],
    ),
    Task(
        annotator="0",
        user_id="res_08",
        instruction="Transfer Amelia Garcia (E10003) to Engineering (DEPT1001); manager remains Sophia Nguyen (E10001). Log the transfer in review PR5017.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Amelia", "last_name": "Garcia"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1001"}),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"department_id": "DEPT1001"},
                },
            ),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5017",
                        "employee_id": "E10003",
                        "period_start": "2025-10-15",
                        "period_end": "2025-10-15"
                    }
                },
            ),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            "Amelia Garcia transferred to DEPT1001; review PR5017 logged."
        ],
    ),
    Task(
        annotator="0",
        user_id="res_09",
        instruction="Enroll Sophia Nguyen (E10001) in Vision Plan BEN4006 effective immediately. Create benefit plan BEN4006 (name 'Vision Plan') and performance review PR5018 to log the benefit change.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Sophia", "last_name": "Nguyen"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(
                name="add_benefit_plan",
                kwargs={
                    "benefit_plan": {
                        "benefit_plan_id": "BEN4006",
                        "name": "Vision Plan"
                    }
                },
            ),
            Action(
                name="set_employee_benefits",
                kwargs={
                    "employee_id": "E10001",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003", "BEN4006"],
                },
            ),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5018",
                        "employee_id": "E10001",
                        "period_start": "2025-07-28",
                        "period_end": "2025-07-28"
                    }
                },
            ),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            "Vision Plan BEN4006 added for Sophia Nguyen; review PR5018 logged."
        ],
    ),
    Task(
        annotator="0",
        user_id="res_10",
        instruction="Approve a one-month unpaid sabbatical for Amelia Garcia starting 2025-11-01 and update her status.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Amelia", "last_name": "Garcia"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(
                name="add_leave_record",
                kwargs={
                    "leave": {
                        "leave_id": "LV6102",
                        "employee_id": "E10003",
                        "leave_type": "Sabbatical",
                        "start_date": "2025-11-01",
                        "end_date": "2025-11-30",
                        "status": "Approved",
                        "notes": "One-month unpaid sabbatical approved.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10003", "updates": {"status": "On Leave"}},
            ),
            Action(name="list_leave_records", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            "Unpaid sabbatical LV6102 approved for Amelia Garcia; status set to 'On Leave.'"
        ],
    ),
    Task(
        annotator="0",
        user_id="res_11",
        instruction="Record a Performance Improvement Plan for Daniel Kim: review PR5019 covering 2025-11-01 to 2025-11-30 with rating 'Needs Improvement'.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Daniel", "last_name": "Kim"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5019",
                        "employee_id": "E10002",
                        "period_start": "2025-11-01",
                        "period_end": "2025-11-30",
                        "rating": "Needs Improvement"
                    }
                },
            ),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10002"}),
        ],
        outputs=["Performance Improvement Plan PR5019 recorded for Daniel Kim."],
    ),
    Task(
        annotator="0",
        user_id="res_12",
        instruction="Set Sophia Nguyen's work location to Remote – Seattle.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Sophia", "last_name": "Nguyen"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"work_location": "Remote - Seattle"},
                },
            ),

        ],
        outputs=["Sophia Nguyen work location set to Remote - Seattle."],
    ),
    Task(
        annotator="0",
        user_id="res_13",
        instruction="Perform a data audit on past leave for Amelia Garcia (E10003). Her parental leave (LV6001) is complete but is still marked as 'Scheduled'. Update the leave record's status to 'Taken' to correctly reflect its completion. Confirm her main employment status is 'Active'. For verification, retrieve her updated leave schedule.",
        actions=[
            Action(
                name="update_leave_record",
                kwargs={"leave_id": "LV6001", "updates": {"status": "Taken"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="list_leave_records", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            """
            {
              "count": 1,
              "results": [
                {
                  "leave_id": "LV6001",
                  "employee_id": "E10003",
                  "leave_type": "Parental",
                  "start_date": "2024-11-01",
                  "end_date": "2025-02-01",
                  "status": "Taken"
                }
              ]
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="res_14",
        instruction="Record holiday bonus BON3004 of USD 4,000 for Amelia Garcia dated 2026-12-15.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Amelia", "last_name": "Garcia"}},
            ),
            Action(
                name="add_bonus_payment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON3004",
                        "employee_id": "E10003",
                        "amount": 4000,
                        "currency": "USD",
                        "payment_date": "2026-12-15"
                    }
                },
            ),
            Action(name="list_bonus_payments", kwargs={"employee_id": "E10003"}),
        ],
        outputs=["Holiday bonus BON3004 of $4,000 recorded for Amelia Garcia."],
    ),
    Task(
        annotator="0",
        user_id="res_15",
        instruction="Store education document ED7005 (Executive MBA enrollment dated 2026-07-05) for Sophia Nguyen.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Sophia", "last_name": "Nguyen"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "ED7005",
                        "employee_id": "E10001",
                        "doc_type": "Education",
                        "title": "Executive MBA Enrollment",
                        "date": "2026-07-05"
                    }
                },
            ),
            Action(name="list_employee_documents", kwargs={"employee_id": "E10001"}),
        ],
        outputs=["Document ED7005 stored for Sophia Nguyen."],
    ),
    Task(
        annotator="0",
        user_id="res_16",
        instruction="Promote Daniel Kim to Lead Analyst (level L.3), raise his base salary by 10 % effective 2026-09-01, and log the change.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Daniel", "last_name": "Kim"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10002"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10002", "updates": {"level_id": "L.3"}},
            ),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10002",
                    "compensation_id": "COMP2015",
                    "effective_date": "2026-09-01",
                    "salary_increase_pct": 10
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
        ],
        outputs=["Daniel Kim promoted to L.3 with 10% salary increase (compensation COMP2015)."],
    ),
    Task(
        annotator="0",
        user_id="res_17",
        instruction="Enroll Amelia Garcia in the Vision Plan (BEN4006) effective immediately and log the benefit change.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Amelia", "last_name": "Garcia"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(
                name="set_employee_benefits",
                kwargs={
                    "employee_id": "E10003",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4004", "BEN4006"],
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
        ],
        outputs=["Vision Plan BEN4006 added for Amelia Garcia."],
    ),
    Task(
        annotator="0",
        user_id="res_18",
        instruction="Increase Sophia Nguyen's equity grant by $15,000 effective 2026-08-10 and log the change.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Sophia", "last_name": "Nguyen"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10001"}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10001",
                    "compensation_id": "COMP2016",
                    "effective_date": "2026-08-10",
                    "equity_increase_amount": 15000
                },
            ),
            Action(name="get_compensation", kwargs={"employee_id": "E10001"}),
        ],
        outputs=["Sophia Nguyen equity grant increased by $15,000 (compensation COMP2016)."],
    ),
    Task(
        annotator="0",
        user_id="res_19",
        instruction="Change Daniel Kim's work location to the San Diego Office and log the update.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Daniel", "last_name": "Kim"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"work_location": "San Diego Office"},
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
        ],
        outputs=["Daniel Kim work location updated to San Diego Office."],
    ),
    Task(
        annotator="0",
        user_id="res_20",
        instruction="Record spot bonus BON3005 of USD 6,000 for Sophia Nguyen dated 2026-09-30.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Sophia", "last_name": "Nguyen"}},
            ),
            Action(
                name="add_bonus_payment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON3005",
                        "employee_id": "E10001",
                        "amount": 6000,
                        "currency": "USD",
                        "payment_date": "2026-09-30"
                    }
                },
            ),
            Action(name="list_bonus_payments", kwargs={"employee_id": "E10001"}),
        ],
        outputs=["$6,000 spot bonus BON3005 recorded for Sophia Nguyen."],
    ),
    Task(
        annotator="0",
        user_id="res_21",
        instruction="Record approved volunteer leave LV6106 from 2026-09-15 to 2026-09-19 for Daniel Kim and set his status to 'On Leave'.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Daniel", "last_name": "Kim"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(
                name="add_leave_record",
                kwargs={
                    "leave": {
                        "leave_id": "LV6106",
                        "employee_id": "E10002",
                        "leave_type": "Volunteer Leave",
                        "start_date": "2026-09-15",
                        "end_date": "2026-09-19",
                        "status": "Approved"
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10002", "updates": {"status": "On Leave"}},
            ),
            Action(name="list_leave_records", kwargs={"employee_id": "E10002"}),
        ],
        outputs=["Volunteer leave LV6106 recorded; Daniel Kim status set to 'On Leave'."],
    ),
    Task(
        annotator="0",
        user_id="res_22",
        instruction="Increase Daniel Kim's equity grant by $10,000 via compensation record COMP5003 effective 2026-01-15 and display updated compensation history.",
        actions=[
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10002",
                    "compensation_id": "COMP5003",
                    "effective_date": "2026-01-15",
                    "equity_increase_amount": 10000,
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"performance_review_ids": ["PR5002", "PR8003"]},
                },
            ),
            Action(name="get_compensation", kwargs={"employee_id": "E10002"}),
        ],
        outputs=["Compensation history includes new record COMP5003 with +$10,000 equity."],
    ),
    Task(
        annotator="0",
        user_id="res_23",
        instruction="Store certification document ED7006 (AWS Solutions Architect, 2026-09-22) for Amelia Garcia.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Amelia", "last_name": "Garcia"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "ED7006",
                        "employee_id": "E10003",
                        "doc_type": "Certification",
                        "title": "AWS Solutions Architect",
                        "date": "2026-09-22"
                    }
                },
            ),
            Action(name="list_employee_documents", kwargs={"employee_id": "E10003"}),
        ],
        outputs=["Document ED7006 stored for Amelia Garcia."],
    ),
    Task(
        annotator="0",
        user_id="res_24",
        instruction="Create compensation record COMP2017 for Daniel Kim with bonus target 17 % effective 2026-10-01.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Daniel", "last_name": "Kim"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10002"}),
            Action(
                name="set_compensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP2017",
                        "employee_id": "E10002",
                        "base_salary": 210000,
                        "currency": "USD",
                        "bonus_target_pct": 17,
                        "equity_grant": 40000,
                        "effective_date": "2026-10-01"
                    }
                },
            ),
            Action(name="get_compensation", kwargs={"employee_id": "E10002"}),
        ],
        outputs=["Daniel Kim bonus target set to 17 % (compensation COMP2017)."],
    ),
    Task(
        annotator="0",
        user_id="res_25",
        instruction="Record Q2-2026 performance review PR5050 (rating 'Exceeds') for Amelia Garcia.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Amelia", "last_name": "Garcia"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5050",
                        "employee_id": "E10003",
                        "period_start": "2026-04-01",
                        "period_end": "2026-06-30",
                        "rating": "Exceeds",
                        "manager_id": "E10001"
                    }
                },
            ),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10003"}),
        ],
        outputs=["Q2 2026 review PR5050 recorded for Amelia Garcia."],
    ),
    Task(
        annotator="0",
        user_id="res_26",
        instruction="If Elena Rodriguez's salary is below 75,000 EUR or bonus target below 8 %, apply compensation record COMP2018 (salary 78 000 EUR, bonus 10 %) effective 2025-07-15 and show updated compensation.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Elena", "last_name": "Rodriguez"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10005"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10005"}),
            Action(
                name="conditional_compensation_check_and_update",
                kwargs={
                    "employee_id": "E10005",
                    "compensation_id": "COMP2018",
                    "effective_date": "2025-07-15",
                    "salary_threshold": 75000,
                    "target_salary": 78000,
                    "bonus_threshold": 8,
                    "target_bonus": 10,
                },
            ),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10005"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10005"}),
        ],
        outputs=["Compensation updated for Elena Rodriguez if thresholds met (see COMP2018)."],
    ),
    Task(
        annotator="0",
        user_id="res_27",
        instruction="Approve Marcus Chen's sabbatical LV6107 from 2025-08-01 to 2025-08-21, approve any pending leaves, set status 'On Leave', and store approval doc ED7007.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Marcus", "last_name": "Chen"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10006"}),
            Action(name="list_leave_records", kwargs={"employee_id": "E10006"}),
            Action(
                name="update_leave_records_by_status",
                kwargs={
                    "employee_id": "E10006",
                    "current_status": "Pending",
                    "new_status": "Approved"
                },
            ),
            Action(
                name="add_leave_record",
                kwargs={
                    "leave": {
                        "leave_id": "LV6107",
                        "employee_id": "E10006",
                        "leave_type": "Sabbatical",
                        "start_date": "2025-08-01",
                        "end_date": "2025-08-21",
                        "status": "Approved"
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10006", "updates": {"status": "On Leave"}},
            ),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "ED7007",
                        "employee_id": "E10006",
                        "doc_type": "Leave",
                        "title": "Sabbatical Approval",
                        "date": "2025-07-20"
                    }
                },
            ),
            Action(name="list_employee_documents", kwargs={"employee_id": "E10006"}),
            Action(name="list_leave_records", kwargs={"employee_id": "E10006"}),
        ],
        outputs=["Marcus Chen sabbatical LV6107 recorded; status On Leave; doc ED7007 stored."],
    ),
    Task(
        annotator="0",
        user_id="res_28",
        instruction="Transfer Rahul Singh to Finance (DEPT1004) under manager E10011; if latest rating is 'Exceeds', update level to L.3; add benefit BEN4005.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Rahul", "last_name": "Singh"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10004"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1004"}),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {"department_id": "DEPT1004", "manager_id": "E10011"},
                },
            ),
            Action(
                name="conditional_level_update",
                kwargs={
                    "employee_id": "E10004",
                    "required_rating": "Exceeds",
                    "new_level": "L.3",
                },
            ),
            Action(
                name="set_employee_benefits",
                kwargs={
                    "employee_id": "E10004",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4005"],
                },
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10004"}),
        ],
        outputs=["Rahul Singh transferred to Finance; level updated if eligible; benefit BEN4005 added."],
    ),
    Task(
        annotator="0",
        user_id="res_29",
        instruction="Record Q2-2025 review PR5053 (rating 'Exceeds') for Amelia Garcia; if bonus target <18 %, set to 20 % via COMP2019 and grant $5 500 bonus BON3006.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Amelia", "last_name": "Garcia"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5053",
                        "employee_id": "E10003",
                        "period_start": "2025-04-01",
                        "period_end": "2025-06-30",
                        "rating": "Exceeds",
                        "manager_id": "E10001",
                        "summary": "Outstanding Q2 performance with significant contributions to platform improvements.",
                    }
                },
            ),
            Action(
                name="conditional_compensation_increase",
                kwargs={
                    "employee_id": "E10003",
                    "compensation_id": "COMP2019",
                    "effective_date": "2025-07-25",
                    "condition": "bonus_target_pct < 18",
                    "new_bonus_target_pct": 20,
                },
            ),
            Action(
                name="add_bonus_payment",
                kwargs={
                    "bonus": {
                        "bonus_id": "BON3006",
                        "employee_id": "E10003",
                        "amount": 5500,
                        "currency": "USD",
                        "payment_date": "2025-07-25",
                        "reason": "Q2 2025 performance bonus for exceeding targets.",
                    }
                },
            ),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10003"}),
            Action(name="list_bonus_payments", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
        ],
        outputs=["PR5053 recorded; bonus target conditionally set to 20 %; bonus BON3006 awarded."],
    ),
    Task(
        annotator="0",
        user_id="res_30",
        instruction="Re-activate Daniel Kim's status to Active, ensure benefits include BEN4006, store medical clearance ED7008, and confirm compensation current.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Daniel", "last_name": "Kim"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="list_leave_records", kwargs={"employee_id": "E10002"}),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10002", "updates": {"status": "Active"}},
            ),
            Action(
                name="set_employee_benefits",
                kwargs={
                    "employee_id": "E10002",
                    "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003", "BEN4006"],
                },
            ),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "ED7008",
                        "employee_id": "E10002",
                        "doc_type": "Medical",
                        "title": "Return to Work Clearance",
                        "date": "2025-07-30",
                        "notes": "Medical clearance for return to active duty after leave period.",
                    }
                },
            ),
            Action(name="get_compensation", kwargs={"employee_id": "E10002"}),
            Action(name="list_employee_documents", kwargs={"employee_id": "E10002"}),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
        ],
        outputs=["Daniel Kim onboarding complete: status Active, benefits restored, medical doc ED7008 stored."],
    ),
    Task(
        annotator="0",
        user_id="res_31",
        instruction="Promote Elena Rodriguez to Senior Financial Analyst (L.2), increase her base salary by 15% effective 2025-08-01, grant her 5,000 EUR in equity, and if she's not enrolled in the 401(k) plan, add it to her benefits. Document the promotion.",
        actions=[
            Action(name="search_employees", kwargs={"filters": {"first_name": "Elena", "last_name": "Rodriguez"}}),
            Action(name="get_employee", kwargs={"employee_id": "E10005"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10005"}),
            Action(name="update_employee", kwargs={"employee_id": "E10005", "updates": {"level_id": "L.2"}}),
            Action(
                name="set_compensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP2005",
                        "employee_id": "E10005",
                        "base_salary": 135700,
                        "currency": "USD",
                        "bonus_target_pct": 10,
                        "equity_grant": 5000,
                        "effective_date": "2025-08-01"
                    }
                },
            ),
            Action(name="add_employee_benefit_if_missing", kwargs={"employee_id": "E10005", "benefit_plan_id": "BEN4003", "current_benefit_plan_ids": ["BEN4001", "BEN4005"]}),
            Action(name="get_employee", kwargs={"employee_id": "E10005"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10005"}),
        ],
        outputs=["Elena Rodriguez promoted, compensation COMP20250801 added, 401(k) benefit ensured."],
    ),
    Task(
        annotator="0",
        user_id="res_32",
        instruction="Process Sophia Nguyen's request for 4 weeks of unpaid personal leave (LV6108) from 2025-09-01 to 2025-09-28. If her current equity grant is above 70,000, maintain her benefits during leave. Set status appropriately and upload leave documentation.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Sophia", "last_name": "Nguyen"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10001"}),
            Action(name="list_leave_records", kwargs={"employee_id": "E10001"}),
            Action(
                name="conditional_benefit_maintenance",
                kwargs={
                    "employee_id": "E10001",
                    "equity_threshold": 70000,
                    "maintain_benefits": ["BEN4001", "BEN4002", "BEN4003", "BEN4006"],
                    "reduced_benefits": ["BEN4001"],
                },
            ),
            Action(
                name="add_leave_record",
                kwargs={
                    "leave": {
                        "leave_id": "LV6108",
                        "employee_id": "E10001",
                        "leave_type": "Personal Leave",
                        "start_date": "2025-09-01",
                        "end_date": "2025-09-28",
                        "status": "Approved",
                        "notes": "4-week unpaid personal leave with conditional benefit maintenance based on equity level.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={"employee_id": "E10001", "updates": {"status": "On Leave"}},
            ),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "ED7009",
                        "employee_id": "E10001",
                        "doc_type": "Leave",
                        "title": "Personal Leave Authorization",
                        "date": "2025-08-15"
                    }
                },
            ),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5056",
                        "employee_id": "E10001",
                        "period_start": "2025-09-01",
                        "period_end": "2025-09-28",
                        "rating": "N/A",
                        "manager_id": "N/A",
                        "summary": "Personal leave approved with conditional benefit maintenance based on equity level analysis.",
                    }
                },
            ),
            Action(name="list_employee_documents", kwargs={"employee_id": "E10001"}),
            Action(name="list_leave_records", kwargs={"employee_id": "E10001"}),
        ],
        outputs=["Personal leave LV6108 recorded for Sophia Nguyen; benefits adjusted per equity threshold; doc ED7009 stored."],
    ),
    Task(
        annotator="0",
        user_id="res_33",
        instruction="Begin termination process for Marcus Chen effective 2025-09-15. Calculate final compensation, remove active benefits except Legal Insurance, upload termination documentation, and if he has any pending leave, mark it as cancelled.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Marcus", "last_name": "Chen"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10006"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10006"}),
            Action(name="list_leave_records", kwargs={"employee_id": "E10006"}),
            Action(name="update_leave_records_by_status", kwargs={"employee_id": "E10006", "current_status": "Pending", "new_status": "Cancelled"}),
            Action(name="add_bonus_payment", kwargs={"bonus": {"bonus_id": "BON3010", "employee_id": "E10006", "amount": 2500, "currency": "EUR", "payment_date": "2025-09-15"}}),
            Action(
                name="terminate_employee",
                kwargs={"employee_id": "E10006", "termination_date": "2025-09-15"},
            ),
            Action(name="set_employee_benefits", kwargs={"employee_id": "E10006", "benefit_plan_ids": ["BEN9999"]}),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "ED7010",
                        "employee_id": "E10006",
                        "doc_type": "Termination",
                        "title": "Termination Notice",
                        "date": "2025-09-15",
                        "notes": "Voluntary termination with final compensation calculated and benefits transition completed.",
                    }
                },
            ),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5057",
                        "employee_id": "E10006",
                        "period_start": "2025-09-15",
                        "period_end": "2025-09-15",
                        "rating": "N/A",
                        "manager_id": "E10012",
                        "summary": "Termination processed with final compensation payout and benefit adjustments, pending leave cancelled.",
                    }
                },
            ),
            Action(name="list_employee_documents", kwargs={"employee_id": "E10006"}),
            Action(name="get_employee", kwargs={"employee_id": "E10006"}),
        ],
        outputs=["Marcus Chen termination processed; leave cancelled; bonus BON3010 paid; benefits set to Legal Insurance; doc ED7010 stored."],
    ),
    Task(
        annotator="0",
        user_id="res_34",
        instruction="Assign Rahul Singh to a 6-month cross-functional project with Marketing (temporary assignment). Check his current department, temporarily update his manager to E10013, add a project assignment review, and if his bonus target is below 12%, increase it to 15%.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Rahul", "last_name": "Singh"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10004"}),
            Action(name="get_department", kwargs={"department_id": "DEPT1005"}),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {
                        "manager_id": "E10013",
                        "notes": "Temporary assignment to Marketing cross-functional project for 6 months.",
                    },
                },
            ),
            Action(name="update_employee", kwargs={"employee_id": "E10004", "updates": {"manager_id": "E10013"}}),
            Action(
                name="conditional_compensation_increase",
                kwargs={
                    "employee_id": "E10004",
                    "compensation_id": "COMP2021",
                    "effective_date": "2025-08-01",
                    "condition": "bonus_target_pct < 12",
                    "new_bonus_target_pct": 15,
                },
            ),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5058",
                        "employee_id": "E10004",
                        "period_start": "2025-08-01",
                        "period_end": "2026-01-31",
                        "rating": "N/A",
                        "manager_id": "E10013",
                        "summary": "Assigned to 6-month cross-functional Marketing project with bonus target increased to 15%.",
                    }
                },
            ),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "ED7011",
                        "employee_id": "E10004",
                        "doc_type": "Assignment",
                        "title": "Cross-functional Project Assignment",
                        "date": "2025-08-01",
                        "notes": "6-month temporary assignment to Marketing department for strategic initiative.",
                    }
                },
            ),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10004"}),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
        ],
        outputs=["Rahul Singh assigned to Marketing project; bonus target adjusted via COMP2021; doc ED7011 stored."],
    ),
    Task(
        annotator="0",
        user_id="res_35",
        instruction="Approve Amelia Garcia's 2-month research sabbatical (LV6109) from 2025-10-01 to 2025-11-30. If her current level is L.3 or above, maintain full compensation during sabbatical. Upload sabbatical agreement and adjust status accordingly.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Amelia", "last_name": "Garcia"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10003"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10003"}),
            Action(name="list_leave_records", kwargs={"employee_id": "E10003"}),
            Action(
                name="conditional_sabbatical_compensation",
                kwargs={
                    "employee_id": "E10003",
                    "level_threshold": "L.3",
                    "paid_leave_type": "Research Sabbatical - Paid",
                    "unpaid_leave_type": "Research Sabbatical - Unpaid",
                },
            ),
            Action(
                name="add_leave_record",
                kwargs={
                    "leave": {
                        "leave_id": "LV6109",
                        "employee_id": "E10003",
                        "leave_type": "Research Sabbatical",
                        "start_date": "2025-10-01",
                        "end_date": "2025-11-30",
                        "status": "Approved",
                        "notes": "2-month research sabbatical with conditional compensation based on level L.3+ threshold.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"status": "On Sabbatical"},
                },
            ),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {
                        "doc_id": "ED7012",
                        "employee_id": "E10003",
                        "doc_type": "Agreement",
                        "title": "Research Sabbatical Agreement",
                        "date": "2025-09-15"
                    }
                },
            ),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5059",
                        "employee_id": "E10003",
                        "period_start": "2025-10-01",
                        "period_end": "2025-11-30",
                        "rating": "N/A",
                        "manager_id": "E10001",
                        "summary": "Research sabbatical approved with compensation maintenance.",
                    }
                },
            ),
            Action(name="list_employee_documents", kwargs={"employee_id": "E10003"}),
            Action(name="list_leave_records", kwargs={"employee_id": "E10003"}),
        ],
        outputs=["Amelia Garcia research sabbatical LV6109 recorded; compensation maintained; doc ED7012 stored."],
    ),
    Task(
        annotator="0",
        user_id="res_36",
        instruction="Implement a Performance Improvement Plan for Daniel Kim starting 2025-08-15. Create a 90-day PIP review, temporarily reduce his bonus target to 20%, upload PIP documentation, and schedule follow-up milestone reviews at 30 and 60 days.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Daniel", "last_name": "Kim"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10002"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10002"}),
            Action(
                name="set_compensation",
                kwargs={
                    "compensation": {
                        "compensation_id": "COMP2022",
                        "employee_id": "E10002",
                        "base_salary": 210000,
                        "currency": "USD",
                        "bonus_target_pct": 20,
                        "equity_grant": 40000,
                        "effective_date": "2025-08-15",
                    }
                },
            ),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5060",
                        "employee_id": "E10002",
                        "period_start": "2025-08-15",
                        "period_end": "2025-11-15",
                        "rating": "Needs Improvement"
                    }
                },
            ),
            Action(
                name="add_employee_document",
                kwargs={
                    "document": {"doc_id": "ED7013", "employee_id": "E10002", "doc_type": "PIP", "title": "Performance Improvement Plan", "date": "2025-08-15"}},
            ),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5061",
                        "employee_id": "E10002",
                        "period_start": "2025-09-15",
                        "period_end": "2025-09-15",
                        "rating": "Pending",
                        "manager_id": "E10012",
                        "summary": "30-day PIP milestone review - progress assessment scheduled.",
                    }
                },
            ),
            Action(
                name="add_performance_review",
                kwargs={
                    "review": {
                        "review_id": "PR5062",
                        "employee_id": "E10002",
                        "period_start": "2025-10-15",
                        "period_end": "2025-10-15",
                        "rating": "Pending",
                        "manager_id": "E10012",
                        "summary": "60-day PIP milestone review - mid-point evaluation scheduled.",
                    }
                },
            ),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10002"}),
            Action(name="list_employee_documents", kwargs={"employee_id": "E10002"}),
        ],
        outputs=["Daniel Kim PIP initiated; bonus target set to 20 %; doc ED7013 stored."],
    ),
    Task(
        annotator="0",
        user_id="res_37",
        instruction="Process Elena Rodriguez's relocation from Madrid to London Office effective 2025-09-01. Update her work location, check if she needs EU Commuter Stipend adjustment, add a $3,000 relocation bonus, and upload relocation documentation.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Elena", "last_name": "Rodriguez"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10005"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10005"}),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {"work_location": "London Office"},
                },
            ),
            Action(
                name="set_employee_benefits",
                kwargs={
                    "employee_id": "E10005",
                    "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4005"],
                },
            ),
            Action(name="add_bonus_payment", kwargs={"bonus": {"bonus_id": "BON3007", "employee_id": "E10005", "amount": 3000, "currency": "EUR", "payment_date": "2025-09-01"}}),
            Action(name="add_employee_document", kwargs={"document": {"doc_id": "ED7014", "employee_id": "E10005", "doc_type": "Relocation", "title": "Office Relocation Authorization", "date": "2025-08-20"}}),
            Action(name="list_bonus_payments", kwargs={"employee_id": "E10005"}),
            Action(name="get_employee", kwargs={"employee_id": "E10005"}),
        ],
        outputs=["Elena Rodriguez relocated to London Office; bonus BON3007 paid; doc ED7014 stored."],
    ),
    Task(
        annotator="0",
        user_id="res_38",
        instruction="Review Sophia Nguyen's equity position and if her current grant is below 80,000, increase it by 10,000 effective 2025-08-30. Also check her performance reviews from 2024 and if rated 'Exceeds', award a $12,000 leadership bonus.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Sophia", "last_name": "Nguyen"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10001"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10001"}),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10001"}),
            Action(
                name="increase_employee_compensation",
                kwargs={
                    "employee_id": "E10001",
                    "compensation_id": "COMP2023",
                    "effective_date": "2025-08-30",
                    "equity_increase_amount": 10000,
                },
            ),
            Action(
                name="add_bonus_payment",
                kwargs={"bonus": {"bonus_id": "BON3008", "employee_id": "E10001", "amount": 12000, "currency": "USD", "payment_date": "2025-08-30"}},
            ),
            Action(
                name="add_performance_review",
                kwargs={"review": {"review_id": "PR5064", "employee_id": "E10001", "period_start": "2025-08-30", "period_end": "2025-08-30", "rating": "N/A"}},
            ),
            Action(name="list_bonus_payments", kwargs={"employee_id": "E10001"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10001"}),
        ],
        outputs=["Sophia Nguyen equity increased; leadership bonus BON3008 awarded; review PR5064 recorded."],
    ),
    Task(
        annotator="0",
        user_id="res_39",
        instruction="Process emergency family leave for Rahul Singh (LV6110) from 2025-07-10 to 2025-07-24. Set status to 'Emergency Leave', maintain all benefits, upload emergency documentation, and if he has project assignments, notify temporary coverage.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Rahul", "last_name": "Singh"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
            Action(name="list_leave_records", kwargs={"employee_id": "E10004"}),
            Action(
                name="add_leave_record",
                kwargs={
                    "leave": {
                        "leave_id": "LV6110",
                        "employee_id": "E10004",
                        "leave_type": "Emergency Family Leave",
                        "start_date": "2025-07-10",
                        "end_date": "2025-07-24",
                        "status": "Approved",
                        "notes": "Emergency family leave with full benefits maintained and project coverage arranged.",
                    }
                },
            ),
            Action(
                name="update_employee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {"status": "Emergency Leave"},
                },
            ),
            Action(
                name="add_employee_document",
                kwargs={"document": {"doc_id": "ED7015", "employee_id": "E10004", "doc_type": "Emergency Leave", "title": "Emergency Family Leave Authorization", "date": "2025-07-10"}},
            ),
            Action(name="list_employee_documents", kwargs={"employee_id": "E10004"}),
            Action(name="list_leave_records", kwargs={"employee_id": "E10004"}),
            Action(name="get_employee", kwargs={"employee_id": "E10004"}),
        ],
        outputs=["Rahul Singh emergency leave LV6110 recorded; status set; doc ED7015 stored."],
    ),
    Task(
        annotator="0",
        user_id="res_40",
        instruction="Conduct annual review cycle completion for Marcus Chen. If his status is 'Active', create his 2025 annual review with 'Meets' rating, check if his bonus target should be adjusted based on level L.4 defaults, and award year-end bonus of $4,200.",
        actions=[
            Action(
                name="search_employees",
                kwargs={"filters": {"first_name": "Marcus", "last_name": "Chen"}},
            ),
            Action(name="get_employee", kwargs={"employee_id": "E10006"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10006"}),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10006"}),
            Action(
                name="add_performance_review",
                kwargs={"review": {"review_id": "PR5066", "employee_id": "E10006", "period_start": "2025-01-01", "period_end": "2025-12-31", "rating": "Meets"}},
            ),
            Action(
                name="conditional_bonus_target_normalization",
                kwargs={
                    "employee_id": "E10006",
                    "compensation_id": "COMP2024",
                    "effective_date": "2025-12-31",
                    "target_bonus_pct": 15,
                },
            ),
            Action(
                name="add_bonus_payment",
                kwargs={"bonus": {"bonus_id": "BON3009", "employee_id": "E10006", "amount": 4200, "currency": "EUR", "payment_date": "2025-12-31"}},
            ),
            Action(name="list_performance_reviews", kwargs={"employee_id": "E10006"}),
            Action(name="list_bonus_payments", kwargs={"employee_id": "E10006"}),
            Action(name="get_compensation", kwargs={"employee_id": "E10006"}),
        ],
        outputs=["Marcus Chen annual review PR5066 recorded; bonus target normalized if needed; year-end bonus BON3009 awarded."],
    ),
]
