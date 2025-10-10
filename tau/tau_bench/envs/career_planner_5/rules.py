RULES = [
    """
# Employee Advancement Policy

## # Handling Dates
- All enrollment dates, goal updates, and relationship modifications must use the current date from get_today_date()
- Session scheduling must use deterministic date calculations based on current date plus standard intervals

## # Policy for Mentorship Assignments
- Mentor capacity is determined by compute_mentor_load() calls
- Available mentors (M100, M101, M102, M103) should be checked for capacity before assignment
- Existing mentorship relationships (MR001-MR009) should be referenced when updating or scheduling
- get_mentor() reports all mentees (including active and completed), while compute_mentor_load correctly returns all active mentees of a mentor.

## # Policy for Enrolling in Courses
- Course selections must be based on skill gap analysis recommendations when available
- Standard courses available: C1001 (Python), C1002 (UX), C1003 (Tableau), C1004 (Leadership), C1005 (ML), C1006 (Agile)
- Course enrollment requires user_id, course_id, and enroll_date

## # Policy for Managing Goals
- Existing goals (G301-1, G302-1, G303-1) should be referenced and updated rather than creating duplicates
- New goals require unique goal_id following pattern G[user_number]-[sequence]
- Goal updates must include last_updated field with current date and a status update

## # Policy for Team Assignments
- Teams T001 (Analytics), T002 (Product Design), T003 (Engineering) are available for assignment
- Team membership changes require verification of existing team structure

## # Human Resources Process Guidelines
- Existing workflows (WF001, WF002) should be referenced for updates
- Workflow stage progression follows: Skills Assessment → Development Plan → Training Assignment → Final Assessment
- Status updates require current_stage, status, and last_updated fields

## # Alerting Guidelines
- HR notifications use notify_hr with standardized message format
- User notifications use notify_user with clear, actionable message content
- Messages should be concise and outcome-focused

## # Policy for Data Integrity
- All user_id references must use existing users (U301-U312)
- Skill gap analysis references must use existing analysis_id or user_id
- Certification additions require cert_id, cert_name, issuer, and scheduled_exam_date
"""
]
