# Copyright Sierra

from .create_user import CreateUser
from .get_user_by_username import GetUserByUsername
from .get_user_by_id import GetUserById
from .get_user_by_name import GetUserByName
from .update_user_status import UpdateUserStatus
from .get_active_users_by_department import GetActiveUsersByDepartment
from .get_role_by_name import GetRoleByName
from .grant_role import GrantRole
from .get_roles_by_permission import GetRolesByPermission
from .get_user_roles import GetUserRoles
from .get_user_role import GetUserRole
from .revoke_role import RevokeRole
from .create_role import CreateRole
from .assign_permission_to_role import AssignPermissionToRole
from .get_permissions_by_resource import GetPermissionsByResource
from .get_permission_by_action_and_resource import GetPermissionByActionAndResource
from .get_role_permissions import GetRolePermissions
from .create_hubspot_ticket import CreateHubspotTicket
from .send_email import SendEmail
from .send_slack_message import SendSlackMessage
from .write_audit_log import WriteAuditLog
from .get_user_sessions import GetUserSessions
from .get_resource_by_name import GetResourceByName
from .create_access_request import CreateAccessRequest
from .get_access_request_details import GetAccessRequestDetails
from .create_certification import CreateCertification
from .get_certification_details import GetCertificationDetails
from .create_policy_exception import CreatePolicyException
from .get_policy_exception_details import GetPolicyExceptionDetails
from .get_current_time import GetCurrentTime
from .get_users_by_role import GetUsersByRole
from .create_permission import CreatePermission
from .create_resource import CreateResource
from .update_access_request_status import UpdateAccessRequestStatus
from .create_siem_alert import CreateSiemAlert
from .update_policy_exception_status import UpdatePolicyExceptionStatus
from .update_user_department import UpdateUserDepartment
from .update_user_mfa_status import UpdateUserMfaStatus
from .approve_policy_exception import ApprovePolicyException
from .update_resource_owner import UpdateResourceOwner
from .create_role_with_permission import CreateRoleWithPermission
from .list_roles import ListRoles
from .update_hubspot_ticket_status import UpdateHubspotTicketStatus
from .get_users_by_department import GetUsersByDepartment
from .merge_and_deprecate_role import MergeAndDeprecateRole
from .update_role_details import UpdateRoleDetails
from .list_inactive_users import ListInactiveUsers
from .terminate_user_session import TerminateUserSession
from .update_user_details import UpdateUserDetails
from .update_hubspot_ticket_assignee import UpdateHubspotTicketAssignee
from .get_hubspot_tickets_by_requester import GetHubspotTicketsByRequester
from .get_hubspot_tickets_by_assignee import GetHubspotTicketsByAssignee
from .get_resources_by_owner import GetResourcesByOwner
from .get_permission_details import GetPermissionDetails
from .get_siem_alerts import GetSiemAlerts
from .remove_permission_from_role import RemovePermissionFromRole
from .remove_role import RemoveRole
from .remove_permission import RemovePermission

ALL_TOOLS = [
    CreateUser,
    GetUserByUsername,
    GetUserById,
    GetUserByName,
    UpdateUserStatus,
    GetActiveUsersByDepartment,
    GetRoleByName,
    GrantRole,
    GetRolesByPermission,
    GetUserRoles,
    GetUserRole,
    RevokeRole,
    CreateRole,
    AssignPermissionToRole,
    GetPermissionsByResource,
    GetPermissionByActionAndResource,
    GetRolePermissions,
    CreateHubspotTicket,
    SendEmail,
    SendSlackMessage,
    WriteAuditLog,
    GetUserSessions,
    GetResourceByName,
    CreateAccessRequest,
    GetAccessRequestDetails,
    CreateCertification,
    GetCertificationDetails,
    CreatePolicyException,
    GetPolicyExceptionDetails,
    GetCurrentTime,
    GetUsersByRole,
    CreatePermission,
    CreateResource,
    UpdateAccessRequestStatus,
    CreateSiemAlert,
    UpdatePolicyExceptionStatus,
    UpdateUserDepartment,
    UpdateUserMfaStatus,
    ApprovePolicyException,
    UpdateResourceOwner,
    CreateRoleWithPermission,
    ListRoles,
    UpdateHubspotTicketStatus,
    GetUsersByDepartment,
    MergeAndDeprecateRole,
    UpdateRoleDetails,
    ListInactiveUsers,
    TerminateUserSession,
    UpdateUserDetails,
    UpdateHubspotTicketAssignee,
    GetHubspotTicketsByRequester,
    GetHubspotTicketsByAssignee,
    GetResourcesByOwner,
    GetPermissionDetails,
    GetSiemAlerts,
    RemovePermissionFromRole,
    RemoveRole,
    RemovePermission,
]
