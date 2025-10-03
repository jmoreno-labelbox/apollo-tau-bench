from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="req01",
        instruction="Review Isabella Chen's (E10001) salary on 2025-01-01. Add a note for the audit and record an audit performance evaluation. Her salary should remain unchanged if she already earns above $250,000. However, should her salary fall under $250,000, increase it to meet the $250,000 threshold.",
        actions=[
            Action(name="GetCompensationRecords", kwargs={"employee_id": "E10001"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"notes": "Founder-level equity grant. Audit note appended 2025-01-01.", "performance_review_ids": ["PR5001", "PR_AUDIT_20250101"]},
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR_AUDIT_20250101",
                        "employee_id": "E10001",
                        "period_start": "2025-01-01",
                        "period_end": "2025-01-01",
                        "rating": "Pending",
                        "summary": "Compensation audit on 2025-01-01.",
                    }
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            "Isabella Chen's compensation was audited on 2025-01-01; no changes were needed. The audit note and review are stored."
        ],
    ),
    Task(
        annotator="0",
        user_id="req02",
        instruction="Handle the transfer of Michael Park (E10002) from the Sales team IND New York to the Berlin-based Engineering department, provided he isn't already assigned there. Update his department designation to DEPT1001, set his work_location to 'Munich Office' if applicable, and assign his manager to Isabella Chen (E10001). If changes are implemented, document a relocation leave (LV2002) spanning from 2026-04-01 to 2026-04-14, and establish an integration performance assessment (PR2002). Include a transfer note and verify the modifications by returning the revised employee record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "department_id": "DEPT1001",
                        "work_location": "Munich Office",
                        "manager_id": "E10001",
                        "notes": "High performer—President's Club 2023. Transferred to Engineering – Munich Office.",
                        "performance_review_ids": ["PR5002", "PR2002"],
                    },
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV2002",
                        "employee_id": "E10002",
                        "leave_type": "Relocation",
                        "start_date": "2026-04-01",
                        "end_date": "2026-04-14",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR2002",
                        "employee_id": "E10002",
                        "period_start": "2026-04-14",
                        "period_end": "2026-04-14",
                        "rating": "Pending",
                        "summary": "Post-relocation integration review.",
                    }
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            "Michael Park is now IND Engineering (Munich Office) under Isabella Chen. Relocation leave LV2002 and review PR2002 are recorded."
        ],
    ),
    Task(
        annotator="0",
        user_id="req03",
        instruction="Handle the promotion of Emma Rodriguez (E10003) to lead the Q2 Accessibility Initiative, if not yet accomplished. Generate compensation record COMP5001 with a base_salary = $160,000 USD, effective as of 2026-04-01, and prepare performance review PR5001 for project kickoff. Add a promotion note and provide her updated record as confirmation.",
        actions=[
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP5001",
                        "employee_id": "E10003",
                        "base_salary": 160000,
                        "currency": "USD",
                        "effective_date": "2026-04-01",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR5001",
                        "employee_id": "E10003",
                        "period_start": "2026-04-01",
                        "period_end": "2026-04-01",
                        "rating": "Pending",
                        "summary": "Project kickoff review – Accessibility Initiative.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP5001",
                        "notes": "Promoted to Project Lead for Accessibility Initiative on 2026-04-01.",
                        "performance_review_ids": ["PR5003", "PR5010", "PR5001"],
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            "Emma Rodriguez is now Project Lead for the Accessibility Initiative with updated compensation (COMP5001) and review PR5001."
        ],
    ),
    Task(
        annotator="0",
        user_id="req04",
        instruction="Initiate the structured off-boarding for William Liu (E10006), if it hasn't been started. Change status to 'Offboarding', log transition leave LV3006 (2026-05-01 → 2026-05-15), draft final performance review PR3006, transfer his benefits to COBRA, and attach a confirmation note sanctioned by HR and IT. Submit the updated employee record for verification.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {
                        "status": "Offboarding",
                        "benefit_plan_ids": ["COBRA"],
                        "notes": "Previously led successful product launches at major tech companies. Offboarding initiated; HR & IT confirmed.",
                        "performance_review_ids": ["PR3006"],
                    },
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV3006",
                        "employee_id": "E10006",
                        "leave_type": "Transition",
                        "start_date": "2026-05-01",
                        "end_date": "2026-05-15",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR3006",
                        "employee_id": "E10006",
                        "period_start": "2026-05-01",
                        "period_end": "2026-05-15",
                        "rating": "Final",
                        "summary": "Final performance review during offboarding.",
                    }
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
        ],
        outputs=[
            "William Liu has been set to Offboarding status with transition leave LV3006 and final review PR3006. COBRA benefits applied and HR/IT confirmation noted."
        ],
    ),
    Task(
        annotator="0",
        user_id="req05",
        instruction="Handle succession planning for Isabella Chen (E10001) as she prepares for her sabbatical. Add a succession-planning note, schedule sabbatical leave LV6002 from 2026-07-01 to 2026-09-01, incorporate planning review PR6002, update her benefit plans to include BEN4012, and confirm by returning her updated record.",
        actions=[
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"notes": "Founder-level equity grant. Succession planning initiated.", "performance_review_ids": ["PR6002"]},
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR6002",
                        "employee_id": "E10001",
                        "period_start": "2026-07-01",
                        "period_end": "2026-07-01",
                        "rating": "Pending",
                        "summary": "Succession planning review.",
                    }
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV6002",
                        "employee_id": "E10001",
                        "leave_type": "Sabbatical",
                        "start_date": "2026-07-01",
                        "end_date": "2026-09-01",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4012"], "performance_review_ids": ["PR5001", "PR6002"]},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            "Succession planning for Isabella Chen is IND place: sabbatical leave LV6002, review PR6002, benefit update, and succession note recorded."
        ],
    ),
    Task(
        annotator="0",
        user_id="req06",
        instruction="On 2025-03-01, deliver a formal written warning to Michael Park (E10002) for repeated tardiness. Prepare performance review PR7002 for the warning, plan improvement-plan leave LV7002 from 2025-04-01 to 2025-04-14, organize follow-up review PR7002F dated 2025-07-15, and attach an acknowledgment note.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR7002",
                        "employee_id": "E10002",
                        "period_start": "2025-03-01",
                        "period_end": "2025-03-01",
                        "rating": "Needs Improvement",
                        "summary": "Written warning for repeated tardiness issued 2025-03-01.",
                    }
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV7002",
                        "employee_id": "E10002",
                        "leave_type": "Improvement Plan",
                        "start_date": "2025-04-01",
                        "end_date": "2025-04-14",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR7002F",
                        "employee_id": "E10002",
                        "period_start": "2025-07-15",
                        "period_end": "2025-07-15",
                        "rating": "Pending",
                        "summary": "Follow-up review after improvement plan scheduled.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"notes": "Disciplinary action confirmed"},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            "Formal warning, improvement plan, and acknowledgment for Michael Park recorded with reviews PR7002 and PR7002F."
        ],
    ),
    Task(
        annotator="0",
        user_id="req07",
        instruction="On 2025-09-01, designate Emma Rodriguez (E10003) to participate IND the cross-functional Green Initiative project. Ensure compensation adjustment COMP8002 is logged to update her base salary to 165,000 USD effective 2026-09-01, initiate review PR8002 dated 2025-09-01, plan project-training leave LV8002 for 2025-09-05→2025-09-10, and complete recognition review PR8002R dated 2026-12-15. Modify her department to DEPT1005, incorporate benefit plan BEN4008, set compensation to COMP8002, include a project note, and revise her performance review. Provide her updated record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP8002",
                        "employee_id": "E10003",
                        "base_salary": 165000,
                        "currency": "USD",
                        "bonus_target_pct": 22,
                        "equity_grant": 35000,
                        "effective_date": "2026-09-01",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR8002",
                        "employee_id": "E10003",
                        "period_start": "2026-09-01",
                        "period_end": "2025-09-01",
                        "rating": "Pending",
                        "summary": "Green Initiative kickoff review.",
                    }
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV8002",
                        "employee_id": "E10003",
                        "leave_type": "Project Training",
                        "start_date": "2026-09-05",
                        "end_date": "2026-09-10",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR8002R",
                        "employee_id": "E10003",
                        "period_start": "2025-12-15",
                        "period_end": "2025-12-15",
                        "rating": "Outstanding",
                        "summary": "Recognition for leadership on Green Initiative.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {
                        "department_id": "DEPT1005",
                        "benefit_plan_ids": ["BEN4001", "BEN4003", "BEN4004", "BEN4008"],
                        "compensation_id": "COMP8002",
                        "performance_review_ids": ["PR5003", "PR5010", "PR8002", "PR8002R"],
                        "notes": "On parental leave 2024-11-01 → 2025-02-01. Assigned to Green Initiative 2026-09-01.",
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            "Emma Rodriguez assigned to Green Initiative with compensation COMP8002, reviews PR8002/PR8002R, training leave LV8002, and updated benefits."
        ],
    ),
    Task(
        annotator="0",
        user_id="req08",
        instruction="Implement retention incentives for Olivia Martinez (E10005) effective 2025-10-01. Incorporate compensation record COMP9003 (with a base salary of 80,000 EUR), handle retention review PR9003 dated 2025-10-01, organize retention-training leave LV9003 from 2025-10-05 to 2025-10-10, and finalize recognition review PR9003R dated 2025-12-15. Broaden her benefit plans with BEN4013, include a retention note, update her compensation and performance reviews, and provide her updated record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP9003",
                        "employee_id": "E10005",
                        "base_salary": 80000,
                        "currency": "EUR",
                        "bonus_target_pct": 10,
                        "equity_grant": 4000,
                        "effective_date": "2026-10-01",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR9003",
                        "employee_id": "E10005",
                        "period_start": "2025-10-01",
                        "period_end": "2025-10-01",
                        "rating": "Pending",
                        "manager_id": "E10011",
                        "summary": "Retention plan review.",
                    }
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV9003",
                        "employee_id": "E10005",
                        "leave_type": "Retention Training",
                        "start_date": "2026-10-05",
                        "end_date": "2026-10-10",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR9003R",
                        "employee_id": "E10005",
                        "period_start": "2025-12-15",
                        "period_end": "2025-12-15",
                        "rating": "Outstanding",
                        "manager_id": "E10011",
                        "summary": "Recognition for loyalty following retention program.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "benefit_plan_ids": ["BEN4001", "BEN4005", "BEN4013"],
                        "compensation_id": "COMP9003",
                        "performance_review_ids": ["PR9003", "PR9003R"],
                        "notes": "Recent graduate—ESADE Business School. Retention incentives applied 2026-10-01.",
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
        ],
        outputs=[
            "Olivia Martinez retention incentives applied: compensation COMP9003, reviews PR9003/PR9003R, training leave LV9003, and updated benefits."
        ],
    ),
    Task(
        annotator="0",
        user_id="req09",
        instruction="Handle the emergency response for Arjun Patel (E10004) following an on-site incident on 2025-11-01. Set his status to 'On Leave', create medical leave LV10003 from 2025-11-01 to 2025-11-15), extend benefit plans with BEN4008, log incident-compliance review PR10003 (dated 2025-11-01) and recovery review PR10003R (dated 2025-12-01), append an emergency-response note, update the performance review, and return his updated record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10004", "updates": {"status": "On Leave"}},
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV10003",
                        "employee_id": "E10004",
                        "leave_type": "Medical",
                        "start_date": "2026-11-01",
                        "end_date": "2026-11-15",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR10003",
                        "employee_id": "E10004",
                        "period_start": "2026-11-01",
                        "period_end": "2025-11-01",
                        "rating": "Pending",
                        "manager_id": "E10001",
                        "summary": "Incident compliance acknowledgment.",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR10003R",
                        "employee_id": "E10004",
                        "period_start": "2025-12-01",
                        "period_end": "2026-12-01",
                        "rating": "Pending",
                        "manager_id": "E10001",
                        "summary": "Post-incident recovery review.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {"notes": "HR and manager notified"},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
        ],
        outputs=[
            "Emergency response for Arjun Patel recorded with leave LV10003, reviews PR10003/PR10003R, updated benefits, and status 'On Leave'."
        ],
    ),
    Task(
        annotator="0",
        user_id="req10",
        instruction="Coordinate Isabella Chen's (E10001) assignment to a GBR cross-border project effective 2025-12-01. Update her work location to 'Manchester Office', create compensation record COMP11001 with a base salary of £260,000 GBP effective 2025-12-01, log assignment prep leave LV11001 for 2025-11-15 to 2025-11-30, add cross-border compliance review PR11001 dated 2025-12-01, extend her benefit plans with BEN4014, append notes for assignment acceptance and digital signature, update compensation and performance reviews, and return her updated record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP11001",
                        "employee_id": "E10001",
                        "base_salary": 260000,
                        "currency": "GBP",
                        "bonus_target_pct": 30,
                        "equity_grant": 60000,
                        "effective_date": "2026-12-01",
                    }
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV11001",
                        "employee_id": "E10001",
                        "leave_type": "Assignment Prep",
                        "start_date": "2026-11-15",
                        "end_date": "2026-11-30",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR11001",
                        "employee_id": "E10001",
                        "period_start": "2025-12-01",
                        "period_end": "2025-12-01",
                        "rating": "Pending",
                        "manager_id": "E10012",
                        "summary": "Cross-border compliance acknowledgment.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "work_location": "Manchester Office",
                        "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003", "BEN4014"],
                        "compensation_id": "COMP11001",
                        "performance_review_ids": ["PR5001", "PR11001"],
                        "notes": "Founder-level equity grant. Assignment acceptance recorded 2026-12-01. Digital signature captured.",
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            "Isabella Chen's GBR assignment recorded with compensation COMP11001, leave LV11001, compliance review PR11001, updated benefits, and notes appended."
        ],
    ),
    Task(
        annotator="0",
        user_id="req11",
        instruction="Emma Rodriguez (E10003) will take parental leave from 1 March 2026 to 1 June 2026. Kindly register this leave request as LV8001 (status 'Scheduled') and then display her complete leave history so she can verify the dates.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV8001",
                        "employee_id": "E10003",
                        "leave_type": "Parental",
                        "start_date": "2026-03-01",
                        "end_date": "2026-06-01",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(name="GetLeaveRecords", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            "Parental leave LV8001 captured for Emma Rodriguez; her updated leave list is returned."
        ],
    ),
    Task(
        annotator="0",
        user_id="req12",
        instruction="Conduct a quick data-quality verification for Olivia Martinez (E10005). Following this, append a brief audit note ('Data audit completed 2 Feb 2026') to her file, then retrieve her employee record, pay history, and review history for Finance approval.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {"notes": "Recent graduate—ESADE Business School. Data audit completed 2026-02-02."},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(name="GetCompensationRecords", kwargs={"employee_id": "E10005"}),
            Action(name="GetPerformanceReviews", kwargs={"employee_id": "E10005"}),
        ],
        outputs=[
            "Audit note added for Olivia Martinez; refreshed employee, compensation, and review data returned."
        ],
    ),
    Task(
        annotator="0",
        user_id="req13",
        instruction="Handle Isabella Chen's (E10001) request for personal time off from 1 July 2026 to 10 July 2026 by logging leave LV8002 (status Scheduled) and providing her with a complete confirmation of her leave records.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV8002",
                        "employee_id": "E10001",
                        "leave_type": "Personal",
                        "start_date": "2026-07-01",
                        "end_date": "2026-07-10",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(name="GetLeaveRecords", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            "Personal leave LV8002 logged for Isabella Chen and full leave list returned."
        ],
    ),
    Task(
        annotator="0",
        user_id="req14",
        instruction="Following Michael Park's impressive performance IND 2025, adjust his annual bonus target to 28%, ensuring his base pay remains at $210,000. Coordinate the recording of the new compensation package (ID COMP3002, effective 1 January 2026) and integrate review PR6002 summarising the results. Conclude with an update to his notes reflecting the review date.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP3002",
                        "employee_id": "E10002",
                        "base_salary": 210000,
                        "currency": "USD",
                        "bonus_target_pct": 28,
                        "equity_grant": 40000,
                        "effective_date": "2026-01-01",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR6002",
                        "employee_id": "E10002",
                        "period_start": "2025-01-01",
                        "period_end": "2025-12-31",
                        "rating": "Exceeds",
                        "manager_id": "E10012",
                        "summary": "2025 annual review – bonus target raised to 28%.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"notes": "Annual review completed 2026-01-15."},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetCompensationRecords", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            "Michael Park's comp update (COMP3002) and review PR6002 saved; employee record returned."
        ],
    ),
    Task(
        annotator="0",
        user_id="req15",
        instruction="Introduce Olivia Martinez (E10005) to the Finance department. Verify her assigned department is DEPT1004, log her starting compensation package COMP9001 (effective 1 Sep 2026, €75 000 base, 5 % bonus), and record the onboarding date IND her file. Provide her updated employee and compensation details so that Finance HR can conduct a final review.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "department_id": "DEPT1004",
                        "notes": "Onboarded to Finance 2026-09-01.",
                    },
                },
            ),
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP9001",
                        "employee_id": "E10005",
                        "base_salary": 75000,
                        "currency": "EUR",
                        "bonus_target_pct": 5,
                        "equity_grant": 2500,
                        "effective_date": "2026-09-01",
                    }
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(name="GetCompensationRecords", kwargs={"employee_id": "E10005"}),
        ],
        outputs=[
            "Olivia Martinez is now fully set up IND Finance with starting package COMP9001."
        ],
    ),
    Task(
        annotator="0",
        user_id="req16",
        instruction="During the January 2 2026 audit, update William Liu's (E10006) compensation and performance file. Adjust his base salary to €65,000 (maintaining bonus 5% and equity €5,000) effective January 1 2026 (record ID COMP3006) and document audit review PR6004 dated January 2 2026 (rating 'Meets'). Include a brief note '2026 compensation audit completed'. Submit his updated record for Finance to archive.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP3006",
                        "employee_id": "E10006",
                        "base_salary": 65000,
                        "currency": "EUR",
                        "bonus_target_pct": 5,
                        "equity_grant": 5000,
                        "effective_date": "2026-01-01",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR6004",
                        "employee_id": "E10006",
                        "period_start": "2026-01-02",
                        "period_end": "2026-01-02",
                        "rating": "Meets",
                        "manager_id": "E10012",
                        "summary": "2026 compensation audit recorded.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {
                        "compensation_id": "COMP3006",
                        "performance_review_ids": ["PR5011", "PR6004"],
                        "notes": "Previously led successful product launches at major tech companies. 2026 compensation audit completed.",
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
        ],
        outputs=[
            "William Liu's 2026 audit recorded with comp COMP3006 and review PR6004. Record returned."
        ],
    ),
    Task(
        annotator="0",
        user_id="req17",
        instruction="On October 1 2025, William Liu (E10006) will be transitioning to the Finance department as a Senior Accountant. Adjust his department to DEPT1004 and update his position to POS3013. Increase his salary to €65,000 (bonus 5%, equity €5,000) IND compensation record COMP3007 with effect from October 1 2025, and document the transition review PR9002 on that date, assigning the rating as Pending. Include a note stating 'Transferred to Finance 1 Oct 2025'. Distribute his updated profile to the new team for a warm welcome.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {
                        "department_id": "DEPT1004",
                        "position_id": "POS3013",
                        "notes": "Previously led successful product launches at major tech companies. Transferred to Finance 2025-10-01.",
                    },
                },
            ),
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP3007",
                        "employee_id": "E10006",
                        "base_salary": 65000,
                        "currency": "EUR",
                        "bonus_target_pct": 5,
                        "equity_grant": 5000,
                        "effective_date": "2025-10-01",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR9002",
                        "employee_id": "E10006",
                        "period_start": "2025-10-01",
                        "period_end": "2025-10-01",
                        "rating": "Pending",
                        "manager_id": "E10011",
                        "summary": "Transition to Finance as Senior Accountant recorded.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {
                        "compensation_id": "COMP3007",
                        "performance_review_ids": ["PR5011", "PR9002"],
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
        ],
        outputs=[
            "William Liu welcomed to Finance with comp COMP3007 and review PR9002. Updated profile returned."
        ],
    ),
    Task(
        annotator="0",
        user_id="req18",
        instruction="Isabella Chen (E10001) has enrolled in the Wellness Plan BEN4010 beginning on September 1 2026. Implement the plan, record her acceptance IND review PR8005 (dated September 1 2026), and add 'Digital signature for wellness plan confirmed.' to her notes. Kindly circulate her updated profile once this is completed.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4003", "BEN4010"],
                        "notes": "Founder-level equity grant. Digital signature for wellness plan confirmed.",
                    },
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR8005",
                        "employee_id": "E10001",
                        "period_start": "2026-09-01",
                        "period_end": "2026-09-01",
                        "rating": "Acknowledged",
                        "summary": "Wellness benefit BEN4010 accepted.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"performance_review_ids": ["PR5001", "PR8005"]},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            "Wellness plan BEN4010 recorded for Isabella Chen with review PR8005. Updated profile returned."
        ],
    ),
    Task(
        annotator="0",
        user_id="req19",
        instruction="Manage the onboarding process for Emma Rodriguez (E10003). First, record: 'Orientation status: IND Progress', then include a second note: 'Completed training modules: HR101, MKTG201, ETHICS202'. Submit confirmation review PR8006 dated March13 2026 (rating 'Complete'). Return her updated record for inclusion in HR files.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"notes": "On parental leave 2024-11-01 → 2025-02-01. Orientation status: IND Progress"},
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"notes": "On parental leave 2024-11-01 → 2025-02-01. Orientation status: IND Progress. Completed training modules: HR101, MKTG201, ETHICS202"},
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR8006",
                        "employee_id": "E10003",
                        "period_start": "2026-03-31",
                        "period_end": "2026-03-31",
                        "rating": "Complete",
                        "summary": "Orientation and training completed.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10003",
                    "updates": {"performance_review_ids": ["PR5003", "PR5010", "PR8006"]},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            "Onboarding tracked for Emma Rodriguez with review PR8006. Updated record returned."
        ],
    ),
    Task(
        annotator="0",
        user_id="req20",
        instruction="Assemble Isabella Chen's (E10001) Q2 2026 report. Conduct a review of document PR8007 covering april 1 to june 30 2026 (rating 'Pending') and append the note 'Q2 2026 HR report completed.' Provide her updated profile once saved.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR8007",
                        "employee_id": "E10001",
                        "period_start": "2026-04-01",
                        "period_end": "2026-06-30",
                        "rating": "Pending",
                        "summary": "Q2 2026 Quarterly Review.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "notes": "Founder-level equity grant. Q2 2026 HR report completed.",
                        "performance_review_ids": ["PR5001", "PR8007"],
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            "Q2 2026 review PR8007 added for Isabella Chen and note appended; updated record returned."
        ],
    ),
    Task(
        annotator="0",
        user_id="req21",
        instruction="Please ensure Michael Park (E10002) receives Parental Leave cover beginning August 1 2026. Update his benefit list to include BEN4004, document a small stipend IND compensation record COMP9002 (base salary remains $220,000, bonus 30%, equity $45,000, effective August 1 2026), and subsequently share his revised profile for HR to complete the filing of paperwork.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"benefit_plan_ids": ["BEN4001", "BEN4002", "BEN4004"]},
                },
            ),
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP9002",
                        "employee_id": "E10002",
                        "base_salary": 220000,
                        "currency": "USD",
                        "bonus_target_pct": 30,
                        "equity_grant": 45000,
                        "effective_date": "2026-08-01",
                    }
                },
            ),
            Action(
                name="GetEmployee",
                kwargs={"employee_id": "E10002"},
            ),
            Action(
                name="GetCompensationRecords",
                kwargs={"employee_id": "E10002"},
            ),
        ],
        outputs=[
            "Parental Leave benefit BEN4004 added for Michael Park with stipend COMP9002; updated profile returned."
        ],
    ),
    Task(
        annotator="0",
        user_id="req22",
        instruction="Proceed to acknowledge Emma Rodriguez (E10003) as a Senior Front-end Engineer. Effective January 1 2026, adjust her position to POS3006, salary $155,000 with 15% bonus (comp record COMP4003), and register the review PR7003 (rating 'Exceeds') overseen by Isabella Chen. Lastly, retrieve the Engineering (DEPT1001) details so we can inform the department head.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10003", "updates": {"position_id": "POS3006"}},
            ),
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP4003",
                        "employee_id": "E10003",
                        "base_salary": 155000,
                        "currency": "USD",
                        "bonus_target_pct": 15,
                        "equity_grant": 25000,
                        "effective_date": "2026-01-01",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR7003",
                        "employee_id": "E10003",
                        "period_start": "2026-01-01",
                        "period_end": "2026-01-01",
                        "rating": "Exceeds",
                        "manager_id": "E10001",
                        "summary": "Promotion to Senior Front-end Engineer recorded.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10003", "updates": {"notes": "Promotion and compensation updated 2026-01-01"}},
            ),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
        ],
        outputs=[
            "Emma Rodriguez promoted with comp COMP4003 and review PR7003; Engineering department head confirmed."
        ],
    ),
    Task(
        annotator="0",
        user_id="req23",
        instruction="Handle the inclusion of Arjun Patel (E10004) IND a Finance cross-department project commencing on July 24 2025 under William Liu (E10006). Modify his manager and department details accordingly, document review PR8008 for that date with the rating 'Acknowledged', and arrange his project-assignment leave LV9004 from September 1 to 15 2026. Return his updated record for inclusion in the project dossier.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10004", "updates": {"department_id": "DEPT1004", "manager_id": "E10006"}},
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR8008",
                        "employee_id": "E10004",
                        "period_start": "2025-07-24",
                        "period_end": "2025-07-24",
                        "rating": "Acknowledged",
                        "summary": "Finance project assignment under William Liu recorded.",
                    }
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV9004",
                        "employee_id": "E10004",
                        "leave_type": "Project Assignment",
                        "start_date": "2026-09-01",
                        "end_date": "2026-09-15",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
        ],
        outputs=[
            "Arjun Patel assigned to Finance project with review PR8008 and leave LV9004; profile returned."
        ],
    ),
    Task(
        annotator="0",
        user_id="req24",
        instruction="Coordinate a prompt records examination for Olivia Martinez (E10005). Append the remark 'Data audit completed 10 Feb 2026' and subsequently retrieve her employee record along with her compensation and review history for archiving.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id":"E10005"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id":"E10005",
                    "updates":{"notes":"Recent graduate—ESADE Business School. Data audit completed 2026-02-10."},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id":"E10005"}),
            Action(name="GetCompensationRecords", kwargs={"employee_id":"E10005"}),
            Action(name="GetPerformanceReviews", kwargs={"employee_id":"E10005"}),
        ],
        outputs=["Data audit note added; Elena's records returned."]
    ),
    Task(
        annotator="0",
        user_id="req25",
        instruction="William Liu (E10006) is assigned to assist Marketing IND Q4 2026. Transfer him to DEPT1005, retain position POS3006, initiate review PR7006 dated October 1 2026 (rating Pending) with manager E10013, and arrange transition leave LV9005 from October 1 to the 10th of 2026. Amend his notes to include 'Temporary transfer to Marketing Q4 2026'. Deliver his revised profile once recorded.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id":"E10006"}),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id":"E10006", "updates":{"department_id":"DEPT1005", "position_id":"POS3006", "notes":"Previously led successful product launches at major tech companies. Temporary transfer to Marketing Q4 2026."}},
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review":{
                        "review_id":"PR7006",
                        "employee_id":"E10006",
                        "period_start":"2026-10-01",
                        "period_end":"2026-10-01",
                        "rating":"Pending",
                        "manager_id":"E10013",
                        "summary":"Temporary Marketing transfer recorded.",
                    }
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record":{
                        "leave_id":"LV9005",
                        "employee_id":"E10006",
                        "leave_type":"Transition",
                        "start_date":"2026-10-01",
                        "end_date":"2026-10-10",
                        "status":"Scheduled",
                    }
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id":"E10006"}),
        ],
        outputs=["Marketing transfer logged for William Liu with review PR7006 and leave LV9005; profile returned."]
    ),
    Task(
        annotator="0",
        user_id="req26",
        instruction="Isabella Chen (E10001) spearheaded our July 24 2025 diversity campaign. Log review PR8010 (rating 'Outstanding', date July 24 2025) and incorporate the note 'Diversity initiative participation: Active lead'. Subsequently, distribute her refreshed profile for the newsletter.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR8010",
                        "employee_id": "E10001",
                        "period_start": "2025-07-24",
                        "period_end": "2025-07-24",
                        "rating": "Outstanding",
                        "summary": "Leadership IND company-wide diversity initiative recorded.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "notes": "Founder-level equity grant. Diversity initiative participation: Active lead.",
                        "performance_review_ids": ["PR5001", "PR8010"],
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
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
                    "PR8010"
                ],
                "skills": [
                    "Leadership",
                    "Cloud Architecture",
                    "Python"
                ],
                "role_description": "Chief Technology Officer overseeing all engineering functions.",
                "notes": "Founder-level equity grant. Diversity initiative participation: Active lead."
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="req27",
        instruction="Michael Park (E10002) accomplished his 2026 compliance training on February 15 2026. Please record review PR9104 (rating 'Complete', date February 15 2026) and include the note 'Compliance modules HR101 & ITSEC303 completed'. Submit his updated record for audit files.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR9104",
                        "employee_id": "E10002",
                        "period_start": "2026-02-15",
                        "period_end": "2026-02-15",
                        "rating": "Complete",
                        "summary": "2026 compliance training completed.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {"notes": "Compliance modules HR101 & ITSEC303 completed 2026-02-15."},
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
        ],
        outputs=[
            "Michael Park's compliance training, leave balance, and completion records are updated and confirmed."
        ],
    ),
    Task(
        annotator="0",
        user_id="req28",
        instruction="All Engineering (DEPT1001) employees are required to attend a one-day Cybersecurity Awareness session on August 1 2026. Generate review IDs PR13001 (E10001), PR13002 (E10003), and PR13003 (E10004) with rating 'Pending', allocate a corresponding same-day training leave (LV13001-03), and attach a brief 'Cybersecurity training assigned' note for each. Finally, return the department roster for IT to track attendance.",
        actions=[
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(name="AddPerformanceReview", kwargs={"performance_review": {"review_id": "PR13001", "employee_id": "E10001", "period_start": "2026-08-01", "period_end": "2026-08-01", "rating": "Pending", "summary": "Cybersecurity training scheduled."}}),
            Action(name="AddLeaveRecord", kwargs={"leave_record": {"leave_id": "LV13001", "employee_id": "E10001", "leave_type": "Cybersecurity Training", "start_date": "2026-08-01", "end_date": "2026-08-01", "status": "Scheduled"}}),
            Action(name="UpdateEmployee", kwargs={"employee_id": "E10001", "updates": {"notes": "Cybersecurity training assigned", "performance_review_ids": ["PR5001", "PR13001"]}}),
            Action(name="AddPerformanceReview", kwargs={"performance_review": {"review_id": "PR13002", "employee_id": "E10003", "period_start": "2026-08-01", "period_end": "2026-08-01", "rating": "Pending", "summary": "Cybersecurity training scheduled."}}),
            Action(name="AddLeaveRecord", kwargs={"leave_record": {"leave_id": "LV13002", "employee_id": "E10003", "leave_type": "Cybersecurity Training", "start_date": "2026-08-01", "end_date": "2026-08-01", "status": "Scheduled"}}),
            Action(name="UpdateEmployee", kwargs={"employee_id": "E10003", "updates": {"notes": "Cybersecurity training assigned", "performance_review_ids": ["PR5003", "PR5010", "PR13002"]}}),
            Action(name="AddPerformanceReview", kwargs={"performance_review": {"review_id": "PR13003", "employee_id": "E10004", "period_start": "2026-08-01", "period_end": "2026-08-01", "rating": "Pending", "summary": "Cybersecurity training scheduled."}}),
            Action(name="AddLeaveRecord", kwargs={"leave_record": {"leave_id": "LV13003", "employee_id": "E10004", "leave_type": "Cybersecurity Training", "start_date": "2026-08-01", "end_date": "2026-08-01", "status": "Scheduled"}}),
            Action(name="UpdateEmployee", kwargs={"employee_id": "E10004", "updates": {"notes": "Cybersecurity training assigned", "performance_review_ids": ["PR5004", "PR5009", "PR13003"]}}),
            Action(name="GetDepartment", kwargs={"department_id": "DEPT1001"}),
        ],
        outputs=[
            "all engineering members, IND DEPT1001, now have a cybersecurity training assigned"
        ]
    ),
    Task(
        annotator="0",
        user_id="req29",
        instruction="Handle the update of the HR file for Arjun Patel (E10004). Add a note to his record indicating a new emergency contact: 'Emergency contact updated: Priya Singh, +1-555-123-4567'. Additionally, coordinate the documentation of his annual safety training completion by generating a 'Complete' performance review for the 2026 calendar year. Ensure to obtain his updated employee record for verification.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR8012",
                        "employee_id": "E10004",
                        "period_start": "2026-01-01",
                        "period_end": "2026-12-31",
                        "rating": "Complete",
                        "summary": "Annual safety training completed.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10004",
                    "updates": {
                        "notes": "Visa sponsored (H-1B). Emergency contact updated: Priya Singh, +1-555-123-4567",
                        "performance_review_ids": ["PR5004", "PR5009", "PR8012"],
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
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
                    "PR8012"
                ],
                "skills": [
                    "Go",
                    "Kubernetes",
                    "CI/CD"
                ],
                "role_description": "Backend Engineer focusing on micro-services.",
                "notes": "Visa sponsored (H-1B). Emergency contact updated: Priya Singh, +1-555-123-4567"
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="req30",
        instruction="William Liu (E10006) is set to move to Marketing on January 1 2027 as a Lead Analyst. Begin by adding position POS4001 (title 'Lead Analyst', Finance family, level L.4), update his department/position/manager details, create the compensation record COMP8013 ($90,000 base, bonus 12%, equity $10,000, effective 1 Jan 2027), include review PR8013 (rating 'Pending', date January 1 2027), and book relocation leave LV8013 from January 10 to 20 2027. Please provide his updated profile.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
            Action(
                name="AddPosition",
                kwargs={
                    "position": {
                        "position_id": "POS4001",
                        "title": "Lead Analyst",
                        "family": "Marketing",
                        "level_id": "L.4",
                        "department_id": "DEPT1005",
                        "description": "Leads marketing analytics initiatives.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {
                        "department_id": "DEPT1005",
                        "position_id": "POS4001",
                        "manager_id": "E10001",
                    },
                },
            ),
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP8013",
                        "employee_id": "E10006",
                        "base_salary": 90000,
                        "currency": "USD",
                        "bonus_target_pct": 12,
                        "equity_grant": 10000,
                        "effective_date": "2027-01-01",
                    }
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV8013",
                        "employee_id": "E10006",
                        "leave_type": "Relocation",
                        "start_date": "2027-01-10",
                        "end_date": "2027-01-20",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR8013",
                        "employee_id": "E10006",
                        "period_start": "2027-01-01",
                        "period_end": "2027-01-01",
                        "rating": "Pending",
                        "summary": "Onboarding to Marketing as Lead Analyst.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10006",
                    "updates": {
                        "compensation_id": "COMP8013",
                        "performance_review_ids": ["PR5011", "PR8013"],
                        "notes": "Previously led successful product launches at major tech companies. Transfer to Marketing 2027-01-01.",
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
        ],
        outputs=["Marketing transfer logged for William Liu with comp COMP8013, review PR8013 and leave LV8013; profile returned."]
    ),
    Task(
        annotator="0",
        user_id="req31",
        instruction="Manage the upgrade of benefits for Olivia Martinez (E10005) effective February 1 2027. Update her benefits list to include BEN4006 and BEN4007, document this modification with review PR10002 (rating 'Pending', from 2027-02-01 to 2027-07-31, manager E10011), arrange medical leave LV10002 (from 2027-03-01 to 2027-03-15), allocate retention bonus compensation COMP10002 (EUR 80,000 base, 10% bonus target, €5,000 equity, effective 2027-03-01), and revise her notes. Provide her renewed employee record and compensation history.",
        actions=[
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {"benefit_plan_ids": ["BEN4001", "BEN4006", "BEN4007"]},
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR10002",
                        "employee_id": "E10005",
                        "period_start": "2027-02-01",
                        "period_end": "2027-07-31",
                        "rating": "Pending",
                        "manager_id": "E10011",
                        "summary": "Benefit package upgrade recorded.",
                    }
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV10002",
                        "employee_id": "E10005",
                        "leave_type": "Medical",
                        "start_date": "2027-03-01",
                        "end_date": "2027-03-15",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP10002",
                        "employee_id": "E10005",
                        "base_salary": 80000,
                        "currency": "EUR",
                        "bonus_target_pct": 10,
                        "equity_grant": 5000,
                        "effective_date": "2027-03-01",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP10002",
                        "performance_review_ids": ["PR10002"],
                        "notes": "Benefit overhaul completed 2027-03-01.",
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(name="GetCompensationRecords", kwargs={"employee_id": "E10005"}),
        ],
        outputs=[
            "Benefits upgraded, retention compensation COMP10002 granted, review PR10002 logged, and medical leave LV10002 scheduled for Olivia Martinez. Updated record returned.",
        ],
    ),
    Task(
        annotator="0",
        user_id="req32",
        instruction="From March 1 2027, implement a retention package for Olivia Martinez (E10005): incorporate BEN4006 (Vision Plan) and BEN4007 (Life Insurance), log medical leave LV8015 from 2027-03-01 to 2027-03-15, offer compensation COMP8014 (EUR 80,000 base, 10% bonus target, €5,000 equity, effective 2027-03-01), record review PR8014 (rating 'Pending' from 2027-03-01 to 2027-07-31, manager E10011), and document the update. Deliver her modified profile.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {"benefit_plan_ids": ["BEN4001", "BEN4005", "BEN4006", "BEN4007"]},
                },
            ),
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP8014",
                        "employee_id": "E10005",
                        "base_salary": 80000,
                        "currency": "EUR",
                        "bonus_target_pct": 10,
                        "equity_grant": 5000,
                        "effective_date": "2027-03-01",
                    }
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV8015",
                        "employee_id": "E10005",
                        "leave_type": "Medical",
                        "start_date": "2027-03-01",
                        "end_date": "2027-03-15",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR8014",
                        "employee_id": "E10005",
                        "period_start": "2027-03-01",
                        "period_end": "2027-07-31",
                        "rating": "Pending",
                        "summary": "Retention package documented.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP8014",
                        "performance_review_ids": ["PR8014"],
                        "notes": "Retention package recorded 2027-03-01.",
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
        ],
        outputs=[
            "Retention package COMP8014, review PR8014, and medical leave LV8015 recorded for Olivia Martinez. Updated profile returned.",
        ],
    ),
    Task(
        annotator="0",
        user_id="req33",
        instruction="Handle a paid sabbatical for Isabella Chen (E10001) from 1 May 2027 to 1 Aug 2027. Designate her status as 'On Sabbatical', appoint Emma Rodriguez (E10003) as acting manager, and document sabbatical leave LV10004 for the identical timeframe. Conduct a succession-planning review PR10004 (rating 'Pending') and a stipend record COMP10004 (USD 250 000 base, 10 % bonus target, no equity, effective 2027-05-01). Attach a note, link the new review and stipend to her profile, then return her record along with compensation history.",
        actions=[
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV10004",
                        "employee_id": "E10001",
                        "leave_type": "Sabbatical",
                        "start_date": "2027-05-01",
                        "end_date": "2027-08-01",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "status": "On Sabbatical",
                        "manager_id": "E10003",
                    },
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR10004",
                        "employee_id": "E10001",
                        "period_start": "2027-05-01",
                        "period_end": "2027-08-01",
                        "rating": "Pending",
                        "manager_id": "E10003",
                        "summary": "Succession planning during sabbatical.",
                    }
                },
            ),
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP10004",
                        "employee_id": "E10001",
                        "base_salary": 250000,
                        "currency": "USD",
                        "bonus_target_pct": 10,
                        "equity_grant": 0,
                        "effective_date": "2027-05-01",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {
                        "notes": "Sabbatical and succession planning 2027-05-01"
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetCompensationRecords", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            "Isabella Chen is on sabbatical. Succession, compensation, and reporting details are confirmed."
        ],
    ),
    Task(
        annotator="0",
        user_id="req34",
        instruction="Coordinate the start of an international Engineering assignment for Michael Park (E10002) starting April 1, 2027. Establish position POS4003 (Project Lead, Engineering, L.5), transition him to DEPT1001 under the supervision of Arjun Patel (E10004), grant him compensation COMP8015 of $230,000 base, 20% bonus target, $50,000 equity, effective 2027-04-01), arrange prep leave LV8016 from 2027-03-15 to 2027-03-25), and log assignment review PR8015 (rating 'Pending' from 2027-04-01 to 2027-12-31). Make sure his profile is updated with the new compensation and review, then return the record.",
        actions=[
            Action(
                name="AddPosition",
                kwargs={
                    "position": {
                        "position_id": "POS4003",
                        "title": "Project Lead",
                        "department_id": "DEPT1001",
                        "level_id": "L.5",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "department_id": "DEPT1001",
                        "position_id": "POS4003",
                        "manager_id": "E10004",
                    },
                },
            ),
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP8015",
                        "employee_id": "E10002",
                        "base_salary": 230000,
                        "currency": "USD",
                        "bonus_target_pct": 20,
                        "equity_grant": 50000,
                        "effective_date": "2027-04-01",
                    }
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV8016",
                        "employee_id": "E10002",
                        "leave_type": "Assignment Prep",
                        "start_date": "2027-03-15",
                        "end_date": "2027-03-25",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR8015",
                        "employee_id": "E10002",
                        "period_start": "2027-04-01",
                        "period_end": "2027-12-31",
                        "rating": "Pending",
                        "summary": "Global Projects assignment review.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10002",
                    "updates": {
                        "notes": "High performer—President's Club 2023. Multi-country assignment 2027-04-01",
                        "performance_review_ids": ["PR5002", "PR8015"],
                    },
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
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
                "position_id": "POS4003",
                "department_id": "DEPT1001",
                "level_id": "L.5",
                "manager_id": "E10004",
                "work_location": "Boston Office",
                "work_email": "michael.park@example.com",
                "work_phone": "+1-212-555-0144",
                "compensation_id": "COMP2002",
                "benefit_plan_ids": [
                    "BEN4001",
                    "BEN4002"
                ],
                "performance_review_ids": [
                    "PR5002",
                    "PR8015"
                ],
                "skills": [
                    "Sales Strategy",
                    "CRM",
                    "Negotiation"
                ],
                "role_description": "Regional VP of Sales for the Eastern territory.",
                "notes": "High performer—President's Club 2023. Multi-country assignment 2027-04-01"
            }
            """
        ],
    ),
    Task(
        annotator="0",
        user_id="req35",
        instruction="All current employees are required to acknowledge the Company Code of Conduct (DOC_CC_2025). For the employee IDs ranging from E10001 to E10006, produce a compliance review (PR12001-PR12006, rating set to 'Pending' on 2026-07-10), plan a one-day leave on 2026-07-20 (LV12001-LV12006) as the deadline for digital signing, and annotate their records with 'Code of Conduct 2025 assigned; department head notified'. Provide a summary upon completion.",
        actions=[
            Action(
                name="AddPerformanceReview",
                kwargs={"performance_review": {"review_id": "PR12001", "employee_id": "E10001", "period_start": "2026-07-10", "period_end": "2026-07-10", "rating": "Pending", "summary": "DOC_CC_2025 acknowledgment required."}},
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={"leave_record": {"leave_id": "LV12001", "employee_id": "E10001", "leave_type": "Policy Signature", "start_date": "2026-07-20", "end_date": "2026-07-20", "status": "Scheduled"}},
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10001", "updates": {"notes": "Code of Conduct 2025 assigned; department head notified"}},
            ),
            # E10002
            Action(
                name="AddPerformanceReview",
                kwargs={"performance_review": {"review_id": "PR12002", "employee_id": "E10002", "period_start": "2026-07-10", "period_end": "2026-07-10", "rating": "Pending", "summary": "DOC_CC_2025 acknowledgment required."}},
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={"leave_record": {"leave_id": "LV12002", "employee_id": "E10002", "leave_type": "Policy Signature", "start_date": "2026-07-20", "end_date": "2026-07-20", "status": "Scheduled"}},
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10002", "updates": {"notes": "Code of Conduct 2025 assigned; department head notified"}},
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={"performance_review": {"review_id": "PR12003", "employee_id": "E10003", "period_start": "2026-07-10", "period_end": "2026-07-10", "rating": "Pending", "summary": "DOC_CC_2025 acknowledgment required."}},
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={"leave_record": {"leave_id": "LV12003", "employee_id": "E10003", "leave_type": "Policy Signature", "start_date": "2026-07-20", "end_date": "2026-07-20", "status": "Scheduled"}},
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10003", "updates": {"notes": "Code of Conduct 2025 assigned; department head notified"}},
            ),
            # E10004
            Action(
                name="AddPerformanceReview",
                kwargs={"performance_review": {"review_id": "PR12004", "employee_id": "E10004", "period_start": "2026-07-10", "period_end": "2026-07-10", "rating": "Pending", "summary": "DOC_CC_2025 acknowledgment required."}},
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={"leave_record": {"leave_id": "LV12004", "employee_id": "E10004", "leave_type": "Policy Signature", "start_date": "2026-07-20", "end_date": "2026-07-20", "status": "Scheduled"}},
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10004", "updates": {"notes": "Code of Conduct 2025 assigned; department head notified"}},
            ),
            # E10005
            Action(
                name="AddPerformanceReview",
                kwargs={"performance_review": {"review_id": "PR12005", "employee_id": "E10005", "period_start": "2026-07-10", "period_end": "2026-07-10", "rating": "Pending", "summary": "DOC_CC_2025 acknowledgment required."}},
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={"leave_record": {"leave_id": "LV12005", "employee_id": "E10005", "leave_type": "Policy Signature", "start_date": "2026-07-20", "end_date": "2026-07-20", "status": "Scheduled"}},
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10005", "updates": {"notes": "Code of Conduct 2025 assigned; department head notified"}},
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={"performance_review": {"review_id": "PR12006", "employee_id": "E10006", "period_start": "2026-07-10", "period_end": "2026-07-10", "rating": "Pending", "summary": "DOC_CC_2025 acknowledgment required."}},
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={"leave_record": {"leave_id": "LV12006", "employee_id": "E10006", "leave_type": "Policy Signature", "start_date": "2026-07-20", "end_date": "2026-07-20", "status": "Scheduled"}},
            ),
            Action(
                name="UpdateEmployee",
                kwargs={"employee_id": "E10006", "updates": {"notes": "Code of Conduct 2025 assigned; department head notified"}},
            ),
        ],
        outputs=[
            "Compliance reviews (PR12001-PR12006) and signature deadline leaves (LV12001-LV12006) scheduled. All employee records updated for Code of Conduct 2025 rollout.",
        ],
    ),
    Task(
        annotator="0",
        user_id="req36",
        instruction="Effective August 1, 2027, Olivia Martinez (E10005) will assume a new expanded dual-role. Reflect this change by updating her position to POS4002 (Analyst II), assigning compensation COMP8017 (base €85,000, 12% bonus target, €7,000 equity, starting from 2027-08-01), scheduling dual-role training leave LV8018 from 2027-08-10 to 2027-08-20, recording the review PR8017 (Pending from 2027-08-01 to 2027-12-31, manager E10011), and modifying her notes. Return her updated profile and compensation history.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10005",
                    "updates": {
                        "position_id": "POS4002",
                        "compensation_id": "COMP8017",
                        "notes": "Dual-role assignment confirmed 2027-08-01.",
                    },
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV8018",
                        "employee_id": "E10005",
                        "leave_type": "Dual-Role Training",
                        "start_date": "2027-08-10",
                        "end_date": "2027-08-20",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR8017",
                        "employee_id": "E10005",
                        "period_start": "2027-08-01",
                        "period_end": "2027-12-31",
                        "rating": "Pending",
                        "summary": "Dual-role performance review.",
                    }
                },
            ),
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
        ],
        outputs=[
            "Dual-role promotion recorded — position POS4002, compensation COMP8017, leave LV8018 and review PR8017 are now linked to Olivia Martinez's file.",
        ],
    ),
    Task(
        annotator="0",
        user_id="req37",
        instruction="Commencing on August 10 2026, Isabella Chen will begin mentoring Olivia Martinez. Document this mentorship relationship, record the mentorship kickoff (PR15002) and schedule a follow-up checkpoint (PR15003 on September 10 2026), and update the notes for both individuals. Provide Elena's updated record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(name="UpdateEmployee", kwargs={"employee_id": "E10001", "updates": {"notes": "Mentor for E10005 from 2026-08-10"}}),
            Action(name="UpdateEmployee", kwargs={"employee_id": "E10005", "updates": {"notes": "Mentee of E10001 starting 2026-08-10"}}),
            Action(name="AddPerformanceReview", kwargs={"performance_review": {"review_id": "PR15002", "employee_id": "E10005", "period_start": "2026-08-10", "period_end": "2026-08-10", "rating": "Pending", "summary": "Mentorship kick-off with E10001."}}),
            Action(name="AddPerformanceReview", kwargs={"performance_review": {"review_id": "PR15003", "employee_id": "E10005", "period_start": "2026-09-10", "period_end": "2026-09-10", "rating": "Pending", "summary": "Mentorship follow-up with E10001."}}),
            Action(name="UpdateEmployee", kwargs={"employee_id": "E10005", "updates": {"performance_review_ids": ["PR15002", "PR15003"]}}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
        ],
        outputs=[
            "Mentorship between Isabella Chen and Olivia Martinez documented with reviews PR15002 and PR15003; records updated.",
        ],
    ),
    Task(
        annotator="0",
        user_id="req38",
        instruction="Acknowledge Isabella Chen's executive bonus approved on October 1 2027: set up compensation COMP10009 (base $300,000, 35% bonus target, $100,000 equity), record review PR10009 (Pending, Q4 2027), and arrange executive-retreat leave LV10009 from October 15 to 20 2027), expand her benefits with BEN4009 and include the modification. Provide her updated profile and compensation history.",
        actions=[
            Action(
                name="AddCompensationRecord",
                kwargs={
                    "compensation_record": {
                        "compensation_id": "COMP10009",
                        "employee_id": "E10001",
                        "base_salary": 300000,
                        "currency": "USD",
                        "bonus_target_pct": 35,
                        "equity_grant": 100000,
                        "effective_date": "2027-10-01",
                    }
                },
            ),
            Action(
                name="AddPerformanceReview",
                kwargs={
                    "performance_review": {
                        "review_id": "PR10009",
                        "employee_id": "E10001",
                        "period_start": "2027-10-01",
                        "period_end": "2027-12-31",
                        "rating": "Pending",
                        "manager_id": "E10001",
                        "summary": "Executive leadership review.",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"notes": "Executive review and bonus 2027-10-01"},
                },
            ),
            Action(
                name="AddLeaveRecord",
                kwargs={
                    "leave_record": {
                        "leave_id": "LV10009",
                        "employee_id": "E10001",
                        "leave_type": "Executive Retreat",
                        "start_date": "2027-10-15",
                        "end_date": "2027-10-20",
                        "status": "Scheduled",
                    }
                },
            ),
            Action(
                name="UpdateEmployee",
                kwargs={
                    "employee_id": "E10001",
                    "updates": {"benefit_plan_ids": ["BEN4001", "BEN4009"]},
                },
            ),
            Action(name="GetCompensationRecords", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
        ],
        outputs=[
            "Executive bonus COMP10009, review PR10009 and retreat leave LV10009 added for Isabella Chen; profile and comp history returned.",
        ],
    ),
    Task(
        annotator="0",
        user_id="req39",
        instruction="Arjun Patel transitions to Sales (DEPT1002) on November 1 2027. Connect compensation package COMP8018 (base $185,000, 18% bonus, $25,000 equity, effective 2027-11-01), arrange onboarding leave LV8020 (November 1 to 10 2027), incorporate review PR8019 (Pending, from 2027-11-01 to 2027-12-31) and document the modification. Return his updated record.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(name="UpdateEmployee", kwargs={"employee_id": "E10004", "updates": {"department_id": "DEPT1002"}}),
            Action(name="AddCompensationRecord", kwargs={"compensation_record": {"compensation_id": "COMP8018", "employee_id": "E10004", "base_salary": 185000, "currency": "USD", "bonus_target_pct": 18, "equity_grant": 25000, "effective_date": "2027-11-01"}}),
            Action(name="AddLeaveRecord", kwargs={"leave_record": {"leave_id": "LV8020", "employee_id": "E10004", "leave_type": "Onboarding", "start_date": "2027-11-01", "end_date": "2027-11-10", "status": "Scheduled"}}),
            Action(name="AddPerformanceReview", kwargs={"performance_review": {"review_id": "PR8019", "employee_id": "E10004", "period_start": "2027-11-01", "period_end": "2027-12-31", "rating": "Pending", "summary": "Sales onboarding review."}}),
            Action(name="UpdateEmployee", kwargs={"employee_id": "E10004", "updates": {"compensation_id": "COMP8018", "performance_review_ids": ["PR5004", "PR5009", "PR8019"], "notes": "Department transfer recorded 2027-11-01."}}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
        ],
        outputs=[
            "Sales transfer complete — compensation COMP8018, leave LV8020, and review PR8019 linked to Arjun Patel's profile.",
        ],
    ),
    Task(
        annotator="0",
        user_id="req40",
        instruction="A number of colleagues still need to sign Remote-Work Policy 101. Highlight E10001-E10006, add compliance reviews PR14001-PR14006 (Pending on 2026-07-10), plan a one-day reminder leave LV14001-LV14006 on 2026-07-15, update their notes accordingly, and summarise the rollout.",
        actions=[
            Action(name="GetEmployee", kwargs={"employee_id": "E10001"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10002"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10003"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10004"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10005"}),
            Action(name="GetEmployee", kwargs={"employee_id": "E10006"}),
            # E10001
            Action(name="AddPerformanceReview", kwargs={"performance_review": {"review_id": "PR14001", "employee_id": "E10001", "period_start": "2026-07-10", "period_end": "2026-07-10", "rating": "Pending", "summary": "Policy 101 acknowledgment."}}),
            Action(name="AddLeaveRecord", kwargs={"leave_record": {"leave_id": "LV14001", "employee_id": "E10001", "leave_type": "Policy Reminder", "start_date": "2026-07-15", "end_date": "2026-07-15", "status": "Scheduled"}}),
            Action(name="UpdateEmployee", kwargs={"employee_id": "E10001", "updates": {"notes": "Remote Work Policy 101 pending acknowledgment."}}),
            # E10002
            Action(name="AddPerformanceReview", kwargs={"performance_review": {"review_id": "PR14002", "employee_id": "E10002", "period_start": "2026-07-10", "period_end": "2026-07-10", "rating": "Pending", "summary": "Policy 101 acknowledgment."}}),
            Action(name="AddLeaveRecord", kwargs={"leave_record": {"leave_id": "LV14002", "employee_id": "E10002", "leave_type": "Policy Reminder", "start_date": "2026-07-15", "end_date": "2026-07-15", "status": "Scheduled"}}),
            Action(name="UpdateEmployee", kwargs={"employee_id": "E10002", "updates": {"notes": "Remote Work Policy 101 pending acknowledgment."}}),
            # E10003
            Action(name="AddPerformanceReview", kwargs={"performance_review": {"review_id": "PR14003", "employee_id": "E10003", "period_start": "2026-07-10", "period_end": "2026-07-10", "rating": "Pending", "summary": "Policy 101 acknowledgment."}}),
            Action(name="AddLeaveRecord", kwargs={"leave_record": {"leave_id": "LV14003", "employee_id": "E10003", "leave_type": "Policy Reminder", "start_date": "2026-07-15", "end_date": "2026-07-15", "status": "Scheduled"}}),
            Action(name="UpdateEmployee", kwargs={"employee_id": "E10003", "updates": {"notes": "Remote Work Policy 101 pending acknowledgment."}}),
            # E10004
            Action(name="AddPerformanceReview", kwargs={"performance_review": {"review_id": "PR14004", "employee_id": "E10004", "period_start": "2026-07-10", "period_end": "2026-07-10", "rating": "Pending", "summary": "Policy 101 acknowledgment."}}),
            Action(name="AddLeaveRecord", kwargs={"leave_record": {"leave_id": "LV14004", "employee_id": "E10004", "leave_type": "Policy Reminder", "start_date": "2026-07-15", "end_date": "2026-07-15", "status": "Scheduled"}}),
            Action(name="UpdateEmployee", kwargs={"employee_id": "E10004", "updates": {"notes": "Remote Work Policy 101 pending acknowledgment."}}),
            # E10005
            Action(name="AddPerformanceReview", kwargs={"performance_review": {"review_id": "PR14005", "employee_id": "E10005", "period_start": "2026-07-10", "period_end": "2026-07-10", "rating": "Pending", "summary": "Policy 101 acknowledgment."}}),
            Action(name="AddLeaveRecord", kwargs={"leave_record": {"leave_id": "LV14005", "employee_id": "E10005", "leave_type": "Policy Reminder", "start_date": "2026-07-15", "end_date": "2026-07-15", "status": "Scheduled"}}),
            Action(name="UpdateEmployee", kwargs={"employee_id": "E10005", "updates": {"notes": "Remote Work Policy 101 pending acknowledgment."}}),
            # E10006
            Action(name="AddPerformanceReview", kwargs={"performance_review": {"review_id": "PR14006", "employee_id": "E10006", "period_start": "2026-07-10", "period_end": "2026-07-10", "rating": "Pending", "summary": "Policy 101 acknowledgment."}}),
            Action(name="AddLeaveRecord", kwargs={"leave_record": {"leave_id": "LV14006", "employee_id": "E10006", "leave_type": "Policy Reminder", "start_date": "2026-07-15", "end_date": "2026-07-15", "status": "Scheduled"}}),
            Action(name="UpdateEmployee", kwargs={"employee_id": "E10006", "updates": {"notes": "Remote Work Policy 101 pending acknowledgment."}}),
        ],
        outputs=[
            "Remote-Work Policy reminder scheduled — reviews PR14001-PR14006 and leaves LV14001-LV14006 created; notes updated for all flagged employees.",
        ],
    ),
]
