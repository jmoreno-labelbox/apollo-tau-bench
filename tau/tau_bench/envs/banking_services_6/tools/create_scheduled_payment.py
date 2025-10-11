# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
def _get_next_id(table: List[Dict[str, Any]], key: str, prefix: str) -> str:
    if not table:
        return f"{prefix}_00001"
    max_id = 0
    for item in table:
        try:
            num = int(item[key].split('_')[-1])
            if num > max_id:
                max_id = num
        except (ValueError, IndexError):
            continue
    return f"{prefix}_{max_id + 1:05d}"

class GetUserByUpnOrHrId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id=None, actor=None, asset_id=None, asset_type=None, assignment_id=None, body=None, completed_at=None, created_at=None, csv_path=None, current_kpis=None, database_table=None, days=None, department=None, details=None, employee_id=None, end_date=None, event=None, event_type=None, export_path=None, group_ids=None, hr_id=None, input_path=None, issue_type=None, job_title=None, kpi_data_path=None, kpis=None, last_day=None, legal_name=None, license_id=None, license_type=None, lifecycle_id=None, location_uri=None, manager_id=None, memo=None, memo_id=None, metrics=None, metrics_path=None, open_tickets=None, operation=None, output_path=None, pdf_path=None, personal_email=None, pickup_code=None, previous_kpis=None, priority=None, process=None, recipient_group=None, report_date=None, report_path=None, retention_label=None, start_date=None, status=None, subject=None, summary=None, system=None, template_path=None, tickets=None, tickets_with_metrics=None, timestamp=None, timezone=None, upn=None, user_lookup=None, workflow_id=None) -> str:
        user_lookup = user_lookup
        accounts = data.get("directory_accounts", [])
        for acc in accounts:
            if acc.get("hr_id") == user_lookup or acc.get("upn") == user_lookup or acc.get("employee_id") == user_lookup:
                return json.dumps(acc, indent=2)
        return json.dumps({"user_lookup": user_lookup, "account": None}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_user_by_upn_or_hr_id", "description": "Retrieve a user's directory account using their UPN, HR ID, or Employee ID.", "parameters": {"type": "object", "properties": {"user_lookup": {"type": "string"}}, "required": ["user_lookup"]}}}

class CreateDirectoryAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        legal_name = legal_name
        hr_id = hr_id
        accounts = data.get("directory_accounts", [])
        username = legal_name.lower().replace(" ", ".")
        upn = f"{username}@company.com"
        name_part = "".join(filter(str.isalnum, legal_name.split()[0])).lower()
        last_initial = legal_name.split()[-1][0].lower()
        hr_num = hr_id.split('-')[-1]
        account_id = f"acc_{name_part}{last_initial}{hr_num}"
        new_account = {"account_id": account_id, "employee_id": f"emp_{hr_num}", "hr_id": hr_id, "username": username, "upn": upn, "status": "enabled", "created_at": FIXED_NOW, "disabled_at": None}
        accounts.append(new_account)
        return json.dumps(new_account, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_directory_account", "description": "Create a new user account in the directory.", "parameters": {"type": "object", "properties": {"legal_name": {"type": "string"}, "hr_id": {"type": "string"}, "department": {"type": "string"}, "job_title": {"type": "string"}}, "required": ["legal_name", "hr_id", "department", "job_title"]}}}

class SetDirectoryAccountStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        account_id = account_id
        status = status
        accounts = data.get("directory_accounts", [])
        account = next((a for a in accounts if a.get("account_id") == account_id), None)
        if not account:
            return json.dumps({"error": f"Account {account_id} not found."}, indent=2)
        if status not in ["enabled", "disabled", "inactive"]:
            return json.dumps({"error": "Status must be 'enabled', 'disabled', or 'inactive'."}, indent=2)
        account["status"] = status
        account["disabled_at"] = FIXED_NOW if status in ["disabled", "inactive"] else None
        return json.dumps(account, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_directory_account_status", "description": "Enable or disable a user's directory account.", "parameters": {"type": "object", "properties": {"account_id": {"type": "string"}, "status": {"type": "string"}}, "required": ["account_id", "status"]}}}

class LookupRoleProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        department = department
        job_title = job_title
        profiles = data.get("rbac_group_map", [])
        profile = next((p for p in profiles if p.get("department") == department and p.get("job_title") == job_title), None)
        if not profile:
            return json.dumps({"department": department, "job_title": job_title, "profile": None}, indent=2)
        return json.dumps(profile, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "lookup_role_profile", "description": "Look up the role profile for a given department and job title to get group IDs and license bundles.", "parameters": {"type": "object", "properties": {"department": {"type": "string"}, "job_title": {"type": "string"}}, "required": ["department", "job_title"]}}}

class AddUserToGroups(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        account_id = account_id
        group_ids = group_ids
        audit_log = data.setdefault("group_membership_audit", [])
        added_groups = []
        for group_id in group_ids:
            audit_id = _get_next_id(audit_log, "audit_id", "gma")
            audit_log.append({"audit_id": audit_id, "account_id": account_id, "group_id": group_id, "action": "add", "actor": "SYSTEM", "timestamp": FIXED_NOW})
            added_groups.append(group_id)
        return json.dumps({"status": "success", "account_id": account_id, "groups_added": added_groups}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "add_user_to_groups", "description": "Add a user to a list of access groups and log the changes.", "parameters": {"type": "object", "properties": {"account_id": {"type": "string"}, "group_ids": {"type": "array", "items": {"type": "string"}}}, "required": ["account_id", "group_ids"]}}}

class CheckLicenseAvailability(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        license_id = license_id
        inventory = data.get("license_inventory", [])
        license_info = next((lic for lic in inventory if lic.get("license_id") == license_id), None)
        if not license_info:
            return json.dumps({"error": f"License ID {license_id} not found in inventory."}, indent=2)
        available = license_info.get("total_seats", 0) - license_info.get("used_seats", 0)
        return json.dumps({"license_id": license_id, "seats_available": available > 0, "available_count": available}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "check_license_availability", "description": "Check if there are available seats for a given license SKU.", "parameters": {"type": "object", "properties": {"license_id": {"type": "string"}}, "required": ["license_id"]}}}

class AssignLicense(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        account_id = account_id
        employee_id = employee_id
        license_id = license_id
        assignments = data.setdefault("license_assignments", [])
        assignment_id = _get_next_id(assignments, "assignment_id", "lca")
        new_assignment = {"assignment_id": assignment_id, "account_id": account_id, "employee_id": employee_id, "license_id": license_id, "status": "active", "assigned_at": FIXED_NOW}
        assignments.append(new_assignment)
        return json.dumps(new_assignment, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "assign_license", "description": "Assign a single license to a user by creating an assignment record. Does not check availability.", "parameters": {"type": "object", "properties": {"account_id": {"type": "string"}, "employee_id": {"type": "string"}, "license_id": {"type": "string"}}, "required": ["account_id", "employee_id", "license_id"]}}}

class UpdateLicenseInventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        license_id = license_id
        operation = operation
        inventory = data.get("license_inventory", [])
        license_info = next((lic for lic in inventory if lic.get("license_id") == license_id), None)
        if not license_info:
            return json.dumps({"error": f"License ID {license_id} not found in inventory."}, indent=2)
        if operation == "increment":
            license_info["used_seats"] += 1
        elif operation == "decrement":
            license_info["used_seats"] = max(0, license_info.get("used_seats", 0) - 1)
        else:
            return json.dumps({"error": "Operation must be 'increment' or 'decrement'."}, indent=2)
        return json.dumps({"license_id": license_id, "new_used_seats": license_info["used_seats"], "operation": operation}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_license_inventory", "description": "Atomically increment or decrement the used_seats count for a license in inventory.", "parameters": {"type": "object", "properties": {"license_id": {"type": "string"}, "operation": {"type": "string"}}, "required": ["license_id", "operation"]}}}

class FindAvailableAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        asset_type = asset_type
        assets = data.get("it_assets", [])
        asset = next((a for a in assets if a.get("asset_type") == asset_type and a.get("status") == "in_stock"), None)
        if not asset:
            return json.dumps({"asset_type": asset_type, "asset": None}, indent=2)
        return json.dumps(asset, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_available_asset", "description": "Find an available IT asset of a specific type (e.g., 'laptop').", "parameters": {"type": "object", "properties": {"asset_type": {"type": "string"}}, "required": ["asset_type"]}}}

class AssignAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        asset_id = asset_id
        employee_id = employee_id
        assets = data.get("it_assets", [])
        asset = next((a for a in assets if a.get("asset_id") == asset_id), None)
        if not asset:
            return json.dumps({"error": f"Asset {asset_id} not found."}, indent=2)
        asset["assigned_to"] = employee_id
        asset["status"] = "READY FOR PICKUP"
        asset["mdm_enrolled"] = True
        return json.dumps(asset, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "assign_asset", "description": "Assign an IT asset to an employee.", "parameters": {"type": "object", "properties": {"asset_id": {"type": "string"}, "employee_id": {"type": "string"}}, "required": ["asset_id", "employee_id"]}}}

class CreateDeviceWorkflow(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        employee_id = employee_id
        asset_id = asset_id
        process = process
        workflow_id = workflow_id
        status = (status if status is not None else "pending_pickup" if process == "onboarding" else "pending_return")
        pickup_code = pickup_code
        created_at = (created_at if created_at is not None else FIXED_NOW)
        completed_at = completed_at

        workflows = data.setdefault("device_workflow", [])

        if not workflow_id:
            workflow_id = _get_next_id(workflows, "workflow_id", "dwf")
        if not pickup_code and process == "onboarding":
            pickup_code = f"PU{workflow_id[-4:]}"

        return_code = f"RT{workflow_id[-4:]}" if "offboarding" in process else None

        new_workflow = {
            "workflow_id": workflow_id,
            "employee_id": employee_id,
            "asset_id": asset_id,
            "process": process,
            "status": status,
            "pickup_code": pickup_code,
            "return_code": return_code,
            "created_at": created_at,
            "completed_at": completed_at
        }
        workflows.append(new_workflow)
        return json.dumps(new_workflow, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_device_workflow", "description": "Create a device workflow entry for provisioning and pickup or for return.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}, "asset_id": {"type": "string"}, "process": {"type": "string"}}, "required": ["employee_id", "asset_id", "process"]}}}

class CreateJiraTicket(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        issue_type = issue_type
        summary = summary
        priority = (priority if priority is not None else "P2")
        tickets = data.setdefault("jira_tickets", [])
        jira_id = f"ITSD-{1001 + len(tickets)}"
        new_ticket = {"jira_id": jira_id, "issue_type": issue_type, "summary": summary, "priority": priority, "status": "To Do", "created_at": FIXED_NOW, "updated_at": FIXED_NOW}
        tickets.append(new_ticket)
        return json.dumps(new_ticket, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_jira_ticket", "description": "Create a Jira ticket for tracking issues.", "parameters": {"type": "object", "properties": {"issue_type": {"type": "string"}, "summary": {"type": "string"}, "priority": {"type": "string"}}, "required": ["issue_type", "summary"]}}}

class CreateAuditRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        lifecycle_id = lifecycle_id
        event = event
        details = details
        actor = (actor if actor is not None else "SYSTEM")
        timestamp = (timestamp if timestamp is not None else FIXED_NOW)
        audit_table = data.setdefault("lifecycle_audit", [])
        audit_id = _get_next_id(audit_table, "audit_id", "lcaud")
        audit_table.append({"audit_id": audit_id, "lifecycle_id": lifecycle_id, "event": event, "details": details, "timestamp": timestamp, "actor": actor})
        return json.dumps({"status": "success", "event_logged": event}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_audit_record", "description": "Create a deterministic record in the lifecycle audit log.", "parameters": {"type": "object", "properties": {"lifecycle_id": {"type": "string"}, "event": {"type": "string"}, "details": {"type": "object"}, "actor": {"type": "string"}, "timestamp": {"type": "string"}}, "required": ["lifecycle_id", "event", "details", "actor", "timestamp"]}}}

class GetUserLicenseAssignments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        employee_id = employee_id
        assignments = data.get("license_assignments", [])
        user_licenses = [a for a in assignments if a.get("employee_id") == employee_id and a.get("status") == "active"]
        return json.dumps(user_licenses, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_user_license_assignments", "description": "Get a list of all active license assignments for a given employee.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}}, "required": ["employee_id"]}}}

class GetLicenseAssignmentByType(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        employee_id = employee_id
        license_type = license_type
        assignments = data.get("license_assignments", [])
        assignment = next((a for a in assignments if a.get("employee_id") == employee_id and a.get("license_id") == license_type and a.get("status") == "active"), None)
        if not assignment:
            return json.dumps({"error": f"Active assignment for license {license_type} not found for employee {employee_id}."}, indent=2)
        return json.dumps(assignment, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_license_assignment_by_type", "description": "Get a specific active license assignment for a user by license ID.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}, "license_type": {"type": "string"}}, "required": ["employee_id", "license_type"]}}}

class RevokeLicense(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        assignment_id = assignment_id
        assignments = data.get("license_assignments", [])
        assignment = next((a for a in assignments if a.get("assignment_id") == assignment_id), None)
        if not assignment:
            return json.dumps({"error": f"Assignment {assignment_id} not found."}, indent=2)
        assignment["status"] = "revoked"
        assignment["revoked_at"] = FIXED_NOW
        return json.dumps(assignment, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "revoke_license", "description": "Revoke a user's license by updating its status. Does not check inventory.", "parameters": {"type": "object", "properties": {"assignment_id": {"type": "string"}}, "required": ["assignment_id"]}}}

class RemoveUserFromGroups(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        account_id = account_id
        group_ids = group_ids
        audit_log = data.setdefault("group_membership_audit", [])
        removed_groups = []
        for group_id in group_ids:
            audit_id = _get_next_id(audit_log, "audit_id", "gma")
            audit_log.append({"audit_id": audit_id, "account_id": account_id, "group_id": group_id, "action": "remove", "actor": "SYSTEM", "timestamp": FIXED_NOW})
            removed_groups.append(group_id)
        return json.dumps({"status": "success", "account_id": account_id, "groups_removed": removed_groups}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "remove_user_from_groups", "description": "Remove a user from a list of access groups and log the changes.", "parameters": {"type": "object", "properties": {"account_id": {"type": "string"}, "group_ids": {"type": "array", "items": {"type": "string"}}}, "required": ["account_id", "group_ids"]}}}

class ArchiveMailbox(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        employee_id = employee_id
        mailboxes = data.get("mailboxes", [])
        archives = data.setdefault("data_archives", [])
        mailbox = next((m for m in mailboxes if m.get("employee_id") == employee_id), None)
        if not mailbox:
            return json.dumps({"error": f"Mailbox for employee {employee_id} not found."}, indent=2)
        mailbox["status"] = "archived"
        archive_id = f"arch_{mailbox['mailbox_id'].split('_')[-1]}"
        new_archive = {"archive_id": archive_id, "employee_id": employee_id, "mailbox_id": mailbox["mailbox_id"], "archive_path": f"s3://corp-archives/mail/{employee_id}/{FIXED_NOW.split('T')[0]}", "retention_policy": mailbox["retention_policy"], "created_at": FIXED_NOW}
        archives.append(new_archive)
        return json.dumps(new_archive, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "archive_mailbox", "description": "Archives a user's mailbox and creates a data archive record.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}}, "required": ["employee_id"]}}}

class GetUserAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        employee_id = employee_id
        assets = data.get("it_assets", [])
        asset = next((a for a in assets if a.get("assigned_to") == employee_id), None)
        if not asset:
            return json.dumps({"employee_id": employee_id, "asset": None}, indent=2)
        return json.dumps(asset, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_user_asset", "description": "Find an IT asset assigned to a specific employee.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}}, "required": ["employee_id"]}}}

class ExportServiceDeskTickets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        start_date = start_date
        end_date = end_date
        export_path = export_path
        tickets = data.get("tickets", [])
        return json.dumps({"export_path": export_path, "ticket_count": len(tickets), "start_date": start_date, "end_date": end_date}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "export_service_desk_tickets", "description": "Export service desk tickets within a date range to CSV.", "parameters": {"type": "object", "properties": {"start_date": {"type": "string"}, "end_date": {"type": "string"}, "export_path": {"type": "string"}}, "required": ["start_date", "end_date", "export_path"]}}}

class NormalizeTicketTimestamps(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        input_path = input_path
        output_path = output_path
        timezone = (timezone if timezone is not None else "UTC")
        return json.dumps({"status": "normalized", "input_path": input_path, "output_path": output_path, "timezone": timezone}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "normalize_ticket_timestamps", "description": "Normalize ticket timestamps to specified timezone.", "parameters": {"type": "object", "properties": {"input_path": {"type": "string"}, "output_path": {"type": "string"}, "timezone": {"type": "string"}}, "required": ["input_path", "output_path"]}}}

class CalculateServiceDeskKPIs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        input_path = input_path
        metrics = metrics
        output_path = output_path
        kpis = {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}
        return json.dumps({"kpis": kpis, "output_path": output_path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "calculate_service_desk_kpis", "description": "Calculate service desk KPIs from ticket data.", "parameters": {"type": "object", "properties": {"input_path": {"type": "string"}, "metrics": {"type": "array", "items": {"type": "string"}}, "output_path": {"type": "string"}}, "required": ["input_path", "metrics", "output_path"]}}}

class GenerateReportPDF(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        kpi_data_path = kpi_data_path
        template_path = template_path
        output_path = output_path
        return json.dumps({"status": "generated", "output_path": output_path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "generate_report_pdf", "description": "Generate a PDF report from KPI data using a template.", "parameters": {"type": "object", "properties": {"kpi_data_path": {"type": "string"}, "template_path": {"type": "string"}, "output_path": {"type": "string"}}, "required": ["kpi_data_path", "template_path", "output_path"]}}}

class SaveMetricsToDatabase(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        metrics_path = metrics_path
        database_table = database_table
        report_date = report_date
        metrics_db = data.setdefault("daily_metrics", [])
        run_id = f"run_{report_date.replace('-', '')}"
        new_metric = {"run_id": run_id, "report_date": report_date, "database_table": database_table}
        metrics_db.append(new_metric)
        return json.dumps({"status": "success", "run_id": run_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "save_metrics_to_database", "description": "Save calculated metrics to database.", "parameters": {"type": "object", "properties": {"metrics_path": {"type": "string"}, "database_table": {"type": "string"}, "report_date": {"type": "string"}}, "required": ["metrics_path", "database_table", "report_date"]}}}

class NotifyManagementTeam(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        report_path = report_path
        recipient_group = recipient_group
        subject = subject
        return json.dumps({"status": "notified", "recipient_group": recipient_group, "subject": subject}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "notify_management_team", "description": "Send notification to management team with report.", "parameters": {"type": "object", "properties": {"report_path": {"type": "string"}, "recipient_group": {"type": "string"}, "subject": {"type": "string"}}, "required": ["report_path", "recipient_group", "subject"]}}}

class ExportRecentTickets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        days = (days if days is not None else 30)
        tickets = data.get("tickets", [])
        report_path = f"\\\\IT\\Reports\\DailyReports\\{FIXED_NOW.split('T')[0]}\\Tickets_Export.csv"
        return json.dumps({"export_path": report_path, "ticket_count": len(tickets)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "export_recent_tickets", "description": "Exports all tickets updated in the last N days to a CSV file.", "parameters": {"type": "object", "properties": {"days": {"type": "integer"}}, "required": ["days"]}}}

class CalculateTicketKPIs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        export_path = export_path
        if not "Tickets_Export.csv" in export_path:
            return json.dumps({"error": "Invalid export path provided."}, indent=2)
        kpis = {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}
        return json.dumps(kpis, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "calculate_ticket_kpis", "description": "Calculates standard service desk KPIs from a ticket export CSV.", "parameters": {"type": "object", "properties": {"export_path": {"type": "string"}}, "required": ["export_path"]}}}

class GenerateHealthReportPDF(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        kpis = kpis
        if not all(k in kpis for k in ["total_open", "avg_age_open_hours"]):
            return json.dumps({"status": "failed", "reason": "KPI data is incomplete", "missing_fields": [k for k in ["total_open", "avg_age_open_hours"] if k not in kpis]}, indent=2)
        report_path = f"\\\\IT\\Reports\\DailyReports\\{FIXED_NOW.split('T')[0]}\\ServiceDesk_Health_Report.pdf"
        return json.dumps({"report_path": report_path, "status": "generated"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "generate_health_report_pdf", "description": "Generates a PDF health report from calculated KPI data.", "parameters": {"type": "object", "properties": {"kpis": {"type": "object"}}, "required": ["kpis"]}}}

class SaveReportToMetricsDB(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        kpis = kpis
        report_date = FIXED_NOW.split('T')[0]
        metrics_db = data.setdefault("daily_metrics", [])
        run_id = f"run_{report_date.replace('-', '')}"
        new_metric = {"run_id": run_id, "report_date": report_date, **kpis}
        metrics_db.append(new_metric)
        return json.dumps({"status": "success", "run_id": run_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "save_report_to_metrics_db", "description": "Saves the calculated daily KPIs to the historical metrics database.", "parameters": {"type": "object", "properties": {"kpis": {"type": "object"}}, "required": ["kpis"]}}}

class NotifyTeamOfReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        pdf_path = pdf_path
        csv_path = csv_path
        recipient = "it-management-dl@company.com"
        return json.dumps({"status": "notified", "recipient": recipient, "attachments": [pdf_path, csv_path]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "notify_team_of_report", "description": "Sends an email notification with the generated reports as attachments.", "parameters": {"type": "object", "properties": {"pdf_path": {"type": "string"}, "csv_path": {"type": "string"}}, "required": ["pdf_path", "csv_path"]}}}

class ScheduleDeviceReturn(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        employee_id = employee_id
        asset_id = asset_id
        workflows = data.setdefault("device_workflow", [])
        workflow_id = _get_next_id(workflows, "workflow_id", "dwf")
        return_code = f"RT{workflow_id[-4:]}"
        new_workflow = {"workflow_id": workflow_id, "employee_id": employee_id, "asset_id": asset_id, "process": "device_return", "status": "pending_return", "return_code": return_code, "created_at": FIXED_NOW, "completed_at": None}
        workflows.append(new_workflow)
        return json.dumps(new_workflow, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "schedule_device_return", "description": "Schedule device return for an employee.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}, "asset_id": {"type": "string"}}, "required": ["employee_id", "asset_id"]}}}

class ReadOnboardingMemo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        memo_id = memo_id
        memo = next((m for m in data.get("hr_memos", []) if m.get("memo_id") == memo_id and m.get("type") == "onboarding"), None)
        if not memo:
            return json.dumps({"error": f"Onboarding memo {memo_id} not found."}, indent=2)
        return json.dumps(memo, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "read_onboarding_memo", "description": "Reads and returns a specific onboarding memo from the HR memos table.", "parameters": {"type": "object", "properties": {"memo_id": {"type": "string"}}, "required": ["memo_id"]}}}

class ValidateMemoFields(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        memo = memo
        required_fields = ["legal_name", "department", "job_title", "manager_id", "start_date"]
        missing_fields = [field for field in required_fields if field not in memo]
        if missing_fields:
            return json.dumps({"is_valid": False, "missing_fields": missing_fields}, indent=2)
        return json.dumps({"is_valid": True, "missing_fields": []}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "validate_memo_fields", "description": "Validates that a parsed HR memo contains all required fields for onboarding.", "parameters": {"type": "object", "properties": {"memo": {"type": "object"}}, "required": ["memo"]}}}

class CreateMailbox(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        employee_id = employee_id
        upn = upn
        mailboxes = data.setdefault("mailboxes", [])
        mailbox_id = _get_next_id(mailboxes, "mailbox_id", "mbx")
        new_mailbox = {"mailbox_id": mailbox_id, "employee_id": employee_id, "address": upn, "status": "active", "retention_policy": "std_2y", "created_at": FIXED_NOW}
        mailboxes.append(new_mailbox)
        return json.dumps(new_mailbox, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_mailbox", "description": "Creates an Exchange Online mailbox for a new user.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}, "upn": {"type": "string"}}, "required": ["employee_id", "upn"]}}}

class EnrollDeviceInMDM(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        asset_id = asset_id
        asset = next((a for a in data.get("it_assets", []) if a.get("asset_id") == asset_id), None)
        if asset:
            asset["mdm_enrolled"] = True
            return json.dumps({"asset_id": asset_id, "enrollment_status": "success"}, indent=2)
        return json.dumps({"error": f"Asset {asset_id} not found for MDM enrollment."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "enroll_device_in_mdm", "description": "Enrolls a specified IT asset into the Mobile Device Management system.", "parameters": {"type": "object", "properties": {"asset_id": {"type": "string"}}, "required": ["asset_id"]}}}

class SendNewHireWelcomeEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        upn = upn
        personal_email = personal_email
        pickup_code = pickup_code
        return json.dumps({"status": "sent", "recipients": [upn, personal_email], "pickup_code": pickup_code}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "send_new_hire_welcome_email", "description": "Sends a welcome email to the new hire's company and personal addresses with device pickup information.", "parameters": {"type": "object", "properties": {"upn": {"type": "string"}, "personal_email": {"type": "string"}, "pickup_code": {"type": "string"}}, "required": ["upn", "personal_email", "pickup_code"]}}}

class NotifyManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        manager_id = manager_id
        subject = subject
        body = body
        return json.dumps({"status": "sent", "recipient_manager_id": manager_id, "subject": subject}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "notify_manager", "description": "Sends a notification email to a manager for onboarding or offboarding events.", "parameters": {"type": "object", "properties": {"manager_id": {"type": "string"}, "subject": {"type": "string"}, "body": {"type": "string"}}, "required": ["manager_id", "subject", "body"]}}}

class AddMemoToLifecycleQueue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        memo_id = memo_id
        hr_id = hr_id
        event_type = event_type
        queue = data.setdefault("lifecycle_queue", [])
        lifecycle_id = _get_next_id(queue, "lifecycle_id", "lcq")
        new_entry = {"lifecycle_id": lifecycle_id, "memo_id": memo_id, "employee_ref": hr_id, "event": event_type, "status": "queued", "created_at": FIXED_NOW}
        queue.append(new_entry)
        return json.dumps(new_entry, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "add_memo_to_lifecycle_queue", "description": "Adds a new memo to the lifecycle queue to initiate a process like onboarding or offboarding.", "parameters": {"type": "object", "properties": {"memo_id": {"type": "string"}, "hr_id": {"type": "string"}, "event_type": {"type": "string"}}, "required": ["memo_id", "hr_id", "event_type"]}}}

class CalculateTicketMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        tickets = tickets
        calculated_tickets = []
        for ticket in tickets:
            ticket["age_hours"] = 72 # Mock calculation
            ticket["ttr_mins"] = 240 # Mock calculation
            calculated_tickets.append(ticket)
        return json.dumps(calculated_tickets, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "calculate_ticket_metrics", "description": "Calculates metrics like age and time-to-resolution for a list of tickets.", "parameters": {"type": "object", "properties": {"tickets": {"type": "array", "items": {"type": "object"}}}, "required": ["tickets"]}}}

class AggregateTicketKPIs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        tickets_with_metrics = tickets_with_metrics
        kpis = {"open_count": len(tickets_with_metrics), "open_count_p1": 5, "avg_age_open_hours": 72.5, "avg_ttr_mins": 240.0, "pct_closed_1d": 50.0}
        return json.dumps(kpis, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "aggregate_ticket_kpis", "description": "Aggregates final KPIs from a list of tickets with pre-calculated metrics.", "parameters": {"type": "object", "properties": {"tickets_with_metrics": {"type": "array", "items": {"type": "object"}}}, "required": ["tickets_with_metrics"]}}}

class GetUserGroupMemberships(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        account_id = account_id
        account = next((a for a in data.get("directory_accounts", []) if a.get("account_id") == account_id), None)
        if account and "group_ids" in account:
            return json.dumps({"account_id": account_id, "group_ids": account["group_ids"]}, indent=2)
        return json.dumps({"account_id": account_id, "group_ids": []}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_user_group_memberships", "description": "Takes a snapshot of a user's current access groups for auditing.", "parameters": {"type": "object", "properties": {"account_id": {"type": "string"}}, "required": ["account_id"]}}}

class ScheduleDeviceMDMRemoval(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        asset_id = asset_id
        last_day = last_day
        return json.dumps({"asset_id": asset_id, "removal_scheduled_for": last_day, "status": "pending_removal"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "schedule_device_mdm_removal", "description": "Schedules a device for removal from MDM on a specific date.", "parameters": {"type": "object", "properties": {"asset_id": {"type": "string"}, "last_day": {"type": "string"}}, "required": ["asset_id", "last_day"]}}}

class ArchiveUserAppAccounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        employee_id = employee_id
        app_accounts = data.get("app_accounts", [])
        archived_count = 0
        for acc in app_accounts:
            if acc.get("employee_id") == employee_id:
                acc["status"] = "archived"
                archived_count += 1
        return json.dumps({"employee_id": employee_id, "app_accounts_archived": archived_count}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "archive_user_app_accounts", "description": "Archives a user's accounts in integrated applications like Slack or GitHub.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}}, "required": ["employee_id"]}}}

class UpdateLifecycleQueueStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        lifecycle_id = lifecycle_id
        status = status
        queue = data.get("lifecycle_queue", [])
        entry = next((e for e in queue if e.get("lifecycle_id") == lifecycle_id), None)
        if not entry:
            return json.dumps({"error": f"Lifecycle entry {lifecycle_id} not found."}, indent=2)
        entry["status"] = status
        return json.dumps(entry, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_lifecycle_queue_status", "description": "Updates the status of an event in the lifecycle queue (e.g., to 'completed').", "parameters": {"type": "object", "properties": {"lifecycle_id": {"type": "string"}, "status": {"type": "string"}}, "required": ["lifecycle_id", "status"]}}}

class ReadOffboardingMemo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        memo_id = memo_id
        memo = next((m for m in data.get("hr_memos", []) if m.get("memo_id") == memo_id and m.get("type") == "offboarding"), None)
        if not memo:
            return json.dumps({"error": f"Offboarding memo {memo_id} not found."}, indent=2)
        return json.dumps(memo, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "read_offboarding_memo", "description": "Reads and returns a specific offboarding memo from the HR memos table.", "parameters": {"type": "object", "properties": {"memo_id": {"type": "string"}}, "required": ["memo_id"]}}}

class CreateDataArchiveEntry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        employee_id = employee_id
        system = system
        retention_label = retention_label
        location_uri = location_uri
        archives = data.setdefault("data_archives", [])
        archive_id = _get_next_id(archives, "archive_id", "arch")
        new_archive = {"archive_id": archive_id, "employee_id": employee_id, "system": system, "location_uri": location_uri, "retention_label": retention_label, "created_at": FIXED_NOW}
        archives.append(new_archive)
        return json.dumps(new_archive, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_data_archive_entry", "description": "Creates an entry in the data archives table, typically after a mailbox export.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}, "system": {"type": "string"}, "retention_label": {"type": "string"}, "location_uri": {"type": "string"}}, "required": ["employee_id", "system", "retention_label", "location_uri"]}}}

class FilterOpenTickets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        tickets = data.get("tickets", [])
        open_statuses = ["New", "In Progress", "On Hold", "Open"]
        open_tickets = [t for t in tickets if t.get("status") in open_statuses]
        return json.dumps(open_tickets, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "filter_open_tickets", "description": "Filters a list of tickets to return only those that are not resolved or closed.", "parameters": {"type": "object", "properties": {}, "required": []}}}

class BuildOpenTicketsCSV(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        open_tickets = open_tickets
        file_path = f"\\\\IT\\Reports\\DailyReports\\{FIXED_NOW.split('T')[0]}\\Open_Tickets.csv"
        return json.dumps({"file_path": file_path, "rows_written": len(open_tickets)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "build_open_tickets_csv", "description": "Builds and saves the Open_Tickets.csv file from a list of open tickets.", "parameters": {"type": "object", "properties": {"open_tickets": {"type": "array", "items": {"type": "object"}}}, "required": ["open_tickets"]}}}

class UnassignAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        asset_id = asset_id
        assets = data.get("it_assets", [])
        asset = next((a for a in assets if a.get("asset_id") == asset_id), None)
        if not asset:
            return json.dumps({"error": f"Asset {asset_id} not found."}, indent=2)
        asset["assigned_to"] = None
        asset["status"] = "in_stock"
        return json.dumps(asset, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "unassign_asset", "description": "Unassigns an IT asset from an employee and returns it to stock.", "parameters": {"type": "object", "properties": {"asset_id": {"type": "string"}}, "required": ["asset_id"]}}}

class GetLastReportRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        report_runs = data.get("report_runs", [])
        if not report_runs:
            return json.dumps({"error": "No previous report runs found."}, indent=2)
        last_run = report_runs[-1]
        # Mocking the KPIs that would have been stored with the run
        last_run["kpis"] = {"total_open": 45, "avg_age_open_hours": 22.0, "avg_ttr_mins": 1300, "pct_closed_1d": 65.0, "p1_open_count": 4}
        return json.dumps(last_run, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_last_report_run", "description": "Retrieves the data from the last successful service desk health report run.", "parameters": {"type": "object", "properties": {}, "required": []}}}

class CompareTicketKPIs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        current_kpis = current_kpis
        previous_kpis = previous_kpis
        delta = {
            "total_open_delta": current_kpis.get("total_open", 0) - previous_kpis.get("total_open", 0),
            "p1_open_delta": current_kpis.get("p1_open_count", 0) - previous_kpis.get("p1_open_count", 0)
        }
        analysis_summary = f"KPI comparison complete. Open tickets changed by {delta['total_open_delta']}. P1 tickets changed by {delta['p1_open_delta']}."
        return json.dumps({"analysis_summary": analysis_summary, "delta": delta}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "compare_ticket_kpis", "description": "Compares two sets of ticket KPIs to find the delta.", "parameters": {"type": "object", "properties": {"current_kpis": {"type": "object"}, "previous_kpis": {"type": "object"}}, "required": ["current_kpis", "previous_kpis"]}}}

def _get_next_scheduled_payment_id(data: Dict[str, Any]) -> str:
    payment_ids = [p['payment_id'] for p in data.get('scheduled_payments', [])]
    return _get_next_id('sp', payment_ids)

class CreateScheduledPayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], amount, beneficiary_id, customer_id, frequency, source_account_id, start_date) -> str:
        payment_id = _get_next_scheduled_payment_id(data)
        new_payment = {
                "payment_id": payment_id,
                "customer_id": customer_id,
                "source_account_id": source_account_id,
                "beneficiary_id": beneficiary_id,
                "amount": amount,
                "currency": next((a['currency'] for a in data['accounts'] if a['account_id'] == source_account_id), "EUR"),
                "frequency": frequency,
                "start_date": start_date,
                "next_payment_date": start_date,
                "status": "Active"
        }
        data['scheduled_payments'].append(new_payment)
        return json.dumps(new_payment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_scheduled_payment",
                        "description": "Schedules a new recurring payment.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"}, "source_account_id": {"type": "string"},
                                        "beneficiary_id": {"type": "string"}, "amount": {"type": "number"}, "frequency": {"type": "string"}, "start_date": {"type": "string"}
                                },
                                "required": ["customer_id", "source_account_id", "beneficiary_id", "amount", "frequency", "start_date"]
                        }
                }
        }