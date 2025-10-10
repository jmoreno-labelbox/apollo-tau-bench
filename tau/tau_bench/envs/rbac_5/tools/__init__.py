from datetime import datetime
# Copyright Sierra


def get_current_timestamp():
    """Return current timestamp in ISO format."""
    return datetime.now().isoformat()



def _find_by_id(items, id_key, id_value):
    """Find item by ID."""
    for item in items:
        if item.get(id_key) == id_value:
            return item
    return None


from .create_user import CreateUser
from .update_user import UpdateUser
from .get_user import GetUser
from .get_role import GetRole
from .update_role import UpdateRole
from .get_user_roles import GetUserRoles
from .create_role import CreateRole
from .is_admin import IsAdmin
from .create_resource import CreateResource
from .get_resource import GetResource
from .list_users_with_access_to_resource import ListUsersWithAccessToResource
from .can_access_resource import CanAccessResource
from .get_access_request import GetAccessRequest
from .decide_access_request import DecideAccessRequest
from .ensure_user_role import EnsureUserRole
from .update_user_role import UpdateUserRole
from .get_base_role_by_department import GetBaseRoleByDepartment
from .check_so_d_conflicts import CheckSoDConflicts
from .get_certification import GetCertification
from .complete_certification import CompleteCertification
from .create_certification import CreateCertification
from .get_policy_exception import GetPolicyException
from .create_policy_exception import CreatePolicyException
from .decide_policy_exception import DecidePolicyException
from .get_permission import GetPermission
from .create_permission import CreatePermission
from .get_role_permissions import GetRolePermissions
from .assign_permission_to_role import AssignPermissionToRole
from .create_audit_log_entry import CreateAuditLogEntry
from .create_hub_spot_ticket import CreateHubSpotTicket
from .update_hub_spot_ticket import UpdateHubSpotTicket
from .get_hub_spot_ticket import GetHubSpotTicket
from .post_slack_message import PostSlackMessage
from .send_email import SendEmail
from .create_siem_alert import CreateSiemAlert
from .get_siem_alert import GetSiemAlert
from .update_session import UpdateSession
from .get_session import GetSession

ALL_TOOLS = [
    CreateUser,
    UpdateUser,
    GetUser,
    GetRole,
    UpdateRole,
    GetUserRoles,
    CreateRole,
    IsAdmin,
    CreateResource,
    GetResource,
    ListUsersWithAccessToResource,
    CanAccessResource,
    GetAccessRequest,
    DecideAccessRequest,
    EnsureUserRole,
    UpdateUserRole,
    GetBaseRoleByDepartment,
    CheckSoDConflicts,
    GetCertification,
    CompleteCertification,
    CreateCertification,
    GetPolicyException,
    CreatePolicyException,
    DecidePolicyException,
    GetPermission,
    CreatePermission,
    GetRolePermissions,
    AssignPermissionToRole,
    CreateAuditLogEntry,
    CreateHubSpotTicket,
    UpdateHubSpotTicket,
    GetHubSpotTicket,
    PostSlackMessage,
    SendEmail,
    CreateSiemAlert,
    GetSiemAlert,
    UpdateSession,
    GetSession,
]
