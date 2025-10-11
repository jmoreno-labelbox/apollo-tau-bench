# Copyright Sierra



# Utility functions
def _params(data, kwargs):
    """Merge data and kwargs into params dict."""
    return {**data, **kwargs}

def _require(params, keys):
    """Check if required keys exist in params."""
    missing = [k for k in keys if k not in params or params[k] is None]
    if missing:
        return f"Error: Missing required parameters: {', '.join(missing)}"
    return None


def _export_ext_from_profile(profile):
    """Extract export extension from profile."""
    return profile.get("export_extension", "png") if isinstance(profile, dict) else "png"



def _ensure(data, table_name, key_name, key_value):
    """Ensure an item exists in a table."""
    table = data.get(table_name, {})
    if isinstance(table, dict):
        table = list(table.values())
    
    for item in table:
        if item.get(key_name) == key_value:
            return item
    return None


from .find_gmail_threads import find_gmail_threads
from .get_gmail_thread import get_gmail_thread
from .list_gmail_messages import list_gmail_messages
from .create_gmail_thread import create_gmail_thread
from .append_gmail_message import append_gmail_message
from .apply_gmail_labels import apply_gmail_labels
from .list_artifacts import list_artifacts
from .list_assets import list_assets
from .export_assets import export_assets
from .list_figma_comments import list_figma_comments
from .create_figma_comment import create_figma_comment
from .list_audit_findings_ds import list_audit_findings_ds
from .list_audit_findings_a11y import list_audit_findings_a11y
from .generate_audit_report import GenerateAuditReport
from .update_audit_status import update_audit_status
from .get_audit import get_audit
from .list_review_cycles import list_review_cycles
from .create_review_cycle import create_review_cycle
from .get_review_cycle import get_review_cycle
from .list_review_approvals import list_review_approvals
from .update_review_approval import update_review_approval
from .attach_thread_to_review_cycle import attach_thread_to_review_cycle
from .update_review_cycle_status import update_review_cycle_status
from .verify_single_thread_per_cycle import verify_single_thread_per_cycle
from .list_releases import list_releases
from .get_release_diff import get_release_diff
from .create_fix_plan import create_fix_plan
from .deliver_fix_plan import deliver_fix_plan
from .upsert_fix_items import upsert_fix_items
from .update_fix_item_status import update_fix_item_status
from .governance_update import governance_update
from .record_automation_run import record_automation_run

ALL_TOOLS = [
    find_gmail_threads,
    get_gmail_thread,
    list_gmail_messages,
    create_gmail_thread,
    append_gmail_message,
    apply_gmail_labels,
    list_artifacts,
    list_assets,
    export_assets,
    list_figma_comments,
    create_figma_comment,
    list_audit_findings_ds,
    list_audit_findings_a11y,
    GenerateAuditReport,
    update_audit_status,
    get_audit,
    list_review_cycles,
    create_review_cycle,
    get_review_cycle,
    list_review_approvals,
    update_review_approval,
    attach_thread_to_review_cycle,
    update_review_cycle_status,
    verify_single_thread_per_cycle,
    list_releases,
    get_release_diff,
    create_fix_plan,
    deliver_fix_plan,
    upsert_fix_items,
    update_fix_item_status,
    governance_update,
    record_automation_run,
]
