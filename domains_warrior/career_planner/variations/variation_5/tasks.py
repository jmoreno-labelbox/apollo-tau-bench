from domains.dto import Task, Action

TASKS = [
    # Task 1: Basic course enrollment with skill validation (Complexity: 8)
    Task(
        annotator="0",
        user_id="res_01",
        instruction="You need Jack Wang enrolled in Machine Learning course with his promotion goal updated to reflect the enrollment.",
        actions=[
            Action("get_today_date", {}),
            Action(
                "get_user_id_from_name", {"first_name": "Jack", "last_name": "Wang"}
            ),
            Action("search_users", {"filters": {"user_id": "U301"}}),
            Action(
                "enroll_in_course",
                {"user_id": "U301", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action("get_goal", {"user_id": "U301", "goal_id": "G301-1"}),
            Action(
                "update_goal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {"last_updated": "2025-10-02"},
                },
            ),
            Action(
                "notify_hr",
                {"message": "U301 machine learning course enrollment completed"},
            ),
        ],
        outputs=[
            "User U301 enrolled in course C1005",
            "Goal G301-1 updated for user U301",
            '"notified": "HR"',
        ],
    ),
    # Task 2: Team assignment with basic mentorship setup (Complexity: 9)
    Task(
        annotator="pra-01",
        user_id="res_02",
        instruction="Add Harper King to the Analytics Team and establish a mentorship relationship with mentor M100, with a focus on analytics and career growth. Then notify him with the following message: 'Welcome to the Analytics Team! You have been assigned a mentor to support your career growth.', and then notify hr with the following message: 'Harper King has been added to the Analytics Team and assigned mentor.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Harper", "last_name": "King"},
            ),
            Action("add_team_member", {"team_id": "T001", "user_id": "U305"}),
            Action("compute_mentor_load", {"mentor_id": "M100"}),
            Action("get_today_date", {}),
            Action(
                "add_mentorship_relationship",
                {
                    "mentor_id": "M100",
                    "mentee_id": "U305",
                    "status": "Active",
                    "start_date": "2025-10-02",
                    "focus_areas": ["Analytics", "Career Growth"],
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U305",
                    "message": "Welcome to the Analytics Team! You have been assigned a mentor to support your career growth.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Harper King has been added to the Analytics Team and assigned mentor."
                },
            ),
        ],
        outputs=[
            "User U305 added to team T001",
            "Mentorship relationship MR011 created",
            "notified_user",
            "notified",
        ],
    ),
    # Task 3: Skills assessment with course recommendation (Complexity: 10)
    Task(
        annotator="0",
        user_id="res_03",
        instruction="Enroll Chloe Scott in a foundational UX course to enhance her competency and update her development goal saying 'Active - Course Assigned'. Then notify her with the following message: 'You have been enrolled in the 'UX Design Fundamentals' course to support your development goals.', and then notify hr with the following message: 'Chloe Scott has been enrolled in course UX Design Fundamentals'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U307", "course_id": "C1002", "enroll_date": "2025-10-02"},
            ),
            Action("list_user_goals", {"user_id": "U307"}),
            Action(
                "update_goal",
                {
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "updates": {
                        "status": "Active - Course Assigned",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action("get_course", {"course_id": "C1002"}),
            Action(
                "notify_user",
                {
                    "user_id": "U307",
                    "message": "You have been enrolled in the 'UX Design Fundamentals' course to support your development goals.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Chloe Scott has been enrolled in course UX Design Fundamentals."
                },
            ),
        ],
        outputs=[
            "User U307 enrolled in course C1002",
            "Goal G307-1 updated for user U307",
            "notified_user",
            "notified",
        ],
    ),
    # Task 4: Mentorship session scheduling with capacity check (Complexity: 8)
    Task(
        annotator="0",
        user_id="res_04",
        instruction="Schedule the next mentorship session for David Adams two weeks from today. Notify him with the message: 'Your next mentorship session has been scheduled. Please check your calendar for details.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "David", "last_name": "Adams"},
            ),
            Action("list_user_mentorships", {"user_id": "U304"}),
            Action("get_today_date", {}),
            Action(
                "schedule_mentorship_session",
                {"relationship_id": "MR002", "session_date": "2025-10-16"},
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR002",
                    "updates": {"next_session_date": "2025-10-16"},
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U304",
                    "message": "Your next mentorship session has been scheduled. Please check your calendar for details.",
                },
            ),
        ],
        outputs=[
            '"scheduled_for": "2025-10-16"',
            "relationship MR002 updated",
            "notified_user",
        ],
    ),
    # Task 5: Certification tracking with goal alignment (Complexity: 11)
    Task(
        annotator="0",
        user_id="res_05",
        instruction="Register the 'AWS Security Specialty' certification from 'AWS' for Logan Garcia, using a new certification ID 'C7011' and scheduling the exam 60 days from today. Update his certification goal to reflect 10% progress. Notify HR with the message: 'Logan Garcia (U303) has registered for the AWS Security Specialty exam.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action("get_today_date", {}),
            Action(
                "add_user_certification",
                {
                    "user_id": "U303",
                    "cert": {
                        "cert_id": "C7011",
                        "cert_name": "AWS Security Specialty",
                        "issuer": "AWS",
                        "issue_date": None,
                        "scheduled_exam_date": "2025-12-01",
                    },
                },
            ),
            Action("list_user_goals", {"user_id": "U303"}),
            Action(
                "update_goal",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 10,
                        "status": "In Progress - Exam Scheduled",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Logan Garcia (U303) has registered for the AWS Security Specialty exam."
                },
            ),
        ],
        outputs=[
            "Certification AWS Security Specialty added for user U303",
            "Goal G303-1 updated for user U303",
            '"notified": "HR"',
        ],
    ),
    # Task 6: Course progress update with goal synchronization (Complexity: 9)
    Task(
        annotator="0",
        user_id="res_06",
        instruction="Update Ava Nguyen's progress for her 'Python' course to 50%. Also, update the 'last_updated' field on her career goal related to 'Python'. Finally, notify her with the message: 'Your progress on the Python course has been updated to 50%. Keep up the great work!' and notify HR with the message: 'Ava Nguyen has reached a 50% progress milestone in her Python course, supporting her development goal.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action("get_course_id_by_name", {"course_name": "Python"}),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U302", "keyword": "Python"},
            ),
            Action("get_today_date", {}),
            Action(
                "update_user_course_progress",
                {
                    "user_id": "U302",
                    "course_id": "C1001",
                    "updates": {
                        "current_progress_percent": 50,
                    },
                },
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {"last_updated": "2025-10-02"},
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U302",
                    "message": "Your progress on the Python course has been updated to 50%. Keep up the great work!",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Ava Nguyen has reached a 50% progress milestone in her Python course, supporting her development goal."
                },
            ),
        ],
        outputs=[
            "course progress updated",
            "Goal G302-1 updated for user U302",
            "notified_user",
            "notified",
        ],
    ),
    # Task 7: Workflow stage advancement with validation (Complexity: 10)
    Task(
        annotator="0",
        user_id="res_07",
        instruction="Advance Ava Nguyen's promotion workflow to the 'Development Plan' stage. Identify the designated planner for this stage, find their full name, and update the workflow notes to reflect their assignment. Enroll Ava in the course recommended by the workflow. Also, update her career goal related to 'Python' by appending to the description: 'Development plan now active under WF001.'. Notify Ava with the message: 'Your promotion workflow has advanced to the Development Plan stage and you have been enrolled in required training.' and notify the assigned planner with the message: 'You have been assigned as the planner for Ava Nguyen's development plan in promotion workflow WF001.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action("find_hr_workflow_for_user", {"user_id": "U302"}),
            Action("get_hr_workflow", {"workflow_id": "WF001"}),
            Action("search_users", {"filters": {"user_id": "U310"}}),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U302", "keyword": "Python"},
            ),
            Action("get_goal", {"user_id": "U302", "goal_id": "G302-1"}),
            Action("get_today_date", {}),
            Action(
                "update_hr_workflow",
                {
                    "workflow_id": "WF001",
                    "updates": {
                        "current_stage": "Development Plan",
                        "status": "In Progress",
                        "notes_append": "Plan assigned to planner Harper Bennett.",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U302", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "goal_description": "Add Python to clinical-analytics toolkit and deliver an internal POC to demonstrate leadership in data-driven decision making. Development plan now active under WF001.",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U302",
                    "message": "Your promotion workflow has advanced to the Development Plan stage and you have been enrolled in required training.",
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U310",
                    "message": "You have been assigned as the planner for Ava Nguyen's development plan in promotion workflow WF001.",
                },
            ),
        ],
        outputs=[
            "workflow WF001 updated",
            "User U302 enrolled in course C1005",
            "Goal G302-1 updated for user U302",
            "notified_user",
            "notified_user",
        ],
    ),
    # Task 8: Dual competency development with mentorship enhancement (Complexity: 12)
    Task(
        annotator="0",
        user_id="res_08",
        instruction="First, verify that Alexander Adams meets the '3+ years PM experience' prerequisite for the 'Project Management Professional (PMP)' course. If he does, enroll him. Then, update his goal related to 'Staff SRE' to add the note: 'PMP course enrolled to support leadership path.' Also, update his mentorship relationship by adding 'Strategic Leadership' to the existing focus areas. Finally, notify both Alexander and his manager about the enrollment with the message: 'Alexander Adams has been enrolled in the PMP course to support his strategic development goals.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Alexander", "last_name": "Adams"},
            ),
            Action("search_users", {"filters": {"user_id": "U306"}}),
            Action(
                "get_course_id_by_name",
                {"course_name": "Project Management Professional (PMP)"},
            ),
            Action("get_course", {"course_id": "C1004"}),
            Action("list_user_goals", {"user_id": "U306"}),
            Action("list_user_mentorships", {"user_id": "U306"}),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U306", "course_id": "C1004", "enroll_date": "2025-10-02"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {
                        "goal_description": "Advance to Staff Site Reliability Engineer and lead reliability roadmap. PMP course enrolled to support leadership path.",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR004",
                    "updates": {
                        "focus_areas": [
                            "Site Reliability Engineering",
                            "Leadership",
                            "Infrastructure",
                            "Strategic Leadership",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U306",
                    "message": "Alexander Adams has been enrolled in the PMP course to support his strategic development goals.",
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U312",
                    "message": "Alexander Adams has been enrolled in the PMP course to support his strategic development goals.",
                },
            ),
        ],
        outputs=[
            "User U306 enrolled in course C1004",
            "Goal G306-1 updated for user U306",
            "relationship MR004 updated",
            "notified_user",
            "notified_user",
        ],
    ),
    # Task 9: Data visualization competency with specialized training (Complexity: 11)
    Task(
        annotator="0",
        user_id="res_09",
        instruction="To support Logan Garcia's development, enroll him in the 'Data Visualization with Tableau' course. Update his primary goal metric related to 'AWS Security' with 'Pass AWS Security Specialty exam and complete Tableau course'. Also, update his mentorship relationship by adding 'Data Visualization' to the existing focus areas. Notify him with the message: 'You have been enrolled in a Tableau course as a foundational step towards your AWS Security goal, which has been updated to reflect this.' and notify HR with the message: 'Logan Garcia has been enrolled in supplemental Tableau training to support his primary AWS Security goal.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action(
                "get_course_id_by_name",
                {"course_name": "Data Visualization with Tableau"},
            ),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U303", "keyword": "AWS Security"},
            ),
            Action("get_goal", {"user_id": "U303", "goal_id": "G303-1"}),
            Action("list_user_mentorships", {"user_id": "U303"}),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U303", "course_id": "C1003", "enroll_date": "2025-10-02"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "metric": "Pass AWS Security Specialty exam and complete Tableau course",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR006",
                    "updates": {
                        "focus_areas": [
                            "Cloud Security",
                            "Compliance",
                            "Career Transition",
                            "Data Visualization",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U303",
                    "message": "You have been enrolled in a Tableau course as a foundational step towards your AWS Security goal, which has been updated to reflect this.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Logan Garcia has been enrolled in supplemental Tableau training to support his primary AWS Security goal."
                },
            ),
        ],
        outputs=[
            "User U303 enrolled in course C1003",
            "Goal G303-1 updated for user U303",
            "relationship MR006 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 10: Cross-functional team integration with accessibility focus (Complexity: 12)
    Task(
        annotator="0",
        user_id="res_10",
        instruction="Assign Chloe Scott to the 'Product Design Team'. Update her primary career goal to append the note: 'Now a member of the Product Design Team to lead accessibility initiatives.' Schedule a mentorship session for next week. Notify Chloe with the message: 'You have been assigned to the Product Design Team to lead accessibility initiatives. Your career goal has been updated and a mentorship session is scheduled.' Also, notify her new manager and HR with the message: 'Chloe Scott has been assigned to the Product Design Team to lead accessibility initiatives. Her development plan has been updated.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action("get_team_id_by_name", {"team_name": "Product Design Team"}),
            Action("get_team", {"team_id": "T002"}),
            Action("list_user_goals", {"user_id": "U307"}),
            Action("list_user_mentorships", {"user_id": "U307"}),
            Action("get_today_date", {}),
            Action("add_team_member", {"team_id": "T002", "user_id": "U307"}),
            Action(
                "update_goal",
                {
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "updates": {
                        "goal_description": "Publish company-wide accessibility guidelines and train designers. Now a member of the Product Design Team to lead accessibility initiatives.",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "schedule_mentorship_session",
                {"relationship_id": "MR003", "session_date": "2025-10-09"},
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U307",
                    "message": "You have been assigned to the Product Design Team to lead accessibility initiatives. Your career goal has been updated and a mentorship session is scheduled.",
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U304",
                    "message": "Chloe Scott has been assigned to the Product Design Team to lead accessibility initiatives. Her development plan has been updated.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Chloe Scott has been assigned to the Product Design Team to lead accessibility initiatives. Her development plan has been updated."
                },
            ),
        ],
        outputs=[
            "User U307 added to team T002",
            "Goal G307-1 updated for user U307",
            '"scheduled_for": "2025-10-09"',
            "notified_user",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 11: ML specialization with backup mentorship (Complexity: 13)
    Task(
        annotator="0",
        user_id="res_11",
        instruction="To support Jack Wang's development, enroll him in the 'Machine Learning Specialization' course. Update his goal related to 'Director of Data Science' to reflect this enrollment by appending 'and complete ML Specialization' to its metric. Also, update his mentorship relationship by adding 'Machine Learning' to the existing focus areas. Notify him with the message: 'You have been enrolled in the ML Specialization as a step towards your Director goal, which has been updated to reflect this.' and notify HR with the message: 'Jack Wang has been enrolled in supplemental ML training to support his primary promotion goal.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Jack", "last_name": "Wang"},
            ),
            Action(
                "get_course_id_by_name",
                {"course_name": "Machine Learning Specialization"},
            ),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U301", "keyword": "Director of Data Science"},
            ),
            Action("get_goal", {"user_id": "U301", "goal_id": "G301-1"}),
            Action("list_user_mentorships", {"user_id": "U301"}),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U301", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "metric": "Complete ML course and publish 2 predictive models and complete ML Specialization",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR001",
                    "updates": {
                        "focus_areas": [
                            "Leadership",
                            "Data Science",
                            "Career Growth",
                            "Machine Learning",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U301",
                    "message": "You have been enrolled in the ML Specialization as a step towards your Director goal, which has been updated to reflect this.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Jack Wang has been enrolled in supplemental ML training to support his primary promotion goal."
                },
            ),
        ],
        outputs=[
            "User U301 enrolled in course C1005",
            "Goal G301-1 updated for user U301",
            "relationship MR001 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 12: Performance intervention with comprehensive support (Complexity: 14)
    Task(
        annotator="0",
        user_id="res_12",
        instruction="To support David Adams' performance, enroll him in the 'UX Design Fundamentals' course. Create a new 'Skill Development' goal for him with ID 'G304-2' and description 'Complete UX Design Fundamentals to strengthen technical foundations'. Enhance his mentorship relationship by appending 'Technical Foundation Support' to the focus areas. Notify him with the message: 'A performance support plan has been initiated. You have been enrolled in a foundational course and a new goal has been set. Please connect with your mentor.' and notify HR with the message: 'A performance support plan has been activated for David Adams, including course enrollment and a new development goal.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "David", "last_name": "Adams"},
            ),
            Action("get_course_id_by_name", {"course_name": "UX Design Fundamentals"}),
            Action("list_user_mentorships", {"user_id": "U304"}),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U304", "course_id": "C1002", "enroll_date": "2025-10-02"},
            ),
            Action(
                "add_goal",
                {
                    "user_id": "U304",
                    "goal": {
                        "goal_id": "G304-2",
                        "goal_type": "Skill Development",
                        "status": "Active",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": "Technical Foundation Support",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U304",
                    "message": "A performance support plan has been initiated. You have been enrolled in a foundational course and a new goal has been set. Please connect with your mentor.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "A performance support plan has been activated for David Adams, including course enrollment and a new development goal."
                },
            ),
        ],
        outputs=[
            "User U304 enrolled in course C1002",
            "goal G304-2 added for U304",
            "relationship MR002 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 13: Comprehensive progress analysis with targeted interventions (Complexity: 15)
    Task(
        annotator="0",
        user_id="res_13",
        instruction="To address skill gaps, enroll Ava Nguyen in the 'Machine Learning Specialization' course. Update her goal related to 'Python' to reflect this new training. Also, establish a new mentorship relationship for her by selecting the first available mentor (checking in alphabetical order from M100) with a focus on 'Machine Learning'. Notify her with the message: 'To support your career advancement, you have been enrolled in the Machine Learning Specialization course and assigned a new mentor.' and notify HR with the message: 'Ava Nguyen has been enrolled in targeted ML training and assigned a mentor to address identified skill gaps.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action("get_course_id_by_name", {"course_name": "Machine Learning"}),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U302", "keyword": "Python"},
            ),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U302", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action("compute_mentor_load", {"mentor_id": "M100"}),
            Action(
                "add_mentorship_relationship",
                {
                    "mentor_id": "M100",
                    "mentee_id": "U302",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": ["Machine Learning"],
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U302",
                    "message": "To support your career advancement, you have been enrolled in the Machine Learning Specialization course and assigned a new mentor.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Ava Nguyen has been enrolled in targeted ML training and assigned a mentor to address identified skill gaps."
                },
            ),
        ],
        outputs=[
            "User U302 enrolled in course C1005",
            "Goal G302-1 updated for user U302",
            "Mentorship relationship MR011 created",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 14: Technical competency advancement with certification alignment (Complexity: 13)
    Task(
        annotator="0",
        user_id="res_14",
        instruction="To advance Logan Garcia's technical skills, enroll him in the 'Advanced Python' course. Update his goal related to 'AWS Security' by setting its target date to 90 days from today. Also, update his mentorship relationship to set the focus areas to Cloud Security, Compliance, and Python Development. Notify him with the message: 'To support your technical development, you have been enrolled in the Advanced Python course. Your AWS certification goal and mentorship plan have been updated accordingly.' and notify HR with the message: 'Logan Garcia has been enrolled in Python training to complement his cloud security goals. His development plan has been updated.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action("get_course_id_by_name", {"course_name": "Advanced Python"}),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U303", "keyword": "AWS Security"},
            ),
            Action("list_user_mentorships", {"user_id": "U303"}),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U303", "course_id": "C1001", "enroll_date": "2025-10-02"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "target_date": "2025-12-31",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR006",
                    "updates": {
                        "focus_areas": [
                            "Cloud Security",
                            "Compliance",
                            "Python Development",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U303",
                    "message": "To support your technical development, you have been enrolled in the Advanced Python course. Your AWS certification goal and mentorship plan have been updated accordingly.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Logan Garcia has been enrolled in Python training to complement his cloud security goals. His development plan has been updated."
                },
            ),
        ],
        outputs=[
            "User U303 enrolled in course C1001",
            "Goal G303-1 updated for user U303",
            "relationship MR006 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 15: AWS certification pathway with readiness assessment (Complexity: 12)
    Task(
        annotator="0",
        user_id="res_15",
        instruction="To position David Adams for certification, update his primary career goal related to 'DesignOps' by appending the note: 'This goal is supported by pursuing AWS Solutions Architect certification.' Register him for the 'AWS Solutions Architect Associate' exam (cert ID 'C7012') scheduled for 180 days from today. Also, update his mentorship focus areas to include 'AWS Certification Prep'. Notify him with the message: 'A new development path has been created for you to pursue AWS certification. Your primary career goal and mentorship plan have been updated.' and notify HR with the message: 'A certification path for AWS Solutions Architect Associate has been established for David Adams.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "David", "last_name": "Adams"},
            ),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U304", "keyword": "DesignOps"},
            ),
            Action("list_user_mentorships", {"user_id": "U304"}),
            Action("get_today_date", {}),
            Action(
                "add_user_certification",
                {
                    "user_id": "U304",
                    "cert": {
                        "cert_id": "C7012",
                        "cert_name": "AWS Solutions Architect Associate",
                        "issuer": "AWS",
                        "scheduled_exam_date": "2026-03-31",
                    },
                },
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U304",
                    "goal_id": "G304-1",
                    "updates": {
                        "goal_description": "Move into DesignOps Lead role and formalize cross-team processes. This goal is supported by pursuing AWS Solutions Architect certification.",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": [
                            "Design Operations",
                            "Leadership",
                            "Process Management",
                            "AWS Certification Prep",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U304",
                    "message": "A new development path has been created for you to pursue AWS certification. Your primary career goal and mentorship plan have been updated.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "A certification path for AWS Solutions Architect Associate has been established for David Adams."
                },
            ),
        ],
        outputs=[
            "Certification AWS Solutions Architect Associate added for user U304",
            "Goal G304-1 updated for user U304",
            "relationship MR002 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 16: Mentor capacity optimization with reassignment (Complexity: 11)
    Task(
        annotator="0",
        user_id="res_16",
        instruction="To optimize mentor capacity, reassign Chloe Scott from her current mentor. The new mentor must be the one with the lowest current mentee load (checking M101, M102, and M103), with alphabetical preference as a tie-breaker. The new relationship should inherit the focus areas from the old one. The old relationship should be marked as 'Inactive - Reassigned'. Notify Chloe with the message: 'To ensure you continue to receive quality support, your mentorship has been reassigned to a new mentor. Please check your profile for details.' and notify HR with the message: 'Mentor load balancing has been performed. Chloe Scott has been reassigned to a new mentor.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action("list_user_mentorships", {"user_id": "U307"}),
            Action("get_today_date", {}),
            Action("compute_mentor_load", {"mentor_id": "M101"}),
            Action("compute_mentor_load", {"mentor_id": "M102"}),
            Action("compute_mentor_load", {"mentor_id": "M103"}),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR003",
                    "updates": {
                        "status": "Inactive - Reassigned",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "add_mentorship_relationship",
                {
                    "mentor_id": "M103",
                    "mentee_id": "U307",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Accessibility",
                        "Mentorship",
                        "Design Leadership",
                    ],
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U307",
                    "message": "To ensure you continue to receive quality support, your mentorship has been reassigned to a new mentor. Please check your profile for details.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Mentor load balancing has been performed. Chloe Scott has been reassigned to a new mentor."
                },
            ),
        ],
        outputs=[
            "relationship MR003 updated",
            "Mentorship relationship MR011 created",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 17: Data visualization mastery with specialized mentorship (Complexity: 12)
    Task(
        annotator="0",
        user_id="res_17",
        instruction="To establish Ava Nguyen's data visualization competency, enroll her in the 'Data Visualization with Tableau' course. Create a new 'Skill Development' goal for her with ID 'G302-2' and description 'Achieve proficiency in Tableau for clinical analytics'. Also, establish a new mentorship relationship for her with the first available mentor (checking M100-M103 by lowest load, then alphabetically) with focus areas on Clinical Analytics, Python and Tableau. Notify her with the message: 'A new development path has been created for you to master data visualization. You have been enrolled in a Tableau course, and a new goal and mentorship have been established.' and notify HR with the message: 'Ava Nguyen has been enrolled in Tableau training with a new goal and mentorship to support her data visualization competency.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action(
                "get_course_id_by_name",
                {"course_name": "Data Visualization with Tableau"},
            ),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U302", "course_id": "C1003", "enroll_date": "2025-10-02"},
            ),
            Action(
                "add_goal",
                {
                    "user_id": "U302",
                    "goal": {
                        "goal_id": "G302-2",
                        "goal_type": "Skill Development",
                        "goal_description": "Achieve proficiency in Tableau for clinical analytics",
                        "status": "Active",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action("compute_mentor_load", {"mentor_id": "M100"}),
            Action("compute_mentor_load", {"mentor_id": "M101"}),
            Action("compute_mentor_load", {"mentor_id": "M102"}),
            Action("compute_mentor_load", {"mentor_id": "M103"}),
            Action(
                "add_mentorship_relationship",
                {
                    "mentor_id": "M103",
                    "mentee_id": "U302",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": ["Clinical Analytics", "Python", "Tableau"],
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U302",
                    "message": "A new development path has been created for you to master data visualization. You have been enrolled in a Tableau course, and a new goal and mentorship have been established.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Ava Nguyen has been enrolled in Tableau training with a new goal and mentorship to support her data visualization competency."
                },
            ),
        ],
        outputs=[
            "User U302 enrolled in course C1003",
            "goal G302-2 added for U302",
            "Mentorship relationship MR014 created",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 18: Goal progress validation with technical advancement (Complexity: 10)
    Task(
        annotator="0",
        user_id="res_18",
        instruction="To validate Logan Garcia's AWS Security goal progress, enroll him in the 'Advanced Python' course. Update his goal related to 'AWS Security' to 25% progress. Schedule a mentorship session for 14 days from today. Notify him with the message: 'Your AWS Security goal progress has been updated. You have been enrolled in a new course and a mentorship session has been scheduled to discuss your technical advancement.' and notify HR with the message: 'Logan Garcia's AWS Security goal has been updated with a new course enrollment and a scheduled mentorship session.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action("get_course_id_by_name", {"course_name": "Advanced Python"}),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U303", "keyword": "AWS Security"},
            ),
            Action("list_user_mentorships", {"user_id": "U303"}),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U303", "course_id": "C1001", "enroll_date": "2025-10-02"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 25,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "schedule_mentorship_session",
                {"relationship_id": "MR006", "session_date": "2025-10-16"},
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U303",
                    "message": "Your AWS Security goal progress has been updated. You have been enrolled in a new course and a mentorship session has been scheduled to discuss your technical advancement.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Logan Garcia's AWS Security goal has been updated with a new course enrollment and a scheduled mentorship session."
                },
            ),
        ],
        outputs=[
            "User U303 enrolled in course C1001",
            "Goal G303-1 updated for user U303",
            '"scheduled_for": "2025-10-16"',
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 19: Cross-functional competency with team integration (Complexity: 13)
    Task(
        annotator="0",
        user_id="res_19",
        instruction="To position David Adams for cross-functional leadership, enroll him in the 'Machine Learning Specialization' course. Add a new 'Leadership' goal with ID 'G304-2' and description 'Lead a cross-functional design project leveraging ML insights'. Update his mentorship focus areas to be ['Design Operations', 'Leadership', 'Process Management', 'Cross-functional Collaboration']. Notify him with the message: 'To support your growth into cross-functional leadership, you have been enrolled in a Machine Learning course and a new leadership goal has been created.' and notify HR with the message: 'David Adams has been enrolled in ML training to support a new cross-functional leadership goal.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "David", "last_name": "Adams"},
            ),
            Action(
                "get_course_id_by_name",
                {"course_name": "Machine Learning Specialization"},
            ),
            Action("list_user_mentorships", {"user_id": "U304"}),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U304", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action(
                "add_goal",
                {
                    "user_id": "U304",
                    "goal": {
                        "goal_id": "G304-2",
                        "goal_type": "Leadership",
                        "goal_description": "Lead a cross-functional design project leveraging ML insights",
                        "status": "Active",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": [
                            "Design Operations",
                            "Leadership",
                            "Process Management",
                            "Cross-functional Collaboration",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U304",
                    "message": "To support your growth into cross-functional leadership, you have been enrolled in a Machine Learning course and a new leadership goal has been created.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "David Adams has been enrolled in ML training to support a new cross-functional leadership goal."
                },
            ),
        ],
        outputs=[
            "User U304 enrolled in course C1005",
            "goal G304-2 added for U304",
            "relationship MR002 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 20: Strategic development with Agile competency (Complexity: 11)
    Task(
        annotator="0",
        user_id="res_20",
        instruction="Establish a strategic development plan for David Adams by enrolling him in the 'Agile Product Management' course. Update his mentorship focus areas to include 'Agile Methodologies'. Schedule a mentorship session for 14 days from today. Notify him with the message: 'A new strategic development plan has been initiated. You have been enrolled in an Agile course, and a mentorship session has been scheduled to discuss next steps.' and notify HR with the message: 'A strategic development plan has been established for David Adams, including Agile course enrollment and mentorship alignment.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "David", "last_name": "Adams"},
            ),
            Action(
                "get_course_id_by_name",
                {"course_name": "Agile Product Management"},
            ),
            Action("list_user_mentorships", {"user_id": "U304"}),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U304", "course_id": "C1006", "enroll_date": "2025-10-02"},
            ),
            Action(
                "schedule_mentorship_session",
                {"relationship_id": "MR002", "session_date": "2025-10-16"},
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": [
                            "Design Operations",
                            "Leadership",
                            "Process Management",
                            "Agile Methodologies",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U304",
                    "message": "A new strategic development plan has been initiated. You have been enrolled in an Agile course, and a mentorship session has been scheduled to discuss next steps.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "A strategic development plan has been established for David Adams, including Agile course enrollment and mentorship alignment."
                },
            ),
        ],
        outputs=[
            "User U304 enrolled in course C1006",
            '"scheduled_for": "2025-10-16"',
            "relationship MR002 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 21: ML competency validation with workflow coordination (Complexity: 14)
    Task(
        annotator="0",
        user_id="res_21",
        instruction="To validate Jack Wang's ML competency, enroll him in the 'Machine Learning Specialization' course. Update his goal related to Director of Data Science to 45% progress. Also, update his mentorship relationship to set the focus areas to Leadership, Data Science, Career Growth, and Machine Learning. Notify HR with the message: 'Jack Wang has been enrolled in the Machine Learning Specialization to validate competency for his promotion goal. His development plan has been updated.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Jack", "last_name": "Wang"},
            ),
            Action(
                "get_course_id_by_name",
                {"course_name": "Machine Learning Specialization"},
            ),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U301", "keyword": "Director of Data Science"},
            ),
            Action("list_user_mentorships", {"user_id": "U301"}),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U301", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 45,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR001",
                    "updates": {
                        "focus_areas": [
                            "Leadership",
                            "Data Science",
                            "Career Growth",
                            "Machine Learning",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Jack Wang has been enrolled in the Machine Learning Specialization to validate competency for his promotion goal. His development plan has been updated."
                },
            ),
        ],
        outputs=[
            "User U301 enrolled in course C1005",
            "Goal G301-1 updated for user U301",
            "relationship MR001 updated",
            '"notified": "HR"',
        ],
    ),
    # Task 22: Development Plan coordination with dual course assignment (Complexity: 13)
    Task(
        annotator="0",
        user_id="res_22",
        instruction="Establish a development plan for Ava Nguyen by advancing her promotion workflow to the 'Development Plan' stage and setting a review date for 60 days from today. Enroll her in the 'Machine Learning Specialization' and 'Data Visualization with Tableau' courses. Update her goal related to 'Python' to 40% progress. Notify her with the message: 'Your development plan has been established. You have been enrolled in new courses to support your promotion goals.' and notify HR with the message: 'A development plan for Ava Nguyen has been established, including new course enrollments and a scheduled review date.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action("find_hr_workflow_for_user", {"user_id": "U302"}),
            Action(
                "get_course_id_by_name",
                {"course_name": "Machine Learning Specialization"},
            ),
            Action(
                "get_course_id_by_name",
                {"course_name": "Data Visualization with Tableau"},
            ),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U302", "keyword": "Python"},
            ),
            Action("get_today_date", {}),
            Action(
                "update_hr_workflow",
                {
                    "workflow_id": "WF001",
                    "updates": {
                        "current_stage": "Development Plan",
                        "status": "In Progress",
                        "review_date": "2025-12-01",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U302", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U302", "course_id": "C1003", "enroll_date": "2025-10-02"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 40,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U302",
                    "message": "Your development plan has been established. You have been enrolled in new courses to support your promotion goals.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "A development plan for Ava Nguyen has been established, including new course enrollments and a scheduled review date."
                },
            ),
        ],
        outputs=[
            "workflow WF001 updated",
            "User U302 enrolled in course C1005",
            "User U302 enrolled in course C1003",
            "Goal G302-1 updated for user U302",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 23: Leadership advancement with mentorship enhancement (Complexity: 12)
    Task(
        annotator="0",
        user_id="res_23",
        instruction="To prepare Chloe Scott for a leadership role, enroll her in the 'Agile Product Management' course. Update her primary goal on accessibility to append the note: 'and master Agile methodologies for future leadership roles.' Also, update her mentorship focus areas to include 'Agile Leadership'. Notify Chloe, her manager, and HR with the message: 'A new leadership development plan has been initiated for Chloe Scott. She has been enrolled in Agile training, and her career goal and mentorship plan have been updated to support this.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action("search_users", {"filters": {"user_id": "U307"}}),
            Action(
                "get_course_id_by_name",
                {"course_name": "Agile Product Management"},
            ),
            Action("list_user_goals", {"user_id": "U307"}),
            Action("list_user_mentorships", {"user_id": "U307"}),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U307", "course_id": "C1006", "enroll_date": "2025-10-02"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "updates": {
                        "goal_description": "Publish company-wide accessibility guidelines and train designers. and master Agile methodologies for future leadership roles.",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR003",
                    "updates": {
                        "focus_areas": [
                            "Accessibility",
                            "Mentorship",
                            "Design Leadership",
                            "Agile Leadership",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U307",
                    "message": "A new leadership development plan has been initiated for Chloe Scott. She has been enrolled in Agile training, and her career goal and mentorship plan have been updated to support this.",
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U304",
                    "message": "A new leadership development plan has been initiated for Chloe Scott. She has been enrolled in Agile training, and her career goal and mentorship plan have been updated to support this.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "A new leadership development plan has been initiated for Chloe Scott. She has been enrolled in Agile training, and her career goal and mentorship plan have been updated to support this."
                },
            ),
        ],
        outputs=[
            "User U307 enrolled in course C1006",
            "Goal G307-1 updated for user U307",
            "relationship MR003 updated",
            "notified_user",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 24: Post-MBA strategic positioning with certification planning (Complexity: 14)
    Task(
        annotator="0",
        user_id="res_24",
        instruction="To establish a post-MBA strategic leadership pathway for Logan Garcia, register him for the 'Project Management Professional (PMP)' certification (cert ID 'C7014') with an exam date 225 days from today. Enroll him in the 'Agile Product Management' course. Create a new 'Leadership' goal with ID 'G303-2' and description 'Achieve PMP certification and demonstrate strategic leadership'. Update his mentorship focus areas to include 'Strategic Leadership'. Notify him with the message: 'Your post-MBA leadership pathway has been established. You have been registered for the PMP exam, enrolled in a new course, and a new goal has been created.' and notify HR with the message: 'A post-MBA strategic leadership pathway has been established for Logan Garcia, including PMP registration and a new development goal.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action(
                "get_course_id_by_name",
                {"course_name": "Agile Product Management"},
            ),
            Action("list_user_mentorships", {"user_id": "U303"}),
            Action("get_today_date", {}),
            Action(
                "add_user_certification",
                {
                    "user_id": "U303",
                    "cert": {
                        "cert_id": "C7014",
                        "cert_name": "Project Management Professional (PMP)",
                        "issuer": "PMI",
                        "scheduled_exam_date": "2026-05-14",
                    },
                },
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U303", "course_id": "C1006", "enroll_date": "2025-10-02"},
            ),
            Action(
                "add_goal",
                {
                    "user_id": "U303",
                    "goal": {
                        "goal_id": "G303-2",
                        "goal_type": "Leadership",
                        "goal_description": "Achieve PMP certification and demonstrate strategic leadership",
                        "status": "Active",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR006",
                    "updates": {
                        "focus_areas": [
                            "Cloud Security",
                            "Compliance",
                            "Strategic Leadership",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U303",
                    "message": "Your post-MBA leadership pathway has been established. You have been registered for the PMP exam, enrolled in a new course, and a new goal has been created.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "A post-MBA strategic leadership pathway has been established for Logan Garcia, including PMP registration and a new development goal."
                },
            ),
        ],
        outputs=[
            "Certification Project Management Professional (PMP) added for user U303",
            "User U303 enrolled in course C1006",
            "goal G303-2 added for U303",
            "relationship MR006 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 25: Stakeholder management competency with mentor coordination (Complexity: 11)
    Task(
        annotator="0",
        user_id="res_25",
        instruction="To advance David Adams' stakeholder management competency, enroll him in the 'Project Management Professional (PMP)' course. Update his mentorship focus areas to include 'Stakeholder Alignment'. Notify him with the message: 'To advance your stakeholder management competency, you have been enrolled in a leadership course and your mentorship plan has been updated.' and notify HR with the message: 'David Adams has been enrolled in leadership training to support his stakeholder management competency.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "David", "last_name": "Adams"},
            ),
            Action(
                "get_course_id_by_name",
                {"course_name": "Project Management Professional (PMP)"},
            ),
            Action("list_user_mentorships", {"user_id": "U304"}),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U304", "course_id": "C1004", "enroll_date": "2025-10-02"},
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": [
                            "Design Operations",
                            "Leadership",
                            "Process Management",
                            "Stakeholder Alignment",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U304",
                    "message": "To advance your stakeholder management competency, you have been enrolled in a leadership course and your mentorship plan has been updated.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "David Adams has been enrolled in leadership training to support his stakeholder management competency."
                },
            ),
        ],
        outputs=[
            "User U304 enrolled in course C1004",
            "relationship MR002 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 26: Foundation skills acceleration with goal synchronization (Complexity: 9)
    Task(
        annotator="0",
        user_id="res_26",
        instruction="To accelerate Ava Nguyen's foundation skills, enroll her in the 'Advanced Python' course. Synchronize her goal related to 'Python' by updating its progress to 10%. Notify her with the message: 'To accelerate your foundation skills, you have been enrolled in the Advanced Python course and your goal progress has been updated.' and notify HR with the message: 'Ava Nguyen has been enrolled in Python training to accelerate her foundation skills. Her goal progress has been synchronized.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action("get_course_id_by_name", {"course_name": "Advanced Python"}),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U302", "keyword": "Python"},
            ),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U302", "course_id": "C1001", "enroll_date": "2025-10-02"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 10,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U302",
                    "message": "To accelerate your foundation skills, you have been enrolled in the Advanced Python course and your goal progress has been updated.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Ava Nguyen has been enrolled in Python training to accelerate her foundation skills. Her goal progress has been synchronized."
                },
            ),
        ],
        outputs=[
            "User U302 enrolled in course C1001",
            "Goal G302-1 updated for user U302",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 27: Mentor capacity monitoring with alert generation (Complexity: 7)
    Task(
        annotator="0",
        user_id="res_27",
        instruction="To optimize mentor capacity for Mentor M100, reassign their most recent mentee, Chloe Scott, to a new mentor. The new mentor must be the one with the lowest current mentee load (checking M101, M102, and M103), with alphabetical preference as a tie-breaker. The new relationship should inherit the focus areas from the old one. The old relationship should be marked as 'Inactive - Reassigned'. Notify Chloe with the message: 'To ensure you continue to receive quality support, your mentorship has been reassigned to a new mentor. Please check your profile for details.' and notify HR with the message: 'Mentor load balancing has been performed. Chloe Scott has been reassigned from Mentor M100 to a new mentor to optimize capacity.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action("list_user_mentorships", {"user_id": "U307"}),
            Action("get_today_date", {}),
            Action("compute_mentor_load", {"mentor_id": "M101"}),
            Action("compute_mentor_load", {"mentor_id": "M102"}),
            Action("compute_mentor_load", {"mentor_id": "M103"}),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR003",
                    "updates": {
                        "status": "Inactive - Reassigned",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "add_mentorship_relationship",
                {
                    "mentor_id": "M103",
                    "mentee_id": "U307",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": ["Accessibility", "Mentorship", "Design Leadership"],
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U307",
                    "message": "To ensure you continue to receive quality support, your mentorship has been reassigned to a new mentor. Please check your profile for details.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Mentor load balancing has been performed. Chloe Scott has been reassigned from Mentor M100 to a new mentor to optimize capacity."
                },
            ),
        ],
        outputs=[
            "relationship MR003 updated",
            "Mentorship relationship MR011 created",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 28: Skill gap remediation with ML specialization (Complexity: 10)
    Task(
        annotator="0",
        user_id="res_28",
        instruction="To address Ava Nguyen's skill gaps, enroll her in the 'Machine Learning Specialization' course. Synchronize her goal related to 'Python' by updating its progress to 15%. Notify her with the message: 'To address your skill gaps, you have been enrolled in the Machine Learning Specialization and your goal progress has been updated.' and notify HR with the message: 'Ava Nguyen has been enrolled in ML training to address identified skill gaps. Her goal progress has been synchronized.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action(
                "get_course_id_by_name",
                {"course_name": "Machine Learning Specialization"},
            ),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U302", "keyword": "Python"},
            ),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U302", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 15,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U302",
                    "message": "To address your skill gaps, you have been enrolled in the Machine Learning Specialization and your goal progress has been updated.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Ava Nguyen has been enrolled in ML training to address identified skill gaps. Her goal progress has been synchronized."
                },
            ),
        ],
        outputs=[
            "User U302 enrolled in course C1005",
            "Goal G302-1 updated for user U302",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 29: Transition goal management with market alignment (Complexity: 8)
    Task(
        annotator="0",
        user_id="res_29",
        instruction="Synchronize Jack Wang's 'Director of Data Science' goal by updating its progress to match his current average course progress. If the new progress is over 50%, schedule a review session with his mentor for next week. Notify Jack about the goal update, and if a session was scheduled, include that information in his notification and also notify his mentor.",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Jack", "last_name": "Wang"},
            ),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U301", "keyword": "Director of Data Science"},
            ),
            Action("compute_average_progress", {"user_id": "U301"}),
            Action("list_user_mentorships", {"user_id": "U301"}),
            Action("get_today_date", {}),
            Action(
                "update_goal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 72.5,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "schedule_mentorship_session",
                {"relationship_id": "MR001", "session_date": "2025-10-09"},
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U301",
                    "message": "Your Director promotion goal has been updated to 72.5% based on your average course progress. A review session with your mentor has been scheduled for 2025-10-09.",
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "M102",
                    "message": "A progress review session with your mentee, Jack Wang, has been scheduled for 2025-10-09 to discuss his recent goal advancement.",
                },
            ),
        ],
        outputs=[
            "Goal G301-1 updated for user U301",
            '"scheduled_for": "2025-10-09"',
            "notified_user",
            "notified_user",
        ],
    ),
    # Task 30: Analytics mastery enhancement with supplemental training (Complexity: 9)
    Task(
        annotator="0",
        user_id="res_30",
        instruction="To enhance Jack Wang's analytics mastery, enroll him in the 'Data Visualization with Tableau' course. Track this progress by updating his goal related to 'Director of Data Science' to 50%. Notify him with the message: 'To enhance your analytics mastery, you have been enrolled in a Tableau course and your goal progress has been updated.' and notify HR with the message: 'Jack Wang has been enrolled in supplemental Tableau training to support his analytics mastery. His goal progress has been updated.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Jack", "last_name": "Wang"},
            ),
            Action(
                "get_course_id_by_name",
                {"course_name": "Data Visualization with Tableau"},
            ),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U301", "keyword": "Director of Data Science"},
            ),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U301", "course_id": "C1003", "enroll_date": "2025-10-02"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 50,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U301",
                    "message": "To enhance your analytics mastery, you have been enrolled in a Tableau course and your goal progress has been updated.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Jack Wang has been enrolled in supplemental Tableau training to support his analytics mastery. His goal progress has been updated."
                },
            ),
        ],
        outputs=[
            "User U301 enrolled in course C1003",
            "Goal G301-1 updated for user U301",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 31: Workflow progression with skill validation (Complexity: 12)
    Task(
        annotator="0",
        user_id="res_31",
        instruction="You need Ava Nguyen's promotion workflow progressed to Development Plan with Skills Assessment completion validated and ML course enrollment initiated.",
        actions=[
            Action(
                "get_user_id_from_name", {"first_name": "Ava", "last_name": "Nguyen"}
            ),
            Action("search_users", {"filters": {"user_id": "U302"}}),
            Action("get_today_date", {}),
            Action("get_hr_workflow", {"workflow_id": "WF001"}),
            Action(
                "update_hr_workflow",
                {
                    "workflow_id": "WF001",
                    "updates": {
                        "current_stage": "Development Plan",
                        "status": "In Progress",
                        "skills_assessment_completed": "2025-10-02",
                    },
                },
            ),
            Action(
                "enroll_in_course",
                {"user_id": "U302", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action("get_goal", {"user_id": "U302", "goal_id": "G302-1"}),
            Action(
                "update_goal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {"last_updated": "2025-10-02"},
                },
            ),
            Action(
                "notify_hr",
                {"message": "WF001 progression to Development Plan completed"},
            ),
        ],
        outputs=[
            "workflow WF001 updated",
            "User U302 enrolled in course C1005",
            "Goal G302-1 updated for user U302",
            '"notified": "HR"',
        ],
    ),
    # Task 32: Leadership coaching optimization with milestone achievement (Complexity: 13)
    Task(
        annotator="0",
        user_id="res_32",
        instruction="To finalize Alexander Adams' leadership development, mark his primary goal related to 'Staff SRE' as 100% complete, appending the note 'Final leadership milestone achieved.' to its description. Schedule a final coaching session with his mentor for next week. Notify Alexander, his mentor, and HR with the message: 'Alexander Adams has successfully completed his Staff SRE leadership goal. A final coaching session has been scheduled to conclude his development plan.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Alexander", "last_name": "Adams"},
            ),
            Action("list_user_goals", {"user_id": "U306"}),
            Action("list_user_mentorships", {"user_id": "U306"}),
            Action("get_today_date", {}),
            Action(
                "update_goal",
                {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {
                        "progress_percent": 100,
                        "status": "Completed",
                        "goal_description": "Advance to Staff Site Reliability Engineer and lead reliability roadmap. Final leadership milestone achieved.",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "schedule_mentorship_session",
                {"relationship_id": "MR004", "session_date": "2025-10-09"},
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U306",
                    "message": "Alexander Adams has successfully completed his Staff SRE leadership goal. A final coaching session has been scheduled to conclude his development plan.",
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "M101",
                    "message": "Alexander Adams has successfully completed his Staff SRE leadership goal. A final coaching session has been scheduled to conclude his development plan.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Alexander Adams has successfully completed his Staff SRE leadership goal. A final coaching session has been scheduled to conclude his development plan."
                },
            ),
        ],
        outputs=[
            "Goal G306-1 updated for user U306",
            '"scheduled_for": "2025-10-09"',
            "notified_user",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 33: Performance review with goal advancement (Complexity: 11)
    Task(
        annotator="0",
        user_id="res_33",
        instruction="Following his quarterly performance review, update Jack Wang's goal related to 'Director of Data Science' by setting its progress to 65%. Notify him with the message: 'Your quarterly performance review has been completed and your promotion goal progress has been updated.' and notify HR with the message: 'The quarterly performance review for Jack Wang is complete. His promotion goal has been updated accordingly.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Jack", "last_name": "Wang"},
            ),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U301", "keyword": "Director of Data Science"},
            ),
            Action("get_today_date", {}),
            Action(
                "update_goal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 65,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U301",
                    "message": "Your quarterly performance review has been completed and your promotion goal progress has been updated.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "The quarterly performance review for Jack Wang is complete. His promotion goal has been updated accordingly."
                },
            ),
        ],
        outputs=[
            "Goal G301-1 updated for user U301",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 34: Accelerated learning with workflow advancement (Complexity: 14)
    Task(
        annotator="0",
        user_id="res_34",
        instruction="Initiate an accelerated learning program for Ava Nguyen by updating her 'Advanced Python' course progress to 25%. Advance her promotion workflow to the 'Training Assignment' stage. Update her goal related to 'Python' to 45% progress. Notify her with the message: 'Your accelerated learning program has been initiated. Your course and goal progress have been updated, and your promotion workflow has been advanced.' and notify HR with the message: 'An accelerated learning program for Ava Nguyen has been initiated. Her promotion workflow has advanced to the Training Assignment stage.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action("get_course_id_by_name", {"course_name": "Advanced Python"}),
            Action("find_hr_workflow_for_user", {"user_id": "U302"}),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U302", "keyword": "Python"},
            ),
            Action("get_today_date", {}),
            Action(
                "update_user_course_progress",
                {
                    "user_id": "U302",
                    "course_id": "C1001",
                    "updates": {
                        "current_progress_percent": 25,
                        "status": "In Progress",
                    },
                },
            ),
            Action(
                "update_hr_workflow",
                {
                    "workflow_id": "WF001",
                    "updates": {
                        "current_stage": "Training Assignment",
                        "status": "In Progress",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 45,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U302",
                    "message": "Your accelerated learning program has been initiated. Your course and goal progress have been updated, and your promotion workflow has been advanced.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "An accelerated learning program for Ava Nguyen has been initiated. Her promotion workflow has advanced to the Training Assignment stage."
                },
            ),
        ],
        outputs=[
            "course progress updated",
            "workflow WF001 updated",
            "Goal G302-1 updated for user U302",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 35: Cross-functional analytics integration (Complexity: 12)
    Task(
        annotator="0",
        user_id="res_35",
        instruction="To position Harper King for cross-functional integration, assign her to the 'Product Design Team'. Create a new 'Cross-functional Development' goal with ID 'G305-2' and description 'Master analytics-design integration'. Establish a new mentorship relationship with the first available mentor (checking M100-M103 by lowest load, then alphabetically) with focus areas ['Product Marketing', 'Data Analytics', 'Design Thinking']. Notify her with the message: 'Your cross-functional development path has been established. You have been assigned to a new team, and a new goal and mentorship have been created.' and notify HR with the message: 'Harper King has been assigned to the Product Design Team to support cross-functional development. A new goal and mentorship have been established.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Harper", "last_name": "King"},
            ),
            Action("get_team_id_by_name", {"team_name": "Product Design Team"}),
            Action("get_today_date", {}),
            Action("add_team_member", {"team_id": "T002", "user_id": "U305"}),
            Action(
                "add_goal",
                {
                    "user_id": "U305",
                    "goal": {
                        "goal_id": "G305-2",
                        "goal_type": "Cross-functional Development",
                        "goal_description": "Master analytics-design integration",
                        "status": "Active",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action("compute_mentor_load", {"mentor_id": "M100"}),
            Action("compute_mentor_load", {"mentor_id": "M101"}),
            Action("compute_mentor_load", {"mentor_id": "M102"}),
            Action("compute_mentor_load", {"mentor_id": "M103"}),
            Action(
                "add_mentorship_relationship",
                {
                    "mentor_id": "M103",
                    "mentee_id": "U305",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Product Marketing",
                        "Data Analytics",
                        "Design Thinking",
                    ],
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U305",
                    "message": "Your cross-functional development path has been established. You have been assigned to a new team, and a new goal and mentorship have been created.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Harper King has been assigned to the Product Design Team to support cross-functional development. A new goal and mentorship have been established."
                },
            ),
        ],
        outputs=[
            "User U305 added to team T002",
            "goal G305-2 added for U305",
            "Mentorship relationship MR011 created",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 36: Comprehensive certification strategy with goal alignment (Complexity: 13)
    Task(
        annotator="0",
        user_id="res_36",
        instruction="To establish Logan Garcia's PMP certification strategy, register him for the 'Project Management Professional (PMP)' exam (cert ID 'C7015') scheduled for 230 days from today. Create a new 'Certification' goal with ID 'G303-2' and description 'Achieve PMP certification'. Update his mentorship focus areas to include 'PMP Certification Strategy'. Notify him with the message: 'Your PMP certification strategy has been established. You have been registered for the exam, and a new goal and mentorship focus have been created.' and notify HR with the message: 'A PMP certification strategy has been established for Logan Garcia, including exam registration and a new development goal.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action("list_user_mentorships", {"user_id": "U303"}),
            Action("get_today_date", {}),
            Action(
                "add_user_certification",
                {
                    "user_id": "U303",
                    "cert": {
                        "cert_id": "C7015",
                        "cert_name": "Project Management Professional (PMP)",
                        "issuer": "PMI",
                        "scheduled_exam_date": "2026-05-20",
                    },
                },
            ),
            Action(
                "add_goal",
                {
                    "user_id": "U303",
                    "goal": {
                        "goal_id": "G303-2",
                        "goal_type": "Certification",
                        "goal_description": "Achieve PMP certification",
                        "status": "Active",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR006",
                    "updates": {
                        "focus_areas": [
                            "Cloud Security",
                            "Compliance",
                            "PMP Certification Strategy",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U303",
                    "message": "Your PMP certification strategy has been established. You have been registered for the exam, and a new goal and mentorship focus have been created.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "A PMP certification strategy has been established for Logan Garcia, including exam registration and a new development goal."
                },
            ),
        ],
        outputs=[
            "Certification Project Management Professional (PMP) added for user U303",
            "goal G303-2 added for U303",
            "relationship MR006 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 37: Advanced accessibility leadership with UX enhancement (Complexity: 14)
    Task(
        annotator="0",
        user_id="res_37",
        instruction="To position Chloe Scott for advanced accessibility leadership, enroll her in the 'UX Design Fundamentals' course. Schedule a mentorship session for 16 days from today. Update her mentorship focus areas to include 'Advanced Accessibility Strategy'. Notify her with the message: 'Your advanced accessibility leadership pathway has been established. You have been enrolled in a new course and a mentorship session has been scheduled.' and notify HR with the message: 'An advanced accessibility leadership pathway has been established for Chloe Scott, including new course enrollment and mentorship coordination.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action("get_course_id_by_name", {"course_name": "UX Design Fundamentals"}),
            Action("list_user_mentorships", {"user_id": "U307"}),
            Action("get_today_date", {}),
            Action(
                "enroll_in_course",
                {"user_id": "U307", "course_id": "C1002", "enroll_date": "2025-10-02"},
            ),
            Action(
                "schedule_mentorship_session",
                {"relationship_id": "MR003", "session_date": "2025-10-18"},
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR003",
                    "updates": {
                        "focus_areas": [
                            "Accessibility",
                            "Mentorship",
                            "Design Leadership",
                            "Advanced Accessibility Strategy",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U307",
                    "message": "Your advanced accessibility leadership pathway has been established. You have been enrolled in a new course and a mentorship session has been scheduled.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "An advanced accessibility leadership pathway has been established for Chloe Scott, including new course enrollment and mentorship coordination."
                },
            ),
        ],
        outputs=[
            "User U307 enrolled in course C1002",
            '"scheduled_for": "2025-10-18"',
            "relationship MR003 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 38: Enterprise performance optimization with executive development (Complexity: 15)
    Task(
        annotator="0",
        user_id="res_38",
        instruction="To position Alexander Adams for enterprise-level performance, schedule an executive coaching session for 10 days from today. Update his mentorship focus areas to include 'Executive Coaching'. Notify him with the message: 'To support your enterprise-level performance goals, an executive coaching session has been scheduled and your mentorship plan has been updated.' and notify HR with the message: 'An executive coaching session has been scheduled for Alexander Adams to support his enterprise-level performance goals.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Alexander", "last_name": "Adams"},
            ),
            Action("list_user_mentorships", {"user_id": "U306"}),
            Action("get_today_date", {}),
            Action(
                "schedule_mentorship_session",
                {"relationship_id": "MR004", "session_date": "2025-10-12"},
            ),
            Action(
                "update_mentorship_relationship",
                {
                    "relationship_id": "MR004",
                    "updates": {
                        "focus_areas": [
                            "Site Reliability Engineering",
                            "Leadership",
                            "Infrastructure",
                            "Executive Coaching",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U306",
                    "message": "To support your enterprise-level performance goals, an executive coaching session has been scheduled and your mentorship plan has been updated.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "An executive coaching session has been scheduled for Alexander Adams to support his enterprise-level performance goals."
                },
            ),
        ],
        outputs=[
            '"scheduled_for": "2025-10-12"',
            "relationship MR004 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 39: Advanced coaching with strategic goal advancement (Complexity: 11)
    Task(
        annotator="0",
        user_id="res_39",
        instruction="Advance Alexander Adams' primary career advancement goal by updating its progress to 50%. Also, schedule a mentorship session for 12 days from today to track his progress. Notify him with the message: 'Your career advancement goal has been updated. A new mentorship session has been scheduled to track your progress.' and notify HR with the message: 'Alexander Adams' primary career goal has been advanced and a new mentorship session has been scheduled.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Alexander", "last_name": "Adams"},
            ),
            Action("list_user_goals", {"user_id": "U306"}),
            Action("list_user_mentorships", {"user_id": "U306"}),
            Action("get_today_date", {}),
            Action(
                "schedule_mentorship_session",
                {"relationship_id": "MR004", "session_date": "2025-10-14"},
            ),
            Action(
                "update_goal",
                {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {
                        "progress_percent": 50,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U306",
                    "message": "Your career advancement goal has been updated. A new mentorship session has been scheduled to track your progress.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "Alexander Adams' primary career goal has been advanced and a new mentorship session has been scheduled."
                },
            ),
        ],
        outputs=[
            '"scheduled_for": "2025-10-14"',
            "Goal G306-1 updated for user U306",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 40: Comprehensive skill validation with certification readiness (Complexity: 15)
    Task(
        annotator="0",
        user_id="res_40",
        instruction="To complete Logan Garcia's skill validation, update his goal related to 'AWS Security' to 70% progress. Schedule a mentorship session for 20 days from today to confirm certification readiness. Notify him with the message: 'Your skill validation is complete. Your goal progress has been updated, and a mentorship session has been scheduled to confirm certification readiness.' and notify HR with the message: 'A comprehensive skill validation for Logan Garcia has been completed. His goal progress has been updated and a mentorship session is scheduled.'",
        actions=[
            Action(
                "get_user_id_from_name",
                {"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action(
                "get_goal_id_by_description",
                {"user_id": "U303", "keyword": "AWS Security"},
            ),
            Action("list_user_mentorships", {"user_id": "U303"}),
            Action("get_today_date", {}),
            Action(
                "update_goal",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 70,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "schedule_mentorship_session",
                {"relationship_id": "MR006", "session_date": "2025-10-22"},
            ),
            Action(
                "notify_user",
                {
                    "user_id": "U303",
                    "message": "Your skill validation is complete. Your goal progress has been updated, and a mentorship session has been scheduled to confirm certification readiness.",
                },
            ),
            Action(
                "notify_hr",
                {
                    "message": "A comprehensive skill validation for Logan Garcia has been completed. His goal progress has been updated and a mentorship session is scheduled."
                },
            ),
        ],
        outputs=[
            "Goal G303-1 updated for user U303",
            '"scheduled_for": "2025-10-22"',
            "notified_user",
            '"notified": "HR"',
        ],
    ),
]
