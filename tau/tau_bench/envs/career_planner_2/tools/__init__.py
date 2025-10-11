# Copyright Sierra

from .get_user_profile import GetUserProfile
from .get_skill_gap import GetSkillGap
from .get_performance_review import GetPerformanceReview
from .get_course_progress import GetCourseProgress
from .get_user_course_progress import GetUserCourseProgress
from .search_courses import SearchCourses
from .search_job_postings import SearchJobPostings
from .get_job_application import GetJobApplication
from .shortlist_candidate import ShortlistCandidate
from .update_application_status import UpdateApplicationStatus
from .assign_course import AssignCourse
from .link_mentor import LinkMentor
from .update_workflow_stage import UpdateWorkflowStage
from .set_performance_goal import SetPerformanceGoal
from .update_skill_proficiency import UpdateSkillProficiency
from .get_team_training_log import GetTeamTrainingLog
from .update_team_training_log import UpdateTeamTrainingLog
from .get_user_certification import GetUserCertification
from .update_user_certification import UpdateUserCertification
from .find_user_by_name import FindUserByName
from .find_course_by_name import FindCourseByName
from .find_job_by_title import FindJobByTitle
from .find_application import FindApplication
from .find_mentor import FindMentor
from .find_workflow import FindWorkflow
from .get_workflow_details import GetWorkflowDetails

ALL_TOOLS = [
    GetUserProfile,
    GetSkillGap,
    GetPerformanceReview,
    GetCourseProgress,
    GetUserCourseProgress,
    SearchCourses,
    SearchJobPostings,
    GetJobApplication,
    ShortlistCandidate,
    UpdateApplicationStatus,
    AssignCourse,
    LinkMentor,
    UpdateWorkflowStage,
    SetPerformanceGoal,
    UpdateSkillProficiency,
    GetTeamTrainingLog,
    UpdateTeamTrainingLog,
    GetUserCertification,
    UpdateUserCertification,
    FindUserByName,
    FindCourseByName,
    FindJobByTitle,
    FindApplication,
    FindMentor,
    FindWorkflow,
    GetWorkflowDetails,
]
