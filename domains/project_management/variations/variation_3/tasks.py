from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="training_expense_coordinator",
        instruction="""
        You are emp_data_01. On June 15, 2025, you attended an ML conference and paid $1200 for registration and workshop
        fees. You possess the receipt and wish to submit this for reimbursement under the training category for project
        proj_ai_01. Submit the reimbursement on June 17, 2025 with the description 'ML conference registration and workshop fees'. Prior to submission, verify your reimbursement history, and only submit if the total value of claimed reimbursements is less than 1500.
        Post-submission, review your reimbursement history for this fiscal year to ascertain the total amount you've claimed.
        """,
        actions=[
            Action(
                name="GetEmployeeReimbursementHistory",
                kwargs={"employee_id": "emp_data_01", "fiscal_year": 2025},
            ),
            Action(
                name="SubmitReimbursement",
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
                name="GetEmployeeReimbursementHistory",
                kwargs={"employee_id": "emp_data_01", "fiscal_year": 2025},
            ),
        ],
        outputs=['"total_reimbursements": 2400'],
    ),
    Task(
        annotator="0",
        user_id="certification_expense_validator",
        instruction="""
        You are employee emp_devops_02. Validate an expense submission for yourself dated March 25, 2024 for project
        proj_enterprise_01 for $800 in the software_licenses category from sprint sprint_002. Upon successful validation,
        submit the reimbursement with the description 'Kubernetes certification exam' along with the receipt. Lastly,
        review your expense history for fiscal year 2024 and print your total reimbursements.
        """,
        actions=[
            Action(
                name="ValidateExpenseSubmission",
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
                name="SubmitReimbursement",
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
                name="GetEmployeeExpenseHistory",
                kwargs={"employee_id": "emp_devops_02", "fiscal_year": 2024},
            ),
        ],
        outputs=['"total_reimbursements": 1050'],
    ),
    Task(
        annotator="0",
        user_id="analytics_budget_monitor",
        instruction="As an employee identified as emp_data_01 from the data team, begin by examining the budget status for team_analytics_01, including a breakdown of members for fiscal year 2024. Next, determine your cost rate with the overhead factored in. Should your weekly cost exceed $5000, initiate a financial alert for a budget overrun on project proj_ai_01, setting a threshold at 90% to alert both yourself and emp_pm_04. Conclude by obtaining the financial report for project proj_ai_01 for fiscal year 2024.",
        actions=[
            Action(
                name="GetTeamBudgetStatus",
                kwargs={
                    "team_id": "team_analytics_01",
                    "include_member_breakdown": True,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="CalculateEmployeeCostRate",
                kwargs={"employee_id": "emp_data_01", "include_overhead": True},
            ),
            Action(
                name="CreateFinancialAlert",
                kwargs={
                    "alert_type": "budget_overrun",
                    "entity_type": "project",
                    "entity_id": "proj_ai_01",
                    "threshold_value": 90,
                    "notify_list": ["emp_data_01", "emp_pm_04"],
                },
            ),
            Action(
                name="GetFinancialReport",
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
        Identified as Ashley Martinez, employee ID emp_analyst_02, associated with the Analytics team, you participated in a data visualization workshop on June 25, 2025, incurring a cost of $550, and you possess the receipt. Start by reviewing your team's budget status for team_analytics_01 for fiscal year 2024, with a member breakdown. If the budget utilization by the team surpasses 75%, trigger a budget alert for project proj_insights_01 with a threshold of 85% to notify both yourself and Jason Park (emp_analyst_01). Then, confirm whether you can claim the $550 training expense for project proj_insights_01. Upon successful validation, proceed to submit the reimbursement. Lastly, assess your complete reimbursement history for fiscal year 2025 and present the total reimbursement amount claimed.
        """,
        actions=[
            Action(
                name="GetTeamBudgetStatus",
                kwargs={
                    "team_id": "team_analytics_01",
                    "include_member_breakdown": True,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="ValidateExpenseSubmission",
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
                name="SubmitReimbursement",
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
                name="GetEmployeeReimbursementHistory",
                kwargs={"employee_id": "emp_analyst_02", "fiscal_year": 2025},
            ),
        ],
        outputs=['"total_reimbursements": 550'],
    ),
    Task(
        annotator="0",
        user_id="project_optimization_specialist",
        instruction="""
        You're evaluating Q1 performance figures. Sprint sprint_001 highlighted the need for contractor resources in its
        retrospective. Start by reconciling expenses for sprint_001. Then, set up a budget alert entitled 'Analytics Project Budget
        Alert' for project proj_reporting_01 with a 90%
        threshold, notifying emp_analyst_01 and emp_analyst_02. Subsequent to that, retrieve the project financial report for project
        proj_reporting_01 for the fiscal year 2024. Provide the total budget alongside the amount spent.
        """,
        actions=[
            Action(
                name="ReconcileSprintExpenses", kwargs={"sprint_id": "sprint_001"}
            ),
            Action(
                name="CreateBudgetThresholdAlert",
                kwargs={
                    "project_id": "proj_reporting_01",
                    "threshold_percentage": 90,
                    "alert_recipients": ["emp_analyst_01", "emp_analyst_02"],
                    "alert_name": "Analytics Project Budget Alert",
                },
            ),
            Action(
                name="GetFinancialReport",
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
        instruction="You're examining cost efficiency across various projects. Initiate by computing the project cost for proj_ai_01, including planned costs without specified as_of_date. Afterward, acquire the cost of employee emp_data_01 by project for proj_ai_01, factoring in expenses. Should the employee's total cost be under $30000, initiate a budget modification for proj_ai_01, increasing it by $75000, referencing 'Data scientist costs exceeding projections - ML expertise critical for project success' as emp_pm_04 for the fiscal year 2024. Then, ascertain the employee cost rate for emp_data_01 including overhead. Lastly, devise a budget from velocity for proj_mobile_01 aiming for 200 story points with an additional 15% buffer.",
        actions=[
            Action(
                name="CalculateProjectCost",
                kwargs={
                    "project_id": "proj_ai_01",
                    "include_planned": True,
                    "as_of_date": None,
                },
            ),
            Action(
                name="GetEmployeeCostByProject",
                kwargs={
                    "employee_id": "emp_data_01",
                    "project_id": "proj_ai_01",
                    "include_expenses": True,
                },
            ),
            Action(
                name="RequestBudgetModification",
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
                name="CalculateEmployeeCostRate",
                kwargs={"employee_id": "emp_data_01", "include_overhead": True},
            ),
            Action(
                name="CreateBudgetFromVelocity",
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
        As the coordinator for budget planning in Q3, review the present utilization for Emily Davis (emp_devops_04)
        and compute her cost rate factoring in overhead. Should her utilization fall below 80%, initiate a new $2,200,000
        budget for the cloud migration project proj_cloud_01 (critical project) for the fiscal year 2024 including these categories:
        infrastructure $1,100,000, development $770,000, and contingency $330,000. Implement a 90% budget alert for the project
        named 'Cloud Migration Budget Alert - 90% Threshold' to notify emp_devops_04 and emp_pm_04.
        Subsequently, prepare a financial report for proj_cloud_01 for the fiscal year 2024 and inform me about the utilization specifics.
        """,
        actions=[
            Action(
                name="CalculateEmployeeCostRate",
                kwargs={"employee_id": "emp_devops_04", "include_overhead": True},
            ),
            Action(
                name="CreateProjectBudget",
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
                name="CreateBudgetThresholdAlert",
                kwargs={
                    "project_id": "proj_cloud_01",
                    "threshold_percentage": 90,
                    "alert_recipients": ["emp_devops_04", "emp_pm_04"],
                    "alert_name": "Cloud Migration Budget Alert - 90% Threshold",
                },
            ),
            Action(
                name="GetFinancialReport",
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
        You are identified as emp_dev_03. You recently participated in the Data Science Strategy Summit on July 10, 2024,
        incurring a $245 expense which covers registration and hands-on workshops. You possess a receipt and wish to file
        this reimbursement under the training category for project proj_mobile_01. The submission of the reimbursement
        is dated July 12, 2024, with the description: 'Data Science Summit registration and workshop participation'.
        Prior to submission, review your reimbursement record for the fiscal year 2024. Proceed with the submission only
        if your current total claimed reimbursements are under $500. Additionally, ensure the expense is validated before
        progressing with the reimbursement, setting the parameters: sprint ID and task ID to None. Once submitted, check
        the new total of claimed reimbursements for this fiscal year to confirm the updated amount.

        """,
        actions=[
            Action(
                name="GetEmployeeReimbursementHistory",
                kwargs={"employee_id": "emp_dev_03", "fiscal_year": 2024},
            ),
            Action(
                name="ValidateExpenseSubmission",
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
                name="SubmitReimbursement",
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
                name="GetEmployeeReimbursementHistory",
                kwargs={"employee_id": "emp_dev_03", "fiscal_year": 2024},
            ),
        ],
        outputs=['"total_reimbursements": 695'],
    ),
    Task(
        annotator="0",
        user_id="expense_compliance_reviewer",
        instruction="""
        Oversee the review of expense compliance for the data team. Check whether emp_data_02 is eligible to submit a $350
        ETL tool license expense dated June 22, 2025 for proj_platform_02. Also check a $299 conference expense for the
        same project and date. Upon successful validation of both, compute the velocity-budget ratio for team_analytics_01
        for the last sprint in fiscal year 2024. If the cost per story point surpasses $450, initiate a budget amendment
        to reduce proj_reporting_01 by $25,000, citing 'Optimizing budget allocation based on velocity metrics'
        as emp_analyst_01. Ultimately, file the conference expense as a reimbursement for 'Data Engineering Summit 2025
        - ETL best practices conference' attended on June 22, 2025, providing the receipt.
        """,
        actions=[
            Action(
                name="ValidateExpenseSubmission",
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
                name="ValidateExpenseSubmission",
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
                name="CalculateVelocityBudgetRatio",
                kwargs={
                    "team_id": "team_analytics_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="RequestBudgetModification",
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
                name="SubmitReimbursement",
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
        Manage a Q1 efficiency review. Verify the budget status for team_mobile_01 and team_dev_01 along with member
        breakdowns for fiscal year 2024. If team_mobile_01 has a budget utilization below 50%, allocate $75,000 to
        team_dev_01 for fiscal year 2024.
        Subsequently, reconcile expenses for sprint_005 which team_dev_01 completed. If the reconciliation shows a
        cost per story point exceeding $450, set up a vendor from the sprint_005 retrospective (retro_002) for
        'TechBoost Consultants' as a development staffing vendor with Net 30 payment terms and team feedback
        highlighting the need for development expertise.
        Lastly, compile a financial report for the Engineering department for fiscal year 2024 including
        employee costs. Report on the department's budget utilization.
        """,
        actions=[
            Action(
                name="GetTeamBudgetStatus",
                kwargs={
                    "team_id": "team_mobile_01",
                    "include_member_breakdown": True,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="GetTeamBudgetStatus",
                kwargs={
                    "team_id": "team_dev_01",
                    "include_member_breakdown": True,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="TransferBudgetBetweenTeams",
                kwargs={
                    "source_team_id": "team_mobile_01",
                    "target_team_id": "team_dev_01",
                    "transfer_amount": 75000,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="ReconcileSprintExpenses", kwargs={"sprint_id": "sprint_005"}
            ),
            Action(
                name="GenerateDepartmentFinancialReport",
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
        Your task is to enhance sprint performance across various teams. Handle the reconciliation of expenses for sprint_001 (analytics team) and sprint_005 (dev team). Examine their cost per story point metrics, and determine the total project cost for proj_reporting_01, taking into account the planned expenses.
        If the anticipated total expense surpasses $100,000, arrange a cost projection for proj_reporting_01 over a three-month period without including any contingency for the 2024 fiscal year. Subsequently, assess whether Matthew Wilson (emp_analyst_03) is eligible to expense $580 for advanced analytics software (Tableau Premium license) pertaining to proj_gamma_03, which is not linked to any particular sprint or task. If eligibility is confirmed, proceed to file this as a claim for reimbursement for the software purchased on June 25, 2025, with the receipt attached. Use 'Advanced analytics software license - Tableau Premium' as the description for the reimbursement submission.
        Conclude by providing the status of the reimbursement.
        """,
        actions=[
            Action(
                name="ReconcileSprintExpenses", kwargs={"sprint_id": "sprint_001"}
            ),
            Action(
                name="ReconcileSprintExpenses", kwargs={"sprint_id": "sprint_005"}
            ),
            Action(
                name="CalculateProjectCost",
                kwargs={"project_id": "proj_reporting_01", "include_planned": True},
            ),
            Action(
                name="CreateCostForecast",
                kwargs={
                    "project_id": "proj_reporting_01",
                    "forecast_months": 3,
                    "include_contingency": False,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="ValidateExpenseSubmission",
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
                name="SubmitReimbursement",
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
        Your role involves sourcing vendors according to team requirements. Determine the velocity-budget ratio for team_analytics_01 by reviewing the previous sprint from fiscal year 2024. Should the average cost per story point be greater than $450, establish 'DataBoost Analytics' as a staffing vendor, ensuring Net 30 payment terms based on retrospective retro_002 feedback, reflecting the team's high-priority need for enhanced testing data and analytics expertise. Next, review the department's budget overview for Analytics. If budget utilization exceeds 40%, allocate $40,000 from team_mobile_01 to team_analytics_01, stating 'Analytics team at capacity - vendor support needed' for the same fiscal year. Finally, obtain the vendor status for vendor_001 to inspect their payment history.
        """,
        actions=[
            Action(
                name="CalculateVelocityBudgetRatio",
                kwargs={
                    "team_id": "team_analytics_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="CreateVendorFromRetrospective",
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
                name="GetDepartmentBudgetOverview",
                kwargs={"department_name": "Analytics", "fiscal_year": 2024},
            ),
            Action(
                name="TransferBudgetBetweenTeams",
                kwargs={
                    "source_team_id": "team_mobile_01",
                    "target_team_id": "team_analytics_01",
                    "transfer_amount": 40000,
                    "fiscal_year": 2024,
                },
            ),
            Action(name="GetVendorStatus", kwargs={"vendor_id": "vendor_001"}),
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
        Handle the coordination of quarterly budget reviews across departments. Initially, create the financial report for
        the Engineering department for the fiscal year 2024, ensuring to include employee costs. Should the budget utilization exceed
        39%, verify the Analytics department's budget utilization. If utilization in the Analytics department is under 50%,
        coordinate a budget transfer of $50,000 from team_analytics_01 to team_dev_01, with the reason 'Quarterly rebalancing -
        engineering at capacity'. Following the transfer, establish a budget threshold alert at 85% for proj_web_01, informing
        emp_arch_01 and emp_pm_03, naming it 'Web Portal Budget Alert - Q1 Rebalancing'. Inform me about the Analytics
        department's budget utilization and the progress of the budget transfer.
        """,
        actions=[
            Action(
                name="GenerateDepartmentFinancialReport",
                kwargs={
                    "department_name": "Engineering",
                    "fiscal_year": 2024,
                    "include_employee_costs": True,
                },
            ),
            Action(
                name="GenerateDepartmentFinancialReport",
                kwargs={
                    "department_name": "Analytics",
                    "fiscal_year": 2024,
                    "include_employee_costs": False,
                },
            ),
            Action(
                name="TransferBudgetBetweenTeams",
                kwargs={
                    "source_team_id": "team_analytics_01",
                    "target_team_id": "team_dev_01",
                    "transfer_amount": 50000,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="CreateBudgetThresholdAlert",
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
        You will be examining cost allocation for sprint_002. Initially, obtain the sprint financial analysis for sprint_002.
        Subsequently, verify the cost breakdown for task_003 to ascertain current expenses. Assign $1,500 for API documentation and
        testing tools - Postman Enterprise to task_003 under the software_licenses category. Then, allocate $800 for
        performance monitoring software - New Relic subscription to task_019 in the infrastructure category.
        Lastly, calculate the velocity-budget ratio for team_dev_01 by reviewing the last sprint for the fiscal year 2024
        and provide me with the average cost per story point.
        """,
        actions=[
            Action(
                name="GetSprintFinancialAnalysis", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(name="GetTaskCostBreakdown", kwargs={"task_id": "task_003"}),
            Action(
                name="AllocateTaskExpenses",
                kwargs={
                    "task_id": "task_003",
                    "expense_amount": 1500,
                    "expense_category": "software_licenses",
                    "description": "API documentation and testing tools - Postman Enterprise",
                },
            ),
            Action(
                name="AllocateTaskExpenses",
                kwargs={
                    "task_id": "task_019",
                    "expense_amount": 800,
                    "expense_category": "infrastructure",
                    "description": "Performance monitoring software - New Relic subscription",
                },
            ),
            Action(
                name="CalculateVelocityBudgetRatio",
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
        instruction="You're organizing resource allocation for the upcoming quarter. Calculate the velocity-budget ratio for team_analytics_01 by reviewing the last sprint for fiscal year 2024. Then, initiate a request to increase the budget for proj_reporting_01 by $100,000, using 'Insufficient runway for planned features - velocity analysis shows budget depletion' as the reason from emp_analyst_01 for fiscal year 2024. Following this, obtain the employee cost breakdown for emp_analyst_02 on proj_reporting_01, including their expenses. Establish an alert for budget overrun on proj_reporting_01 at an 80% threshold, notifying emp_analyst_01 and emp_analyst_02 as part of a project entity alert. Lastly, inform me of the team's average velocity and the projected number of sprints remaining.",
        actions=[
            Action(
                name="CalculateVelocityBudgetRatio",
                kwargs={
                    "team_id": "team_analytics_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="RequestBudgetModification",
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
                name="GetEmployeeCostByProject",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_reporting_01",
                    "include_expenses": True,
                },
            ),
            Action(
                name="CreateFinancialAlert",
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
        instruction="""You are supervising a crucial project escalation. Begin by obtaining the budget status for proj_mobile_01. Next, verify the team budget status for team_mobile_01, including a member breakdown for fiscal year 2024. If proj_web_01 has more than $200,000 available, redirect $80,000 from team_dev_01 to team_mobile_01, citing 'Critical mobile launch support - customer deadline at risk' for fiscal year 2024. After completing the transfer, compute the project ROI for proj_mobile_01, presuming $500,000 in revenue and $150,000 in cost savings. Let me know the status of the transfer and the ROI percentage.""",
        actions=[
            Action(
                name="GetBudgetStatus",
                kwargs={"project_id": "proj_mobile_01", "fiscal_year": 2024},
            ),
            Action(
                name="GetTeamBudgetStatus",
                kwargs={
                    "team_id": "team_mobile_01",
                    "include_member_breakdown": True,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="GetBudgetStatus",
                kwargs={"project_id": "proj_web_01", "fiscal_year": 2024},
            ),
            Action(
                name="TransferBudgetBetweenTeams",
                kwargs={
                    "source_team_id": "team_dev_01",
                    "target_team_id": "team_mobile_01",
                    "transfer_amount": 80000,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="CalculateProjectRoi",
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
        Review the Q2 expense compliance for the analytics team. Obtain the expense history for emp_analyst_01 for
        fiscal year 2025. Should the average submission delay exceed 1, generate a financial
        alert for approval_needed on expense entity_id emp_analyst_01, notifying emp_analyst_01 and emp_pm_04. Following that,
        confirm if emp_analyst_02 is eligible to submit a $499 expense for advanced SQL training relevant to proj_insights_01. Provided
        the validation is successful and their total expenses for 2025 remain below $5,000, process the reimbursement with the description
        'Advanced SQL masterclass - query optimization and analytics' attended on June 20, 2025 (receipt is available). Lastly,
        retrieve emp_analyst_02's expense history for fiscal year 2025 and inform me of the number of late
        submissions.
        """,
        actions=[
            Action(
                name="GetEmployeeExpenseHistory",
                kwargs={"employee_id": "emp_analyst_01", "fiscal_year": 2025},
            ),
            Action(
                name="CreateFinancialAlert",
                kwargs={
                    "alert_type": "approval_needed",
                    "entity_type": "expense",
                    "entity_id": "emp_analyst_01",
                    "threshold_value": None,
                    "notify_list": ["emp_analyst_01", "emp_pm_04"],
                },
            ),
            Action(
                name="ValidateExpenseSubmission",
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
                name="GetEmployeeExpenseHistory",
                kwargs={"employee_id": "emp_analyst_02", "fiscal_year": 2025},
            ),
            Action(
                name="SubmitReimbursement",
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
                name="GetEmployeeExpenseHistory",
                kwargs={"employee_id": "emp_analyst_02", "fiscal_year": 2025},
            ),
        ],
        outputs=['"late_submissions": 1'],
    ),
    Task(
        annotator="0",
        user_id="project_phase_planner",
        instruction="""
        Plan the budget for next year's web portal. First, compute the velocity-budget ratio for
        team_dev_01 considering the past 1 sprint for fiscal year 2024. Proceed to verify if emp_dev_05
        is eligible to submit a $600 expense for advanced full-stack training on June 22, 2024 pertinent to the web project. Ensure
        the expense is marked as 'training' and not linked to any specific sprint or task. When validated, examine the project's budget
        status for fiscal year 2024. Should the total budget surpass $200,000, set a
        budget threshold alert at 75% for proj_web_01, naming it 'Web Portal 2024 Budget Alert' and notifying
        emp_dev_05 and emp_arch_01. Let me know the total budget that was established and whether the alert was initiated.
        """,
        actions=[
            Action(
                name="CalculateVelocityBudgetRatio",
                kwargs={
                    "team_id": "team_dev_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="ValidateExpenseSubmission",
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
                name="GetBudgetStatus",
                kwargs={"project_id": "proj_web_01", "fiscal_year": 2024},
            ),
            Action(
                name="CreateBudgetThresholdAlert",
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
        You are executing quarterly budget health assessments. Secure the budget status for proj_ai_01 for the fiscal year 2024.
        Should the burn rate surpass 58%, verify the budget status for proj_enterprise_01 for fiscal year 2024. If
        proj_enterprise_01 shows a healthy budget status with an available amount exceeding $1,000,000, initiate a budget
        modification to lower proj_enterprise_01 by $200,000 for fiscal year 2024, citing 'Reallocation to critical
        AI project - burn rate exceeding targets' as emp_arch_01. Subsequently, compute the employee cost rate for emp_data_01
        including overhead. Should their annual rate top $300,000, devise a cost forecast for proj_ai_01 for a 6-month span
        with contingency for fiscal year 2024. Relay to me proj_ai_01's burn rate and the budget modification status.
        """,
        actions=[
            Action(
                name="GetBudgetStatus",
                kwargs={"project_id": "proj_ai_01", "fiscal_year": 2024},
            ),
            Action(
                name="GetBudgetStatus",
                kwargs={"project_id": "proj_enterprise_01", "fiscal_year": 2024},
            ),
            Action(
                name="RequestBudgetModification",
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
                name="CalculateEmployeeCostRate",
                kwargs={"employee_id": "emp_data_01", "include_overhead": True},
            ),
            Action(
                name="CreateCostForecast",
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
        You must manage pending vendor payments. Retrieve the vendor status for vendor_001. Provided they have fewer than 3
        late payments, handle payment for invoice inv_001 for $125,000 using a wire transfer as emp_finance_01. Following that,
        obtain the vendor status for vendor_005. Record a fresh invoice from
        vendor_005: invoice number SEC-INV-2025-1122 for $35,000, invoice date July 1, 2025, due August 15, 2025.
        Indicate if the invoice was recorded.
        """,
        actions=[
            Action(name="GetVendorStatus", kwargs={"vendor_id": "vendor_001"}),
            Action(
                name="ProcessVendorPayment",
                kwargs={
                    "invoice_id": "inv_001",
                    "payment_amount": 125000,
                    "payment_method": "wire",
                    "processor_id": "emp_finance_01",
                },
            ),
            Action(name="GetVendorStatus", kwargs={"vendor_id": "vendor_005"}),
            Action(
                name="RecordInvoice",
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
        Handle the assessment of project costs to identify potential overruns. Compute the project cost for proj_enterprise_01
        inclusive of planned costs. Should the total actual expenditure surpass $50,000, initiate a budget adjustment to
        augment the budget by $300,000, citing 'Actual costs exceeding projections - additional resources needed
        for critical path' as emp_arch_01 for fiscal year 2024. Subsequently, obtain the project financial report for
        proj_enterprise_01 for fiscal year 2024. Inform me of the total project cost and the status of the modification request.
        """,
        actions=[
            Action(
                name="CalculateProjectCost",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "include_planned": True,
                    "as_of_date": None,
                },
            ),
            Action(
                name="RequestBudgetModification",
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
                name="GetFinancialReport",
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
        Coordinate the review of vendor payment compliance. Retrieve the status of vendor_005. Confirm a purchase order PO-2024-010
        for vendor_005 on proj_enterprise_01
        amounting to $50,000 for security consulting and assessment services for fiscal year 2024. If confirmation reveals no
        warnings, set up a financial alert for payment_due on vendor vendor_005 with a 3-day threshold, notifying
        emp_finance_01 and emp_finance_02. Let me know the number of late payments reported for the vendor.
        """,
        actions=[
            Action(name="GetVendorStatus", kwargs={"vendor_id": "vendor_005"}),
            Action(
                name="ValidatePurchaseOrder",
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
                name="CreateFinancialAlert",
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
        instruction="When partitioning shared cloud infrastructure costs, fetch the project financial report for proj_ai_01 for fiscal year 2024. Should the utilization rate be beyond 39%, distribute expense exp_002 ($25,000 for cloud infrastructure) among projects as follows: 50% to proj_ai_01 ($12,500), 30% to proj_enterprise_01 ($7,500), and 20% to proj_platform_02 ($5,000) using emp_finance_01 for fiscal year 2024. Proceed to compute the project ROI for proj_ai_01 factoring in $180,000 in revenue and $45,000 in cost savings. Inform me of the expense allocation results and the ROI percentage for proj_ai_01.",
        actions=[
            Action(
                name="GetFinancialReport",
                kwargs={
                    "report_type": "project",
                    "entity_id": "proj_ai_01",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="AllocateCosts",
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
                name="CalculateProjectRoi",
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
        instruction="""While handling Q2 training reimbursements, retrieve the employee expense history for emp_devops_02 for fiscal year 2025. If their total expenses fall below $3,000, proceed to file a reimbursement for a Kubernetes CKA certification exam taken on June 18, 2025, costing $400 under the professional_development category for proj_platform_02 with a provided receipt. Next, verify if emp_devops_04 is eligible to file a $575 expense for a Docker training on June 23, 2025, for proj_platform_02 (without any sprint_id or task_id linked). If permissible, process that reimbursement as well for a Docker advanced administration course, ensuring receipt submission. Lastly, determine the employee cost rate for emp_devops_04 including overhead costs. Provide the count of reimbursements successfully processed and the weekly rate for emp_devops_04.""",
        actions=[
            Action(
                name="GetEmployeeExpenseHistory",
                kwargs={"employee_id": "emp_devops_02", "fiscal_year": 2025},
            ),
            Action(
                name="SubmitReimbursement",
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
                name="ValidateExpenseSubmission",
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
                name="SubmitReimbursement",
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
                name="CalculateEmployeeCostRate",
                kwargs={"employee_id": "emp_devops_04", "include_overhead": True},
            ),
        ],
        outputs=["2", '"weekly_rate": 6480.0'],
    ),
    Task(
        annotator="0",
        user_id="portfolio_financial_analyst",
        instruction="""
        Handle quarterly project reviews. Retrieve the financial report for proj_reporting_01 for fiscal year 2024.
        Should proj_reporting_01's utilization rate fall below 50%, relocate $35,000 from team_analytics_01 to
        team_mobile_01 for fiscal year 2024.
        Following the transfer, set up a budget threshold alert at 95% for proj_mobile_01 with the alert title
        'Mobile Launch Critical Budget Alert' to inform emp_pm_03 and emp_dev_03. Subsequently, work out the project cost
        for proj_mobile_01 including planned expenditures. Provide me with the total actual and total planned costs for proj_mobile_01.
        """,
        actions=[
            Action(
                name="GetFinancialReport",
                kwargs={
                    "report_type": "project",
                    "entity_id": "proj_reporting_01",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="TransferBudgetBetweenTeams",
                kwargs={
                    "source_team_id": "team_analytics_01",
                    "target_team_id": "team_mobile_01",
                    "transfer_amount": 35000,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="CreateBudgetThresholdAlert",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "threshold_percentage": 95,
                    "alert_recipients": ["emp_pm_03", "emp_dev_03"],
                    "alert_name": "Mobile Launch Critical Budget Alert",
                },
            ),
            Action(
                name="CalculateProjectCost",
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
        instruction="Coordinate the setup for automated vendor monitoring. Acquire the vendor status for vendor_001. If there are no late payments, proceed with the payment for invoice inv_001 for $125,000 using ach while representing emp_finance_02. Once payment is made, establish a financial alert for payment_due on vendor vendor_001 with a 7-day threshold, notifying emp_finance_01 and emp_finance_02. Next, ascertain the employee cost by project for emp_data_01 on proj_ai_01, including expenses. If their total expenditure surpasses $20,000, initiate another alert for budget_overrun on project proj_ai_01 with an 85% threshold, informing emp_data_01 and emp_pm_04. Inform me of the number of alerts generated and the total cost for emp_data_01.",
        actions=[
            Action(name="GetVendorStatus", kwargs={"vendor_id": "vendor_001"}),
            Action(
                name="ProcessVendorPayment",
                kwargs={
                    "invoice_id": "inv_001",
                    "payment_amount": 125000,
                    "payment_method": "ach",
                    "processor_id": "emp_finance_02",
                },
            ),
            Action(
                name="CreateFinancialAlert",
                kwargs={
                    "alert_type": "payment_due",
                    "entity_type": "vendor",
                    "entity_id": "vendor_001",
                    "threshold_value": 7,
                    "notify_list": ["emp_finance_01", "emp_finance_02"],
                },
            ),
            Action(
                name="GetEmployeeCostByProject",
                kwargs={
                    "employee_id": "emp_data_01",
                    "project_id": "proj_ai_01",
                    "include_expenses": True,
                },
            ),
            Action(
                name="CreateFinancialAlert",
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
        Handle emergency budget reallocation. Obtain the budget status for team_mobile_01 for fiscal year
        2024. Redirect $50,000 from team_analytics_01 to team_mobile_01 with the reason
        'Emergency support - mobile launch critical path' for fiscal year 2024. Once the transfer is executed, acquire the
        department budget overview for Engineering for fiscal year 2024. If the utilization percentage exceeds 35%,
        initiate a financial alert for budget_overrun on entity_type department entity_id dept_eng with a 90% threshold
        notifying emp_arch_01 and emp_pm_03. Inform me about the transfer status and whether an alert was initiated.
        """,
        actions=[
            Action(
                name="GetTeamBudgetStatus",
                kwargs={
                    "team_id": "team_mobile_01",
                    "include_member_breakdown": False,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="TransferBudgetBetweenTeams",
                kwargs={
                    "source_team_id": "team_analytics_01",
                    "target_team_id": "team_mobile_01",
                    "transfer_amount": 50000,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="GetDepartmentBudgetOverview",
                kwargs={"department_name": "Engineering", "fiscal_year": 2024},
            ),
            Action(
                name="CreateFinancialAlert",
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
        instruction="Coordinate month-end vendor invoice processing. Retrieve the vendor status for vendor_004. If there are no outstanding invoices, log a new invoice from them: invoice FDT-2025-2345 for $18,500 with invoice date July 1, 2025 and due July 30, 2025. Subsequently, verify purchase order PO-2024-015 for vendor_004 on proj_web_01 for $25,000 for additional frontend development tools and licenses for fiscal year 2024. If the verification confirms sufficient funds, record another invoice from vendor_004: invoice FDT-2025-2346 for $25,000 with invoice date July 1, 2025 and due August 15, 2025 for PO-2024-015. Finally, establish a payment due alert for vendor_004 with a 10-day threshold notifying emp_finance_01. Let me know the first invoice ID and if the PO verification was successful.",
        actions=[
            Action(name="GetVendorStatus", kwargs={"vendor_id": "vendor_004"}),
            Action(
                name="RecordInvoice",
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
                name="ValidatePurchaseOrder",
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
                name="RecordInvoice",
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
                name="CreateFinancialAlert",
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
        Handle the audit of project financials to identify potential issues. Obtain the project financial summary for proj_ai_01 for
        fiscal year 2024. Should the monthly burn rate surpass $20,000, determine the velocity-budget ratio for
        team_analytics_01 (make use of this team ID even if it's not the project's main team) reviewing 1 sprint
        for fiscal year 2024. In case the cost per story point goes beyond $450, request a budget modification for proj_ai_01
        to reduce by $100,000 citing 'Burn rate exceeding projections - cost optimization required' as emp_pm_04 for
        fiscal year 2024. Then, compile a cost forecast for proj_ai_01 for 3 months, excluding contingency for fiscal year
        2024. Inform me of the monthly burn rate and the overall forecasted cost.
        """,
        actions=[
            Action(
                name="GetProjectFinancialSummary",
                kwargs={"project_id": "proj_ai_01", "fiscal_year": 2024},
            ),
            Action(
                name="CalculateVelocityBudgetRatio",
                kwargs={
                    "team_id": "team_analytics_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="RequestBudgetModification",
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
                name="CreateCostForecast",
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
        Coordinate the evaluation of staffing costs for project assignments. Figure out the employee cost rate for emp_arch_01
        (senior architect) including overhead. If their annual rate is more than $350,000, compute the cost rate for
        emp_analyst_03 (junior analyst) with overhead. If the junior's weekly rate is below $5,000, check
        if emp_analyst_03 can file a $399 expense for analytics training on June 25, 2025 for proj_gamma_03
        without assigning it to a specific sprint or task. If valid, proceed to submit the reimbursement for an 'Advanced
        analytics and statistics course' with receipt provided. Finally, retrieve emp_analyst_03's expense history for
        2025. Inform me of the architect's annual rate and the junior analyst's utilization percentage.
        """,
        actions=[
            Action(
                name="CalculateEmployeeCostRate",
                kwargs={"employee_id": "emp_arch_01", "include_overhead": True},
            ),
            Action(
                name="CalculateEmployeeCostRate",
                kwargs={"employee_id": "emp_analyst_03", "include_overhead": True},
            ),
            Action(
                name="ValidateExpenseSubmission",
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
                name="SubmitReimbursement",
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
                name="GetEmployeeExpenseHistory",
                kwargs={"employee_id": "emp_analyst_03", "fiscal_year": 2025},
            ),
        ],
        outputs=['"annual_rate": 673920.0', '"utilization_percentage": 60.0'],
    ),
    Task(
        annotator="0",
        user_id="department_rebalancing_analyst",
        instruction="""
        Handle department budget optimization for Q2. Acquire the department budget overview for Analytics for fiscal year
        2024. Should the utilization percentage fall below 60%, obtain the department overview for Engineering. In the event that
        Engineering's utilization exceeds 37%, divert $45,000 from team_analytics_01 to team_dev_01 for fiscal year 2024.
        Following the transfer, set up a budget threshold alert at 70% for proj_reporting_01 titled 'Reporting Project Budget Alert - Post Rebalancing' alerting
        emp_analyst_01 and emp_analyst_02. Conclude by telling me the utilization percentage for Analytics.
        """,
        actions=[
            Action(
                name="GetDepartmentBudgetOverview",
                kwargs={"department_name": "Analytics", "fiscal_year": 2024},
            ),
            Action(
                name="GetDepartmentBudgetOverview",
                kwargs={"department_name": "Engineering", "fiscal_year": 2024},
            ),
            Action(
                name="TransferBudgetBetweenTeams",
                kwargs={
                    "source_team_id": "team_analytics_01",
                    "target_team_id": "team_dev_01",
                    "transfer_amount": 45000,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="CreateBudgetThresholdAlert",
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
        Coordinate the planning for a potential project extension. Retrieve the budget status for proj_enterprise_01 for fiscal year
        2024. If the utilization rate registers below 70%, formulate a cost forecast for proj_enterprise_01 spanning 4 months including
        contingency. Provided the budget exhaustion month surpasses month 3, compute the employee cost rate for
        emp_devops_02 inclusive of overhead. If their weekly rate is under $7,000, pursue a budget modification for
        proj_enterprise_01 to amplify by $250,000 using 'Project extension approved - 4 month runway needed'
        as emp_arch_01. Conclude by informing me of the budget utilization rate and the total forecasted cost.
        """,
        actions=[
            Action(
                name="GetBudgetStatus",
                kwargs={"project_id": "proj_enterprise_01", "fiscal_year": 2024},
            ),
            Action(
                name="CreateCostForecast",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "forecast_months": 4,
                    "include_contingency": True,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="CalculateEmployeeCostRate",
                kwargs={"employee_id": "emp_devops_02", "include_overhead": True},
            ),
            Action(
                name="RequestBudgetModification",
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
        As you analyze task efficiency for cost optimization, retrieve the task cost breakdown for task_003 (API endpoint
        development). If the cost per story point goes over $500, obtain the task cost breakdown for task_012 (permissions
        system). Subsequently, compute the velocity-budget ratio for team_dev_01 looking
        back 1 sprint for fiscal year 2024. In the event that the average cost per story point surpasses $450, generate a financial alert
        (use alert_XXX as the alert id and set threshold value as none)
        for approval_needed on entity_type project entity_id proj_web_01 to notify emp_arch_01 and emp_pm_03. Inform me
        of task_003's cost per story point and whether an alert was initiated.
        """,
        actions=[
            Action(name="GetTaskCostBreakdown", kwargs={"task_id": "task_003"}),
            Action(name="GetTaskCostBreakdown", kwargs={"task_id": "task_012"}),
            Action(
                name="CalculateVelocityBudgetRatio",
                kwargs={
                    "team_id": "team_dev_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="CreateFinancialAlert",
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
        As part of quarterly vendor purchase processing, confirm the purchase order PO-2024-020 for vendor_003 on
        proj_mobile_01 for $75,000 with description 'Cloud infrastructure and services - Q3' for fiscal year 2024.
        Following this, obtain the vendor status for vendor_003. Subsequently, compute the project cost for proj_mobile_01 including planned
        expenses. Thereafter, issue a financial alert (use alert_3022e583 for alert ID) for budget_overrun on proj_mobile_01
        with a 90% threshold and notify
        emp_pm_03 and emp_arch_01. In conclusion, log a new invoice (use inv_651be335 for invoice ID) from vendor_003:
        invoice CloudTech-2025-9876 for $75,000
        with an invoice date of July 1, 2025, and due date of August 30, 2025, in reference to the validated PO. Report to me the validation
        status and indicate if any warnings were detected.
        """,
        actions=[
            Action(
                name="ValidatePurchaseOrder",
                kwargs={
                    "po_number": "PO-2024-020",
                    "vendor_id": "vendor_003",
                    "project_id": "proj_mobile_01",
                    "amount": 75000,
                    "description": "Cloud infrastructure and services - Q3",
                    "fiscal_year": 2024,
                },
            ),
            Action(name="GetVendorStatus", kwargs={"vendor_id": "vendor_003"}),
            Action(
                name="CalculateProjectCost",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "include_planned": True,
                    "as_of_date": None,
                },
            ),
            Action(
                name="CreateFinancialAlert",
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
                name="RecordInvoice",
                kwargs={
                    "vendor_id": "vendor_003",
                    "invoice_id": "inv_651be335",
                    "po_number": "PO-2024-020",
                    "invoice_number": "CloudTech-2025-9876",
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
        Handle the analysis of employee project efficiency. Obtain the employee cost by project for emp_devops_02 on
        proj_enterprise_01, including expenses. If their total cost surpasses $2,000, determine their cost rate
        with overhead. Should their annual rate be more than $250,000, verify if they are eligible to expense $420 for CloudTech
        certification (professional_development category) on June 24, 2025, for proj_enterprise_01 without
        associating it with a specific sprint or task. If eligibility is confirmed, review the project financial summary for
        proj_enterprise_01 for the fiscal year 2024. Should the weekly burn rate be greater than $5,000, initiate a financial
        alert for budget_overrun on the project entity proj_enterprise_01 at a 92% threshold, notifying
        emp_devops_02 and emp_arch_01. Let me know the employee's total cost and the project's remaining budget.
        """,
        actions=[
            Action(
                name="GetEmployeeCostByProject",
                kwargs={
                    "employee_id": "emp_devops_02",
                    "project_id": "proj_enterprise_01",
                    "include_expenses": True,
                },
            ),
            Action(
                name="CalculateEmployeeCostRate",
                kwargs={"employee_id": "emp_devops_02", "include_overhead": True},
            ),
            Action(
                name="ValidateExpenseSubmission",
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
                name="GetProjectFinancialSummary",
                kwargs={"project_id": "proj_enterprise_01", "fiscal_year": 2024},
            ),
            Action(
                name="CreateFinancialAlert",
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
        Coordinate the setup of budget alerts based on sprint performance. Reconcile the sprint expenses for sprint_005. If the
        total cost is zero, retrieve the sprint financial analysis for sprint_001 instead. Should sprint_001's total cost
        exceed $13,000, set up a budget threshold alert at 80% for proj_web_01, notifying emp_arch_01 and
        emp_dev_05 with the name 'Web Portal Sprint Performance Alert'. Then obtain the employee cost by project for
        emp_dev_05 on proj_web_01, including expenses. If their total cost is less than $30,000, establish another budget
        alert at 70% for proj_api_02, notifying emp_dev_05 and emp_pm_03 with the name 'API Platform Budget Watch'.
        Provide me with the number of alerts created and emp_dev_05's total cost.
        """,
        actions=[
            Action(
                name="ReconcileSprintExpenses", kwargs={"sprint_id": "sprint_005"}
            ),
            Action(
                name="GetSprintFinancialAnalysis", kwargs={"sprint_id": "sprint_001"}
            ),
            Action(
                name="CreateBudgetThresholdAlert",
                kwargs={
                    "project_id": "proj_web_01",
                    "threshold_percentage": 80,
                    "alert_recipients": ["emp_arch_01", "emp_dev_05"],
                    "alert_name": "Web Portal Sprint Performance Alert",
                },
            ),
            Action(
                name="GetEmployeeCostByProject",
                kwargs={
                    "employee_id": "emp_dev_05",
                    "project_id": "proj_web_01",
                    "include_expenses": True,
                },
            ),
            Action(
                name="CreateBudgetThresholdAlert",
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
         You are tasked with enhancing the financial planning for proj_insights_01. Start by going over the recent
         performance of team_analytics_01: calculate the velocity-to-budget ratio using the latest sprint data
         available for fiscal year 2024. With that information, move on to draft a revised budget for proj_insights_01 using
         the identifier budget_XXYYY. This budget is set for fiscal year 2025 and amounts to $675,000. Distribute it among
         the following categories: $410,000 for analytics, $140,000 for infrastructure, $60,000 for training, and $65,000 for
         contingency. Next, obtain the annual cost rate for emp_analyst_02, making sure you include overhead in the calculation.
         If the rate is less than $410,000, file a reimbursement request (ID: rb_XXXYY) with the description 'Excel advanced
         data analysis workshop' attended on June 22, 2025. The amount is $925, categorized under training, with a valid
         receipt, and assigned to proj_insights_01.

        Finally, access the budget status for proj_insights_01 for fiscal year 2025. Report both the success of the budget
        creation and the health of the budget.

        """,
        actions=[
            Action(
                name="CalculateVelocityBudgetRatio",
                kwargs={
                    "team_id": "team_analytics_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="CreateProjectBudget",
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
                name="CalculateEmployeeCostRate",
                kwargs={"employee_id": "emp_analyst_02", "include_overhead": True},
            ),
            Action(
                name="SubmitReimbursement",
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
                name="GetBudgetStatus",
                kwargs={"project_id": "proj_insights_01", "fiscal_year": 2025},
            ),
        ],
        outputs=['"success": true', '"budget_health": "healthy"'],
    ),
    Task(
        annotator="0",
        user_id="project_expansion_strategist",
        instruction="""
        You are assessing projects for potential expansion based on performance. Compute the project ROI for
        proj_web_01 with $320,000 revenue and $120,000 cost savings for fiscal year 2024. If the ROI percentage
        surpasses 50%, obtain the financial report for proj_web_01. If the utilization rate is under 60%, develop a budget
        from velocity for proj_web_01 aiming at 500 story points with 20% buffer. Then determine the employee cost rate
        for emp_dev_05, including overhead. If their utilization percentage exceeds 100%, generate a financial alert for
        approval_needed on entity_type project for proj_web_01 without any threshold value, notifying emp_arch_01 and
        emp_dev_05. Inform me of the ROI percentage and whether the project is eligible for expansion.
        """,
        actions=[
            Action(
                name="CalculateProjectRoi",
                kwargs={
                    "project_id": "proj_web_01",
                    "revenue_generated": 320000,
                    "cost_savings": 120000,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="GetFinancialReport",
                kwargs={
                    "report_type": "project",
                    "entity_id": "proj_web_01",
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="CreateBudgetFromVelocity",
                kwargs={
                    "project_id": "proj_web_01",
                    "target_story_points": 500,
                    "buffer_percentage": 20,
                },
            ),
            Action(
                name="CalculateEmployeeCostRate",
                kwargs={"employee_id": "emp_dev_05", "include_overhead": True},
            ),
            Action(
                name="CreateFinancialAlert",
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
        Handle the setup of budgets for analytics expansion projects. Work out the velocity-budget ratio for
        team_analytics_01 using data from the last sprint for fiscal year 2024. Following the analysis, craft a project budget
        for proj_insights_01 (referencing budget_54S41 for the budget ID) for fiscal year 2025 with a total of $650,000 and specific allocations: analytics $400,000,
        infrastructure $150,000, training $50,000, and contingency $50,000. Then find out the employee cost rate for
        emp_analyst_02, including overhead costs. If their annual rate falls below $400,000, file a reimbursement (identified as rb_asd54) for a Tableau
        advanced data visualization workshop they attended on June 24, 2025 for $950 under the training category
        for project proj_insights_01 (they have the receipt). Lastly, determine the budget status for proj_insights_01
        for fiscal year 2025. Inform me about the budget creation status and the remaining amount.
        """,
        actions=[
            Action(
                name="CalculateVelocityBudgetRatio",
                kwargs={
                    "team_id": "team_analytics_01",
                    "lookback_sprints": 1,
                    "fiscal_year": 2024,
                },
            ),
            Action(
                name="CreateProjectBudget",
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
                name="CalculateEmployeeCostRate",
                kwargs={"employee_id": "emp_analyst_02", "include_overhead": True},
            ),
            Action(
                name="SubmitReimbursement",
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
                name="GetBudgetStatus",
                kwargs={"project_id": "proj_insights_01", "fiscal_year": 2025},
            ),
        ],
        outputs=['"success": true', '"available_amount": 650000'],
    ),
    Task(
        annotator="0",
        user_id="project_variance_analyst",
        instruction="""
        Coordinate an analysis of cost variances for critical projects. Compute the project cost for proj_mobile_01 including
        planned costs without specifying an as_of_date. Retrieve the employee cost by project for emp_dev_03 on proj_mobile_01
        incorporating expenses. Should the employee's total cost exceed $5,000, arrange a budget modification for proj_mobile_01 to increase by
        $125,000 for fiscal year 2024, citing 'Actual costs exceeding plan by 20%+ - additional funding required'
        as emp_pm_03. Then establish a cost forecast for proj_mobile_01 for a 6-month period with contingency for fiscal year 2024.
        Let me know the actual total cost and confirm if the forecast accommodates a contingency.
        """,
        actions=[
            Action(
                name="CalculateProjectCost",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "include_planned": True,
                    "as_of_date": None,
                },
            ),
            Action(
                name="GetEmployeeCostByProject",
                kwargs={
                    "employee_id": "emp_dev_03",
                    "project_id": "proj_mobile_01",
                    "include_expenses": True,
                },
            ),
            Action(
                name="RequestBudgetModification",
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
                name="CreateCostForecast",
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
