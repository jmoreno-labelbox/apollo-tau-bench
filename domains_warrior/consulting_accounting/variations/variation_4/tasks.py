from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="A",
        user_id="ca_v4_001",
        instruction=(
            "You ensure base records and contacts are in place and then produce an August‑2024 context snapshot. "
            "End state: publisher_id 'PUB010' exists with exactly name 'Maple Leaf Educational', "
            "address '100 Bloor St W, Toronto, ON', contact_email 'ap@mapleleafedu.ca', "
            "gst_number 'GST-999-010' and is readable; publisher_id 'PUB002' contact_email is "
            "updated to 'ap@northernlights-edu.ca' and is readable; consultant_id 'CONS001' phone is updated to "
            "'+1-416-555-0199' and is readable; August‑2024 time entries for ['PROJ001'] are fetched for "
            "period_start '2024-08-01' and period_end '2024-08-31'; hourly rate is resolved for ['PROJ001']; "
            "a single‑line sample total is computed (10 hours at 85.0 with hst_rate 0.13); and the A/R aging for "
            "period_label '2024-08' is exported. Each write is verified via a subsequent read, using only available tools."
        ),
        actions=[
            Action(name="create_publisher", kwargs={
                "publisher_id": "PUB010",
                "name": "Maple Leaf Educational",
                "address": "100 Bloor St W, Toronto, ON",
                "contact_email": "ap@mapleleafedu.ca",
                "gst_number": "GST-999-010"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB010"}),

            Action(name="update_publisher_contact", kwargs={
                "publisher_id": "PUB002",
                "contact_email": "ap@northernlights-edu.ca"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB002"}),

            Action(name="update_consultant_contact", kwargs={
                "consultant_id": "CONS001",
                "phone": "+1-416-555-0199"
            }),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="fetch_time_entries", kwargs={
                "project_id_list": ["PROJ001"],
                "period_start": "2024-08-01",
                "period_end": "2024-08-31"
            }),
            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 10, "rate": 85.0}],
                "hst_rate": 0.13
            }),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "PUB010 created & read; PUB002 AP updated & read; CONS001 phone updated & read; "
            "Aug‑2024 entries fetched; rate resolved for PROJ001; sample total computed; AR_Aging_2024-08 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_002",
        instruction=(
            "You run an A/R health pass and onboard a new client. End state: new publisher_id 'PUB011' "
            "exists with exactly name 'Canopy Learning Ltd.', address '77 Front St E, Toronto, ON', "
            "contact_email 'ap@canopylearning.ca', gst_number 'GST-999-011' and is readable; 12‑month collection KPIs "
            "(window_months 12) are computed; the A/R aging for period_label '2024-09' is exported; and publisher_id "
            "'PUB003' has contact_email updated to 'ap@canopypress.ca' and is readable. Each write is verified via a "
            "subsequent read."
        ),
        actions=[
            Action(name="create_publisher", kwargs={
                "publisher_id": "PUB011",
                "name": "Canopy Learning Ltd.",
                "address": "77 Front St E, Toronto, ON",
                "contact_email": "ap@canopylearning.ca",
                "gst_number": "GST-999-011"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB011"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
            Action(name="update_publisher_contact", kwargs={
                "publisher_id": "PUB003",
                "contact_email": "ap@canopypress.ca"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB003"}),
        ],
        outputs=[
            "PUB011 created & read; 12‑month KPIs computed; AR_Aging_2024-09 exported; "
            "PUB003 AP updated & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_003",
        instruction=(
            "You prepare a July‑2024 billing overview and refresh key contacts. Fetch time entries for "
            "['PROJ001','PROJ003'] from 2024-07-01 to 2024-07-31, resolve rates for those projects, and run a sample "
            "two‑line totals using the resolved rates (12h @85.0 and 8h @75.0, HST 0.13). Update CONS001 email to "
            "sarah.thompson+billing@consultingpro.ca and read it back. Update PUB002 AP email to "
            "ap@northernlights-edu.ca and read it back. Export the A/R aging for period label 2024-07."
        ),
        actions=[
            Action(name="fetch_time_entries", kwargs={"project_id_list": ["PROJ001", "PROJ003"], "period_start": "2024-07-01", "period_end": "2024-07-31"}),
            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001", "PROJ003"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 12, "rate": 85.0}, {"hours": 8, "rate": 75.0}], "hst_rate": 0.13}),

            Action(name="update_consultant_contact", kwargs={"consultant_id": "CONS001", "email": "sarah.thompson+billing@consultingpro.ca"}),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="update_publisher_contact", kwargs={"publisher_id": "PUB002", "contact_email": "ap@northernlights-edu.ca"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB002"}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-07"}),
        ],
        outputs=[
            "July context fetched/resolved; sample totals computed; CONS001 email updated & read; "
            "PUB002 AP updated & read; AR_Aging_2024-07 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_004",
        instruction=(
            "You set up PUB010 and its project, then run an August‑2024 micro‑billing check. "
            "End state: publisher_id 'PUB010' exists with exactly name 'Maple Leaf Educational', address "
            "'100 Bloor St W, Toronto, ON', contact_email 'ap@mapleleafedu.ca', gst_number 'GST-999-010' and is readable; "
            "project_id 'PROJ990' exists under 'PUB010' with isbn '978-1-9876-5432-1', project_title 'Intro Statistics, 5e', "
            "default_hourly_rate 105.0, override_hourly_rate None, account_code 'STAT-5E-2025', is_active True and is readable; "
            "you resolve the rate for ['PROJ990'] and compute a single‑line sample total (4 hours at 105.0 with hst_rate 0.13); "
            "and the A/R aging for period_label '2024-08' is exported. Each write is verified via a subsequent read."
        ),
        actions=[
            Action(name="create_publisher", kwargs={
                "publisher_id": "PUB010",
                "name": "Maple Leaf Educational",
                "address": "100 Bloor St W, Toronto, ON",
                "contact_email": "ap@mapleleafedu.ca",
                "gst_number": "GST-999-010"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB010"}),
            Action(name="create_project", kwargs={
                "project_id": "PROJ990",
                "publisher_id": "PUB010",
                "isbn": "978-1-9876-5432-1",
                "project_title": "Intro Statistics, 5e",
                "default_hourly_rate": 105.0,
                "override_hourly_rate": None,
                "account_code": "STAT-5E-2025",
                "is_active": True
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ990"}),
            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ990"]}),
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 4, "rate": 105.0}],
                "hst_rate": 0.13
            }),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "PUB010 created & read; PROJ990 created & read; PROJ990 rate resolved; "
            "4h micro‑total computed; AR_Aging_2024-08 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_005",
        instruction=(
            "You refresh October‑2024 A/R context and confirm key contacts. End state: open invoices (status 'open') "
            "are reviewed; A/R aging exports exist for period labels '2024-10' and '2024-09'; publisher_id 'PUB004' "
            "contact_email is updated to 'ap@bluepeakpublishing.ca' and is readable; consultant_id 'CONS001' address is "
            "confirmed by writing '1234 Oak Street, Toronto, ON M5V 3A8' and reading it back; 12‑month collection KPIs are "
            "computed (window_months 12); projects are listed and project_id 'PROJ004' details are readable; and, for a quick "
            "risk check, you compute days outstanding using invoice_number '2024-010' with due_date '2024-10-31' and today "
            "'2024-11-15' (15 days) and categorize that value. Each write is verified via a subsequent read using only the "
            "available domain tools."
        ),
        actions=[
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),

            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB004"}),
            Action(name="update_publisher_contact", kwargs={"publisher_id": "PUB004", "contact_email": "ap@bluepeakpublishing.ca"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB004"}),

            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),
            Action(name="update_consultant_contact", kwargs={"consultant_id": "CONS001", "address": "1234 Oak Street, Toronto, ON M5V 3A8"}),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-010", "period_end": "2024-10-31"}],
                "today": "2024-11-15"
            }),
            Action(name="categorize_aging", kwargs={
                "aging": [{"invoice_number": "2024-010", "days_outstanding": 15}]
            }),

            Action(name="fetch_projects", kwargs={}),
            Action(name="get_project_details", kwargs={"project_id": "PROJ004"}),
        ],
        outputs=[
            "Open invoices listed; AR_Aging_2024-10 and AR_Aging_2024-09 exported; PUB004 AP updated & read; "
            "CONS001 address confirmed & read; KPIs computed; 15 days categorized; projects listed; PROJ004 read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_006",
        instruction=(
            "You introduce publisher_id 'PUB013' named 'Maple STEM Press' and align a September‑2024 billing check. "
            "End state: 'PUB013' exists with name 'Maple STEM Press' and is readable; publisher_id 'PUB002' is readable; "
            "open invoices (status 'open') are reviewed and 12‑month KPIs are computed; you resolve rates for ['PROJ003'] "
            "and compute sample totals (6h @75.0 and 2h @75.0 with hst_rate 0.13); you export the A/R aging for '2024-09'. "
            "Each write is verified via a subsequent read."
        ),
        actions=[
            Action(name="create_publisher", kwargs={
                "publisher_id": "PUB013",
                "name": "Maple STEM Press"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB013"}),

            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB002"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ003"]}),
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 6, "rate": 75.0}, {"hours": 2, "rate": 75.0}],
                "hst_rate": 0.13
            }),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "PUB013 created & read; PUB002 read; open invoices reviewed; KPIs computed; rates resolved; sample totals; AR_Aging_2024-09 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_007",
        instruction=(
            "You tidy November‑2024 contact data and compute a confirmation total with context. End state: publisher_id 'PUB005' "
            "contact_email is updated to 'ap@westwoodpress.ca' and is readable; consultant_id 'CONS001' email is updated to "
            "'sarah.thompson@consultingpro.ca' and is readable; open invoices (status 'open') are reviewed and 12‑month KPIs computed; "
            "you resolve rates for ['PROJ003'] and compute a sample total (2h @75.0 with hst_rate 0.13); export A/R aging '2024-11'. "
            "Each write is verified via a subsequent read."
        ),
        actions=[
            Action(name="update_publisher_contact", kwargs={
                "publisher_id": "PUB005",
                "contact_email": "ap@westwoodpress.ca"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB005"}),

            Action(name="update_consultant_contact", kwargs={
                "consultant_id": "CONS001",
                "email": "sarah.thompson@consultingpro.ca"
            }),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ003"]}),
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 2, "rate": 75.0}],
                "hst_rate": 0.13
            }),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "PUB005 AP updated & read; CONS001 email updated & read; open invoices reviewed; KPIs computed; rate resolved; sample total; aging exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_008",
        instruction=(
            "You establish a November‑2024 readiness context for publisher_id 'PUB003'. "
            "End state: project_id 'PROJ999' exists under 'PUB003' with isbn '978-1-3100-0007-3', "
            "project_title 'Literature Survey, 1e', default_hourly_rate 91.0 and is visible; 'PUB003' is readable; "
            "open invoices (status 'open') are reviewed and 12‑month collection KPIs are available; "
            "rates are resolved for ['PROJ999','PROJ003'] and sample totals are computed (1h @91.0 and 2h @91.0 with hst_rate 0.13); "
            "an A/R aging PDF exists for period label '2024-11'; projects are listed and details for 'PROJ003' are visible; "
        ),
        actions=[
            Action(name="create_project", kwargs={
                "project_id": "PROJ999",
                "publisher_id": "PUB003",
                "isbn": "978-1-3100-0007-3",
                "project_title": "Literature Survey, 1e",
                "default_hourly_rate": 91.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ999"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB003"}),
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ999", "PROJ003"]}),
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 1, "rate": 91.0}, {"hours": 2, "rate": 91.0}],
                "hst_rate": 0.13
            }),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
            Action(name="fetch_projects", kwargs={}),
            Action(name="get_project_details", kwargs={"project_id": "PROJ003"}),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-010"}),
        ],
        outputs=[
            "PROJ999 created & read; PUB003 read; open invoices reviewed; KPIs computed; rates resolved; sample totals; "
            "AR_Aging_2024-11 exported; projects listed; PROJ003 read; invoice 2024-010 read;"
        ],
    ),    
    Task(
        annotator="A",
        user_id="ca_v4_009",
        instruction=(
            "You normalize contact data and produce a September‑2024 A/R snapshot for validation. "
            "End state: publisher_id 'PUB001' contact_email equals 'accounts@nelson-edu.ca' and is visible; "
            "consultant_id 'CONS001' email equals 'sarah.thompson@consultingpro.ca' and is visible; "
            "open invoices (status 'open') are reviewed and 12‑month KPIs are available; "
            "rates are resolved for ['PROJ001'] and a sample total is computed (6h @85.0 with hst_rate 0.13); "
            "A/R aging PDFs exist for period labels '2024-09' and '2024-08'; "
            "projects are listed and details for 'PROJ001' are visible; "
            "representative open invoices '2024-009' and '2024-021' are readable, and an audit event 'reviewed' is recorded for '2024-009' and listed."
        ),
        actions=[
            Action(name="update_publisher_contact", kwargs={
                "publisher_id": "PUB001",
                "contact_email": "accounts@nelson-edu.ca"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB001"}),

            Action(name="update_consultant_contact", kwargs={
                "consultant_id": "CONS001",
                "email": "sarah.thompson@consultingpro.ca"
            }),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 6, "rate": 85.0}],
                "hst_rate": 0.13
            }),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),

            Action(name="fetch_projects", kwargs={}),
            Action(name="get_project_details", kwargs={"project_id": "PROJ001"}),

            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-009"}),
            Action(name="record_invoice_audit", kwargs={
                "invoice_number": "2024-009",
                "event_type": "reviewed"
            }),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-009"}),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-021"}),
        ],
        outputs=[
            "PUB001 AP updated & read; CONS001 email updated & read; open invoices reviewed; KPIs computed; "
            "rate resolved; total computed; AR_Aging_2024-09 and AR_Aging_2024-08 exported; projects listed; PROJ001 read; "
            "invoices 2024-009 and 2024-021 read; audit for 2024-009 recorded & listed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_010",
        instruction=(
            "You update contact info and confirm a September‑2024 total with context. End state: publisher_id 'PUB003' contact_email is "
            "updated to 'accounts@canopypress.ca' and is readable; consultant_id 'CONS001' phone is updated to '+1-416-555-0199' and is readable; "
            "open invoices (status 'open') are reviewed and 12‑month KPIs computed; resolve rates for ['PROJ001','PROJ003'] and compute sample totals "
            "(3h @85.0 and 2h @75.0 with hst_rate 0.13); export A/R aging '2024-09'. Each write is verified via a subsequent read."
        ),
        actions=[
            Action(name="update_publisher_contact", kwargs={
                "publisher_id": "PUB003",
                "contact_email": "accounts@canopypress.ca"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB003"}),

            Action(name="update_consultant_contact", kwargs={
                "consultant_id": "CONS001",
                "phone": "+1-416-555-0199"
            }),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001", "PROJ003"]}),
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 3, "rate": 85.0}, {"hours": 2, "rate": 75.0}],
                "hst_rate": 0.13
            }),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "PUB003 AP updated & read; CONS001 phone updated & read; open invoices reviewed; KPIs computed; rates resolved; totals computed; aging exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_011",
        instruction=(
            "You add a focused writing project and align October‑2024 reporting for publisher_id 'PUB004'. End state: "
            "project_id 'PROJ1011' exists with isbn '978-1-3100-1011-0', project_title 'Writing Workshop, 1e', "
            "default_hourly_rate 94.0 and is visible; 'PUB004' is readable; rates are resolved for ['PROJ1011','PROJ001'] and "
            "a sample total is computed (2h @94.0 and 3h @85.0 with hst_rate 0.13); open invoices are reviewed and "
            "12‑month KPIs are available; the A/R aging PDF exists for '2024-10' and a snapshot is saved for "
            "'2024-10-31' referencing that PDF."
        ),
        actions=[
            Action(name="create_project", kwargs={
                "project_id": "PROJ1011",
                "publisher_id": "PUB004",
                "isbn": "978-1-3100-1011-0",
                "project_title": "Writing Workshop, 1e",
                "default_hourly_rate": 94.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ1011"}),

            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB004"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ1011", "PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 94.0}, {"hours": 3, "rate": 85.0}], "hst_rate": 0.13}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-10-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-10-31"}),
        ],
        outputs=[
            "PROJ1011 created & read; PUB004 read; rates resolved; totals computed; open invoices reviewed; KPIs computed; "
            "AR_Aging_2024-10 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_012",
        instruction=(
            "You introduce publisher_id 'PUB021' named 'Pioneer Learning Press' and stage an August‑2024 snapshot. "
            "End state: 'PUB021' exists and is visible; a small project 'PROJ1012' under 'PUB021' exists with isbn '978-1-3100-1012-7', "
            "project_title 'Civics Primer, 1e', default_hourly_rate 86.0 and is visible; sample totals are computed (2h @86.0 with hst_rate 0.13); "
            "the A/R aging PDF exists for '2024-08' and a dashboard snapshot is stored for '2024-08-31' referencing that PDF."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB021", "name": "Pioneer Learning Press"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB021"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ1012",
                "publisher_id": "PUB021",
                "isbn": "978-1-3100-1012-7",
                "project_title": "Civics Primer, 1e",
                "default_hourly_rate": 86.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ1012"}),

            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 86.0}], "hst_rate": 0.13}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-08-31"}),
        ],
        outputs=[
            "PUB021 created & read; PROJ1012 created & read; sample total computed; AR_Aging_2024-08 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_013",
        instruction=(
            "You add a STEM project and check November‑2024 risk. End state: project_id 'PROJ1013' exists under 'PUB003' with "
            "isbn '978-1-3100-1013-4', project_title 'Applied Physics, 1e', default_hourly_rate 98.0 and is visible; "
            "open invoices are reviewed and 12‑month KPIs are available; a sample total is computed (4h @98.0 with hst_rate 0.13); "
            "for risk, days outstanding are computed for invoice '2024-010' as of '2024-11-15' (15 days) and categorized."
        ),
        actions=[
            Action(name="create_project", kwargs={
                "project_id": "PROJ1013",
                "publisher_id": "PUB003",
                "isbn": "978-1-3100-1013-4",
                "project_title": "Applied Physics, 1e",
                "default_hourly_rate": 98.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ1013"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 4, "rate": 98.0}], "hst_rate": 0.13}),

            Action(name="compute_days_outstanding", kwargs={"invoices": [{"invoice_number": "2024-010", "period_end": "2024-10-31"}], "today": "2024-11-15"}),
            Action(name="categorize_aging", kwargs={"aging": [{"invoice_number": "2024-010", "days_outstanding": 15}]}),
        ],
        outputs=[
            "PROJ1013 created & read; open invoices reviewed; KPIs computed; sample total; 15 days categorized for 2024-010."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_014",
        instruction=(
            "You register project_id 'PROJ1015' for 'PUB005' and compute an October‑2024 sample with context. End state: "
            "'PROJ1015' exists with isbn '978-1-3100-1015-8', project_title 'Canadian Geography, 2e', default_hourly_rate 90.0 and is visible; "
            "'PUB005' is readable; a sample total is computed (4h @90.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-10'."
        ),
        actions=[
            Action(name="create_project", kwargs={
                "project_id": "PROJ1015",
                "publisher_id": "PUB005",
                "isbn": "978-1-3100-1015-8",
                "project_title": "Canadian Geography, 2e",
                "default_hourly_rate": 90.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ1015"}),

            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB005"}),

            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 4, "rate": 90.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "PROJ1015 created & read; PUB005 read; sample total; AR_Aging_2024-10 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_015",
        instruction=(
            "You tighten August‑2024 contact data and verify KPIs. End state: 'PUB001' contact_email equals 'ap@nelson-edu.ca' and "
            "is visible; 'CONS001' address equals '1234 Oak Street, Toronto, ON M5V 3A8' and is visible; "
            "open invoices are reviewed and 12‑month KPIs are available; a sample total is computed (3h @85.0 with hst_rate 0.13); "
            "the A/R aging PDF exists for '2024-08'."
        ),
        actions=[
            Action(name="update_publisher_contact", kwargs={"publisher_id": "PUB001", "contact_email": "ap@nelson-edu.ca"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB001"}),

            Action(name="update_consultant_contact", kwargs={"consultant_id": "CONS001", "address": "1234 Oak Street, Toronto, ON M5V 3A8"}),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 3, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "PUB001 AP updated & read; CONS001 address updated & read; open invoices reviewed; KPIs computed; sample total; AR_Aging_2024-08 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_016",
        instruction=(
            "You open publisher_id 'PUB024' named 'Aurora Study House' and align September‑2024 reporting. End state: "
            "'PUB024' exists and is visible; open invoices are reviewed; KPIs over 12 months are available; "
            "the A/R aging PDF exists for '2024-09' and a snapshot is saved for '2024-09-30' referencing that PDF; "
            "a sample total is computed (2h @85.0 and 2h @75.0 with hst_rate 0.13) using rates for ['PROJ001','PROJ003']."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB024", "name": "Aurora Study House"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB024"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-09-30", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-09.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-09-30"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001", "PROJ003"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 85.0}, {"hours": 2, "rate": 75.0}], "hst_rate": 0.13}),
        ],
        outputs=[
            "PUB024 created & read; open invoices reviewed; KPIs computed; AR_Aging_2024-09 exported; snapshot saved & read; rates resolved; totals computed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_017",
        instruction=(
            "You update contact info and verify August‑2024 totals. End state: 'CONS001' phone equals '+1-647-555-2244' and is visible; "
            "'PUB004' is readable; rates resolve for ['PROJ001'] and a sample total is computed (4h @85.0 with hst_rate 0.13); "
            "the A/R aging PDF exists for '2024-08'."
        ),
        actions=[
            Action(name="update_consultant_contact", kwargs={"consultant_id": "CONS001", "phone": "+1-647-555-2244"}),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB004"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 4, "rate": 85.0}], "hst_rate": 0.13}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "CONS001 phone updated & read; PUB004 read; rate resolved; total computed; AR_Aging_2024-08 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_018",
        instruction=(
            "You create publisher_id 'PUB025' named 'Lakeside Scholastic' and finalize an August snapshot. End state: "
            "'PUB025' exists and is visible; the A/R aging PDF exists for '2024-08' and a dashboard snapshot is saved for '2024-08-31' "
            "referencing that PDF; a sample total is computed (2h @85.0 with hst_rate 0.13) using rates for ['PROJ001']."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB025", "name": "Lakeside Scholastic"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB025"}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-08-31"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 85.0}], "hst_rate": 0.13}),
        ],
        outputs=[
            "PUB025 created & read; AR_Aging_2024-08 exported; snapshot saved & read; rate resolved; total computed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_019",
        instruction=(
            "You create project_id 'PROJ1018' for 'PUB004' and compute a November‑2024 sample. End state: "
            "'PROJ1018' exists with isbn '978-1-3100-1018-9', project_title 'Intro Data Science, 2e', default_hourly_rate 105.0 and is visible; "
            "a sample total is computed (4h @105.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-11'."
        ),
        actions=[
            Action(name="create_project", kwargs={
                "project_id": "PROJ1018",
                "publisher_id": "PUB004",
                "isbn": "978-1-3100-1018-9",
                "project_title": "Intro Data Science, 2e",
                "default_hourly_rate": 105.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ1018"}),

            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 4, "rate": 105.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "PROJ1018 created & read; sample total; AR_Aging_2024-11 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_020",
        instruction=(
            "You update contacts and confirm a September‑2024 total. End state: 'PUB003' contact_email equals "
            "'accounts@canopypress.ca' and is visible; 'CONS001' phone equals '+1-416-555-0199' and is visible; "
            "rates resolve for ['PROJ001','PROJ003'] and sample totals are computed (3h @85.0 and 2h @75.0 with hst_rate 0.13); "
            "the A/R aging PDF exists for '2024-09'."
        ),
        actions=[
            Action(name="update_publisher_contact", kwargs={"publisher_id": "PUB003", "contact_email": "accounts@canopypress.ca"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB003"}),

            Action(name="update_consultant_contact", kwargs={"consultant_id": "CONS001", "phone": "+1-416-555-0199"}),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001", "PROJ003"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 3, "rate": 85.0}, {"hours": 2, "rate": 75.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "PUB003 AP updated & read; CONS001 phone updated & read; rates resolved; totals computed; AR_Aging_2024-09 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_021",
        instruction=(
            "You establish publisher_id 'PUB027' named 'North Coast Education' and complete an August snapshot. End state: "
            "'PUB027' exists and is visible; the A/R aging PDF exists for '2024-08' and a snapshot is saved for '2024-08-31' "
            "referencing that PDF; a sample total is computed (5h @85.0 with hst_rate 0.13) using rates for ['PROJ001']."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB027", "name": "North Coast Education"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB027"}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-08-31"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 5, "rate": 85.0}], "hst_rate": 0.13}),
        ],
        outputs=[
            "PUB027 created & read; AR_Aging_2024-08 exported; snapshot saved & read; rate resolved; total computed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_022",
        instruction=(
            "You add project_id 'PROJ1019' for 'PUB001' and compute a July‑2024 confirmation. End state: "
            "'PROJ1019' exists with isbn '978-1-3100-1019-6', project_title 'Intro Chemistry, 2e', default_hourly_rate 85.0 and is visible; "
            "a sample total is computed (4h @85.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-07'."
        ),
        actions=[
            Action(name="create_project", kwargs={
                "project_id": "PROJ1019",
                "publisher_id": "PUB001",
                "isbn": "978-1-3100-1019-6",
                "project_title": "Intro Chemistry, 2e",
                "default_hourly_rate": 85.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ1019"}),

            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 4, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-07"}),
        ],
        outputs=[
            "PROJ1019 created & read; sample total; AR_Aging_2024-07 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_023",
        instruction=(
            "You normalize contacts and produce a July‑2024 risk view. End state: publisher_id 'PUB002' contact_email equals "
            "'ap@northernlights-edu.ca' and is visible; consultant_id 'CONS001' gst_number equals '123456789RT0001' and is visible; "
            "open invoices are reviewed and 12‑month KPIs are available; the A/R aging PDF exists for '2024-07'; days outstanding are computed "
            "for '2024-023' as of '2024-08-01' (17 days) and categorized; projects are listed and 'PROJ003' details are visible."
        ),
        actions=[
            Action(name="update_publisher_contact", kwargs={"publisher_id": "PUB002", "contact_email": "ap@northernlights-edu.ca"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB002"}),

            Action(name="update_consultant_contact", kwargs={"consultant_id": "CONS001", "gst_number": "123456789RT0001"}),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-07"}),

            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-023", "period_end": "2024-07-15"}],
                "today": "2024-08-01"
            }),
            Action(name="categorize_aging", kwargs={"aging": [{"invoice_number": "2024-023", "days_outstanding": 17}]}),

            Action(name="fetch_projects", kwargs={}),
            Action(name="get_project_details", kwargs={"project_id": "PROJ003"})
        ],
        outputs=[
            "PUB002 AP updated & read; CONS001 GST updated & read; open invoices reviewed; KPIs computed; AR_Aging_2024-07 exported; "
            "17 days categorized for 2024-023; projects listed; PROJ003 read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_024",
        instruction=(
            "You align rates and contacts for a September‑2024 confirmation. End state: consultant_id 'CONS001' email equals "
            "'accounts+ar@consultingpro.ca' and is visible; publisher_id 'PUB001' contact_email equals 'ap@nelson-edu.ca' and is visible; "
            "rates are resolved for ['PROJ001','PROJ003'] and a sample total is computed (2h @85.0 and 2h @75.0 with hst_rate 0.13); "
            "open invoices are reviewed; 12‑month KPIs are available; the A/R aging PDF exists for '2024-09'."
        ),
        actions=[
            Action(name="update_consultant_contact", kwargs={"consultant_id": "CONS001", "email": "accounts+ar@consultingpro.ca"}),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="update_publisher_contact", kwargs={"publisher_id": "PUB001", "contact_email": "ap@nelson-edu.ca"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB001"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001", "PROJ003"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 85.0}, {"hours": 2, "rate": 75.0}], "hst_rate": 0.13}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"})
        ],
        outputs=[
            "CONS001 email updated & read; PUB001 AP updated & read; rates resolved; totals computed; open invoices reviewed; KPIs computed; AR_Aging_2024-09 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_025",
        instruction=(
            "You refresh AP contacts and verify October‑2024 A/R for two publishers. End state: 'PUB004' contact_email equals "
            "'ap@bluepeakpublishing.ca' and is visible; 'PUB005' contact_email equals 'ap@westwoodpress.ca' and is visible; open invoices are reviewed; "
            "12‑month KPIs are available; projects are listed and 'PROJ004' details are visible; the A/R aging PDF exists for '2024-10'."
        ),
        actions=[
            Action(name="update_publisher_contact", kwargs={"publisher_id": "PUB004", "contact_email": "ap@bluepeakpublishing.ca"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB004"}),

            Action(name="update_publisher_contact", kwargs={"publisher_id": "PUB005", "contact_email": "ap@westwoodpress.ca"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB005"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="fetch_projects", kwargs={}),
            Action(name="get_project_details", kwargs={"project_id": "PROJ004"}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"})
        ],
        outputs=[
            "PUB004 and PUB005 AP updated & read; open invoices reviewed; KPIs computed; projects listed; PROJ004 read; AR_Aging_2024-10 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_026",
        instruction=(
            "You add a project for 'PUB001' and confirm an August‑2024 total. End state: project_id 'PROJ2035' exists with isbn '978-1-3100-2035-3', "
            "project_title 'Chemistry Workbook, 1e', default_hourly_rate 87.0 and is visible; rates are resolved for ['PROJ2035','PROJ001'] and a sample "
            "total is computed (2h @87.0 and 2h @85.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-08'."
        ),
        actions=[
            Action(name="create_project", kwargs={
                "project_id": "PROJ2035",
                "publisher_id": "PUB001",
                "isbn": "978-1-3100-2035-3",
                "project_title": "Chemistry Workbook, 1e",
                "default_hourly_rate": 87.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ2035"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ2035", "PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 87.0}, {"hours": 2, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"})
        ],
        outputs=[
            "PROJ2035 created & read; rates resolved; totals computed; AR_Aging_2024-08 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_027",
        instruction=(
            "You update GST references and verify July‑2024 A/R. End state: publisher_id 'PUB002' gst_number equals 'GST-UPDATED-002' and is visible; "
            "consultant_id 'CONS001' gst_number equals '123456789RT0001' and is visible; open invoices are reviewed; 12‑month KPIs are available; "
            "the A/R aging PDF exists for '2024-07'."
        ),
        actions=[
            Action(name="update_publisher_contact", kwargs={"publisher_id": "PUB002", "gst_number": "GST-UPDATED-002"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB002"}),

            Action(name="update_consultant_contact", kwargs={"consultant_id": "CONS001", "gst_number": "123456789RT0001"}),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-07"})
        ],
        outputs=[
            "PUB002 GST updated & read; CONS001 GST updated & read; open invoices reviewed; KPIs computed; AR_Aging_2024-07 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_028",
        instruction=(
            "You add publisher_id 'PUB035' named 'Northern Ridge Press' and anchor a July‑2024 baseline. End state: 'PUB035' exists and is visible; "
            "project_id 'PROJ2041' under 'PUB035' exists with isbn '978-1-3100-2041-6', project_title 'Algebra Readiness, 1e', default_hourly_rate 93.0 "
            "and is visible; a sample total is computed (2h @93.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-07' and a snapshot is stored "
            "for '2024-07-31' referencing that PDF and is readable."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB035", "name": "Northern Ridge Press"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB035"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ2041",
                "publisher_id": "PUB035",
                "isbn": "978-1-3100-2041-6",
                "project_title": "Algebra Readiness, 1e",
                "default_hourly_rate": 93.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ2041"}),

            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 93.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-07"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-07-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-07.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-07-31"})
        ],
        outputs=[
            "PUB035 created & read; PROJ2041 created & read; sample total; AR_Aging_2024-07 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_029",
        instruction=(
            "You register publisher_id 'PUB036' named 'Cedar Grove Texts' and prepare an October‑2024 summary. End state: 'PUB036' exists and is "
            "visible; open invoices are reviewed; 12‑month KPIs are available; the A/R aging PDF exists for '2024-10'; the contact for 'PUB003' "
            "equals 'ap@canopypress.ca' and is readable."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB036", "name": "Cedar Grove Texts"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB036"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),

            Action(name="update_publisher_contact", kwargs={"publisher_id": "PUB003", "contact_email": "ap@canopypress.ca"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB003"})
        ],
        outputs=[
            "PUB036 created & read; open invoices reviewed; KPIs computed; AR_Aging_2024-10 exported; PUB003 AP updated & read."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_030",
        instruction=(
            "You open project_id 'PROJ2044' for 'PUB004' and run a November‑2024 check. End state: 'PROJ2044' exists with isbn '978-1-3100-2044-7', "
            "project_title 'Media Literacy, 1e', default_hourly_rate 101.0 and is visible; rates resolve for ['PROJ2044'] and a sample total is computed "
            "(3h @101.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-11'; representative invoice '2024-010' is readable."
        ),
        actions=[
            Action(name="create_project", kwargs={
                "project_id": "PROJ2044",
                "publisher_id": "PUB004",
                "isbn": "978-1-3100-2044-7",
                "project_title": "Media Literacy, 1e",
                "default_hourly_rate": 101.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ2044"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ2044"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 3, "rate": 101.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),

            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-010"})
        ],
        outputs=[
            "PROJ2044 created & read; rate resolved; total computed; AR_Aging_2024-11 exported; invoice 2024-010 read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_031",
        instruction=(
            "You add publisher_id 'PUB039' named 'Coastal Curriculum Press' and stage a dual export. End state: 'PUB039' exists and is visible; "
            "the A/R aging PDFs exist for '2024-08' and '2024-09'; a dashboard snapshot is stored for '2024-08-31' referencing the '2024-08' PDF "
            "and is readable; open invoices are reviewed."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB039", "name": "Coastal Curriculum Press"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB039"}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-08-31"}),

            Action(name="fetch_invoices", kwargs={"status": "open"})
        ],
        outputs=[
            "PUB039 created & read; AR_Aging_2024-08 and AR_Aging_2024-09 exported; snapshot 2024-08-31 saved & read; open invoices reviewed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_032",
        instruction=(
            "You update two AP contacts and confirm November‑2024 KPIs. End state: 'PUB001' contact_email equals 'accounts@nelson-edu.ca' and is visible; "
            "'PUB003' contact_email equals 'accounts@canopypress.ca' and is visible; open invoices are reviewed; 12‑month KPIs are available; "
            "the A/R aging PDF exists for '2024-11'."
        ),
        actions=[
            Action(name="update_publisher_contact", kwargs={"publisher_id": "PUB001", "contact_email": "accounts@nelson-edu.ca"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB001"}),

            Action(name="update_publisher_contact", kwargs={"publisher_id": "PUB003", "contact_email": "accounts@canopypress.ca"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB003"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"})
        ],
        outputs=[
            "PUB001 and PUB003 AP updated & read; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_033",
        instruction=(
            "You add publisher_id 'PUB041' named 'Evergreen Academic House' and a writing project, then confirm October‑2024 totals. "
            "End state: 'PUB041' exists and is visible; 'PROJ2055' exists with isbn '978-1-3100-2055-8', project_title 'Essay Skills, 1e', "
            "default_hourly_rate 91.0 and is visible; rates resolve for ['PROJ2055','PROJ001'] and a sample total is computed "
            "(2h @91.0 and 1h @85.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-10'."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB041", "name": "Evergreen Academic House"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB041"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ2055",
                "publisher_id": "PUB041",
                "isbn": "978-1-3100-2055-8",
                "project_title": "Essay Skills, 1e",
                "default_hourly_rate": 91.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ2055"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ2055", "PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 91.0}, {"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"})
        ],
        outputs=[
            "PUB041 created & read; PROJ2055 created & read; rates resolved; totals computed; AR_Aging_2024-10 exported."
        ],
    ),




    Task(
        annotator="A",
        user_id="ca_v4_034",
        instruction=(
            "You generate an October‑2024 invoice for publisher_id 'PUB004'. "
            "End state: invoice_number '2024-120' exists for period_start '2024-10-01' and period_end '2024-10-31' "
            "with correct totals for a single line (5h @102.0 with hst_rate 0.13) and is readable; "
            "a line is inserted for project_id 'PROJ2024' with isbn '978-1-3100-2024-6' (5h @102.0) and is listable; "
            "the A/R aging PDF exists for period label '2024-10'. "
            "Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-120.pdf'."
        ),
        actions=[
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 5, "rate": 102.0}],
                "hst_rate": 0.13
            }),
            Action(name="insert_invoice", kwargs={
                "invoice_number": "2024-120",
                "publisher_id": "PUB004",
                "invoice_date": "2024-10-31",
                "period_start": "2024-10-01",
                "period_end": "2024-10-31",
                "subtotal": 510.0,
                "hst_amount": 66.3,
                "total_due": 576.3,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-120.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-120"}),
            Action(name="insert_invoice_lines", kwargs={
                "invoice_number": "2024-120",
                "lines": [{"project_id": "PROJ2024", "isbn": "978-1-3100-2024-6", "hours": 5, "rate": 102.0}]
            }),
            Action(name="list_invoice_lines", kwargs={"invoice_number": "2024-120"}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "Invoice 2024-120 inserted & read with correct totals; line inserted & listed; AR_Aging_2024-10 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_035",
        instruction=(
            "You open publisher_id 'PUB031' named 'Cardinal Academic' and register a November‑2024 package. "
            "End state: 'PUB031' exists and is readable; project_id 'PROJ2026A' exists under 'PUB031' with "
            "isbn '978-1-3100-2026-1', project_title 'Advanced Writing, 1e', default_hourly_rate 96.0 and is readable; "
            "the rate is resolved for ['PROJ2026A'] and a sample total is computed (3h @96.0 with hst_rate 0.13); "
            "open invoices are reviewed; 12‑month KPIs are available; the A/R aging PDF exists for '2024-11' and "
            "a dashboard snapshot is stored for '2024-11-30' referencing "
            "'https://storage.example.com/reports/AR_Aging_2024-11.pdf' and is readable by id."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB031", "name": "Cardinal Academic"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB031"}),
            Action(name="create_project", kwargs={
                "project_id": "PROJ2026A",
                "publisher_id": "PUB031",
                "isbn": "978-1-3100-2026-1",
                "project_title": "Advanced Writing, 1e",
                "default_hourly_rate": 96.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ2026A"}),
            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ2026A"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 3, "rate": 96.0}], "hst_rate": 0.13}),
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-11-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_id": 1}),
        ],
        outputs=[
            "PUB031 created & read; PROJ2026A created & read; rate resolved & sample total computed; "
            "open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported; snapshot saved & read by id."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_036",
        instruction=(
            "You register publisher_id 'PUB032' named 'Harborview Education' and file summer A/R snapshots. "
            "End state: 'PUB032' exists and is readable; A/R aging PDFs exist for '2024-07' and '2024-06'; "
            "dashboard snapshots are stored for '2024-07-31' and '2024-06-30' referencing those PDFs and are readable by id; "
            "open invoices are reviewed and 12‑month KPIs are available."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB032", "name": "Harborview Education"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB032"}),
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-07"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-07-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-07.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_id": 1}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-06"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-06-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-06.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_id": 2}),
        ],
        outputs=[
            "PUB032 created & read; open invoices reviewed; KPIs computed; AR_Aging_2024-07 and AR_Aging_2024-06 exported; both snapshots saved & read by id."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_037",
        instruction=(
            "You build a January‑2025 risk classification for two invoices and confirm September A/R. "
            "End state: as of '2025-01-15', days outstanding are computed for '2024-026' with period_end '2024-06-30' "
            "and '2024-013' with period_end '2024-06-15' resulting in 199 and 214 days and are categorized; "
            "open invoices for publisher_id 'PUB001' are reviewed; the A/R aging PDF exists for '2024-09'; "
            "an audit event 'risk_categorized' is recorded for '2024-026' and is listable."
        ),
        actions=[
            Action(name="compute_days_outstanding", kwargs={
                "invoices": [
                    {"invoice_number": "2024-026", "period_end": "2024-06-30"},
                    {"invoice_number": "2024-013", "period_end": "2024-06-15"}
                ],
                "today": "2025-01-15"
            }),
            Action(name="categorize_aging", kwargs={
                "aging": [
                    {"invoice_number": "2024-026", "days_outstanding": 199},
                    {"invoice_number": "2024-013", "days_outstanding": 214}
                ]
            }),
            Action(name="fetch_invoices", kwargs={"status": "open", "publisher_id": "PUB001"}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-026", "event_type": "risk_categorized"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-026"}),
        ],
        outputs=[
            "Aging computed & categorized; PUB001 open invoices reviewed; AR_Aging_2024-09 exported; risk audit recorded & listed for 2024-026."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_038",
        instruction=(
            "You create a September‑2024 invoice for publisher_id 'PUB003'. "
            "End state: invoice_number '2024-131' exists for period_start '2024-09-01' and period_end '2024-09-30' "
            "with totals subtotal 388.0, hst_amount 50.44, total_due 438.44 using hst_rate 0.13 and is readable; "
            "invoice lines are inserted for project_id 'PROJ2032' with isbn '978-1-3100-2032-2' (4h @97.0) and are listable; "
            "an audit event 'generated' is recorded and listable. "
            "Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-131.pdf'."
        ),
        actions=[
            Action(name="insert_invoice", kwargs={
                "invoice_number": "2024-131",
                "publisher_id": "PUB003",
                "invoice_date": "2024-09-30",
                "period_start": "2024-09-01",
                "period_end": "2024-09-30",
                "subtotal": 388.0,
                "hst_amount": 50.44,
                "total_due": 438.44,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-131.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-131"}),
            Action(name="insert_invoice_lines", kwargs={
                "invoice_number": "2024-131",
                "lines": [{"project_id": "PROJ2032", "isbn": "978-1-3100-2032-2", "hours": 4, "rate": 97.0}]
            }),
            Action(name="list_invoice_lines", kwargs={"invoice_number": "2024-131"}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-131", "event_type": "generated"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-131"}),
        ],
        outputs=[
            "Invoice 2024-131 inserted & read; lines inserted & listed; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_039",
        instruction=(
            "You establish publisher_id 'PUB033' named 'Prairie Learning Co.' and stage a September‑2024 snapshot. "
            "End state: 'PUB033' exists and is readable; project_id 'PROJ2034' exists with isbn '978-1-3100-2034-6', "
            "project_title 'Prairie Math, 1e', default_hourly_rate 89.0 and is readable; a sample total is computed (3h @89.0, hst_rate 0.13); "
            "open invoices are reviewed; the A/R aging PDF exists for '2024-09' and a dashboard snapshot is stored for '2024-09-30' "
            "referencing 'https://storage.example.com/reports/AR_Aging_2024-09.pdf' and is readable by id."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB033", "name": "Prairie Learning Co."}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB033"}),
            Action(name="create_project", kwargs={
                "project_id": "PROJ2034",
                "publisher_id": "PUB033",
                "isbn": "978-1-3100-2034-6",
                "project_title": "Prairie Math, 1e",
                "default_hourly_rate": 89.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ2034"}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 3, "rate": 89.0}], "hst_rate": 0.13}),
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-09-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-09.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_id": 1}),
        ],
        outputs=[
            "PUB033 created & read; PROJ2034 created & read; sample total; open invoices reviewed; AR_Aging_2024-09 exported; snapshot saved & read by id."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_040",
        instruction=(
            "You verify August‑2024 context around 'PROJ003' and add proper proofing. "
            "End state: projects are listed and 'PROJ003' details are readable; rates resolve for ['PROJ003'] and a sample total "
            "is computed (5h @75.0 with hst_rate 0.13); open invoices are reviewed and 12‑month KPIs are available; "
            "the A/R aging for '2024-08' is exported and a dashboard snapshot for '2024-08-31' referencing "
            "'https://storage.example.com/reports/AR_Aging_2024-08.pdf' is saved and readable by id; "
            "an audit event 'reviewed' is recorded for invoice '2024-009' and listable."
        ),
        actions=[
            Action(name="fetch_projects", kwargs={}),
            Action(name="get_project_details", kwargs={"project_id": "PROJ003"}),
            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ003"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 5, "rate": 75.0}], "hst_rate": 0.13}),
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-08-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_id": 1}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-009", "event_type": "reviewed"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-009"}),
        ],
        outputs=[
            "Projects listed; PROJ003 read; rate resolved; total computed; open invoices reviewed; KPIs computed; "
            "AR_Aging_2024-08 exported; snapshot saved & read by id; invoice 2024-009 audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_041",
        instruction=(
            "You open publisher_id 'PUB034' named 'Silver Birch Academic' and finalize a November‑2024 aging snapshot with context. "
            "End state: 'PUB034' exists and is readable; open invoices are reviewed; 12‑month KPIs are available; "
            "the A/R aging PDF exists for '2024-11' and a dashboard snapshot is saved for '2024-11-30' referencing that PDF and is readable by id; "
            "for confirmation, the rate resolves for ['PROJ001'] and a sample total is computed (2h @85.0, hst_rate 0.13)."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB034", "name": "Silver Birch Academic"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB034"}),
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-11-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_id": 1}),
            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 85.0}], "hst_rate": 0.13}),
        ],
        outputs=[
            "PUB034 created & read; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported; snapshot saved & read by id; rate resolved & sample total computed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_042",
        instruction=(
            "You verify near‑term due status and file a September‑2024 export with proofing. "
            "End state: days outstanding for '2024-024' using period_end '2024-10-31' and today '2024-10-29' "
            "are computed as -2 days and categorized as 'upcoming_due'; open invoices are reviewed; "
            "the A/R aging PDF exists for '2024-09' and a dashboard snapshot for '2024-09-30' referencing "
            "'https://storage.example.com/reports/AR_Aging_2024-09.pdf' is saved and readable by id; "
            "an audit event 'risk_reviewed' is recorded for '2024-024' and is listable."
        ),
        actions=[
            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-024", "period_end": "2024-10-31"}],
                "today": "2024-10-29"
            }),
            Action(name="categorize_aging", kwargs={"aging": [{"invoice_number": "2024-024", "days_outstanding": -2}]}),
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-09-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-09.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_id": 1}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-024", "event_type": "risk_reviewed"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-024"}),
        ],
        outputs=[
            "Upcoming‑due flagged for 2024-024; open invoices reviewed; AR_Aging_2024-09 exported; snapshot saved & read by id; risk audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_043",
        instruction=(
            "You register publisher_id 'PUB037' named 'Seaway Academics' and compile a September‑2024 snapshot. "
            "End state: 'PUB037' exists and is readable; project_id 'PROJ2046' exists under 'PUB037' with isbn '978-1-3100-2046-1', "
            "project_title 'Statistics Primer, 1e', default_hourly_rate 95.0 and is readable; a sample total is computed "
            "(2h @95.0 with hst_rate 0.13); open invoices are reviewed; the A/R aging PDF exists for '2024-09' and a snapshot "
            "is saved for '2024-09-30' referencing 'https://storage.example.com/reports/AR_Aging_2024-09.pdf' and is readable by id."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB037", "name": "Seaway Academics"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB037"}),
            Action(name="create_project", kwargs={
                "project_id": "PROJ2046",
                "publisher_id": "PUB037",
                "isbn": "978-1-3100-2046-1",
                "project_title": "Statistics Primer, 1e",
                "default_hourly_rate": 95.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ2046"}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 95.0}], "hst_rate": 0.13}),
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-09-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-09.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_id": 1}),
        ],
        outputs=[
            "PUB037 created & read; PROJ2046 created & read; sample total; open invoices reviewed; AR_Aging_2024-09 exported; snapshot saved & read by id."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_044",
        instruction=(
            "You validate November‑2024 visibility and a representative invoice. "
            "End state: projects are listed and 'PROJ001' details are readable; open invoices are reviewed and 12‑month KPIs are available; "
            "the A/R aging PDF exists for '2024-11'; for confirmation, the rate resolves for ['PROJ001'] and a sample total is computed "
            "(1h @85.0 with hst_rate 0.13); invoice '2024-025' is readable; an audit event 'reviewed' is recorded for '2024-025' and is listable."
        ),
        actions=[
            Action(name="fetch_projects", kwargs={}),
            Action(name="get_project_details", kwargs={"project_id": "PROJ001"}),
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-025"}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-025", "event_type": "reviewed"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-025"}),
        ],
        outputs=[
            "Projects listed; PROJ001 read; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported; sample total computed; invoice 2024-025 read; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_045",
        instruction=(
            "You create a concise July‑2024 invoice for publisher_id 'PUB004' and log audit. "
            "End state: invoice_number '2024-134' exists for period_start '2024-07-01' and period_end '2024-07-31' "
            "with totals (subtotal 340.0, hst_amount 44.2, total_due 384.2) and is readable; one line is inserted for "
            "project_id 'PROJ001' with isbn '978-1-3100-0001-0' (4h @85.0) and is listable; an audit event 'generated' is recorded and listable. "
            "Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-134.pdf'."
        ),
        actions=[
            Action(name="insert_invoice", kwargs={
                "invoice_number": "2024-134",
                "publisher_id": "PUB004",
                "invoice_date": "2024-07-31",
                "period_start": "2024-07-01",
                "period_end": "2024-07-31",
                "subtotal": 340.0,
                "hst_amount": 44.2,
                "total_due": 384.2,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-134.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-134"}),
            Action(name="insert_invoice_lines", kwargs={
                "invoice_number": "2024-134",
                "lines": [{"project_id": "PROJ001", "isbn": "978-1-3100-0001-0", "hours": 4, "rate": 85.0}]
            }),
            Action(name="list_invoice_lines", kwargs={"invoice_number": "2024-134"}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-134", "event_type": "generated"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-134"}),
        ],
        outputs=[
            "Invoice 2024-134 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_046",
        instruction=(
            "You onboard publisher_id 'PUB040' named 'Red Maple Learning' and add a math project, then build a September‑2024 snapshot. "
            "End state: 'PUB040' exists and is readable; project_id 'PROJ2053' exists with isbn '978-1-3100-2053-4', project_title 'Pre‑Calculus, 1e', "
            "default_hourly_rate 99.0 and is readable; a sample total is computed (2h @99.0 with hst_rate 0.13); "
            "the A/R aging PDF exists for '2024-09' and a dashboard snapshot is stored for '2024-09-30' referencing "
            "'https://storage.example.com/reports/AR_Aging_2024-09.pdf' and is readable by id."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB040", "name": "Red Maple Learning"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB040"}),
            Action(name="create_project", kwargs={
                "project_id": "PROJ2053",
                "publisher_id": "PUB040",
                "isbn": "978-1-3100-2053-4",
                "project_title": "Pre‑Calculus, 1e",
                "default_hourly_rate": 99.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ2053"}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 99.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-09-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-09.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_id": 1}),
        ],
        outputs=[
            "PUB040 created & read; PROJ2053 created & read; sample total; AR_Aging_2024-09 exported; snapshot saved & read by id."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_047",
        instruction=(
            "You formalize an August‑2024 invoice for publisher_id 'PUB005' from an algebra project. "
            "End state: project_id 'PROJ2056' exists with isbn '978-1-3100-2056-5', project_title 'Algebra Toolkit, 1e', "
            "default_hourly_rate 92.0 and is readable; invoice_number '2024-135' exists for period_start '2024-08-01' and "
            "period_end '2024-08-31' with correct totals (3h @92.0, hst_rate 0.13) and is readable; an audit event 'generated' is recorded and listable. "
            "Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-135.pdf'."
        ),
        actions=[
            Action(name="create_project", kwargs={
                "project_id": "PROJ2056",
                "publisher_id": "PUB005",
                "isbn": "978-1-3100-2056-5",
                "project_title": "Algebra Toolkit, 1e",
                "default_hourly_rate": 92.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ2056"}),
            Action(name="insert_invoice", kwargs={
                "invoice_number": "2024-135",
                "publisher_id": "PUB005",
                "invoice_date": "2024-08-31",
                "period_start": "2024-08-01",
                "period_end": "2024-08-31",
                "subtotal": 276.0,
                "hst_amount": 35.88,
                "total_due": 311.88,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-135.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-135"}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-135", "event_type": "generated"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-135"}),
        ],
        outputs=[
            "PROJ2056 created & read; invoice 2024-135 inserted & read; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_048",
        instruction=(
            "You add publisher_id 'PUB042' named 'Bright Horizons Press' and capture a November‑2024 dashboard. "
            "End state: 'PUB042' exists and is readable; open invoices are reviewed and 12‑month KPIs are available; "
            "the A/R aging PDF exists for '2024-11' and a dashboard snapshot is saved for '2024-11-30' referencing that PDF and is readable by id; "
            "a representative invoice '2024-021' is readable; for confirmation, the rate resolves for ['PROJ001'] and a sample total is computed "
            "(2h @85.0 with hst_rate 0.13)."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB042", "name": "Bright Horizons Press"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB042"}),
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-11-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_id": 1}),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-021"}),
            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 85.0}], "hst_rate": 0.13}),
        ],
        outputs=[
            "PUB042 created & read; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported; snapshot saved & read by id; invoice 2024-021 read; sample total computed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_049",
        instruction=(
            "You create a November‑2024 invoice for publisher_id 'PUB005' and log its audit. "
            "End state: before invoicing, you validate a representative time‑entry row with description "
            "'Hours for November', isbn '978-1-3100-2027-8', account_code 'DATA-LIT-1E' and hours_worked 3; "
            "you compute totals for a single line (3h @90.0, hst_rate 0.13); invoice_number '2024-130' exists "
            "for period_start '2024-11-01' and period_end '2024-11-30' with those totals and is readable; "
            "an audit event 'generated' is recorded and listable. Use pdf_path "
            "'https://storage.example.com/invoices/2024/INV-2024-130.pdf'."
        ),
        actions=[
            Action(name="validate_time_entries", kwargs={
                "rows": [{
                    "description": "Hours for November",
                    "isbn": "978-1-3100-2027-8",
                    "account_code": "DATA-LIT-1E",
                    "hours_worked": 3
                }]
            }),
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 3, "rate": 90.0}],
                "hst_rate": 0.13
            }),
            Action(name="insert_invoice", kwargs={
                "invoice_number": "2024-130",
                "publisher_id": "PUB005",
                "invoice_date": "2024-11-30",
                "period_start": "2024-11-01",
                "period_end": "2024-11-30",
                "subtotal": 270.0,
                "hst_amount": 35.1,
                "total_due": 305.1,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-130.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-130"}),
            Action(name="record_invoice_audit", kwargs={
                "invoice_number": "2024-130",
                "event_type": "generated"
            }),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-130"}),
        ],
        outputs=[
            "Time entries validated; totals computed; invoice 2024-130 inserted & read; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_050",
        instruction=(
            "You formalize the November‑2024 email step for a pending invoice. "
            "End state: invoice_number '2024-011' is emailed using publisher_id 'PUB005' and consultant_id 'CONS001' with "
            "subject 'Invoice 2024-011 (November 2024)', body 'Friendly reminder: attached is invoice 2024-011.' and "
            "attachment 'https://storage.example.com/invoices/2024/INV-2024-011.pdf', and the invoice is re‑read with "
            "sent_at populated; an audit event 'emailed' is recorded and listable; open invoices are reviewed; "
            "12‑month KPIs are available; the A/R aging PDF exists for '2024-11'."
        ),
        actions=[
            Action(name="send_invoice_email", kwargs={
                "publisher_id": "PUB005",
                "consultant_id": "CONS001",
                "invoice_number": "2024-011",
                "subject": "Invoice 2024-011 (November 2024)",
                "body_text": "Friendly reminder: attached is invoice 2024-011.",
                "attachment": "https://storage.example.com/invoices/2024/INV-2024-011.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-011"}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-011", "event_type": "emailed"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-011"}),
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "Invoice 2024-011 emailed & re‑read; audit recorded & listed; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_051",
        instruction=(
            "You record a September‑2024 invoice for publisher_id 'PUB001' and log its audit, validating time entries first. "
            "End state: a representative time‑entry row with description 'September hours', isbn '978-1-3100-0001-0', "
            "account_code 'ENG-1E' and hours_worked 6 is validated; invoice_number '2024-132' exists for period_start "
            "'2024-09-01' and period_end '2024-09-30' with totals (subtotal 510.0, hst_amount 66.3, total_due 576.3) and is readable; "
            "an audit event 'generated' is recorded and listable; the A/R aging PDF exists for '2024-09'. Use pdf_path "
            "'https://storage.example.com/invoices/2024/INV-2024-132.pdf'."
        ),
        actions=[
            Action(name="validate_time_entries", kwargs={
                "rows": [{
                    "description": "September hours",
                    "isbn": "978-1-3100-0001-0",
                    "account_code": "ENG-1E",
                    "hours_worked": 6
                }]
            }),
            Action(name="insert_invoice", kwargs={
                "invoice_number": "2024-132",
                "publisher_id": "PUB001",
                "invoice_date": "2024-09-30",
                "period_start": "2024-09-01",
                "period_end": "2024-09-30",
                "subtotal": 510.0,
                "hst_amount": 66.3,
                "total_due": 576.3,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-132.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-132"}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-132", "event_type": "generated"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-132"}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "Time entries validated; invoice 2024-132 inserted & read; audit recorded & listed; AR_Aging_2024-09 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_052",
        instruction=(
            "You create a concise August‑2024 invoice for publisher_id 'PUB002' and log its lifecycle. "
            "End state: invoice_number '2024-133' exists for period_start '2024-08-01' and period_end '2024-08-31' with totals "
            "(subtotal 300.0, hst_amount 39.0, total_due 339.0) and is readable; a single line is inserted for 'PROJ003' with "
            "isbn '978-1-3100-0003-7' (4h @75.0) and is listable; an audit event 'generated' is recorded and listable. "
            "Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-133.pdf'."
        ),
        actions=[
            Action(name="insert_invoice", kwargs={
                "invoice_number": "2024-133",
                "publisher_id": "PUB002",
                "invoice_date": "2024-08-31",
                "period_start": "2024-08-01",
                "period_end": "2024-08-31",
                "subtotal": 300.0,
                "hst_amount": 39.0,
                "total_due": 339.0,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-133.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-133"}),
            Action(name="insert_invoice_lines", kwargs={
                "invoice_number": "2024-133",
                "lines": [
                    {"project_id": "PROJ003", "isbn": "978-1-3100-0003-7", "hours": 4, "rate": 75.0}
                ]
            }),
            Action(name="list_invoice_lines", kwargs={"invoice_number": "2024-133"}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-133", "event_type": "generated"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-133"}),
        ],
        outputs=[
            "Invoice 2024-133 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_053",
        instruction=(
            "You onboard publisher_id 'PUB043' named 'Evergreen Learning Co.' and stage an October‑2024 baseline. "
            "End state: 'PUB043' exists and is readable; project_id 'PROJ3053' under 'PUB043' exists with isbn "
            "'978-1-3100-3053-1', project_title 'Media Literacy, 1e', default_hourly_rate 93.0 and is readable; "
            "rates are resolved for ['PROJ3053','PROJ001']; a sample total is computed (2h @93.0 and 1h @85.0 with hst_rate 0.13); "
            "the A/R aging PDF exists for '2024-10'; a dashboard snapshot is stored for '2024-10-31' referencing that PDF and is readable by date."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB043", "name": "Evergreen Learning Co."}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB043"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ3053",
                "publisher_id": "PUB043",
                "isbn": "978-1-3100-3053-1",
                "project_title": "Media Literacy, 1e",
                "default_hourly_rate": 93.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ3053"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ3053", "PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 93.0}, {"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-10-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-10-31"}),
        ],
        outputs=[
            "PUB043 created & read; PROJ3053 created & read; rates resolved; sample total computed; "
            "AR_Aging_2024-10 exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_054",
        instruction=(
            "You create a concise November‑2024 invoice for publisher_id 'PUB004' and record its audit. "
            "End state: invoice_number '2024-141' exists for period_start '2024-11-01' and period_end '2024-11-30' with correct totals "
            "(4h @88.0, hst_rate 0.13) and is readable; a single line is inserted for project_id 'PROJ003' with isbn '978-1-3100-0003-7' "
            "for 4h @88.0 and is listable; an audit event 'generated' is recorded and listable. "
            "Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-141.pdf'."
        ),
        actions=[
            Action(name="insert_invoice", kwargs={
                "invoice_number": "2024-141",
                "publisher_id": "PUB004",
                "invoice_date": "2024-11-30",
                "period_start": "2024-11-01",
                "period_end": "2024-11-30",
                "subtotal": 352.0,
                "hst_amount": 45.76,
                "total_due": 397.76,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-141.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-141"}),

            Action(name="insert_invoice_lines", kwargs={
                "invoice_number": "2024-141",
                "lines": [{"project_id": "PROJ003", "isbn": "978-1-3100-0003-7", "hours": 4, "rate": 88.0}]
            }),
            Action(name="list_invoice_lines", kwargs={"invoice_number": "2024-141"}),

            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-141", "event_type": "generated"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-141"}),
        ],
        outputs=[
            "Invoice 2024-141 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_055",
        instruction=(
            "You open publisher_id 'PUB044' named 'Cedar Ridge Press' and align an August‑2024 snapshot. "
            "End state: 'PUB044' exists and is readable; project_id 'PROJ3057' exists with isbn '978-1-3100-3057-2', "
            "project_title 'Financial Literacy, 1e', default_hourly_rate 91.0 and is readable; a sample total is computed "
            "(2h @91.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-08' and a dashboard snapshot is stored for '2024-08-31' "
            "referencing that PDF and is readable by date."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB044", "name": "Cedar Ridge Press"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB044"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ3057",
                "publisher_id": "PUB044",
                "isbn": "978-1-3100-3057-2",
                "project_title": "Financial Literacy, 1e",
                "default_hourly_rate": 91.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ3057"}),

            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 91.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-08-31"}),
        ],
        outputs=[
            "PUB044 created & read; PROJ3057 created & read; sample total; AR_Aging_2024-08 exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_056",
        instruction=(
            "You create publisher_id 'PUB045' named 'Northern Summit Press' and prepare a July‑2024 sample. "
            "End state: 'PUB045' exists and is readable; project_id 'PROJ3059' exists with isbn '978-1-3100-3059-6', "
            "project_title 'Intro Philosophy, 1e', default_hourly_rate 87.0 and is readable; rates are resolved for "
            "['PROJ3059','PROJ001']; a sample total is computed (1h @87.0 and 1h @85.0 with hst_rate 0.13); "
            "the A/R aging PDF exists for '2024-07'."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB045", "name": "Northern Summit Press"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB045"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ3059",
                "publisher_id": "PUB045",
                "isbn": "978-1-3100-3059-6",
                "project_title": "Intro Philosophy, 1e",
                "default_hourly_rate": 87.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ3059"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ3059", "PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 1, "rate": 87.0}, {"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-07"}),
        ],
        outputs=[
            "PUB045 created & read; PROJ3059 created & read; rates resolved; sample total; AR_Aging_2024-07 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_057",
        instruction=(
            "You formalize a September‑2024 invoice for publisher_id 'PUB003' and log its audit. "
            "End state: invoice_number '2024-142' exists for period_start '2024-09-01' and period_end '2024-09-30' with correct totals "
            "(2h @97.0, hst_rate 0.13) and is readable; a single line is inserted for project_id 'PROJ003' with isbn '978-1-3100-0003-7' "
            "for 2h @97.0 and is listable; an audit event 'generated' is recorded and listable. "
            "Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-142.pdf'."
        ),
        actions=[
            Action(name="insert_invoice", kwargs={
                "invoice_number": "2024-142",
                "publisher_id": "PUB003",
                "invoice_date": "2024-09-30",
                "period_start": "2024-09-01",
                "period_end": "2024-09-30",
                "subtotal": 194.0,
                "hst_amount": 25.22,
                "total_due": 219.22,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-142.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-142"}),
            Action(name="insert_invoice_lines", kwargs={
                "invoice_number": "2024-142",
                "lines": [{"project_id": "PROJ003", "isbn": "978-1-3100-0003-7", "hours": 2, "rate": 97.0}]
            }),
            Action(name="list_invoice_lines", kwargs={"invoice_number": "2024-142"}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-142", "event_type": "generated"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-142"}),
        ],
        outputs=[
            "Invoice 2024-142 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_058",
        instruction=(
            "You add publisher_id 'PUB047' named 'Horizon Peak Education' and log an August‑2024 snapshot with sample math totals. "
            "End state: 'PUB047' exists and is readable; project_id 'PROJ3064' exists with isbn '978-1-3100-3064-0', "
            "project_title 'Discrete Math, 1e', default_hourly_rate 104.0 and is readable; a sample total is computed "
            "(1h @104.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-08' and a dashboard snapshot is stored for '2024-08-31' "
            "referencing that PDF and is readable by date."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB047", "name": "Horizon Peak Education"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB047"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ3064",
                "publisher_id": "PUB047",
                "isbn": "978-1-3100-3064-0",
                "project_title": "Discrete Math, 1e",
                "default_hourly_rate": 104.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ3064"}),

            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 1, "rate": 104.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-08-31"}),
        ],
        outputs=[
            "PUB047 created & read; PROJ3064 created & read; sample total; aging exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_059",
        instruction=(
            "You create a September‑2024 invoice for publisher_id 'PUB002' with one line and record its audit. "
            "End state: invoice_number '2024-144' exists for period_start '2024-09-01' and period_end '2024-09-30' with correct totals "
            "(3h @75.0, hst_rate 0.13) and is readable; a single line is inserted for 'PROJ003' with isbn '978-1-3100-0003-7' "
            "(3h @75.0) and is listable; an audit event 'generated' is recorded and listable. "
            "Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-144.pdf'."
        ),
        actions=[
            Action(name="insert_invoice", kwargs={
                "invoice_number": "2024-144",
                "publisher_id": "PUB002",
                "invoice_date": "2024-09-30",
                "period_start": "2024-09-01",
                "period_end": "2024-09-30",
                "subtotal": 225.0,
                "hst_amount": 29.25,
                "total_due": 254.25,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-144.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-144"}),

            Action(name="insert_invoice_lines", kwargs={
                "invoice_number": "2024-144",
                "lines": [
                    {"project_id": "PROJ003", "isbn": "978-1-3100-0003-7", "hours": 3, "rate": 75.0}
                ]
            }),
            Action(name="list_invoice_lines", kwargs={"invoice_number": "2024-144"}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-144", "event_type": "generated"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-144"}),
        ],
        outputs=[
            "Invoice 2024-144 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_060",
        instruction=(
            "You add publisher_id 'PUB051' named 'Maple Grove Education' and register a writing project for an October‑2024 check. "
            "End state: 'PUB051' exists and is readable; project_id 'PROJ3073' exists with isbn '978-1-3100-3073-8', "
            "project_title 'Advanced Composition, 1e', default_hourly_rate 95.0 and is readable; rates are resolved for "
            "['PROJ3073','PROJ001']; a sample total is computed (2h @95.0 and 1h @85.0 with hst_rate 0.13); "
            "the A/R aging PDF exists for '2024-10'."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB051", "name": "Maple Grove Education"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB051"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ3073",
                "publisher_id": "PUB051",
                "isbn": "978-1-3100-3073-8",
                "project_title": "Advanced Composition, 1e",
                "default_hourly_rate": 95.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ3073"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ3073", "PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 95.0}, {"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "PUB051 created & read; PROJ3073 created & read; rates resolved; sample total; AR_Aging_2024-10 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_061",
        instruction=(
            "You set up publisher_id 'PUB053' named 'Pine Valley Learning' and confirm an August‑2024 math sample. "
            "End state: 'PUB053' exists and is readable; project_id 'PROJ3076' exists with isbn '978-1-3100-3076-7', "
            "project_title 'Linear Algebra, 1e', default_hourly_rate 101.0 and is readable; a sample total is computed "
            "(2h @101.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-08'."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB053", "name": "Pine Valley Learning"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB053"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ3076",
                "publisher_id": "PUB053",
                "isbn": "978-1-3100-3076-7",
                "project_title": "Linear Algebra, 1e",
                "default_hourly_rate": 101.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ3076"}),

            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 101.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "PUB053 created & read; PROJ3076 created & read; sample total; AR_Aging_2024-08 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_062",
        instruction=(
            "You refresh November‑2024 context and categorize a representative invoice, storing a dashboard snapshot. "
            "End state: open invoices are reviewed; 12‑month KPIs are available; days outstanding for invoice '2024-009' as of '2024-11-15' "
            "using period_end '2024-09-30' (46 days) are categorized; the A/R aging PDF exists for '2024-11'; "
            "a dashboard snapshot is stored for '2024-11-30' referencing that PDF and is readable by date."
        ),
        actions=[
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-009", "period_end": "2024-09-30"}],
                "today": "2024-11-15"
            }),
            Action(name="categorize_aging", kwargs={"aging": [{"invoice_number": "2024-009", "days_outstanding": 46}]}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-11-30", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-11-30"}),
        ],
        outputs=[
            "Open invoices reviewed; KPIs computed; 46 days categorized for 2024-009; AR_Aging_2024-11 exported; snapshot saved & read by date."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_063",
        instruction=(
            "You add publisher_id 'PUB054' named 'Aspen Trail Press' and stage a September‑2024 readiness check. "
            "End state: 'PUB054' exists and is readable; project_id 'PROJ3078' exists with isbn '978-1-3100-3078-1', "
            "project_title 'World History, 1e', default_hourly_rate 92.0 and is readable; rates are resolved for ['PROJ3078']; "
            "a sample total is computed (3h @92.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-09'."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB054", "name": "Aspen Trail Press"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB054"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ3078",
                "publisher_id": "PUB054",
                "isbn": "978-1-3100-3078-1",
                "project_title": "World History, 1e",
                "default_hourly_rate": 92.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ3078"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ3078"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 3, "rate": 92.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "PUB054 created & read; PROJ3078 created & read; rate resolved; sample total; AR_Aging_2024-09 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_064",
        instruction=(
            "You generate an August‑2024 invoice for publisher_id 'PUB002' and log its audit. "
            "End state: invoice_number '2024-146' exists for period_start '2024-08-01' and period_end '2024-08-31' with correct totals "
            "(2h @85.0, hst_rate 0.13) and is readable; one line is inserted for 'PROJ001' with isbn '978-1-3100-0001-0' (2h @85.0) and is listable; "
            "an audit event 'generated' is recorded and listable. "
            "Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-146.pdf'."
        ),
        actions=[
            Action(name="insert_invoice", kwargs={
                "invoice_number": "2024-146",
                "publisher_id": "PUB002",
                "invoice_date": "2024-08-31",
                "period_start": "2024-08-01",
                "period_end": "2024-08-31",
                "subtotal": 170.0,
                "hst_amount": 22.1,
                "total_due": 192.1,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-146.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-146"}),

            Action(name="insert_invoice_lines", kwargs={
                "invoice_number": "2024-146",
                "lines": [{"project_id": "PROJ001", "isbn": "978-1-3100-0001-0", "hours": 2, "rate": 85.0}]
            }),
            Action(name="list_invoice_lines", kwargs={"invoice_number": "2024-146"}),

            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-146", "event_type": "generated"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-146"}),
        ],
        outputs=[
            "Invoice 2024-146 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_065",
        instruction=(
            "You create publisher_id 'PUB055' named 'Summit Ridge Learning' and establish an October‑2024 dashboard with a small sample. "
            "End state: 'PUB055' exists and is readable; open invoices are reviewed; 12‑month KPIs are available; "
            "rates are resolved for ['PROJ001']; a sample total is computed (1h @85.0 with hst_rate 0.13); "
            "the A/R aging PDF exists for '2024-10'; a dashboard snapshot is stored for '2024-10-31' "
            "referencing that PDF and is readable by date."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB055", "name": "Summit Ridge Learning"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB055"}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-10-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-10-31"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
        ],
        outputs=[
            "PUB055 created & read; AR_Aging_2024-10 exported; snapshot saved & read by date; open invoices reviewed; KPIs computed; rate resolved; sample total."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_066",
        instruction=(
            "You add publisher_id 'PUB056' named 'Cobalt Creek Press' and prepare a September‑2024 sample with rates. "
            "End state: 'PUB056' exists and is readable; project_id 'PROJ3083' exists with isbn '978-1-3100-3083-6', "
            "project_title 'Intro Sociology, 1e', default_hourly_rate 86.0 and is readable; rates are resolved for "
            "['PROJ3083','PROJ001']; a sample total is computed (2h @86.0 and 1h @85.0 with hst_rate 0.13); "
            "the A/R aging PDF exists for '2024-09'."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB056", "name": "Cobalt Creek Press"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB056"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ3083",
                "publisher_id": "PUB056",
                "isbn": "978-1-3100-3083-6",
                "project_title": "Intro Sociology, 1e",
                "default_hourly_rate": 86.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ3083"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ3083", "PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 86.0}, {"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "PUB056 created & read; PROJ3083 created & read; rates resolved; sample total; AR_Aging_2024-09 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_067",
        instruction=(
            "You record an October‑2024 invoice for publisher_id 'PUB005' and verify its line items. "
            "End state: invoice_number '2024-147' exists for period_start '2024-10-01' and period_end '2024-10-31' with correct totals "
            "(4h @90.0, hst_rate 0.13) and is readable; a single line is inserted for project_id 'PROJ003' with isbn '978-1-3100-0003-7' "
            "(4h @90.0) and is listable; an audit event 'generated' is recorded and listable. "
            "Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-147.pdf'."
        ),
        actions=[
            Action(name="insert_invoice", kwargs={
                "invoice_number": "2024-147",
                "publisher_id": "PUB005",
                "invoice_date": "2024-10-31",
                "period_start": "2024-10-01",
                "period_end": "2024-10-31",
                "subtotal": 360.0,
                "hst_amount": 46.8,
                "total_due": 406.8,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-147.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-147"}),

            Action(name="insert_invoice_lines", kwargs={
                "invoice_number": "2024-147",
                "lines": [{"project_id": "PROJ003", "isbn": "978-1-3100-0003-7", "hours": 4, "rate": 90.0}]
            }),
            Action(name="list_invoice_lines", kwargs={"invoice_number": "2024-147"}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-147", "event_type": "generated"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-147"}),
        ],
        outputs=[
            "Invoice 2024-147 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_068",
        instruction=(
            "You formalize a September‑2024 invoice for publisher_id 'PUB004' with one project and verify context. "
            "End state: invoice_number '2024-148' exists for period_start '2024-09-01' and period_end '2024-09-30' with correct totals "
            "(2h @85.0, hst_rate 0.13) and is readable; a single line is inserted for 'PROJ001' (2h @85.0, isbn '978-1-3100-0001-0') and is listable; "
            "an audit event 'generated' is recorded and listable. Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-148.pdf'."
        ),
        actions=[
            Action(name="insert_invoice", kwargs={
                "invoice_number": "2024-148",
                "publisher_id": "PUB004",
                "invoice_date": "2024-09-30",
                "period_start": "2024-09-01",
                "period_end": "2024-09-30",
                "subtotal": 170.0,
                "hst_amount": 22.1,
                "total_due": 192.1,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-148.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-148"}),

            Action(name="insert_invoice_lines", kwargs={
                "invoice_number": "2024-148",
                "lines": [
                    {"project_id": "PROJ001", "isbn": "978-1-3100-0001-0", "hours": 2, "rate": 85.0}
                ]
            }),
            Action(name="list_invoice_lines", kwargs={"invoice_number": "2024-148"}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-148", "event_type": "generated"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-148"}),
        ],
        outputs=[
            "Invoice 2024-148 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_069",
        instruction=(
            "You add project_id 'PROJ3054' for publisher_id 'PUB005' and confirm a November‑2024 sample with an explicit aging check. "
            "End state: 'PROJ3054' exists with isbn '978-1-3100-3054-8', project_title 'Canadian Literature, 2e', "
            "default_hourly_rate 90.0 and is readable; rates are resolved for ['PROJ3054']; a sample total is computed "
            "(3h @90.0 with hst_rate 0.13); days outstanding for '2024-010' as of '2024-11-15' using period_end '2024-10-31' "
            "(15 days) are categorized; the A/R aging PDF exists for '2024-11'."
        ),
        actions=[
            Action(name="create_project", kwargs={
                "project_id": "PROJ3054",
                "publisher_id": "PUB005",
                "isbn": "978-1-3100-3054-8",
                "project_title": "Canadian Literature, 2e",
                "default_hourly_rate": 90.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ3054"}),
            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ3054"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 3, "rate": 90.0}], "hst_rate": 0.13}),
            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-010", "period_end": "2024-10-31"}],
                "today": "2024-11-15"
            }),
            Action(name="categorize_aging", kwargs={"aging": [{"invoice_number": "2024-010", "days_outstanding": 15}]}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "PROJ3054 created & read; rate resolved; sample total computed; 15 days categorized for 2024-010; AR_Aging_2024-11 exported."
        ],
    ),    
    Task(
        annotator="A",
        user_id="ca_v4_070",
        instruction=(
            "You validate readiness for November‑2024 around project_id 'PROJ001' and record an aging categorization. "
            "End state: projects are listed and 'PROJ001' details are readable; rates are resolved for ['PROJ001']; "
            "a sample total is computed (3h @85.0 with hst_rate 0.13); open invoices are reviewed; 12‑month KPIs are available; "
            "the A/R aging PDF exists for '2024-11'; days outstanding for invoice '2024-010' as of '2024-11-20' using period_end '2024-10-31' "
            "(20 days) are categorized; an invoice audit event 'aging_categorized' is recorded for '2024-010' and listable."
        ),
        actions=[
            Action(name="fetch_projects", kwargs={}),
            Action(name="get_project_details", kwargs={"project_id": "PROJ001"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 3, "rate": 85.0}], "hst_rate": 0.13}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),

            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-010", "period_end": "2024-10-31"}],
                "today": "2024-11-20"
            }),
            Action(name="categorize_aging", kwargs={"aging": [{"invoice_number": "2024-010", "days_outstanding": 20}]}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-010", "event_type": "aging_categorized"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-010"}),
        ],
        outputs=[
            "Projects listed; PROJ001 read; rate resolved; sample total; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported; "
            "20 days categorized for 2024-010; audit recorded & listed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_071",
        instruction=(
            "You normalize contacts and verify an October‑2024 sample for publisher_id 'PUB003' with an aging categorization. "
            "End state: 'PUB003' contact_email equals 'accounts@canopypress.ca' and is readable; "
            "CONS001 address equals '1234 Oak Street, Toronto, ON M5V 3A8' and is readable; "
            "rates are resolved for ['PROJ003']; a sample total is computed (2h @75.0 with hst_rate 0.13); "
            "days outstanding for '2024-010' as of '2024-11-15' using period_end '2024-10-31' (15 days) are categorized; "
            "the A/R aging PDF exists for '2024-10'."
        ),
        actions=[
            Action(name="update_publisher_contact", kwargs={"publisher_id": "PUB003", "contact_email": "accounts@canopypress.ca"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB003"}),

            Action(name="update_consultant_contact", kwargs={"consultant_id": "CONS001", "address": "1234 Oak Street, Toronto, ON M5V 3A8"}),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ003"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 75.0}], "hst_rate": 0.13}),
            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-010", "period_end": "2024-10-31"}],
                "today": "2024-11-15"
            }),
            Action(name="categorize_aging", kwargs={"aging": [{"invoice_number": "2024-010", "days_outstanding": 15}]}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "PUB003 AP updated & read; CONS001 address updated & read; rate resolved; sample total; 15 days categorized for 2024-010; AR_Aging_2024-10 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_072",
        instruction=(
            "You create publisher_id 'PUB049' named 'Blue Shore Academics' with a civics project and confirm a September‑2024 context. "
            "End state: 'PUB049' exists and is readable; project_id 'PROJ3069' exists with isbn '978-1-3100-3069-4', "
            "project_title 'Civics Foundations, 1e', default_hourly_rate 88.0 and is readable; open invoices are reviewed; "
            "12‑month KPIs are available; a sample total is computed (2h @88.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-09'."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB049", "name": "Blue Shore Academics"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB049"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ3069",
                "publisher_id": "PUB049",
                "isbn": "978-1-3100-3069-4",
                "project_title": "Civics Foundations, 1e",
                "default_hourly_rate": 88.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ3069"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 2, "rate": 88.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "PUB049 created & read; PROJ3069 created & read; open invoices reviewed; KPIs computed; sample total; AR_Aging_2024-09 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_073",
        instruction=(
            "You formalize a November‑2024 email for invoice '2024-010' and capture the audit with context. "
            "End state: invoice_number '2024-010' is emailed using publisher_id 'PUB005' and consultant_id 'CONS001' with subject "
            "'Invoice 2024-010 (November 2024)', body 'Please see attached invoice 2024-010.' and attachment "
            "'https://storage.example.com/invoices/2024/INV-2024-010.pdf', and the invoice is re‑read with sent_at populated; "
            "an audit event 'emailed' is recorded and listable; open invoices are reviewed; 12‑month KPIs are available; the A/R aging PDF exists for '2024-11'."
        ),
        actions=[
            Action(name="send_invoice_email", kwargs={
                "publisher_id": "PUB005",
                "consultant_id": "CONS001",
                "invoice_number": "2024-010",
                "subject": "Invoice 2024-010 (November 2024)",
                "body_text": "Please see attached invoice 2024-010.",
                "attachment": "https://storage.example.com/invoices/2024/INV-2024-010.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-010"}),
            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-010", "event_type": "emailed"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-010"}),
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "Invoice 2024-010 emailed & re‑read; audit recorded & listed; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_074",
        instruction=(
            "You ensure November‑2024 readiness for publisher_id 'PUB004' by creating a data science project and confirming totals with an aging categorization. "
            "End state: project_id 'PROJ3081' exists with isbn '978-1-3100-3081-2', project_title 'Data Science Projects, 1e', "
            "default_hourly_rate 106.0 and is readable; rates are resolved for ['PROJ3081']; a sample total is computed (1h @106.0 with hst_rate 0.13); "
            "open invoices are reviewed; the A/R aging PDF exists for '2024-11'; days outstanding for '2024-010' as of '2024-11-15' using period_end '2024-10-31' "
            "(15 days) are categorized."
        ),
        actions=[
            Action(name="create_project", kwargs={
                "project_id": "PROJ3081",
                "publisher_id": "PUB004",
                "isbn": "978-1-3100-3081-2",
                "project_title": "Data Science Projects, 1e",
                "default_hourly_rate": 106.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ3081"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ3081"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 1, "rate": 106.0}], "hst_rate": 0.13}),
            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),

            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-010", "period_end": "2024-10-31"}],
                "today": "2024-11-15"
            }),
            Action(name="categorize_aging", kwargs={"aging": [{"invoice_number": "2024-010", "days_outstanding": 15}]}),
        ],
        outputs=[
            "PROJ3081 created & read; rate resolved; sample total; open invoices reviewed; AR_Aging_2024-11 exported; 15 days categorized for 2024-010."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_075",
        instruction=(
            "You tidy September‑2024 contact details and log an upcoming‑due classification with context. "
            "End state: publisher_id 'PUB001' contact_email equals 'accounts@nelson-edu.ca' and is readable; "
            "days outstanding for invoice '2024-024' as of '2024-09-29' using period_end '2024-10-01' (‑2 days) are categorized as 'upcoming_due'; "
            "an invoice audit event 'aging_categorized' is recorded for '2024-024' and listable; open invoices are reviewed; 12‑month KPIs are available; "
            "the A/R aging PDF exists for '2024-09'."
        ),
        actions=[
            Action(name="update_publisher_contact", kwargs={"publisher_id": "PUB001", "contact_email": "accounts@nelson-edu.ca"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB001"}),

            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-024", "period_end": "2024-10-01"}],
                "today": "2024-09-29"
            }),
            Action(name="categorize_aging", kwargs={"aging": [{"invoice_number": "2024-024", "days_outstanding": -2}]}),

            Action(name="record_invoice_audit", kwargs={"invoice_number": "2024-024", "event_type": "aging_categorized"}),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-024"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "PUB001 AP updated & read; upcoming‑due flagged for 2024-024; audit recorded & listed; open invoices reviewed; KPIs computed; AR_Aging_2024-09 exported."
        ],
    ),    
    Task(
        annotator="A",
        user_id="ca_v4_076",
        instruction=(
            "You add publisher_id 'PUB048' named 'Bright Pine Press' and align November‑2024 reporting with a small sample. "
            "End state: 'PUB048' exists and is readable; open invoices are reviewed; 12‑month KPIs are available; "
            "rates are resolved for ['PROJ001']; a sample total is computed (1h @85.0 with hst_rate 0.13); "
            "the A/R aging PDF exists for '2024-11'; a dashboard snapshot is stored for '2024-11-30' and is readable by date."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB048", "name": "Bright Pine Press"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB048"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-11-30", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-11-30"}),
        ],
        outputs=[
            "PUB048 created & read; open invoices reviewed; KPIs computed; rate resolved; sample total; AR_Aging_2024-11 exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_077",
        instruction=(
            "You add publisher_id 'PUB057' named 'Harbor Lights Learning' and stage an August‑2024 dashboard with a small total. "
            "End state: 'PUB057' exists and is readable; a sample total is computed (1h @85.0 with hst_rate 0.13) using rate for ['PROJ001']; "
            "the A/R aging PDF exists for '2024-08'; a dashboard snapshot is stored for '2024-08-31' and is readable by date; "
            "days outstanding for '2024-010' as of '2024-08-15' using period_end '2024-07-31' (15 days) are categorized."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB057", "name": "Harbor Lights Learning"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB057"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-08-31"}),

            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-010", "period_end": "2024-07-31"}],
                "today": "2024-08-15"
            }),
            Action(name="categorize_aging", kwargs={"aging": [{"invoice_number": "2024-010", "days_outstanding": 15}]}),
        ],
        outputs=[
            "PUB057 created & read; rate resolved; sample total; AR_Aging_2024-08 exported; snapshot saved & read by date; 15 days categorized for 2024-010."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_078",
        instruction=(
            "You introduce publisher_id 'PUB046' named 'Lantern House Education' and prepare a November‑2024 snapshot. "
            "End state: 'PUB046' exists and is readable; project_id 'PROJ3061' exists with isbn '978-1-3100-3061-9', "
            "project_title 'Critical Thinking, 1e', default_hourly_rate 99.0 and is readable; open invoices are reviewed; "
            "12‑month KPIs are available; the A/R aging PDF exists for '2024-11'; a dashboard snapshot is stored for '2024-11-30' and is readable by date."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB046", "name": "Lantern House Education"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB046"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ3061",
                "publisher_id": "PUB046",
                "isbn": "978-1-3100-3061-9",
                "project_title": "Critical Thinking, 1e",
                "default_hourly_rate": 99.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ3061"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-11-30", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-11-30"}),
        ],
        outputs=[
            "PUB046 created & read; PROJ3061 created & read; open invoices reviewed; KPIs computed; aging exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_079",
        instruction=(
            "You compute and categorize a November‑2024 aging check and verify context with a saved snapshot. "
            "End state: days outstanding for invoice '2024-021' as of '2024-11-20' using period_end '2024-10-31' (20 days) are categorized; "
            "projects are listed; 'PROJ003' details are readable; rates are resolved for ['PROJ003']; a sample total is computed (1h @75.0 with hst_rate 0.13); "
            "open invoices are reviewed; 12‑month KPIs are available; the A/R aging PDF exists for '2024-11'; a dashboard snapshot is stored for '2024-11-30' and is readable by date."
        ),
        actions=[
            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-021", "period_end": "2024-10-31"}],
                "today": "2024-11-20"
            }),
            Action(name="categorize_aging", kwargs={"aging": [{"invoice_number": "2024-021", "days_outstanding": 20}]}),

            Action(name="fetch_projects", kwargs={}),
            Action(name="get_project_details", kwargs={"project_id": "PROJ003"}),
            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ003"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 1, "rate": 75.0}], "hst_rate": 0.13}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-11-30", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-11-30"}),
        ],
        outputs=[
            "20 days categorized for 2024-021; projects listed; PROJ003 read; rate resolved; sample total; open invoices reviewed; KPIs computed; "
            "AR_Aging_2024-11 exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_080",
        instruction=(
            "You add publisher_id 'PUB050' named 'Riverbend Academic' and store an August‑2024 dashboard with a small sample. "
            "End state: 'PUB050' exists and is readable; open invoices are reviewed; 12‑month KPIs are available; "
            "rates are resolved for ['PROJ001']; a sample total is computed (1h @85.0 with hst_rate 0.13); "
            "the A/R aging PDF exists for '2024-08'; a dashboard snapshot is stored for '2024-08-31' and is readable by date."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB050", "name": "Riverbend Academic"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB050"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-08-31"}),
        ],
        outputs=[
            "PUB050 created & read; open invoices reviewed; KPIs computed; rate resolved; sample total; AR_Aging_2024-08 exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_081",
        instruction=(
            "You register publisher_id 'PUB052' named 'Aurora Ridge Press' and store a November‑2024 snapshot with a small sample. "
            "End state: 'PUB052' exists and is readable; open invoices are reviewed; 12‑month KPIs are available; "
            "rates are resolved for ['PROJ001']; a sample total is computed (1h @85.0 with hst_rate 0.13); "
            "the A/R aging PDF exists for '2024-11'; a dashboard snapshot is stored for '2024-11-30' and is readable by date."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB052", "name": "Aurora Ridge Press"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB052"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),
            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-11-30", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-11-30"}),
        ],
        outputs=[
            "PUB052 created & read; open invoices reviewed; KPIs computed; rate resolved; sample total; AR_Aging_2024-11 exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_082",
        instruction=(
            "You add publisher_id 'PUB057' named 'Harbor Lights Learning' and stage an August‑2024 dashboard with a small total. "
            "End state: 'PUB057' exists and is readable; a sample total is computed (1h @85.0 with hst_rate 0.13) using rate for ['PROJ001']; "
            "the A/R aging PDF exists for '2024-08'; a dashboard snapshot is stored for '2024-08-31' referencing "
            "'https://storage.example.com/reports/AR_Aging_2024-08.pdf' and is readable by date; "
            "days outstanding for '2024-010' as of '2024-08-15' using period_end '2024-07-31' (15 days) are categorized."
        ),
        actions=[
            Action(name="create_publisher", kwargs={"publisher_id": "PUB057", "name": "Harbor Lights Learning"}),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB057"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={"lines": [{"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
            Action(name="insert_dashboard_snapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-08-31"}),

            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-010", "period_end": "2024-07-31"}],
                "today": "2024-08-15"
            }),
            Action(name="categorize_aging", kwargs={"aging": [{"invoice_number": "2024-010", "days_outstanding": 15}]}),
        ],
        outputs=[
            "PUB057 created & read; rate resolved; sample total; AR_Aging_2024-08 exported; snapshot saved & read by date; 15 days categorized for 2024-010."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_083",
        instruction=(
            "You onboard a new client and align an October‑2024 snapshot. End state: "
            "publisher_id 'PUB021' named 'Algonquin Scholastic' exists and is readable; "
            "project_id 'PROJ1102' exists under 'PUB021' with isbn '978-1-3100-1010-1', project_title 'Intro Statistics, 1e', default_hourly_rate 95.0 and is readable; "
            "rates are resolved for ['PROJ1102','PROJ001'] and sample totals are computed (3h @95.0 and 2h @85.0); "
            "A/R aging for '2024-10' is exported and a snapshot stored for '2024-10-31' using the same PDF."
        ),
        actions=[
            Action(name="create_publisher", kwargs={
                "publisher_id": "PUB021",
                "name": "Algonquin Scholastic"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB021"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ1102",
                "publisher_id": "PUB021",
                "isbn": "978-1-3100-1010-1",
                "project_title": "Intro Statistics, 1e",
                "default_hourly_rate": 95.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ1102"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ1102", "PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 3, "rate": 95.0}, {"hours": 2, "rate": 85.0}],
                "hst_rate": 0.13
            }),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-10-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-10-31"}),
        ],
        outputs=[
            "PUB021 created & read; PROJ1102 created & read; rates resolved; totals computed; AR_Aging_2024-10 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_084",
        instruction=(
            "You open a new publisher and align a November‑2024 review. End state: "
            "publisher_id 'PUB022' named 'Bayview K12' exists and is readable; "
            "project_id 'PROJ1104' exists under 'PUB022' with isbn '978-1-3100-1013-2', project_title 'Civics Basics, 1e', default_hourly_rate 80.0 and is readable; "
            "rates are resolved for ['PROJ1104'] and a sample total is computed (6h @80.0); "
            "open invoices are reviewed and 12‑month KPIs are available; "
            "A/R aging for '2024-11' is exported and a snapshot stored for '2024-11-30'."
        ),
        actions=[
            Action(name="create_publisher", kwargs={
                "publisher_id": "PUB022",
                "name": "Bayview K12"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB022"}),

            Action(name="create_project", kwargs={
                "project_id": "PROJ1104",
                "publisher_id": "PUB022",
                "isbn": "978-1-3100-1013-2",
                "project_title": "Civics Basics, 1e",
                "default_hourly_rate": 80.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ1104"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ1104"]}),
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 6, "rate": 80.0}],
                "hst_rate": 0.13
            }),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-11-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-11-30"}),
        ],
        outputs=[
            "PUB022 created & read; PROJ1104 created & read; rate resolved; total computed; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_085",
        instruction=(
            "You normalize contacts and run a quick October‑2024 health check. End state: "
            "consultant_id 'CONS001' phone equals '+1-416-555-0177' and is readable; "
            "publisher_id 'PUB004' is readable; "
            "open invoices are reviewed and 12‑month KPIs are available; "
            "A/R aging for '2024-10' is exported."
        ),
        actions=[
            Action(name="update_consultant_contact", kwargs={
                "consultant_id": "CONS001",
                "phone": "+1-416-555-0177"
            }),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB004"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "CONS001 phone updated & read; PUB004 read; open invoices reviewed; KPIs computed; AR_Aging_2024-10 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_086",
        instruction=(
            "You register a data‑science project and complete an October‑2024 risk pass for publisher_id 'PUB004'. End state: "
            "project_id 'PROJ1105' exists with isbn '978-1-3100-1014-9', project_title 'Data Science Labs, 1e', default_hourly_rate 105.0 and is readable; "
            "a sample total is computed (4h @105.0 with hst_rate 0.13); "
            "A/R aging '2024-10' is exported and a snapshot stored for '2024-10-31'; "
            "a risk check computes days outstanding for invoice_number '2024-024' using due_date '2024-10-31' as of '2024-11-10' and categorizes it."
        ),
        actions=[
            Action(name="create_project", kwargs={
                "project_id": "PROJ1105",
                "publisher_id": "PUB004",
                "isbn": "978-1-3100-1014-9",
                "project_title": "Data Science Labs, 1e",
                "default_hourly_rate": 105.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ1105"}),

            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 4, "rate": 105.0}],
                "hst_rate": 0.13
            }),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-10-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-10-31"}),

            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-024", "period_end": "2024-10-31"}],
                "today": "2024-11-10"
            }),
            Action(name="categorize_aging", kwargs={
                "aging": [{"invoice_number": "2024-024", "days_outstanding": 10}]
            }),
        ],
        outputs=[
            "PROJ1105 created & read; sample total; AR_Aging_2024-10 exported; snapshot saved & read; 2024-024 aging categorized."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_087",
        instruction=(
            "You open a new publisher and file an August‑2024 snapshot. End state: "
            "publisher_id 'PUB023' named 'North Shore Academy' exists and is readable; "
            "contact_email equals 'accounts@northshoreacademy.ca' and is readable; "
            "A/R aging for '2024-08' is exported and a snapshot stored for '2024-08-31'."
        ),
        actions=[
            Action(name="create_publisher", kwargs={
                "publisher_id": "PUB023",
                "name": "North Shore Academy"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB023"}),

            Action(name="update_publisher_contact", kwargs={
                "publisher_id": "PUB023",
                "contact_email": "accounts@northshoreacademy.ca"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB023"}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-08-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-08-31"}),
        ],
        outputs=[
            "PUB023 created & read; AP updated & read; AR_Aging_2024-08 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_088",
        instruction=(
            "You reconcile July‑2024 A/R for publisher_id 'PUB002'. End state: "
            "publisher_id 'PUB002' is readable; "
            "a risk check computes days outstanding for invoice_number '2024-023' using due_date '2024-07-15' as of '2024-07-20' and categorizes it; "
            "A/R aging for '2024-07' is exported and a snapshot is stored for '2024-07-31'."
        ),
        actions=[
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB002"}),

            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-023", "period_end": "2024-07-15"}],
                "today": "2024-07-20"
            }),
            Action(name="categorize_aging", kwargs={
                "aging": [{"invoice_number": "2024-023", "days_outstanding": 5}]
            }),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-07"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-07-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-07.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-07-31"}),
        ],
        outputs=[
            "PUB002 read; 2024-023 aging categorized; AR_Aging_2024-07 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_089",
        instruction=(
            "You add a humanities project and align an August‑2024 review. End state: "
            "project_id 'PROJ1106' exists for 'PUB003' with isbn '978-1-3100-1015-6', project_title 'Philosophy Primer, 1e', default_hourly_rate 91.0 and is readable; "
            "rates are resolved for ['PROJ1106'] and a sample total is computed (2h @91.0); "
            "A/R aging for '2024-08' is exported and a snapshot stored for '2024-08-31'."
        ),
        actions=[
            Action(name="create_project", kwargs={
                "project_id": "PROJ1106",
                "publisher_id": "PUB003",
                "isbn": "978-1-3100-1015-6",
                "project_title": "Philosophy Primer, 1e",
                "default_hourly_rate": 91.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ1106"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ1106"]}),
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 2, "rate": 91.0}],
                "hst_rate": 0.13
            }),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-08"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-08-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-08-31"}),
        ],
        outputs=[
            "PROJ1106 created & read; rate resolved; total computed; AR_Aging_2024-08 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_090",
        instruction=(
            "You update billing contacts and compute a November‑2024 confirmation. End state: "
            "publisher_id 'PUB003' contact_email equals 'ap@canopypress.ca' and is readable; "
            "consultant_id 'CONS001' email equals 'sarah.thompson+ar@consultingpro.ca' and is readable; "
            "rates are resolved for ['PROJ001','PROJ003'] and a sample total is computed (2h @85.0 and 2h @75.0); "
            "A/R aging for '2024-11' is exported."
        ),
        actions=[
            Action(name="update_publisher_contact", kwargs={
                "publisher_id": "PUB003",
                "contact_email": "ap@canopypress.ca"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB003"}),

            Action(name="update_consultant_contact", kwargs={
                "consultant_id": "CONS001",
                "email": "sarah.thompson+ar@consultingpro.ca"
            }),
            Action(name="get_consultant_profile", kwargs={"consultant_id": "CONS001"}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001", "PROJ003"]}),
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 2, "rate": 85.0}, {"hours": 2, "rate": 75.0}],
                "hst_rate": 0.13
            }),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "PUB003 AP updated & read; CONS001 email updated & read; rates resolved; total computed; AR_Aging_2024-11 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_091",
        instruction=(
            "You create a social studies project and reconcile a July‑2024 snapshot. End state: "
            "project_id 'PROJ1109' exists for 'PUB005' with isbn '978-1-3100-1018-7', project_title 'Social Studies, 1e', default_hourly_rate 90.0 and is readable; "
            "sample totals (2h @90.0 and 2h @90.0) are computed; "
            "A/R aging '2024-07' is exported and a snapshot stored for '2024-07-31'."
        ),
        actions=[
            Action(name="create_project", kwargs={
                "project_id": "PROJ1109",
                "publisher_id": "PUB005",
                "isbn": "978-1-3100-1018-7",
                "project_title": "Social Studies, 1e",
                "default_hourly_rate": 90.0
            }),
            Action(name="get_project_details", kwargs={"project_id": "PROJ1109"}),

            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 2, "rate": 90.0}, {"hours": 2, "rate": 90.0}],
                "hst_rate": 0.13
            }),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-07"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-07-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-07.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-07-31"}),
        ],
        outputs=[
            "PROJ1109 created & read; sample totals; AR_Aging_2024-07 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_092",
        instruction=(
            "You generate and deliver a December‑2024 invoice for publisher_id 'PUB004'. End state: "
            "invoice_number 'INV-2024-401' exists for 'PUB004' with invoice_date '2024-12-31', period_start '2024-12-01', "
            "period_end '2024-12-31', subtotal 1200.0, hst_amount 156.0, total_due 1356.0, "
            "pdf_path '/invoices/2024/INV-2024-401.pdf' and is readable; "
            "the invoice is emailed from consultant_id 'CONS001' with subject 'Invoice INV-2024-401' and body_text 'December 2024 invoice attached.' and attachment "
            "'/invoices/2024/INV-2024-401.pdf'; an 'emailed' audit is recorded and listed."
        ),
        actions=[
            Action(name="insert_invoice", kwargs={
                "invoice_number": "INV-2024-401",
                "publisher_id": "PUB004",
                "invoice_date": "2024-12-31",
                "period_start": "2024-12-01",
                "period_end": "2024-12-31",
                "subtotal": 1200.0,
                "hst_amount": 156.0,
                "total_due": 1356.0,
                "pdf_path": "/invoices/2024/INV-2024-401.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "INV-2024-401"}),

            Action(name="send_invoice_email", kwargs={
                "publisher_id": "PUB004",
                "consultant_id": "CONS001",
                "invoice_number": "INV-2024-401",
                "subject": "Invoice INV-2024-401",
                "body_text": "December 2024 invoice attached.",
                "attachment": "/invoices/2024/INV-2024-401.pdf"
            }),
            Action(name="record_invoice_audit", kwargs={
                "invoice_number": "INV-2024-401",
                "event_type": "emailed"
            }),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "INV-2024-401"}),
            Action(name="get_invoice_details", kwargs={"invoice_number": "INV-2024-401"}),
        ],
        outputs=[
            "Invoice INV-2024-401 inserted & read; emailed; emailed audit recorded & listed; invoice re-read."
        ],
    ),    
    Task(
        annotator="A",
        user_id="ca_v4_093",
        instruction=(
            "You normalize contact info and complete a September‑2024 review for publisher_id 'PUB001'. End state: "
            "contact_email equals 'ap@nelson-edu.ca' and is readable; "
            "invoice_number '2024-021' is readable; an audit event 'review_follow_up' is recorded for '2024-021' and listed; "
            "A/R aging for '2024-09' is exported and a dashboard snapshot is stored for '2024-09-30'; "
            "a quick risk check computes days outstanding for '2024-021' using due_date '2024-09-15' with today '2024-10-01' and categorizes it."
        ),
        actions=[
            Action(name="update_publisher_contact", kwargs={
                "publisher_id": "PUB001",
                "contact_email": "ap@nelson-edu.ca"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB001"}),

            Action(name="get_invoice_details", kwargs={"invoice_number": "2024-021"}),
            Action(name="record_invoice_audit", kwargs={
                "invoice_number": "2024-021",
                "event_type": "review_follow_up"
            }),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-021"}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-09"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-09-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-09.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-09-30"}),

            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-021", "due_date": "2024-09-15", "invoice_date": "2024-09-15"}],
                "today": "2024-10-01"
            }),
            Action(name="categorize_aging", kwargs={
                "aging": [{"invoice_number": "2024-021", "days_outstanding": 16}]
            }),
        ],
        outputs=[
            "PUB001 AP updated & read; 2024-021 read; audit recorded & listed; AR_Aging_2024-09 exported; snapshot saved & read; 2024-021 aging categorized."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_094",
        instruction=(
            "You validate October‑2024 time tracking for a light billing estimate. End state: "
            "time entries for ['PROJ001','PROJ003'] from '2024-10-01' to '2024-10-31' are fetched and validated; "
            "hours are grouped by ISBN; rates are resolved for ['PROJ001','PROJ003'] and a sample total is computed (5h @85.0 and 3h @75.0); "
            "A/R aging for '2024-10' is exported and a dashboard snapshot is stored for '2024-10-31' using that PDF; "
            "an audit 'reviewed' is recorded for invoice_number '2024-010' and listed."
        ),
        actions=[
            Action(name="fetch_time_entries", kwargs={
                "project_id_list": ["PROJ001", "PROJ003"],
                "period_start": "2024-10-01",
                "period_end": "2024-10-31"
            }),
            Action(name="validate_time_entries", kwargs={"rows": []}),
            Action(name="group_hours_by_isbn", kwargs={"rows": []}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001", "PROJ003"]}),
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 5, "rate": 85.0}, {"hours": 3, "rate": 75.0}],
                "hst_rate": 0.13
            }),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-10-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-10-31"}),

            Action(name="record_invoice_audit", kwargs={
                "invoice_number": "2024-010",
                "event_type": "reviewed"
            }),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "2024-010"}),
        ],
        outputs=[
            "Time entries fetched; validated; grouped; rates resolved; totals computed; AR_Aging_2024-10 exported; snapshot saved & read; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_095",
        instruction=(
            "You assemble and send an October‑2024 invoice for publisher_id 'PUB001'. End state: "
            "invoice_number 'INV-2024-230' exists with invoice_date '2024-10-31', period_start '2024-10-01', period_end '2024-10-31', "
            "subtotal 850.0, hst_amount 110.5, total_due 960.5, pdf_path '/invoices/2024/INV-2024-230.pdf' and is readable; "
            "the invoice is emailed from consultant_id 'CONS001' with subject 'Invoice INV-2024-230' and body_text 'October 2024 invoice attached.' and attachment; "
            "an 'emailed' audit is recorded and listed."
        ),
        actions=[
            Action(name="insert_invoice", kwargs={
                "invoice_number": "INV-2024-230",
                "publisher_id": "PUB001",
                "invoice_date": "2024-10-31",
                "period_start": "2024-10-01",
                "period_end": "2024-10-31",
                "subtotal": 850.0,
                "hst_amount": 110.5,
                "total_due": 960.5,
                "pdf_path": "/invoices/2024/INV-2024-230.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "INV-2024-230"}),

            Action(name="send_invoice_email", kwargs={
                "publisher_id": "PUB001",
                "consultant_id": "CONS001",
                "invoice_number": "INV-2024-230",
                "subject": "Invoice INV-2024-230",
                "body_text": "October 2024 invoice attached.",
                "attachment": "/invoices/2024/INV-2024-230.pdf"
            }),
            Action(name="record_invoice_audit", kwargs={
                "invoice_number": "INV-2024-230",
                "event_type": "emailed"
            }),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "INV-2024-230"}),
            Action(name="get_invoice_details", kwargs={"invoice_number": "INV-2024-230"}),
        ],
        outputs=[
            "Invoice INV-2024-230 inserted & read; emailed; emailed audit recorded & listed; invoice re-read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_096",
        instruction=(
            "You build and email a September‑2024 invoice for publisher_id 'PUB005'. End state: "
            "invoice_number 'INV-2024-361' exists with invoice_date '2024-09-30', period_start '2024-09-01', period_end '2024-09-30', "
            "subtotal 765.0, hst_amount 99.45, total_due 864.45, pdf_path '/invoices/2024/INV-2024-361.pdf' and is readable; "
            "it is emailed from consultant_id 'CONS001' with subject 'Invoice INV-2024-361' and body_text 'September 2024 invoice attached.' and attachment; "
            "an 'emailed' audit is recorded and listed."
        ),
        actions=[
            Action(name="insert_invoice", kwargs={
                "invoice_number": "INV-2024-361",
                "publisher_id": "PUB005",
                "invoice_date": "2024-09-30",
                "period_start": "2024-09-01",
                "period_end": "2024-09-30",
                "subtotal": 765.0,
                "hst_amount": 99.45,
                "total_due": 864.45,
                "pdf_path": "/invoices/2024/INV-2024-361.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "INV-2024-361"}),

            Action(name="send_invoice_email", kwargs={
                "publisher_id": "PUB005",
                "consultant_id": "CONS001",
                "invoice_number": "INV-2024-361",
                "subject": "Invoice INV-2024-361",
                "body_text": "September 2024 invoice attached.",
                "attachment": "/invoices/2024/INV-2024-361.pdf"
            }),
            Action(name="record_invoice_audit", kwargs={
                "invoice_number": "INV-2024-361",
                "event_type": "emailed"
            }),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "INV-2024-361"}),
            Action(name="get_invoice_details", kwargs={"invoice_number": "INV-2024-361"}),
        ],
        outputs=[
            "Invoice INV-2024-361 inserted & read; emailed; emailed audit recorded & listed; invoice re-read."
        ],
    ),  
    Task(
        annotator="A",
        user_id="ca_v4_097",
        instruction=(
            "You update October‑2024 contacts and run KPIs with a quick risk check. End state: "
            "publisher_id 'PUB004' contact_email equals 'ap@bluepeakpublishing.ca' and is readable; "
            "open invoices are reviewed and 12‑month KPIs are available; "
            "A/R aging for '2024-10' is exported and a snapshot stored for '2024-10-31'; "
            "for risk, days outstanding are computed for invoice_number '2024-024' using due_date '2024-10-31' as of '2024-11-05' and categorized."
        ),
        actions=[
            Action(name="update_publisher_contact", kwargs={
                "publisher_id": "PUB004",
                "contact_email": "ap@bluepeakpublishing.ca"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB004"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-10-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-10-31"}),

            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-024", "due_date": "2024-10-31", "invoice_date": "2024-10-31"}],
                "today": "2024-11-05"
            }),
            Action(name="categorize_aging", kwargs={
                "aging": [{"invoice_number": "2024-024", "days_outstanding": 5}]
            }),
        ],
        outputs=[
            "PUB004 AP updated & read; open invoices reviewed; KPIs computed; AR_Aging_2024-10 exported; snapshot saved & read; 2024-024 aging categorized."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_098",
        instruction=(
            "You compose and email an August‑2024 invoice for publisher_id 'PUB003'. End state: "
            "invoice_number 'INV-2024-209' exists with invoice_date '2024-08-31', period_start '2024-08-01', period_end '2024-08-31', "
            "subtotal 875.0, hst_amount 113.75, total_due 988.75, pdf_path '/invoices/2024/INV-2024-209.pdf' and is readable; "
            "the invoice is emailed from consultant_id 'CONS001' with subject 'Invoice INV-2024-209' and body_text 'August 2024 invoice attached.' and attachment; "
            "an 'emailed' audit is recorded and listed."
        ),
        actions=[
            Action(name="insert_invoice", kwargs={
                "invoice_number": "INV-2024-209",
                "publisher_id": "PUB003",
                "invoice_date": "2024-08-31",
                "period_start": "2024-08-01",
                "period_end": "2024-08-31",
                "subtotal": 875.0,
                "hst_amount": 113.75,
                "total_due": 988.75,
                "pdf_path": "/invoices/2024/INV-2024-209.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "INV-2024-209"}),

            Action(name="send_invoice_email", kwargs={
                "publisher_id": "PUB003",
                "consultant_id": "CONS001",
                "invoice_number": "INV-2024-209",
                "subject": "Invoice INV-2024-209",
                "body_text": "August 2024 invoice attached.",
                "attachment": "/invoices/2024/INV-2024-209.pdf"
            }),
            Action(name="record_invoice_audit", kwargs={
                "invoice_number": "INV-2024-209",
                "event_type": "emailed"
            }),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "INV-2024-209"}),
            Action(name="get_invoice_details", kwargs={"invoice_number": "INV-2024-209"}),
        ],
        outputs=[
            "Invoice INV-2024-209 inserted & read; emailed; emailed audit recorded & listed; invoice re-read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_099",
        instruction=(
            "You align a November‑2024 invoice for publisher_id 'PUB001' and confirm delivery. End state: "
            "invoice_number 'INV-2024-231' exists with invoice_date '2024-11-30', period_start '2024-11-01', period_end '2024-11-30', "
            "subtotal 900.0, hst_amount 117.0, total_due 1017.0, pdf_path '/invoices/2024/INV-2024-231.pdf' and is readable; "
            "it is emailed from consultant_id 'CONS001' with subject 'Invoice INV-2024-231' and body_text 'November 2024 invoice attached.' and attachment; "
            "an 'emailed' audit is recorded and listed."
        ),
        actions=[
            Action(name="insert_invoice", kwargs={
                "invoice_number": "INV-2024-231",
                "publisher_id": "PUB001",
                "invoice_date": "2024-11-30",
                "period_start": "2024-11-01",
                "period_end": "2024-11-30",
                "subtotal": 900.0,
                "hst_amount": 117.0,
                "total_due": 1017.0,
                "pdf_path": "/invoices/2024/INV-2024-231.pdf"
            }),
            Action(name="get_invoice_details", kwargs={"invoice_number": "INV-2024-231"}),

            Action(name="send_invoice_email", kwargs={
                "publisher_id": "PUB001",
                "consultant_id": "CONS001",
                "invoice_number": "INV-2024-231",
                "subject": "Invoice INV-2024-231",
                "body_text": "November 2024 invoice attached.",
                "attachment": "/invoices/2024/INV-2024-231.pdf"
            }),
            Action(name="record_invoice_audit", kwargs={
                "invoice_number": "INV-2024-231",
                "event_type": "emailed"
            }),
            Action(name="list_invoice_audit", kwargs={"invoice_number": "INV-2024-231"}),
            Action(name="get_invoice_details", kwargs={"invoice_number": "INV-2024-231"}),
        ],
        outputs=[
            "Invoice INV-2024-231 inserted & read; emailed; emailed audit recorded & listed; invoice re-read."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_100",
        instruction=(
            "You onboard 'Everest Academy' and run an October‑2024 check. End state: "
            "publisher_id 'PUB024' named 'Everest Academy' exists and is readable; "
            "open invoices are reviewed and 12‑month KPIs are available; "
            "rates are resolved for ['PROJ001'] and a sample total is computed (2h @85.0); "
            "A/R aging '2024-10' is exported and a snapshot stored for '2024-10-31'; "
            "for risk, you compute days outstanding for invoice_number '2024-021' using due_date '2024-09-15' as of '2024-10-10' and categorize it."
        ),
        actions=[
            Action(name="create_publisher", kwargs={
                "publisher_id": "PUB024",
                "name": "Everest Academy"
            }),
            Action(name="get_publisher_info", kwargs={"publisher_id": "PUB024"}),

            Action(name="fetch_invoices", kwargs={"status": "open"}),
            Action(name="compute_collection_kpis", kwargs={"window_months": 12}),

            Action(name="resolve_hourly_rates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="calculate_invoice_totals", kwargs={
                "lines": [{"hours": 2, "rate": 85.0}],
                "hst_rate": 0.13
            }),

            Action(name="export_ar_aging_report", kwargs={"period_label": "2024-10"}),
            Action(name="insert_dashboard_snapshot", kwargs={
                "snapshot_date": "2024-10-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"
            }),
            Action(name="get_dashboard_snapshot_details", kwargs={"snapshot_date": "2024-10-31"}),

            Action(name="compute_days_outstanding", kwargs={
                "invoices": [{"invoice_number": "2024-021", "due_date": "2024-09-15", "invoice_date": "2024-09-15"}],
                "today": "2024-10-10"
            }),
            Action(name="categorize_aging", kwargs={
                "aging": [{"invoice_number": "2024-021", "days_outstanding": 25}]
            }),
        ],
        outputs=[
            "PUB024 created & read; open invoices reviewed; KPIs computed; rate resolved; total computed; AR_Aging_2024-10 exported; snapshot saved & read; 2024-021 aging categorized."
        ],
    ),
]