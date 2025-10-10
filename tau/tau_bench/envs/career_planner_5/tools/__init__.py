# Copyright owned by Sierra

from .get_today_date import get_today_date
from .get_user_id_from_name import get_user_id_from_name
from .get_course_id_by_name import get_course_id_by_name
from .get_goal_id_by_description import get_goal_id_by_description
from .get_team_id_by_name import get_team_id_by_name
from .find_hr_workflow_for_user import find_hr_workflow_for_user
from .search_users import search_users
from .get_course import get_course
from .enroll_in_course import enroll_in_course
from .list_user_courses import list_user_courses
from .get_user_course_progress import get_user_course_progress
from .update_user_course_progress import update_user_course_progress
from .compute_average_progress import compute_average_progress
from .list_user_goals import list_user_goals
from .get_goal import get_goal
from .add_goal import add_goal
from .update_goal import update_goal
from .get_team import get_team
from .add_team_member import add_team_member
from .get_skill_gap_analysis import get_skill_gap_analysis
from .list_user_mentorships import list_user_mentorships
from .add_mentorship_relationship import add_mentorship_relationship
from .update_mentorship_relationship import update_mentorship_relationship
from .schedule_mentorship_session import schedule_mentorship_session
from .compute_mentor_load import compute_mentor_load
from .get_hr_workflow import get_hr_workflow
from .update_hr_workflow import update_hr_workflow
from .add_user_certification import add_user_certification
from .notify_hr import notify_hr
from .notify_user import notify_user

ALL_TOOLS = [
    get_today_date,
    get_user_id_from_name,
    get_course_id_by_name,
    get_goal_id_by_description,
    get_team_id_by_name,
    find_hr_workflow_for_user,
    search_users,
    get_course,
    enroll_in_course,
    list_user_courses,
    get_user_course_progress,
    update_user_course_progress,
    compute_average_progress,
    list_user_goals,
    get_goal,
    add_goal,
    update_goal,
    get_team,
    add_team_member,
    get_skill_gap_analysis,
    list_user_mentorships,
    add_mentorship_relationship,
    update_mentorship_relationship,
    schedule_mentorship_session,
    compute_mentor_load,
    get_hr_workflow,
    update_hr_workflow,
    add_user_certification,
    notify_hr,
    notify_user,
]
