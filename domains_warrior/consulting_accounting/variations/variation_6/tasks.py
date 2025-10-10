from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="v6",
        user_id="task_01",
        instruction=(
            "You produce the August 2025 Accounts Receivable report for all open invoices issued through 2025-08-23, "
            "and you archive a dashboard snapshot. Use period label '2025-08' and set the exact PDF "
            "location to 'https://test.storage.com/reports/accounts_receivable_2025-08.pdf'. Compute collection "
            "KPIs over a 12-month window. Create a dashboard snapshot dated '2025-08-23' that references "
            "that same PDF path. Success means the report path equals that URL and a snapshot exists for "
            "2025-08-23 with that exact pdf_path."
        ),
        actions=[
            Action(
                name="query_invoices",
                kwargs={"status": "open", "date_to": "2025-08-23"},
            ),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="render_accounts_receivable_report",
                kwargs={"period_label": "2025-08"},
            ),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "snapshot_date": "2025-08-23",
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2025-08.pdf",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot", kwargs={"snapshot_date": "2025-08-23"}
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2025-08.pdf')",
            "dashboard_snapshot('2025-08-23')",
            "kpis(window_months=12)",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_02",
        instruction="You confirm your immediate due status and submit an export with proofing in September 2024. "
                    "Your end state: days outstanding for '2024-024' using period_end '2024-10-31' and today '2024-10-29' "
                    "are computed as -2 days and categorized as 'upcoming_due'; open invoices are reviewed; "
                    "the Account Receivable aging PDF exists for '2024-09' and a dashboard snapshot for '2024-09-30' "
                    "referencing 'https://test.storage.com/reports/accounts_receivable_2024-09.pdf' is saved and readable by id; "
                    "an audit event 'risk_reviewed' is recorded for '2024-024' and is listable.",
        actions=[
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-024", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-10-29",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": -2, "invoice_number": "2024-024"}]
                },
            ),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-09.pdf",
                    "snapshot_date": "2024-09-30",
                },
            ),
            Action(name="fetch_dashboard_snapshot", kwargs={"snapshot_id": 1}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "risk_reviewed", "invoice_number": "2024-024"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-024"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
            "dashboard_snapshot('2024-09-30')",
            "audit_event('2024-024','risk_reviewed')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_03",
        instruction="You formalize a November‑2024 email for invoice '2024-010' and capture the audit with context. "
                    "Your end state: invoice_number '2024-010' is emailed using publisher_id 'PUB004' and consultant_id '"
                    "CONS001' with subject 'Invoice 2024-010 (November 2024)', body 'Please see attached invoice 2024-010.' "
                    "and attachment 'https://test.storage.com/invoices/2024/INV-2024-010.pdf', and the "
                    "invoice is re‑read with sent_at populated; an audit event 'emailed' is recorded and listable; "
                    "open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'.",
        actions=[
            Action(
                name="dispatch_invoice_email",
                kwargs={
                    "attachment": "https://test.storage.com/invoices/2024/INV-2024-010.pdf",
                    "body_text": "Please see attached invoice 2024-010.",
                    "consultant_id": "CONS001",
                    "invoice_number": "2024-010",
                    "publisher_id": "PUB004",
                    "subject": "Invoice 2024-010 (November 2024)",
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-010"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "emailed", "invoice_number": "2024-010"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-010"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "audit_event('2024-010','emailed')",
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_04",
        instruction="You update contact info and confirm a September‑2024 total with context. Your end state: publisher_id 'PUB003' contact_email is updated to 'accounts@canopypress.ca' and is readable; consultant_id 'CONS001' phone is updated to '+1-416-555-0199' and is readable; open invoices (status 'open') are reviewed and 12‑month KPIs computed; resolve rates for ['PROJ001','PROJ003'] and compute sample totals (3h @85.0 and 2h @75.0 with hst_rate 0.13); export Account Receivable aging '2024-09'. Each write is verified via a subsequent read.",
        actions=[
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "accounts@canopypress.ca",
                    "publisher_id": "PUB003",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB003"}),
            Action(
                name="mutate_consultant_contact",
                kwargs={"consultant_id": "CONS001", "phone": "+1-416-555-0199"},
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ001", "PROJ003"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 3, "rate": 85.0}, {"hours": 2, "rate": 75.0}],
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_05",
        instruction="You add publisher_id 'PUB056' named 'Cobalt Creek Press' and prepare a September‑2024 sample with rates. Your end state: 'PUB056' exists and is readable; project_id 'PROJ3083' exists with isbn '978-1-3100-3083-6', project_title 'Intro Sociology, 1e', default_hourly_rate 86.0 and is readable; rates are resolved for ['PROJ3083','PROJ001']; a sample total is computed (2h @86.0 and 1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-09'.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Cobalt Creek Press", "publisher_id": "PUB056"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB056"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 86.0,
                    "isbn": "978-1-3100-3083-6",
                    "project_id": "PROJ3083",
                    "project_title": "Intro Sociology, 1e",
                    "publisher_id": "PUB056",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ3083"}),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ3083", "PROJ001"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 86.0}, {"hours": 1, "rate": 85.0}],
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_06",
        instruction="You record a September‑2024 invoice for publisher_id 'PUB001' and log its audit, validating time entries first. Your end state: a representative time‑entry row with description 'September hours', isbn '978-1-3100-0001-0', account_code 'ENG-1E' and hours_worked 6 is validated; invoice_number '2024-132' exists for period_start '2024-09-01' and period_end '2024-09-30' with totals (subtotal 510.0, hst_amount 66.3, total_due 576.3) and is readable; an audit event 'generated' is recorded and listable; the Account Receivable aging PDF exists for '2024-09'. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-132.pdf'.",
        actions=[
            Action(
                name="audit_time_entries",
                kwargs={
                    "rows": [
                        {
                            "account_code": "ENG-1E",
                            "description": "September hours",
                            "hours_worked": 6,
                            "isbn": "978-1-3100-0001-0",
                        }
                    ]
                },
            ),
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 66.3,
                    "invoice_date": "2024-09-30",
                    "invoice_number": "2024-132",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-132.pdf",
                    "period_end": "2024-09-30",
                    "period_start": "2024-09-01",
                    "publisher_id": "PUB001",
                    "subtotal": 510.0,
                    "total_due": 576.3,
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-132"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "generated", "invoice_number": "2024-132"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-132"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "invoice_pdf('https://test.storage.com/invoices/2024/INV-2024-132.pdf')",
            "audit_event('2024-132','generated')",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_07",
        instruction="You run an Account Receivable health pass and onboard a new client. Your end state: new publisher_id 'PUB011' exists with exactly name 'Canopy Learning Ltd.', address '77 Front St E, Toronto, ON', contact_email 'ap@canopylearning.ca', gst_number 'GST-999-011' and is readable; 12‑month collection KPIs (window_months 12) are computed; the Account Receivable aging for period_label '2024-09' is exported; and publisher_id 'PUB003' has contact_email updated to 'ap@canopypress.ca' and is readable. Each write is verified via a subsequent read.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={
                    "address": "77 Front St E, Toronto, ON",
                    "contact_email": "ap@canopylearning.ca",
                    "gst_number": "GST-999-011",
                    "name": "Canopy Learning Ltd.",
                    "publisher_id": "PUB011",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB011"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
            Action(
                name="mutate_client_contact",
                kwargs={"contact_email": "ap@canopypress.ca", "publisher_id": "PUB003"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB003"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_08",
        instruction="You normalize contacts and verify an October‑2024 sample for publisher_id 'PUB003' with an aging categorization. Your end state: 'PUB003' contact_email equals 'accounts@canopypress.ca' and is readable; CONS001 address equals '1234 Oak Street, Toronto, ON M5V 3A8' and is readable; rates are resolved for ['PROJ003']; a sample total is computed (2h @75.0 with hst_rate 0.13); days outstanding for '2024-010' as of '2024-11-15' using period_end '2024-10-31' (15 days) are categorized; the Account Receivable aging PDF exists for '2024-10'.",
        actions=[
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "accounts@canopypress.ca",
                    "publisher_id": "PUB003",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB003"}),
            Action(
                name="mutate_consultant_contact",
                kwargs={
                    "address": "1234 Oak Street, Toronto, ON M5V 3A8",
                    "consultant_id": "CONS001",
                },
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ003"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 75.0}]},
            ),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-15",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 15, "invoice_number": "2024-010"}]
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_09",
        instruction="You open publisher_id 'PUB024' named 'Aurora Study House' and align September‑2024 reporting. Your end state: 'PUB024' exists and is visible; open invoices are reviewed; KPIs over 12 months are available; the Account Receivable aging PDF exists for '2024-09' and a snapshot is saved for '2024-09-30' referencing that PDF; a sample total is computed (2h @85.0 and 2h @75.0 with hst_rate 0.13) using rates for ['PROJ001','PROJ003'].",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Aurora Study House", "publisher_id": "PUB024"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB024"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-09.pdf",
                    "snapshot_date": "2024-09-30",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-09-30"},
            ),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ001", "PROJ003"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 85.0}, {"hours": 2, "rate": 75.0}],
                },
            ),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
            "dashboard_snapshot('2024-09-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_10",
        instruction="You compute and categorize a November‑2024 aging check and verify context with a saved snapshot. Your end state: days outstanding for invoice '2024-021' as of '2024-11-20' using period_end '2024-10-31' (20 days) are categorized; projects are listed; 'PROJ003' details are readable; rates are resolved for ['PROJ003']; a sample total is computed (1h @75.0 with hst_rate 0.13); open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'; a dashboard snapshot is stored for '2024-11-30' and is readable by date.",
        actions=[
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-021", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-20",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 20, "invoice_number": "2024-021"}]
                },
            ),
            Action(name="list_projects_catalog", kwargs={}),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ003"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ003"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 75.0}]},
            ),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-11-30"},
            ),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
            "dashboard_snapshot('2024-11-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_11",
        instruction="You ensure November‑2024 readiness for publisher_id 'PUB004' by creating a data science project and confirming totals with an aging categorization. Your end state: project_id 'PROJ3081' exists with isbn '978-1-3100-3081-2', project_title 'Data Science Projects, 1e', default_hourly_rate 106.0 and is readable; rates are resolved for ['PROJ3081']; a sample total is computed (1h @106.0 with hst_rate 0.13); open invoices are reviewed; the Account Receivable aging PDF exists for '2024-11'; days outstanding for '2024-010' as of '2024-11-15' using period_end '2024-10-31' (15 days) are categorized.",
        actions=[
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 106.0,
                    "isbn": "978-1-3100-3081-2",
                    "project_id": "PROJ3081",
                    "project_title": "Data Science Projects, 1e",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ3081"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ3081"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 106.0}]},
            ),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-15",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 15, "invoice_number": "2024-010"}]
                },
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_12",
        instruction="You add a focused writing project and align October‑2024 reporting for publisher_id 'PUB004'. Your end state: project_id 'PROJ1011' exists with isbn '978-1-3100-1011-0', project_title 'Writing Workshop, 1e', default_hourly_rate 94.0 and is visible; 'PUB004' is readable; rates are resolved for ['PROJ1011','PROJ001'] and a sample total is computed (2h @94.0 and 3h @85.0 with hst_rate 0.13); open invoices are reviewed and 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-10' and a snapshot is saved for '2024-10-31' referencing that PDF.",
        actions=[
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 94.0,
                    "isbn": "978-1-3100-1011-0",
                    "project_id": "PROJ1011",
                    "project_title": "Writing Workshop, 1e",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ1011"}),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB004"}),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ1011", "PROJ001"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 94.0}, {"hours": 3, "rate": 85.0}],
                },
            ),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
            "dashboard_snapshot('2024-10-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_13",
        instruction="You create publisher_id 'PUB045' named 'Northern Summit Press' and prepare a July‑2024 sample. Your end state: 'PUB045' exists and is readable; project_id 'PROJ3059' exists with isbn '978-1-3100-3059-6', project_title 'Intro Philosophy, 1e', default_hourly_rate 87.0 and is readable; rates are resolved for ['PROJ3059','PROJ001']; a sample total is computed (1h @87.0 and 1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-07'.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Northern Summit Press", "publisher_id": "PUB045"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB045"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 87.0,
                    "isbn": "978-1-3100-3059-6",
                    "project_id": "PROJ3059",
                    "project_title": "Intro Philosophy, 1e",
                    "publisher_id": "PUB045",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ3059"}),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ3059", "PROJ001"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 1, "rate": 87.0}, {"hours": 1, "rate": 85.0}],
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-07"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-07.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_14",
        instruction="You formalize a September‑2024 invoice for publisher_id 'PUB003' and log its audit. Your end state: invoice_number '2024-142' exists for period_start '2024-09-01' and period_end '2024-09-30' with correct totals (2h @97.0, hst_rate 0.13) and is readable; a single line is inserted for project_id 'PROJ003' with isbn '978-1-3100-0003-7' for 2h @97.0 and is listable; an audit event 'generated' is recorded and listable. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-142.pdf'.",
        actions=[
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 25.22,
                    "invoice_date": "2024-09-30",
                    "invoice_number": "2024-142",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-142.pdf",
                    "period_end": "2024-09-30",
                    "period_start": "2024-09-01",
                    "publisher_id": "PUB003",
                    "subtotal": 194.0,
                    "total_due": 219.22,
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-142"}),
            Action(
                name="create_invoice_lines",
                kwargs={
                    "invoice_number": "2024-142",
                    "lines": [
                        {
                            "hours": 2,
                            "isbn": "978-1-3100-0003-7",
                            "project_id": "PROJ003",
                            "rate": 97.0,
                        }
                    ],
                },
            ),
            Action(name="list_invoice_lines_by_invoice", kwargs={"invoice_number": "2024-142"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "generated", "invoice_number": "2024-142"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-142"}),
        ],
        outputs=[
            "invoice_pdf('https://test.storage.com/invoices/2024/INV-2024-142.pdf')",
            "audit_event('2024-142','generated')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_15",
        instruction="You formalize a November‑2024 email for invoice '2024-010' and capture the audit with context. "
                    "Your end state: invoice_number '2024-010' is emailed using publisher_id 'PUB004' and consultant_id '"
                    "CONS001' with subject 'Invoice 2024-010 (November 2024)', body 'Please see attached invoice 2024-010.' "
                    "and attachment 'https://test.storage.com/invoices/2024/INV-2024-010.pdf', and the "
                    "invoice is re‑read with sent_at populated; an audit event 'emailed' is recorded and listable; "
                    "open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'.",
        actions=[
            Action(
                name="dispatch_invoice_email",
                kwargs={
                    "attachment": "https://test.storage.com/invoices/2024/INV-2024-010.pdf",
                    "body_text": "Please see attached invoice 2024-010.",
                    "consultant_id": "CONS001",
                    "invoice_number": "2024-010",
                    "publisher_id": "PUB004",
                    "subject": "Invoice 2024-010 (November 2024)",
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-010"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "emailed", "invoice_number": "2024-010"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-010"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "audit_event('2024-010','emailed')",
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_16",
        instruction="You onboard publisher_id 'PUB040' named 'Red Maple Learning' and add a math project, then build a September‑2024 snapshot. Your end state: 'PUB040' exists and is readable; project_id 'PROJ2053' exists with isbn '978-1-3100-2053-4', project_title 'Pre‑Calculus, 1e', default_hourly_rate 99.0 and is readable; a sample total is computed (2h @99.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-09' and a dashboard snapshot is stored for '2024-09-30' referencing 'https://test.storage.com/reports/accounts_receivable_2024-09.pdf' and is readable by id.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Red Maple Learning", "publisher_id": "PUB040"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB040"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 99.0,
                    "isbn": "978-1-3100-2053-4",
                    "project_id": "PROJ2053",
                    "project_title": "Pre‑Calculus, 1e",
                    "publisher_id": "PUB040",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ2053"}),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 99.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-09.pdf",
                    "snapshot_date": "2024-09-30",
                },
            ),
            Action(name="fetch_dashboard_snapshot", kwargs={"snapshot_id": 1}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
            "dashboard_snapshot('2024-09-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_17",
        instruction="You create a November‑2024 invoice for publisher_id 'PUB005' and log its audit. Your end state: before invoicing, you validate a representative time‑entry row with description 'Hours for November', isbn '978-1-3100-2027-8', account_code 'DATA-LIT-1E' and hours_worked 3; you compute totals for a single line (3h @90.0, hst_rate 0.13); invoice_number '2024-130' exists for period_start '2024-11-01' and period_end '2024-11-30' with those totals and is readable; an audit event 'generated' is recorded and listable. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-130.pdf'.",
        actions=[
            Action(
                name="audit_time_entries",
                kwargs={
                    "rows": [
                        {
                            "account_code": "DATA-LIT-1E",
                            "description": "Hours for November",
                            "hours_worked": 3,
                            "isbn": "978-1-3100-2027-8",
                        }
                    ]
                },
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 90.0}]},
            ),
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 35.1,
                    "invoice_date": "2024-11-30",
                    "invoice_number": "2024-130",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-130.pdf",
                    "period_end": "2024-11-30",
                    "period_start": "2024-11-01",
                    "publisher_id": "PUB005",
                    "subtotal": 270.0,
                    "total_due": 305.1,
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-130"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "generated", "invoice_number": "2024-130"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-130"}),
        ],
        outputs=[
            "invoice_pdf('https://test.storage.com/invoices/2024/INV-2024-130.pdf')",
            "audit_event('2024-130','generated')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_18",
        instruction="You normalize contact info and complete a September‑2024 review for publisher_id 'PUB001'. Your end state: contact_email equals 'ap@nelson-edu.ca' and is readable; invoice_number '2024-021' is readable; an audit event 'review_follow_up' is recorded for '2024-021' and listed; Account Receivable aging for '2024-09' is exported and a dashboard snapshot is stored for '2024-09-30'; a quick risk check computes days outstanding for '2024-021' using due_date '2024-09-15' with today '2024-10-01' and categorizes it.",
        actions=[
            Action(
                name="mutate_client_contact",
                kwargs={"contact_email": "ap@nelson-edu.ca", "publisher_id": "PUB001"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB001"}),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-021"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "review_follow_up", "invoice_number": "2024-021"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-021"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-09.pdf",
                    "snapshot_date": "2024-09-30",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-09-30"},
            ),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {
                            "due_date": "2024-09-15",
                            "invoice_date": "2024-09-15",
                            "invoice_number": "2024-021",
                        }
                    ],
                    "today": "2024-10-01",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 16, "invoice_number": "2024-021"}]
                },
            ),
        ],
        outputs=[
            "audit_event('2024-021','review_follow_up')",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
            "dashboard_snapshot('2024-09-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_19",
        instruction="You add publisher_id 'PUB057' named 'Harbor Lights Learning' and stage an August‑2024 dashboard with a small total. Your end state: 'PUB057' exists and is readable; a sample total is computed (1h @85.0 with hst_rate 0.13) using rate for ['PROJ001']; the Account Receivable aging PDF exists for '2024-08'; a dashboard snapshot is stored for '2024-08-31' and is readable by date; days outstanding for '2024-010' as of '2024-08-15' using period_end '2024-07-31' (15 days) are categorized.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Harbor Lights Learning", "publisher_id": "PUB057"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB057"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 85.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-07-31"}
                    ],
                    "today": "2024-08-15",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 15, "invoice_number": "2024-010"}]
                },
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
            "dashboard_snapshot('2024-08-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_20",
        instruction="You create a September‑2024 invoice for publisher_id 'PUB003'. Your end state: invoice_number '2024-131' exists for period_start '2024-09-01' and period_end '2024-09-30' with totals subtotal 388.0, hst_amount 50.44, total_due 438.44 using hst_rate 0.13 and is readable; invoice lines are inserted for project_id 'PROJ2032' with isbn '978-1-3100-2032-2' (4h @97.0) and are listable; an audit event 'generated' is recorded and listable. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-131.pdf'.",
        actions=[
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 50.44,
                    "invoice_date": "2024-09-30",
                    "invoice_number": "2024-131",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-131.pdf",
                    "period_end": "2024-09-30",
                    "period_start": "2024-09-01",
                    "publisher_id": "PUB003",
                    "subtotal": 388.0,
                    "total_due": 438.44,
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-131"}),
            Action(
                name="create_invoice_lines",
                kwargs={
                    "invoice_number": "2024-131",
                    "lines": [
                        {
                            "hours": 4,
                            "isbn": "978-1-3100-2032-2",
                            "project_id": "PROJ2032",
                            "rate": 97.0,
                        }
                    ],
                },
            ),
            Action(name="list_invoice_lines_by_invoice", kwargs={"invoice_number": "2024-131"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "generated", "invoice_number": "2024-131"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-131"}),
        ],
        outputs=[
            "invoice_pdf('https://test.storage.com/invoices/2024/INV-2024-131.pdf')",
            "audit_event('2024-131','generated')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_21",
        instruction="You add publisher_id 'PUB039' named 'Coastal Curriculum Press' and stage a dual export. Your end state: 'PUB039' exists and is visible; the Account Receivable aging PDFs exist for '2024-08' and '2024-09'; a dashboard snapshot is stored for '2024-08-31' referencing the '2024-08' PDF and is readable; open invoices are reviewed.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Coastal Curriculum Press", "publisher_id": "PUB039"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB039"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
            Action(name="query_invoices", kwargs={"status": "open"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
            "dashboard_snapshot('2024-08-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_22",
        instruction="You register publisher_id 'PUB037' named 'Seaway Academics' and compile a September‑2024 snapshot. Your end state: 'PUB037' exists and is readable; project_id 'PROJ2046' exists under 'PUB037' with isbn '978-1-3100-2046-1', project_title 'Statistics Primer, 1e', default_hourly_rate 95.0 and is readable; a sample total is computed (2h @95.0 with hst_rate 0.13); open invoices are reviewed; the Account Receivable aging PDF exists for '2024-09' and a snapshot is saved for '2024-09-30' referencing 'https://test.storage.com/reports/accounts_receivable_2024-09.pdf' and is readable by id.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Seaway Academics", "publisher_id": "PUB037"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB037"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 95.0,
                    "isbn": "978-1-3100-2046-1",
                    "project_id": "PROJ2046",
                    "project_title": "Statistics Primer, 1e",
                    "publisher_id": "PUB037",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ2046"}),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 95.0}]},
            ),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-09.pdf",
                    "snapshot_date": "2024-09-30",
                },
            ),
            Action(name="fetch_dashboard_snapshot", kwargs={"snapshot_id": 1}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
            "dashboard_snapshot('2024-09-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_23",
        instruction="You add publisher_id 'PUB041' named 'Evergreen Academic House' and a writing project, then confirm October‑2024 totals. Your end state: 'PUB041' exists and is visible; 'PROJ2055' exists with isbn '978-1-3100-2055-8', project_title 'Essay Skills, 1e', default_hourly_rate 91.0 and is visible; rates resolve for ['PROJ2055','PROJ001'] and a sample total is computed (2h @91.0 and 1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-10'.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Evergreen Academic House", "publisher_id": "PUB041"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB041"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 91.0,
                    "isbn": "978-1-3100-2055-8",
                    "project_id": "PROJ2055",
                    "project_title": "Essay Skills, 1e",
                    "publisher_id": "PUB041",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ2055"}),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ2055", "PROJ001"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 91.0}, {"hours": 1, "rate": 85.0}],
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_24",
        instruction="You update October‑2024 contacts and run KPIs with a quick risk check. Your end state: publisher_id 'PUB004' contact_email equals 'ap@bluepeakpublishing.ca' and is readable; open invoices are reviewed and 12‑month KPIs are available; Account Receivable aging for '2024-10' is exported and a snapshot stored for '2024-10-31'; for risk, days outstanding are computed for invoice_number '2024-024' using due_date '2024-10-31' as of '2024-11-05' and categorized.",
        actions=[
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "ap@bluepeakpublishing.ca",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB004"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {
                            "due_date": "2024-10-31",
                            "invoice_date": "2024-10-31",
                            "invoice_number": "2024-024",
                        }
                    ],
                    "today": "2024-11-05",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 5, "invoice_number": "2024-024"}]
                },
            ),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
            "dashboard_snapshot('2024-10-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_25",
        instruction="You register publisher_id 'PUB052' named 'Aurora Ridge Press' and store a November‑2024 snapshot with a small sample. Your end state: 'PUB052' exists and is readable; open invoices are reviewed; 12‑month KPIs are available; rates are resolved for ['PROJ001']; a sample total is computed (1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-11'; a dashboard snapshot is stored for '2024-11-30' and is readable by date.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Aurora Ridge Press", "publisher_id": "PUB052"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB052"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 85.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-11-30"},
            ),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
            "dashboard_snapshot('2024-11-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_26",
        instruction="You formalize the November‑2024 email step for a pending invoice. Your end state: invoice_number '2024-011' is emailed using publisher_id 'PUB005' and consultant_id 'CONS001' with subject 'Invoice 2024-011 (November 2024)', body 'Friendly reminder: attached is invoice 2024-011.' and attachment 'https://test.storage.com/invoices/2024/INV-2024-011.pdf', and the invoice is re‑read with sent_at populated; an audit event 'emailed' is recorded and listable; open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'.",
        actions=[
            Action(
                name="dispatch_invoice_email",
                kwargs={
                    "attachment": "https://test.storage.com/invoices/2024/INV-2024-011.pdf",
                    "body_text": "Friendly reminder: attached is invoice 2024-011.",
                    "consultant_id": "CONS001",
                    "invoice_number": "2024-011",
                    "publisher_id": "PUB005",
                    "subject": "Invoice 2024-011 (November 2024)",
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-011"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "emailed", "invoice_number": "2024-011"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-011"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "audit_event('2024-011','emailed')",
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_27",
        instruction=(
            "You open a new publisher and align a November-2024 review. "
            "Your end state: publisher_id 'PUB022' named 'Bayview K12' exists and is readable; "
            "project_id 'PROJ1104' exists under 'PUB022' with isbn '978-1-3100-1013-2', "
            "project_title 'Civics Basics, 1e', default_hourly_rate 80.0, and is readable; "
            "rates are resolved for ['PROJ1104']; "
            "you compute a sample total for 6h @80.0 via compute_invoice_totals using HST rate 0.13; "
            "open invoices are reviewed and 12-month KPIs are available; "
            "Accounts Receivable aging for '2024-11' is exported (PDF: 'https://test.storage.com/reports/accounts_receivable_2024-11.pdf'); "
            "a dashboard snapshot for '2024-11-30' exists and is readable by snapshot_date—if an entry already exists for that date, you rely on it; "
            "otherwise you store a snapshot for '2024-11-30' using the same A/R PDF and then verify it by fetching with the snapshot_date."
        ),
    actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Bayview K12", "publisher_id": "PUB022"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB022"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 80.0,
                    "isbn": "978-1-3100-1013-2",
                    "project_id": "PROJ1104",
                    "project_title": "Civics Basics, 1e",
                    "publisher_id": "PUB022",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ1104"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ1104"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 6, "rate": 80.0}]},
            ),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-11-30"},
            ),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
            "dashboard_snapshot('2024-11-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_28",
        instruction="You update GST references and verify July‑2024 Account Receivable. Your end state: publisher_id 'PUB002' gst_number equals 'GST-UPDATED-002' and is visible; consultant_id 'CONS001' gst_number equals '123456789RT0001' and is visible; open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-07'.",
        actions=[
            Action(
                name="mutate_client_contact",
                kwargs={"gst_number": "GST-UPDATED-002", "publisher_id": "PUB002"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB002"}),
            Action(
                name="mutate_consultant_contact",
                kwargs={"consultant_id": "CONS001", "gst_number": "123456789RT0001"},
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-07"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-07.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_29",
        instruction="You reconcile July‑2024 Account Receivable for publisher_id 'PUB002'. Your end state: publisher_id 'PUB002' is readable; a risk check computes days outstanding for invoice_number '2024-023' using due_date '2024-07-15' as of '2024-07-20' and categorizes it; Account Receivable aging for '2024-07' is exported and a snapshot is stored for '2024-07-31'.",
        actions=[
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB002"}),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-023", "period_end": "2024-07-15"}
                    ],
                    "today": "2024-07-20",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 5, "invoice_number": "2024-023"}]
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-07"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-07.pdf",
                    "snapshot_date": "2024-07-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-07-31"},
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-07.pdf')",
            "dashboard_snapshot('2024-07-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_30",
        instruction="You generate an October‑2024 invoice for publisher_id 'PUB004'. Your end state: invoice_number '2024-120' exists for period_start '2024-10-01' and period_end '2024-10-31' with correct totals for a single line (5h @102.0 with hst_rate 0.13) and is readable; a line is inserted for project_id 'PROJ2024' with isbn '978-1-3100-2024-6' (5h @102.0) and is listable; the Account Receivable aging PDF exists for period label '2024-10'. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-120.pdf'.",
        actions=[
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 5, "rate": 102.0}]},
            ),
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 66.3,
                    "invoice_date": "2024-10-31",
                    "invoice_number": "2024-120",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-120.pdf",
                    "period_end": "2024-10-31",
                    "period_start": "2024-10-01",
                    "publisher_id": "PUB004",
                    "subtotal": 510.0,
                    "total_due": 576.3,
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-120"}),
            Action(
                name="create_invoice_lines",
                kwargs={
                    "invoice_number": "2024-120",
                    "lines": [
                        {
                            "hours": 5,
                            "isbn": "978-1-3100-2024-6",
                            "project_id": "PROJ2024",
                            "rate": 102.0,
                        }
                    ],
                },
            ),
            Action(name="list_invoice_lines_by_invoice", kwargs={"invoice_number": "2024-120"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "invoice_pdf('https://test.storage.com/invoices/2024/INV-2024-120.pdf')",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_31",
        instruction="You normalize contact data and produce a September‑2024 Account Receivable snapshot for validation. Your end state: publisher_id 'PUB001' contact_email equals 'accounts@nelson-edu.ca' and is visible; consultant_id 'CONS001' email equals 'sarah.thompson@consultingpro.ca' and is visible; open invoices (status 'open') are reviewed and 12‑month KPIs are available; rates are resolved for ['PROJ001'] and a sample total is computed (6h @85.0 with hst_rate 0.13); Account Receivable aging PDFs exist for period labels '2024-09' and '2024-08'; projects are listed and details for 'PROJ001' are visible; representative open invoices '2024-009' and '2024-021' are readable, and an audit event 'reviewed' is recorded for '2024-009' and listed.",
        actions=[
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "accounts@nelson-edu.ca",
                    "publisher_id": "PUB001",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB001"}),
            Action(
                name="mutate_consultant_contact",
                kwargs={
                    "consultant_id": "CONS001",
                    "email": "sarah.thompson@consultingpro.ca",
                },
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 6, "rate": 85.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
            Action(name="list_projects_catalog", kwargs={}),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ001"}),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-009"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "reviewed", "invoice_number": "2024-009"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-009"}),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-021"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
            "audit_event('2024-009','reviewed')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_32",
        instruction="You add publisher_id 'PUB042' named 'Bright Horizons Press' and capture a November‑2024 dashboard. Your end state: 'PUB042' exists and is readable; open invoices are reviewed and 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11' and a dashboard snapshot is saved for '2024-11-30' referencing that PDF and is readable by id; a representative invoice '2024-021' is readable; for confirmation, the rate resolves for ['PROJ001'] and a sample total is computed (2h @85.0 with hst_rate 0.13).",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Bright Horizons Press", "publisher_id": "PUB042"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB042"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(name="fetch_dashboard_snapshot", kwargs={"snapshot_id": 1}),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-021"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 85.0}]},
            ),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
            "dashboard_snapshot('2024-11-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_33",
        instruction="You add publisher_id 'PUB051' named 'Maple Grove Education' and register a writing project for an October‑2024 check. Your end state: 'PUB051' exists and is readable; project_id 'PROJ3073' exists with isbn '978-1-3100-3073-8', project_title 'Advanced Composition, 1e', default_hourly_rate 95.0 and is readable; rates are resolved for ['PROJ3073','PROJ001']; a sample total is computed (2h @95.0 and 1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-10'.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Maple Grove Education", "publisher_id": "PUB051"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB051"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 95.0,
                    "isbn": "978-1-3100-3073-8",
                    "project_id": "PROJ3073",
                    "project_title": "Advanced Composition, 1e",
                    "publisher_id": "PUB051",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ3073"}),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ3073", "PROJ001"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 95.0}, {"hours": 1, "rate": 85.0}],
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_34",
        instruction="You generate an August‑2024 invoice for publisher_id 'PUB002' and log its audit. Your end state: invoice_number '2024-146' exists for period_start '2024-08-01' and period_end '2024-08-31' with correct totals (2h @85.0, hst_rate 0.13) and is readable; one line is inserted for 'PROJ001' with isbn '978-1-3100-0001-0' (2h @85.0) and is listable; an audit event 'generated' is recorded and listable. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-146.pdf'.",
        actions=[
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 22.1,
                    "invoice_date": "2024-08-31",
                    "invoice_number": "2024-146",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-146.pdf",
                    "period_end": "2024-08-31",
                    "period_start": "2024-08-01",
                    "publisher_id": "PUB002",
                    "subtotal": 170.0,
                    "total_due": 192.1,
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-146"}),
            Action(
                name="create_invoice_lines",
                kwargs={
                    "invoice_number": "2024-146",
                    "lines": [
                        {
                            "hours": 2,
                            "isbn": "978-1-3100-0001-0",
                            "project_id": "PROJ001",
                            "rate": 85.0,
                        }
                    ],
                },
            ),
            Action(name="list_invoice_lines_by_invoice", kwargs={"invoice_number": "2024-146"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "generated", "invoice_number": "2024-146"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-146"}),
        ],
        outputs=[
            "invoice_pdf('https://test.storage.com/invoices/2024/INV-2024-146.pdf')",
            "audit_event('2024-146','generated')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_35",
        instruction="You tidy September‑2024 contact details and log an upcoming‑due classification with context. Your end state: publisher_id 'PUB001' contact_email equals 'accounts@nelson-edu.ca' and is readable; days outstanding for invoice '2024-024' as of '2024-09-29' using period_end '2024-10-01' (‑2 days) are categorized as 'upcoming_due'; an invoice audit event 'aging_categorized' is recorded for '2024-024' and listable; open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-09'.",
        actions=[
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "accounts@nelson-edu.ca",
                    "publisher_id": "PUB001",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB001"}),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-024", "period_end": "2024-10-01"}
                    ],
                    "today": "2024-09-29",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": -2, "invoice_number": "2024-024"}]
                },
            ),
            Action(
                name="log_invoice_event",
                kwargs={
                    "event_type": "aging_categorized",
                    "invoice_number": "2024-024",
                },
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-024"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "audit_event('2024-024','aging_categorized')",
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_36",
        instruction="You create a concise July‑2024 invoice for publisher_id 'PUB004' and log audit. Your end state: invoice_number '2024-134' exists for period_start '2024-07-01' and period_end '2024-07-31' with totals (subtotal 340.0, hst_amount 44.2, total_due 384.2) and is readable; one line is inserted for project_id 'PROJ001' with isbn '978-1-3100-0001-0' (4h @85.0) and is listable; an audit event 'generated' is recorded and listable. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-134.pdf'.",
        actions=[
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 44.2,
                    "invoice_date": "2024-07-31",
                    "invoice_number": "2024-134",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-134.pdf",
                    "period_end": "2024-07-31",
                    "period_start": "2024-07-01",
                    "publisher_id": "PUB004",
                    "subtotal": 340.0,
                    "total_due": 384.2,
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-134"}),
            Action(
                name="create_invoice_lines",
                kwargs={
                    "invoice_number": "2024-134",
                    "lines": [
                        {
                            "hours": 4,
                            "isbn": "978-1-3100-0001-0",
                            "project_id": "PROJ001",
                            "rate": 85.0,
                        }
                    ],
                },
            ),
            Action(name="list_invoice_lines_by_invoice", kwargs={"invoice_number": "2024-134"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "generated", "invoice_number": "2024-134"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-134"}),
        ],
        outputs=[
            "invoice_pdf('https://test.storage.com/invoices/2024/INV-2024-134.pdf')",
            "audit_event('2024-134','generated')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_37",
        instruction="You formalize a November‑2024 email for invoice '2024-010' and capture the audit with context. "
                    "Your end state: invoice_number '2024-010' is emailed using publisher_id 'PUB004' and consultant_id '"
                    "CONS001' with subject 'Invoice 2024-010 (November 2024)', body 'Please see attached invoice 2024-010.' "
                    "and attachment 'https://test.storage.com/invoices/2024/INV-2024-010.pdf', and the "
                    "invoice is re‑read with sent_at populated; an audit event 'emailed' is recorded and listable; "
                    "open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'.",
        actions=[
            Action(
                name="dispatch_invoice_email",
                kwargs={
                    "attachment": "https://test.storage.com/invoices/2024/INV-2024-010.pdf",
                    "body_text": "Please see attached invoice 2024-010.",
                    "consultant_id": "CONS001",
                    "invoice_number": "2024-010",
                    "publisher_id": "PUB004",
                    "subject": "Invoice 2024-010 (November 2024)",
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-010"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "emailed", "invoice_number": "2024-010"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-010"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "audit_event('2024-010','emailed')",
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_38",
        instruction="You onboard publisher_id 'PUB043' named 'Evergreen Learning Co.' and stage an October‑2024 baseline. Your end state: 'PUB043' exists and is readable; project_id 'PROJ3053' under 'PUB043' exists with isbn '978-1-3100-3053-1', project_title 'Media Literacy, 1e', default_hourly_rate 93.0 and is readable; rates are resolved for ['PROJ3053','PROJ001']; a sample total is computed (2h @93.0 and 1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-10'; a dashboard snapshot is stored for '2024-10-31' referencing that PDF and is readable by date.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Evergreen Learning Co.", "publisher_id": "PUB043"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB043"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 93.0,
                    "isbn": "978-1-3100-3053-1",
                    "project_id": "PROJ3053",
                    "project_title": "Media Literacy, 1e",
                    "publisher_id": "PUB043",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ3053"}),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ3053", "PROJ001"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 93.0}, {"hours": 1, "rate": 85.0}],
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
            "dashboard_snapshot('2024-10-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_39",
        instruction="You register a data‑science project and complete an October‑2024 risk pass for publisher_id 'PUB004'. Your end state: project_id 'PROJ1105' exists with isbn '978-1-3100-1014-9', project_title 'Data Science Labs, 1e', default_hourly_rate 105.0 and is readable; a sample total is computed (4h @105.0 with hst_rate 0.13); Account Receivable aging '2024-10' is exported and a snapshot stored for '2024-10-31'; a risk check computes days outstanding for invoice_number '2024-024' using due_date '2024-10-31' as of '2024-11-10' and categorizes it.",
        actions=[
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 105.0,
                    "isbn": "978-1-3100-1014-9",
                    "project_id": "PROJ1105",
                    "project_title": "Data Science Labs, 1e",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ1105"}),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 4, "rate": 105.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-024", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-10",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 10, "invoice_number": "2024-024"}]
                },
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
            "dashboard_snapshot('2024-10-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_40",
        instruction="You add a STEM project and check November‑2024 risk. Your end state: project_id 'PROJ1013' exists under 'PUB003' with isbn '978-1-3100-1013-4', project_title 'Applied Physics, 1e', default_hourly_rate 98.0 and is visible; open invoices are reviewed and 12‑month KPIs are available; a sample total is computed (4h @98.0 with hst_rate 0.13); for risk, days outstanding are computed for invoice '2024-010' as of '2024-11-15' (15 days) and categorized.",
        actions=[
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 98.0,
                    "isbn": "978-1-3100-1013-4",
                    "project_id": "PROJ1013",
                    "project_title": "Applied Physics, 1e",
                    "publisher_id": "PUB003",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ1013"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 4, "rate": 98.0}]},
            ),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-15",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 15, "invoice_number": "2024-010"}]
                },
            ),
        ],
        outputs=[
            "kpis(window_months=12)",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_41",
        instruction="You build a January‑2025 risk classification for two invoices and confirm September Account Receivable. Your end state: as of '2025-01-15', days outstanding are computed for '2024-026' with period_end '2024-06-30' and '2024-013' with period_end '2024-06-15' resulting in 199 and 214 days and are categorized; open invoices for publisher_id 'PUB001' are reviewed; the Account Receivable aging PDF exists for '2024-09'; an audit event 'risk_categorized' is recorded for '2024-026' and is listable.",
        actions=[
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-026", "period_end": "2024-06-30"},
                        {"invoice_number": "2024-013", "period_end": "2024-06-15"},
                    ],
                    "today": "2025-01-15",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [
                        {"days_outstanding": 199, "invoice_number": "2024-026"},
                        {"days_outstanding": 214, "invoice_number": "2024-013"},
                    ]
                },
            ),
            Action(
                name="query_invoices",
                kwargs={"publisher_id": "PUB001", "status": "open"},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "risk_categorized", "invoice_number": "2024-026"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-026"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
            "audit_event('2024-026','risk_categorized')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_42",
        instruction="You align rates and contacts for a September‑2024 confirmation. Your end state: consultant_id 'CONS001' email equals 'accounts+ar@consultingpro.ca' and is visible; publisher_id 'PUB001' contact_email equals 'ap@nelson-edu.ca' and is visible; rates are resolved for ['PROJ001','PROJ003'] and a sample total is computed (2h @85.0 and 2h @75.0 with hst_rate 0.13); open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-09'.",
        actions=[
            Action(
                name="mutate_consultant_contact",
                kwargs={
                    "consultant_id": "CONS001",
                    "email": "accounts+ar@consultingpro.ca",
                },
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(
                name="mutate_client_contact",
                kwargs={"contact_email": "ap@nelson-edu.ca", "publisher_id": "PUB001"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB001"}),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ001", "PROJ003"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 85.0}, {"hours": 2, "rate": 75.0}],
                },
            ),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_43",
        instruction="You verify August‑2024 context around 'PROJ003' and add proper proofing. Your end state: projects are listed and 'PROJ003' details are readable; rates resolve for ['PROJ003'] and a sample total is computed (5h @75.0 with hst_rate 0.13); open invoices are reviewed and 12‑month KPIs are available; the Account Receivable aging for '2024-08' is exported and a dashboard snapshot for '2024-08-31' referencing 'https://test.storage.com/reports/accounts_receivable_2024-08.pdf' is saved and readable by id; an audit event 'reviewed' is recorded for invoice '2024-009' and listable.",
        actions=[
            Action(name="list_projects_catalog", kwargs={}),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ003"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ003"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 5, "rate": 75.0}]},
            ),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(name="fetch_dashboard_snapshot", kwargs={"snapshot_id": 1}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "reviewed", "invoice_number": "2024-009"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-009"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
            "dashboard_snapshot('2024-08-31')",
            "audit_event('2024-009','reviewed')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_44",
        instruction="You open publisher_id 'PUB034' named 'Silver Birch Academic' and finalize a November‑2024 aging snapshot with context. Your end state: 'PUB034' exists and is readable; open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11' and a dashboard snapshot is saved for '2024-11-30' referencing that PDF and is readable by id; for confirmation, the rate resolves for ['PROJ001'] and a sample total is computed (2h @85.0, hst_rate 0.13).",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Silver Birch Academic", "publisher_id": "PUB034"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB034"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(name="fetch_dashboard_snapshot", kwargs={"snapshot_id": 1}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 85.0}]},
            ),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
            "dashboard_snapshot('2024-11-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_45",
        instruction="You create project_id 'PROJ1018' for 'PUB004' and compute a November‑2024 sample. Your end state: 'PROJ1018' exists with isbn '978-1-3100-1018-9', project_title 'Intro Data Science, 2e', default_hourly_rate 105.0 and is visible; a sample total is computed (4h @105.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-11'.",
        actions=[
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 105.0,
                    "isbn": "978-1-3100-1018-9",
                    "project_id": "PROJ1018",
                    "project_title": "Intro Data Science, 2e",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ1018"}),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 4, "rate": 105.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_46",
        instruction="You record an October‑2024 invoice for publisher_id 'PUB005' and verify its line items. Your end state: invoice_number '2024-147' exists for period_start '2024-10-01' and period_end '2024-10-31' with correct totals (4h @90.0, hst_rate 0.13) and is readable; a single line is inserted for project_id 'PROJ003' with isbn '978-1-3100-0003-7' (4h @90.0) and is listable; an audit event 'generated' is recorded and listable. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-147.pdf'.",
        actions=[
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 46.8,
                    "invoice_date": "2024-10-31",
                    "invoice_number": "2024-147",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-147.pdf",
                    "period_end": "2024-10-31",
                    "period_start": "2024-10-01",
                    "publisher_id": "PUB005",
                    "subtotal": 360.0,
                    "total_due": 406.8,
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-147"}),
            Action(
                name="create_invoice_lines",
                kwargs={
                    "invoice_number": "2024-147",
                    "lines": [
                        {
                            "hours": 4,
                            "isbn": "978-1-3100-0003-7",
                            "project_id": "PROJ003",
                            "rate": 90.0,
                        }
                    ],
                },
            ),
            Action(name="list_invoice_lines_by_invoice", kwargs={"invoice_number": "2024-147"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "generated", "invoice_number": "2024-147"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-147"}),
        ],
        outputs=[
            "invoice_pdf('https://test.storage.com/invoices/2024/INV-2024-147.pdf')",
            "audit_event('2024-147','generated')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_47",
        instruction="You refresh November‑2024 context and categorize a representative invoice, storing a dashboard snapshot. Your end state: open invoices are reviewed; 12‑month KPIs are available; days outstanding for invoice '2024-009' as of '2024-11-15' using period_end '2024-09-30' (46 days) are categorized; the Account Receivable aging PDF exists for '2024-11'; a dashboard snapshot is stored for '2024-11-30' referencing that PDF and is readable by date.",
        actions=[
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-009", "period_end": "2024-09-30"}
                    ],
                    "today": "2024-11-15",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 46, "invoice_number": "2024-009"}]
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-11-30"},
            ),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
            "dashboard_snapshot('2024-11-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_48",
        instruction="You set up publisher_id 'PUB053' named 'Pine Valley Learning' and confirm an August‑2024 math sample. Your end state: 'PUB053' exists and is readable; project_id 'PROJ3076' exists with isbn '978-1-3100-3076-7', project_title 'Linear Algebra, 1e', default_hourly_rate 101.0 and is readable; a sample total is computed (2h @101.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-08'.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Pine Valley Learning", "publisher_id": "PUB053"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB053"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 101.0,
                    "isbn": "978-1-3100-3076-7",
                    "project_id": "PROJ3076",
                    "project_title": "Linear Algebra, 1e",
                    "publisher_id": "PUB053",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ3076"}),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 101.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_49",
        instruction="You establish a November‑2024 readiness context for publisher_id 'PUB003'. Your end state: project_id 'PROJ999' exists under 'PUB003' with isbn '978-1-3100-0007-3', project_title 'Literature Survey, 1e', default_hourly_rate 91.0 and is visible; 'PUB003' is readable; open invoices (status 'open') are reviewed and 12‑month collection KPIs are available; rates are resolved for ['PROJ999','PROJ003'] and sample totals are computed (1h @91.0 and 2h @91.0 with hst_rate 0.13); an Account Receivable aging PDF exists for period label '2024-11'; projects are listed and details for 'PROJ003' are visible;",
        actions=[
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 91.0,
                    "isbn": "978-1-3100-0007-3",
                    "project_id": "PROJ999",
                    "project_title": "Literature Survey, 1e",
                    "publisher_id": "PUB003",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ999"}),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB003"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ999", "PROJ003"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 1, "rate": 91.0}, {"hours": 2, "rate": 91.0}],
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
            Action(name="list_projects_catalog", kwargs={}),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ003"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_50",
        instruction="You open publisher_id 'PUB031' named 'Cardinal Academic' and register a November‑2024 package. Your end state: 'PUB031' exists and is readable; project_id 'PROJ2026A' exists under 'PUB031' with isbn '978-1-3100-2026-1', project_title 'Advanced Writing, 1e', default_hourly_rate 96.0 and is readable; the rate is resolved for ['PROJ2026A'] and a sample total is computed (3h @96.0 with hst_rate 0.13); open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11' and a dashboard snapshot is stored for '2024-11-30' referencing 'https://test.storage.com/reports/accounts_receivable_2024-11.pdf' and is readable by id.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Cardinal Academic", "publisher_id": "PUB031"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB031"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 96.0,
                    "isbn": "978-1-3100-2026-1",
                    "project_id": "PROJ2026A",
                    "project_title": "Advanced Writing, 1e",
                    "publisher_id": "PUB031",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ2026A"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ2026A"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 96.0}]},
            ),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(name="fetch_dashboard_snapshot", kwargs={"snapshot_id": 1}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
            "dashboard_snapshot('2024-11-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_51",
        instruction=(
            "You onboard 'Everest Academy' and run an October-2024 check. "
            "Your end state: publisher_id 'PUB024' named 'Everest Academy' exists and is readable; "
            "open invoices are reviewed and 12-month KPIs are available; "
            "rates are resolved for ['PROJ001']; "
            "you compute a sample total for 2h @85.0 via compute_invoice_totals using HST rate 0.13; "
            "Accounts Receivable aging for '2024-10' is exported (PDF: 'https://test.storage.com/reports/accounts_receivable_2024-10.pdf'); "
            "a dashboard snapshot for '2024-10-31' exists and is readable by snapshot_date—if no snapshot exists for that date, you store one using the same A/R PDF; "
            "for risk, you compute days outstanding for invoice_number '2024-021' as of '2024-10-10' using due_date '2024-09-15' and categorize it into aging buckets."
        ),
    actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Everest Academy", "publisher_id": "PUB024"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB024"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 85.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {
                            "due_date": "2024-09-15",
                            "invoice_date": "2024-09-15",
                            "invoice_number": "2024-021",
                        }
                    ],
                    "today": "2024-10-10",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 25, "invoice_number": "2024-021"}]
                },
            ),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
            "dashboard_snapshot('2024-10-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_52",
        instruction="You formalize an August‑2024 invoice for publisher_id 'PUB005' from an algebra project. Your end state: project_id 'PROJ2056' exists with isbn '978-1-3100-2056-5', project_title 'Algebra Toolkit, 1e', default_hourly_rate 92.0 and is readable; invoice_number '2024-135' exists for period_start '2024-08-01' and period_end '2024-08-31' with correct totals (3h @92.0, hst_rate 0.13) and is readable; an audit event 'generated' is recorded and listable. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-135.pdf'.",
        actions=[
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 92.0,
                    "isbn": "978-1-3100-2056-5",
                    "project_id": "PROJ2056",
                    "project_title": "Algebra Toolkit, 1e",
                    "publisher_id": "PUB005",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ2056"}),
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 35.88,
                    "invoice_date": "2024-08-31",
                    "invoice_number": "2024-135",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-135.pdf",
                    "period_end": "2024-08-31",
                    "period_start": "2024-08-01",
                    "publisher_id": "PUB005",
                    "subtotal": 276.0,
                    "total_due": 311.88,
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-135"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "generated", "invoice_number": "2024-135"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-135"}),
        ],
        outputs=[
            "invoice_pdf('https://test.storage.com/invoices/2024/INV-2024-135.pdf')",
            "audit_event('2024-135','generated')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_53",
        instruction="You prepare a July‑2024 billing overview and refresh key contacts. Fetch time entries for ['PROJ001','PROJ003'] from 2024-07-01 to 2024-07-31, resolve rates for those projects, and run a sample two‑line totals using the resolved rates (12h @85.0 and 8h @75.0, HST 0.13). Update CONS001 email to sarah.thompson+billing@consultingpro.ca and read it back. Update PUB002 AP email to ap@northernlights-edu.ca and read it back. Export the Account Receivable aging for period label 2024-07.",
        actions=[
            Action(
                name="read_time_entries",
                kwargs={
                    "period_end": "2024-07-31",
                    "period_start": "2024-07-01",
                    "project_id_list": ["PROJ001", "PROJ003"],
                },
            ),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ001", "PROJ003"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 12, "rate": 85.0}, {"hours": 8, "rate": 75.0}],
                },
            ),
            Action(
                name="mutate_consultant_contact",
                kwargs={
                    "consultant_id": "CONS001",
                    "email": "sarah.thompson+billing@consultingpro.ca",
                },
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "ap@northernlights-edu.ca",
                    "publisher_id": "PUB002",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB002"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-07"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-07.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_54",
        instruction="You create a concise August‑2024 invoice for publisher_id 'PUB002' and log its lifecycle. Your end state: invoice_number '2024-133' exists for period_start '2024-08-01' and period_end '2024-08-31' with totals (subtotal 300.0, hst_amount 39.0, total_due 339.0) and is readable; a single line is inserted for 'PROJ003' with isbn '978-1-3100-0003-7' (4h @75.0) and is listable; an audit event 'generated' is recorded and listable. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-133.pdf'.",
        actions=[
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 39.0,
                    "invoice_date": "2024-08-31",
                    "invoice_number": "2024-133",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-133.pdf",
                    "period_end": "2024-08-31",
                    "period_start": "2024-08-01",
                    "publisher_id": "PUB002",
                    "subtotal": 300.0,
                    "total_due": 339.0,
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-133"}),
            Action(
                name="create_invoice_lines",
                kwargs={
                    "invoice_number": "2024-133",
                    "lines": [
                        {
                            "hours": 4,
                            "isbn": "978-1-3100-0003-7",
                            "project_id": "PROJ003",
                            "rate": 75.0,
                        }
                    ],
                },
            ),
            Action(name="list_invoice_lines_by_invoice", kwargs={"invoice_number": "2024-133"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "generated", "invoice_number": "2024-133"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-133"}),
        ],
        outputs=[
            "invoice_pdf('https://test.storage.com/invoices/2024/INV-2024-133.pdf')",
            "audit_event('2024-133','generated')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_55",
        instruction="You update contact info and verify August‑2024 totals. Your end state: 'CONS001' phone equals '+1-647-555-2244' and is visible; 'PUB004' is readable; rates resolve for ['PROJ001'] and a sample total is computed (4h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-08'.",
        actions=[
            Action(
                name="mutate_consultant_contact",
                kwargs={"consultant_id": "CONS001", "phone": "+1-647-555-2244"},
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB004"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 4, "rate": 85.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_56",
        instruction="You establish publisher_id 'PUB033' named 'Prairie Learning Co.' and stage a September‑2024 snapshot. Your end state: 'PUB033' exists and is readable; project_id 'PROJ2034' exists with isbn '978-1-3100-2034-6', project_title 'Prairie Math, 1e', default_hourly_rate 89.0 and is readable; a sample total is computed (3h @89.0, hst_rate 0.13); open invoices are reviewed; the Account Receivable aging PDF exists for '2024-09' and a dashboard snapshot is stored for '2024-09-30' referencing 'https://test.storage.com/reports/accounts_receivable_2024-09.pdf' and is readable by id.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Prairie Learning Co.", "publisher_id": "PUB033"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB033"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 89.0,
                    "isbn": "978-1-3100-2034-6",
                    "project_id": "PROJ2034",
                    "project_title": "Prairie Math, 1e",
                    "publisher_id": "PUB033",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ2034"}),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 89.0}]},
            ),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-09.pdf",
                    "snapshot_date": "2024-09-30",
                },
            ),
            Action(name="fetch_dashboard_snapshot", kwargs={"snapshot_id": 1}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
            "dashboard_snapshot('2024-09-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_57",
        instruction="You create a September‑2024 invoice for publisher_id 'PUB002' with one line and record its audit. Your end state: invoice_number '2024-144' exists for period_start '2024-09-01' and period_end '2024-09-30' with correct totals (3h @75.0, hst_rate 0.13) and is readable; a single line is inserted for 'PROJ003' with isbn '978-1-3100-0003-7' (3h @75.0) and is listable; an audit event 'generated' is recorded and listable. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-144.pdf'.",
        actions=[
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 29.25,
                    "invoice_date": "2024-09-30",
                    "invoice_number": "2024-144",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-144.pdf",
                    "period_end": "2024-09-30",
                    "period_start": "2024-09-01",
                    "publisher_id": "PUB002",
                    "subtotal": 225.0,
                    "total_due": 254.25,
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-144"}),
            Action(
                name="create_invoice_lines",
                kwargs={
                    "invoice_number": "2024-144",
                    "lines": [
                        {
                            "hours": 3,
                            "isbn": "978-1-3100-0003-7",
                            "project_id": "PROJ003",
                            "rate": 75.0,
                        }
                    ],
                },
            ),
            Action(name="list_invoice_lines_by_invoice", kwargs={"invoice_number": "2024-144"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "generated", "invoice_number": "2024-144"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-144"}),
        ],
        outputs=[
            "invoice_pdf('https://test.storage.com/invoices/2024/INV-2024-144.pdf')",
            "audit_event('2024-144','generated')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_58",
        instruction="You add project_id 'PROJ3054' for publisher_id 'PUB005' and confirm a November‑2024 sample with an explicit aging check. Your end state: 'PROJ3054' exists with isbn '978-1-3100-3054-8', project_title 'Canadian Literature, 2e', default_hourly_rate 90.0 and is readable; rates are resolved for ['PROJ3054']; a sample total is computed (3h @90.0 with hst_rate 0.13); days outstanding for '2024-010' as of '2024-11-15' using period_end '2024-10-31' (15 days) are categorized; the Account Receivable aging PDF exists for '2024-11'.",
        actions=[
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 90.0,
                    "isbn": "978-1-3100-3054-8",
                    "project_id": "PROJ3054",
                    "project_title": "Canadian Literature, 2e",
                    "publisher_id": "PUB005",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ3054"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ3054"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 90.0}]},
            ),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-15",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 15, "invoice_number": "2024-010"}]
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_59",
        instruction="You normalize contacts and produce a July‑2024 risk view. Your end state: publisher_id 'PUB002' contact_email equals 'ap@northernlights-edu.ca' and is visible; consultant_id 'CONS001' gst_number equals '123456789RT0001' and is visible; open invoices are reviewed and 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-07'; days outstanding are computed for '2024-023' as of '2024-08-01' (17 days) and categorized; projects are listed and 'PROJ003' details are visible.",
        actions=[
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "ap@northernlights-edu.ca",
                    "publisher_id": "PUB002",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB002"}),
            Action(
                name="mutate_consultant_contact",
                kwargs={"consultant_id": "CONS001", "gst_number": "123456789RT0001"},
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-07"}),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-023", "period_end": "2024-07-15"}
                    ],
                    "today": "2024-08-01",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 17, "invoice_number": "2024-023"}]
                },
            ),
            Action(name="list_projects_catalog", kwargs={}),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ003"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-07.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_60",
        instruction="You add publisher_id 'PUB054' named 'Aspen Trail Press' and stage a September‑2024 readiness check. Your end state: 'PUB054' exists and is readable; project_id 'PROJ3078' exists with isbn '978-1-3100-3078-1', project_title 'World History, 1e', default_hourly_rate 92.0 and is readable; rates are resolved for ['PROJ3078']; a sample total is computed (3h @92.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-09'.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Aspen Trail Press", "publisher_id": "PUB054"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB054"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 92.0,
                    "isbn": "978-1-3100-3078-1",
                    "project_id": "PROJ3078",
                    "project_title": "World History, 1e",
                    "publisher_id": "PUB054",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ3078"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ3078"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 92.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_61",
        instruction="You refresh AP contacts and verify October‑2024 Account Receivable for two publishers. Your end state: 'PUB004' contact_email equals 'ap@bluepeakpublishing.ca' and is visible; 'PUB005' contact_email equals 'ap@westwoodpress.ca' and is visible; open invoices are reviewed; 12‑month KPIs are available; projects are listed and 'PROJ004' details are visible; the Account Receivable aging PDF exists for '2024-10'.",
        actions=[
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "ap@bluepeakpublishing.ca",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB004"}),
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "ap@westwoodpress.ca",
                    "publisher_id": "PUB005",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB005"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="list_projects_catalog", kwargs={}),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ004"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_62",
        instruction="You introduce publisher_id 'PUB013' named 'Maple STEM Press' and align a September‑2024 billing check. Your end state: 'PUB013' exists with name 'Maple STEM Press' and is readable; publisher_id 'PUB002' is readable; open invoices (status 'open') are reviewed and 12‑month KPIs are computed; you resolve rates for ['PROJ003'] and compute sample totals (6h @75.0 and 2h @75.0 with hst_rate 0.13); you export the Account Receivable aging for '2024-09'. Each write is verified via a subsequent read.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Maple STEM Press", "publisher_id": "PUB013"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB013"}),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB002"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ003"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 6, "rate": 75.0}, {"hours": 2, "rate": 75.0}],
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_63",
        instruction="You tidy November‑2024 contact data and compute a confirmation total with context. Your end state: publisher_id 'PUB005' contact_email is updated to 'ap@westwoodpress.ca' and is readable; consultant_id 'CONS001' email is updated to 'sarah.thompson@consultingpro.ca' and is readable; open invoices (status 'open') are reviewed and 12‑month KPIs computed; you resolve rates for ['PROJ003'] and compute a sample total (2h @75.0 with hst_rate 0.13); export Account Receivable aging '2024-11'. Each write is verified via a subsequent read.",
        actions=[
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "ap@westwoodpress.ca",
                    "publisher_id": "PUB005",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB005"}),
            Action(
                name="mutate_consultant_contact",
                kwargs={
                    "consultant_id": "CONS001",
                    "email": "sarah.thompson@consultingpro.ca",
                },
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ003"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 75.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_64",
        instruction="You formalize a September‑2024 invoice for publisher_id 'PUB004' with one project and verify context. Your end state: invoice_number '2024-148' exists for period_start '2024-09-01' and period_end '2024-09-30' with correct totals (2h @85.0, hst_rate 0.13) and is readable; a single line is inserted for 'PROJ001' (2h @85.0, isbn '978-1-3100-0001-0') and is listable; an audit event 'generated' is recorded and listable. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-148.pdf'.",
        actions=[
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 22.1,
                    "invoice_date": "2024-09-30",
                    "invoice_number": "2024-148",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-148.pdf",
                    "period_end": "2024-09-30",
                    "period_start": "2024-09-01",
                    "publisher_id": "PUB004",
                    "subtotal": 170.0,
                    "total_due": 192.1,
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-148"}),
            Action(
                name="create_invoice_lines",
                kwargs={
                    "invoice_number": "2024-148",
                    "lines": [
                        {
                            "hours": 2,
                            "isbn": "978-1-3100-0001-0",
                            "project_id": "PROJ001",
                            "rate": 85.0,
                        }
                    ],
                },
            ),
            Action(name="list_invoice_lines_by_invoice", kwargs={"invoice_number": "2024-148"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "generated", "invoice_number": "2024-148"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-148"}),
        ],
        outputs=[
            "invoice_pdf('https://test.storage.com/invoices/2024/INV-2024-148.pdf')",
            "audit_event('2024-148','generated')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_65",
        instruction=(
            "You onboard a new client and align an October-2024 snapshot. "
            "Your end state: publisher_id 'PUB021' named 'Algonquin Scholastic' exists and is readable; "
            "project_id 'PROJ1102' exists under 'PUB021' with isbn '978-1-3100-1010-1', "
            "project_title 'Intro Statistics, 1e', default_hourly_rate 95.0, and is readable; "
            "rates are resolved for ['PROJ1102','PROJ001']; "
            "you compute sample totals for 3h @95.0 and 2h @85.0 using HST rate 0.13 (hst_rate=0.13); "
            "Accounts Receivable aging for '2024-10' is exported and a snapshot is stored for '2024-10-31' using the same PDF."
        ),
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Algonquin Scholastic", "publisher_id": "PUB021"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB021"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 95.0,
                    "isbn": "978-1-3100-1010-1",
                    "project_id": "PROJ1102",
                    "project_title": "Intro Statistics, 1e",
                    "publisher_id": "PUB021",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ1102"}),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ1102", "PROJ001"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 3, "rate": 95.0}, {"hours": 2, "rate": 85.0}],
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
            "dashboard_snapshot('2024-10-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_66",
        instruction="You update contacts and confirm a September‑2024 total. Your end state: 'PUB003' contact_email equals 'accounts@canopypress.ca' and is visible; 'CONS001' phone equals '+1-416-555-0199' and is visible; rates resolve for ['PROJ001','PROJ003'] and sample totals are computed (3h @85.0 and 2h @75.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-09'.",
        actions=[
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "accounts@canopypress.ca",
                    "publisher_id": "PUB003",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB003"}),
            Action(
                name="mutate_consultant_contact",
                kwargs={"consultant_id": "CONS001", "phone": "+1-416-555-0199"},
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ001", "PROJ003"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 3, "rate": 85.0}, {"hours": 2, "rate": 75.0}],
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_67",
        instruction="You add publisher_id 'PUB050' named 'Riverbend Academic' and store an August‑2024 dashboard with a small sample. Your end state: 'PUB050' exists and is readable; open invoices are reviewed; 12‑month KPIs are available; rates are resolved for ['PROJ001']; a sample total is computed (1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-08'; a dashboard snapshot is stored for '2024-08-31' and is readable by date.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Riverbend Academic", "publisher_id": "PUB050"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB050"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 85.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
            "dashboard_snapshot('2024-08-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_68",
        instruction="You validate November‑2024 visibility and a representative invoice. Your end state: projects are listed and 'PROJ001' details are readable; open invoices are reviewed and 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'; for confirmation, the rate resolves for ['PROJ001'] and a sample total is computed (1h @85.0 with hst_rate 0.13); invoice '2024-025' is readable; an audit event 'reviewed' is recorded for '2024-025' and is listable.",
        actions=[
            Action(name="list_projects_catalog", kwargs={}),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ001"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 85.0}]},
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-025"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "reviewed", "invoice_number": "2024-025"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-025"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
            "audit_event('2024-025','reviewed')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_69",
        instruction=(
            "You create a social studies project and reconcile a July-2024 snapshot. "
            "Your end state: project_id 'PROJ1109' exists for 'PUB005' with isbn '978-1-3100-1018-7', "
            "project_title 'Social Studies, 1e', default_hourly_rate 90.0, and is readable; "
            "sample totals are calculated for two time entries (2h @90.0 and 2h @90.0) using HST rate 0.13; "
            "Accounts Receivable aging for '2024-07' is exported and available at 'https://test.storage.com/reports/accounts_receivable_2024-07.pdf'; "
            "a dashboard snapshot dated '2024-07-31' exists, is readable by snapshot_date, and references the same A/R PDF."
        ),
    actions=[
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 90.0,
                    "isbn": "978-1-3100-1018-7",
                    "project_id": "PROJ1109",
                    "project_title": "Social Studies, 1e",
                    "publisher_id": "PUB005",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ1109"}),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 90.0}, {"hours": 2, "rate": 90.0}],
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-07"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-07.pdf",
                    "snapshot_date": "2024-07-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-07-31"},
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-07.pdf')",
            "dashboard_snapshot('2024-07-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_70",
        instruction="You establish publisher_id 'PUB027' named 'North Coast Education' and complete an August snapshot. Your end state: 'PUB027' exists and is visible; the Account Receivable aging PDF exists for '2024-08' and a snapshot is saved for '2024-08-31' referencing that PDF; a sample total is computed (5h @85.0 with hst_rate 0.13) using rates for ['PROJ001'].",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "North Coast Education", "publisher_id": "PUB027"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB027"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 5, "rate": 85.0}]},
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
            "dashboard_snapshot('2024-08-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_71",
        instruction="You ensure base records and contacts are in place and then produce an August‑2024 context snapshot. Your end state: publisher_id 'PUB010' exists with exactly name 'Maple Leaf Educational', address '100 Bloor St W, Toronto, ON', contact_email 'ap@mapleleafedu.ca', gst_number 'GST-999-010' and is readable; publisher_id 'PUB002' contact_email is updated to 'ap@northernlights-edu.ca' and is readable; consultant_id 'CONS001' phone is updated to '+1-416-555-0199' and is readable; August‑2024 time entries for ['PROJ001'] are fetched for period_start '2024-08-01' and period_end '2024-08-31'; hourly rate is resolved for ['PROJ001']; a single‑line sample total is computed (10 hours at 85.0 with hst_rate 0.13); and the Account Receivable aging for period_label '2024-08' is exported. Each write is verified via a subsequent read, using only available tools.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={
                    "address": "100 Bloor St W, Toronto, ON",
                    "contact_email": "ap@mapleleafedu.ca",
                    "gst_number": "GST-999-010",
                    "name": "Maple Leaf Educational",
                    "publisher_id": "PUB010",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB010"}),
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "ap@northernlights-edu.ca",
                    "publisher_id": "PUB002",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB002"}),
            Action(
                name="mutate_consultant_contact",
                kwargs={"consultant_id": "CONS001", "phone": "+1-416-555-0199"},
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(
                name="read_time_entries",
                kwargs={
                    "period_end": "2024-08-31",
                    "period_start": "2024-08-01",
                    "project_id_list": ["PROJ001"],
                },
            ),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 10, "rate": 85.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_72",
        instruction="You formalize a November‑2024 email for invoice '2024-010' and capture the audit with context. "
                    "Your end state: invoice_number '2024-010' is emailed using publisher_id 'PUB004' and consultant_id '"
                    "CONS001' with subject 'Invoice 2024-010 (November 2024)', body 'Please see attached invoice 2024-010.' "
                    "and attachment 'https://test.storage.com/invoices/2024/INV-2024-010.pdf', and the "
                    "invoice is re‑read with sent_at populated; an audit event 'emailed' is recorded and listable; "
                    "open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'.",
        actions=[
            Action(
                name="dispatch_invoice_email",
                kwargs={
                    "attachment": "https://test.storage.com/invoices/2024/INV-2024-010.pdf",
                    "body_text": "Please see attached invoice 2024-010.",
                    "consultant_id": "CONS001",
                    "invoice_number": "2024-010",
                    "publisher_id": "PUB004",
                    "subject": "Invoice 2024-010 (November 2024)",
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-010"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "emailed", "invoice_number": "2024-010"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-010"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "audit_event('2024-010','emailed')",
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_73",
        instruction="You add publisher_id 'PUB047' named 'Horizon Peak Education' and log an August‑2024 snapshot with sample math totals. Your end state: 'PUB047' exists and is readable; project_id 'PROJ3064' exists with isbn '978-1-3100-3064-0', project_title 'Discrete Math, 1e', default_hourly_rate 104.0 and is readable; a sample total is computed (1h @104.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-08' and a dashboard snapshot is stored for '2024-08-31' referencing that PDF and is readable by date.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Horizon Peak Education", "publisher_id": "PUB047"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB047"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 104.0,
                    "isbn": "978-1-3100-3064-0",
                    "project_id": "PROJ3064",
                    "project_title": "Discrete Math, 1e",
                    "publisher_id": "PUB047",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ3064"}),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 104.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
            "dashboard_snapshot('2024-08-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_74",
        instruction=(
            "You validate October-2024 time tracking for a light billing estimate. "
            "Your end state: time entries for ['PROJ001','PROJ003'] from '2024-10-01' to '2024-10-31' are fetched and validated; "
            "hours are grouped by ISBN; rates are resolved for ['PROJ001','PROJ003']; "
            "a sample total for 5h @85.0 and 3h @75.0 is calculated using HST rate 0.13; "
            "Accounts Receivable aging for '2024-10' is exported and available at 'https://test.storage.com/reports/accounts_receivable_2024-10.pdf'; "
            "a dashboard snapshot dated '2024-10-31' exists, is readable by snapshot_date, and references the same A/R PDF; "
            "an audit event 'reviewed' for invoice_number '2024-010' is recorded and visible."
        ),
    actions=[
            Action(
                name="read_time_entries",
                kwargs={
                    "period_end": "2024-10-31",
                    "period_start": "2024-10-01",
                    "project_id_list": ["PROJ001", "PROJ003"],
                },
            ),
            Action(name="audit_time_entries", kwargs={"rows": []}),
            Action(name="aggregate_hours_by_isbn", kwargs={"rows": []}),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ001", "PROJ003"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 5, "rate": 85.0}, {"hours": 3, "rate": 75.0}],
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "reviewed", "invoice_number": "2024-010"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-010"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
            "dashboard_snapshot('2024-10-31')",
            "audit_event('2024-010','reviewed')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_75",
        instruction="You create a concise November‑2024 invoice for publisher_id 'PUB004' and record its audit. Your end state: invoice_number '2024-141' exists for period_start '2024-11-01' and period_end '2024-11-30' with correct totals (4h @88.0, hst_rate 0.13) and is readable; a single line is inserted for project_id 'PROJ003' with isbn '978-1-3100-0003-7' for 4h @88.0 and is listable; an audit event 'generated' is recorded and listable. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-141.pdf'.",
        actions=[
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 45.76,
                    "invoice_date": "2024-11-30",
                    "invoice_number": "2024-141",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-141.pdf",
                    "period_end": "2024-11-30",
                    "period_start": "2024-11-01",
                    "publisher_id": "PUB004",
                    "subtotal": 352.0,
                    "total_due": 397.76,
                },
            ),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-141"}),
            Action(
                name="create_invoice_lines",
                kwargs={
                    "invoice_number": "2024-141",
                    "lines": [
                        {
                            "hours": 4,
                            "isbn": "978-1-3100-0003-7",
                            "project_id": "PROJ003",
                            "rate": 88.0,
                        }
                    ],
                },
            ),
            Action(name="list_invoice_lines_by_invoice", kwargs={"invoice_number": "2024-141"}),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "generated", "invoice_number": "2024-141"},
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-141"}),
        ],
        outputs=[
            "invoice_pdf('https://test.storage.com/invoices/2024/INV-2024-141.pdf')",
            "audit_event('2024-141','generated')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_76",
        instruction=(
            "You update billing contacts and produce a November-2024 billing review. "
            "Your end state: publisher_id 'PUB003' has contact_email 'ap@canopypress.ca' and is readable; "
            "consultant_id 'CONS001' has email 'sarah.thompson+ar@consultingpro.ca' and is readable; "
            "rates are resolved for ['PROJ001','PROJ003']; "
            "you compute a sample total for 2h @85.0 and 2h @75.0 via compute_invoice_totals using HST rate 0.13; "
            "Accounts Receivable aging for '2024-11' is exported (PDF: 'https://test.storage.com/reports/accounts_receivable_2024-11.pdf')."
        ),
    actions=[
            Action(
                name="mutate_client_contact",
                kwargs={"contact_email": "ap@canopypress.ca", "publisher_id": "PUB003"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB003"}),
            Action(
                name="mutate_consultant_contact",
                kwargs={
                    "consultant_id": "CONS001",
                    "email": "sarah.thompson+ar@consultingpro.ca",
                },
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ001", "PROJ003"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 85.0}, {"hours": 2, "rate": 75.0}],
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_77",
        instruction="You add a project for 'PUB001' and confirm an August‑2024 total. Your end state: project_id 'PROJ2035' exists with isbn '978-1-3100-2035-3', project_title 'Chemistry Workbook, 1e', default_hourly_rate 87.0 and is visible; rates are resolved for ['PROJ2035','PROJ001'] and a sample total is computed (2h @87.0 and 2h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-08'.",
        actions=[
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 87.0,
                    "isbn": "978-1-3100-2035-3",
                    "project_id": "PROJ2035",
                    "project_title": "Chemistry Workbook, 1e",
                    "publisher_id": "PUB001",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ2035"}),
            Action(
                name="map_hourly_rates",
                kwargs={"project_id_list": ["PROJ2035", "PROJ001"]},
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 87.0}, {"hours": 2, "rate": 85.0}],
                },
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_78",
        instruction="You create publisher_id 'PUB049' named 'Blue Shore Academics' with a civics project and confirm a September‑2024 context. Your end state: 'PUB049' exists and is readable; project_id 'PROJ3069' exists with isbn '978-1-3100-3069-4', project_title 'Civics Foundations, 1e', default_hourly_rate 88.0 and is readable; open invoices are reviewed; 12‑month KPIs are available; a sample total is computed (2h @88.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-09'.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Blue Shore Academics", "publisher_id": "PUB049"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB049"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 88.0,
                    "isbn": "978-1-3100-3069-4",
                    "project_id": "PROJ3069",
                    "project_title": "Civics Foundations, 1e",
                    "publisher_id": "PUB049",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ3069"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 88.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_79",
        instruction="You normalize contacts and run a quick October‑2024 health check. Your end state: consultant_id 'CONS001' phone equals '+1-416-555-0177' and is readable; publisher_id 'PUB004' is readable; open invoices are reviewed and 12‑month KPIs are available; Account Receivable aging for '2024-10' is exported.",
        actions=[
            Action(
                name="mutate_consultant_contact",
                kwargs={"consultant_id": "CONS001", "phone": "+1-416-555-0177"},
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB004"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_80",
        instruction="You introduce publisher_id 'PUB046' named 'Lantern House Education' and prepare a November‑2024 snapshot. Your end state: 'PUB046' exists and is readable; project_id 'PROJ3061' exists with isbn '978-1-3100-3061-9', project_title 'Critical Thinking, 1e', default_hourly_rate 99.0 and is readable; open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'; a dashboard snapshot is stored for '2024-11-30' and is readable by date.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Lantern House Education", "publisher_id": "PUB046"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB046"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 99.0,
                    "isbn": "978-1-3100-3061-9",
                    "project_id": "PROJ3061",
                    "project_title": "Critical Thinking, 1e",
                    "publisher_id": "PUB046",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ3061"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-11-30"},
            ),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
            "dashboard_snapshot('2024-11-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_81",
        instruction="You create publisher_id 'PUB055' named 'Summit Ridge Learning' and establish an October‑2024 dashboard with a small sample. Your end state: 'PUB055' exists and is readable; open invoices are reviewed; 12‑month KPIs are available; rates are resolved for ['PROJ001']; a sample total is computed (1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-10'; a dashboard snapshot is stored for '2024-10-31' referencing that PDF and is readable by date.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Summit Ridge Learning", "publisher_id": "PUB055"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB055"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 85.0}]},
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
            "dashboard_snapshot('2024-10-31')",
            "kpis(window_months=12)",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_82",
        instruction="You open project_id 'PROJ2044' for 'PUB004' and run a November‑2024 check. Your end state: 'PROJ2044' exists with isbn '978-1-3100-2044-7', project_title 'Media Literacy, 1e', default_hourly_rate 101.0 and is visible; rates resolve for ['PROJ2044'] and a sample total is computed (3h @101.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-11'; representative invoice '2024-010' is readable.",
        actions=[
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 101.0,
                    "isbn": "978-1-3100-2044-7",
                    "project_id": "PROJ2044",
                    "project_title": "Media Literacy, 1e",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ2044"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ2044"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 101.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
            Action(name="fetch_invoice_record", kwargs={"invoice_number": "2024-010"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_83",
        instruction="You add publisher_id 'PUB035' named 'Northern Ridge Press' and anchor a July‑2024 baseline. Your end state: 'PUB035' exists and is visible; project_id 'PROJ2041' under 'PUB035' exists with isbn '978-1-3100-2041-6', project_title 'Algebra Readiness, 1e', default_hourly_rate 93.0 and is visible; a sample total is computed (2h @93.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-07' and a snapshot is stored for '2024-07-31' referencing that PDF and is readable.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Northern Ridge Press", "publisher_id": "PUB035"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB035"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 93.0,
                    "isbn": "978-1-3100-2041-6",
                    "project_id": "PROJ2041",
                    "project_title": "Algebra Readiness, 1e",
                    "publisher_id": "PUB035",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ2041"}),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 93.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-07"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-07.pdf",
                    "snapshot_date": "2024-07-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-07-31"},
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-07.pdf')",
            "dashboard_snapshot('2024-07-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_84",
        instruction=(
            "You add a humanities project and align an August-2024 review. "
            "Your end state: project_id 'PROJ1106' exists for 'PUB003' with isbn '978-1-3100-1015-6', "
            "project_title 'Philosophy Primer, 1e', default_hourly_rate 91.0, and is readable; "
            "rates are resolved for ['PROJ1106']; "
            "a sample total for 2h @91.0 is calculated using HST rate 0.13; "
            "Accounts Receivable aging for '2024-08' is exported and available at 'https://test.storage.com/reports/accounts_receivable_2024-08.pdf'; "
            "a dashboard snapshot dated '2024-08-31' exists, is readable by snapshot_date, and references the same A/R PDF."
        ),
    actions=[
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 91.0,
                    "isbn": "978-1-3100-1015-6",
                    "project_id": "PROJ1106",
                    "project_title": "Philosophy Primer, 1e",
                    "publisher_id": "PUB003",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ1106"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ1106"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 91.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
            "dashboard_snapshot('2024-08-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_85",
        instruction=(
            "You compose and email an August-2024 invoice for publisher_id 'PUB003'. "
            "Your end state: invoice_number 'INV-2024-209' exists with invoice_date '2024-08-31', "
            "period_start '2024-08-01', period_end '2024-08-31', subtotal 875.0, hst_amount 113.75, total_due 988.75, "
            "pdf_path '/invoices/2024/INV-2024-209.pdf' and is readable; the invoice email has been sent from consultant_id 'CONS001' "
            "with subject 'Invoice INV-2024-209', body_text 'August 2024 invoice attached.' and the attachment; "
            "the invoice record shows a populated 'sent_at' timestamp; an 'emailed' audit for 'INV-2024-209' is recorded and visible."
        ),
    actions=[
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 113.75,
                    "invoice_date": "2024-08-31",
                    "invoice_number": "INV-2024-209",
                    "pdf_path": "/invoices/2024/INV-2024-209.pdf",
                    "period_end": "2024-08-31",
                    "period_start": "2024-08-01",
                    "publisher_id": "PUB003",
                    "subtotal": 875.0,
                    "total_due": 988.75,
                },
            ),
            Action(
                name="fetch_invoice_record", kwargs={"invoice_number": "INV-2024-209"}
            ),
            Action(
                name="dispatch_invoice_email",
                kwargs={
                    "attachment": "/invoices/2024/INV-2024-209.pdf",
                    "body_text": "August 2024 invoice attached.",
                    "consultant_id": "CONS001",
                    "invoice_number": "INV-2024-209",
                    "publisher_id": "PUB003",
                    "subject": "Invoice INV-2024-209",
                },
            ),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "emailed", "invoice_number": "INV-2024-209"},
            ),
            Action(
                name="list_invoice_events", kwargs={"invoice_number": "INV-2024-209"}
            ),
            Action(
                name="fetch_invoice_record", kwargs={"invoice_number": "INV-2024-209"}
            ),
        ],
        outputs=[
            "invoice_pdf('/invoices/2024/INV-2024-209.pdf')",
            "audit_event('INV-2024-209','emailed')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_86",
        instruction="You refresh October‑2024 Account Receivable context and confirm key contacts. Your end state: open invoices (status 'open') are reviewed; Account Receivable aging exports exist for period labels '2024-10' and '2024-09'; publisher_id 'PUB004' contact_email is updated to 'ap@bluepeakpublishing.ca' and is readable; consultant_id 'CONS001' address is confirmed by writing '1234 Oak Street, Toronto, ON M5V 3A8' and reading it back; 12‑month collection KPIs are computed (window_months 12); projects are listed and project_id 'PROJ004' details are readable; and, for a quick risk check, you compute days outstanding using invoice_number '2024-010' with due_date '2024-10-31' and today '2024-11-15' (15 days) and categorize that value. Each write is verified via a subsequent read using only the available domain tools.",
        actions=[
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-09"}),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB004"}),
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "ap@bluepeakpublishing.ca",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB004"}),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(
                name="mutate_consultant_contact",
                kwargs={
                    "address": "1234 Oak Street, Toronto, ON M5V 3A8",
                    "consultant_id": "CONS001",
                },
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-15",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 15, "invoice_number": "2024-010"}]
                },
            ),
            Action(name="list_projects_catalog", kwargs={}),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ004"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-09.pdf')",
            "kpis(window_months=12)",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_87",
        instruction="You open publisher_id 'PUB044' named 'Cedar Ridge Press' and align an August‑2024 snapshot. Your end state: 'PUB044' exists and is readable; project_id 'PROJ3057' exists with isbn '978-1-3100-3057-2', project_title 'Financial Literacy, 1e', default_hourly_rate 91.0 and is readable; a sample total is computed (2h @91.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-08' and a dashboard snapshot is stored for '2024-08-31' referencing that PDF and is readable by date.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Cedar Ridge Press", "publisher_id": "PUB044"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB044"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 91.0,
                    "isbn": "978-1-3100-3057-2",
                    "project_id": "PROJ3057",
                    "project_title": "Financial Literacy, 1e",
                    "publisher_id": "PUB044",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ3057"}),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 91.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
            "dashboard_snapshot('2024-08-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_88",
        instruction="You add publisher_id 'PUB048' named 'Bright Pine Press' and align November‑2024 reporting with a small sample. Your end state: 'PUB048' exists and is readable; open invoices are reviewed; 12‑month KPIs are available; rates are resolved for ['PROJ001']; a sample total is computed (1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-11'; a dashboard snapshot is stored for '2024-11-30' and is readable by date.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Bright Pine Press", "publisher_id": "PUB048"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB048"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 85.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-11-30"},
            ),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
            "dashboard_snapshot('2024-11-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_89",
        instruction="You introduce publisher_id 'PUB021' named 'Pioneer Learning Press' and stage an August‑2024 snapshot. Your end state: 'PUB021' exists and is visible; a small project 'PROJ1012' under 'PUB021' exists with isbn '978-1-3100-1012-7', project_title 'Civics Primer, 1e', default_hourly_rate 86.0 and is visible; sample totals are computed (2h @86.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-08' and a dashboard snapshot is stored for '2024-08-31' referencing that PDF.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Pioneer Learning Press", "publisher_id": "PUB021"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB021"}),
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 86.0,
                    "isbn": "978-1-3100-1012-7",
                    "project_id": "PROJ1012",
                    "project_title": "Civics Primer, 1e",
                    "publisher_id": "PUB021",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ1012"}),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 86.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
            "dashboard_snapshot('2024-08-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_90",
        instruction="You validate readiness for November‑2024 around project_id 'PROJ001' and record an aging categorization. Your end state: projects are listed and 'PROJ001' details are readable; rates are resolved for ['PROJ001']; a sample total is computed (3h @85.0 with hst_rate 0.13); open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'; days outstanding for invoice '2024-010' as of '2024-11-20' using period_end '2024-10-31' (20 days) are categorized; an invoice audit event 'aging_categorized' is recorded for '2024-010' and listable.",
        actions=[
            Action(name="list_projects_catalog", kwargs={}),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ001"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 85.0}]},
            ),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-20",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 20, "invoice_number": "2024-010"}]
                },
            ),
            Action(
                name="log_invoice_event",
                kwargs={
                    "event_type": "aging_categorized",
                    "invoice_number": "2024-010",
                },
            ),
            Action(name="list_invoice_events", kwargs={"invoice_number": "2024-010"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
            "audit_event('2024-010','aging_categorized')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_91",
        instruction="You open a new publisher and file an August‑2024 snapshot. Your end state: publisher_id 'PUB023' named 'North Shore Academy' exists and is readable; contact_email equals 'accounts@northshoreacademy.ca' and is readable; Account Receivable aging for '2024-08' is exported and a snapshot stored for '2024-08-31'.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "North Shore Academy", "publisher_id": "PUB023"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB023"}),
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "accounts@northshoreacademy.ca",
                    "publisher_id": "PUB023",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB023"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
            "dashboard_snapshot('2024-08-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_92",
        instruction="You register project_id 'PROJ1015' for 'PUB005' and compute an October‑2024 sample with context. Your end state: 'PROJ1015' exists with isbn '978-1-3100-1015-8', project_title 'Canadian Geography, 2e', default_hourly_rate 90.0 and is visible; 'PUB005' is readable; a sample total is computed (4h @90.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-10'.",
        actions=[
            Action(
                name="add_project_card",
                kwargs={
                    "default_hourly_rate": 90.0,
                    "isbn": "978-1-3100-1015-8",
                    "project_id": "PROJ1015",
                    "project_title": "Canadian Geography, 2e",
                    "publisher_id": "PUB005",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ1015"}),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB005"}),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 4, "rate": 90.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_93",
        instruction="You create publisher_id 'PUB025' named 'Lakeside Scholastic' and finalize an August snapshot. Your end state: 'PUB025' exists and is visible; the Account Receivable aging PDF exists for '2024-08' and a dashboard snapshot is saved for '2024-08-31' referencing that PDF; a sample total is computed (2h @85.0 with hst_rate 0.13) using rates for ['PROJ001'].",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Lakeside Scholastic", "publisher_id": "PUB025"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB025"}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 85.0}]},
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
            "dashboard_snapshot('2024-08-31')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_94",
        instruction="You register publisher_id 'PUB036' named 'Cedar Grove Texts' and prepare an October‑2024 summary. Your end state: 'PUB036' exists and is visible; open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-10'; the contact for 'PUB003' equals 'ap@canopypress.ca' and is readable.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Cedar Grove Texts", "publisher_id": "PUB036"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB036"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-10"}),
            Action(
                name="mutate_client_contact",
                kwargs={"contact_email": "ap@canopypress.ca", "publisher_id": "PUB003"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB003"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-10.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_95",
        instruction="You update two AP contacts and confirm November‑2024 KPIs. Your end state: 'PUB001' contact_email equals 'accounts@nelson-edu.ca' and is visible; 'PUB003' contact_email equals 'accounts@canopypress.ca' and is visible; open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'.",
        actions=[
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "accounts@nelson-edu.ca",
                    "publisher_id": "PUB001",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB001"}),
            Action(
                name="mutate_client_contact",
                kwargs={
                    "contact_email": "accounts@canopypress.ca",
                    "publisher_id": "PUB003",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB003"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-11.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_96",
        instruction="You register publisher_id 'PUB032' named 'Harborview Education' and file summer Account Receivable snapshots. Your end state: 'PUB032' exists and is readable; Account Receivable aging PDFs exist for '2024-07' and '2024-06'; dashboard snapshots are stored for '2024-07-31' and '2024-06-30' referencing those PDFs and are readable by id; open invoices are reviewed and 12‑month KPIs are available.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Harborview Education", "publisher_id": "PUB032"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB032"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-07"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-07.pdf",
                    "snapshot_date": "2024-07-31",
                },
            ),
            Action(name="fetch_dashboard_snapshot", kwargs={"snapshot_id": 1}),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-06"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-06.pdf",
                    "snapshot_date": "2024-06-30",
                },
            ),
            Action(name="fetch_dashboard_snapshot", kwargs={"snapshot_id": 2}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-07.pdf')",
            "dashboard_snapshot('2024-07-31')",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-06.pdf')",
            "dashboard_snapshot('2024-06-30')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_97",
        instruction="You assemble and send an October‑2024 invoice for publisher_id 'PUB001'. Your end state: invoice_number 'INV-2024-230' exists with invoice_date '2024-10-31', period_start '2024-10-01', period_end '2024-10-31', subtotal 850.0, hst_amount 110.5, total_due 960.5, pdf_path '/invoices/2024/INV-2024-230.pdf' and is readable; the invoice is emailed from consultant_id 'CONS001' with subject 'Invoice INV-2024-230' and body_text 'October 2024 invoice attached.' and attachment; an 'emailed' audit is recorded and listed.",
        actions=[
            Action(
                name="create_invoice_record",
                kwargs={
                    "hst_amount": 110.5,
                    "invoice_date": "2024-10-31",
                    "invoice_number": "INV-2024-230",
                    "pdf_path": "/invoices/2024/INV-2024-230.pdf",
                    "period_end": "2024-10-31",
                    "period_start": "2024-10-01",
                    "publisher_id": "PUB001",
                    "subtotal": 850.0,
                    "total_due": 960.5,
                },
            ),
            Action(
                name="fetch_invoice_record", kwargs={"invoice_number": "INV-2024-230"}
            ),
            Action(
                name="dispatch_invoice_email",
                kwargs={
                    "attachment": "/invoices/2024/INV-2024-230.pdf",
                    "body_text": "October 2024 invoice attached.",
                    "consultant_id": "CONS001",
                    "invoice_number": "INV-2024-230",
                    "publisher_id": "PUB001",
                    "subject": "Invoice INV-2024-230",
                },
            ),
            Action(
                name="log_invoice_event",
                kwargs={"event_type": "emailed", "invoice_number": "INV-2024-230"},
            ),
            Action(
                name="list_invoice_events", kwargs={"invoice_number": "INV-2024-230"}
            ),
            Action(
                name="fetch_invoice_record", kwargs={"invoice_number": "INV-2024-230"}
            ),
        ],
        outputs=[
            "invoice_pdf('/invoices/2024/INV-2024-230.pdf')",
            "audit_event('INV-2024-230','emailed')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_98",
        instruction="You set up PUB010 and its project, then run an August‑2024 micro‑billing check. Your end state: publisher_id 'PUB010' exists with exactly name 'Maple Leaf Educational', address '100 Bloor St W, Toronto, ON', contact_email 'ap@mapleleafedu.ca', gst_number 'GST-999-010' and is readable; project_id 'PROJ990' exists under 'PUB010' with isbn '978-1-9876-5432-1', project_title 'Intro Statistics, 5e', default_hourly_rate 105.0, override_hourly_rate None, account_code 'STAT-5E-2025', is_active True and is readable; you resolve the rate for ['PROJ990'] and compute a single‑line sample total (4 hours at 105.0 with hst_rate 0.13); and the Account Receivable aging for period_label '2024-08' is exported. Each write is verified via a subsequent read.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={
                    "address": "100 Bloor St W, Toronto, ON",
                    "contact_email": "ap@mapleleafedu.ca",
                    "gst_number": "GST-999-010",
                    "name": "Maple Leaf Educational",
                    "publisher_id": "PUB010",
                },
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB010"}),
            Action(
                name="add_project_card",
                kwargs={
                    "account_code": "STAT-5E-2025",
                    "default_hourly_rate": 105.0,
                    "is_active": True,
                    "isbn": "978-1-9876-5432-1",
                    "override_hourly_rate": None,
                    "project_id": "PROJ990",
                    "project_title": "Intro Statistics, 5e",
                    "publisher_id": "PUB010",
                },
            ),
            Action(name="fetch_project_card", kwargs={"project_id": "PROJ990"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ990"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 4, "rate": 105.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_99",
        instruction="You tighten August‑2024 contact data and verify KPIs. Your end state: 'PUB001' contact_email equals 'ap@nelson-edu.ca' and is visible; 'CONS001' address equals '1234 Oak Street, Toronto, ON M5V 3A8' and is visible; open invoices are reviewed and 12‑month KPIs are available; a sample total is computed (3h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-08'.",
        actions=[
            Action(
                name="mutate_client_contact",
                kwargs={"contact_email": "ap@nelson-edu.ca", "publisher_id": "PUB001"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB001"}),
            Action(
                name="mutate_consultant_contact",
                kwargs={
                    "address": "1234 Oak Street, Toronto, ON M5V 3A8",
                    "consultant_id": "CONS001",
                },
            ),
            Action(name="fetch_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(name="query_invoices", kwargs={"status": "open"}),
            Action(name="derive_collection_kpis", kwargs={"window_months": 12}),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 85.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "kpis(window_months=12)",
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
        ],
    ),
    Task(
        annotator="V2",
        user_id="task_100",
        instruction="You add publisher_id 'PUB057' named 'Harbor Lights Learning' and stage an August‑2024 dashboard with a small total. Your end state: 'PUB057' exists and is readable; a sample total is computed (1h @85.0 with hst_rate 0.13) using rate for ['PROJ001']; the Account Receivable aging PDF exists for '2024-08'; a dashboard snapshot is stored for '2024-08-31' referencing 'https://test.storage.com/reports/accounts_receivable_2024-08.pdf' and is readable by date; days outstanding for '2024-010' as of '2024-08-15' using period_end '2024-07-31' (15 days) are categorized.",
        actions=[
            Action(
                name="add_client_profile",
                kwargs={"name": "Harbor Lights Learning", "publisher_id": "PUB057"},
            ),
            Action(name="fetch_client_profile", kwargs={"publisher_id": "PUB057"}),
            Action(
                name="map_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="compute_invoice_totals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 85.0}]},
            ),
            Action(name="render_accounts_receivable_report", kwargs={"period_label": "2024-08"}),
            Action(
                name="create_dashboard_snapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="fetch_dashboard_snapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
            Action(
                name="derive_days_outstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-07-31"}
                    ],
                    "today": "2024-08-15",
                },
            ),
            Action(
                name="bucketize_aging",
                kwargs={
                    "aging": [{"days_outstanding": 15, "invoice_number": "2024-010"}]
                },
            ),
        ],
        outputs=[
            "report_pdf('https://test.storage.com/reports/accounts_receivable_2024-08.pdf')",
            "dashboard_snapshot('2024-08-31')",
        ],
    ),
]
