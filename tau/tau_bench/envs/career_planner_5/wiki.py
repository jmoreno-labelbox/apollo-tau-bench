WIKI = """
"""
# Career Development Policy

## Date Management
- All enrollment dates, goal updates, and relationship modifications must use the current date from get_today_date()
- Session scheduling must use deterministic date calculations based on current date plus standard intervals

## Mentorship Assignment Policy
- Mentor capacity is determined by compute_mentor_load() calls
- Available mentors (M100, M101, M102, M103) should be checked for capacity before assignment
- Existing mentorship relationships (MR001-MR009) should be referenced when updating or scheduling
- get_mentor() reports all mentees (including active and completed), while compute_mentor_load correctly returns all active mentees of a mentor.

## Course Enrollment Policy
- Course selections must be based on skill gap analysis recommendations when available
- Standard courses available: C1001 (Python), C1002 (UX), C1003 (Tableau), C1004 (Leadership), C1005 (ML), C1006 (Agile)
- Course enrollment requires user_id, course_id, and enroll_date

## Goal Management Policy
- Existing goals (G301-1, G302-1, G303-1) should be referenced and updated rather than creating duplicates
- New goals require unique goal_id following pattern G[user_number
"""
