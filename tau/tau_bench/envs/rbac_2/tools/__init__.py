# Copyright owned by Sierra

from .get_current_time import GetCurrentTime
from .create_user import CreateUser
from .get_user_details_by_id import GetUserDetailsById
from .get_user_details_by_username import GetUserDetailsByUsername
from .get_user_details_by_email import GetUserDetailsByEmail
from .get_role_id_by_name import GetRoleIdByName
from .create_access_request import CreateAccessRequest
from .assign_role_to_user import AssignRoleToUser
from .log_audit_event import LogAuditEvent
from .send_email import SendEmail
from .update_user_status import UpdateUserStatus
from .get_user_roles_by_user_id import GetUserRolesByUserId
from .revoke_role_from_user import RevokeRoleFromUser
from .get_access_request_by_id import GetAccessRequestById
from .get_resource_details_by_id import GetResourceDetailsById
from .approve_access_request import ApproveAccessRequest
from .get_siem_alert_by_id import GetSiemAlertById
from .get_certification_details_by_id import GetCertificationDetailsById
from .find_users_with_role import FindUsersWithRole
from .update_certification_status import UpdateCertificationStatus
from .create_policy_exception import CreatePolicyException
from .create_hubspot_ticket import CreateHubspotTicket
from .get_permission_by_name import GetPermissionByName
from .list_user_sessions import ListUserSessions
from .reject_access_request import RejectAccessRequest
from .get_resource_by_name import GetResourceByName
from .create_siem_alert import CreateSiemAlert
from .get_slack_message_by_id import GetSlackMessageById
from .find_access_request_by_details import FindAccessRequestByDetails
from .send_slack_message import SendSlackMessage
from .get_role_details_by_id import GetRoleDetailsById
from .find_resources import FindResources
from .update_user_department import UpdateUserDepartment
from .get_resource_by_name import GetResourceByName
from .get_hubspot_ticket_by_id import GetHubspotTicketById
from .update_hubspot_ticket import UpdateHubspotTicket
from .revoke_policy_exception import RevokePolicyException
from .get_policy_exception_by_id import GetPolicyExceptionById
from .get_policy_exception_by_user_id import GetPolicyExceptionByUserId
from .find_roles_by_resource_id import FindRolesByResourceId
from .find_hubspot_ticket_by_description import FindHubspotTicketByDescription
from .get_permission_by_id import GetPermissionById
from .find_resources_by_role_id import FindResourcesByRoleId
from .get_session_details_by_id import GetSessionDetailsById
from .check_user_sessions_by_id import CheckUserSessionsById
from .update_resource_owner import UpdateResourceOwner
from .update_access_request import UpdateAccessRequest
from .find_access_requests_by_user_id import FindAccessRequestsByUserId
from .get_permission_by_resource_id import GetPermissionByResourceId
from .get_user_role_details_by_user_role_id import GetUserRoleDetailsByUserRoleId

ALL_TOOLS = [
    GetCurrentTime,
    CreateUser,
    GetUserDetailsById,
    GetUserDetailsByUsername,
    GetUserDetailsByEmail,
    GetRoleIdByName,
    CreateAccessRequest,
    AssignRoleToUser,
    LogAuditEvent,
    SendEmail,
    UpdateUserStatus,
    GetUserRolesByUserId,
    RevokeRoleFromUser,
    GetAccessRequestById,
    GetResourceDetailsById,
    ApproveAccessRequest,
    GetSiemAlertById,
    GetCertificationDetailsById,
    FindUsersWithRole,
    UpdateCertificationStatus,
    CreatePolicyException,
    CreateHubspotTicket,
    GetPermissionByName,
    ListUserSessions,
    RejectAccessRequest,
    GetResourceByName,
    CreateSiemAlert,
    GetSlackMessageById,
    FindAccessRequestByDetails,
    SendSlackMessage,
    GetRoleDetailsById,
    FindResources,
    UpdateUserDepartment,
    GetResourceByName,
    GetHubspotTicketById,
    UpdateHubspotTicket,
    RevokePolicyException,
    GetPolicyExceptionById,
    GetPolicyExceptionByUserId,
    FindRolesByResourceId,
    FindHubspotTicketByDescription,
    GetPermissionById,
    FindResourcesByRoleId,
    GetSessionDetailsById,
    CheckUserSessionsById,
    UpdateResourceOwner,
    UpdateAccessRequest,
    FindAccessRequestsByUserId,
    GetPermissionByResourceId,
    GetUserRoleDetailsByUserRoleId,
]
