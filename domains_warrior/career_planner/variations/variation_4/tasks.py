from domains.dto import Task, Action

TASKS = [
    # Task 1: Enroll Jack Wang in Machine Learning Specialization and update his Data Science goal to 30% progress
    Task(
        annotator="0",
        user_id="res_01",
        instruction=(
            "Enroll Jack Wang in the Machine Learning Specialization course and update his Data Science leadership goal to 30% progress using today's date."
        ),
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Jack", "last_name": "Wang"}
            ),
            Action(
                "get_course_by_name", {"course_name": "Machine Learning Specialization"}
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U301", "course_id": "C1005", "enroll_date": "2025-07-04"},
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U301", "goal_description_keywords": "Data Science"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {"progress_percent": 30, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "User U301 enrolled in course C1005",
            "Goal G301-1 updated for user U301",
        ],
    ),
    # Task 2: Update Ava Nguyen's clinical analytics goal to 25% progress based on her Advanced Python course enrollment
    Task(
        annotator="0",
        user_id="res_02",
        instruction="Update Ava Nguyen's clinical analytics goal to 25% progress reflecting her Advanced Python course enrollment using today's date.",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Ava", "last_name": "Nguyen"}
            ),
            Action("get_course_by_name", {"course_name": "Advanced Python"}),
            Action(
                "enroll_in_course",
                {"user_id": "U302", "course_id": "C1001", "enroll_date": "2025-07-04"},
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U302", "goal_description_keywords": "clinical analytics"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {"progress_percent": 25, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "User U302 enrolled in course C1001",
            "Goal G302-1 updated for user U302",
        ],
    ),
    # Task 3: Update David Adams's DesignOps goal to 35% progress based on his UX Design Fundamentals completion
    Task(
        annotator="0",
        user_id="res_03",
        instruction=(
            "Mark David Adams as completed in UX Design Fundamentals course and update his DesignOps goal to 35% progress using today's date."
        ),
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "David", "last_name": "Adams"}
            ),
            Action("get_course_by_name", {"course_name": "UX Design Fundamentals"}),
            Action(
                "mark_course_completed",
                {
                    "user_id": "U304",
                    "course_id": "C1002",
                    "completion_date": "2025-07-04",
                },
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U304", "goal_description_keywords": "DesignOps"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U304",
                    "goal_id": "G304-1",
                    "updates": {"progress_percent": 35, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "Course C1002 marked completed for user U304",
            "Goal G304-1 updated for user U304",
        ],
    ),
    # Task 4: Add Web Accessibility Specialist certification for Chloe Scott with deterministic exam date
    Task(
        annotator="0",
        user_id="res_04",
        instruction="For Chloe Scott, add the 'Web Accessibility Specialist' certification from IAAP to her profile, with the exam scheduled 9 months from today. Then, create a new high-priority goal for her to 'Obtain the Web Accessibility Specialist certification'. Finally, send her a confirmation email with 'Your New Certification Goal' as a subject and 'This email confirms that the 'Web Accessibility Specialist' certification has been added to your profile. A new goal has been created to track your progress.' to the body.",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Chloe", "last_name": "Scott"}
            ),
            Action(
                "add_user_certification",
                {
                    "user_id": "U307",
                    "cert": {
                        "cert_name": "Web Accessibility Specialist",
                        "issuer": "IAAP",
                        "scheduled_exam_date": "2026-04-04",
                    },
                },
            ),
            Action(
                "add_user_goal",
                {
                    "user_id": "U307",
                    "goal": {
                        "goal_type": "Certification",
                        "goal_description": "Obtain the Web Accessibility Specialist certification",
                        "target_certification": "Web Accessibility Specialist",
                        "priority": "High",
                        "status": "Active",
                        "last_updated": "2025-07-04",
                    },
                },
            ),
            Action(
                "send_email_to_user",
                {
                    "user_id": "U307",
                    "subject": "Your New Certification Goal",
                    "body": "This email confirms that the 'Web Accessibility Specialist' certification has been added to your profile. A new goal has been created to track your progress.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 5: Update Logan Garcia's AWS Security goal to 20% progress with job market insights
    Task(
        annotator="0",
        user_id="res_05",
        instruction="First, check the job market demand for a 'Product Manager' to see if the demand score is high (above 8.0), then proceed with the following for Logan Garcia: enroll him in the 'Project Management Professional (PMP)' course to support his pivot to cloud-compliance. Then, update his 'cloud-compliance' goal to 25% progress and append to the description: 'Enrolled in PMP to build project leadership skills.' Finally, send him an email with the subject 'Your Cloud Compliance Career Path' and body 'Demand for roles like Product Manager is high. To support your goal, you have been enrolled in the PMP course. Your goal description has been updated to reflect this new step.'",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Logan", "last_name": "Garcia"}
            ),
            Action("get_job_market_insights", {"role": "Product Manager"}),
            Action(
                "get_course_by_name",
                {"course_name": "Project Management Professional (PMP)"},
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U303", "course_id": "C1004", "enroll_date": "2025-07-04"},
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U303", "goal_description_keywords": "cloud-compliance"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 25,
                        "goal_description": "Pass AWS Security Specialty exam to pivot toward cloud-compliance. Enrolled in PMP to build project leadership skills.",
                        "last_updated": "2025-07-04",
                    },
                },
            ),
            Action(
                "send_email_to_user",
                {
                    "user_id": "U303",
                    "subject": "Your Cloud Compliance Career Path",
                    "body": "Demand for roles like Product Manager is high. To support your goal, you have been enrolled in the PMP course. Your goal description has been updated to reflect this new step.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 6: Position Logan Garcia for compliance advancement with AWS certification and ML course enrollment
    Task(
        annotator="0",
        user_id="res_06",
        instruction=(
            "Add AWS Security Specialty certification for Logan Garcia with exam scheduled 10 months from today, enroll him in Machine Learning Specialization, and update his goal to 15% progress."
        ),
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Logan", "last_name": "Garcia"}
            ),
            Action(
                "add_user_certification",
                {
                    "user_id": "U303",
                    "cert": {
                        "cert_name": "AWS Security Specialty",
                        "issuer": "AWS",
                        "scheduled_exam_date": "2026-05-04",
                    },
                },
            ),
            Action(
                "get_course_by_name", {"course_name": "Machine Learning Specialization"}
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U303", "course_id": "C1005", "enroll_date": "2025-07-04"},
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U303", "goal_description_keywords": "AWS Security"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {"progress_percent": 15, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "User U303 enrolled in course C1005",
            "Goal G303-1 updated for user U303",
        ],
    ),
    # Task 7: Enroll Ava Nguyen in Agile Product Management and update her clinical analytics goal to 35% progress
    Task(
        annotator="0",
        user_id="res_07",
        instruction=(
            "Enroll Ava Nguyen in Agile Product Management course and update her clinical analytics goal to 35% progress using today's date."
        ),
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Ava", "last_name": "Nguyen"}
            ),
            Action("get_course_by_name", {"course_name": "Agile Product Management"}),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U302", "goal_description_keywords": "clinical-analytics"},
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U302", "course_id": "C1006", "enroll_date": "2025-07-04"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {"progress_percent": 35, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "User U302 enrolled in course C1006",
            "Goal G302-1 updated for user U302",
        ],
    ),
    # Task 8: Enroll Alexander Adams in UX Design Fundamentals and update his Staff SRE goal to 40% progress
    Task(
        annotator="0",
        user_id="res_08",
        instruction=(
            "Enroll Alexander Adams in UX Design Fundamentals course and update his Staff SRE goal to 40% progress using today's date."
        ),
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name",
                {"first_name": "Alexander", "last_name": "Adams"},
            ),
            Action("get_course_by_name", {"course_name": "UX Design Fundamentals"}),
            Action(
                "enroll_in_course",
                {"user_id": "U306", "course_id": "C1002", "enroll_date": "2025-07-04"},
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U306", "goal_description_keywords": "Staff SRE"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {"progress_percent": 40, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "User U306 enrolled in course C1002",
            "Goal G306-1 updated for user U306",
        ],
    ),
    # Task 9: Establish Logan Garcia's comprehensive credentials with MBA, AWS certification, and Climate Science course
    Task(
        annotator="0",
        user_id="res_09",
        instruction=(
            "Add Major Business Administration degree from University of Chicago for Logan Garcia with today's graduation date, add AWS Security Specialty certification with exam scheduled 10 months from today, enroll him in Climate Science & Policy course, and update his AWS Security goal to 15% progress."
        ),
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Logan", "last_name": "Garcia"}
            ),
            Action("generate_unique_edu_id", {"prefix": "ED"}),
            Action(
                "add_user_education",
                {
                    "user_id": "U303",
                    "education": {
                        "degree": "MBA",
                        "school": "University of Chicago",
                        "major": "Business Administration",
                        "graduation_date": "2025-07-04",
                    },
                },
            ),
            Action(
                "add_user_certification",
                {
                    "user_id": "U303",
                    "cert": {
                        "cert_name": "AWS Security Specialty",
                        "issuer": "AWS",
                        "scheduled_exam_date": "2026-05-04",
                    },
                },
            ),
            Action("get_course_by_name", {"course_name": "Climate Science & Policy"}),
            Action(
                "enroll_in_course",
                {"user_id": "U303", "course_id": "C1007", "enroll_date": "2025-07-04"},
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U303", "goal_description_keywords": "AWS Security"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 15,
                        "status": "Active",
                        "last_updated": "2025-07-04",
                    },
                },
            ),
        ],
        outputs=[
            "Education MBA added for user U303",
            "Certification AWS Security Specialty added for user U303",
            "User U303 enrolled in course C1007",
            "Goal G303-1 updated for user U303",
        ],
    ),
    # Task 10: Support Harper King's Product Marketing transition with mentorship and goal update
    Task(
        annotator="0",
        user_id="res_10",
        instruction="Establish a new mentorship for Harper King with Mentor M100, focusing on Product Marketing. Then, update her Product Marketing Specialist goal to 30% progress as of today.",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Harper", "last_name": "King"}
            ),
            Action(
                "assign_mentor",
                {
                    "mentee_id": "U305",
                    "mentor_id": "M100",
                    "focus_areas": ["Product Marketing"],
                    "start_date": "2025-07-04",
                },
            ),
            Action(
                "get_user_goals_by_type",
                {
                    "user_id": "U305",
                    "goal_description_keywords": "Product Marketing Specialist",
                },
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U305",
                    "goal_id": "G305-1",
                    "updates": {"progress_percent": 30, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[],
    ),
    # Task 11: Advance Jack Wang's ML expertise to 80% and log leadership skill gap analysis
    Task(
        annotator="0",
        user_id="res_11",
        instruction=(
            "Update Jack Wang's Machine Learning Specialization course progress to 80%, log a leadership skill gap analysis showing he needs Advanced level from current Intermediate, and update his Data Science goal to 50% progress."
        ),
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Jack", "last_name": "Wang"}
            ),
            Action(
                "get_course_by_name", {"course_name": "Machine Learning Specialization"}
            ),
            Action(
                "update_course_progress",
                {"user_id": "U301", "course_id": "C1005", "progress_percent": 80},
            ),
            Action("generate_unique_analysis_id", {"prefix": "SGA"}),
            Action(
                "log_soft_skill_gap",
                {
                    "user_id": "U301",
                    "analysis": {
                        "analysis_id": "SGA001",
                        "skill": "leadership",
                        "current_proficiency": "Intermediate",
                        "required_proficiency": "Advanced",
                        "recommended_courses": [],
                    },
                },
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U301", "goal_description_keywords": "Data Science"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {"progress_percent": 50, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "Course C1005 progress updated to 80% for user U301",
            "Skill gap analysis logged for user U301",
            "Goal G301-1 updated for user U301",
        ],
    ),
    # Task 12: Progress external candidate EXT001's Product Marketing application to interview stage
    Task(
        annotator="0",
        user_id="res_12",
        instruction=(
            "Log job application for external candidate EXT001 to Product Marketing Specialist role with skill match score 85, schedule interview for 6 days from today, and update application status to Interview Scheduled."
        ),
        actions=[
            Action("get_today_date", {}),
            Action("search_talent_network", {"candidate_id": "EXT001"}),
            Action("get_job_by_title", {"job_title": "Product Marketing Specialist"}),
            Action("generate_unique_application_id", {"prefix": "APP"}),
            Action(
                "log_job_application",
                {
                    "candidate_id": "EXT001",
                    "job_id": "J004",
                    "apply_date": "2025-07-04",
                    "skill_match_score": 85,
                },
            ),
            Action("get_job_market_insights", {"role": "Product Marketing Specialist"}),
            Action(
                "schedule_interview",
                {
                    "candidate_id": "EXT001",
                    "application_id": "APP001",
                    "interview_date": "2025-07-10",
                },
            ),
            Action(
                "update_application",
                {
                    "candidate_id": "EXT001",
                    "application_id": "APP001",
                    "updates": {
                        "status": "Interview Scheduled",
                        "last_updated": "2025-07-04",
                    },
                },
            ),
        ],
        outputs=[
            "Application logged for candidate EXT001",
            "Interview scheduled for 2025-07-10",
            "Application updated to Interview Scheduled",
        ],
    ),
    # Task 13: Complete Owen Walker's Climate Science course and log mentoring session with goal update
    Task(
        annotator="0",
        user_id="res_13",
        instruction="Mark Owen Walker's Climate Science & Policy course as completed today, log mentoring session with mentor M101 for today on policy expertise, and update his AR training goal to 65% progress.",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Owen", "last_name": "Walker"}
            ),
            Action("get_course_by_name", {"course_name": "Climate Science & Policy"}),
            Action(
                "log_course_completion",
                {
                    "user_id": "U309",
                    "course_id": "C1007",
                    "completion_date": "2025-07-04",
                },
            ),
            Action(
                "log_mentoring_session",
                {
                    "mentee_id": "U309",
                    "mentor_id": "M101",
                    "session_date": "2025-07-04",
                    "notes": "Policy expertise development",
                },
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U309", "goal_description_keywords": "AR"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U309",
                    "goal_id": "G309-1",
                    "updates": {"progress_percent": 65, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "Course C1007 marked completed for user U309",
            "Mentoring session logged for U309",
            "Goal G309-1 updated for user U309",
        ],
    ),
    # Task 14: Enroll Lucas Young in UX Design Fundamentals and update his Learning Analytics goal to 45% progress
    Task(
        annotator="0",
        user_id="res_14",
        instruction="Enroll Lucas Young in UX Design Fundamentals course and update his Learning Analytics goal to 45% progress using today's date.",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Lucas", "last_name": "Young"}
            ),
            Action("get_course_by_name", {"course_name": "UX Design Fundamentals"}),
            Action(
                "enroll_in_course",
                {"user_id": "U311", "course_id": "C1002", "enroll_date": "2025-07-04"},
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U311", "goal_description_keywords": "Learning Analytics"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U311",
                    "goal_id": "G311-1",
                    "updates": {"progress_percent": 45, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "User U311 enrolled in course C1002",
            "Course progress logged for U311",
            "Goal G311-1 updated for user U311",
        ],
    ),
    # Task 15: Enroll Henry Hassan in Data Visualization course and update his UX Writer goal to 15% progress
    Task(
        annotator="0",
        user_id="res_15",
        instruction=(
            "Enroll Henry Hassan in Data Visualization with Tableau course and update his UX Writer goal to 15% progress using today's date."
        ),
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Henry", "last_name": "Hassan"}
            ),
            Action("get_skill_gap_analysis", {"user_id": "U308"}),
            Action("compute_skill_gap_score", {"user_id": "U308"}),
            Action(
                "get_course_by_name", {"course_name": "Data Visualization with Tableau"}
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U308", "course_id": "C1003", "enroll_date": "2025-07-04"},
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U308", "goal_description_keywords": "UX Writer"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U308",
                    "goal_id": "G308-1",
                    "updates": {"progress_percent": 15, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "User U308 enrolled in course C1003",
            "Goal G308-1 updated for user U308",
        ],
    ),
    # Task 16: Update Ava Nguyen's clinical analytics goal to 40% progress
    Task(
        annotator="0",
        user_id="res_16",
        instruction="For Ava Nguyen, first check if her 'clinical-analytics' goal progress is below 50%. If it is, increment her progress by 15%. Also, enroll her in the 'Advanced Python' course to support this goal. Finally, send an email to her manager, Jack Wang, with the subject 'Progress Update for Ava Nguyen' and body 'This is to confirm that Ava Nguyen\\'s clinical analytics goal progress has been updated. She has also been enrolled in the Advanced Python course (C1001) to support her development.'",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Ava", "last_name": "Nguyen"}
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U302", "goal_description_keywords": "clinical-analytics"},
            ),
            Action(
                "check_goal_progress_threshold",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "threshold": 50,
                    "comparison": "below",
                },
            ),
            Action(
                "calculate_progress_increment", {"current_progress": 0, "increment": 15}
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {"progress_percent": 15, "last_updated": "2025-07-04"},
                },
            ),
            Action("get_course_by_name", {"course_name": "Advanced Python"}),
            Action(
                "enroll_in_course",
                {"user_id": "U302", "course_id": "C1001", "enroll_date": "2025-07-04"},
            ),
            Action("search_users", {"filters": {"user_id": "U302"}}),
            Action(
                "send_email_to_user",
                {
                    "user_id": "U301",
                    "subject": "Progress Update for Ava Nguyen",
                    "body": "This is to confirm that Ava Nguyen's clinical analytics goal progress has been updated. She has also been enrolled in the Advanced Python course (C1001) to support her development.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 17: Enroll Logan Garcia in Data Visualization course and update his AWS Security goal to 50% progress
    Task(
        annotator="0",
        user_id="res_17",
        instruction=(
            "Enroll Logan Garcia in Data Visualization with Tableau course and update his AWS Security goal to 50% progress using today's date."
        ),
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Logan", "last_name": "Garcia"}
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U303", "goal_description_keywords": "AWS Security"},
            ),
            Action(
                "check_goal_progress_threshold",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "threshold": 50,
                    "comparison": "below",
                },
            ),
            Action(
                "get_course_by_name", {"course_name": "Data Visualization with Tableau"}
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U303", "course_id": "C1003", "enroll_date": "2025-07-04"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {"progress_percent": 50, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "User U303 enrolled in course C1003",
            "Goal G303-1 updated for user U303",
        ],
    ),
    # Task 18: Verify Jack Wang's Advanced Python completion status and list his credentials
    Task(
        annotator="0",
        user_id="res_18",
        instruction="For Jack Wang, first check if his 'Advanced Python' course, and mark it as complete as of today. Then, find his goal related to becoming 'Director of Data Science' and increase its progress by 25%. Also, add the 'Advanced Python Certificate' from 'Coursera' to his profile. Finally, send him an email with the subject 'Course and Goal Progress Update' and body 'Congratulations on completing the Advanced Python course (C1001)! Your goal to become Director of Data Science has been updated, and the new certificate has been added to your profile.'",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Jack", "last_name": "Wang"}
            ),
            Action("get_course_by_name", {"course_name": "Advanced Python"}),
            Action(
                "check_course_completion_status",
                {"user_id": "U301", "course_id": "C1001"},
            ),
            Action(
                "mark_course_completed",
                {
                    "user_id": "U301",
                    "course_id": "C1001",
                    "completion_date": "2025-07-04",
                },
            ),
            Action(
                "get_user_goals_by_type",
                {
                    "user_id": "U301",
                    "goal_description_keywords": "Director of Data Science",
                },
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {"progress_percent": 50, "last_updated": "2025-07-04"},
                },
            ),
            Action(
                "add_user_certification",
                {
                    "user_id": "U301",
                    "cert": {
                        "cert_name": "Advanced Python Certificate",
                        "issuer": "Coursera",
                        "issue_date": "2025-07-04",
                    },
                },
            ),
            Action(
                "send_email_to_user",
                {
                    "user_id": "U301",
                    "subject": "Course and Goal Progress Update",
                    "body": "Congratulations on completing the Advanced Python course (C1001)! Your goal to become Director of Data Science has been updated, and the new certificate has been added to your profile.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 19: Enroll Ava Nguyen in ML and Agile courses, add ML certification with exam scheduled 14 months from today
    Task(
        annotator="0",
        user_id="res_19",
        instruction=(
            "Enroll Ava Nguyen in Machine Learning Specialization and Agile Product Management courses, add Machine Learning Professional certification from Coursera with exam scheduled 14 months from today, and update her clinical analytics goal to 30% progress."
        ),
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Ava", "last_name": "Nguyen"}
            ),
            Action("get_skill_gap_analysis", {"user_id": "U302"}),
            Action(
                "get_course_by_name", {"course_name": "Machine Learning Specialization"}
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U302", "course_id": "C1005", "enroll_date": "2025-07-04"},
            ),
            Action("get_course_by_name", {"course_name": "Agile Product Management"}),
            Action(
                "enroll_in_course",
                {"user_id": "U302", "course_id": "C1006", "enroll_date": "2025-07-04"},
            ),
            Action(
                "add_user_certification",
                {
                    "user_id": "U302",
                    "cert": {
                        "cert_name": "Machine Learning Professional",
                        "issuer": "Coursera",
                        "scheduled_exam_date": "2026-09-04",
                    },
                },
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U302", "goal_description_keywords": "clinical analytics"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {"progress_percent": 30, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "User U302 enrolled in course C1005",
            "User U302 enrolled in course C1006",
            "Certification Machine Learning Professional added for user U302",
            "Goal G302-1 updated for user U302",
        ],
    ),
    # Task 20: Add Chloe Scott's MA degree and Leadership Coach certification both dated today
    Task(
        annotator="0",
        user_id="res_20",
        instruction="Chloe Scott just graduated today with an MA in Organizational Leadership from Northwestern University and also received her Leadership Coach certification from ICF. First, add these two credentials to her profile. Based on these new qualifications, create a new high-priority 'Role Transition' goal for her with the description 'Transition to a Design Lead role within 18 months'. Then, assign Mentor M102 to her for 'Leadership' and 'Career Strategy' coaching. Finally, send an email to her manager, David Adams, with the subject 'Career Path Update for Chloe Scott' and body 'Chloe Scott has completed a new degree and certification in leadership. A new goal has been created to support her transition to a Design Lead role, and a Mentor has been assigned.'",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Chloe", "last_name": "Scott"}
            ),
            Action(
                "add_user_education",
                {
                    "user_id": "U307",
                    "education": {
                        "degree": "MA",
                        "field": "Organizational Leadership",
                        "institution": "Northwestern University",
                        "grad_year": 2025,
                    },
                },
            ),
            Action(
                "add_user_certification",
                {
                    "user_id": "U307",
                    "cert": {
                        "cert_name": "Leadership Coach",
                        "issuer": "ICF",
                        "issue_date": "2025-07-04",
                    },
                },
            ),
            Action(
                "add_user_goal",
                {
                    "user_id": "U307",
                    "goal": {
                        "goal_type": "Role Transition",
                        "goal_description": "Transition to a Design Lead role within 18 months",
                        "priority": "High",
                        "status": "Active",
                        "last_updated": "2025-07-04",
                    },
                },
            ),
            Action(
                "assign_mentor",
                {
                    "mentee_id": "U307",
                    "mentor_id": "M102",
                    "focus_areas": ["Leadership", "Career Strategy"],
                    "start_date": "2025-07-04",
                },
            ),
            Action("search_users", {"filters": {"user_id": "U307"}}),
            Action(
                "get_user_id_from_name", {"first_name": "David", "last_name": "Adams"}
            ),
            Action(
                "send_email_to_user",
                {
                    "user_id": "U304",
                    "subject": "Career Path Update for Chloe Scott",
                    "body": "Chloe Scott has completed a new degree and certification in leadership. A new goal has been created to support her transition to a Design Lead role, and a Mentor has been assigned.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 21: Add Jack Wang's MS degree, enroll in ML course, add cloud certification, and update goal to 60%
    Task(
        annotator="0",
        user_id="res_21",
        instruction="Add MS in Data Engineering from Stanford University for Jack Wang with today's graduation date, enroll him in Machine Learning Specialization course, add Google Cloud Professional Data Engineer certification from Google with exam scheduled 13 months from today, and update his Data Science goal to 60% progress.",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Jack", "last_name": "Wang"}
            ),
            Action("generate_unique_edu_id", {"prefix": "ED"}),
            Action(
                "add_user_education",
                {
                    "user_id": "U301",
                    "education": {
                        "degree": "M.S.",
                        "school": "Stanford University",
                        "major": "Data Engineering",
                        "graduation_date": "2025-07-04",
                    },
                },
            ),
            Action(
                "get_course_by_name", {"course_name": "Machine Learning Specialization"}
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U301", "course_id": "C1005", "enroll_date": "2025-07-04"},
            ),
            Action(
                "add_user_certification",
                {
                    "user_id": "U301",
                    "cert": {
                        "cert_name": "Google Cloud Professional Data Engineer",
                        "issuer": "Google",
                        "scheduled_exam_date": "2026-08-04",
                    },
                },
            ),
            Action("get_all_goals", {"user_id": "U301"}),
            Action(
                "update_goal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {"progress_percent": 60, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "Education M.S. added for user U301",
            "User U301 enrolled in course C1005",
            "Certification Google Cloud Professional Data Engineer added for user U301",
            "Goal G301-1 updated for user U301",
        ],
    ),
    # Task 22: Assign mentor M101 to David Adams and enroll him in Agile Product Management
    Task(
        annotator="0",
        user_id="res_22",
        instruction="Assign mentor M101 to David Adams with focus on Interaction Design starting today, enroll him in Agile Product Management course, and update his DesignOps goal to 45% progress.",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "David", "last_name": "Adams"}
            ),
            Action("get_all_goals", {"user_id": "U304"}),
            Action(
                "assign_mentor",
                {
                    "user_id": "U304",
                    "mentor_id": "M101",
                    "focus_areas": ["Interaction Design"],
                    "start_date": "2025-07-04",
                },
            ),
            Action("get_course_by_name", {"course_name": "Agile Product Management"}),
            Action(
                "enroll_in_course",
                {"user_id": "U304", "course_id": "C1006", "enroll_date": "2025-07-04"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U304",
                    "goal_id": "G304-1",
                    "updates": {"progress_percent": 45, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "Mentor M101 assigned to U304",
            "User U304 enrolled in course C1006",
            "Goal G304-1 updated for user U304",
        ],
    ),
    # Task 23: Complete Chloe Scott's change management training and add Scrum Master certification
    Task(
        annotator="0",
        user_id="res_23",
        instruction="Today is 2025-07-04 Mark Chloe Scott as completed in change management training session TS004 today, enroll her in the Agile Product Management course, add a Professional Scrum Master certification from Scrum.org with an exam scheduled on 2026-08-04, and update her Accessibility goal to 55% progress.",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Chloe", "last_name": "Scott"}
            ),
            Action(
                "update_team_training_log",
                {
                    "training_session_id": "TS004",
                    "user_id": "U307",
                    "status": "Completed",
                    "completion_date": "2025-07-04",
                    "skills_gained": ["Change Management"],
                },
            ),
            Action("get_course_by_name", {"course_name": "Agile Product Management"}),
            Action(
                "enroll_in_course",
                {"user_id": "U307", "course_id": "C1006", "enroll_date": "2025-07-04"},
            ),
            Action(
                "add_user_certification",
                {
                    "user_id": "U307",
                    "cert": {
                        "cert_name": "Professional Scrum Master",
                        "issuer": "Scrum.org",
                        "issue_date": None,
                        "expiry_date": None,
                        "scheduled_exam_date": "2026-08-04",
                    },
                },
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U307", "goal_description_keywords": "Accessibility"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "updates": {"progress_percent": 55, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[],
    ),
    # Task 24: Complete Henry Hassan's technical writing training, enroll in UX Design, add certification, and apply to UX Writer job
    Task(
        annotator="0",
        user_id="res_24",
        instruction="Mark Henry Hassan as completed in training session TS010 today, enroll him in the UX Design Fundamentals course, add a Technical Writing Professional certification from STC, and update his UX Writer goal to 35% progress.",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Henry", "last_name": "Hassan"}
            ),
            Action(
                "update_team_training_log",
                {
                    "training_session_id": "TS010",
                    "user_id": "U308",
                    "status": "Completed",
                    "completion_date": "2025-07-04",
                    "skills_gained": [],
                },
            ),
            Action("get_course_by_name", {"course_name": "UX Design Fundamentals"}),
            Action(
                "enroll_in_course",
                {"user_id": "U308", "course_id": "C1002", "enroll_date": "2025-07-04"},
            ),
            Action(
                "add_user_certification",
                {
                    "user_id": "U308",
                    "cert": {
                        "cert_name": "Technical Writing Professional",
                        "issuer": "STC",
                        "issue_date": "2025-07-04",
                    },
                },
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U308", "goal_description_keywords": "UX Writer"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U308",
                    "goal_id": "G308-1",
                    "updates": {"progress_percent": 35, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[],
    ),
    # Task 25: Enroll Jack Wang in Data Science Foundations course and update his goal to 50% progress
    Task(
        annotator="0",
        user_id="res_25",
        instruction="First, check the severity of Jack Wang's 'Machine Learning' skill gap. If the severity is 'High', enroll him in the 'Machine Learning Specialization' course. Then, find his goal related to becoming 'Director of Data Science' and update its progress to 50% and its metric to 'Complete course and publish 2 models'. Finally, notify his mentor, with the message: 'Action plan initiated for Jack Wang: Enrolled in Machine Learning Specialization to address a high-severity skill gap. Goal has been updated accordingly.'",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Jack", "last_name": "Wang"}
            ),
            Action(
                "check_skill_gap_severity",
                {"user_id": "U301", "skill": "Machine Learning"},
            ),
            Action(
                "get_course_by_name", {"course_name": "Machine Learning Specialization"}
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U301", "course_id": "C1005", "enroll_date": "2025-07-04"},
            ),
            Action(
                "get_user_goals_by_type",
                {
                    "user_id": "U301",
                    "goal_description_keywords": "Director of Data Science",
                },
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 50,
                        "metric": "Complete C1005 and publish 2 models",
                        "last_updated": "2025-07-04",
                    },
                },
            ),
            Action("list_user_mentors", {"user_id": "U301"}),
            Action(
                "update_mentorship_note",
                {
                    "mentor_id": "M102",
                    "mentee_id": "U301",
                    "note": "Action plan initiated for Jack Wang: Enrolled in Machine Learning Specialization to address a high-severity skill gap. Goal has been updated accordingly.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 26: Schedule Strategic Product Leadership training for Team T002 on specified date
    Task(
        annotator="0",
        user_id="res_26",
        instruction="First, check if the Product Design Team's training hours are below the 150-hour threshold. If they are, schedule the 'Project Management Professional (PMP)' training for them on August 1, 2025, and bulk-enroll the entire team as of today. Then, to align with this new training, update the priority of all 'Role Transition' goals for this team to 'High'. Finally, notify HR with the message: 'Product Design Team (T002) scheduled for PMP training (C1004) and enrolled. Related Role Transition goals have been prioritized.'",
        actions=[
            Action("get_today_date", {}),
            Action("search_teams", {"filters": {"team_name": "Product Design Team"}}),
            Action(
                "check_team_training_threshold",
                {"team_id": "T002", "threshold": 150, "comparison": "below"},
            ),
            Action(
                "get_course_by_name",
                {"course_name": "Project Management Professional (PMP)"},
            ),
            Action(
                "schedule_team_training",
                {"team_id": "T002", "course_id": "C1004", "session_date": "2025-08-01"},
            ),
            Action(
                "bulk_enroll_team",
                {"team_id": "T002", "course_id": "C1004", "enroll_date": "2025-07-04"},
            ),
            Action(
                "bulk_update_team_goals",
                {
                    "team_id": "T002",
                    "goal_type": "Role Transition",
                    "updates": {"priority": "High"},
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Product Design Team (T002) scheduled for PMP training (C1004) and enrolled. Related Role Transition goals have been prioritized."
                },
            ),
        ],
        outputs=[],
    ),
    # Task 27: Assess Henry Hassan's skills and enroll him in Data Visualization course with goal update
    Task(
        annotator="0",
        user_id="res_27",
        instruction=(
            "Assess Henry Hassan's skill gaps, enroll him in Data Visualization with Tableau course, and update his UX Writer goal to 20% progress using today's date."
        ),
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Henry", "last_name": "Hassan"}
            ),
            Action("get_skill_gap_analysis", {"user_id": "U308"}),
            Action("compute_skill_gap_score", {"user_id": "U308"}),
            Action(
                "get_course_by_name", {"course_name": "Data Visualization with Tableau"}
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U308", "goal_description_keywords": "UX Writer"},
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U308", "course_id": "C1003", "enroll_date": "2025-07-04"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U308",
                    "goal_id": "G308-1",
                    "updates": {"progress_percent": 20, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "User U308 enrolled in course C1003",
            "Goal G308-1 updated for user U308",
        ],
    ),
    # Task 28: Add Clinical Data Management certification for Ava Nguyen and create new certification goal
    Task(
        annotator="0",
        user_id="res_28",
        instruction="First, check if Ava Nguyen has any existing certification goals related to 'Clinical Data'. If not, add the 'Clinical Data Management Professional' certification from SCDM to her profile, with an exam scheduled 9 months from today. Then, create a new high-priority certification goal for her with the description 'Achieve Clinical Data Management Professional certification to deepen domain expertise', a timeframe of 12 months. Also, assign Mentor M100 to her for 'Python' and 'Career Strategy' coaching. Finally, notify her manager, Jack Wang, with the message: 'A new certification goal for Clinical Data Management has been created for Ava Nguyen. A Mentor has been assigned to support her.'",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Ava", "last_name": "Nguyen"}
            ),
            Action(
                "get_user_goals_by_type",
                {
                    "user_id": "U302",
                    "goal_type": "Certification",
                    "goal_description_keywords": "Clinical Data",
                },
            ),
            Action(
                "add_user_certification",
                {
                    "user_id": "U302",
                    "cert": {
                        "cert_name": "Clinical Data Management Professional",
                        "issuer": "SCDM",
                        "scheduled_exam_date": "2026-04-04",
                    },
                },
            ),
            Action(
                "add_user_goal",
                {
                    "user_id": "U302",
                    "goal": {
                        "goal_type": "Certification",
                        "goal_description": "Achieve Clinical Data Management Professional certification to deepen domain expertise",
                        "target_certification": "Clinical Data Management Professional",
                        "timeframe": "12 months",
                        "priority": "High",
                        "status": "Active",
                        "last_updated": "2025-07-04",
                    },
                },
            ),
            Action(
                "assign_mentor",
                {
                    "mentee_id": "U302",
                    "mentor_id": "M100",
                    "focus_areas": ["Python", "Career Strategy"],
                    "start_date": "2025-07-04",
                },
            ),
            Action("search_users", {"filters": {"user_id": "U302"}}),
            Action(
                "send_email_to_user",
                {
                    "user_id": "U301",
                    "subject": "New Development Plan for Ava Nguyen",
                    "body": "A new certification goal for Clinical Data Management has been created for Ava Nguyen. A Mentor has been assigned to support her.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 29: Check Owen Walker's course completion and goal status
    Task(
        annotator="0",
        user_id="res_29",
        instruction="For Owen Walker, first check his 'AR-based onboarding' goal to check if it's below 20% progress. Then, update its progress to 20%. Then, enroll him in the 'Project Management Professional (PMP)' course to help him manage this project. Finally, notify his manager, who is also Owen Walker, with the subject 'Goal Update and New Enrollment for Owen Walker' and body 'Owen Walker\\'s AR onboarding goal has been updated to 20% progress. He has also been enrolled in the PMP course to support this initiative.'",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Owen", "last_name": "Walker"}
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U309", "goal_description_keywords": "AR-based onboarding"},
            ),
            Action(
                "check_goal_progress_threshold",
                {
                    "user_id": "U309",
                    "goal_id": "G309-1",
                    "threshold": 20,
                    "comparison": "below",
                },
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U309",
                    "goal_id": "G309-1",
                    "updates": {"progress_percent": 20, "last_updated": "2025-07-04"},
                },
            ),
            Action(
                "get_course_by_name",
                {"course_name": "Project Management Professional (PMP)"},
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U309", "course_id": "C1004", "enroll_date": "2025-07-04"},
            ),
            Action("search_users", {"filters": {"user_id": "U309"}}),
            Action(
                "send_email_to_user",
                {
                    "user_id": "U309",
                    "subject": "Goal Update and New Enrollment for Owen Walker",
                    "body": "Owen Walker's AR onboarding goal has been updated to 20% progress. He has also been enrolled in the PMP course to support this initiative.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 30: Check mentor M101's capacity and workload
    Task(
        annotator="0",
        user_id="res_30",
        instruction="First, check if Mentor M102's current mentee load is below their capacity of 4. If it is, assign Harper Bennett to them for 'People Analytics' and 'Leadership' coaching. Then, create a new 'Role Transition' goal for Harper with the description 'Transition to People Analytics Lead' and enroll her in the 'Data Visualization with Tableau' course. Finally, send an email to Harper with the subject 'Your New Development Plan' and body 'You have been assigned to Mentor M102. A new goal has been created for your transition to People Analytics Lead, and you have been enrolled in the Data Visualization with Tableau course.'",
        actions=[
            Action("get_today_date", {}),
            Action("get_mentor", {"mentor_id": "M102"}),
            Action("compute_mentor_load", {"mentor_id": "M102"}),
            Action(
                "get_user_id_from_name",
                {"first_name": "Harper", "last_name": "Bennett"},
            ),
            Action(
                "assign_mentor",
                {
                    "mentee_id": "U310",
                    "mentor_id": "M102",
                    "focus_areas": ["People Analytics", "Leadership"],
                    "start_date": "2025-07-04",
                },
            ),
            Action(
                "add_user_goal",
                {
                    "user_id": "U310",
                    "goal": {
                        "goal_type": "Role Transition",
                        "goal_description": "Transition to People Analytics Lead",
                        "target_role": "People Analytics Lead",
                        "status": "Active",
                        "last_updated": "2025-07-04",
                    },
                },
            ),
            Action(
                "get_course_by_name", {"course_name": "Data Visualization with Tableau"}
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U310", "course_id": "C1003", "enroll_date": "2025-07-04"},
            ),
            Action(
                "send_email_to_user",
                {
                    "user_id": "U310",
                    "subject": "Your New Development Plan",
                    "body": "You have been assigned to Mentor M102. A new goal has been created for your transition to People Analytics Lead, and you have been enrolled in the Data Visualization with Tableau course.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 31: Schedule Data Science Foundations training for Team T001 and notify HR
    Task(
        annotator="0",
        user_id="res_31",
        instruction="First, check if the Data Analytics Team's average course progress is below 70%. If it is, schedule the 'Machine Learning Specialization' training for them on September 20, 2025. Then, bulk-enroll all team members in this new course. Also, update all of the team's 'Role Transition' goals to a 'High' priority. Finally, notify HR with the message: 'The Data Analytics Team (T001) has been scheduled for and enrolled in the Machine Learning Specialization (C1005) course. All related Role Transition goals have been prioritized.'",
        actions=[
            Action("search_teams", {"filters": {"team_name": "Data Analytics Team"}}),
            Action(
                "check_team_average_threshold",
                {"team_id": "T001", "threshold": 70, "comparison": "below"},
            ),
            Action(
                "get_course_by_name", {"course_name": "Machine Learning Specialization"}
            ),
            Action(
                "schedule_team_training",
                {"team_id": "T001", "course_id": "C1005", "session_date": "2025-09-20"},
            ),
            Action("get_today_date", {}),
            Action(
                "bulk_enroll_team",
                {"team_id": "T001", "course_id": "C1005", "enroll_date": "2025-07-04"},
            ),
            Action(
                "bulk_update_team_goals",
                {
                    "team_id": "T001",
                    "goal_type": "Role Transition",
                    "updates": {"priority": "High"},
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "The Data Analytics Team (T001) has been scheduled for and enrolled in the Machine Learning Specialization (C1005) course. All related Role Transition goals have been prioritized."
                },
            ),
        ],
        outputs=[],
    ),
    # Task 32: Enroll Chloe Scott in Data Visualization course and update her Accessibility goal to 80% progress
    Task(
        annotator="0",
        user_id="res_32",
        instruction=(
            "Assess Chloe Scott's current progress, get UX Designer market insights, enroll her in Data Visualization with Tableau course, and update her Accessibility goal to 80% progress using today's date."
        ),
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Chloe", "last_name": "Scott"}
            ),
            Action("compute_average_progress", {"user_id": "U307"}),
            Action("get_job_market_insights", {"role": "UX Designer"}),
            Action(
                "get_course_by_name", {"course_name": "Data Visualization with Tableau"}
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U307", "course_id": "C1003", "enroll_date": "2025-07-04"},
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U307", "goal_description_keywords": "Accessibility"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "updates": {"progress_percent": 80, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "User U307 enrolled in course C1003",
            "Goal G307-1 updated for user U307",
        ],
    ),
    # Task 33: Assess Jack Wang's readiness for Data Science Director role and update goal to 65% progress
    Task(
        annotator="0",
        user_id="res_33",
        instruction="First, assess Jack Wang's readiness score for his 'Director of Data Science' goal. If his score is above 60, enroll him in the 'Project Management Professional (PMP)' course to build leadership skills and update his goal's metric to include 'Complete PMP certification'. Finally, notify his mentor, M102, with the message: 'Jack Wang has met the readiness threshold for his Director goal. He has been enrolled in the PMP course and his goal has been updated.'",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Jack", "last_name": "Wang"}
            ),
            Action("get_skill_gap_analysis", {"user_id": "U301"}),
            Action(
                "check_readiness_threshold",
                {"user_id": "U301", "threshold": 60, "comparison": "above"},
            ),
            Action(
                "get_course_by_name",
                {"course_name": "Project Management Professional (PMP)"},
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U301", "course_id": "C1004", "enroll_date": "2025-07-04"},
            ),
            Action(
                "get_user_goals_by_type",
                {
                    "user_id": "U301",
                    "goal_description_keywords": "Director of Data Science",
                },
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "metric": "Complete PMP certification",
                        "last_updated": "2025-07-04",
                    },
                },
            ),
            Action("list_user_mentors", {"user_id": "U301"}),
            Action(
                "update_mentorship_note",
                {
                    "mentor_id": "M102",
                    "mentee_id": "U301",
                    "note": "Jack Wang has met the readiness threshold for his Director goal. He has been enrolled in the PMP course and his goal has been updated.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 34: Renew Alexander Adams's AWS certification and enroll him in PMP course with goal update
    Task(
        annotator="0",
        user_id="res_34",
        instruction=(
            "Check Alexander Adams's AWS certification expiry, add AWS Solutions Architect Associate renewal certification with exam scheduled 4 months from today, enroll him in Project Management Professional course, update his Staff SRE goal to 35% progress, and notify HR of the certification renewal."
        ),
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name",
                {"first_name": "Alexander", "last_name": "Adams"},
            ),
            Action("list_user_certifications", {"user_id": "U306"}),
            Action("compute_cert_expiry", {"user_id": "U306", "cert_id": "C7005"}),
            Action(
                "add_user_certification",
                {
                    "user_id": "U306",
                    "cert": {
                        "cert_name": "AWS Solutions Architect Associate – Renewal",
                        "issuer": "AWS",
                        "scheduled_exam_date": "2025-11-04",
                    },
                },
            ),
            Action(
                "get_course_by_name",
                {"course_name": "Project Management Professional (PMP)"},
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U306", "course_id": "C1004", "enroll_date": "2025-07-04"},
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U306", "goal_description_keywords": "Staff SRE"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {"progress_percent": 35, "last_updated": "2025-07-04"},
                },
            ),
            Action(
                "notify_hr", {"message": "AWS certification renewal scheduled for U306"}
            ),
        ],
        outputs=[
            "Certification AWS Solutions Architect Associate – Renewal added for user U306",
            "User U306 enrolled in course C1004",
            "Goal G306-1 updated for user U306",
        ],
    ),
    # Task 35: Check mentor M103's capacity and workload
    Task(
        annotator="0",
        user_id="res_35",
        instruction="First, check if Mentor M103 has a current active mentee load below their capacity of 2. Then, assign Ava Nguyen to them for 'Career Growth' and 'Skill Mastery' coaching as of today. After the assignment, create a new active 'Skill Mastery' goal for Ava with the description 'Master Python for clinical analytics with mentor guidance' and Python as a target skill to acquire. Finally, send an email to Ava with the subject 'New Mentor and Goal Assigned' and body 'You have been assigned to Mentor M103 for career growth. A new goal has been created to track your progress in mastering Python.'",
        actions=[
            Action("get_today_date", {}),
            Action("get_mentor", {"mentor_id": "M103"}),
            Action("compute_mentor_load", {"mentor_id": "M103"}),
            Action(
                "get_user_id_from_name", {"first_name": "Ava", "last_name": "Nguyen"}
            ),
            Action(
                "assign_mentor",
                {
                    "mentee_id": "U302",
                    "mentor_id": "M103",
                    "focus_areas": ["Career Growth", "Skill Mastery"],
                    "start_date": "2025-07-04",
                },
            ),
            Action(
                "add_user_goal",
                {
                    "user_id": "U302",
                    "goal": {
                        "goal_type": "Skill Mastery",
                        "goal_description": "Master Python for clinical analytics with mentor guidance",
                        "target_skills_to_acquire": ["Python"],
                        "status": "Active",
                    },
                },
            ),
            Action(
                "send_email_to_user",
                {
                    "user_id": "U302",
                    "subject": "New Mentor and Goal Assigned",
                    "body": "You have been assigned to Mentor M103 for career growth. A new goal has been created to track your progress in mastering Python.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 36: Comprehensive Team T004 optimization with training, mentorship, and skill development
    Task(
        annotator="0",
        user_id="res_36",
        instruction="For Harper King of the Marketing Team, schedule Project Management Professional (PMP) training for August 15, 2025. Then, assign Mentor M102 for coaching on Product Marketing and Leadership. Finally, create a skill development plan for Harper focusing on Data Analytics and Brand Positioning, and notify HR that the optimization plan is complete.",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Harper", "last_name": "King"}
            ),
            Action("search_teams", {"filters": {"team_name": "Marketing Team"}}),
            Action(
                "get_course_by_name",
                {"course_name": "Project Management Professional (PMP)"},
            ),
            Action(
                "schedule_team_training",
                {"team_id": "T004", "course_id": "C1004", "session_date": "2025-08-15"},
            ),
            Action(
                "assign_mentor",
                {
                    "mentee_id": "U305",
                    "mentor_id": "M102",
                    "focus_areas": ["Product Marketing", "Leadership"],
                    "start_date": "2025-07-04",
                },
            ),
            Action(
                "create_skill_development_plan",
                {
                    "user_id": "U305",
                    "focus_areas": ["Data Analytics", "Brand Positioning"],
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Team T004 performance optimization complete. Training scheduled for course C1004. Mentor M102 assigned to user U305. New skill plan created."
                },
            ),
        ],
        outputs=[],
    ),
    # Task 37: Bulk enroll Team T005 in PMP training and update Logan Garcia's goal
    Task(
        annotator="0",
        user_id="res_37",
        instruction="First, check if the Compliance Team's average course progress is below 50%. Then, bulk-enroll the team in the 'Project Management Professional (PMP)' course as of today. Then, to align with this new training, perform a bulk update on all 'Certification' goals for this team, setting their priority to 'High'. Finally, notify the team lead, Logan Garcia, with the subject 'Compliance Team Development Initiative' and body 'The Compliance team (T005) has been enrolled in PMP training (C1004) due to progress metrics. All related certification goals have been prioritized.'",
        actions=[
            Action("get_today_date", {}),
            Action("search_teams", {"filters": {"team_name": "Compliance Team"}}),
            Action(
                "check_team_average_threshold",
                {"team_id": "T005", "threshold": 50, "comparison": "below"},
            ),
            Action(
                "get_course_by_name",
                {"course_name": "Project Management Professional (PMP)"},
            ),
            Action(
                "bulk_enroll_team",
                {"team_id": "T005", "course_id": "C1004", "enroll_date": "2025-07-04"},
            ),
            Action(
                "bulk_update_team_goals",
                {
                    "team_id": "T005",
                    "goal_type": "Certification",
                    "updates": {"priority": "High"},
                },
            ),
            Action(
                "get_user_id_from_name", {"first_name": "Logan", "last_name": "Garcia"}
            ),
            Action(
                "send_email_to_user",
                {
                    "user_id": "U303",
                    "subject": "Compliance Team Development Initiative",
                    "body": "The Compliance team (T005) has been enrolled in PMP training (C1004) due to progress metrics. All related certification goals have been prioritized.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 38: Add HashiCorp Terraform certification for Alexander Adams and enroll in Data Visualization
    Task(
        annotator="0",
        user_id="res_38",
        instruction="Check Alexander Adams's Terraform skill gap severity, add a HashiCorp Terraform Associate certification with an issue date 2 months ago, enroll him in the Data Visualization with Tableau course, update his Staff SRE goal to 50% progress, and send a confirmation email with subject: 'Confirmation of your development plan updates' and body: 'This is to confirm the following updates to your career plan: A new certification (HashiCorp Terraform Associate) has been added. You have been enrolled in course C1003. Your goal G306-1 has been updated.'.",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name",
                {"first_name": "Alexander", "last_name": "Adams"},
            ),
            Action("get_skill_gap_analysis", {"user_id": "U306"}),
            Action(
                "check_skill_gap_severity", {"user_id": "U306", "skill": "Terraform"}
            ),
            Action(
                "add_user_certification",
                {
                    "user_id": "U306",
                    "cert": {
                        "cert_name": "HashiCorp Terraform Associate",
                        "issuer": "HashiCorp",
                        "issue_date": "2025-05-04",
                    },
                },
            ),
            Action(
                "get_course_by_name", {"course_name": "Data Visualization with Tableau"}
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U306", "course_id": "C1003", "enroll_date": "2025-07-04"},
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U306", "goal_description_keywords": "Staff SRE"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {"progress_percent": 50, "last_updated": "2025-07-04"},
                },
            ),
            Action(
                "send_email_to_user",
                {
                    "user_id": "U306",
                    "subject": "Confirmation of your development plan updates",
                    "body": "This is to confirm the following updates to your career plan: A new certification (HashiCorp Terraform Associate) has been added. You have been enrolled in course C1003. Your goal G306-1 has been updated.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 39: Assess Henry Hassan's readiness and enroll in UX Design Fundamentals with goal update
    Task(
        annotator="0",
        user_id="res_39",
        instruction=(
            "Assess Henry Hassan's skill gaps and readiness against 85% threshold, enroll him in UX Design Fundamentals course, and update his UX Writer goal to 25% progress using today's date."
        ),
        actions=[
            Action(
                "get_user_id_from_name", {"first_name": "Henry", "last_name": "Hassan"}
            ),
            Action("get_skill_gap_analysis", {"user_id": "U308"}),
            Action("get_today_date", {}),
            Action("compute_skill_gap_score", {"user_id": "U308"}),
            Action(
                "check_readiness_threshold",
                {"user_id": "U308", "threshold": 85, "comparison": "below"},
            ),
            Action("get_course_by_name", {"course_name": "UX Design Fundamentals"}),
            Action(
                "enroll_in_course",
                {"user_id": "U308", "course_id": "C1002", "enroll_date": "2025-07-04"},
            ),
            Action(
                "get_user_goals_by_type",
                {"user_id": "U308", "goal_description_keywords": "UX Writer"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U308",
                    "goal_id": "G308-1",
                    "updates": {"progress_percent": 25, "last_updated": "2025-07-04"},
                },
            ),
        ],
        outputs=[
            "User U308 enrolled in course C1002",
            "Goal G308-1 updated for user U308",
        ],
    ),
    # Task 40: Enroll Owen Walker in Data Visualization course for AR training module development
    Task(
        annotator="0",
        user_id="res_40",
        instruction="For Owen Walker, first check if he is already enrolled in the 'Data Visualization with Tableau' course. Then, enroll him as of today. Then, create a new 'Skill Mastery' goal for him with the description 'Master Tableau for L&D reporting' and a timeframe of 6 months. Finally, send an email to his manager, who is also Owen Walker, with the subject 'New Development Action for Owen Walker' and body 'Owen Walker has been enrolled in the Data Visualization with Tableau course and a new supporting goal has been created.'",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Owen", "last_name": "Walker"}
            ),
            Action(
                "get_course_by_name", {"course_name": "Data Visualization with Tableau"}
            ),
            Action("list_user_courses", {"user_id": "U309"}),
            Action(
                "enroll_in_course",
                {"user_id": "U309", "course_id": "C1003", "enroll_date": "2025-07-04"},
            ),
            Action(
                "add_user_goal",
                {
                    "user_id": "U309",
                    "goal": {
                        "goal_type": "Skill Mastery",
                        "goal_description": "Master Tableau for L&D reporting",
                        "target_skills_to_acquire": ["Tableau"],
                        "timeframe": "6 months",
                        "status": "Active",
                        "last_updated": "2025-07-04",
                    },
                },
            ),
            Action("search_users", {"filters": {"user_id": "U309"}}),
            Action(
                "send_email_to_user",
                {
                    "user_id": "U309",
                    "subject": "New Development Action for Owen Walker",
                    "body": "Owen Walker has been enrolled in the Data Visualization with Tableau course and a new supporting goal has been created.",
                },
            ),
        ],
        outputs=[],
    ),
]
