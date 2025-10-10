from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="training_expense_coordinator",
        instruction="""
        You are emp_data_01. You attended an ML conference on June 15, 2025 and paid $1200 for registration and workshop
        fees. You have the receipt and want to submit this for reimbursement under the training category for project
        proj_ai_01. You are submitting the reimbursement on June 17, 2025 and the reimbursement description is
        'ML conference registration and workshop fees'. Before submitting, you should check your reimbursement history,
        only submit the reimbursement if the total value of your reimbursements claimed is less then 1500.
        After submitting, check your reimbursement history for this fiscal year to see how much you've claimed.
        """,
        actions=[
            Action(
                name="get_employee_reimbursement_history",
                kwargs={"employee_id": "emp_data_01", "fiscal_year": 2025},
            ),
            Action(
                name="submit_reimbursement",
                kwargs={
                    "employee_id": "emp_data_01",
                    "expense_date": "2025-06-15T00:00:00Z",
                    "submission_date": "2025-06-17T00:00:00Z",
                    "amount": 1200,
                    "description": "ML conference registration and workshop fees",
                    "category": "training",
                    "receipt_provided": True,
                    "project_id": "proj_ai_01",
                },
            ),
            Action(
                name="get_employee_reimbursement_history",
                kwargs={"employee_id": "emp_data_01", "fiscal_year": 2025},
            ),
        ],
        outputs=['"total_reimbursements": 2400'],
    ),
    Task(
        annotator="0",
        user_id="certification_expense_validator",
        instruction="""
        You are employee emp_devops_02. You need to validate an expense submission for yourself on March 25, 2024 for project
        proj_enterprise_01 for $800 in the software_licenses category from sprint sprint_002. If the validation passes,
        submit the reimbursement with the description 'Kubernetes certification exam' and receipt provided. Finally,
        check your expense history for fiscal year 2024 and print your total reimbursements.
        """,
        actions=[
            Action(
                name="validate_expense_submission",
                kwargs={
                    "employee_id": "emp_devops_02",
                    "project_id": "proj_enterprise_01",
                    "amount": 800,
                    "expense_date": "2024-03-25T00:00:00Z",
                    "category": "software_licenses",
                    "sprint_id": "sprint_002",
                    "task_id": None,
                },
            ),
            Action(
                name="submit_reimbursement",
                kwargs={
                    "employee_id": "emp_devops_02",
                    "expense_date": "2024-03-25T00:00:00Z",
                    "amount": 800,
                    "description": "Kubernetes certification exam",
                    "category": "software_licenses",
                    "receipt_provided": True,
                    "project_id": "proj_enterprise_01",
                },
            ),
            Action(
                name="get_employee_expense_history",
                kwargs={"employee_id": "emp_devops_02", "fiscal_year": 2024},
            ),
        ],
        outputs=['"total_reimbursements": 1050'],
    ),
    Task(
        annotator="0",
        user_id="analytics_budget_monitor",
        instruction="You are employee emp_data_01 from the data team. First, check the team budget status for team_analytics_01 including member breakdown for fiscal year 2024. Then calculate your cost rate with overhead included. If your weekly cost is over $5000, create a financial alert for budget overrun on project proj_ai_01 with a threshold of 90% to notify yourself and emp_pm_04. Finally, get the financial report for project proj_ai_01 for fiscal year 2024.",
        actions=[
            Action(
                name="get_team_budget_status",
                kwargs={
                    "team_id": "team_analytics_01",
                    "include_member_breakdown": True,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="calculate_employee_cost_rate",
                kwargs={"employee_id": "emp_data_01", "include_overhead": True},
            ),
            Action(
                name="create_financial_alert",
                kwargs={
                    "alert_type": "budget_overrun",
                    "entity_type": "project",
                    "entity_id": "proj_ai_01",
                    "threshold_value": 90,
                    "notify_list": ["emp_data_01", "emp_pm_04"],
                },
            ),
            Action(
                name="get_financial_report",
                kwargs={
                    "report_type": "project",
                    "entity_id": "proj_ai_01",
                    "fiscal_year": 2024,
                },
            ),
        ],
        outputs=[
            '"budget_utilization": 0.0',
            '"weekly_cost": 9072.0',
            '"utilization_percentage": 80.0',
        ],
    ),
    Task(
        annotator="0",
        user_id="analytics_team_coordinator",
        instruction="""
        You are Rachel Green, employee ID emp_analyst_02, working on the Analytics team. You attended a data
        visualization workshop on June 25, 2025 that cost $550 and have the receipt. First check your team's budget
        status for team_analytics_01 for fiscal year 2024 with member breakdown. If the team's budget utilization is
        over 75%, create a budget alert for project proj_insights_01 with an 85% threshold to notify yourself and
        David Kim (emp_analyst_01). Then validate if you can submit this $550 training expense for project
        proj_insights_01. If validation passes, submit the reimbursement. Finally, check your total reimbursement
        history for fiscal year 2025 and output the total of reimbursement claimed.
        """,
        actions=[
            Action(
                name="get_team_budget_status",
                kwargs={
                    "team_id": "team_analytics_01",
                    "include_member_breakdown": True,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="validate_expense_submission",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_insights_01",
                    "amount": 550,
                    "expense_date": "2025-06-25T00:00:00Z",
                    "category": "training",
                    "sprint_id": None,
                    "task_id": None,
                },
            ),
            Action(
                name="submit_reimbursement",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "expense_date": "2025-06-25T00:00:00Z",
                    "amount": 550,
                    "description": "data visualization workshop",
                    "category": "training",
                    "receipt_provided": True,
                    "project_id": "proj_insights_01",
                },
            ),
            Action(
                name="get_employee_reimbursement_history",
                kwargs={"employee_id": "emp_analyst_02", "fiscal_year": 2025},
            ),
        ],
        outputs=['"total_reimbursements": 550'],
    ),
    Task(
        annotator="0",
        user_id="project_optimization_specialist",
        instruction="""
        You're reviewing Q1 performance data. Sprint sprint_001 mentioned needing contractor resources in its
        retrospective. First, reconcile expenses for sprint_001. Then, create a budget alert named 'Analytics Project Budget
        Alert' for project proj_reporting_01 with 90%
        threshold notifying emp_analyst_01 and emp_analyst_02. Then get the project financial report for project
        proj_reporting_01 for fiscal year 2024. Output the total budget and spent value.
        """,
        actions=[
            Action(
                name="reconcile_sprint_expenses", kwargs={"sprint_id": "sprint_001"}
            ),
            Action(
                name="create_budget_threshold_alert",
                kwargs={
                    "project_id": "proj_reporting_01",
                    "threshold_percentage": 90,
                    "alert_recipients": ["emp_analyst_01", "emp_analyst_02"],
                    "alert_name": "Analytics Project Budget Alert",
                },
            ),
            Action(
                name="get_financial_report",
                kwargs={
                    "report_type": "project",
                    "entity_id": "proj_reporting_01",
                    "fiscal_year": 2024,
                },
            ),
        ],
        outputs=['"total_budget": 450000', '"spent": 185000'],
    ),
    Task(
        annotator="0",
        user_id="cost_efficiency_analyst",
        instruction="You're analyzing cost efficiency across projects. First calculate the project cost for proj_ai_01 including planned costs with no specific as_of_date. Then get employee emp_data_01's cost by project for proj_ai_01 including expenses. If the employee's total cost is less than $30000, request a budget modification for proj_ai_01 to increase by $75000 citing 'Data scientist costs exceeding projections - ML expertise critical for project success' as emp_pm_04 for fiscal year 2024. Next calculate employee cost rate for emp_data_01 with overhead. Finally, create a budget from velocity for proj_mobile_01 targeting 200 story points with 15% buffer.",
        actions=[
            Action(
                name="calculate_project_cost",
                kwargs={
                    "project_id": "proj_ai_01",
                    "include_planned": True,
                    "as_of_date": None,
                },
            ),
            Action(
                name="get_employee_cost_by_project",
                kwargs={
                    "employee_id": "emp_data_01",
                    "project_id": "proj_ai_01",
                    "include_expenses": True,
                },
            ),
            Action(
                name="request_budget_modification",
                kwargs={
                    "project_id": "proj_ai_01",
                    "modification_amount": 75000,
                    "modification_type": "increase",
                    "justification": "Data scientist costs exceeding projections - ML expertise critical for project success",
                    "requestor_id": "emp_pm_04",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="calculate_employee_cost_rate",
                kwargs={"employee_id": "emp_data_01", "include_overhead": True},
            ),
            Action(
                name="create_budget_from_velocity",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_story_points": 200,
                    "buffer_percentage": 15,
                },
            ),
        ],
        outputs=[
            '"total": 25000',
            '"status": "pending_approval"',
            '"total_budget": 115000.0',
        ],
    ),
    Task(
        annotator="0",
        user_id="budget_planning_coordinator",
        instruction="""
        You are coordinating budget planning for Q3. Check the current utilization for Sarah Thompson (emp_devops_04)
        and calculate her cost rate including overhead. If her utilization is below 80%, create a new $2,200,000 budget
        for the cloud migration project proj_cloud_01 (critical project) for fiscal year 2024 with categories: infrastructure $1,100,000,
        development $770,000, and contingency $330,000. Set up a 90% budget alert for the project with the name
        'Cloud Migration Budget Alert - 90% Threshold' notifying emp_devops_04 and emp_pm_04.
        Then generate a project financial report for proj_cloud_01 for fiscal year 2024 and tell me the utilization details.
        """,
        actions=[
            Action(
                name="calculate_employee_cost_rate",
                kwargs={"employee_id": "emp_devops_04", "include_overhead": True},
            ),
            Action(
                name="create_project_budget",
                kwargs={
                    "project_id": "proj_cloud_01",
                    "fiscal_year": 2024,
                    "total_budget": 2200000,
                    "budget_categories": {
                        "infrastructure": 1100000,
                        "development": 770000,
                        "contingency": 330000,
                    },
                },
            ),
            Action(
                name="create_budget_threshold_alert",
                kwargs={
                    "project_id": "proj_cloud_01",
                    "threshold_percentage": 90,
                    "alert_recipients": ["emp_devops_04", "emp_pm_04"],
                    "alert_name": "Cloud Migration Budget Alert - 90% Threshold",
                },
            ),
            Action(
                name="get_financial_report",
                kwargs={
                    "report_type": "project",
                    "entity_id": "proj_cloud_01",
                    "fiscal_year": 2024,
                },
            ),
        ],
        outputs=['"utilization_percentage": 60.0', '"utilization_rate": 0.0'],
    ),
    Task(
        annotator="0",
        user_id="conference_reimbursement_checker",
        instruction="""
        You are emp_dev_03. You recently attended the Data Science Strategy Summit on July 10, 2024, and incurred
        an expense of $245 covering the registration and hands-on workshops. You have a receipt and wish to submit this
        reimbursement under the training category for project proj_mobile_01. You are submitting the reimbursement on
        July 12, 2024, with the following description: 'Data Science Summit registration and workshop participation'.
        Before proceeding, check your reimbursement history for the fiscal year 2024. Only submit the reimbursement if
        your total claimed reimbursements are currently less than $500. Also, validate the expense before reimbursement
        submission, you can set the parameters: sprint ID and task ID as None. After submission, verify the updated reimbursement
        total for this fiscal year to confirm the new amount claimed.

        """,
        actions=[
            Action(
                name="get_employee_reimbursement_history",
                kwargs={"employee_id": "emp_dev_03", "fiscal_year": 2024},
            ),
            Action(
                name="validate_expense_submission",
                kwargs={
                    "employee_id": "emp_dev_03",
                    "project_id": "proj_mobile_01",
                    "amount": 245,
                    "expense_date": "2024-07-10T00:00:00Z",
                    "category": "training",
                    "sprint_id": None,
                    "task_id": None,
                },
            ),
            Action(
                name="submit_reimbursement",
                kwargs={
                    "employee_id": "emp_dev_03",
                    "expense_date": "2024-07-10T00:00:00Z",
                    "submission_date": "2024-07-12T00:00:00Z",
                    "amount": 245,
                    "description": "Data Science Summit registration and workshop participation",
                    "category": "training",
                    "receipt_provided": True,
                    "project_id": "proj_mobile_01",
                },
            ),
            Action(
                name="get_employee_reimbursement_history",
                kwargs={"employee_id": "emp_dev_03", "fiscal_year": 2024},
            ),
        ],
        outputs=['"total_reimbursements": 695'],
    ),
    Task(
        annotator="0",
        user_id="expense_compliance_reviewer",
        instruction="""
        You're reviewing expense compliance for the data team. Validate if emp_data_02 can submit an $350 ETL tool
        license expense dated June 22, 2025 for proj_platform_02. Also validate a $299 conference expense for the
        same project and date. If both validations pass, calculate the velocity-budget ratio for team_analytics_01 over
        the last sprint for fiscal year 2024. If the cost per story point exceeds $450, request a budget modification
        to decrease proj_reporting_01 by $25,000 citing 'Optimizing budget allocation based on velocity metrics'
        as emp_analyst_01. Finally, submit the conference expense as a reimbursement for 'Data Engineering Summit 2025
        - ETL best practices conference' attended on June 22, 2025, with receipt provided.
        """,
        actions=[
            Action(
                name="validate_expense_submission",
                kwargs={
                    "employee_id": "emp_data_02",
                    "project_id": "proj_platform_02",
                    "amount": 350,
                    "expense_date": "2025-06-22T00:00:00Z",
                    "category": "software_licenses",
                    "sprint_id": None,
                    "task_id": None,
                },
            ),
            Action(
                name="validate_expense_submission",
                kwargs={
                    "employee_id": "emp_data_02",
                    "project_id": "proj_platform_02",
                    "amount": 299,
                    "expense_date": "2025-06-22T00:00:00Z",
                    "category": "training",
                    "sprint_id": None,
                    "task_id": None,
                },
            ),
            Action(
                name="calculate_velocity_budget_ratio",
                kwargs={
                    "team_id": "team_analytics_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="request_budget_modification",
                kwargs={
                    "project_id": "proj_reporting_01",
                    "modification_amount": 25000,
                    "modification_type": "decrease",
                    "justification": "Optimizing budget allocation based on velocity metrics",
                    "requestor_id": "emp_analyst_01",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="submit_reimbursement",
                kwargs={
                    "employee_id": "emp_data_02",
                    "expense_date": "2025-06-22T00:00:00Z",
                    "amount": 299,
                    "description": "Data Engineering Summit 2025 - ETL best practices conference",
                    "category": "training",
                    "receipt_provided": True,
                    "project_id": "proj_platform_02",
                },
            ),
        ],
        outputs=[
            '"allocation_percentage": 65.0',
            '"valid": true',
            '"status": "pending_approval"',
        ],
    ),
    Task(
        annotator="0",
        user_id="quarterly_efficiency_analyst",
        instruction="""
        You're conducting a Q1 efficiency review. Check budget status for team_mobile_01 and team_dev_01 with member
        breakdowns for fiscal year 2024. If team_mobile_01's budget utilization is below 50%, transfer $75,000 to
        team_dev_01 for fiscal year 2024.
        Then reconcile expenses for sprint_005 which team_dev_01 completed. If the cost per story point from
        reconciliation exceeds $450, create a vendor from the sprint_005 retrospective (retro_002) for
        'TechBoost Consultants' as a development staffing vendor with Net 30 payment terms and team feedback
        indicating performance was needed with development expertise.
        Finally, generate a financial report for the Engineering department for fiscal year 2024 including
        employee costs. Report the department's budget utilization.
        """,
        actions=[
            Action(
                name="get_team_budget_status",
                kwargs={
                    "team_id": "team_mobile_01",
                    "include_member_breakdown": True,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="get_team_budget_status",
                kwargs={
                    "team_id": "team_dev_01",
                    "include_member_breakdown": True,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="transfer_budget_between_teams",
                kwargs={
                    "source_team_id": "team_mobile_01",
                    "target_team_id": "team_dev_01",
                    "transfer_amount": 75000,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="reconcile_sprint_expenses", kwargs={"sprint_id": "sprint_005"}
            ),
            Action(
                name="generate_department_financial_report",
                kwargs={
                    "department_name": "Engineering",
                    "fiscal_year": 2024,
                    "include_employee_costs": True,
                },
            ),
        ],
        outputs=[
            '"budget_utilization": 39.14',
        ],
    ),
    Task(
        annotator="0",
        user_id="sprint_performance_optimizer",
        instruction="""
        You're optimizing sprint performance across teams. Reconcile expenses for sprint_001 (analytics team) and
        sprint_005 (dev team). Compare their cost per story point values, and calculate the project cost for
        proj_reporting_01 including planned costs.
        If the planned total cost is over $100,000, create a cost forecast for proj_reporting_01 for 3 months without
        contingency for fiscal year 2024. Then validate if Tom Anderson (emp_analyst_03) can expense $580 for
        advanced analytics software (Tableau Premium license) for proj_gamma_03, not associated with any specific
        sprint or task. If valid, submit this as a reimbursement for a software purchase made on June 25, 2025 with
        receipt provided. Use 'Advanced analytics software license - Tableau Premium' as the reimbursement submission description.
        Finally output the reimbursement status.
        """,
        actions=[
            Action(
                name="reconcile_sprint_expenses", kwargs={"sprint_id": "sprint_001"}
            ),
            Action(
                name="reconcile_sprint_expenses", kwargs={"sprint_id": "sprint_005"}
            ),
            Action(
                name="calculate_project_cost",
                kwargs={"project_id": "proj_reporting_01", "include_planned": True},
            ),
            Action(
                name="create_cost_forecast",
                kwargs={
                    "project_id": "proj_reporting_01",
                    "forecast_months": 3,
                    "include_contingency": False,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="validate_expense_submission",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_gamma_03",
                    "amount": 580,
                    "expense_date": "2025-06-25T00:00:00Z",
                    "category": "software_licenses",
                    "sprint_id": None,
                    "task_id": None,
                },
            ),
            Action(
                name="submit_reimbursement",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "expense_date": "2025-06-25T00:00:00Z",
                    "amount": 580,
                    "description": "Advanced analytics software license - Tableau Premium",
                    "category": "software_licenses",
                    "receipt_provided": True,
                    "project_id": "proj_gamma_03",
                },
            ),
        ],
        outputs=[
            '"status": "pending_approval"',
        ],
    ),
    Task(
        annotator="0",
        user_id="vendor_sourcing_specialist",
        instruction="""
        You're sourcing vendors based on team needs. Calculate the velocity-budget ratio for team_analytics_01
        looking back the last sprint for fiscal year 2024. If the average cost per story point exceeds $450,
        create a vendor 'DataBoost Analytics' as a staffing vendor with Net 30 payment terms from retrospective
        retro_002 with team feedback capturing their need for better testing data, analytics expertise as
        high priority. Then check the department budget overview for Analytics. If the utilization percentage is over
        40%, transfer $40,000 from team_mobile_01 to team_analytics_01 citing 'Analytics team at capacity -
        vendor support needed' for fiscal year 2024. Finally, get vendor status for vendor_001 to check their
        payment history.
        """,
        actions=[
            Action(
                name="calculate_velocity_budget_ratio",
                kwargs={
                    "team_id": "team_analytics_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="create_vendor_from_retrospective",
                kwargs={
                    "vendor_name": "DataBoost Analytics",
                    "vendor_type": "staffing",
                    "payment_terms": "Net 30",
                    "team_feedback": {
                        "need": "better_testing_data",
                        "expertise": "analytics",
                        "priority": "high",
                    },
                    "retrospective_id": "retro_002",
                },
            ),
            Action(
                name="get_department_budget_overview",
                kwargs={"department_name": "Analytics", "fiscal_year": 2024},
            ),
            Action(
                name="transfer_budget_between_teams",
                kwargs={
                    "source_team_id": "team_mobile_01",
                    "target_team_id": "team_analytics_01",
                    "transfer_amount": 40000,
                    "fiscal_year": 2024,
                },
            ),
            Action(name="get_vendor_status", kwargs={"vendor_id": "vendor_001"}),
        ],
        outputs=[
            '"vendor_id": "vendor_',
            '"utilization_percentage": 41.11',
            '"status": "pending_review"',
            '"late_payments_count": 0',
        ],
    ),
    Task(
        annotator="0",
        user_id="department_budget_coordinator",
        instruction="""
        You are coordinating quarterly budget reviews across departments. First, generate the financial report for
        the Engineering department for fiscal year 2024 including employee costs. If the budget utilization is above
        39%, check the budget utilization of the Analytics department. If the Analytics department budget utilization is below 50%,
        facilitate a budget transfer of $50,000 from team_analytics_01 to team_dev_01, citing 'Quarterly rebalancing -
        engineering at capacity'. After the transfer, create a budget threshold alert at 85% for proj_web_01 notifying
        emp_arch_01 and emp_pm_03, naming it 'Web Portal Budget Alert - Q1 Rebalancing'. Tell me the Analytics
        department's budget utilization and the status of the budget transfer.
        """,
        actions=[
            Action(
                name="generate_department_financial_report",
                kwargs={
                    "department_name": "Engineering",
                    "fiscal_year": 2024,
                    "include_employee_costs": True,
                },
            ),
            Action(
                name="generate_department_financial_report",
                kwargs={
                    "department_name": "Analytics",
                    "fiscal_year": 2024,
                    "include_employee_costs": False,
                },
            ),
            Action(
                name="transfer_budget_between_teams",
                kwargs={
                    "source_team_id": "team_analytics_01",
                    "target_team_id": "team_dev_01",
                    "transfer_amount": 50000,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="create_budget_threshold_alert",
                kwargs={
                    "project_id": "proj_web_01",
                    "threshold_percentage": 85,
                    "alert_recipients": ["emp_arch_01", "emp_pm_03"],
                    "alert_name": "Web Portal Budget Alert - Q1 Rebalancing",
                },
            ),
        ],
        outputs=['"budget_utilization": 41.11', '"status": "pending_finance_review"'],
    ),
    Task(
        annotator="0",
        user_id="sprint_cost_analyst",
        instruction="""
        You're analyzing cost allocation for sprint_002. First, get the sprint financial analysis for sprint_002.
        Then check the cost breakdown for task_003 to see current expenses. Allocate $1,500 for API documentation and
        testing tools - Postman Enterprise to task_003 under software_licenses category. Next, allocate $800 for
        performance monitoring software - New Relic subscription to task_019 under the infrastructure category.
        Finally, calculate the velocity-budget ratio for team_dev_01 looking back the last sprint for fiscal year 2024
        and tell me the average cost per story point.
        """,
        actions=[
            Action(
                name="get_sprint_financial_analysis", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(name="get_task_cost_breakdown", kwargs={"task_id": "task_003"}),
            Action(
                name="allocate_task_expenses",
                kwargs={
                    "task_id": "task_003",
                    "expense_amount": 1500,
                    "expense_category": "software_licenses",
                    "description": "API documentation and testing tools - Postman Enterprise",
                },
            ),
            Action(
                name="allocate_task_expenses",
                kwargs={
                    "task_id": "task_019",
                    "expense_amount": 800,
                    "expense_category": "infrastructure",
                    "description": "Performance monitoring software - New Relic subscription",
                },
            ),
            Action(
                name="calculate_velocity_budget_ratio",
                kwargs={
                    "team_id": "team_dev_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
        ],
        outputs=['"average_cost_per_story_point": 1650.79'],
    ),
    Task(
        annotator="0",
        user_id="resource_optimization_lead",
        instruction="You're planning resource allocation for next quarter. Calculate the velocity-budget ratio for team_analytics_01 looking back 1 sprint for fiscal year 2024. Then request a budget modification for proj_reporting_01 to increase by $100,000 citing 'Insufficient runway for planned features - velocity analysis shows budget depletion' as emp_analyst_01 for fiscal year 2024. Next, get the employee cost breakdown for emp_analyst_02 on proj_reporting_01 including expenses. Create a financial alert for budget overrun on proj_reporting_01 with an 80% threshold value notifying emp_analyst_01 and emp_analyst_02 as a project entity alert. Finally, tell me the team's average velocity and the projected sprints remaining.",
        actions=[
            Action(
                name="calculate_velocity_budget_ratio",
                kwargs={
                    "team_id": "team_analytics_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="request_budget_modification",
                kwargs={
                    "project_id": "proj_reporting_01",
                    "modification_amount": 100000,
                    "modification_type": "increase",
                    "justification": "Insufficient runway for planned features - velocity analysis shows budget depletion",
                    "requestor_id": "emp_analyst_01",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="get_employee_cost_by_project",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_reporting_01",
                    "include_expenses": True,
                },
            ),
            Action(
                name="create_financial_alert",
                kwargs={
                    "alert_type": "budget_overrun",
                    "entity_type": "project",
                    "entity_id": "proj_reporting_01",
                    "threshold_value": 80,
                    "notify_list": ["emp_analyst_01", "emp_analyst_02"],
                },
            ),
        ],
        outputs=['"average_velocity": 28', '"projected_sprints_remaining": 9.6'],
    ),
    Task(
        annotator="0",
        user_id="critical_project_coordinator",
        instruction="""
        You're managing a critical project escalation. First, get the budget status for proj_mobile_01. Then check
        team budget status for team_mobile_01 including member breakdown for fiscal year 2024.
        If proj_web_01 has more than $200,000 available,
        transfer $80,000 from team_dev_01 to team_mobile_01 citing 'Critical mobile launch support - customer deadline
        at risk' for fiscal year 2024. After the transfer, calculate the project ROI for proj_mobile_01 assuming $500,000
        in revenue and $150,000 in cost savings. Tell me the transfer status and the ROI percentage.
        """,
        actions=[
            Action(
                name="get_budget_status",
                kwargs={"project_id": "proj_mobile_01", "fiscal_year": 2024},
            ),
            Action(
                name="get_team_budget_status",
                kwargs={
                    "team_id": "team_mobile_01",
                    "include_member_breakdown": True,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="get_budget_status",
                kwargs={"project_id": "proj_web_01", "fiscal_year": 2024},
            ),
            Action(
                name="transfer_budget_between_teams",
                kwargs={
                    "source_team_id": "team_dev_01",
                    "target_team_id": "team_mobile_01",
                    "transfer_amount": 80000,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="calculate_project_roi",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "revenue_generated": 500000,
                    "cost_savings": 150000,
                    "fiscal_year": 2024,
                },
            ),
        ],
        outputs=['"status": "approved"', '"roi_percentage": 12400.0'],
    ),
    Task(
        annotator="0",
        user_id="compliance_and_training_manager",
        instruction="""
        You're reviewing Q2 expense compliance for the analytics team. Get the expense history for emp_analyst_01 for
        fiscal year 2025. If the average submission delay is more than 1, create a financial
        alert for approval_needed on expense entity_id emp_analyst_01 notifying emp_analyst_01 and emp_pm_04. Then
        validate if emp_analyst_02 can submit a $499 expense for advanced SQL training for proj_insights_01. If
        validation passes and their total expenses for 2025 are under $5,000, submit the reimbursement with the description
        'Advanced SQL masterclass - query optimization and analytics' attended on June 20, 2025 (they have the receipt). Finally,
        get emp_analyst_02's expense history for fiscal year 2025 and tell me the number of late
        submissions.
        """,
        actions=[
            Action(
                name="get_employee_expense_history",
                kwargs={"employee_id": "emp_analyst_01", "fiscal_year": 2025},
            ),
            Action(
                name="create_financial_alert",
                kwargs={
                    "alert_type": "approval_needed",
                    "entity_type": "expense",
                    "entity_id": "emp_analyst_01",
                    "threshold_value": None,
                    "notify_list": ["emp_analyst_01", "emp_pm_04"],
                },
            ),
            Action(
                name="validate_expense_submission",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_insights_01",
                    "amount": 499,
                    "expense_date": "2025-06-20T00:00:00Z",
                    "category": "training",
                    "sprint_id": None,
                    "task_id": None,
                },
            ),
            Action(
                name="get_employee_expense_history",
                kwargs={"employee_id": "emp_analyst_02", "fiscal_year": 2025},
            ),
            Action(
                name="submit_reimbursement",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "expense_date": "2025-06-20T00:00:00Z",
                    "amount": 499,
                    "description": "Advanced SQL masterclass - query optimization and analytics",
                    "category": "training",
                    "receipt_provided": True,
                    "project_id": "proj_insights_01",
                },
            ),
            Action(
                name="get_employee_expense_history",
                kwargs={"employee_id": "emp_analyst_02", "fiscal_year": 2025},
            ),
        ],
        outputs=['"late_submissions": 1'],
    ),
    Task(
        annotator="0",
        user_id="project_phase_planner",
        instruction="""
        You're planning next year's budget for the web portal. First calculate the velocity-budget ratio for
        team_dev_01 looking back 1 sprint for fiscal year 2024. Then validate if emp_dev_05
        can submit a $600 expense for advanced full-stack training on June 22, 2024 for the web project. The
        expense should be categorized as 'training' and is not associated with any specific sprint or task. If
        valid, check the project's budget status for fiscal year 2024. If the total budget exceeds $200,000, create a
        budget threshold alert at 75% for proj_web_01 with the name 'Web Portal 2024 Budget Alert' notifying
        emp_dev_05 and emp_arch_01. Tell me the total budget created and whether the alert was set up.
        """,
        actions=[
            Action(
                name="calculate_velocity_budget_ratio",
                kwargs={
                    "team_id": "team_dev_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="validate_expense_submission",
                kwargs={
                    "employee_id": "emp_dev_05",
                    "project_id": "proj_web_01",
                    "amount": 600,
                    "expense_date": "2024-06-22T00:00:00Z",
                    "category": "training",
                    "sprint_id": None,
                    "task_id": None,
                },
            ),
            Action(
                name="get_budget_status",
                kwargs={"project_id": "proj_web_01", "fiscal_year": 2024},
            ),
            Action(
                name="create_budget_threshold_alert",
                kwargs={
                    "project_id": "proj_web_01",
                    "threshold_percentage": 75,
                    "alert_recipients": ["emp_dev_05", "emp_arch_01"],
                    "alert_name": "Web Portal 2024 Budget Alert",
                },
            ),
        ],
        outputs=['"total_budget":  850000', '"setup_alert": "true"'],
    ),
    Task(
        annotator="0",
        user_id="budget_health_monitor",
        instruction="""
        You're conducting quarterly budget health checks. Get the budget status for proj_ai_01 for fiscal year 2024.
        If the burn rate exceeds 58%, check the budget status for proj_enterprise_01 for fiscal year 2024. If
        proj_enterprise_01 has a healthy budget status with available amount over $1,000,000, request a budget
        modification to decrease proj_enterprise_01 by $200,000 for fiscal year 2024 citing 'Reallocation to critical
        AI project - burn rate exceeding targets' as emp_arch_01. Then calculate employee cost rate for emp_data_01
        including overhead. If their annual rate exceeds $300,000, create a cost forecast for proj_ai_01 for 6 months
        with contingency for fiscal year 2024. Tell me proj_ai_01's burn rate and the budget modification status.
        """,
        actions=[
            Action(
                name="get_budget_status",
                kwargs={"project_id": "proj_ai_01", "fiscal_year": 2024},
            ),
            Action(
                name="get_budget_status",
                kwargs={"project_id": "proj_enterprise_01", "fiscal_year": 2024},
            ),
            Action(
                name="request_budget_modification",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "modification_amount": 200000,
                    "modification_type": "decrease",
                    "justification": "Reallocation to critical AI project - burn rate exceeding targets",
                    "requestor_id": "emp_arch_01",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="calculate_employee_cost_rate",
                kwargs={"employee_id": "emp_data_01", "include_overhead": True},
            ),
            Action(
                name="create_cost_forecast",
                kwargs={
                    "project_id": "proj_ai_01",
                    "forecast_months": 6,
                    "include_contingency": True,
                    "fiscal_year": 2024,
                },
            ),
        ],
        outputs=['"burn_rate": 59.38', '"status": "pending_approval"'],
    ),
    Task(
        annotator="0",
        user_id="accounts_payable_clerk",
        instruction="""
        You need to process pending vendor payments. Get the vendor status for vendor_001. If they have less than 3
        late payments, process payment for invoice inv_001 for $125,000 using wire transfer as emp_finance_01. Then
        get the vendor status for vendor_005. Record a new invoice from
        vendor_005: invoice number SEC-INV-2025-1122 for $35,000, invoice date July 1, 2025, due August 15, 2025.
        Output if the invoice was recorded.
        """,
        actions=[
            Action(name="get_vendor_status", kwargs={"vendor_id": "vendor_001"}),
            Action(
                name="process_vendor_payment",
                kwargs={
                    "invoice_id": "inv_001",
                    "payment_amount": 125000,
                    "payment_method": "wire",
                    "processor_id": "emp_finance_01",
                },
            ),
            Action(name="get_vendor_status", kwargs={"vendor_id": "vendor_005"}),
            Action(
                name="record_invoice",
                kwargs={
                    "vendor_id": "vendor_005",
                    "po_number": None,
                    "invoice_number": "SEC-INV-2025-1122",
                    "amount": 35000,
                    "invoice_date": "2025-07-01T00:00:00Z",
                    "due_date": "2025-08-15T00:00:00Z",
                },
            ),
        ],
        outputs=['"invoice_recorded": true'],
    ),
    Task(
        annotator="0",
        user_id="project_budget_analyst",
        instruction="""
        You're reviewing project costs for potential overruns. Calculate the project cost for proj_enterprise_01
        including planned costs. If the total actual cost exceeds $50,000, request a budget modification to
        increase the budget by $300,000 citing 'Actual costs exceeding projections - additional resources needed
        for critical path' as emp_arch_01 for fiscal year 2024. Then get the project financial report for
        proj_enterprise_01 for fiscal year 2024. Tell me the total project cost and the modification request status.
        """,
        actions=[
            Action(
                name="calculate_project_cost",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "include_planned": True,
                    "as_of_date": None,
                },
            ),
            Action(
                name="request_budget_modification",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "modification_amount": 300000,
                    "modification_type": "increase",
                    "justification": "Actual costs exceeding projections - additional resources needed for critical path",
                    "requestor_id": "emp_arch_01",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="get_financial_report",
                kwargs={
                    "report_type": "project",
                    "entity_id": "proj_enterprise_01",
                    "fiscal_year": 2024,
                },
            ),
        ],
        outputs=['"total": 51300', '"status": "pending_approval"'],
    ),
    Task(
        annotator="0",
        user_id="vendor_compliance_officer",
        instruction="""
        You're reviewing vendor payment compliance. Get the status for vendor_005. Validate a purchase order PO-2024-010
        for vendor_005 on proj_enterprise_01
        for $50,000 for security consulting and assessment services for fiscal year 2024. If validation shows no
        warnings, create a financial alert for payment_due on vendor vendor_005 with a 3-day threshold notifying
        emp_finance_01 and emp_finance_02. Tell me how many late payments the vendor has.
        """,
        actions=[
            Action(name="get_vendor_status", kwargs={"vendor_id": "vendor_005"}),
            Action(
                name="validate_purchase_order",
                kwargs={
                    "po_number": "PO-2024-010",
                    "vendor_id": "vendor_005",
                    "project_id": "proj_enterprise_01",
                    "amount": 50000,
                    "description": "Security consulting and assessment services",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="create_financial_alert",
                kwargs={
                    "alert_type": "payment_due",
                    "entity_type": "vendor",
                    "entity_id": "vendor_005",
                    "threshold_value": 3,
                    "notify_list": ["emp_finance_01", "emp_finance_02"],
                },
            ),
        ],
        outputs=['"late_payments_count": 1'],
    ),
    Task(
        annotator="0",
        user_id="cost_allocation_specialist",
        instruction="You're allocating shared cloud infrastructure costs. Get the project financial report for proj_ai_01 for fiscal year 2024. If the utilization rate is above 39%, allocate expense exp_002 ($25,000 cloud infrastructure) across projects: 50% to proj_ai_01 ($12,500), 30% to proj_enterprise_01 ($7,500), and 20% to proj_platform_02 ($5,000) as emp_finance_01 for fiscal year 2024. Then calculate the project ROI for proj_ai_01 with $180,000 revenue and $45,000 cost savings. Tell me the allocation status and proj_ai_01's ROI percentage.",
        actions=[
            Action(
                name="get_financial_report",
                kwargs={
                    "report_type": "project",
                    "entity_id": "proj_ai_01",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="allocate_costs",
                kwargs={
                    "expense_id": "exp_002",
                    "allocation_splits": [
                        {"project_id": "proj_ai_01", "percentage": 50, "amount": 12500},
                        {
                            "project_id": "proj_enterprise_01",
                            "percentage": 30,
                            "amount": 7500,
                        },
                        {
                            "project_id": "proj_platform_02",
                            "percentage": 20,
                            "amount": 5000,
                        },
                    ],
                    "allocator_id": "emp_finance_01",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="calculate_project_roi",
                kwargs={
                    "project_id": "proj_ai_01",
                    "revenue_generated": 180000,
                    "cost_savings": 45000,
                    "fiscal_year": 2024,
                },
            ),
        ],
        outputs=['"status": "completed"', '"roi_percentage": 800.0'],
    ),
    Task(
        annotator="0",
        user_id="training_reimbursement_coordinator",
        instruction="""
        You're processing Q2 training reimbursements. Get the employee expense history for emp_devops_02 for fiscal
        year 2025. If their total expenses are under $3,000, submit a reimbursement for a Kubernetes CKA certification
        exam taken on June 18, 2025 for $400 under the professional_development category for proj_platform_02 with
        receipt provided. Then validate if emp_devops_04 can submit a $575 expense for Docker training on June 23, 2025
        for proj_platform_02 (no sprint_id or task_id associated). If valid, submit that reimbursement as well for a
        Docker advanced administration course with receipt provided. Finally, calculate the employee cost rate for
        emp_devops_04 with overhead. Tell me the number of reimbursements successfully submitted and emp_devops_04's
        weekly rate.
        """,
        actions=[
            Action(
                name="get_employee_expense_history",
                kwargs={"employee_id": "emp_devops_02", "fiscal_year": 2025},
            ),
            Action(
                name="submit_reimbursement",
                kwargs={
                    "employee_id": "emp_devops_02",
                    "expense_date": "2025-06-18T00:00:00Z",
                    "amount": 400,
                    "description": "Kubernetes CKA certification exam",
                    "category": "professional_development",
                    "receipt_provided": True,
                    "project_id": "proj_platform_02",
                },
            ),
            Action(
                name="validate_expense_submission",
                kwargs={
                    "employee_id": "emp_devops_04",
                    "project_id": "proj_platform_02",
                    "amount": 575,
                    "expense_date": "2025-06-23T00:00:00Z",
                    "category": "training",
                    "sprint_id": None,
                    "task_id": None,
                },
            ),
            Action(
                name="submit_reimbursement",
                kwargs={
                    "employee_id": "emp_devops_04",
                    "expense_date": "2025-06-23T00:00:00Z",
                    "amount": 575,
                    "description": "Docker advanced administration course",
                    "category": "training",
                    "receipt_provided": True,
                    "project_id": "proj_platform_02",
                },
            ),
            Action(
                name="calculate_employee_cost_rate",
                kwargs={"employee_id": "emp_devops_04", "include_overhead": True},
            ),
        ],
        outputs=["2", '"weekly_rate": 6480.0'],
    ),
    Task(
        annotator="0",
        user_id="portfolio_financial_analyst",
        instruction="""
        You're conducting quarterly project reviews. Get the financial report for proj_reporting_01 for fiscal year 2024.
        If proj_reporting_01's utilization rate is below 50%, transfer $35,000 from team_analytics_01 to
        team_mobile_01 for fiscal year 2024.
        After the transfer, create a budget threshold alert at 95% for proj_mobile_01 with the alert name
        'Mobile Launch Critical Budget Alert' notifying emp_pm_03 and emp_dev_03. Finally, calculate the project cost
        for proj_mobile_01 including planned costs. Tell me proj_mobile_01's total actual cost and total planned cost.
        """,
        actions=[
            Action(
                name="get_financial_report",
                kwargs={
                    "report_type": "project",
                    "entity_id": "proj_reporting_01",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="transfer_budget_between_teams",
                kwargs={
                    "source_team_id": "team_analytics_01",
                    "target_team_id": "team_mobile_01",
                    "transfer_amount": 35000,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="create_budget_threshold_alert",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "threshold_percentage": 95,
                    "alert_recipients": ["emp_pm_03", "emp_dev_03"],
                    "alert_name": "Mobile Launch Critical Budget Alert",
                },
            ),
            Action(
                name="calculate_project_cost",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "include_planned": True,
                    "as_of_date": None,
                },
            ),
        ],
        outputs=['"total_actual_cost": 5200', '"total_planned_cost": 146250.0'],
    ),
    Task(
        annotator="0",
        user_id="vendor_payment_monitor",
        instruction="You're setting up automated vendor monitoring. Get the vendor status for vendor_001. If they have zero late payments, process payment for invoice inv_001 for $125,000 using ach as emp_finance_02. After payment, create a financial alert for payment_due on vendor vendor_001 with a 7-day threshold notifying emp_finance_01 and emp_finance_02. Then get the employee cost by project for emp_data_01 on proj_ai_01 including expenses. If their total cost exceeds $20,000, create another alert for budget_overrun on project proj_ai_01 with 85% threshold notifying emp_data_01 and emp_pm_04. Tell me the number of alerts created and emp_data_01's total cost.",
        actions=[
            Action(name="get_vendor_status", kwargs={"vendor_id": "vendor_001"}),
            Action(
                name="process_vendor_payment",
                kwargs={
                    "invoice_id": "inv_001",
                    "payment_amount": 125000,
                    "payment_method": "ach",
                    "processor_id": "emp_finance_02",
                },
            ),
            Action(
                name="create_financial_alert",
                kwargs={
                    "alert_type": "payment_due",
                    "entity_type": "vendor",
                    "entity_id": "vendor_001",
                    "threshold_value": 7,
                    "notify_list": ["emp_finance_01", "emp_finance_02"],
                },
            ),
            Action(
                name="get_employee_cost_by_project",
                kwargs={
                    "employee_id": "emp_data_01",
                    "project_id": "proj_ai_01",
                    "include_expenses": True,
                },
            ),
            Action(
                name="create_financial_alert",
                kwargs={
                    "alert_type": "budget_overrun",
                    "entity_type": "project",
                    "entity_id": "proj_ai_01",
                    "threshold_value": 85,
                    "notify_list": ["emp_data_01", "emp_pm_04"],
                },
            ),
        ],
        outputs=["2", '"total_cost": 25000'],
    ),
    Task(
        annotator="0",
        user_id="finance_transfer_approver",
        instruction="""
        You're managing emergency budget reallocation. Get the team budget status for team_mobile_01 for fiscal year
        2024. Transfer $50,000 from team_analytics_01 to team_mobile_01 citing
        'Emergency support - mobile launch critical path' for fiscal year 2024. After creating the transfer, get the
        department budget overview for Engineering for fiscal year 2024. If the utilization percentage is above 35%,
        create a financial alert for budget_overrun on entity_type department entity_id dept_eng with 90% threshold
        notifying emp_arch_01 and emp_pm_03. Tell me the transfer status and whether an alert was created.
        """,
        actions=[
            Action(
                name="get_team_budget_status",
                kwargs={
                    "team_id": "team_mobile_01",
                    "include_member_breakdown": False,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="transfer_budget_between_teams",
                kwargs={
                    "source_team_id": "team_analytics_01",
                    "target_team_id": "team_mobile_01",
                    "transfer_amount": 50000,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="get_department_budget_overview",
                kwargs={"department_name": "Engineering", "fiscal_year": 2024},
            ),
            Action(
                name="create_financial_alert",
                kwargs={
                    "alert_type": "budget_overrun",
                    "entity_type": "department",
                    "entity_id": "dept_eng",
                    "threshold_value": 90,
                    "notify_list": ["emp_arch_01", "emp_pm_03"],
                },
            ),
        ],
        outputs=['"status": "pending_finance_review"', '"alert_id": "alert_'],
    ),
    Task(
        annotator="0",
        user_id="invoice_processing_coordinator",
        instruction="You're processing month-end vendor invoices. Get the vendor status for vendor_004. If they have no outstanding invoices, record a new invoice from them: invoice FDT-2025-2345 for $18,500 with invoice date July 1, 2025 and due July 30, 2025. Then validate a purchase order PO-2024-015 for vendor_004 on proj_web_01 for $25,000 for additional frontend development tools and licenses for fiscal year 2024. If validation shows sufficient funds, record another invoice from vendor_004: invoice FDT-2025-2346 for $25,000 with invoice date July 1, 2025 and due August 15, 2025 for PO-2024-015. Finally, create a payment due alert for vendor_004 with 10-day threshold notifying emp_finance_01. Tell me the first invoice ID and whether the PO validation passed.",
        actions=[
            Action(name="get_vendor_status", kwargs={"vendor_id": "vendor_004"}),
            Action(
                name="record_invoice",
                kwargs={
                    "vendor_id": "vendor_004",
                    "po_number": None,
                    "invoice_number": "FDT-2025-2345",
                    "amount": 18500,
                    "invoice_date": "2025-07-01T00:00:00Z",
                    "due_date": "2025-07-30T00:00:00Z",
                },
            ),
            Action(
                name="validate_purchase_order",
                kwargs={
                    "po_number": "PO-2024-015",
                    "vendor_id": "vendor_004",
                    "project_id": "proj_web_01",
                    "amount": 25000,
                    "description": "Additional frontend development tools and licenses",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="record_invoice",
                kwargs={
                    "vendor_id": "vendor_004",
                    "po_number": "PO-2024-015",
                    "invoice_number": "FDT-2025-2346",
                    "amount": 25000,
                    "invoice_date": "2025-07-01T00:00:00Z",
                    "due_date": "2025-08-15T00:00:00Z",
                },
            ),
            Action(
                name="create_financial_alert",
                kwargs={
                    "alert_type": "payment_due",
                    "entity_type": "vendor",
                    "entity_id": "vendor_004",
                    "threshold_value": 10,
                    "notify_list": ["emp_finance_01"],
                },
            ),
        ],
        outputs=['"invoice_id": "inv_', '"validation_status": "valid"'],
    ),
    Task(
        annotator="0",
        user_id="project_financial_auditor",
        instruction="""
        You're auditing project financials for potential issues. Get the project financial summary for proj_ai_01 for
        fiscal year 2024. If the monthly burn rate exceeds $20,000, calculate the velocity-budget ratio for
        team_analytics_01 (use this team ID even though it's not the project's primary team) looking back 1 sprint
        for fiscal year 2024. If the cost per story point is over $450, request a budget modification for proj_ai_01
        to decrease by $100,000 citing 'Burn rate exceeding projections - cost optimization required' as emp_pm_04 for
        fiscal year 2024. Then create a cost forecast for proj_ai_01 for 3 months without contingency for fiscal year
        2024. Tell me the monthly burn rate and total forecasted cost.
        """,
        actions=[
            Action(
                name="get_project_financial_summary",
                kwargs={"project_id": "proj_ai_01", "fiscal_year": 2024},
            ),
            Action(
                name="calculate_velocity_budget_ratio",
                kwargs={
                    "team_id": "team_analytics_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="request_budget_modification",
                kwargs={
                    "project_id": "proj_ai_01",
                    "modification_amount": 100000,
                    "modification_type": "decrease",
                    "justification": "Burn rate exceeding projections - cost optimization required",
                    "requestor_id": "emp_pm_04",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="create_cost_forecast",
                kwargs={
                    "project_id": "proj_ai_01",
                    "forecast_months": 3,
                    "include_contingency": False,
                    "fiscal_year": 2024,
                },
            ),
        ],
        outputs=['"monthly_burn_rate": 24940.8', '"total_forecasted_cost": 74822.4'],
    ),
    Task(
        annotator="0",
        user_id="staffing_cost_optimizer",
        instruction="""
        You're evaluating staffing costs for project assignments. Calculate the employee cost rate for emp_arch_01
        (senior architect) with overhead. If their annual rate exceeds $350,000, calculate the cost rate for
        emp_analyst_03 (junior analyst) with overhead. If the junior's weekly rate is less than $5,000, validate
        if emp_analyst_03 can submit a $399 expense for analytics training on June 25, 2025 for proj_gamma_03
        without associating it to a specific sprint or task. If valid, submit the reimbursement for an 'Advanced
        analytics and statistics course' with receipt provided. Finally, get emp_analyst_03's expense history for
        2025. Tell me the architect's annual rate and the junior analyst's utilization percentage.
        """,
        actions=[
            Action(
                name="calculate_employee_cost_rate",
                kwargs={"employee_id": "emp_arch_01", "include_overhead": True},
            ),
            Action(
                name="calculate_employee_cost_rate",
                kwargs={"employee_id": "emp_analyst_03", "include_overhead": True},
            ),
            Action(
                name="validate_expense_submission",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_gamma_03",
                    "amount": 399,
                    "expense_date": "2025-06-25T00:00:00Z",
                    "category": "training",
                    "sprint_id": None,
                    "task_id": None,
                },
            ),
            Action(
                name="submit_reimbursement",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "expense_date": "2025-06-25T00:00:00Z",
                    "amount": 399,
                    "description": "Advanced analytics and statistics course",
                    "category": "training",
                    "receipt_provided": True,
                    "project_id": "proj_gamma_03",
                },
            ),
            Action(
                name="get_employee_expense_history",
                kwargs={"employee_id": "emp_analyst_03", "fiscal_year": 2025},
            ),
        ],
        outputs=['"annual_rate": 673920.0', '"utilization_percentage": 60.0'],
    ),
    Task(
        annotator="0",
        user_id="department_rebalancing_analyst",
        instruction="""
        You're optimizing department budgets for Q2. Get the department budget overview for Analytics for fiscal year
        2024. If the utilization percentage is below 60%, get the department overview for Engineering. If Engineering's
        utilization is above 37%, transfer $45,000 from team_analytics_01 to team_dev_01 for fiscal year 2024.
        After the transfer, create a budget threshold alert at 70% for proj_reporting_01 named 'Reporting Project Budget Alert - Post Rebalancing' notifying
        emp_analyst_01 and emp_analyst_02. Finally, tell me Analytics's utilization percentage.
        """,
        actions=[
            Action(
                name="get_department_budget_overview",
                kwargs={"department_name": "Analytics", "fiscal_year": 2024},
            ),
            Action(
                name="get_department_budget_overview",
                kwargs={"department_name": "Engineering", "fiscal_year": 2024},
            ),
            Action(
                name="transfer_budget_between_teams",
                kwargs={
                    "source_team_id": "team_analytics_01",
                    "target_team_id": "team_dev_01",
                    "transfer_amount": 45000,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="create_budget_threshold_alert",
                kwargs={
                    "project_id": "proj_reporting_01",
                    "threshold_percentage": 70,
                    "alert_recipients": ["emp_analyst_01", "emp_analyst_02"],
                    "alert_name": "Reporting Project Budget Alert - Post Rebalancing",
                },
            ),
        ],
        outputs=['"utilization_percentage": 41.11'],
    ),
    Task(
        annotator="0",
        user_id="project_extension_planner",
        instruction="""
        You're planning a potential project extension. Get the budget status for proj_enterprise_01 for fiscal year
        2024. If the utilization rate is below 70%, create a cost forecast for proj_enterprise_01 for 4 months with
        contingency. If the budget exhaustion month is beyond month 3, calculate the employee cost rate for
        emp_devops_02 with overhead. If their weekly rate is below $7,000, request a budget modification for
        proj_enterprise_01 to increase by $250,000 citing 'Project extension approved - 4 month runway needed'
        as emp_arch_01. Tell me the budget utilization rate and the total forecasted cost.
        """,
        actions=[
            Action(
                name="get_budget_status",
                kwargs={"project_id": "proj_enterprise_01", "fiscal_year": 2024},
            ),
            Action(
                name="create_cost_forecast",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "forecast_months": 4,
                    "include_contingency": True,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="calculate_employee_cost_rate",
                kwargs={"employee_id": "emp_devops_02", "include_overhead": True},
            ),
            Action(
                name="request_budget_modification",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "modification_amount": 250000,
                    "modification_type": "increase",
                    "justification": "Project extension approved - 4 month runway needed",
                    "requestor_id": "emp_arch_01",
                    "fiscal_year": 2024,
                },
            ),
        ],
        outputs=[
            '"utilization_rate": 41.67',
            '"total_forecasted_cost": 145747.8',
        ],
    ),
    Task(
        annotator="0",
        user_id="task_efficiency_analyst",
        instruction="""
        You're analyzing task efficiency for cost optimization. Get the task cost breakdown for task_003 (API endpoint
        development). If the cost per story point exceeds $500, get the task cost breakdown for task_012 (permissions
        system). Then calculate the velocity-budget ratio for team_dev_01 looking
        back 1 sprint for fiscal year 2024. If the average cost per story point is above $450, create a financial alert
        (use alert_XXX to alert id and set threshold value as none)
        for approval_needed on entity_type project entity_id proj_web_01 notifying emp_arch_01 and emp_pm_03. Tell me
        task_003's cost per story point and whether an alert was created.
        """,
        actions=[
            Action(name="get_task_cost_breakdown", kwargs={"task_id": "task_003"}),
            Action(name="get_task_cost_breakdown", kwargs={"task_id": "task_012"}),
            Action(
                name="calculate_velocity_budget_ratio",
                kwargs={
                    "team_id": "team_dev_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="create_financial_alert",
                kwargs={
                    "alert_id": "alert_XXX",
                    "alert_type": "approval_needed",
                    "entity_type": "project",
                    "entity_id": "proj_web_01",
                    "threshold_value": None,
                    "notify_list": ["emp_arch_01", "emp_pm_03"],
                },
            ),
        ],
        outputs=['"cost_per_story_point": 940', '"alert_created": "true'],
    ),
    Task(
        annotator="0",
        user_id="procurement_approval_manager",
        instruction="""
        You're processing quarterly vendor purchases. Validate purchase order PO-2024-020 for vendor_003 on
        proj_mobile_01 for $75,000 with description 'Cloud infrastructure and services - Q3' for fiscal year 2024.
        Then get the vendor status for vendor_003. Next, calculate the project cost for proj_mobile_01 including planned
        costs. After that, create a financial alert (use alert_3022e583 for alert ID) for budget_overrun on proj_mobile_01
        with 90% threshold notifying
        emp_pm_03 and emp_arch_01. Finally, record a new invoice (use inv_651be335 for invoice ID) from vendor_003:
        invoice AWS-2025-9876 for $75,000
        with invoice date July 1, 2025 and due date August 30, 2025 for the validated PO. Tell me the validation
        status and whether any warnings were present.
        """,
        actions=[
            Action(
                name="validate_purchase_order",
                kwargs={
                    "po_number": "PO-2024-020",
                    "vendor_id": "vendor_003",
                    "project_id": "proj_mobile_01",
                    "amount": 75000,
                    "description": "Cloud infrastructure and services - Q3",
                    "fiscal_year": 2024,
                },
            ),
            Action(name="get_vendor_status", kwargs={"vendor_id": "vendor_003"}),
            Action(
                name="calculate_project_cost",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "include_planned": True,
                    "as_of_date": None,
                },
            ),
            Action(
                name="create_financial_alert",
                kwargs={
                    "alert_id": "alert_3022e583",
                    "alert_type": "budget_overrun",
                    "entity_type": "project",
                    "entity_id": "proj_mobile_01",
                    "threshold_value": 90,
                    "notify_list": ["emp_pm_03", "emp_arch_01"],
                },
            ),
            Action(
                name="record_invoice",
                kwargs={
                    "vendor_id": "vendor_003",
                    "invoice_id": "inv_651be335",
                    "po_number": "PO-2024-020",
                    "invoice_number": "AWS-2025-9876",
                    "amount": 75000,
                    "invoice_date": "2025-07-01T00:00:00Z",
                    "due_date": "2025-08-30T00:00:00Z",
                },
            ),
        ],
        outputs=['"validation_status": "valid"', '"warnings": []'],
    ),
    Task(
        annotator="0",
        user_id="employee_efficiency_evaluator",
        instruction="""
        You're analyzing employee project efficiency. Get the employee cost by project for emp_devops_02 on
        proj_enterprise_01 including expenses. If their total cost exceeds $2,000, calculate their cost rate
        with overhead. If their annual rate is over $250,000, validate if they can expense $420 for AWS
        certification (professional_development category) on June 24, 2025 for proj_enterprise_01 without
        associating it to a specific sprint or task. If valid, check the project financial summary for
        proj_enterprise_01 for fiscal year 2024. If the weekly burn rate exceeds $5,000, create a financial
        alert for budget_overrun on the project entity proj_enterprise_01 with 92% threshold notifying
        emp_devops_02 and emp_arch_01. Tell me the employee's total cost and the project's remaining budget.
        """,
        actions=[
            Action(
                name="get_employee_cost_by_project",
                kwargs={
                    "employee_id": "emp_devops_02",
                    "project_id": "proj_enterprise_01",
                    "include_expenses": True,
                },
            ),
            Action(
                name="calculate_employee_cost_rate",
                kwargs={"employee_id": "emp_devops_02", "include_overhead": True},
            ),
            Action(
                name="validate_expense_submission",
                kwargs={
                    "employee_id": "emp_devops_02",
                    "project_id": "proj_enterprise_01",
                    "amount": 420,
                    "expense_date": "2025-06-24T00:00:00Z",
                    "category": "professional_development",
                    "sprint_id": None,
                    "task_id": None,
                },
            ),
            Action(
                name="get_project_financial_summary",
                kwargs={"project_id": "proj_enterprise_01", "fiscal_year": 2024},
            ),
            Action(
                name="create_financial_alert",
                kwargs={
                    "alert_type": "budget_overrun",
                    "entity_type": "project",
                    "entity_id": "proj_enterprise_01",
                    "threshold_value": 92,
                    "notify_list": ["emp_devops_02", "emp_arch_01"],
                },
            ),
        ],
        outputs=['"total_cost": 2300', '"remaining_budget": 2625000'],
    ),
    Task(
        annotator="0",
        user_id="sprint_budget_monitor",
        instruction="""
        You're setting up budget alerts based on sprint performance. Reconcile sprint expenses for sprint_005. If the
        total cost is zero, get the sprint financial analysis for sprint_001 instead. If sprint_001's total cost
        exceeds $13000, create a budget threshold alert at 80% for proj_web_01 notifying emp_arch_01 and
        emp_dev_05 with the name 'Web Portal Sprint Performance Alert'. Then get the employee cost by project for
        emp_dev_05 on proj_web_01 including expenses. If their total cost is under $30,000, create another budget
        alert at 70% for proj_api_02 notifying emp_dev_05 and emp_pm_03 with the name 'API Platform Budget Watch'.
        Tell me the number of alerts created and emp_dev_05's total cost.
        """,
        actions=[
            Action(
                name="reconcile_sprint_expenses", kwargs={"sprint_id": "sprint_005"}
            ),
            Action(
                name="get_sprint_financial_analysis", kwargs={"sprint_id": "sprint_001"}
            ),
            Action(
                name="create_budget_threshold_alert",
                kwargs={
                    "project_id": "proj_web_01",
                    "threshold_percentage": 80,
                    "alert_recipients": ["emp_arch_01", "emp_dev_05"],
                    "alert_name": "Web Portal Sprint Performance Alert",
                },
            ),
            Action(
                name="get_employee_cost_by_project",
                kwargs={
                    "employee_id": "emp_dev_05",
                    "project_id": "proj_web_01",
                    "include_expenses": True,
                },
            ),
            Action(
                name="create_budget_threshold_alert",
                kwargs={
                    "project_id": "proj_api_02",
                    "threshold_percentage": 70,
                    "alert_recipients": ["emp_dev_05", "emp_pm_03"],
                    "alert_name": "API Platform Budget Watch",
                },
            ),
        ],
        outputs=["2", '"total_cost": 3200'],
    ),
        Task(
        annotator="0",
        user_id="budget_allocation_specialist",
        instruction="""
         You are responsible for refining the financial planning for proj_insights_01. Begin by reviewing the recent
         performance of team_analytics_01: calculate the velocity-to-budget ratio using the most recent sprint data
         available for fiscal year 2024. With that context, proceed to create a revised budget for proj_insights_01 using
         the identifier budget_XXYYY. This budget applies to fiscal year 2025 and totals $675,000. Allocate it across
         the following categories: $410,000 for analytics, $140,000 for infrastructure, $60,000 for training, and $65,000 for
         contingency. Then, retrieve the annual cost rate for emp_analyst_02, ensuring you include overhead in the calculation.
         If the rate is under $410,000, submit a reimbursement request (ID: rb_XXXYY) with the description 'Excel advanced
         data analysis workshop' attended on June 22, 2025. The amount is $925, categorized under training, with a valid
         receipt, and assigned to proj_insights_01.

        Finally, retrieve the budget status for proj_insights_01 for fiscal year 2025. Report both whether the budget
        creation was successful and the budget health.

        """,
        actions=[
            Action(
                name="calculate_velocity_budget_ratio",
                kwargs={
                    "team_id": "team_analytics_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="create_project_budget",
                kwargs={
                    "project_id": "proj_insights_01",
                    "budget_id": "budget_XXYYY",
                    "fiscal_year": 2025,
                    "total_budget": 675000,
                    "budget_categories": {
                        "analytics": 410000,
                        "infrastructure": 140000,
                        "training": 60000,
                        "contingency": 65000,
                    },
                },
            ),
            Action(
                name="calculate_employee_cost_rate",
                kwargs={"employee_id": "emp_analyst_02", "include_overhead": True},
            ),
            Action(
                name="submit_reimbursement",
                kwargs={
                    "reimbursement_id": "rb_XXXYY",
                    "employee_id": "emp_analyst_02",
                    "expense_date": "2025-06-22T00:00:00Z",
                    "amount": 925,
                    "description": "Excel advanced data analysis workshop",
                    "category": "training",
                    "receipt_provided": True,
                    "project_id": "proj_insights_01",
                },
            ),
            Action(
                name="get_budget_status",
                kwargs={"project_id": "proj_insights_01", "fiscal_year": 2025},
            ),
        ],
        outputs=['"success": true', '"budget_health": "healthy"'],
    ),
    Task(
        annotator="0",
        user_id="project_expansion_strategist",
        instruction="""
        You're evaluating projects for potential expansion based on performance. Calculate the project ROI for
        proj_web_01 with $320,000 revenue and $120,000 cost savings for fiscal year 2024. If the ROI percentage
        exceeds 50%, get the financial report for proj_web_01. If the utilization rate is below 60%, create a budget
        from velocity for proj_web_01 targeting 500 story points with 20% buffer. Then calculate employee cost rate
        for emp_dev_05 including overhead. If their utilization percentage exceeds 100%, create a financial alert for
        approval_needed on entity_type project for proj_web_01 with no threshold value, notifying emp_arch_01 and
        emp_dev_05. Tell me the ROI percentage and whether the project qualifies for expansion.
        """,
        actions=[
            Action(
                name="calculate_project_roi",
                kwargs={
                    "project_id": "proj_web_01",
                    "revenue_generated": 320000,
                    "cost_savings": 120000,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="get_financial_report",
                kwargs={
                    "report_type": "project",
                    "entity_id": "proj_web_01",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="create_budget_from_velocity",
                kwargs={
                    "project_id": "proj_web_01",
                    "target_story_points": 500,
                    "buffer_percentage": 20,
                },
            ),
            Action(
                name="calculate_employee_cost_rate",
                kwargs={"employee_id": "emp_dev_05", "include_overhead": True},
            ),
            Action(
                name="create_financial_alert",
                kwargs={
                    "alert_type": "approval_needed",
                    "entity_type": "project",
                    "entity_id": "proj_web_01",
                    "threshold_value": None,
                    "notify_list": ["emp_arch_01", "emp_dev_05"],
                },
            ),
        ],
        outputs=['"roi_percentage": 6467.16', "true"],
    ),
    Task(
        annotator="0",
        user_id="project_budget_planner",
        instruction="""
        You're establishing budgets for analytics expansion projects. Calculate the velocity-budget ratio for
        team_analytics_01 looking back 1 sprint for fiscal year 2024. Based on the analysis, create a project budget
        for proj_insights_01 (use budget_54S41 for budget ID) for fiscal year 2025 with total budget $650,000 and categories: analytics $400,000,
        infrastructure $150,000, training $50,000, and contingency $50,000. Then get the employee cost rate for
        emp_analyst_02 with overhead. If their annual rate is below $400,000, submit a reimbursement (use rb_asd54 for reimbursement ID) for a Tableau
        advanced data visualization workshop they attended on June 24, 2025 for $950 under the training category
        for project proj_insights_01 (they have the receipt). Finally, get the budget status for proj_insights_01
        for fiscal year 2025. Tell me the budget creation status and the available amount.
        """,
        actions=[
            Action(
                name="calculate_velocity_budget_ratio",
                kwargs={
                    "team_id": "team_analytics_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="create_project_budget",
                kwargs={
                    "project_id": "proj_insights_01",
                    "budget_id": "budget_54S41",
                    "fiscal_year": 2025,
                    "total_budget": 650000,
                    "budget_categories": {
                        "analytics": 400000,
                        "infrastructure": 150000,
                        "training": 50000,
                        "contingency": 50000,
                    },
                },
            ),
            Action(
                name="calculate_employee_cost_rate",
                kwargs={"employee_id": "emp_analyst_02", "include_overhead": True},
            ),
            Action(
                name="submit_reimbursement",
                kwargs={
                    "reimbursement_id": "rb_asd54",
                    "employee_id": "emp_analyst_02",
                    "expense_date": "2025-06-24T00:00:00Z",
                    "amount": 950,
                    "description": "Tableau advanced data visualization workshop",
                    "category": "training",
                    "receipt_provided": True,
                    "project_id": "proj_insights_01",
                },
            ),
            Action(
                name="get_budget_status",
                kwargs={"project_id": "proj_insights_01", "fiscal_year": 2025},
            ),
        ],
        outputs=['"success": true', '"available_amount": 650000'],
    ),
    Task(
        annotator="0",
        user_id="project_variance_analyst",
        instruction="""
        You're analyzing cost variances for critical projects. Calculate the project cost for proj_mobile_01 including
        planned costs without specifying an as_of_date. Get the employee cost by project for emp_dev_03 on proj_mobile_01
        including expenses. If the employee's total cost is over $5,000, request a budget modification for proj_mobile_01 to increase by
        $125,000 for fiscal year 2024 citing 'Actual costs exceeding plan by 20%+ - additional funding required'
        as emp_pm_03. Then create a cost forecast for proj_mobile_01 for 6 months with contingency for fiscal year 2024.
        Tell me the actual total cost and whether the forecast includes contingency.
        """,
        actions=[
            Action(
                name="calculate_project_cost",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "include_planned": True,
                    "as_of_date": None,
                },
            ),
            Action(
                name="get_employee_cost_by_project",
                kwargs={
                    "employee_id": "emp_dev_03",
                    "project_id": "proj_mobile_01",
                    "include_expenses": True,
                },
            ),
            Action(
                name="request_budget_modification",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "modification_amount": 125000,
                    "modification_type": "increase",
                    "justification": "Actual costs exceeding plan by 20%+ - additional funding required",
                    "requestor_id": "emp_pm_03",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="create_cost_forecast",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "forecast_months": 6,
                    "include_contingency": True,
                    "fiscal_year": 2024,
                },
            ),
        ],
        outputs=['"total": 5200', '"includes_contingency": true'],
    ),
]
