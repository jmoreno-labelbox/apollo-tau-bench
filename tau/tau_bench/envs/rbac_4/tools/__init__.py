# Copyright Sierra

from .list_users_tool import ListUsersTool
from .get_user_details_tool import GetUserDetailsTool
from .list_roles_tool import ListRolesTool
from .revoke_role_from_user_tool import RevokeRoleFromUserTool
from .list_access_requests_tool import ListAccessRequestsTool
from .approve_access_request_tool import ApproveAccessRequestTool
from .reject_access_request_tool import RejectAccessRequestTool
from .get_certification_details_tool import GetCertificationDetailsTool
from .complete_certification_tool import CompleteCertificationTool
from .list_policy_exceptions_tool import ListPolicyExceptionsTool
from .approve_policy_exception_tool import ApprovePolicyExceptionTool
from .deny_policy_exception_tool import DenyPolicyExceptionTool
from .get_policy_exception_details_tool import GetPolicyExceptionDetailsTool
from .request_policy_exception_tool import RequestPolicyExceptionTool
from .list_siem_alerts_tool import ListSiemAlertsTool
from .get_siem_alert_details_tool import GetSiemAlertDetailsTool
from .create_siem_rule_tool import CreateSiemRuleTool
from .investigate_siem_incident_tool import InvestigateSiemIncidentTool
from .list_sessions_tool import ListSessionsTool
from .terminate_session_tool import TerminateSessionTool
from .audit_iam_access_tool import AuditIamAccessTool
from .search_logs_tool import SearchLogsTool
from .export_logs_tool import ExportLogsTool
from .get_user_roles_tool import GetUserRolesTool
from .get_permission_details_tool import GetPermissionDetailsTool
from .get_resource_details_tool import GetResourceDetailsTool
from .get_role_details_tool import GetRoleDetailsTool
from .create_user_tool import CreateUserTool
from .create_access_request_tool import CreateAccessRequestTool
from .create_hubspot_ticket_tool import CreateHubspotTicketTool
from .update_user_status_tool import UpdateUserStatusTool
from .escalate_siem_alert_tool import EscalateSiemAlertTool
from .search_slack_messages_tool import SearchSlackMessagesTool
from .moderate_slack_channel_tool import ModerateSlackChannelTool
from .create_incident_record_tool import CreateIncidentRecordTool
from .create_audit_log_tool import CreateAuditLogTool
from .send_email_tool import SendEmailTool
from .get_access_request_tool import GetAccessRequestTool
from .post_slack_message_tool import PostSlackMessageTool
from .get_role_members_tool import GetRoleMembersTool
from .assign_certification_tool import AssignCertificationTool
from .revoke_certification_tool import RevokeCertificationTool
from .link_alert_to_incident_tool import LinkAlertToIncidentTool
from .list_certifications_for_reviewer_tool import ListCertificationsForReviewerTool
from .get_ticket_details_tool import GetTicketDetailsTool
from .get_audit_logs_for_target_tool import GetAuditLogsForTargetTool
from .get_siem_alert_tool import GetSiemAlertTool
from .list_user_sessions_tool import ListUserSessionsTool
from .assign_role_to_user_tool import AssignRoleToUserTool
from .list_permissions_for_role_tool import ListPermissionsForRoleTool
from .get_certification_tool import GetCertificationTool
from .remove_role_from_user_tool import RemoveRoleFromUserTool
from .update_ticket_status_tool import UpdateTicketStatusTool
from .update_certification_status_tool import UpdateCertificationStatusTool
from .enable_user_mfa_tool import EnableUserMFATool
from .update_access_request_tool import UpdateAccessRequestTool
from .export_audit_logs_tool import ExportAuditLogsTool
from .get_current_time_tool import GetCurrentTimeTool

ALL_TOOLS = [
    ListUsersTool,
    GetUserDetailsTool,
    ListRolesTool,
    RevokeRoleFromUserTool,
    ListAccessRequestsTool,
    ApproveAccessRequestTool,
    RejectAccessRequestTool,
    GetCertificationDetailsTool,
    CompleteCertificationTool,
    ListPolicyExceptionsTool,
    ApprovePolicyExceptionTool,
    DenyPolicyExceptionTool,
    GetPolicyExceptionDetailsTool,
    RequestPolicyExceptionTool,
    ListSiemAlertsTool,
    GetSiemAlertDetailsTool,
    CreateSiemRuleTool,
    InvestigateSiemIncidentTool,
    ListSessionsTool,
    TerminateSessionTool,
    AuditIamAccessTool,
    SearchLogsTool,
    ExportLogsTool,
    GetUserRolesTool,
    GetPermissionDetailsTool,
    GetResourceDetailsTool,
    GetRoleDetailsTool,
    CreateUserTool,
    CreateAccessRequestTool,
    CreateHubspotTicketTool,
    UpdateUserStatusTool,
    EscalateSiemAlertTool,
    SearchSlackMessagesTool,
    ModerateSlackChannelTool,
    CreateIncidentRecordTool,
    CreateAuditLogTool,
    SendEmailTool,
    GetAccessRequestTool,
    PostSlackMessageTool,
    GetRoleMembersTool,
    AssignCertificationTool,
    RevokeCertificationTool,
    LinkAlertToIncidentTool,
    ListCertificationsForReviewerTool,
    GetTicketDetailsTool,
    GetAuditLogsForTargetTool,
    GetSiemAlertTool,
    ListUserSessionsTool,
    AssignRoleToUserTool,
    ListPermissionsForRoleTool,
    GetCertificationTool,
    RemoveRoleFromUserTool,
    UpdateTicketStatusTool,
    UpdateCertificationStatusTool,
    EnableUserMFATool,
    UpdateAccessRequestTool,
    ExportAuditLogsTool,
    GetCurrentTimeTool,
]
