# Copyright Sierra

from .get_access_request_tool import GetAccessRequestTool
from .review_access_request_tool import ReviewAccessRequestTool
from .get_user_roles_tool import GetUserRolesTool
from .revoke_user_role_tool import RevokeUserRoleTool
from .list_audit_logs_tool import ListAuditLogsTool
from .list_active_sessions_tool import ListActiveSessionsTool
from .create_access_request_tool import CreateAccessRequestTool
from .list_access_requests_by_status_tool import ListAccessRequestsByStatusTool
from .list_access_requests_by_user_tool import ListAccessRequestsByUserTool
from .assign_user_role_tool import AssignUserRoleTool
from .list_role_permissions_tool import ListRolePermissionsTool
from .get_role_name_tool import GetRoleNameTool
from .append_audit_log_tool import AppendAuditLogTool
from .log_revoke_decision_tool import LogRevokeDecisionTool
from .get_access_request_details_tool import GetAccessRequestDetailsTool
from .update_access_request_status_tool import UpdateAccessRequestStatusTool
from .grant_role_tool import GrantRoleTool
from .revoke_role_tool import RevokeRoleTool
from .send_email_tool import SendEmailTool
from .get_user_sessions_tool import GetUserSessionsTool
from .update_hubspot_ticket_status_tool import UpdateHubspotTicketStatusTool
from .update_hubspot_ticket_assignee_tool import UpdateHubspotTicketAssigneeTool
from .get_current_time_tool import GetCurrentTimeTool
from .get_users_by_role_tool import GetUsersByRoleTool
from .get_role_permissions_alias_tool import GetRolePermissionsAliasTool
from .get_hubspot_tickets_by_requester_tool import GetHubspotTicketsByRequesterTool
from .get_hubspot_tickets_by_assignee_tool import GetHubspotTicketsByAssigneeTool
from .complete_certification_tool import CompleteCertificationTool
from .start_certification_tool import StartCertificationTool
from .list_certifications_by_status_tool import ListCertificationsByStatusTool
from .get_permissions_for_user_tool import GetPermissionsForUserTool
from .check_user_status_tool import CheckUserStatusTool
from .assign_role_on_approval_tool import AssignRoleOnApprovalTool
from .list_policy_exceptions_tool import ListPolicyExceptionsTool
from .get_time_window_tool import GetTimeWindowTool
from .get_user_email_tool import GetUserEmailTool
from .list_emails_tool import ListEmailsTool
from .list_siem_alerts_tool import ListSiemAlertsTool
from .acknowledge_siem_alert_tool import AcknowledgeSiemAlertTool
from .list_hubspot_tickets_tool import ListHubspotTicketsTool
from .update_hubspot_ticket_tool import UpdateHubspotTicketTool
from .list_slack_messages_tool import ListSlackMessagesTool
from .list_users_by_mfa_tool import ListUsersByMfaTool
from .set_user_mfa_tool import SetUserMfaTool
from .upsert_email_tool import UpsertEmailTool
from .review_policy_exception_tool import ReviewPolicyExceptionTool
from .process_access_request_e2_e_tool import ProcessAccessRequestE2ETool
from .revoke_role_e2_e_tool import RevokeRoleE2ETool
from .close_hubspot_ticket_basic_tool import CloseHubspotTicketBasicTool
from .complete_certifications_and_audit_tool import CompleteCertificationsAndAuditTool
from .create_and_review_access_request_tool import CreateAndReviewAccessRequestTool

ALL_TOOLS = [
    GetAccessRequestTool,
    ReviewAccessRequestTool,
    GetUserRolesTool,
    RevokeUserRoleTool,
    ListAuditLogsTool,
    ListActiveSessionsTool,
    CreateAccessRequestTool,
    ListAccessRequestsByStatusTool,
    ListAccessRequestsByUserTool,
    AssignUserRoleTool,
    ListRolePermissionsTool,
    GetRoleNameTool,
    AppendAuditLogTool,
    LogRevokeDecisionTool,
    GetAccessRequestDetailsTool,
    UpdateAccessRequestStatusTool,
    GrantRoleTool,
    RevokeRoleTool,
    SendEmailTool,
    GetUserSessionsTool,
    UpdateHubspotTicketStatusTool,
    UpdateHubspotTicketAssigneeTool,
    GetCurrentTimeTool,
    GetUsersByRoleTool,
    GetRolePermissionsAliasTool,
    GetHubspotTicketsByRequesterTool,
    GetHubspotTicketsByAssigneeTool,
    CompleteCertificationTool,
    StartCertificationTool,
    ListCertificationsByStatusTool,
    GetPermissionsForUserTool,
    CheckUserStatusTool,
    AssignRoleOnApprovalTool,
    ListPolicyExceptionsTool,
    GetTimeWindowTool,
    GetUserEmailTool,
    ListEmailsTool,
    ListSiemAlertsTool,
    AcknowledgeSiemAlertTool,
    ListHubspotTicketsTool,
    UpdateHubspotTicketTool,
    ListSlackMessagesTool,
    ListUsersByMfaTool,
    SetUserMfaTool,
    UpsertEmailTool,
    ReviewPolicyExceptionTool,
    ProcessAccessRequestE2ETool,
    RevokeRoleE2ETool,
    CloseHubspotTicketBasicTool,
    CompleteCertificationsAndAuditTool,
    CreateAndReviewAccessRequestTool,
]
