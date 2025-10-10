from domains.dto import Tool
from typing import Any, Dict, List, Optional, Tuple
import json
import re
from datetime import datetime, timedelta

# A hardcoded timestamp for deterministic "now"
HARD_TS = "2024-08-15T12:00:00Z"

# ----------------------------
# Helpers
# ----------------------------
def _err(msg: str, code: str = "bad_request", **extra) -> str:
    """Creates a JSON error message."""
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

def _as_int(x: Any) -> Optional[int]:
    """Safely converts a value to an integer."""
    try:
        return int(x)
    except (ValueError, TypeError):
        return None

def _days_between(d1_str: str, d2_str: str) -> int:
    """A deterministic way to calculate days between two ISO date strings."""
    try:
        # Assumes ISO format with 'Z' for UTC
        d1 = datetime.fromisoformat(d1_str.replace("Z", "+00:00"))
        d2 = datetime.fromisoformat(d2_str.replace("Z", "+00:00"))
        return abs((d2 - d1).days)
    except (ValueError, TypeError):
        return 9999  # Return a large number for invalid formats

def _render_template(template_content: str, context: Dict[str, Any]) -> str:
    """Performs simple string replacement on a template."""
    for key, value in context.items():
        template_content = template_content.replace(f"{{{{{key}}}}}", str(value))
    return template_content

def _get_email_template(data: Dict[str, Any], template_name: str) -> Optional[Dict[str, str]]:
    """Retrieves and parses an email template from onboarding_files."""
    files = data.get("onboarding_files", [])
    # Assume a convention for template paths, e.g., /templates/emails/welcome.json
    template_path = f"/templates/emails/{template_name}.json"
    template_file = next((f for f in files if f.get("file_path") == template_path), None)

    if not template_file:
        return None

    try:
        return json.loads(template_file.get("content_text", "{}"))
    except json.JSONDecodeError:
        return None

def _get_markdown_template(data: Dict[str, Any], template_name: str) -> Optional[Dict[str, str]]:
    """Retrieves and parses a markdown email template from onboarding_files."""
    files = data.get("onboarding_files", [])
    # Correct path for markdown templates
    template_path = f"/onboarding/templates/{template_name}.md"
    template_file = next((f for f in files if f.get("file_path") == template_path), None)

    if not template_file:
        return None

    content = template_file.get("content_text", "")
    if not content:
        return {"subject": "", "body": ""}

    # Assume first line is subject, rest is body
    lines = content.splitlines()
    subject = lines[0].strip()
    body = "\n".join(lines[1:]).strip()
    return {"subject": subject, "body": body}

def _generate_new_thread_id(emails: List[Dict[str, Any]]) -> str:
    """Generates a new sequential thread ID."""
    max_id = 0
    for email in emails:
        thread_id = email.get("thread_id_nullable")
        if thread_id and thread_id.startswith("thread_"):
            try:
                num_part = int(thread_id.split('_')[1])
                if num_part > max_id:
                    max_id = num_part
            except (ValueError, IndexError):
                continue
    return f"thread_{max_id + 1}"

def _next_str_id(rows: List[Dict[str, Any]], key: str, prefix: str) -> str:
    """Generates the next string ID in a sequence (e.g., CAND-001)."""
    if not rows:
        return f"{prefix}1"

    max_id = 0
    for r in rows:
        id_val = r.get(key)
        if id_val and isinstance(id_val, str) and id_val.startswith(prefix):
            try:
                num_part = int(id_val[len(prefix):])
                if num_part > max_id:
                    max_id = num_part
            except ValueError:
                continue

    return f"{prefix}{max_id + 1:03d}"

def _get_hardcoded_template_and_render(template_name: str, context: Dict[str, Any]) -> Dict[str, str]:
    """
    Retrieves a hardcoded template by name and renders it with the given context.
    """
    templates = {
        "welcome": {
            "subject": "Welcome to the Team, {{candidate_name}}!",
            "body": "Dear {{candidate_name}},\n\nWelcome to our team! We're thrilled to have you join us as our new {{role_title}} starting {{start_date}}.\n\nAttached you'll find your personalized welcome packet.\n\nPlease review these documents before your first day. If you have any questions, don't hesitate to reach out.\n\nBest regards,\nHR Team"
        },
        "asset_request_notification": {
            "subject": "Asset Provisioning Request - {{candidate_name}}",
            "body": "A new asset request has been submitted for {{candidate_name}}.\n\nUrgency: {{urgency_level}}\nSpecifications: {{specifications}}\n\nPlease review and process this request."
        },
        "overdue_task_reminder": {
            "subject": "Onboarding Reminder for {{name}}",
            "body": "Hi {{name}},\n\nThis is a friendly reminder to complete the following overdue onboarding tasks:\n\n{{tasks}}\n\nThanks,\nHR Team"
        },
        "orientation_invitation": {
            "subject": "Orientation Invitation for {{candidate_name}}",
            "body": "Hi {{candidate_name}},\n\nPlease join us for your new hire orientation at {{meeting_time}} in {{meeting_location}}.\n\nWe look forward to seeing you there!"
        },
        "manager_introduction": {
            "subject": "Introduction: {{candidate_name}}",
            "body": "Hi {{manager_email_nullable}},\n\nThis is an introduction to your new team member, {{candidate_name}}, who will be starting on {{start_date}}.\n\nBest regards,\nHR Team"
        },
        "it_support_request": {
            "subject": "URGENT: System Access Failure for {{candidate_name}}",
            "body": "Hi IT Support,\n\nPlease investigate and resolve the following system access failures for candidate {{candidate_name}} ({{candidate_email}}):\n\n{{failure_notes}}\n\nThank you,\nHR Onboarding"
        },
        "manager_access_issue_notification": {
            "subject": "Action Required: System Access Issues for {{candidate_name}}",
            "body": "Hi {{manager_name}},\n\nThis is an alert that your new hire, {{candidate_name}}, is experiencing system access issues that may delay their onboarding. Our IT team has been notified.\n\nThanks,\nHR Onboarding"
        },
        "manager_overdue_escalation": {
            "subject": "Escalation: Overdue Onboarding Tasks for {{candidate_name}}",
            "body": "Hi {{manager_name}},\n\nThis is an escalation regarding overdue onboarding tasks for your new hire, {{candidate_name}}. Please follow up with them to ensure their onboarding stays on track.\n\nThanks,\nHR Onboarding"
        }
    }

    template = templates.get(template_name)
    if not template:
        return {"subject": "", "body": ""} # Return empty strings if template not found

    subject = _render_template(template["subject"], context)
    body = _render_template(template["body"], context)

    return {"subject": subject, "body": body}

# ============================================================
# Centralized Role-Based Configurations
# ============================================================

ROLE_SYSTEMS_MAP = {
    "Software Engineer": ["GitHub", "VPN", "AWS Console"],
    "Data Scientist": ["VPN", "AWS Console"],
    "Product Manager": ["GitHub"],
    "Data Analyst": ["VPN", "AWS Console"],
    "UX Designer": ["GitHub"],
    "Marketing Specialist": [],
    "Junior Product Manager": ["GitHub"],
    "Senior Software Engineer": ["GitHub", "VPN", "AWS Console"],
    "UI designer": [],
    "SEO specialist": [],
    "Marketing Specialist": ["VPN", "AWS Console"],
    "DevOps Engineer": ["GitHub", "VPN", "AWS Console", "Kubernetes"],
    "Sales Representative": ["CRM", "VPN"],
    "HR Specialist": ["HRIS", "VPN"],
    "Financial Analyst": ["VPN", "Financial Systems"],
    "Content Writer": ["CMS", "VPN"],
    "Customer Success Manager": ["CRM", "Support Tools"],
    "QA Engineer": ["GitHub", "Testing Tools", "VPN"],
    "Business Analyst": ["VPN", "Analytics Tools"],
    "Graphic Designer": ["Adobe Creative Suite"],
    "Project Manager": ["Project Management Tools", "VPN"],
}

ROLE_CHECKLIST_MAP = {
    "Software Engineer": [
        {"task_name": "Setup developer environment", "due_days": 2},
        {"task_name": "Complete security training", "due_days": 5},
        {"task_name": "Review team codebase", "due_days": 10},
    ],
    "Product Manager": [
        {"task_name": "Meet with key stakeholders", "due_days": 5},
        {"task_name": "Review product roadmap", "due_days": 7},
    ],
    "Data Analyst": [
        {"task_name": "Access data warehouse", "due_days": 2},
        {"task_name": "Review existing dashboards", "due_days": 5},
    ],
    "UX Designer": [
        {"task_name": "Get access to Figma", "due_days": 1},
        {"task_name": "Review design system", "due_days": 3},
    ],
    "Data Scientist": [
        {"task_name": "Setup data science environment", "due_days": 3},
        {"task_name": "Review data governance policies", "due_days": 7},
    ],
    "Marketing Specialist": [
        {"task_name": "Review marketing campaigns", "due_days": 5},
        {"task_name": "Setup marketing tools access", "due_days": 3},
    ],
    "Junior Product Manager": [
        {"task_name": "Shadow senior PM meetings", "due_days": 3},
        {"task_name": "Review product documentation", "due_days": 5},
    ],
    "Senior Software Engineer": [
        {"task_name": "Setup senior developer environment", "due_days": 2},
        {"task_name": "Review architecture documentation", "due_days": 7},
        {"task_name": "Meet with engineering leadership", "due_days": 5},
    ],
    "UI designer": [
        {"task_name": "Setup design tools", "due_days": 1},
        {"task_name": "Review UI guidelines", "due_days": 3},
    ],
    "SEO specialist": [
        {"task_name": "Setup SEO tools access", "due_days": 2},
        {"task_name": "Review current SEO strategy", "due_days": 5},
    ],
    "DevOps Engineer": [
        {"task_name": "Setup infrastructure access", "due_days": 1},
        {"task_name": "Review deployment pipelines", "due_days": 3},
        {"task_name": "Complete security clearance", "due_days": 7},
    ],
    "Sales Representative": [
        {"task_name": "Complete sales training", "due_days": 5},
        {"task_name": "Shadow experienced sales calls", "due_days": 7},
        {"task_name": "Learn CRM system", "due_days": 3},
    ],
    "HR Specialist": [
        {"task_name": "Review HR policies", "due_days": 3},
        {"task_name": "Complete compliance training", "due_days": 5},
        {"task_name": "Setup HRIS access", "due_days": 2},
    ],
    "Financial Analyst": [
        {"task_name": "Access financial systems", "due_days": 2},
        {"task_name": "Review financial processes", "due_days": 5},
        {"task_name": "Meet with finance team", "due_days": 3},
    ],
    "Content Writer": [
        {"task_name": "Review brand guidelines", "due_days": 2},
        {"task_name": "Setup content management system", "due_days": 1},
        {"task_name": "Review existing content strategy", "due_days": 5},
    ],
    "Customer Success Manager": [
        {"task_name": "Learn customer onboarding process", "due_days": 5},
        {"task_name": "Shadow customer calls", "due_days": 7},
        {"task_name": "Setup customer support tools", "due_days": 2},
    ],
    "QA Engineer": [
        {"task_name": "Setup testing environment", "due_days": 2},
        {"task_name": "Review testing procedures", "due_days": 5},
        {"task_name": "Learn automation tools", "due_days": 7},
    ],
    "Business Analyst": [
        {"task_name": "Review business requirements", "due_days": 5},
        {"task_name": "Meet with stakeholders", "due_days": 7},
        {"task_name": "Setup analytics tools", "due_days": 3},
    ],
    "Graphic Designer": [
        {"task_name": "Setup design software", "due_days": 1},
        {"task_name": "Review brand guidelines", "due_days": 2},
        {"task_name": "Meet with creative team", "due_days": 3},
    ],
    "Project Manager": [
        {"task_name": "Review project methodologies", "due_days": 3},
        {"task_name": "Setup project management tools", "due_days": 2},
        {"task_name": "Meet with project teams", "due_days": 5},
    ],
}

ROLE_ASSET_DEFAULTS_MAP = {
    "Software Engineer": {
        "asset_type": "Laptop",
        "urgency_level": "High",
        "specifications": "MacBook Pro 16-inch, 32GB RAM",
    },
    "Data Scientist": {
        "asset_type": "Laptop",
        "urgency_level": "High",
        "specifications": "High-performance laptop, 32GB RAM, 1TB SSD",
    },
    "Default": {
        "asset_type": "Standard Laptop",
        "urgency_level": "Medium",
        "specifications": "Standard issue laptop, 16GB RAM",
    },
}

# ============================================================
# 1. get_candidate_with_full_context
# ============================================================
class GetCandidateWithFullContextTool(Tool):
    """Retrieves candidate record with all linked emails, asset requests, checklist items, and access checks for comprehensive view."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        if not candidate_id:
            return _err("candidate_id is required")

        candidates = data.get("candidates", [])
        candidate = next((c for c in candidates if str(c.get("candidate_id")) == str(candidate_id)), None)

        if not candidate:
            return _err(f"Candidate with id '{candidate_id}' not found", code="not_found")

        result = {
            "candidate": candidate,
            "emails": [e for e in data.get("emails", []) if str(e.get("candidate_id_nullable")) == str(candidate_id)],
            "asset_requests": [ar for ar in data.get("asset_requests", []) if str(ar.get("candidate_id")) == str(candidate_id)],
            "checklist_items": [ci for ci in data.get("checklist_items", []) if str(ci.get("candidate_id")) == str(candidate_id)],
            "access_checks": [ac for ac in data.get("access_checks", []) if str(ac.get("candidate_id")) == str(candidate_id)],
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_candidate_with_full_context",
                "description": "Retrieves candidate record with all linked emails, asset requests, checklist items, and access checks for comprehensive view.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "Target candidate identifier"}
                    },
                    "required": ["candidate_id"],
                },
            },
        }

# ============================================================
# 2. find_candidates_by_onboarding_status
# ============================================================
class FindCandidatesByOnboardingStatusTool(Tool):
    """Queries candidates table filtering by status, optionally including date ranges and related record counts."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("onboarding_status")
        start_date_after = kwargs.get("start_date_after")
        include_counts = kwargs.get("include_record_counts", False)

        if not status:
            return _err("onboarding_status is required")

        valid_statuses = {"Started", "Packet Sent", "Access Issues", "Asset Pending", "Onboarded"}
        if status not in valid_statuses:
            return _err(f"Invalid onboarding_status '{status}'. Valid statuses are: {sorted(list(valid_statuses))}")

        candidates = data.get("candidates", [])

        # Filter by status
        filtered_candidates = [c for c in candidates if c.get("onboarding_status") == status]

        # Filter by start date
        if start_date_after:
            try:
                # Validate date format
                datetime.fromisoformat(start_date_after)
                filtered_candidates = [c for c in filtered_candidates if (c.get("start_date") or "0000-00-00") > start_date_after]
            except ValueError:
                return _err("Invalid start_date_after format. Please use YYYY-MM-DD.")

        results = []
        for candidate in filtered_candidates:
            candidate_id = candidate.get("candidate_id")
            if not candidate_id:
                continue

            result_candidate = candidate.copy()
            if include_counts:
                cid_str = str(candidate_id)
                result_candidate["record_counts"] = {
                    "emails": len([e for e in data.get("emails", []) if str(e.get("candidate_id_nullable")) == cid_str]),
                    "asset_requests": len([ar for ar in data.get("asset_requests", []) if str(ar.get("candidate_id")) == cid_str]),
                    "checklist_items": len([ci for ci in data.get("checklist_items", []) if str(ci.get("candidate_id")) == cid_str]),
                    "access_checks": len([ac for ac in data.get("access_checks", []) if str(ac.get("candidate_id")) == cid_str]),
                }
            results.append(result_candidate)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_candidates_by_onboarding_status",
                "description": "Queries candidates table filtering by status, optionally including date ranges and related record counts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "onboarding_status": {
                            "type": "string",
                            "description": "Status to filter ('Started', 'Packet Sent', 'Access Issues', 'Asset Pending', 'Onboarded')"
                        },
                        "start_date_after": {
                            "type": "string",
                            "description": "Filter candidates starting after date (YYYY-MM-DD)"
                        },
                        "include_record_counts": {
                            "type": "boolean",
                            "description": "Include counts of related emails/tasks/assets"
                        }
                    },
                    "required": ["onboarding_status"],
                },
            },
        }

# ============================================================
# 3. get_overdue_checklist_items
# ============================================================
class GetOverdueChecklistItemsTool(Tool):
    """Queries checklist_items for tasks past due date, grouped by candidate and task priority."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        days_overdue_threshold = _as_int(kwargs.get("days_overdue_threshold", 0))

        if days_overdue_threshold is None:
            return _err("days_overdue_threshold must be an integer.")

        checklist_items = data.get("checklist_items", [])

        overdue_items = []
        for item in checklist_items:
            due_date = item.get("due_date")
            if not due_date or item.get("status") == "Completed":
                continue

            days_overdue = _days_between(due_date, HARD_TS)

            if days_overdue >= days_overdue_threshold:
                if candidate_id is None or str(item.get("candidate_id")) == str(candidate_id):
                    item_copy = item.copy()
                    item_copy["days_overdue"] = days_overdue
                    overdue_items.append(item_copy)

        # Group by candidate
        grouped_results = {}
        for item in overdue_items:
            cid = item.get("candidate_id")
            if cid not in grouped_results:
                grouped_results[cid] = []
            grouped_results[cid].append(item)

        return json.dumps(grouped_results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_overdue_checklist_items",
                "description": "Queries checklist_items for tasks past due date, grouped by candidate and task priority.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "Specific candidate or null for all candidates"},
                        "days_overdue_threshold": {"type": "integer", "description": "Minimum days past due date"}
                    },
                    "required": ["days_overdue_threshold"],
                },
            },
        }

# ============================================================
# 4. check_email_communication_gaps
# ============================================================
class CheckEmailCommunicationGapsTool(Tool):
    """Analyzes emails table to identify candidates missing expected communications (welcome, orientation, reminders)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        expected_email_types = kwargs.get("expected_email_types")

        if not expected_email_types or not isinstance(expected_email_types, list):
            return _err("expected_email_types (array) is required")

        candidates_to_check = []
        if candidate_id:
            candidate = next((c for c in data.get("candidates", []) if str(c.get("candidate_id")) == str(candidate_id)), None)
            if not candidate:
                return _err(f"Candidate '{candidate_id}' not found", code="not_found")
            candidates_to_check.append(candidate)
        else:
            candidates_to_check = data.get("candidates", [])

        emails = data.get("emails", [])
        results = []
        for candidate in candidates_to_check:
            cid = str(candidate.get("candidate_id"))
            candidate_emails = [e for e in emails if str(e.get("candidate_id_nullable")) == cid]

            sent_email_subjects = [str(e.get("subject", "")).lower() for e in candidate_emails]

            missing_types = []
            for email_type in expected_email_types:
                if not any(email_type.lower().replace("_", " ") in subject for subject in sent_email_subjects):
                    missing_types.append(email_type)

            if missing_types:
                results.append({
                    "candidate_id": cid,
                    "candidate_name": candidate.get("candidate_name"),
                    "missing_email_types": missing_types
                })

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_email_communication_gaps",
                "description": "Analyzes emails table to identify candidates missing expected communications (welcome, orientation, reminders).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "Specific candidate or null for all"},
                        "expected_email_types": {"type": "array", "items": {"type": "string"}, "description": "Email types to verify presence of"}
                    },
                    "required": ["expected_email_types"],
                },
            },
        }

# ============================================================
# 5. query_available_assets_by_type
# ============================================================
class QueryAvailableAssetsByTypeTool(Tool):
    """Searches inventory_assets table for available assets matching specifications, with assignment status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_type = kwargs.get("asset_type")
        status_filter = kwargs.get("status_filter")

        if not asset_type:
            return _err("asset_type is required")
        if not status_filter:
            return _err("status_filter is required")

        valid_statuses = {"Available", "Reserved", "Assigned", "In Repair"}
        if status_filter not in valid_statuses:
            return _err(f"Invalid status_filter. Valid statuses are: {sorted(list(valid_statuses))}")

        assets = data.get("inventory_assets", [])

        matching_assets = [
            asset for asset in assets
            if asset.get("asset_type") == asset_type and asset.get("status") == status_filter
        ]

        return json.dumps(matching_assets, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "query_available_assets_by_type",
                "description": "Searches inventory_assets table for available assets matching specifications, with assignment status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_type": {"type": "string", "description": "Equipment type needed ('Laptop', 'Phone', 'Monitor', etc.)"},
                        "status_filter": {"type": "string", "description": "Asset status ('Available', 'Reserved', 'Assigned', 'In Repair')"}
                    },
                    "required": ["asset_type", "status_filter"],
                },
            },
        }

# ============================================================
# 6. get_pending_asset_requests
# ============================================================
class GetPendingAssetRequestsTool(Tool):
    """Retrieves asset_requests with status analysis and linked candidate information for fulfillment planning."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status_filter = kwargs.get("status_filter")
        role_filter = kwargs.get("candidate_role_filter")

        asset_requests = data.get("asset_requests", [])

        # Apply status filter
        if status_filter:
            valid_statuses = {"Pending", "Sent", "Reserved", "Completed"}
            if status_filter not in valid_statuses:
                 return _err(f"Invalid status_filter. Valid statuses are: {sorted(list(valid_statuses))}")
            asset_requests = [r for r in asset_requests if r.get("status") == status_filter]

        results = []
        candidates_map = {str(c.get("candidate_id")): c for c in data.get("candidates", [])}

        for request in asset_requests:
            candidate_id = str(request.get("candidate_id"))
            candidate = candidates_map.get(candidate_id)

            if not candidate:
                continue

            # Apply role filter
            if role_filter and candidate.get("role_title") != role_filter:
                continue

            request_copy = request.copy()
            request_copy["candidate"] = {
                "candidate_id": candidate_id,
                "candidate_name": candidate.get("candidate_name"),
                "role_title": candidate.get("role_title"),
                "start_date": candidate.get("start_date")
            }
            results.append(request_copy)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pending_asset_requests",
                "description": "Retrieves asset_requests with status analysis and linked candidate information for fulfillment planning.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status_filter": {"type": "string", "description": "Request status ('Pending', 'Sent', 'Reserved', 'Completed')"},
                        "candidate_role_filter": {"type": "string", "description": "Filter by candidate role"}
                    },
                    "required": [],
                },
            },
        }

# ============================================================
# 7. analyze_system_access_failures
# ============================================================
class AnalyzeSystemAccessFailuresTool(Tool):
    """Queries access_checks table for failed verifications, grouped by system and failure patterns."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        system_name = kwargs.get("system_name")

        access_checks = data.get("access_checks", [])

        failures = [check for check in access_checks if check.get("status") == "Failed"]

        if candidate_id:
            failures = [f for f in failures if str(f.get("candidate_id")) == str(candidate_id)]

        if system_name:
            failures = [f for f in failures if f.get("system_name") == system_name]

        # Group by system
        analysis = {}
        for f in failures:
            sys_name = f.get("system_name")
            if sys_name not in analysis:
                analysis[sys_name] = {
                    "total_failures": 0,
                    "candidates_affected": set(),
                    "failure_notes": []
                }

            analysis[sys_name]["total_failures"] += 1
            analysis[sys_name]["candidates_affected"].add(f.get("candidate_id"))
            if f.get("note_nullable"):
                analysis[sys_name]["failure_notes"].append(f.get("note_nullable"))

        # Convert set to list for JSON serialization
        for sys_name in analysis:
            analysis[sys_name]["candidates_affected"] = list(analysis[sys_name]["candidates_affected"])
            analysis[sys_name]["affected_candidate_count"] = len(analysis[sys_name]["candidates_affected"])

        return json.dumps(analysis, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyze_system_access_failures",
                "description": "Queries access_checks table for failed verifications, grouped by system and failure patterns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "Specific candidate or null for system-wide analysis"},
                        "system_name": {"type": "string", "description": "Specific system to analyze"}
                    },
                    "required": [],
                },
            },
        }

# ============================================================
# 8. get_draft_emails_requiring_action
# ============================================================
class GetDraftEmailsRequiringActionTool(Tool):
    """Queries emails table for draft messages that need completion and sending, with aging analysis."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        draft_age_days = _as_int(kwargs.get("draft_age_days"))
        candidate_filter = kwargs.get("candidate_filter")

        if draft_age_days is None:
            return _err("draft_age_days (integer) is required")

        emails = data.get("emails", [])
        drafts = [e for e in emails if e.get("draft_flag") == True]

        results = []
        for draft in drafts:
            created_at = draft.get("date_ts")
            if not created_at:
                continue

            age = _days_between(created_at, HARD_TS)
            if age >= draft_age_days:
                if candidate_filter is None or str(draft.get("candidate_id_nullable")) == str(candidate_filter):
                    draft_copy = draft.copy()
                    draft_copy["age_days"] = age
                    results.append(draft_copy)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_draft_emails_requiring_action",
                "description": "Queries emails table for draft messages that need completion and sending, with aging analysis.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "draft_age_days": {"type": "integer", "description": "Minimum age of drafts to include"},
                        "candidate_filter": {"type": "string", "description": "Filter to specific candidate"}
                    },
                    "required": ["draft_age_days"],
                },
            },
        }

# ============================================================
# 9. find_template_files_by_type
# ============================================================
class FindTemplateFilesByTypeTool(Tool):
    """Searches onboarding_files table for available templates, filtering by content type and last update."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        template_category = kwargs.get("template_category")
        mime_type = kwargs.get("mime_type")

        if not template_category:
            return _err("template_category is required")

        files = data.get("onboarding_files", [])

        # Templates are identified by their path.
        templates = [
            f for f in files
            if f"/templates/{template_category}/" in f.get("file_path", "")
        ]

        if mime_type:
            templates = [t for t in templates if t.get("mime_type") == mime_type]

        return json.dumps(templates, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_template_files_by_type",
                "description": "Searches onboarding_files table for available templates, filtering by content type and last update.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "template_category": {"type": "string", "description": "Template type needed ('welcome', 'asset_request', 'reminder')"},
                        "mime_type": {"type": "string", "description": "File format filter"}
                    },
                    "required": ["template_category"],
                },
            },
        }

# ============================================================
# 10. get_candidates_needing_orientation_scheduling
# ============================================================
class GetCandidatesNeedingOrientationSchedulingTool(Tool):
    """Identifies candidates ready for orientation based on status, access checks, and missing invitation timestamps."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        days_until_start = _as_int(kwargs.get("days_until_start"))
        if days_until_start is None:
            return _err("days_until_start (integer) is required")

        candidates = data.get("candidates", [])
        access_checks = data.get("access_checks", [])
        emails = data.get("emails", [])

        ready_candidates = []
        for candidate in candidates:
            start_date = candidate.get("start_date")
            cid = str(candidate.get("candidate_id"))

            if not start_date:
                continue

            # Check days until start
            if _days_between(HARD_TS.split('T')[0], start_date) > days_until_start:
                continue

            # Check status (assuming 'Asset Pending' or 'Packet Sent' are ready states)
            if candidate.get("onboarding_status") not in ["Asset Pending", "Packet Sent", "Started"]:
                 continue

            # Check access checks
            candidate_access_checks = [ac for ac in access_checks if str(ac.get("candidate_id")) == cid]
            if not candidate_access_checks or any(ac.get("status") == "Failed" for ac in candidate_access_checks):
                continue

            # Check for existing orientation invitation by searching subject
            has_invitation = any(
                "orientation invitation" in str(e.get("subject", "")).lower()
                for e in emails
                if str(e.get("candidate_id_nullable")) == cid
            )
            if has_invitation:
                continue

            candidate_copy = candidate.copy()
            # Simple priority scoring
            priority_score = 100 - _days_between(HARD_TS.split('T')[0], start_date)
            candidate_copy["scheduling_priority_score"] = priority_score
            ready_candidates.append(candidate_copy)

        ready_candidates.sort(key=lambda x: x["scheduling_priority_score"], reverse=True)

        return json.dumps(ready_candidates, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_candidates_needing_orientation_scheduling",
                "description": "Identifies candidates ready for orientation based on status, access checks, and missing invitation timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "days_until_start": {"type": "integer", "description": "How many days before start date to schedule"}
                    },
                    "required": ["days_until_start"],
                },
            },
        }

# ============================================================
# 11. analyze_attachment_file_inventory
# ============================================================
class AnalyzeAttachmentFileInventoryTool(Tool):
    """Queries attachments table analyzing file types, sizes, and email linkage patterns across candidates."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        file_type_filter = kwargs.get("file_type_filter")

        attachments = data.get("attachments", [])
        emails = data.get("emails", [])

        # Create a map for quick lookup
        email_id_to_candidate_id = {
            e.get("message_id"): e.get("candidate_id_nullable") for e in emails
        }

        # Filter by candidate if provided
        if candidate_id:
            # Get all attachment IDs linked to the candidate's emails
            candidate_attachment_ids = set()
            for email in emails:
                if str(email.get("candidate_id_nullable")) == str(candidate_id):
                    for att_id in email.get("attachments_ids", []):
                        candidate_attachment_ids.add(att_id)

            attachments = [
                att for att in attachments
                if att.get("attachment_id") in candidate_attachment_ids
            ]

        # Filter by file type
        if file_type_filter:
            attachments = [
                att for att in attachments
                if att.get("mime_type") == file_type_filter
            ]

        # Analysis
        total_size = sum(att.get("size_bytes", 0) for att in attachments)
        file_type_distribution = {}
        for att in attachments:
            mime_type = att.get("mime_type", "unknown")
            file_type_distribution[mime_type] = file_type_distribution.get(mime_type, 0) + 1

        result = {
            "total_attachments": len(attachments),
            "total_size_bytes": total_size,
            "file_type_distribution": file_type_distribution,
            "attachments_sample": attachments[:10] # a sample
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyze_attachment_file_inventory",
                "description": "Queries attachments table analyzing file types, sizes, and email linkage patterns across candidates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "Specific candidate or null for system-wide analysis"},
                        "file_type_filter": {"type": "string", "description": "MIME type filter"}
                    },
                    "required": [],
                },
            },
        }

# ============================================================
# 12. get_email_thread_conversations
# ============================================================
class GetEmailThreadConversationsTool(Tool):
    """Traces email threads using thread_id and reply relationships to reconstruct conversation flows."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        include_drafts = kwargs.get("include_draft_responses", False)

        if not candidate_id:
            return _err("candidate_id is required")

        emails = data.get("emails", [])

        candidate_emails = [
            e for e in emails
            if str(e.get("candidate_id_nullable")) == str(candidate_id)
        ]

        if not include_drafts:
            candidate_emails = [e for e in candidate_emails if not e.get("draft_flag")]

        # Group by thread_id
        threads = {}
        for email in candidate_emails:
            thread_id = email.get("thread_id_nullable")
            if thread_id:
                if thread_id not in threads:
                    threads[thread_id] = []
                threads[thread_id].append(email)

        # Sort emails within each thread by date
        for thread_id in threads:
            threads[thread_id].sort(key=lambda e: e.get("date_ts", ""))

        return json.dumps(threads, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_email_thread_conversations",
                "description": "Traces email threads using thread_id and reply relationships to reconstruct conversation flows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "Target candidate"},
                        "include_draft_responses": {"type": "boolean", "description": "Include unsent draft replies"}
                    },
                    "required": ["candidate_id"],
                },
            },
        }

# ============================================================
# 13. query_label_usage_patterns
# ============================================================
class QueryLabelUsagePatternsTool(Tool):
    """Analyzes email_labels usage across emails to understand categorization patterns and missing labels."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        label_category_filter = kwargs.get("label_category") # This parameter is kept but won't be used as category doesn't exist

        labels_map = {l.get("label_id"): l for l in data.get("email_labels", [])}
        emails = data.get("emails", [])

        usage_stats = {}
        unlabeled_emails = 0

        for email in emails:
            label_ids = email.get("labels_ids", [])
            if not label_ids:
                unlabeled_emails += 1
                continue

            for label_id in label_ids:
                label = labels_map.get(label_id)
                if label:
                    label_name = label.get("name", "Unknown")
                    if label_name not in usage_stats:
                        usage_stats[label_name] = {"count": 0}
                    usage_stats[label_name]["count"] += 1

        result = {
            "label_usage_stats": usage_stats,
            "unlabeled_email_count": unlabeled_emails
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "query_label_usage_patterns",
                "description": "Analyzes email_labels usage across emails to understand categorization patterns and missing labels.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "label_category": {"type": "string", "description": "Specific label type to analyze"}
                    },
                    "required": [],
                },
            },
        }

# ============================================================
# 14. check_file_storage_organization
# ============================================================
class CheckFileStorageOrganizationTool(Tool):
    """Reviews onboarding_files table analyzing file path organization, duplicate content, and candidate file completeness."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")

        files = data.get("onboarding_files", [])

        if candidate_id:
            files = [f for f in files if str(f.get("candidate_id")) == str(candidate_id)]

        # Analyze duplicates based on content_text
        content_map = {}
        duplicates = []
        for file in files:
            content = file.get("content_text")
            if content:
                if content in content_map:
                    duplicates.append({
                        "original": content_map[content],
                        "duplicate": file.get("file_path")
                    })
                else:
                    content_map[content] = file.get("file_path")

        # Analyze organization (simple check for path structure)
        improperly_organized = [
            f.get("file_path") for f in files
            if not re.match(r"/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+/", str(f.get("file_path", "")))
        ]

        result = {
            "total_files_analyzed": len(files),
            "duplicate_files_found": len(duplicates),
            "improperly_organized_paths": improperly_organized,
            "duplicates": duplicates
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_file_storage_organization",
                "description": "Reviews onboarding_files table analyzing file path organization, duplicate content, and candidate file completeness.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "Specific candidate or null for system analysis"}
                    },
                    "required": [],
                },
            },
        }

# ============================================================
# 15. get_manager_candidate_assignments
# ============================================================
class GetManagerCandidateAssignmentsTool(Tool):
    """Analyzes candidates table to understand manager workload distribution and onboarding supervision patterns."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        manager_email = kwargs.get("manager_email")

        candidates = data.get("candidates", [])

        if manager_email:
            candidates = [c for c in candidates if c.get("manager_email_nullable") == manager_email]

        manager_workload = {}
        for candidate in candidates:
            manager = candidate.get("manager_email_nullable")
            if manager:
                if manager not in manager_workload:
                    manager_workload[manager] = {"count": 0, "candidates": []}
                manager_workload[manager]["count"] += 1
                manager_workload[manager]["candidates"].append({
                    "candidate_id": candidate.get("candidate_id"),
                    "candidate_name": candidate.get("candidate_name"),
                    "status": candidate.get("onboarding_status")
                })

        return json.dumps(manager_workload, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_manager_candidate_assignments",
                "description": "Analyzes candidates table to understand manager workload distribution and onboarding supervision patterns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "manager_email": {"type": "string", "description": "Specific manager or null for all managers"}
                    },
                    "required": [],
                },
            },
        }

# ============================================================
# 16. create_new_candidate_record
# ============================================================
class CreateNewCandidateRecordTool(Tool):
    """Inserts candidate into candidates table with validation, duplicate checking, and initial status setting."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_name = kwargs.get("candidate_name")
        role_title = kwargs.get("role_title")
        start_date = kwargs.get("start_date")
        candidate_email = kwargs.get("candidate_email")
        manager_email = kwargs.get("manager_email")

        if not all([candidate_name, role_title, start_date, candidate_email]):
            return _err("candidate_name, role_title, start_date, and candidate_email are required")

        candidates = data.setdefault("candidates", [])

        # Duplicate check
        if any(c.get("candidate_email") == candidate_email for c in candidates):
            return _err(f"Candidate with email '{candidate_email}' already exists.", code="conflict")

        new_candidate = {
            "candidate_id": _next_str_id(candidates, "candidate_id", "CAND-"),
            "candidate_name": candidate_name,
            "candidate_email": candidate_email,
            "role_title": role_title,
            "start_date": start_date,
            "manager_email_nullable": manager_email,
            "onboarding_status": "Started",
            "created_ts": HARD_TS,
            "asset_request_record_id_nullable": None,
            "checklist_follow_up_ts_nullable": None,
            "orientation_invite_ts_nullable": None,
            "manager_intro_invite_ts_nullable": None,
            "welcome_email_message_id_nullable": None
        }

        candidates.append(new_candidate)

        return json.dumps(new_candidate, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_candidate_record",
                "description": "Inserts candidate into candidates table with validation, duplicate checking, and initial status setting.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_name": {"type": "string", "description": "Full name from user input"},
                        "role_title": {"type": "string", "description": "Job position title"},
                        "start_date": {"type": "string", "description": "Start date in YYYY-MM-DD format"},
                        "candidate_email": {"type": "string", "description": "Company email address"},
                        "manager_email": {"type": "string", "description": "Manager email if known"}
                    },
                    "required": ["candidate_name", "role_title", "start_date", "candidate_email"],
                },
            },
        }

# ============================================================
# 17. update_candidate_onboarding_status
# ============================================================
class UpdateCandidateOnboardingStatusTool(Tool):
    """Updates status and related timestamp fields for one or more candidates."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        candidate_ids = kwargs.get("candidate_ids")
        new_status = kwargs.get("new_status")

        if not new_status:
            return _err("new_status is required.")

        ids_to_process = []
        if candidate_ids:
            ids_to_process.extend(candidate_ids)
        if candidate_id:
            ids_to_process.append(candidate_id)

        if not ids_to_process:
            return _err("candidate_id or candidate_ids is required.")

        candidates = data.get("candidates", [])
        updated_candidates = []

        for cid in ids_to_process:
            candidate = next((c for c in candidates if str(c.get("candidate_id")) == str(cid)), None)

            if not candidate:
                if len(ids_to_process) == 1:
                    return _err(f"Candidate '{cid}' not found.", code="not_found")
                continue

            candidate["onboarding_status"] = new_status
            updated_candidates.append(candidate)

        return json.dumps(updated_candidates, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_candidate_onboarding_status",
                "description": "Updates status and related timestamp fields for one or more candidates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "A single target candidate identifier."},
                        "candidate_ids": {"type": "array", "items": {"type": "string"}, "description": "A list of target candidate identifiers."},
                        "new_status": {"type": "string", "description": "Status from workflow analysis"},
                    },
                    "required": ["new_status"],
                },
            },
        }

# ============================================================
# 18. generate_personalized_welcome_file (Refactored)
# ============================================================
class GeneratePersonalizedWelcomeFileTool(Tool):
    """Creates customized welcome markdown in onboarding_files table for one or more candidates."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        candidate_ids = kwargs.get("candidate_ids")

        ids_to_process = []
        if candidate_ids:
            ids_to_process.extend(candidate_ids)
        if candidate_id:
            ids_to_process.append(candidate_id)

        if not ids_to_process:
            return _err("candidate_id or candidate_ids is required.")

        candidates_map = {str(c.get("candidate_id")): c for c in data.get("candidates", [])}
        onboarding_files = data.setdefault("onboarding_files", [])
        created_files = []

        for cid in ids_to_process:
            candidate = candidates_map.get(cid)
            if not candidate:
                if len(ids_to_process) == 1:
                    return _err(f"Candidate '{cid}' not found.", code="not_found")
                continue

            # Hardcoded markdown template
            template_content = """
# Welcome, {{candidate_name}}!

We are thrilled to have you join us as a {{role_title}}. Your first day will be on {{start_date}}.
Your manager will be {{manager_email_nullable}}.

We've prepared this packet to help you get started.
"""

            context = candidate
            content = _render_template(template_content, context)

            new_file_path = f"/onboarding/{cid}/welcome_packet.md"

            new_file = {
                "file_path": new_file_path,
                "content_text": content,
                "mime_type": "text/markdown",
                "created_ts": HARD_TS,
                "updated_ts": HARD_TS,
                "candidate_id": cid
            }
            onboarding_files.append(new_file)
            created_files.append(new_file)

        return json.dumps(created_files, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_personalized_welcome_file",
                "description": "Creates customized welcome markdown for one or more candidates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "A single target candidate identifier."},
                        "candidate_ids": {"type": "array", "items": {"type": "string"}, "description": "A list of target candidate identifiers."}
                    },
                },
            },
        }

# ============================================================
# 19. create_role_based_checklist_tasks (Refactored)
# ============================================================
class CreateRoleBasedChecklistTasksTool(Tool):
    """Inserts multiple checklist_items records based on the roles of one or more candidates."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        candidate_ids = kwargs.get("candidate_ids")

        ids_to_process = []
        if candidate_ids:
            ids_to_process.extend(candidate_ids)
        if candidate_id:
            ids_to_process.append(candidate_id)

        if not ids_to_process:
            return _err("candidate_id or candidate_ids is required.")

        candidates_map = {str(c.get("candidate_id")): c for c in data.get("candidates", [])}
        checklist_items = data.setdefault("checklist_items", [])
        all_created_tasks = []

        for cid in ids_to_process:
            candidate = candidates_map.get(cid)
            if not candidate:
                if len(ids_to_process) == 1:
                    return _err(f"Candidate '{cid}' not found.", code="not_found")
                continue

            start_date_str = candidate.get("start_date")
            if not start_date_str:
                if len(ids_to_process) == 1:
                    return _err("Candidate start_date is required for due date calculation.")
                continue

            start_date = datetime.fromisoformat(start_date_str)
            role_title = candidate.get("role_title", "").replace(" ", "")

            task_list = ROLE_CHECKLIST_MAP.get(role_title, [])
            if not task_list:
                for key, value in ROLE_CHECKLIST_MAP.items():
                    if role_title.lower() in key.lower().replace(" ", ""):
                        task_list = value
                        break

            if not task_list:
                if len(ids_to_process) == 1:
                    return _err(f"No task template found for role '{candidate.get('role_title', '')}'.")
                continue

            created_tasks = []
            for task in task_list:
                due_date = start_date + timedelta(days=task["due_days"])
                new_task = {
                    "item_id": _next_str_id(checklist_items, "item_id", "ITEM-"),
                    "candidate_id": cid,
                    "task_name": task["task_name"],
                    "status": "Pending",
                    "due_date": due_date.strftime("%Y-%m-%d"),
                    "created_ts": HARD_TS,
                    "updated_ts": HARD_TS,
                    "reminder_sent_flag": False,
                    "reminder_email_message_id_nullable": None
                }
                checklist_items.append(new_task)
                created_tasks.append(new_task)
            all_created_tasks.extend(created_tasks)

        return json.dumps(all_created_tasks, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_role_based_checklist_tasks",
                "description": "Inserts multiple checklist_items records based on the roles of one or more candidates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "A single target candidate identifier."},
                        "candidate_ids": {"type": "array", "items": {"type": "string"}, "description": "A list of target candidate identifiers."}
                    },
                },
            },
        }

# ============================================================
# 20. assign_asset_to_candidate
# ============================================================
class AssignAssetToCandidateTool(Tool):
    """Updates inventory_assets table to assign specific asset and updates corresponding asset_requests status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_request_id = kwargs.get("asset_request_id")
        asset_tag = kwargs.get("asset_tag")

        if not asset_request_id or not asset_tag:
            return _err("asset_request_id and asset_tag are required.")

        # Find asset and request
        asset = next((a for a in data.get("inventory_assets", []) if a.get("asset_tag") == asset_tag), None)
        request = next((r for r in data.get("asset_requests", []) if str(r.get("request_id")) == str(asset_request_id)), None)

        if not asset:
            return _err(f"Asset with tag '{asset_tag}' not found.", code="not_found")
        if not request:
            return _err(f"Asset request '{asset_request_id}' not found.", code="not_found")

        if asset.get("status") != "Available":
            return _err(f"Asset '{asset_tag}' is not available for assignment.")

        # Assign asset
        asset["status"] = "Assigned"
        asset["assigned_candidate_id_nullable"] = request.get("candidate_id")

        # Update request
        request["status"] = "Completed"
        request["asset_tag_nullable"] = asset_tag
        request["updated_ts"] = HARD_TS

        result = {
            "asset": asset,
            "asset_request": request
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_asset_to_candidate",
                "description": "Updates inventory_assets table to assign specific asset and updates corresponding asset_requests status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_request_id": {"type": "string", "description": "Request being fulfilled"},
                        "asset_tag": {"type": "string", "description": "Specific asset from availability search"},
                    },
                    "required": ["asset_request_id", "asset_tag"],
                },
            },
        }

# ============================================================
# 21. send_email_with_attachments (Refactored)
# ============================================================
class SendEmailWithAttachmentsTool(Tool):
    """Creates a new email record from a template, with attachments."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        template_name = kwargs.get("template_name")
        template_context = kwargs.get("template_context", {})

        if not candidate_id or not template_name:
            return _err("candidate_id and template_name are required.")

        candidate = next((c for c in data.get("candidates", []) if str(c.get("candidate_id")) == str(candidate_id)), None)
        if not candidate:
            return _err(f"Candidate '{candidate_id}' not found.", code="not_found")

        # Dynamic context generation for specific templates
        if template_name == "it_support_request" and "failure_notes" in template_context:
            # Handle dictionary from analyze_system_access_failures
            if isinstance(template_context['failure_notes'], dict):
                failures = template_context['failure_notes']
                failure_notes_str = "\n".join([f"- {sys}: {', '.join(details.get('failure_notes', []))}" for sys, details in failures.items()])
                template_context['failure_notes'] = failure_notes_str

            # Default recipient for IT support requests
            kwargs.setdefault('to_emails', ['it-support@example.com'])

        if template_name == "asset_fulfillment_notification":
            # Ensure asset_name and asset_tag are in context
            if "asset_name" not in template_context or "asset_tag" not in template_context:
                return _err("asset_fulfillment_notification template requires asset_name and asset_tag in template_context.")

        if not kwargs.get('to_emails'):
            return _err("to_emails is required for this template.")

        context = candidate.copy()
        context.update(template_context)
        rendered_content = _get_hardcoded_template_and_render(template_name, context)

        emails = data.setdefault("emails", [])
        attachments = data.setdefault("attachments", [])
        onboarding_files = data.get("onboarding_files", [])

        new_email = {
            "message_id": _next_str_id(emails, "message_id", "msg_"),
            "subject": rendered_content["subject"],
            "body": rendered_content["body"],
            "from_email": kwargs.get("from_email", "hr@company.com"),
            "to_emails": kwargs.get("to_emails"),
            "cc_emails": kwargs.get("cc_emails", []),
            "date_ts": HARD_TS,
            "labels_ids": kwargs.get("label_ids", []),
            "attachments_ids": [],
            "draft_flag": False, "sent_flag": True,
            "candidate_id_nullable": candidate_id,
            "thread_id_nullable": None, "in_reply_to_message_id_nullable": None
        }

        attachment_paths = kwargs.get("attachment_file_paths", [])
        if template_name == "welcome":
            welcome_packet_path = f"/onboarding/{candidate_id}/welcome_packet.md"
            if any(f.get("file_path") == welcome_packet_path for f in onboarding_files):
                attachment_paths.append(welcome_packet_path)

        for file_path in attachment_paths:
            source_file = next((f for f in onboarding_files if f.get("file_path") == file_path), None)
            if source_file:
                new_attachment_id = _next_str_id(attachments, "attachment_id", "attach_")
                new_attachment = {
                    "attachment_id": new_attachment_id,
                    "message_id": new_email["message_id"],
                    "filename": file_path.split('/')[-1],
                    "mime_type": source_file.get("mime_type"),
                    "file_path": file_path,
                    "size_bytes": source_file.get("size_bytes", 1024),
                    "stored_ts": HARD_TS
                }
                attachments.append(new_attachment)
                new_email["attachments_ids"].append(new_attachment_id)

        emails.append(new_email)

        result = {
            "email": new_email,
            "results": {'system_name': 'Email', 'status': 'Success'}
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_email_with_attachments",
                "description": "Creates a new email from a template, with attachments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "template_name": {"type": "string"},
                        "to_emails": {"type": "array", "items": {"type": "string"}, "description": "Required. List of recipient email addresses."},
                        "from_email": {"type": "string", "description": "Optional: Defaults to hr@company.com"},
                        "cc_emails": {"type": "array", "items": {"type": "string"}},
                        "attachment_file_paths": {"type": "array", "items": {"type": "string"}, "description": "Optional: paths to attach. Welcome packet is auto-attached for 'welcome' template."},
                        "label_ids": {"type": "array", "items": {"type": "string"}},
                        "template_context": {"type": "object", "description": "Optional: context for templates. For IT support, failure notes are auto-generated. For asset_fulfillment_notification, requires asset_name and asset_tag."}
                    },
                    "required": ["candidate_id", "template_name", "to_emails"],
                },
            },
        }

# ============================================================
# 22. run_and_record_system_access_checks (Replaces record_system_access_results)
# ============================================================
class RunAndRecordSystemAccessChecksTool(Tool):
    """Checks necessary system access for one or more candidates based on their role and records the results."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        candidate_ids = kwargs.get("candidate_ids")

        ids_to_process = []
        if candidate_ids:
            ids_to_process.extend(candidate_ids)
        if candidate_id:
            ids_to_process.append(candidate_id)

        if not ids_to_process:
            return _err("candidate_id or candidate_ids is required.")

        candidates_map = {str(c.get("candidate_id")): c for c in data.get("candidates", [])}
        access_checks = data.setdefault("access_checks", [])
        all_created_records = []

        for cid in ids_to_process:
            candidate = candidates_map.get(cid)
            if not candidate:
                if len(ids_to_process) == 1:
                    return _err(f"Candidate '{cid}' not found.", code="not_found")
                continue

            role_title = candidate.get("role_title", "")
            base_systems = ["Email", "SSO", "Slack"]
            role_specific_systems = ROLE_SYSTEMS_MAP.get(role_title, [])
            systems_to_check = base_systems + role_specific_systems

            created_records = []
            for system_name in systems_to_check:
                status = "Success"
                note_nullable = None
                if (sum(ord(c) for c in cid) + len(system_name)) % 7 == 0:
                    status = "Failed"
                    note_nullable = f"Automated check failed. Code: {sum(ord(c) for c in cid[:5])}."

                new_check = {
                    "candidate_id": cid,
                    "system_name": system_name,
                    "status": status,
                    "note_nullable": note_nullable,
                    "checked_ts": HARD_TS
                }
                access_checks.append(new_check)
                created_records.append(new_check)
            all_created_records.extend(created_records)

        return json.dumps(all_created_records, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "run_and_record_system_access_checks",
                "description": "Checks necessary system access for one or more candidates based on their role and records the results.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "A single target candidate identifier."},
                        "candidate_ids": {"type": "array", "items": {"type": "string"}, "description": "A list of target candidate identifiers."}
                    },
                },
            },
        }

# ============================================================
# 23. update_task_completion_status
# ============================================================
class UpdateTaskCompletionStatusTool(Tool):
    """Updates existing records in `checklist_items` array by setting status to 'Completed'."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_ids = kwargs.get("item_ids", [])
        if not item_ids:
            return _err("item_ids array is required.")

        checklist_items = data.get("checklist_items", [])
        updated_items = []

        for item_id in item_ids:
            item = next((i for i in checklist_items if i.get("item_id") == item_id), None)
            if item:
                item["status"] = "Completed"
                item["updated_ts"] = HARD_TS
                item["reminder_sent_flag"] = False
                updated_items.append(item)

        return json.dumps(updated_items, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_task_completion_status",
                "description": "Updates `checklist_items` to mark tasks as 'Completed'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["item_ids"],
                },
            },
        }

# ============================================================
# 24. create_asset_request_with_notification (Refactored)
# ============================================================
class CreateAssetRequestWithNotificationTool(Tool):
    """Creates asset requests and corresponding IT notification emails for one or more candidates."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        candidate_ids = kwargs.get("candidate_ids")

        ids_to_process = []
        if candidate_ids:
            ids_to_process.extend(candidate_ids)
        if candidate_id:
            ids_to_process.append(candidate_id)

        if not ids_to_process:
            return _err("candidate_id or candidate_ids is required.")

        candidates_map = {str(c.get("candidate_id")): c for c in data.get("candidates", [])}
        asset_requests = data.setdefault("asset_requests", [])
        emails = data.setdefault("emails", [])
        all_results = []

        for cid in ids_to_process:
            candidate = candidates_map.get(cid)
            if not candidate:
                if len(ids_to_process) == 1:
                    return _err(f"Candidate '{cid}' not found.", code="not_found")
                continue

            role_title = candidate.get("role_title", "")
            defaults = ROLE_ASSET_DEFAULTS_MAP.get(role_title, ROLE_ASSET_DEFAULTS_MAP["Default"])
            asset_type = kwargs.get("asset_type", defaults["asset_type"])
            urgency = kwargs.get("urgency_level", defaults["urgency_level"])
            specs = kwargs.get("specifications", defaults["specifications"])

            context = {
                "candidate_name": candidate.get("candidate_name", ""),
                "urgency_level": urgency,
                "specifications": specs
            }
            rendered = _get_hardcoded_template_and_render("asset_request_notification", context)

            new_email_id = _next_str_id(emails, "message_id", "msg_")
            new_email = {
                "message_id": new_email_id,
                "subject": rendered["subject"],
                "body": rendered["body"],
                "from_email": "hr@company.com",
                "to_emails": ["it-assets@company.com"],
                "cc_emails": [candidate.get("manager_email_nullable")] if candidate.get("manager_email_nullable") else [],
                "date_ts": HARD_TS, "labels_ids": ["label_1"], "attachments_ids": [],
                "draft_flag": False, "sent_flag": True,
                "candidate_id_nullable": cid,
                "thread_id_nullable": None, "in_reply_to_message_id_nullable": None
            }
            emails.append(new_email)

            new_request = {
                "request_id": _next_str_id(asset_requests, "request_id", "asset_req_"),
                "candidate_id": cid,
                "asset_type": asset_type,
                "status": "Pending",
                "email_message_id_nullable": new_email_id,
                "inventory_checked_flag": False,
                "asset_tag_nullable": None,
                "requested_ts": HARD_TS,
                "updated_ts": HARD_TS
            }
            asset_requests.append(new_request)

            result = {
                "asset_request": new_request,
                "email": new_email,
                "results": {'system_name': 'Email', 'status': 'Success'}
            }
            all_results.append(result)

        return json.dumps(all_results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_asset_request_with_notification",
                "description": "Creates asset requests and corresponding IT notification emails for one or more candidates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "A single target candidate identifier."},
                        "candidate_ids": {"type": "array", "items": {"type": "string"}, "description": "A list of target candidate identifiers."},
                        "asset_type": {"type": "string", "description": "Optional: Defaults based on role."},
                        "urgency_level": {"type": "string", "description": "Optional: Defaults based on role."},
                        "specifications": {"type": "string", "description": "Optional: Defaults based on role."}
                    },
                },
            },
        }

# ============================================================
# 25. apply_email_labels_and_threading
# ============================================================
class ApplyEmailLabelsAndThreadingTool(Tool):
    """Updates existing records in `emails` array by modifying labels and thread IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        label_assignments = kwargs.get("label_assignments", {})
        thread_assignments = kwargs.get("thread_assignments", {})
        message_ids = set(label_assignments.keys()) | set(thread_assignments.keys())

        emails = data.get("emails", [])
        labels_map = {l.get("label_id") for l in data.get("email_labels", [])}
        updated_emails = []

        for msg_id in message_ids:
            email = next((e for e in emails if e.get("message_id") == msg_id), None)
            if email:
                if msg_id in label_assignments:
                    valid_labels = [l for l in label_assignments[msg_id] if l in labels_map]
                    email["labels_ids"] = valid_labels
                if msg_id in thread_assignments:
                    email["thread_id_nullable"] = thread_assignments[msg_id]
                updated_emails.append(email)

        return json.dumps(updated_emails, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_email_labels_and_threading",
                "description": "Updates emails with specified labels and thread IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "label_assignments": {"type": "object"},
                        "thread_assignments": {"type": "object"}
                    },
                    "required": [],
                },
            },
        }

# ============================================================
# 26. send_batch_reminder_emails (Refactored)
# ============================================================
class SendBatchReminderEmailsTool(Tool):
    """Creates multiple reminder emails from a template and updates corresponding `checklist_items`."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_ids = kwargs.get("candidate_ids", [])
        days_overdue_threshold = _as_int(kwargs.get("days_overdue_threshold", 0))
        template_name = "overdue_task_reminder"

        if not candidate_ids:
            return _err("candidate_ids array is required.")
        if days_overdue_threshold is None:
            return _err("days_overdue_threshold must be an integer.")

        emails = data.setdefault("emails", [])
        candidates_map = {c.get("candidate_id"): c for c in data.get("candidates", [])}
        all_checklist_items = data.get("checklist_items", [])

        results = []
        for candidate_id in candidate_ids:
            candidate = candidates_map.get(candidate_id)
            if not candidate: continue

            overdue_tasks = []
            for item in all_checklist_items:
                if str(item.get("candidate_id")) != str(candidate_id):
                    continue
                due_date = item.get("due_date")
                if not due_date or item.get("status") == "Completed":
                    continue
                days_overdue = _days_between(due_date, HARD_TS)
                if days_overdue >= days_overdue_threshold:
                    overdue_tasks.append(item)

            if not overdue_tasks:
                continue

            context = { "name": candidate.get("candidate_name"), "tasks": ", ".join([t.get("task_name", "") for t in overdue_tasks]) }
            rendered = _get_hardcoded_template_and_render(template_name, context)

            # Create Email
            new_email_id = _next_str_id(emails, "message_id", "msg_")
            new_email = {
                "message_id": new_email_id,
                "subject": rendered["subject"],
                "body": rendered["body"],
                "from_email": "hr@company.com",
                "to_emails": [candidate.get("candidate_email")],
                "cc_emails": [candidate.get("manager_email_nullable")] if candidate.get("manager_email_nullable") else [],
                "date_ts": HARD_TS, "labels_ids": ["label_2"], "attachments_ids": [],
                "draft_flag": False, "sent_flag": True,
                "candidate_id_nullable": candidate.get("candidate_id"),
                "thread_id_nullable": None, "in_reply_to_message_id_nullable": None
            }
            emails.append(new_email)

            # Update checklist items
            updated_items = []
            for item in overdue_tasks:
                item["reminder_sent_flag"] = True
                item["reminder_email_message_id_nullable"] = new_email_id
                item["updated_ts"] = HARD_TS
                updated_items.append(item)

            results.append({"created_email": new_email, "updated_checklist_items": updated_items, "results": {'system_name': 'Email', 'status': 'Success'}})

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {"name": "send_batch_reminder_emails",
            "description": "Sends batch reminder emails for overdue tasks.",
            "parameters": {"type": "object", "properties": {
                "candidate_ids": {"type": "array", "items": {"type": "string"}, "description": "List of candidate IDs to send reminders to."},
                "days_overdue_threshold": {"type": "integer", "description": "Minimum days past due date to trigger a reminder."}
            }, "required": ["candidate_ids", "days_overdue_threshold"]}}}

# ============================================================
# 27. update_asset_request_status
# ============================================================
class UpdateAssetRequestStatusTool(Tool):
    """Updates an existing asset request's status and related fields."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        new_status = kwargs.get("new_status")

        request = next((r for r in data.get("asset_requests", []) if r.get("request_id") == request_id), None)
        if not request:
            return _err(f"Request '{request_id}' not found", code="not_found")

        if new_status not in {"Pending", "Sent", "Reserved", "Completed"}:
            return _err("Invalid status.")

        request["status"] = new_status
        request["updated_ts"] = HARD_TS
        if "linked_message_id" in kwargs:
            request["email_message_id_nullable"] = kwargs["linked_message_id"]
        if "assigned_asset_tag" in kwargs:
            request["asset_tag_nullable"] = kwargs["assigned_asset_tag"]
            request["inventory_checked_flag"] = True

        return json.dumps(request, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {"name": "update_asset_request_status",
            "description": "Updates the status of an asset request.",
            "parameters": {"type": "object", "properties": {
                "request_id": {"type": "string"}, "new_status": {"type": "string"},
                "linked_message_id": {"type": "string"}, "assigned_asset_tag": {"type": "string"}
            }, "required": ["request_id", "new_status"]}}}

# ============================================================
# 28. create_orientation_invitation_emails (Refactored)
# ============================================================
class CreateOrientationInvitationEmailsTool(Tool):
    """Creates orientation and manager intro emails for candidates from templates."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidates_map = {c.get("candidate_id"): c for c in data.get("candidates", [])}
        emails = data.setdefault("emails", [])
        results = []

        orientation_details = kwargs.get("orientation_details", {})

        for candidate_id in kwargs.get("ready_candidate_ids", []):
            candidate = candidates_map.get(candidate_id)
            if not candidate: continue

            context = candidate.copy()
            context.update(orientation_details)

            # Orientation Email
            rendered_orient = _get_hardcoded_template_and_render("orientation_invitation", context)
            orient_email_id = _next_str_id(emails, "message_id", "msg_")
            orient_email = {
                "message_id": orient_email_id,
                "subject": rendered_orient["subject"],
                "body": rendered_orient["body"],
                "from_email": "hr@company.com", "to_emails": [candidate.get("candidate_email")],
                "cc_emails": [candidate.get("manager_email_nullable")] if candidate.get("manager_email_nullable") else [],
                "date_ts": HARD_TS, "labels_ids": ["label_4"], "attachments_ids": [],
                "draft_flag": False, "sent_flag": True, "candidate_id_nullable": candidate_id,
                "thread_id_nullable": None, "in_reply_to_message_id_nullable": None
            }
            emails.append(orient_email)

            # Manager Intro Email
            rendered_intro = _get_hardcoded_template_and_render("manager_introduction", context)
            intro_email_id = _next_str_id(emails, "message_id", "msg_")
            intro_email = {
                "message_id": intro_email_id,
                "subject": rendered_intro["subject"],
                "body": rendered_intro["body"],
                "from_email": "hr@company.com", "to_emails": [candidate.get("manager_email_nullable")],
                "cc_emails": [candidate.get("candidate_email")],
                "date_ts": HARD_TS, "labels_ids": ["label_5"], "attachments_ids": [],
                "draft_flag": False, "sent_flag": True, "candidate_id_nullable": candidate_id,
                "thread_id_nullable": None, "in_reply_to_message_id_nullable": None
            }
            emails.append(intro_email)

            candidate["orientation_invite_ts_nullable"] = HARD_TS
            candidate["manager_intro_invite_ts_nullable"] = HARD_TS

            results.append({"candidate_id": candidate_id, "orientation_email": orient_email, "manager_intro_email": intro_email, "updated_candidate": candidate, "results": {'system_name': 'Email', 'status': 'Success'}, "email_type": "orientation invitation"})

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {"name": "create_orientation_invitation_emails",
            "description": "Creates orientation and manager introduction emails.",
            "parameters": {"type": "object", "properties": {
                "ready_candidate_ids": {"type": "array", "items": {"type": "string"}},
                "orientation_details": {"type": "object", "description": "e.g., meeting_time, meeting_location"},
                "orientation_template_name": {"type": "string", "description": "Template name for orientation email"},
                "manager_intro_template_name": {"type": "string", "description": "Template name for manager introduction email"}
            }, "required": ["ready_candidate_ids", "orientation_template_name", "manager_intro_template_name"]}}}

# ============================================================
# 29. archive_completed_candidate_files
# ============================================================
class ArchiveCompletedCandidateFilesTool(Tool):
    """Updates file paths to archive them and creates a summary file."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        prefix = kwargs.get("archive_path_prefix", "/archived")
        files = data.setdefault("onboarding_files", [])

        updated_files = []
        archived_paths = []
        for file in files:
            if file.get("candidate_id") == candidate_id:
                old_path = file["file_path"]
                file["file_path"] = f"{prefix}{old_path}"
                file["updated_ts"] = HARD_TS
                updated_files.append(file)
                archived_paths.append(old_path)

        summary_content = f"Archived {len(archived_paths)} files for candidate {candidate_id}:\n" + "\n".join(archived_paths)
        summary_file = {
            "file_path": f"{prefix}/{candidate_id}/archive_summary.md",
            "content_text": summary_content, "mime_type": "text/markdown",
            "created_ts": HARD_TS, "updated_ts": HARD_TS,
            "candidate_id": candidate_id
        }
        files.append(summary_file)

        return json.dumps(updated_files + [summary_file], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {"name": "archive_completed_candidate_files",
            "description": "Archives files for a completed candidate.",
            "parameters": {"type": "object", "properties": {
                "candidate_id": {"type": "string"}, "archive_path_prefix": {"type": "string"}
            }, "required": ["candidate_id"]}}}

# ============================================================
# 30. consolidate_email_threads_and_cleanup (Fixed)
# ============================================================
class ConsolidateEmailThreadsAndCleanupTool(Tool):
    """Groups emails into threads and cleans up old drafts."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        age_days = kwargs.get("draft_cleanup_age_days", 30)

        all_emails = data.get("emails", [])
        candidate_emails = [e for e in all_emails if e.get("candidate_id_nullable") == candidate_id]
        updated_emails = []

        # Threading by subject
        subject_groups = {}
        for email in candidate_emails:
            subject = str(email.get("subject", "")).strip()
            # Normalize subject by removing Re: Fwd: etc.
            clean_subject = re.sub(r"^(Re|Fwd|RE|FWD):\s*", "", subject)
            if clean_subject not in subject_groups:
                subject_groups[clean_subject] = []
            subject_groups[clean_subject].append(email)

        for subject, group in subject_groups.items():
            if len(group) > 1:
                thread_id = _generate_new_thread_id(all_emails)
                for email in group:
                    if not email.get("thread_id_nullable"):
                        email["thread_id_nullable"] = thread_id
                        updated_emails.append(email)

        # Cleanup old drafts
        for email in candidate_emails:
            if email.get("draft_flag") and _days_between(email.get("date_ts", "0"), HARD_TS) > age_days:
                email["draft_flag"] = False
                email["sent_flag"] = False # It was never sent
                if email not in updated_emails:
                    updated_emails.append(email)

        return json.dumps(updated_emails, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {"name": "consolidate_email_threads_and_cleanup",
            "description": "Groups emails into threads and cleans up old drafts.",
            "parameters": {"type": "object", "properties": {
                "candidate_id": {"type": "string"}, "draft_cleanup_age_days": {"type": "integer"}
            }, "required": ["candidate_id"]}}}

# ============================================================
# 31. update_candidates_record
# ============================================================
class UpdateCandidatesRecordTool(Tool):
    """Updates one or more fields for a list of candidate records."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_ids = kwargs.get("candidate_ids")
        fields_to_update = kwargs.get("fields_to_update")

        if not candidate_ids or not isinstance(candidate_ids, list):
            return _err("candidate_ids (array) is required")
        if not fields_to_update or not isinstance(fields_to_update, dict):
            return _err("fields_to_update (object) is required")

        candidates = data.get("candidates", [])
        updated_candidates = []

        for candidate in candidates:
            if candidate.get("candidate_id") in candidate_ids:
                for field, value in fields_to_update.items():
                    if field in candidate:
                        candidate[field] = value
                updated_candidates.append(candidate)

        return json.dumps(updated_candidates, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_candidates_record",
                "description": "Updates one or more fields for a list of candidate records. Useful for setting timestamps or notes after an action has been performed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_ids": {"type": "array", "items": {"type": "string"}, "description": "List of candidate IDs to update."},
                        "fields_to_update": {"type": "object", "description": "A dictionary of fields to update. e.g., {\"checklist_follow_up_ts_nullable\": \"2024-08-15T12:00:00Z\"}"}
                    },
                    "required": ["candidate_ids", "fields_to_update"],
                },
            },
        }

# ============================================================
# 31. notify_manager
# ============================================================
class NotifyManagerTool(Tool):
    """Sends a standardized notification email to a candidate's manager."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        notification_type = kwargs.get("notification_type")

        if not candidate_id or not notification_type:
            return _err("candidate_id and notification_type are required.")

        candidate = next((c for c in data.get("candidates", []) if str(c.get("candidate_id")) == str(candidate_id)), None)
        if not candidate:
            return _err(f"Candidate '{candidate_id}' not found.", code="not_found")

        manager_email = candidate.get("manager_email_nullable")
        if not manager_email:
            return _err(f"Manager not found for candidate '{candidate_id}'.")

        template_name = f"manager_{notification_type}_notification"

        context = candidate.copy()
        context["manager_name"] = manager_email.split('@')[0]

        rendered = _get_hardcoded_template_and_render(template_name, context)

        emails = data.setdefault("emails", [])
        new_email = {
            "message_id": _next_str_id(emails, "message_id", "msg_"),
            "subject": rendered["subject"],
            "body": rendered["body"],
            "from_email": "hr@company.com",
            "to_emails": [manager_email],
            "cc_emails": [],
            "date_ts": HARD_TS,
            "labels_ids": [],
            "attachments_ids": [],
            "draft_flag": False, "sent_flag": True,
            "candidate_id_nullable": candidate_id,
            "thread_id_nullable": _generate_new_thread_id(emails),
            "in_reply_to_message_id_nullable": None
        }
        emails.append(new_email)

        return json.dumps(new_email, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "notify_manager",
                "description": "Sends a standardized notification email to a candidate's manager.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "notification_type": {"type": "string", "description": "e.g., 'access_issue', 'overdue_escalation'"}
                    },
                    "required": ["candidate_id", "notification_type"],
                },
            },
        }

# ============================================================
# 32. get_available_email_types
# ============================================================
class GetAvailableEmailTypesTool(Tool):
    """Returns a list of valid email types that can be used with the check_email_communication_gaps tool."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email_types = [
            "welcome",
            "asset provisioning request",
            "onboarding reminder",
            "orientation invitation",
            "introduction"
        ]
        return json.dumps(email_types, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_available_email_types",
                "description": "Returns a list of valid email types for checking communication gaps.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }

# ============================================================
# 33. resolve_sso_access_issue (New)
# ============================================================
class ResolveSSOAccessIssueTool(Tool):
    """Simulates an IT intervention to resolve a failed SSO access check for a candidate."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        if not candidate_id:
            return _err("candidate_id is required.")

        access_checks = data.get("access_checks", [])
        updated_checks = []

        # Find and fix the failed SSO check
        sso_check = next((ac for ac in access_checks if ac.get("candidate_id") == candidate_id and ac.get("system_name") == "SSO" and ac.get("status") == "Failed"), None)

        if not sso_check:
            return _err(f"No failed SSO access check found for candidate '{candidate_id}'.", code="not_found")

        sso_check["status"] = "Success"
        sso_check["note_nullable"] = "Resolved by IT."
        sso_check["checked_ts"] = HARD_TS
        updated_checks.append(sso_check)

        # Update dependent systems
        dependent_systems = ["Slack", "GitHub"]
        for system in dependent_systems:
            dependent_check = next((ac for ac in access_checks if ac.get("candidate_id") == candidate_id and ac.get("system_name") == system), None)
            if dependent_check and dependent_check.get("status") in ["Failed", "Pending"]:
                dependent_check["status"] = "Pending"
                dependent_check["note_nullable"] = "Ready for re-check after SSO resolution."
                dependent_check["checked_ts"] = HARD_TS
                updated_checks.append(dependent_check)

        return json.dumps(updated_checks, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "resolve_sso_access_issue",
                "description": "Simulates an IT intervention to resolve a failed SSO access check for a candidate, updating their status to 'Success'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"}
                    },
                    "required": ["candidate_id"],
                },
            },
        }

# ============================================================
# 34. update_access_check_status (New)
# ============================================================
class UpdateAccessCheckStatusTool(Tool):
    """Updates the status of a specific system access check for a candidate."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        system_name = kwargs.get("system_name")
        new_status = kwargs.get("new_status")
        note = kwargs.get("note")

        if not all([candidate_id, system_name, new_status]):
            return _err("candidate_id, system_name, and new_status are required.")

        access_check = next((ac for ac in data.get("access_checks", []) if ac.get("candidate_id") == candidate_id and ac.get("system_name") == system_name), None)

        if not access_check:
            return _err(f"No access check found for candidate '{candidate_id}' and system '{system_name}'.", code="not_found")

        access_check["status"] = new_status
        access_check["note_nullable"] = note
        access_check["checked_ts"] = HARD_TS

        return json.dumps(access_check, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_access_check_status",
                "description": "Updates the status of a specific system access check for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "system_name": {"type": "string"},
                        "new_status": {"type": "string"},
                        "note": {"type": "string"}
                    },
                    "required": ["candidate_id", "system_name", "new_status"],
                },
            },
        }

# ============================================================
# Export instances
# ============================================================
TOOLS = [
    GetCandidateWithFullContextTool(),
    FindCandidatesByOnboardingStatusTool(),
    GetOverdueChecklistItemsTool(),
    CheckEmailCommunicationGapsTool(),
    QueryAvailableAssetsByTypeTool(),
    GetPendingAssetRequestsTool(),
    AnalyzeSystemAccessFailuresTool(),
    GetDraftEmailsRequiringActionTool(),
    FindTemplateFilesByTypeTool(),
    GetCandidatesNeedingOrientationSchedulingTool(),
    AnalyzeAttachmentFileInventoryTool(),
    GetEmailThreadConversationsTool(),
    QueryLabelUsagePatternsTool(),
    CheckFileStorageOrganizationTool(),
    GetManagerCandidateAssignmentsTool(),
    CreateNewCandidateRecordTool(),
    UpdateCandidateOnboardingStatusTool(),
    GeneratePersonalizedWelcomeFileTool(),
    CreateRoleBasedChecklistTasksTool(),
    AssignAssetToCandidateTool(),
    SendEmailWithAttachmentsTool(),
    RunAndRecordSystemAccessChecksTool(),
    UpdateTaskCompletionStatusTool(),
    CreateAssetRequestWithNotificationTool(),
    ApplyEmailLabelsAndThreadingTool(),
    SendBatchReminderEmailsTool(),
    UpdateAssetRequestStatusTool(),
    CreateOrientationInvitationEmailsTool(),
    ArchiveCompletedCandidateFilesTool(),
    ConsolidateEmailThreadsAndCleanupTool(),
    UpdateCandidatesRecordTool(),
    NotifyManagerTool(),
    GetAvailableEmailTypesTool(),
    ResolveSSOAccessIssueTool(),
    UpdateAccessCheckStatusTool(),
]
