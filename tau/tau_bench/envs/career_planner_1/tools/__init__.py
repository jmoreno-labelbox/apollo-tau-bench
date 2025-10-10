# Copyright owned by Sierra.

from .get_job_posting import GetJobPosting
from .get_role_skills import GetRoleSkills
from .search_external_candidates_by_skills import SearchExternalCandidatesBySkills
from .shortlist_external_candidate import ShortlistExternalCandidate
from .get_job_applications import GetJobApplications
from .analyze_applicant_skill_fit import AnalyzeApplicantSkillFit
from .update_application_status import UpdateApplicationStatus
from .schedule_technical_interview import ScheduleTechnicalInterview
from .analyze_external_candidate_skill_fit import AnalyzeExternalCandidateSkillFit
from .recommend_skill_training import RecommendSkillTraining
from .get_user_id_from_name import GetUserIdFromName
from .get_course_id_by_name import GetCourseIdByName
from .get_today_date import GetTodayDate
from .list_user_goals import ListUserGoals
from .update_goal import UpdateGoal
from .get_team import GetTeam
from .add_team_member import AddTeamMember
from .enroll_in_course import EnrollInCourse
from .list_user_courses import ListUserCourses
from .update_user_course_progress import UpdateUserCourseProgress
from .add_mentorship_relationship import AddMentorshipRelationship
from .update_mentorship_relationship import UpdateMentorshipRelationship
from .list_user_mentorships import ListUserMentorships
from .schedule_mentorship_session import ScheduleMentorshipSession
from .get_job_id_by_title import GetJobIdByTitle
from .add_goal import AddGoal
from .find_mentors import FindMentors
from .get_user_profile import GetUserProfile

ALL_TOOLS = [
    GetJobPosting,
    GetRoleSkills,
    SearchExternalCandidatesBySkills,
    ShortlistExternalCandidate,
    GetJobApplications,
    AnalyzeApplicantSkillFit,
    UpdateApplicationStatus,
    ScheduleTechnicalInterview,
    AnalyzeExternalCandidateSkillFit,
    RecommendSkillTraining,
    GetUserIdFromName,
    GetCourseIdByName,
    GetTodayDate,
    ListUserGoals,
    UpdateGoal,
    GetTeam,
    AddTeamMember,
    EnrollInCourse,
    ListUserCourses,
    UpdateUserCourseProgress,
    AddMentorshipRelationship,
    UpdateMentorshipRelationship,
    ListUserMentorships,
    ScheduleMentorshipSession,
    GetJobIdByTitle,
    AddGoal,
    FindMentors,
    GetUserProfile,
]
