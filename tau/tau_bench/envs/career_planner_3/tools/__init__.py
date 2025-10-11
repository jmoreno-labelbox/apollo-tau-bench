# Copyright Sierra

from .get_user_id import GetUserId
from .get_user_goals import GetUserGoals
from .get_role_requirements import GetRoleRequirements
from .get_user_skill_gap import GetUserSkillGap
from .recommend_course_for_gap import RecommendCourseForGap
from .get_team_members import GetTeamMembers
from .get_users_with_leadership_goals import GetUsersWithLeadershipGoals
from .assess_soft_skill_alignment import AssessSoftSkillAlignment
from .shortlist_successor_candidate import ShortlistSuccessorCandidate
from .get_user_target_role import GetUserTargetRole
from .assign_course_to_user import AssignCourseToUser
from .validate_user_goal_alignment import ValidateUserGoalAlignment
from .check_training_needed import CheckTrainingNeeded
from .validate_team_membership import ValidateTeamMembership
from .validate_course_skill_mapping import ValidateCourseSkillMapping
from .get_user_preferences import GetUserPreferences
from .get_user_course_progress import GetUserCourseProgress
from .log_team_training import LogTeamTraining
from .get_user_profile import GetUserProfile

ALL_TOOLS = [
    GetUserId,
    GetUserGoals,
    GetRoleRequirements,
    GetUserSkillGap,
    RecommendCourseForGap,
    GetTeamMembers,
    GetUsersWithLeadershipGoals,
    AssessSoftSkillAlignment,
    ShortlistSuccessorCandidate,
    GetUserTargetRole,
    AssignCourseToUser,
    ValidateUserGoalAlignment,
    CheckTrainingNeeded,
    ValidateTeamMembership,
    ValidateCourseSkillMapping,
    GetUserPreferences,
    GetUserCourseProgress,
    LogTeamTraining,
    GetUserProfile,
]
