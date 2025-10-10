# Copyright Sierra

from .get_today_date import get_today_date
from .search_users import search_users
from .get_course import get_course
from .enroll_in_course import enroll_in_course
from .get_goal import get_goal
from .update_goal import update_goal
from .get_job_market_insights import get_job_market_insights
from .add_user_certification import add_user_certification
from .list_user_certifications import list_user_certifications
from .list_user_courses import list_user_courses
from .add_user_education import add_user_education
from .log_course_completion import log_course_completion
from .log_mentoring_session import log_mentoring_session
from .list_mentoring_sessions import list_mentoring_sessions
from .audit_goal_status import audit_goal_status
from .log_course_progress import log_course_progress
from .recommend_learning_path import recommend_learning_path
from .conditional_progress_update import conditional_progress_update
from .get_team import get_team
from .get_team_members import get_team_members
from .log_team_training import log_team_training
from .list_team_training import list_team_training
from .update_user_training_progress import update_user_training_progress
from .get_mentor import get_mentor
from .schedule_mentorship_session import schedule_mentorship_session
from .list_user_mentorships import list_user_mentorships
from .get_soft_skills import get_soft_skills
from .update_course_progress import update_course_progress
from .log_soft_skill_gap import log_soft_skill_gap
from .list_soft_skill_gap import list_soft_skill_gap
from .analyze_skill_gap import analyze_skill_gap
from .list_user_education import list_user_education
from .search_talent_network import search_talent_network
from .log_job_application import log_job_application
from .update_application import update_application
from .schedule_interview import schedule_interview
from .list_applications import list_applications
from .list_job_postings import list_job_postings
from .reassign_mentor import reassign_mentor
from .conditional_enroll_or_list import conditional_enroll_or_list
from .get_user_course_progress import get_user_course_progress
from .generate_unique_cert_id import generate_unique_cert_id
from .generate_unique_edu_id import generate_unique_edu_id
from .generate_unique_application_id import generate_unique_application_id
from .generate_unique_relationship_id import generate_unique_relationship_id
from .generate_unique_analysis_id import generate_unique_analysis_id
from .check_goal_progress_threshold import check_goal_progress_threshold
from .calculate_progress_increment import calculate_progress_increment
from .get_job_posting import get_job_posting
from .add_job_application import add_job_application
from .list_user_applications import list_user_applications
from .search_job_postings import search_job_postings
from .get_skill_gap_analysis import get_skill_gap_analysis
from .perform_soft_skill_gap_analysis import perform_soft_skill_gap_analysis
from .compute_skill_gap_score import compute_skill_gap_score
from .assign_mentor import assign_mentor
from .list_user_mentors import list_user_mentors
from .list_mentorship_relationships import list_mentorship_relationships
from .compute_mentor_load import compute_mentor_load
from .update_mentorship_note import update_mentorship_note
from .search_teams import search_teams
from .list_team_members import list_team_members
from .check_course_completion_status import check_course_completion_status
from .mark_course_completed import mark_course_completed
from .compute_average_progress import compute_average_progress
from .notify_hr import notify_hr
from .send_email_to_user import send_email_to_user
from .get_team_training_log import get_team_training_log
from .update_team_training_log import update_team_training_log
from .list_user_training_sessions import list_user_training_sessions
from .schedule_team_training import schedule_team_training
from .add_team_training_session import add_team_training_session
from .compute_team_training_hours import compute_team_training_hours
from .compute_team_average_progress import compute_team_average_progress
from .bulk_enroll_course import bulk_enroll_course
from .bulk_update_goals import bulk_update_goals
from .compute_cert_expiry import compute_cert_expiry
from .get_user_id_from_name import get_user_id_from_name
from .bulk_check_team_courses import bulk_check_team_courses
from .bulk_enroll_team import bulk_enroll_team
from .bulk_update_team_goals import bulk_update_team_goals
from .check_readiness_threshold import check_readiness_threshold
from .check_team_average_threshold import check_team_average_threshold
from .check_team_training_threshold import check_team_training_threshold
from .get_user_goals_by_type import get_user_goals_by_type
from .get_course_by_name import get_course_by_name
from .get_job_by_title import get_job_by_title
from .get_all_goals import get_all_goals
from .generate_unique_goal_id import generate_unique_goal_id
from .add_user_goal import add_user_goal
from .check_user_training_completion import check_user_training_completion
from .assess_team_mentorship_coverage import assess_team_mentorship_coverage
from .evaluate_team_training_status import evaluate_team_training_status
from .check_skill_gap_severity import check_skill_gap_severity
from .create_skill_development_plan import create_skill_development_plan

ALL_TOOLS = [
    get_today_date,
    search_users,
    get_course,
    enroll_in_course,
    get_goal,
    update_goal,
    get_job_market_insights,
    add_user_certification,
    list_user_certifications,
    list_user_courses,
    add_user_education,
    log_course_completion,
    log_mentoring_session,
    list_mentoring_sessions,
    audit_goal_status,
    log_course_progress,
    recommend_learning_path,
    conditional_progress_update,
    get_team,
    get_team_members,
    log_team_training,
    list_team_training,
    update_user_training_progress,
    get_mentor,
    schedule_mentorship_session,
    list_user_mentorships,
    get_soft_skills,
    update_course_progress,
    log_soft_skill_gap,
    list_soft_skill_gap,
    analyze_skill_gap,
    list_user_education,
    search_talent_network,
    log_job_application,
    update_application,
    schedule_interview,
    list_applications,
    list_job_postings,
    reassign_mentor,
    conditional_enroll_or_list,
    get_user_course_progress,
    generate_unique_cert_id,
    generate_unique_edu_id,
    generate_unique_application_id,
    generate_unique_relationship_id,
    generate_unique_analysis_id,
    check_goal_progress_threshold,
    calculate_progress_increment,
    get_job_posting,
    add_job_application,
    list_user_applications,
    search_job_postings,
    get_skill_gap_analysis,
    perform_soft_skill_gap_analysis,
    compute_skill_gap_score,
    assign_mentor,
    list_user_mentors,
    list_mentorship_relationships,
    compute_mentor_load,
    update_mentorship_note,
    search_teams,
    list_team_members,
    check_course_completion_status,
    mark_course_completed,
    compute_average_progress,
    notify_hr,
    send_email_to_user,
    get_team_training_log,
    update_team_training_log,
    list_user_training_sessions,
    schedule_team_training,
    add_team_training_session,
    compute_team_training_hours,
    compute_team_average_progress,
    bulk_enroll_course,
    bulk_update_goals,
    compute_cert_expiry,
    get_user_id_from_name,
    bulk_check_team_courses,
    bulk_enroll_team,
    bulk_update_team_goals,
    check_readiness_threshold,
    check_team_average_threshold,
    check_team_training_threshold,
    get_user_goals_by_type,
    get_course_by_name,
    get_job_by_title,
    get_all_goals,
    generate_unique_goal_id,
    add_user_goal,
    check_user_training_completion,
    assess_team_mentorship_coverage,
    evaluate_team_training_status,
    check_skill_gap_severity,
    create_skill_development_plan,
]
