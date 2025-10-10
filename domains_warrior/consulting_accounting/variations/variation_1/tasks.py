from domains.dto import Task, Action

TASKS = [
  Task(
        annotator="0",
        user_id="01",
        instruction=(
            "You are the financial controller for 'Maple Leaf Publishing House' (PUB001). You must conduct an accounts receivable aging review as of '2024-11-30' for invoices INV001, INV004, INV009, and INV021. For each invoice, retrieve details and compute aging using today='2024-11-30'. According to policy, invoices overdue 31–60 days must receive an 'email_reminder' with the note 'Overdue 31–60 days', while invoices overdue more than 60 days must receive a 'second_notice' with the note 'Overdue >60 days'. Log every follow-up to the invoice audit trail. Finally, provide two lists directly in the task output: (a) all invoice IDs that required action, and (b) only those that required escalation beyond 60 days."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV001"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV004"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV009"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV021"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV001", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV004", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV009", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV021", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV009", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV021", "event_type": "second_notice", "notes": "Overdue >60 days"})
        ],
        outputs=[["INV009", "INV021"], ["INV009", "INV021"]]
    ),
    Task(
        annotator="0",
        user_id="02",
        instruction=(
            "You are delivering the Q3-2024 office & travel pack. "
            "For '2024-07-01'..'2024-09-30', normalize deductibility on EXP012 (OFFICE_SUPPLIES) and EXP022/EXP023 (TRAVEL_EXPENSE), "
            "generate the '2024-Q3' dashboard and archive KPI 'Q3_Mixed_Compliance_2024-09-30' as_of '2024-09-30' with sections ['ExpenseMix','Deductibility']. "
            "Return the dashboard path."
        ),
        actions=[
            Action(name="list_expenses_by_date_range_and_category", kwargs={"start_date":"2024-07-01","end_date":"2024-09-30","categories":["OFFICE_SUPPLIES","TRAVEL_EXPENSE"]}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id":"EXP012"}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id":"EXP022"}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id":"EXP023"}),
            Action(name="generate_expense_dashboard", kwargs={"quarter":"2024-Q3","included_expenses":["EXP012","EXP022","EXP023"]}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-09-30","artifact_name":"Q3_Mixed_Compliance_2024-09-30","sections":["ExpenseMix","Deductibility"]}),
        ],
        outputs=["/dashboards/ExpenseDashboards/2024-Q3/expense_dashboard_2024-Q3.pdf"]
    ),
    Task(
        annotator="0",
        user_id="03",
        instruction=(
            "You are the accounts receivable specialist for 'Horizon Academic Press' (PUB003). "
            "As of '2024-11-30', you must perform an aging review on invoices INV013, INV008, INV024, and INV025. "
            "For each invoice, retrieve details and compute aging using today='2024-11-30'. "
            "Per policy, invoices overdue 31–60 days must receive an 'email_reminder' with the note 'Overdue 31–60 days', "
            "and invoices overdue more than 60 days must receive a 'second_notice' with the note 'Overdue >60 days'. "
            "Log every follow-up to the invoice audit trail. Finally, output two lists: (a) all invoice IDs that required action, "
            "and (b) only those that required escalation beyond 60 days."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV013"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV008"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV024"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV025"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV013", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV008", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV024", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV025", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV013", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV008", "event_type": "second_notice", "notes": "Overdue >60 days"})
        ],
        outputs=[["INV013", "INV008"], ["INV013", "INV008"]]
    ),
    Task(
        annotator="0",
        user_id="04",
        instruction=(
            "You are preparing a PUB005 wrap memo as of '2024-11-30'. "
            "Classify INV022 and INV026 with today '2024-11-30'; items over 60 days require 'second_notice' with notes 'Overdue >60 days'. "
            "Archive KPI 'PUB005_Wrap_Memo_2024-11-30' as_of '2024-11-30' with sections ['Collections']. Return acted and escalated lists."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV026","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV026","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB005_Wrap_Memo_2024-11-30","sections":["Collections"]}),
        ],
        outputs=[["INV022","INV026"],["INV022","INV026"]]
    ),
    Task(
        annotator="0",
        user_id="05",
        instruction=(
            "You are the accounts receivable specialist for 'Horizon Academic Press' (PUB003). "
            "As of '2024-11-30', you must perform an aging review for invoices INV008, INV009, INV010, and INV011. "
            "For each invoice, retrieve details and compute aging using today='2024-11-30'. "
            "Per policy, invoices overdue 31–60 days must receive an 'email_reminder' with note 'Overdue 31–60 days', "
            "and invoices overdue more than 60 days must receive a 'second_notice' with note 'Overdue >60 days'. "
            "Log every follow-up to the invoice audit trail. Finally, output two lists: (a) all invoice IDs that required action, "
            "(b) only those that required escalation beyond 60 days."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV008"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV009"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV010"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV011"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV008", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV009", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV010", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV011", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV008", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV009", "event_type": "second_notice", "notes": "Overdue >60 days"})
        ],
        outputs=[["INV008", "INV009"], ["INV008", "INV009"]]
    ),
    Task(
        annotator="0",
        user_id="06",
        instruction=(
            "You are the A/R lead for 'Maple Leaf Publishing House' (PUB001). As of '2024-11-30', complete an aging review for INV004, INV009, INV021, and INV026 under policy, record the required follow-ups, and return two lists: (a) all invoice IDs that required action and (b) only those requiring escalation beyond 60 days."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV004"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV009"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV021"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV026"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV004", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV009", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV021", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV026", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV009", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV021", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV026", "event_type": "second_notice", "notes": "Overdue >60 days"})
        ],
        outputs=[["INV009", "INV021", "INV026"], ["INV009", "INV021", "INV026"]]
    ),
    Task(
        annotator="0",
        user_id="07",
        instruction=(
            "You are the A/R coordinator for 'Horizon Academic Press' (PUB003). As of '2024-11-30', review aging for INV008, INV009, and INV010 under policy, "
            "record the required follow-ups, and return two lists: (a) all invoice IDs that required action and (b) only those requiring escalation beyond 60 days."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV008"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV009"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV010"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV008", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV009", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV010", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV008", "event_type": "second_notice", "notes": "system"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV009", "event_type": "second_notice", "notes": "system"})
        ],
        outputs=[["INV008", "INV009"], ["INV008", "INV009"]]
    ),
    Task(
        annotator="0",
        user_id="08",
        instruction=(
            "You are the financial controller for 'Northern Lights Educational Books' (PUB002). "
            "As of '2024-11-30', you must review open invoices INV012, INV023, and INV007, compute aging using today='2024-11-30', "
            "and record policy-compliant follow-ups. Any invoice more than 60 days overdue must receive a 'second_notice' with notes 'Overdue >60 days'; "
            "paid invoices require no action. Return two lists: (a) all invoice IDs that required follow-up and (b) only those requiring escalation beyond 60 days."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV012"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV023"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV007"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV012","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV023","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV007","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"})
        ],
        outputs=[["INV012","INV023"],["INV012","INV023"]]
    ),
    Task(
        annotator="0",
        user_id="09",
        instruction=(
            "You are the financial controller for 'Prairie Knowledge Publishers' (PUB005). "
            "As of '2024-11-30', conduct an accounts receivable review for invoices "
            "INV011, INV022, INV025, and INV026. For each invoice, retrieve details and compute aging with "
            "today='2024-11-30'. Per policy, invoices overdue 31–60 days must receive an 'email_reminder' with note "
            "'Overdue 31–60 days', and invoices overdue more than 60 days must receive a 'second_notice' with note "
            "'Overdue >60 days'. Log each follow-up to the audit trail. Finally, return two lists: "
            "(a) all invoice IDs requiring action, and (b) those requiring escalation beyond 60 days."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV011"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV022"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV025"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV026"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV011", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV022", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV025", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV026", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV022", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV026", "event_type": "second_notice", "notes": "Overdue >60 days"}),
        ],
        outputs=[["INV022", "INV026"], ["INV022", "INV026"]],
    ),
    Task(
        annotator="0",
        user_id="10",
        instruction=(
            "You are enforcing A/R follow-ups as of '2024-11-30' across invoices ['INV008','INV009','INV021','INV011']. Classify each using today '2024-11-30', "
            "and for any invoice over 60 days overdue, log a 'second_notice' with notes 'Overdue >60 days'. Return two lists: (a) all invoices requiring action, "
            "and (b) those escalated beyond 60 days."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV008", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV009", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV021", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV011", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV008", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV009", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV021", "event_type": "second_notice", "notes": "Overdue >60 days"}),
        ],
        outputs=[["INV008", "INV009", "INV021"], ["INV008", "INV009", "INV021"]],
    ),
    Task(
        annotator="0",
        user_id="11",
        instruction=(
            "You are validating A/R enforcement for 'Northern Lights Educational Books' (PUB002) as of '2024-11-30'. "
            "From PUB002 open items, compute aging for invoices ['INV012','INV023'] using today '2024-11-30' and, per policy, log "
            "a 'second_notice' with notes 'Overdue >60 days' for any over 60 days. Archive a KPI artifact as_of '2024-11-30' with sections "
            "['Collections'] and artifact_name 'PUB002_Collections_2024-11-30'. Return two lists: acted invoices and escalated ones."
        ),
        actions=[
            Action(name="list_publisher_open_invoices", kwargs={"publisher_id":"PUB002"}),
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV012"}),
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV023"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={
                "as_of":"2024-11-30","sections":["Collections"],
                "artifact_name":"PUB002_Collections_2024-11-30"
            })
        ],
        outputs=[["INV012","INV023"],["INV012","INV023"]]
    ),
    Task(
        annotator="0",
        user_id="12",
        instruction=(
            "You are preparing a collections snapshot for 'Northern Lights Educational Books' (PUB002) as of '2024-11-30'. "
            "From PUB002 open items, compute aging for ['INV012','INV023'], log 'second_notice' with notes 'Overdue >60 days' where applicable, "
            "and archive KPI as_of '2024-11-30' with sections ['Collections'] and artifact_name 'PUB002_Collections_Snapshot_2024-11-30'. "
            "Return two lists: acted invoices and escalated ones."
        ),
        actions=[
            Action(name="list_publisher_open_invoices", kwargs={"publisher_id":"PUB002"}),
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV012"}),
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV023"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB002_Collections_Snapshot_2024-11-30"}),
        ],
        outputs=[["INV012","INV023"],["INV012","INV023"]]
    ),
    Task(
        annotator="0",
        user_id="13",
        instruction=(
            "You are issuing a zero-total November 2024 shell invoice for 'Maple Leaf Publishing House' (PUB001). "
            "Use invoice_id 'INV-AUTO-2024-404', invoice_number 'INV-2024-404', invoice_date '2024-11-30', period '2024-11-01'..'2024-11-30'; HST 0.13 on subtotal 0.00. "
            "Archive the PDF, log 'generated' audit, and archive KPI 'PUB001_Shell_Close_2024-11' as_of '2024-11-30' with sections ['Issuance']. "
            "Return 'INV-2024-404'."
        ),
        actions=[
            Action(name="calculate_totals", kwargs={"invoice_lines":[],"hst_rate":0.13}),
            Action(name="compose_invoice_pdf", kwargs={"invoice_id":"INV-AUTO-2024-404","publisher_id":"PUB001"}),
            Action(name="insert_invoice", kwargs={
                "invoice_id":"INV-AUTO-2024-404","publisher_id":"PUB001",
                "subtotal":0.00,"hst_amount":0.00,"total_due":0.00,
                "invoice_number":"INV-2024-404","invoice_date":"2024-11-30",
                "period_start":"2024-11-01","period_end":"2024-11-30",
                "pdf_path":"/invoices/auto/INV-AUTO-2024-404.pdf"
            }),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV-AUTO-2024-404","event_type":"generated","notes":"Invoice generated"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB001_Shell_Close_2024-11","sections":["Issuance"]}),
        ],
        outputs=["INV-2024-404"]
    ),
    Task(
        annotator="0",
        user_id="14",
        instruction=(
            "You are compiling a risk overview for PUB003 as of '2024-11-30'. "
            "Compute expected inflows for ['INV008','INV013','INV022'] with probability_rule 'overdue_60=0.3' and "
            "log 'second_notice' with notes 'Overdue >60 days' for >60d items. "
            "Archive KPI as_of '2024-11-30' sections ['Collections'] (artifact_name 'PUB003_Risk_Overview_2024-11-30'). Return KPI path."
        ),
        actions=[
            Action(name="forecast_inflows", kwargs={"invoices":["INV008","INV013","INV022"],"probability_rule":"overdue_60=0.3"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV008","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV013","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB003_Risk_Overview_2024-11-30"}),
        ],
        outputs=["/reports/kpi/PUB003_Risk_Overview_2024-11-30.pdf"],
    ),
    Task(
        annotator="0",
        user_id="15",
        instruction=(
            "You are validating Q2-2024 MEALS_ENTERTAIN controls. "
            "Scan '2024-04-01'..'2024-06-30' with threshold 150.0, post a zero-value memo 'Q2 meals scan – no exceptions' to 'Governance Memo', "
            "and archive KPI 'Q2_Meals_Controls_2024-06-30' as_of '2024-06-30' with sections ['Deductibility']. Return the KPI path."
        ),
        actions=[
            Action(name="list_expenses_by_date_range_and_category", kwargs={"start_date":"2024-04-01","end_date":"2024-06-30","categories":["MEALS_ENTERTAIN"]}),
            Action(name="flag_high_value_meals", kwargs={"expenses_ref":{"expenses":[{"expense_id":"EXP019","category_code":"MEALS_ENTERTAIN","gross_amount":18.75}]},"threshold":150.0}),
            Action(name="post_journal_entry", kwargs={"date":"2024-06-30","account":"Governance Memo","amount_ref":{"adjustment":0.00},"memo":"Q2 meals scan – no exceptions"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-06-30","artifact_name":"Q2_Meals_Controls_2024-06-30","sections":["Deductibility"]}),
        ],
        outputs=["/reports/kpi/Q2_Meals_Controls_2024-06-30.pdf"]
    ),
    Task(
    annotator="0",
    user_id="16",
    instruction=(
        "You are preparing a PUB002 collections snapshot as of '2024-11-30'. "
        "Evaluate ['INV012','INV023'] using today '2024-11-30'. "
        "Policy: items over 60 days receive a 'second_notice' with notes 'Overdue >60 days'. "
        "For a snapshot memo, escalation is not opened; return two lists in order: "
        "acted (notices sent) and escalated (empty for this snapshot). "
        "Archive KPI as_of '2024-11-30' with sections ['Collections'] "
        "(artifact_name 'PUB002_Collections_Snapshot_2024-11-30')."
    ),
    actions=[
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB002_Collections_Snapshot_2024-11-30"}),
    ],
    outputs=[["INV012","INV023"],[]],
  ),
  Task(
    annotator="0",
    user_id="17",
    instruction=(
        "You are preparing PUB002 AR health as of '2024-11-30'. "
        "Use today '2024-11-30' on ['INV012','INV023'] and record 'second_notice' where >60d. "
        "Keep result concise: acted (notices sent), escalated (if any). "
        "Archive KPI as_of '2024-11-30' sections ['Aging'] (artifact_name 'PUB002_AR_Health_2024-11-30')."
    ),
    actions=[
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Aging"],"artifact_name":"PUB002_AR_Health_2024-11-30"}),
    ],
    outputs=[["INV012","INV023"],[]],
  ),
  Task(
      annotator="0",
      user_id="18",
      instruction=(
          "You are drafting a PUB003 AR follow-up memo as of '2024-11-30'. "
          "Assess ['INV008','INV022'] using today '2024-11-30'. For items over 60 days, send 'second_notice' with notes 'Overdue >60 days'. "
          "Return two arrays in order: acted (notices sent) and escalated (none here). "
          "Archive KPI as_of '2024-11-30' with sections ['Aging'] (artifact_name 'PUB003_Followup_Memo_2024-11-30')."
      ),
      actions=[
          Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV008","today":"2024-11-30"}),
          Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
          Action(name="create_audit_entry", kwargs={"invoice_id":"INV008","event_type":"second_notice","notes":"Overdue >60 days"}),
          Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
          Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Aging"],"artifact_name":"PUB003_Followup_Memo_2024-11-30"}),
      ],
      outputs=[["INV008","INV022"],[]],
  ),
  Task(
        annotator="0",
        user_id="20",
        instruction=(
            "You are running a PUB005 escalation audit as of '2024-11-30' for ['INV022','INV026'] using today '2024-11-30'. "
            "Ensure 'second_notice' with notes 'Overdue >60 days' is logged where >60 days. Return acted and escalated. "
            "Archive KPI as_of '2024-11-30' sections ['Collections'] (artifact_name 'PUB005_Escalation_Audit_2024-11-30')."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV026","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV026","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB005_Escalation_Audit_2024-11-30"}),
        ],
        outputs=[["INV022","INV026"],[]],
    ),
    
    Task(
        annotator="0",
        user_id="21",
        instruction=(
            "You are preparing a PUB001–PUB002 aging digest as of '2024-11-30'. PUB001: ['INV004','INV009']; PUB002: ['INV012']; today '2024-11-30'. "
            "Apply policy (>60 days => 'second_notice' with notes 'Overdue >60 days'). Return two arrays in order: acted (notices sent across both publishers) and escalated (none for this digest). "
            "Archive KPI as_of '2024-11-30' sections ['Aging'] (artifact_name 'Mixed_Aging_Digest_2024-11-30')."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV004","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV009","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV009","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Aging"],"artifact_name":"Mixed_Aging_Digest_2024-11-30"}),
        ],
        outputs=[["INV009","INV012"],[]],
    ),
    Task(
        annotator="0",
        user_id="22",
        instruction=(
            "You are flagging high-value meals for Q2 2024 in MEALS_ENTERTAIN over '2024-04-01'..'2024-06-30' using a threshold of 150.0. "
            "Record a governance memo entry and archive KPI as_of '2024-06-30' sections ['Deductibility'] (artifact_name 'Q2_Meals_Flag_2024-06-30'). Return KPI path."
        ),
        actions=[
            Action(name="list_expenses_by_date_range_and_category", kwargs={"start_date":"2024-04-01","end_date":"2024-06-30","categories":["MEALS_ENTERTAIN"]}),
            Action(name="flag_high_value_meals", kwargs={"expenses_ref":{"expenses":[{"expense_id":"EXP019","category_code":"MEALS_ENTERTAIN","gross_amount":18.75}]},"threshold":150.0}),
            Action(name="post_journal_entry", kwargs={"date":"2024-06-30","account":"Governance Memo","amount":0.00,"memo":"High-value meals scan completed (threshold=150.0)"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-06-30","sections":["Deductibility"],"artifact_name":"Q2_Meals_Flag_2024-06-30"}),
        ],
        outputs=["/reports/kpi/Q2_Meals_Flag_2024-06-30.pdf"],
    ),
    Task(
        annotator="0",
        user_id="23",
        instruction=(
            "You are compiling a risk overview for PUB003 as of '2024-11-30' using expected inflows for ['INV008','INV013','INV022'] with probability_rule 'overdue_60=0.3' and logging required second notices for items over 60 days. "
            "Archive KPI as_of '2024-11-30' sections ['Collections'] (artifact_name 'PUB003_Risk_Overview_2024-11-30'). Return KPI path."
        ),
        actions=[
            Action(name="forecast_inflows", kwargs={"invoices":["INV008","INV013","INV022"],"probability_rule":"overdue_60=0.3"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV008","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV013","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB003_Risk_Overview_2024-11-30"}),
        ],
        outputs=["/reports/kpi/PUB003_Risk_Overview_2024-11-30.pdf"],
    ),
    Task(
        annotator="0",
        user_id="24",
        instruction=(
            "You are preparing a collections digest for PUB003 as of '2024-11-30' using expected inflows for ['INV008','INV013','INV022'] with probability_rule 'overdue_60=0.3'. "
            "Archive KPI as_of '2024-11-30' sections ['Collections'] (artifact_name 'PUB003_Collections_Digest_2024-11-30'). Return KPI path."
        ),
        actions=[
            Action(name="forecast_inflows", kwargs={"invoices":["INV008","INV013","INV022"],"probability_rule":"overdue_60=0.3"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB003_Collections_Digest_2024-11-30"}),
        ],
        outputs=["/reports/kpi/PUB003_Collections_Digest_2024-11-30.pdf"],
    ),
    
    Task(
        annotator="0",
        user_id="25",
        instruction=(
            "You are creating a PUB003 AR bundle as of '2024-11-30' validating ['INV008','INV022'] using today '2024-11-30'. "
            "Send 'second_notice' for items over 60 days and archive KPI as_of '2024-11-30' sections ['Aging','Collections'] (artifact_name 'PUB003_AR_Bundle_2024-11-30'). "
            "Return two arrays: acted (notices sent) and escalated (none)."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV008","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV008","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Aging","Collections"],"artifact_name":"PUB003_AR_Bundle_2024-11-30"}),
        ],
        outputs=[["INV008","INV022"],[]],
    ),
    Task(
        annotator="0",
        user_id="26",
        instruction=(
            "You are preparing a PUB002 collections snapshot as of '2024-11-30'. "
            "Evaluate ['INV012','INV023'] using today '2024-11-30'. Items over 60 days receive a 'second_notice' with notes 'Overdue >60 days'. "
            "Return two arrays in order: acted (notices sent) and escalated (empty for this snapshot). "
            "Archive KPI as_of '2024-11-30' with sections ['Collections'] (artifact_name 'PUB002_Collections_Snapshot_2024-11-30')."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB002_Collections_Snapshot_2024-11-30"}),
        ],
        outputs=[["INV012","INV023"],[]],
    ),
    
    Task(
        annotator="0",
        user_id="27",
        instruction=(
            "You are auditing Q2 2024 expenses for TRAINING_DEV and MEALS_ENTERTAIN covering '2024-04-01'..'2024-06-30'. "
            "Apply deductibility for EXP018 and EXP019 and archive KPI as_of '2024-06-30' sections ['Deductibility'] (artifact_name 'Q2_Expense_Audit_2024-06-30'). Return KPI path."
        ),
        actions=[
            Action(name="list_expenses_by_date_range_and_category", kwargs={"start_date":"2024-04-01","end_date":"2024-06-30","categories":["TRAINING_DEV","MEALS_ENTERTAIN"]}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id":"EXP018"}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id":"EXP019"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-06-30","sections":["Deductibility"],"artifact_name":"Q2_Expense_Audit_2024-06-30"}),
        ],
        outputs=["/reports/kpi/Q2_Expense_Audit_2024-06-30.pdf"],
    ),
    
    Task(
        annotator="0",
        user_id="28",
        instruction=(
            "You are creating a PUB002 late-stage AR check as of '2024-11-30' for ['INV012','INV023'] using today '2024-11-30'. "
            "Send 'second_notice' for items over 60 days and archive KPI as_of '2024-11-30' sections ['Collections'] (artifact_name 'PUB002_LateStage_2024-11-30'). "
            "Return two arrays: acted (notices sent) and escalated (none)."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB002_LateStage_2024-11-30"}),
        ],
        outputs=[["INV012","INV023"],[]],
    ),
    
    Task(
        annotator="0",
        user_id="29",
        instruction=(
            "You are issuing a zero-total November 2024 shell invoice for 'Maple Leaf Publishing House' (PUB001). "
            "Use invoice_id 'INV-AUTO-2024-034' and invoice_number 'INV-2024-034' with invoice_date '2024-11-30', period '2024-11-01'..'2024-11-30', and pdf_path '/invoices/auto/INV-AUTO-2024-034.pdf'. "
            "Record 'generated' with notes 'Invoice generated' and archive KPI as_of '2024-11-30' sections ['Issuance'] (artifact_name 'PUB001_Shell_Issue_2024-11'). Return 'INV-2024-034'."
        ),
        actions=[
            Action(name="calculate_totals", kwargs={"invoice_lines":[],"hst_rate":0.13}),
            Action(name="insert_invoice", kwargs={"invoice_id":"INV-AUTO-2024-034","publisher_id":"PUB001","subtotal":0.00,"hst_amount":0.00,"total_due":0.00,"invoice_number":"INV-2024-034","invoice_date":"2024-11-30","period_start":"2024-11-01","period_end":"2024-11-30","pdf_path":"/invoices/auto/INV-AUTO-2024-034.pdf"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV-AUTO-2024-034","event_type":"generated","notes":"Invoice generated"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Issuance"],"artifact_name":"PUB001_Shell_Issue_2024-11"}),
        ],
        outputs=["INV-2024-034"],
    ),
    Task(
        annotator="0",
        user_id="30",
        instruction=(
            "You are issuing a November 2024 invoice for 'Horizon Academic Press' (PUB003) on project PROJ006. "
            "Bill approved November work ('2024-11-01'..'2024-11-30') from time entry TIME018. "
            "The invoice must use invoice_id 'INV-AUTO-2024-601', invoice_number 'INV-2024-601', invoice_date '2024-11-30', and apply HST 0.13. "
            "Archive the PDF and log an audit event 'generated' with notes 'Invoice generated'. "
            "Return the invoice_number."
        ),
        actions=[
            Action(name="resolve_hourly_rate", kwargs={"project_id": "PROJ006"}),
            Action(name="list_time_entries", kwargs={"project_id": "PROJ006", "month": "2024-11"}),
            Action(name="build_invoice_lines", kwargs={"time_entries": ["TIME018"], "hourly_rate": 100.0}),
            Action(name="calculate_totals", kwargs={"invoice_lines": [{"line_amount": 600.0}], "hst_rate": 0.13}),
            Action(name="compose_invoice_pdf", kwargs={"invoice_id": "INV-AUTO-2024-601", "publisher_id": "PUB003"}),
            Action(name="insert_invoice", kwargs={
                "invoice_id": "INV-AUTO-2024-601",
                "publisher_id": "PUB003",
                "subtotal": 600.0,
                "hst_amount": 78.0,
                "total_due": 678.0,
                "invoice_number": "INV-2024-601",
                "invoice_date": "2024-11-30",
                "pdf_path": "/invoices/auto/INV-AUTO-2024-601.pdf"
            }),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV-AUTO-2024-601", "event_type": "generated", "notes": "Invoice generated"})
        ],
        outputs=["INV-2024-601"]
    ),
    Task(
        annotator="0",
        user_id="31",
        instruction=(
            "You are producing a collections outlook for PUB003 as of '2024-11-30'. "
            "Use expected inflows for ['INV008','INV013','INV022'] with probability_rule 'overdue_60=0.3' and archive KPI as_of '2024-11-30' "
            "with sections ['Collections'] (artifact_name 'PUB003_Collections_Outlook_2024-11-30'). Return the KPI pdf path."
        ),
        actions=[
            Action(name="forecast_inflows", kwargs={"invoices":["INV008","INV013","INV022"],"probability_rule":"overdue_60=0.3"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB003_Collections_Outlook_2024-11-30"}),
        ],
        outputs=["/reports/kpi/PUB003_Collections_Outlook_2024-11-30.pdf"],
    ),
    Task(
        annotator="0",
        user_id="32",
        instruction=(
            "You are validating a PUB003 collections digest as of '2024-11-30'. "
            "Use expected inflows for ['INV008','INV013','INV022'] with probability_rule 'overdue_60=0.3' and archive KPI as_of '2024-11-30' with sections ['Collections'] "
            "(artifact_name 'PUB003_Collections_Digest_2024-11-30'). Return the KPI pdf path."
        ),
        actions=[
            Action(name="forecast_inflows", kwargs={"invoices":["INV008","INV013","INV022"],"probability_rule":"overdue_60=0.3"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB003_Collections_Digest_2024-11-30"}),
        ],
        outputs=["/reports/kpi/PUB003_Collections_Digest_2024-11-30.pdf"],
    ),
    Task(
        annotator="0",
        user_id="33",
        instruction=(
            "You are enforcing A/R follow-ups for 'Horizon Academic Press' (PUB003) as of '2024-11-30'. "
            "Evaluate ['INV008','INV022'] using today '2024-11-30'. Per policy, send 'second_notice' with notes 'Overdue >60 days' for all >60d; treat escalated as the 90+ bucket only. "
            "Archive a KPI as_of '2024-11-30' with sections ['Aging','Collections'] (artifact_name 'PUB003_AR_Followups_2024-11-30'). "
            "Return two lists: acted (>60d) and escalated (90+)."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV008","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV008","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Aging","Collections"],"artifact_name":"PUB003_AR_Followups_2024-11-30"}),
        ],
        outputs=[["INV008","INV022"],["INV008","INV022"]],
    ),
    
    Task(
        annotator="0",
        user_id="34",
        instruction=(
            "You are producing a PUB001 spot check as of '2024-11-30'. Classify ['INV004','INV009'] using today '2024-11-30'; send 'second_notice' on >60d and treat escalated as 90+. "
            "Archive KPI as_of '2024-11-30' with sections ['Aging'] (artifact_name 'PUB001_Spot_2024-11-30'). "
            "Return acted and escalated lists."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV004","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV009","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV009","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Aging"],"artifact_name":"PUB001_Spot_2024-11-30"}),
        ],
        outputs=[["INV009"],[]],
    ),
    
    Task(
        annotator="0",
        user_id="50",
        instruction=(
            "You are compiling a PUB003 collections probability note as of '2024-11-30'. Use expected inflows for ['INV008','INV013','INV022'] with probability_rule 'overdue_60=0.3'. "
            "Archive KPI as_of '2024-11-30' with sections ['Collections'] (artifact_name 'PUB003_Collections_Prob_2024-11-30'). "
            "Return the KPI path."
        ),
        actions=[
            Action(name="forecast_inflows", kwargs={"invoices":["INV008","INV013","INV022"],"probability_rule":"overdue_60=0.3"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB003_Collections_Prob_2024-11-30"}),
        ],
        outputs=["/reports/kpi/PUB003_Collections_Prob_2024-11-30.pdf"],
    ),
    Task(
        annotator="0",
        user_id="35",
        instruction=(
            "You are creating a PUB003 enforcement bundle as of '2024-11-30'. Classify ['INV008','INV022'] using today '2024-11-30'; send 'second_notice' on >60d; escalated is 90+. "
            "Archive KPI as_of '2024-11-30' with sections ['Aging','Collections'] (artifact_name 'PUB003_Enforcement_2024-11-30'). "
            "Return acted and escalated lists."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV008","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV008","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Aging","Collections"],"artifact_name":"PUB003_Enforcement_2024-11-30"}),
        ],
        outputs=[["INV008","INV022"],["INV008","INV022"]],
    ),
    
    Task(
        annotator="0",
        user_id="36",
        instruction=(
            "You are delivering the Q3-2024 mixed expense pack. "
            "For '2024-07-01'..'2024-09-30', normalize deductibility for EXP012 (OFFICE_SUPPLIES) and EXP022/EXP023 (TRAVEL_EXPENSE), "
            "generate the '2024-Q3' dashboard, and archive KPI 'Q3_Mixed_Pack_2024-09-30' as_of '2024-09-30' with sections ['ExpenseMix','Deductibility']. "
            "Return the dashboard path."
        ),
        actions=[
            Action(name="list_expenses_by_date_range_and_category", kwargs={"start_date": "2024-07-01", "end_date": "2024-09-30", "categories": ["OFFICE_SUPPLIES", "TRAVEL_EXPENSE"]}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id": "EXP012"}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id": "EXP022"}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id": "EXP023"}),
            Action(name="generate_expense_dashboard", kwargs={"quarter": "2024-Q3", "included_expenses": ["EXP012", "EXP022", "EXP023"]}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-09-30", "artifact_name": "Q3_Mixed_Pack_2024-09-30", "sections": ["ExpenseMix", "Deductibility"]})
        ],
        outputs=["/dashboards/ExpenseDashboards/2024-Q3/expense_dashboard_2024-Q3.pdf"]
    ),
    
    Task(
        annotator="0",
        user_id="37",
        instruction=(
            "You are confirming the November 2024 tax reserve at month_end '2024-11-30'. You will align the 2024 reserve with 'SNAP004' "
            "(threshold 0.01), book 157.87 to 'Tax Reserve' (memo 'YTD tax reserve true-up'), and archive KPI as_of '2024-11-30' "
            "(artifact_name 'TaxReserve_Alignment_2024-11'). Return 157.87."
        ),
        actions=[
            Action(name="compute_ytd_from_monthly_revenue", kwargs={"year": 2024, "through_month": 11}),
            Action(name="compute_tax_reserve", kwargs={"ytd_revenue": 10909.5, "tax_year": 2024}),
            Action(name="get_dashboard_snapshot", kwargs={"snapshot_id": "SNAP004"}),
            Action(name="reconcile_tax_reserve", kwargs={"computed_tax_reserve_ref": {"tax_reserve": 2891.02}, "snapshot_ref": {"ytd_tax_reserve": 2733.15}, "threshold": 0.01}),
            Action(name="post_journal_entry", kwargs={"date": "2024-11-30", "account": "Tax Reserve", "amount_ref": {"adjustment": 157.87}, "memo": "YTD tax reserve true-up"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "sections": ["TaxReserve"], "artifact_name": "TaxReserve_Alignment_2024-11"}),
        ],
        outputs=["157.87"],
    ),
    
    Task(
        annotator="0",
        user_id="38",
        instruction=(
            "You are verifying November 2024 tax reserve values at month_end '2024-11-30'. You will align with 'SNAP004' (threshold 0.01), "
            "book 157.87 to 'Tax Reserve' (memo 'YTD tax reserve true-up'), and archive KPI as_of '2024-11-30' (artifact_name 'TaxReserve_Verify_2024-11'). "
            "Return 157.87."
        ),
        actions=[
            Action(name="compute_ytd_from_monthly_revenue", kwargs={"year": 2024, "through_month": 11}),
            Action(name="compute_tax_reserve", kwargs={"ytd_revenue": 10909.5, "tax_year": 2024}),
            Action(name="get_dashboard_snapshot", kwargs={"snapshot_id": "SNAP004"}),
            Action(name="reconcile_tax_reserve", kwargs={"computed_tax_reserve_ref": {"tax_reserve": 2891.02}, "snapshot_ref": {"ytd_tax_reserve": 2733.15}, "threshold": 0.01}),
            Action(name="post_journal_entry", kwargs={"date": "2024-11-30", "account": "Tax Reserve", "amount_ref": {"adjustment": 157.87}, "memo": "YTD tax reserve true-up"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "sections": ["TaxReserve"], "artifact_name": "TaxReserve_Verify_2024-11"}),
        ],
        outputs=["157.87"],
    ),
    Task(
        annotator="0",
        user_id="39",
        instruction=(
        "You are validating A/R enforcement for 'Northern Lights Educational Books' (PUB002) as of '2024-11-30'. "
        "From PUB002 open items, compute aging for invoices ['INV012','INV023'] using today '2024-11-30' and, per policy, log "
        "a 'second_notice' with notes 'Overdue >60 days' for any over 60 days. Archive a KPI artifact as_of '2024-11-30' with "
        "artifact_name 'PUB002_Collections_2024-11-30'. Return two lists: acted invoices and escalated ones."
        ),
        actions=[
        Action(name="list_publisher_open_invoices", kwargs={"publisher_id":"PUB002"}),
        Action(name="get_invoice_details", kwargs={"invoice_id":"INV012"}),
        Action(name="get_invoice_details", kwargs={"invoice_id":"INV023"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB002_Collections_2024-11-30"})
        ],
        outputs=[["INV012","INV023"],["INV012","INV023"]]
    ),
    Task(
        annotator="0",
        user_id="40",
        instruction=(
        "You are finalizing a PUB002 late-stage AR check as of '2024-11-30'. Review ['INV012','INV023'] using today '2024-11-30', "
        "log 'second_notice' for >60d and 'escalated' for 90+, and archive KPI as_of '2024-11-30' with artifact_name 'PUB002_LateStage_2024-11-30'. "
        "Return acted and escalated lists."
        ),
        actions=[
        Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV012", "today": "2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV023", "today": "2024-11-30"}),
        Action(name="create_audit_entry", kwargs={"invoice_id": "INV012", "event_type": "second_notice", "notes": "Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id": "INV023", "event_type": "second_notice", "notes": "Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id": "INV012", "event_type": "escalated", "notes": "Overdue 90+ days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id": "INV023", "event_type": "escalated", "notes": "Overdue 90+ days"}),
        Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "artifact_name": "PUB002_LateStage_2024-11-30"}),
        ],
        outputs=[["INV012", "INV023"], ["INV012", "INV023"]],
    ),
    Task(
        annotator="0",
        user_id="41",
        instruction=(
        "You are composing a PUB003 follow-up memo as of '2024-11-30'. Classify ['INV008','INV022'] with today '2024-11-30', "
        "send 'second_notice' on >60d and log 'escalated' for 90+. Archive KPI as_of '2024-11-30' with artifact_name 'PUB003_Followup_Memo_2024-11-30'. "
        "Return acted and escalated lists."
        ),
        actions=[
        Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV008", "today": "2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV022", "today": "2024-11-30"}),
        Action(name="create_audit_entry", kwargs={"invoice_id": "INV008", "event_type": "second_notice", "notes": "Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id": "INV022", "event_type": "second_notice", "notes": "Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id": "INV008", "event_type": "escalated", "notes": "Overdue 90+ days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id": "INV022", "event_type": "escalated", "notes": "Overdue 90+ days"}),
        Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "artifact_name": "PUB003_Followup_Memo_2024-11-30"}),
        ],
        outputs=[["INV008", "INV022"], ["INV008", "INV022"]],
    ),
    Task(
        annotator="0",
        user_id="42",
        instruction=(
        "You are preparing a PUB002 late-stage memo as of '2024-11-30'. Review ['INV012','INV023'] with today '2024-11-30', "
        "log 'second_notice' for >60d and 'escalated' for 90+, and archive KPI as_of '2024-11-30' with artifact_name 'PUB002_LateStage_Memo_2024-11-30'. "
        "Return acted and escalated lists."
        ),
        actions=[
        Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV012", "today": "2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV023", "today": "2024-11-30"}),
        Action(name="create_audit_entry", kwargs={"invoice_id": "INV012", "event_type": "second_notice", "notes": "Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id": "INV023", "event_type": "second_notice", "notes": "Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id": "INV012", "event_type": "escalated", "notes": "Overdue 90+ days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id": "INV023", "event_type": "escalated", "notes": "Overdue 90+ days"}),
        Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "artifact_name": "PUB002_LateStage_Memo_2024-11-30"}),
        ],
        outputs=[["INV012", "INV023"], ["INV012", "INV023"]],
    ),
    
    Task(
        annotator="0",
        user_id="43",
        instruction=(
        "You are validating PUB002 collections as of '2024-11-30'. From PUB002, evaluate ['INV012','INV023'] using today '2024-11-30'; "
        "log 'second_notice' with notes 'Overdue >60 days' for any item beyond 60 days. Archive a KPI as_of '2024-11-30' "
        "with artifact_name 'PUB002_Collections_Validate_2024-11-30'. Return two lists: acted and escalated (>60)."
        ),
        actions=[
        Action(name="list_publisher_open_invoices", kwargs={"publisher_id":"PUB002"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB002_Collections_Validate_2024-11-30"}),
        ],
        outputs=[["INV012","INV023"],["INV012","INV023"]],
    ),
    Task(
        annotator="0",
        user_id="44",
        instruction=(
        "You are validating PUB001 follow-ups as of '2024-11-30'. Compute aging for ['INV009','INV021','INV026'] with today '2024-11-30' and log "
        "'second_notice' with notes 'Overdue >60 days' for those beyond 60 days. Archive a KPI as_of '2024-11-30' with artifact_name "
        "'PUB001_Followups_2024-11-30'. Return acted and escalated (>60) lists."
        ),
        actions=[
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV009","today":"2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV021","today":"2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV026","today":"2024-11-30"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV009","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV021","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV026","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB001_Followups_2024-11-30"}),
        ],
        outputs=[["INV009","INV021","INV026"],["INV009","INV021","INV026"]],
    ),
    Task(
        annotator="0",
        user_id="45",
        instruction=(
        "You are drafting PUB005 follow-ups as of '2024-11-30'. Evaluate ['INV011','INV022','INV026'] with today '2024-11-30'; log "
        "'second_notice' with notes 'Overdue >60 days' on any item beyond 60 days. Archive a KPI as_of '2024-11-30' with artifact_name "
        "'PUB005_Followups_2024-11-30'. Return two lists: acted and escalated (>60)."
        ),
        actions=[
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV011","today":"2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV026","today":"2024-11-30"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV026","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB005_Followups_2024-11-30"}),
        ],
        outputs=[["INV022","INV026"],["INV022","INV026"]],
    ),
    Task(
        annotator="0",
        user_id="46",
        instruction=(
        "You are consolidating a PUB001 AR bundle as of '2024-11-30'. Assess ['INV009','INV021','INV026'] using today '2024-11-30'; log "
        "'second_notice' with 'Overdue >60 days'; archive a KPI as_of '2024-11-30' with artifact_name 'PUB001_AR_Bundle_2024-11-30'. "
        "Return acted and escalated (>60) lists."
        ),
        actions=[
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV009","today":"2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV021","today":"2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV026","today":"2024-11-30"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV009","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV021","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV026","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB001_AR_Bundle_2024-11-30"}),
        ],
        outputs=[["INV009","INV021","INV026"],["INV009","INV021","INV026"]],
    ),
    Task(
        annotator="0",
        user_id="47",
        instruction=(
        "You are assembling a PUB005 AR wrap-up as of '2024-11-30'. Assess ['INV011','INV022','INV026'] with today '2024-11-30'; log "
        "'second_notice' with 'Overdue >60 days' on any item beyond 60 days; archive a KPI as_of '2024-11-30' with artifact_name "
        "'PUB005_AR_Wrap_2024-11-30'. Return two lists: acted and escalated (>60)."
        ),
        actions=[
        Action(name="get_invoice_details", kwargs={"invoice_id":"INV011"}),
        Action(name="get_invoice_details", kwargs={"invoice_id":"INV022"}),
        Action(name="get_invoice_details", kwargs={"invoice_id":"INV026"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV011","today":"2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
        Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV026","today":"2024-11-30"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="create_audit_entry", kwargs={"invoice_id":"INV026","event_type":"second_notice","notes":"Overdue >60 days"}),
        Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB005_AR_Wrap_2024-11-30"}),
        ],
        outputs=[["INV022","INV026"],["INV022","INV026"]],
    ),
    
    Task(
        annotator="A",
        user_id="48",
        instruction=(
            "You complete PUB003’s A/R review for '2024-11-30'. Focus on invoices 'INV008' and 'INV022' as of '2024-11-30'; if an item sits 60+ days past due, "
            "its record carries a 'second_notice' with notes 'Overdue >60 days'. Close the review with a collections KPI saved under "
            "artifact_name 'PUB003_AR_Review_2024-11-30' for that date. End state: 'INV008' and 'INV022' are read and aged for '2024-11-30'; any 60+ day item has "
            "a 'second_notice' (notes 'Overdue >60 days'); the KPI PDF for 'PUB003_AR_Review_2024-11-30' is produced."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV008"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV022"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV008", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV022", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV008", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV022", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "sections": ["Collections"], "artifact_name": "PUB003_AR_Review_2024-11-30"})
        ],
        outputs=[
            "/reports/kpi/PUB003_AR_Review_2024-11-30.pdf"
        ],
    ),
    Task(
        annotator="A",
        user_id="49",
        instruction=(
            "You close PUB003 A/R for '2024-11-30'. On that date, invoices 'INV008' and 'INV022' are on record; any item 60+ days past due carries "
            "an audit 'second_notice' with notes 'Overdue >60 days'. A collections KPI is archived as 'PUB003_AR_Review_2024-11-30' "
            "with sections ['Collections']. End state: both invoices are read and aged for '2024-11-30'; any 60+ day item has 'second_notice' "
            "('Overdue >60 days'); the KPI PDF exists for 'PUB003_AR_Review_2024-11-30'."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV008"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV022"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV008", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV022", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV008", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV022", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={
                "as_of": "2024-11-30",
                "sections": ["Collections"],
                "artifact_name": "PUB003_AR_Review_2024-11-30"
            }),
        ],
        outputs=[
            "/reports/kpi/PUB003_AR_Review_2024-11-30.pdf"
        ],
    ),
    
    Task(
        annotator="A",
        user_id="50",
        instruction=(
            "You regularize PUB003’s month-end collections posture. As of '2024-11-30', both 'INV008' and 'INV022' carry their computed aging and, when 60+ days "
            "past due, an audit 'second_notice' with notes 'Overdue >60 days'. A collections KPI 'PUB003_MonthEnd_Collections_2024-11-30' rounds out the view. "
            "End state: the 'second_notice' entries exist as required and the KPI PDF is produced."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV008", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV008", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV022", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV022", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={
                "as_of": "2024-11-30",
                "sections": ["Collections"],
                "artifact_name": "PUB003_MonthEnd_Collections_2024-11-30"
            }),
        ],
        outputs=[
            "/reports/kpi/PUB003_MonthEnd_Collections_2024-11-30.pdf"
        ],
    ),
    
    Task(
        annotator="0",
        user_id="51",
        instruction=(
            "You are a financial consulting worker supporting PUB003’s A/R as of '2024-11-30' for Horizon Academic Press. "
            "You will read 'INV008' and 'INV022', compute aging with today '2024-11-30', and record 'second_notice' with notes 'Overdue >60 days' for any >60d items. "
            "You will archive a KPI as_of '2024-11-30' with sections ['Collections'] and artifact_name 'PUB003_AR_Review_2024-11-30'. "
            "Return '/reports/kpi/PUB003_AR_Review_2024-11-30.pdf'."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV008"}),
            Action(name="get_invoice_details", kwargs={"invoice_id": "INV022"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV008", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV022", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV008", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV022", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "sections": ["Collections"], "artifact_name": "PUB003_AR_Review_2024-11-30"})
        ],
        outputs=["/reports/kpi/PUB003_AR_Review_2024-11-30.pdf"],
    ),
    Task(
        annotator="0",
        user_id="52",
        instruction=(
            "You are a financial consulting worker closing PUB001 AR actions as of '2024-11-30' for Maple Leaf Publishing House. "
            "You will compute aging for ['INV009','INV021','INV026'] using today '2024-11-30', record 'second_notice' with notes 'Overdue >60 days' on all >60d, "
            "and archive a KPI as_of '2024-11-30' with sections ['Collections'] and artifact_name 'PUB001_Collections_2024-11-30'. "
            "Return ['/reports/kpi/PUB001_Collections_2024-11-30.pdf']. "
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV009", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV021", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV026", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV009", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV021", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV026", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "sections": ["Collections"], "artifact_name": "PUB001_Collections_2024-11-30"})
        ],
        outputs=["/reports/kpi/PUB001_Collections_2024-11-30.pdf"],
    ),
    Task(
        annotator="0",
        user_id="53",
        instruction=(
            "You are a financial consulting worker running a cross-publisher AR sweep as of '2024-11-30' serving PUB003, PUB002, and PUB001. "
            "You will compute aging for ['INV008','INV012','INV009'] with today '2024-11-30', record 'second_notice' with notes 'Overdue >60 days' on all >60d, "
            "and archive a KPI as_of '2024-11-30' with sections ['Collections'] and artifact_name 'Cross_AR_Sweep_2024-11-30'. "
            "Return ['/reports/kpi/Cross_AR_Sweep_2024-11-30.pdf']."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV008", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV012", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV009", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV008", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV012", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV009", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "sections": ["Collections"], "artifact_name": "Cross_AR_Sweep_2024-11-30"})
        ],
        outputs=["/reports/kpi/Cross_AR_Sweep_2024-11-30.pdf"],
    ),
    Task(
        annotator="1",
        user_id="54",
        instruction=(
                "You are a financial consulting worker doing a PUB002 collections summary as of '2024-11-30'. "
                "You will compute aging for ['INV012','INV023'] with today '2024-11-30', record 'second_notice' with notes 'Overdue >60 days', "
                "and archive a KPI as_of '2024-11-30' with sections ['Collections'] and artifact_name 'PUB002_Collections_2024-11-30'. "
                "Return '/reports/kpi/PUB002_Collections_2024-11-30.pdf'."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB002_Collections_2024-11-30"})
        ],
        outputs=["/reports/kpi/PUB002_Collections_2024-11-30.pdf"],
    ),
    
    Task(
        annotator="1",
        user_id="55",
        instruction=(
            "You are a financial consulting worker for Northern Lights Educational Books (PUB002). "
            "As of '2024-11-30', ensure overdue-notice policy is correctly captured on ['INV012','INV023'] and preserve a dated aging artifact "
            "('PUB002_Aging_2024-11-30') for that date. "
            "Return '/reports/kpi/PUB002_Aging_2024-11-30.pdf'."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV012"}),
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV023"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Aging"],"artifact_name":"PUB002_Aging_2024-11-30"})
        ],
        outputs=["/reports/kpi/PUB002_Aging_2024-11-30.pdf"],
    ),
    Task(
      annotator="A",
      user_id="56",
      instruction=(
          "You deliver a Maple Leaf Publishing (PUB001) enforcement note for '2024-11-30'. "
          "Classify 'INV004','INV009','INV021' with today '2024-11-30'; skip paid/current items; send 'second_notice' for each >60 days. "
          "Archive KPI 'PUB001_Enforcement_2024-11-30' under ['Aging','Collections']."
      ),
      actions=[
          Action(name="get_invoice_details", kwargs={"invoice_id": "INV004"}),
          Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV004", "today": "2024-11-30"}),
          Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV009", "today": "2024-11-30"}),
          Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV021", "today": "2024-11-30"}),
          Action(name="create_audit_entry", kwargs={"invoice_id": "INV009", "event_type": "second_notice", "notes": "Overdue >60 days"}),
          Action(name="create_audit_entry", kwargs={"invoice_id": "INV021", "event_type": "second_notice", "notes": "Overdue >60 days"}),
          Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "sections": ["Aging", "Collections"], "artifact_name": "PUB001_Enforcement_2024-11-30"}),
      ],
      outputs=["/reports/kpi/PUB001_Enforcement_2024-11-30.pdf"],
    ),
    Task(
        annotator="0",
        user_id="57",
        instruction=(
            "You are a financial consulting worker validating Q3-2024 OFFICE_SUPPLIES governance (EXP012) for '2024-07-01'..'2024-09-30'. "
            "Apply deductibility, record a policy review memo to 'Governance Memo' with memo 'OFFICE_SUPPLIES Q3 checked (EXP012)', and archive a KPI as_of '2024-09-30' "
            "(artifact_name 'Q3_OfficeSupplies_Check_2024-09-30'). Return the KPI path."
        ),
        actions=[
            Action(name="list_expenses_by_date_range_and_category", kwargs={"start_date":"2024-07-01","end_date":"2024-09-30","categories":["OFFICE_SUPPLIES"]}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id":"EXP012"}),
            Action(name="post_journal_entry", kwargs={"date":"2024-09-30","account":"Governance Memo","amount":0.00,"memo":"OFFICE_SUPPLIES Q3 checked (EXP012)"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-09-30","artifact_name":"Q3_OfficeSupplies_Check_2024-09-30"}),
        ],
        outputs=["/reports/kpi/Q3_OfficeSupplies_Check_2024-09-30.pdf"],
    ),
    Task(
        annotator="0",
        user_id="58",
        instruction=(
            "You are a financial consulting worker executing a PUB002 late-stage check as of '2024-11-30' for INV012 and INV023. "
            "Send 'second_notice' on any >60 days and capture a KPI as_of '2024-11-30' (artifact_name 'PUB002_LateStage_2024-11-30'). "
            "Return two arrays: acted (notices sent) and escalated (none)."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB002_LateStage_2024-11-30"}),
        ],
        outputs=[["INV012","INV023"],[]],
    ),
    Task(
        annotator="0",
        user_id="59",
        instruction=(
            "You are a financial consulting worker issuing PUB001 aging controls as of '2024-11-30'. "
            "Classify INV004, INV009, INV021 with today '2024-11-30'; send 'second_notice' for >60 days and archive a KPI as_of '2024-11-30' "
            "(artifact_name 'PUB001_Aging_Controls_2024-11-30'). Return acted and escalated."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV004","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV009","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV021","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV009","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV021","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB001_Aging_Controls_2024-11-30"}),
        ],
        outputs=[["INV009","INV021"],[]],
    ),
    Task(
        annotator="0",
        user_id="60",
        instruction=(
            "You are a financial consulting worker completing a PUB001 aging pass as of '2024-11-30'. "
            "Classify INV004, INV009, INV021 with today '2024-11-30'; send 'second_notice' for >60 days and file a KPI as_of '2024-11-30' "
            "(artifact_name 'PUB001_Aging_Pass_2024-11-30'). Return acted and escalated lists."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV004"}),
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV009"}),
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV021"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV004","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV009","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV021","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV009","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV021","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB001_Aging_Pass_2024-11-30"}),
        ],
        outputs=[["INV009","INV021"],["INV009","INV021"]],
    ),

    Task(
        annotator="0",
        user_id="61",
        instruction=(
            "You are a financial consulting worker preparing a cashflow outlook as of '2024-11-30'. "
            "Use balances, 3-month schedules, expected inflows from INV008/INV009/INV010 with probability_rule 'overdue_60=0.3', and outflows including taxes. "
            "Build a 3-month monthly view, archive a KPI as_of '2024-11-30' (artifact_name 'Cashflow_Outlook_2024-11-30'), and record a zero-value memo to 'Liquidity Review Memo'. "
            "Return the KPI path."
        ),
        actions=[
            Action(name="get_bank_balances", kwargs={}),
            Action(name="list_recurring_schedules", kwargs={"horizon_months":3}),
            Action(name="forecast_inflows", kwargs={"invoices":["INV008","INV009","INV010"],"probability_rule":"overdue_60=0.3"}),
            Action(name="forecast_outflows", kwargs={"recurring_schedules":True,"taxes":True,"horizon_months":3}),
            Action(name="build_cashflow_view", kwargs={"horizon_months":3,"granularity":"monthly"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"Cashflow_Outlook_2024-11-30"}),
            Action(name="post_journal_entry", kwargs={"date":"2024-11-30","account":"Liquidity Review Memo","amount":0.00}),
        ],
        outputs=["/reports/kpi/Cashflow_Outlook_2024-11-30.pdf"],
    ),
    Task(
        annotator="0",
        user_id="62",
        instruction=(
            "You are a financial consulting worker preparing a PUB005 wrap-up as of '2024-11-30'. "
            "Evaluate INV011, INV022, INV026 with today '2024-11-30'; send 'second_notice' on any >60 days; archive a KPI as_of '2024-11-30' "
            "(artifact_name 'PUB005_Wrap_2024-11-30'). Return acted and escalated lists."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV011","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV026","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV026","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB005_Wrap_2024-11-30"}),
        ],
        outputs=[["INV022","INV026"],["INV022","INV026"]],
    ),
    Task(
        annotator="0",
        user_id="63",
        instruction=(
            "You are a financial consulting worker assembling a Q3-2024 office & travel integrity note. "
            "For '2024-07-01'..'2024-09-30', include OFFICE_SUPPLIES and TRAVEL_EXPENSE items (EXP012, EXP022, EXP023), generate the '2024-Q3' dashboard, "
            "and archive a KPI as_of '2024-09-30' (artifact_name 'Q3_Mixed_Integrity_2024-09-30'). Return the dashboard path."
        ),
        actions=[
            Action(name="list_expenses_by_date_range_and_category", kwargs={"start_date":"2024-07-01","end_date":"2024-09-30","categories":["OFFICE_SUPPLIES","TRAVEL_EXPENSE"]}),
            Action(name="generate_expense_dashboard", kwargs={"quarter":"2024-Q3","included_expenses":["EXP012","EXP022","EXP023"],"as_of":"2024-09-30","artifact_name":"Q3_Mixed_Integrity_2024-09-30"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-09-30","artifact_name":"Q3_Mixed_Integrity_2024-09-30"}),
        ],
        outputs=["/dashboards/ExpenseDashboards/2024-Q3/expense_dashboard_2024-Q3.pdf"],
    ),
    Task(
        annotator="0",
        user_id="64",
        instruction=(
            "You are validating PUB001 follow-ups as of '2024-11-30'. "
            "Classify INV009 and INV021; any item over 60 days receives a 'second_notice' noted 'Overdue >60 days'. "
            "Archive KPI 'PUB001_Followups_2024-11-30' as_of '2024-11-30' with sections ['Collections']. "
            "Return acted and escalated (>60 days) lists."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV009", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV021", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV009", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV021", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "artifact_name": "PUB001_Followups_2024-11-30", "sections": ["Collections"]})
        ],
        outputs=[["INV009", "INV021"], ["INV009", "INV021"]]
    ),
    Task(
        annotator="0",
        user_id="17",
        instruction=(
            "You are issuing a November 2024 invoice for 'Prairie Knowledge Publishers' (PUB005) on project PROJ010 using time entry TIME017. "
            "The invoice must use invoice_id 'INV-AUTO-2024-604', invoice_number 'INV-2024-604', invoice_date '2024-11-30', and apply HST 0.13. "
            "Archive the PDF and record audit 'generated' with notes 'Invoice generated'. "
            "Return the invoice_number."
        ),
        actions=[
            Action(name="resolve_hourly_rate", kwargs={"project_id": "PROJ010"}),
            Action(name="list_time_entries", kwargs={"project_id": "PROJ010", "month": "2024-11"}),
            Action(name="build_invoice_lines", kwargs={"time_entries": ["TIME017"], "hourly_rate": 85.0}),
            Action(name="calculate_totals", kwargs={"invoice_lines": [{"line_amount": 382.5}], "hst_rate": 0.13}),
            Action(name="compose_invoice_pdf", kwargs={"invoice_id": "INV-AUTO-2024-604", "publisher_id": "PUB005"}),
            Action(name="insert_invoice", kwargs={
                "invoice_id": "INV-AUTO-2024-604",
                "publisher_id": "PUB005",
                "subtotal": 382.5,
                "hst_amount": 49.73,
                "total_due": 432.23,
                "invoice_number": "INV-2024-604",
                "invoice_date": "2024-11-30",
                "pdf_path": "/invoices/auto/INV-AUTO-2024-604.pdf"
            }),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV-AUTO-2024-604", "event_type": "generated", "notes": "Invoice generated"})
        ],
        outputs=["INV-2024-604"]
    ),
    Task(
        annotator="0",
        user_id="66",
        instruction=(
            "You are a financial consulting worker verifying Q2-2024 MEALS_ENTERTAIN controls. "
            "Scan '2024-04-01'..'2024-06-30' and confirm no threshold breach at 150.0; record a zero-value memo to 'Governance Memo' with memo 'Q2 meals scan – no exceptions'; "
            "archive a KPI as_of '2024-06-30' (artifact_name 'Q2_Meals_Scan_2024-06-30'). Return the KPI path."
        ),
        actions=[
            Action(name="list_expenses_by_date_range_and_category", kwargs={"start_date":"2024-04-01","end_date":"2024-06-30","categories":["MEALS_ENTERTAIN"]}),
            Action(name="flag_high_value_meals", kwargs={"expenses_ref":{"expenses":[{"expense_id":"EXP019","category_code":"MEALS_ENTERTAIN","gross_amount":18.75}]},"threshold":150.0}),
            Action(name="post_journal_entry", kwargs={"date":"2024-06-30","account":"Governance Memo","amount":0.00,"memo":"Q2 meals scan – no exceptions"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-06-30","artifact_name":"Q2_Meals_Scan_2024-06-30"}),
        ],
        outputs=["/reports/kpi/Q2_Meals_Scan_2024-06-30.pdf"],
    ),
    Task(
        annotator="1",
        user_id="67",
        instruction=(
            "You are a financial consulting worker assisting PUB003 and PUB002 jointly. "
            "As of '2024-11-30', capture required A/R actions across INV008, INV022, INV012, INV023 and file a memo KPI as_of '2024-11-30' "
            "(artifact_name 'Cross_Action_Memo_2024-11-30'). Return the KPI path."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV008","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV008","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"Cross_Action_Memo_2024-11-30"}),
        ],
        outputs=["/reports/kpi/Cross_Action_Memo_2024-11-30.pdf"],
    ),
    Task(
        annotator="0",
        user_id="68",
        instruction=(
            "You are a financial consulting worker enforcing PUB001 collections as of '2024-11-30'. "
            "Work only open items; compute aging for INV009 and INV021 with today '2024-11-30', record 'second_notice' for any >60 days, "
            "and archive a KPI as_of '2024-11-30' (artifact_name 'PUB001_Aging_2024-11-30'). Return acted (>60 days) and the same set as escalated (>60 days)."
        ),
        actions=[
            Action(name="list_publisher_open_invoices", kwargs={"publisher_id":"PUB001"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV009","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV021","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV009","event_type":"second_notice"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV021","event_type":"second_notice"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB001_Aging_2024-11-30"}),
        ],
        outputs=[["INV009","INV021"],["INV009","INV021"]],
    ),
    Task(
        annotator="0",
        user_id="69",
        instruction=(
            "You are a financial consulting worker running a PUB002 A/R health sweep as of '2024-11-30'. "
            "Compute aging for INV012 and INV023 with today '2024-11-30'; for any >60 days, record 'second_notice'. "
            "Archive a KPI as_of '2024-11-30' (artifact_name 'PUB002_AR_Health_2024-11-30'). Return acted (>60 days) and the same set as escalated (>60 days)."
        ),
        actions=[
            Action(name="list_publisher_open_invoices", kwargs={"publisher_id":"PUB002"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB002_AR_Health_2024-11-30"}),
        ],
        outputs=[["INV012","INV023"],["INV012","INV023"]],
    ),

    Task(
        annotator="0",
        user_id="70",
        instruction=(
            "You are a financial consulting worker enforcing PUB003 follow-ups as of '2024-11-30'. "
            "Classify INV008 and INV022 with today '2024-11-30'; send 'second_notice' for any >60 days and capture a KPI as_of '2024-11-30' "
            "(artifact_name 'PUB003_AR_Followups_2024-11-30'). Return acted (>60 days) and the same set as escalated (>60 days)."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV008","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV008","event_type":"second_notice"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB003_AR_Followups_2024-11-30"}),
        ],
        outputs=[["INV008","INV022"],["INV008","INV022"]],
    ),
    Task(
        annotator="0",
        user_id="71",
        instruction=(
            "You are a financial consulting worker performing a PUB001 A/R spot sweep as of '2024-11-30'. "
            "Work INV004, INV009, INV021 with today '2024-11-30'; send 'second_notice' for any >60 days and file a KPI as_of '2024-11-30' "
            "(artifact_name 'PUB001_SpotSweep_2024-11-30'). Return acted (>60 days) and escalated (>60 days) lists."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV004"}),
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV009"}),
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV021"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV004","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV009","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV021","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV009","event_type":"second_notice"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV021","event_type":"second_notice"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB001_SpotSweep_2024-11-30"}),
        ],
        outputs=[["INV009","INV021"],["INV009","INV021"]],
    ),
    Task(
        annotator="0",
        user_id="72",
        instruction=(
            "You are a financial consulting worker delivering a PUB001 enforcement note as of '2024-11-30'. "
            "Classify INV004, INV009, INV021 with today '2024-11-30'; send 'second_notice' on any >60 days; archive a KPI as_of '2024-11-30' "
            "(artifact_name 'PUB001_Enforcement_2024-11-30'). Return two lists where both reflect invoices >60 days (second notices sent)."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV004","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV009","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV021","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV009","event_type":"second_notice"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV021","event_type":"second_notice"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB001_Enforcement_2024-11-30"}),
        ],
        outputs=[["INV009","INV021"],["INV009","INV021"]],
    ),

    Task(
        annotator="0",
        user_id="73",
        instruction=(
            "You are a financial consulting worker creating a PUB005 A/R summary as of '2024-11-30'. "
            "Evaluate INV011, INV022, INV026 with today '2024-11-30'; send 'second_notice' only on >60 days; archive a KPI as_of '2024-11-30' "
            "(artifact_name 'PUB005_AR_Summary_2024-11-30'). Return acted (>60 days) and the same set as escalated (>60 days)."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV011","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV026","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV026","event_type":"second_notice"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB005_AR_Summary_2024-11-30"}),
        ],
        outputs=[["INV022","INV026"],["INV022","INV026"]],
    ),

    Task(
        annotator="0",
        user_id="74",
        instruction=(
            "You are a financial consulting worker closing PUB003 A/R as of '2024-11-30'. "
            "Evaluate INV008 and INV022 with today '2024-11-30', log 'second_notice' on any >60 days, and file a KPI as_of '2024-11-30' "
            "(artifact_name 'PUB003_AR_Close_2024-11-30'). Return acted (>60 days) and the same set as escalated (>60 days)."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV008"}),
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV022"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV008","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV008","event_type":"second_notice"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB003_AR_Close_2024-11-30"}),
        ],
        outputs=[["INV008","INV022"],["INV008","INV022"]],
    ),
    Task(
        annotator="new",
        user_id="75",
        instruction=(
            "You are a financial consulting worker preparing a PUB001 targeted follow-up note. As of '2024-11-30', you apply A/R policy for INV009 and INV021 "
            "using today '2024-11-30'; log 'second_notice' only for items >60 days with notes 'Overdue >60 days'. Archive a KPI as_of '2024-11-30' with sections "
            "['Collections'] and artifact_name 'PUB001_Targeted_2024-11-30'. Return the KPI path."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV009","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV021","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV009","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV021","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB001_Targeted_2024-11-30"})
        ],
        outputs=["/reports/kpi/PUB001_Targeted_2024-11-30.pdf"],
    ),
    Task(
        annotator="new",
        user_id="76",
        instruction=(
            "You are a financial consulting worker preparing a PUB002 late-stage wrap for Northern Lights Educational Books. As of '2024-11-30', "
            "you enforce follow-ups on INV012 and INV023 using today '2024-11-30'; for any >60 days, log 'second_notice' with notes 'Overdue >60 days'. "
            "Archive a KPI as_of '2024-11-30' with sections ['Aging'] and artifact_name 'PUB002_LateStage_2024-11-30'. Return the KPI path."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Aging"],"artifact_name":"PUB002_LateStage_2024-11-30"})
        ],
        outputs=["/reports/kpi/PUB002_LateStage_2024-11-30.pdf"],
    ),
    Task(
        annotator="new",
        user_id="77",
        instruction=(
            "You are a financial consulting worker preparing the November 2024 tax-reserve true-up for the practice. As of '2024-11-30', "
            "you confirm the 2024 reserve derived from 10909.5 aligns to 'SNAP004' within a threshold of 0.01 and book any difference to 'Tax Reserve' with memo "
            "'YTD tax reserve true-up'. Archive a KPI as_of '2024-11-30' with sections ['TaxReserve'] and artifact_name 'TaxReserve_NovTrueUp_2024-11'. Return 157.87."
        ),
        actions=[
            Action(name="compute_ytd_from_monthly_revenue", kwargs={"year":2024,"through_month":11}),
            Action(name="compute_tax_reserve", kwargs={"ytd_revenue":10909.5,"tax_year":2024}),
            Action(name="get_dashboard_snapshot", kwargs={"snapshot_id":"SNAP004"}),
            Action(name="reconcile_tax_reserve", kwargs={"computed_tax_reserve_ref":{"tax_reserve":2891.02},"snapshot_ref":{"ytd_tax_reserve":2733.15},"threshold":0.01}),
            Action(name="post_journal_entry", kwargs={"date":"2024-11-30","account":"Tax Reserve","amount_ref":{"adjustment":157.87},"memo":"YTD tax reserve true-up"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["TaxReserve"],"artifact_name":"TaxReserve_NovTrueUp_2024-11"})
        ],
        outputs=["157.87"],
    ),
    Task(
        annotator="new",
        user_id="78",
        instruction=(
            "You are a financial consulting worker providing a PUB001 cross-check. As of '2024-11-30', you verify A/R notices for INV009, INV021, and INV026 with "
            "today '2024-11-30'; create 'second_notice' only for items >60 days with notes 'Overdue >60 days'. Archive a KPI as_of '2024-11-30' with sections "
            "['Aging'] and artifact_name 'PUB001_CrossCheck_2024-11-30'. Return the KPI path."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV009","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV021","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV026","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV009","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV021","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV026","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Aging"],"artifact_name":"PUB001_CrossCheck_2024-11-30"})
        ],
        outputs=["/reports/kpi/PUB001_CrossCheck_2024-11-30.pdf"],
    ),
    Task(
        annotator="new",
        user_id="79",
        instruction=(
            "You are a financial consulting worker delivering a Q3 2024 mixed expense snapshot for the practice. For '2024-07-01'..'2024-09-30', "
            "you normalize deductibility on EXP012 (OFFICE_SUPPLIES) and EXP022/EXP023 (TRAVEL_EXPENSE), generate the '2024-Q3' dashboard including these, and "
            "archive a KPI as_of '2024-09-30' with sections ['ExpenseMix','Deductibility'] and artifact_name 'Q3_Mixed_Snapshot_2024-09-30'. Return the dashboard path."
        ),
        actions=[
            Action(name="list_expenses_by_date_range_and_category", kwargs={"start_date":"2024-07-01","end_date":"2024-09-30","categories":["OFFICE_SUPPLIES","TRAVEL_EXPENSE"]}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id":"EXP012"}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id":"EXP022"}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id":"EXP023"}),
            Action(name="generate_expense_dashboard", kwargs={"quarter":"2024-Q3","included_expenses":["EXP012","EXP022","EXP023"]}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-09-30","sections":["ExpenseMix","Deductibility"],"artifact_name":"Q3_Mixed_Snapshot_2024-09-30"})
        ],
        outputs=["/dashboards/ExpenseDashboards/2024-Q3/expense_dashboard_2024-Q3.pdf"],
    ),
    Task(
        annotator="new",
        user_id="80",
        instruction=(
            "You are a financial consulting worker producing a PUB005 November collections note. As of '2024-11-30', you enforce policy actions for INV022 and INV026 "
            "using today '2024-11-30'; log 'second_notice' only for items overdue >60 days with notes 'Overdue >60 days'. Archive a KPI as_of '2024-11-30' with sections "
            "['Collections'] and artifact_name 'PUB005_Collections_2024-11-30'. Return the KPI path."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV026","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV026","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB005_Collections_2024-11-30"})
        ],
        outputs=["/reports/kpi/PUB005_Collections_2024-11-30.pdf"],
    ),
    Task(
        annotator="new",
        user_id="81",
        instruction=(
            "You are a financial consulting worker recording a PUB002–PUB003 joint action log. As of '2024-11-30', you capture A/R actions for INV012, INV023, and INV008 "
            "using today '2024-11-30'; log 'second_notice' only for items overdue >60 days with notes 'Overdue >60 days'. Archive a KPI as_of '2024-11-30' with sections "
            "['Aging'] and artifact_name 'Joint_Action_Log_2024-11-30'. Return the KPI path."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV008","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV008","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Aging"],"artifact_name":"Joint_Action_Log_2024-11-30"})
        ],
        outputs=["/reports/kpi/Joint_Action_Log_2024-11-30.pdf"],
    ),
    Task(
        annotator="new",
        user_id="82",
        instruction=(
            "You are a financial consulting worker providing a PUB003 escalation note. As of '2024-11-30', you apply policy for INV008 and INV022 using today "
            "'2024-11-30'; log 'second_notice' only for items >60 days with notes 'Overdue >60 days'. Archive a KPI as_of '2024-11-30' with sections ['Aging'] "
            "and artifact_name 'PUB003_Escalation_2024-11-30'. Return the KPI path."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV008","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV008","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Aging"],"artifact_name":"PUB003_Escalation_2024-11-30"})
        ],
        outputs=["/reports/kpi/PUB003_Escalation_2024-11-30.pdf"],
    ),
    Task(
        annotator="new",
        user_id="83",
        instruction=(
            "You are a financial consulting worker issuing a PUB003–PUB005 cross-publisher actions brief. As of '2024-11-30', you record A/R actions for INV008, INV022, "
            "and INV026 using today '2024-11-30'; log 'second_notice' only for items >60 days with notes 'Overdue >60 days'. Archive a KPI as_of '2024-11-30' with sections "
            "['Collections'] and artifact_name 'PUB3_5_Cross_Brief_2024-11-30'. Return the KPI path."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV008","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV026","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV008","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV026","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"PUB3_5_Cross_Brief_2024-11-30"})
        ],
        outputs=["/reports/kpi/PUB3_5_Cross_Brief_2024-11-30.pdf"],
    ),
    Task(
        annotator="new",
        user_id="84",
        instruction=(
            "You are a financial consulting worker executing a PUB003 A/R closure. As of '2024-11-30', apply policy for INV008 and INV022 using today '2024-11-30'; "
            "log 'second_notice' only for items overdue >60 days with notes 'Overdue >60 days'. Archive a KPI as_of '2024-11-30' with sections ['Aging'] and "
            "artifact_name 'PUB003_AR_Close_2024-11-30'. Return the KPI path."
        ),
        actions=[
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV008"}),
            Action(name="get_invoice_details", kwargs={"invoice_id":"INV022"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV008","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV008","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Aging"],"artifact_name":"PUB003_AR_Close_2024-11-30"})
        ],
        outputs=["/reports/kpi/PUB003_AR_Close_2024-11-30.pdf"],
    ),
    Task(
        annotator="new",
        user_id="85",
        instruction=(
            "You are a financial consulting worker producing a consolidated actions register. As of '2024-11-30', apply policy for INV009, INV021, and INV026 "
            "using today '2024-11-30'; record 'second_notice' only for >60 days with notes 'Overdue >60 days'. Archive a KPI as_of '2024-11-30' with sections "
            "['Collections'] and artifact_name 'Consolidated_Actions_2024-11-30'. Return the KPI path."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV009","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV021","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV026","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV009","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV021","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV026","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","sections":["Collections"],"artifact_name":"Consolidated_Actions_2024-11-30"})
        ],
        outputs=["/reports/kpi/Consolidated_Actions_2024-11-30.pdf"],
    ),
    Task(
        annotator="0",
        user_id="86",
        instruction=(
            "You are a financial consulting worker assembling Q3 2024 expense governance. "
            "Use '2024-07-01'..'2024-09-30' OFFICE_SUPPLIES and TRAVEL_EXPENSE, apply deductibility to EXP012, EXP022, EXP023, "
            "generate a dashboard, and archive KPI artifact_name 'Q3_Expense_Governance_2024-09-30'. Return the dashboard path."
        ),
        actions=[
            Action(name="list_expenses_by_date_range_and_category", kwargs={"start_date":"2024-07-01","end_date":"2024-09-30","categories":["OFFICE_SUPPLIES","TRAVEL_EXPENSE"]}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id":"EXP012"}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id":"EXP022"}),
            Action(name="apply_deductibility_rules", kwargs={"expense_id":"EXP023"}),
            Action(name="generate_expense_dashboard", kwargs={"quarter":"2024-Q3","included_expenses":["EXP012","EXP022","EXP023"],"as_of":"2024-09-30","artifact_name":"Q3_Expense_Governance_2024-09-30"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-09-30","artifact_name":"Q3_Expense_Governance_2024-09-30"}),
        ],
        outputs=["/dashboards/ExpenseDashboards/2024-Q3/expense_dashboard_2024-Q3.pdf"],
    ),
    Task(
        annotator="0",
        user_id="87",
        instruction=(
            "You are reconciling the practice's November month-end 2024 tax reserve on '2024-11-30'. "
            "Compute YTD revenue for 2024 through month 11, derive the 2024 corporate tax reserve using the tax rate table, "
            "compare it to snapshot 'SNAP004' and compute an adjustment with threshold 0.01, post the adjustment to account 'Tax Reserve' with memo 'YTD tax reserve true-up', "
            "and archive a KPI artifact as_of '2024-11-30' named 'TaxReserve_Nov_Recon_2024-11'. "
            "Also persist a dashboard snapshot using the computed YTD revenue and tax reserve and the KPI pdf path. "
            "Return the adjustment amount."
        ),
        actions=[
            Action(name="compute_ytd_from_monthly_revenue", kwargs={"year": 2024, "through_month": 11}),
            Action(name="compute_tax_reserve", kwargs={"ytd_revenue": 10909.5, "tax_year": 2024}),
            Action(name="get_dashboard_snapshot", kwargs={"snapshot_id": "SNAP004"}),
            Action(name="reconcile_tax_reserve", kwargs={"computed_tax_reserve_ref": {"tax_reserve": 2891.02}, "snapshot_ref": {"ytd_tax_reserve": 2733.15}, "threshold": 0.01}),
            Action(name="post_journal_entry", kwargs={"date": "2024-11-30", "account": "Tax Reserve", "amount_ref": {"adjustment": 157.87}, "memo": "YTD tax reserve true-up"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "sections": ["TaxReserve"], "artifact_name": "TaxReserve_Nov_Recon_2024-11"}),
            Action(name="create_dashboard_snapshot", kwargs={"snapshot_date": "2024-11-30", "ytd_revenue": 10909.5, "ytd_tax_reserve": 2891.02, "pdf_path": "/reports/kpi/TaxReserve_Nov_Recon_2024-11.pdf"})
        ],
        outputs=["157.87"]
    ),
    Task(
        annotator="0",
        user_id="88",
        instruction=(
            "You are compiling a cross-publisher collections bundle as of '2024-11-30' for PUB001 and PUB003. "
            "List open invoices for PUB001 and PUB003, retrieve payment behavior for both (PUB001, PUB003), "
            "forecast expected inflows on ['INV009','INV021','INV008','INV022'] using probability_rule 'overdue_60=0.3', "
            "and archive a KPI artifact as_of '2024-11-30' with sections ['Collections','Behavior'] named 'Cross_PUB001_PUB003_2024-11-30'. "
            "Return the KPI path."
        ),
        actions=[
            Action(name="list_publisher_open_invoices", kwargs={"publisher_id": "PUB001"}),
            Action(name="list_publisher_open_invoices", kwargs={"publisher_id": "PUB003"}),
            Action(name="compute_payment_behavior", kwargs={"publisher_id": "PUB001"}),
            Action(name="compute_payment_behavior", kwargs={"publisher_id": "PUB003"}),
            Action(name="forecast_inflows", kwargs={"invoices": ["INV009", "INV021", "INV008", "INV022"], "probability_rule": "overdue_60=0.3"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "sections": ["Collections", "Behavior"], "artifact_name": "Cross_PUB001_PUB003_2024-11-30"})
        ],
        outputs=["/reports/kpi/Cross_PUB001_PUB003_2024-11-30.pdf"]
    ),
    Task(
        annotator="0",
        user_id="89",
        instruction=(
            "You are closing November 2024 tax posture as of '2024-11-30'. "
            "Confirm 2024 YTD revenue through month 11, compute the 2024 corporate tax reserve, reconcile against snapshot 'SNAP004' with a 0.01 threshold, "
            "book the resulting difference to account 'Tax Reserve' with memo 'YTD tax reserve true-up', archive a KPI artifact named 'TaxReserve_Close_2024-11', "
            "and persist a dashboard snapshot referencing the KPI path alongside computed YTD and reserve. "
            "Return 157.87."
        ),
        actions=[
            Action(name="compute_ytd_from_monthly_revenue", kwargs={"year": 2024, "through_month": 11}),
            Action(name="compute_tax_reserve", kwargs={"ytd_revenue": 10909.5, "tax_year": 2024}),
            Action(name="get_dashboard_snapshot", kwargs={"snapshot_id": "SNAP004"}),
            Action(name="reconcile_tax_reserve", kwargs={"computed_tax_reserve_ref": {"tax_reserve": 2891.02}, "snapshot_ref": {"ytd_tax_reserve": 2733.15}, "threshold": 0.01}),
            Action(name="post_journal_entry", kwargs={"date": "2024-11-30", "account": "Tax Reserve", "amount_ref": {"adjustment": 157.87}, "memo": "YTD tax reserve true-up"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "sections": ["TaxReserve"], "artifact_name": "TaxReserve_Close_2024-11"}),
            Action(name="create_dashboard_snapshot", kwargs={"snapshot_date": "2024-11-30", "ytd_revenue": 10909.5, "ytd_tax_reserve": 2891.02, "pdf_path": "/reports/kpi/TaxReserve_Close_2024-11.pdf"})
        ],
        outputs=["157.87"]
    ),
    Task(
        annotator="0",
        user_id="90",
        instruction=(
            "You are preparing a four-month cashflow view as of '2024-11-30'. "
            "Use current bank balances, active recurring schedules for 4 months with taxes included, "
            "forecast expected inflows from ['INV008','INV009','INV010'] with probability_rule 'overdue_60=0.3', "
            "build a monthly projection for 4 months, archive a KPI named 'Cashflow_4M_Outlook_2024-11-30' as_of '2024-11-30', "
            "and post a zero-value memo to account 'Liquidity Review Memo' with memo text '4-month cashflow outlook archived'. "
            "Return the KPI path."
        ),
        actions=[
            Action(name="get_bank_balances", kwargs={}),
            Action(name="list_recurring_schedules", kwargs={"horizon_months": 4}),
            Action(name="forecast_inflows", kwargs={"invoices": ["INV008", "INV009", "INV010"], "probability_rule": "overdue_60=0.3"}),
            Action(name="forecast_outflows", kwargs={"recurring_schedules": True, "taxes": True, "horizon_months": 4}),
            Action(name="build_cashflow_view", kwargs={"horizon_months": 4, "granularity": "monthly"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "sections": ["Cashflow"], "artifact_name": "Cashflow_4M_Outlook_2024-11-30"}),
            Action(name="post_journal_entry", kwargs={"date": "2024-11-30", "account": "Liquidity Review Memo", "amount_ref": {"adjustment": 0.00}, "memo": "4-month cashflow outlook archived"})
        ],
        outputs=["/reports/kpi/Cashflow_4M_Outlook_2024-11-30.pdf"]
    ),
    Task(
        annotator="0",
        user_id="91",
        instruction=(
            "You are performing a November 2024 reserve verification as of '2024-11-30'. "
            "Confirm 2024 YTD revenue through month 11, compute the 2024 reserve, reconcile to 'SNAP004' with threshold 0.01, "
            "book any difference to 'Tax Reserve' with memo 'YTD tax reserve true-up', and archive a KPI named 'TaxReserve_Verification_2024-11' as_of '2024-11-30'. "
            "Return 157.87."
        ),
        actions=[
            Action(name="compute_ytd_from_monthly_revenue", kwargs={"year": 2024, "through_month": 11}),
            Action(name="compute_tax_reserve", kwargs={"ytd_revenue": 10909.5, "tax_year": 2024}),
            Action(name="get_dashboard_snapshot", kwargs={"snapshot_id": "SNAP004"}),
            Action(name="reconcile_tax_reserve", kwargs={"computed_tax_reserve_ref": {"tax_reserve": 2891.02}, "snapshot_ref": {"ytd_tax_reserve": 2733.15}, "threshold": 0.01}),
            Action(name="post_journal_entry", kwargs={"date": "2024-11-30", "account": "Tax Reserve", "amount_ref": {"adjustment": 157.87}, "memo": "YTD tax reserve true-up"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "sections": ["TaxReserve"], "artifact_name": "TaxReserve_Verification_2024-11"})
        ],
        outputs=["157.87"]
    ),
    Task(
        annotator="0",
        user_id="92",
        instruction=(
            "You are compiling a cross-publisher collections brief as of '2024-11-30' for PUB002 and PUB005. "
            "List open invoices for those publishers, include their payment behavior, forecast expected inflows on ['INV012','INV023','INV022','INV026'] with probability_rule 'overdue_60=0.3', "
            "and archive a KPI artifact as_of '2024-11-30' with sections ['Collections','Behavior'] named 'PUB002_PUB005_Collections_2024-11-30'. "
            "Return the KPI path."
        ),
        actions=[
            Action(name="list_publisher_open_invoices", kwargs={"publisher_id": "PUB002"}),
            Action(name="list_publisher_open_invoices", kwargs={"publisher_id": "PUB005"}),
            Action(name="compute_payment_behavior", kwargs={"publisher_id": "PUB002"}),
            Action(name="compute_payment_behavior", kwargs={"publisher_id": "PUB005"}),
            Action(name="forecast_inflows", kwargs={"invoices": ["INV012", "INV023", "INV022", "INV026"], "probability_rule": "overdue_60=0.3"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "sections": ["Collections", "Behavior"], "artifact_name": "PUB002_PUB005_Collections_2024-11-30"})
        ],
        outputs=["/reports/kpi/PUB002_PUB005_Collections_2024-11-30.pdf"]
    ),
    Task(
        annotator="0",
        user_id="93",
        instruction=(
            "You are preparing a five-month cashflow outlook as of '2024-11-30'. "
            "Use current bank balances, include recurring schedules=True and taxes=True over a 5-month horizon, "
            "forecast expected inflows from invoices ['INV008','INV009','INV010'] using probability_rule 'overdue_60=0.3', "
            "build a monthly view for 5 months, archive a KPI named 'Cashflow_5M_Outlook_2024-11-30' as_of '2024-11-30', "
            "and post a zero-value memo to account 'Liquidity Review Memo' with memo text '5-month cashflow outlook archived'. "
            "Return the KPI path."
        ),
        actions=[
            Action(name="get_bank_balances", kwargs={}),
            Action(name="list_recurring_schedules", kwargs={"horizon_months": 5}),
            Action(name="forecast_inflows", kwargs={"invoices": ["INV008", "INV009", "INV010"], "probability_rule": "overdue_60=0.3"}),
            Action(name="forecast_outflows", kwargs={"recurring_schedules": True, "taxes": True, "horizon_months": 5}),
            Action(name="build_cashflow_view", kwargs={"horizon_months": 5, "granularity": "monthly"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "artifact_name": "Cashflow_5M_Outlook_2024-11-30", "sections": ["Cashflow"]}),
            Action(name="post_journal_entry", kwargs={"date": "2024-11-30", "account": "Liquidity Review Memo", "amount_ref": {"adjustment": 0.00}, "memo": "5-month cashflow outlook archived"})
        ],
        outputs=["/reports/kpi/Cashflow_5M_Outlook_2024-11-30.pdf"]
    ),
    Task(
        annotator="0",
        user_id="94",
        instruction=(
            "You are issuing a zero-total November 2024 shell invoice for 'Horizon Academic Press' (PUB003). "
            "Use invoice_id 'INV-AUTO-2024-302' and invoice_number 'INV-2024-302' with invoice_date '2024-11-30', period '2024-11-01'..'2024-11-30', "
            "apply HST at 0.13 (subtotal 0.00), archive the PDF, and log an audit event 'generated' with notes 'Invoice generated'. "
            "Also archive a KPI as_of '2024-11-30' named 'PUB003_Shell_Issue_2024-11'. "
            "Return 'INV-2024-302'."
        ),
        actions=[
            Action(name="calculate_totals", kwargs={"invoice_lines": [], "hst_rate": 0.13}),
            Action(name="compose_invoice_pdf", kwargs={"invoice_id": "INV-AUTO-2024-302", "publisher_id": "PUB003"}),
            Action(name="insert_invoice", kwargs={
                "invoice_id": "INV-AUTO-2024-302",
                "publisher_id": "PUB003",
                "subtotal": 0.00,
                "hst_amount": 0.00,
                "total_due": 0.00,
                "invoice_number": "INV-2024-302",
                "invoice_date": "2024-11-30",
                "period_start": "2024-11-01",
                "period_end": "2024-11-30",
                "pdf_path": "/invoices/auto/INV-AUTO-2024-302.pdf"
            }),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV-AUTO-2024-302", "event_type": "generated", "notes": "Invoice generated"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "artifact_name": "PUB003_Shell_Issue_2024-11", "sections": []})
        ],
        outputs=["INV-2024-302"]
    ),
    Task(
        annotator="0",
        user_id="95",
        instruction=(
            "You are enforcing PUB002 A/R actions as of '2024-11-30'. "
            "List PUB002 open items, compute aging for INV012 and INV023 with today '2024-11-30', log 'second_notice' with notes 'Overdue >60 days' where applicable, "
            "and archive a KPI as_of '2024-11-30' named 'PUB002_Actions_2024-11-30'. "
            "Return two arrays: acted and escalated (>60 days)."
        ),
        actions=[
            Action(name="list_publisher_open_invoices", kwargs={"publisher_id": "PUB002"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV012", "today": "2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id": "INV023", "today": "2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV012", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id": "INV023", "event_type": "second_notice", "notes": "Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-11-30", "artifact_name": "PUB002_Actions_2024-11-30", "sections": []})
        ],
        outputs=[["INV012", "INV023"], ["INV012", "INV023"]]
    ),
    Task(
        annotator="0",
        user_id="96",
        instruction=(
            "You are confirming Q2-2024 MEALS_ENTERTAIN governance. "
            "Scan '2024-04-01'..'2024-06-30' with threshold 150.0, note no exceptions, post a zero-value memo to account 'Governance Memo' with memo 'Q2 meals scan – no exceptions', "
            "and archive a KPI as_of '2024-06-30' named 'Q2_Meals_Scan_2024-06-30'. "
            "Return the KPI path."
        ),
        actions=[
            Action(name="list_expenses_by_date_range_and_category", kwargs={"start_date": "2024-04-01", "end_date": "2024-06-30", "categories": ["MEALS_ENTERTAIN"]}),
            Action(name="flag_high_value_meals", kwargs={"expenses_ref": {"expenses": [{"expense_id": "EXP019", "category_code": "MEALS_ENTERTAIN", "gross_amount": 18.75}]}, "threshold": 150.0}),
            Action(name="post_journal_entry", kwargs={"date": "2024-06-30", "account": "Governance Memo", "amount_ref": {"adjustment": 0.00}, "memo": "Q2 meals scan – no exceptions"}),
            Action(name="build_kpi_report", kwargs={"as_of": "2024-06-30", "artifact_name": "Q2_Meals_Scan_2024-06-30", "sections": []})
        ],
        outputs=["/reports/kpi/Q2_Meals_Scan_2024-06-30.pdf"]
    ),
    Task(
        annotator="0",
        user_id="97",
        instruction=(
            "You are enforcing A/R follow-ups for 'Maple Leaf Publishing House' (PUB001) as of '2024-11-30'. "
            "Work only open items INV009 and INV021; items over 60 days must carry a 'second_notice' with notes 'Overdue >60 days'. "
            "Archive a KPI as_of '2024-11-30' named 'PUB001_Enforcement_2024-11-30' with sections ['Collections']. "
            "Return two arrays: acted and escalated (>60 days)."
        ),
        actions=[
            Action(name="list_publisher_open_invoices", kwargs={"publisher_id":"PUB001"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV009","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV021","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV009","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV021","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB001_Enforcement_2024-11-30","sections":["Collections"]}),
        ],
        outputs=[["INV009","INV021"],["INV009","INV021"]]
    ),
    Task(
        annotator="0",
        user_id="98",
        instruction=(
            "You are creating a PUB002 collections memo as of '2024-11-30'. "
            "Work open items INV012 and INV023; items >60 days must have a 'second_notice' noted 'Overdue >60 days'. "
            "Archive KPI 'PUB002_Collections_Memo_2024-11-30' as_of '2024-11-30' with sections ['Collections']. "
            "Return two arrays: acted and escalated (>60 days)."
        ),
        actions=[
            Action(name="list_publisher_open_invoices", kwargs={"publisher_id":"PUB002"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV012","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV023","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV012","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV023","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB002_Collections_Memo_2024-11-30","sections":["Collections"]}),
        ],
        outputs=[["INV012","INV023"],["INV012","INV023"]]
    ),
    Task(
        annotator="0",
        user_id="99",
        instruction=(
            "You are producing a PUB003 enforcement update as of '2024-11-30'. "
            "Apply policy to INV008 and INV022 using today '2024-11-30'; items >60 days require 'second_notice' with notes 'Overdue >60 days'. "
            "Archive KPI 'PUB003_Enforcement_Update_2024-11-30' as_of '2024-11-30' with sections ['Aging','Collections']. "
            "Return acted and escalated (>60 days) lists."
        ),
        actions=[
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV008","today":"2024-11-30"}),
            Action(name="compute_invoice_aging", kwargs={"invoice_id":"INV022","today":"2024-11-30"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV008","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="create_audit_entry", kwargs={"invoice_id":"INV022","event_type":"second_notice","notes":"Overdue >60 days"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"PUB003_Enforcement_Update_2024-11-30","sections":["Aging","Collections"]}),
        ],
        outputs=[["INV008","INV022"],["INV008","INV022"]]
    ),
    Task(
        annotator="0",
        user_id="100",
        instruction=(
            "You are confirming the November 2024 tax reserve at month_end '2024-11-30'. "
            "Compute 2024 YTD through month 11 and the 2024 reserve; reconcile to 'SNAP004' with 0.01 threshold, book the difference to 'Tax Reserve' "
            "with memo 'YTD tax reserve true-up', and archive KPI 'TaxReserve_Confirm_2024-11' as_of '2024-11-30' with sections ['TaxReserve']. "
            "Return 157.87."
        ),
        actions=[
            Action(name="compute_ytd_from_monthly_revenue", kwargs={"year":2024,"through_month":11}),
            Action(name="compute_tax_reserve", kwargs={"ytd_revenue":10909.5,"tax_year":2024}),
            Action(name="get_dashboard_snapshot", kwargs={"snapshot_id":"SNAP004"}),
            Action(name="reconcile_tax_reserve", kwargs={"computed_tax_reserve_ref":{"tax_reserve":2891.02},"snapshot_ref":{"ytd_tax_reserve":2733.15},"threshold":0.01}),
            Action(name="post_journal_entry", kwargs={"date":"2024-11-30","account":"Tax Reserve","amount_ref":{"adjustment":157.87},"memo":"YTD tax reserve true-up"}),
            Action(name="build_kpi_report", kwargs={"as_of":"2024-11-30","artifact_name":"TaxReserve_Confirm_2024-11","sections":["TaxReserve"]}),
        ],
        outputs=["157.87"]
    ),
    
]