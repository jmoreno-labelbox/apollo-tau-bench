
tasks = [
    {
        "annotator": 0,
        "user_id": "res_01",
        "instruction": "Enroll Ava Nguyen in the Machine Learning Specialization course and update his Data Science leadership goal to 30% progress using today's date.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U301",
                    "goal_description_keywords": "Data Science"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 30,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "User U301 enrolled in course C1005",
                "Goal G301-1 updated for user U301"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_02",
        "instruction": "Update Harper Bennett's clinical analytics goal to 25% progress reflecting her Advanced Python course enrollment using today's date.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Advanced Python"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1001",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U302",
                    "goal_description_keywords": "clinical analytics"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 25,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "User U302 enrolled in course C1001",
                "Goal G302-1 updated for user U302"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_03",
        "instruction": "Mark Michael Rodriguez as completed in UX Design Fundamentals course and update his DesignOps goal to 35% progress using today's date.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Adams"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "UX Design Fundamentals"
                },
            },
            {
                "name": "markCourseCompleted",
                "arguments": {
                    "user_id": "U304",
                    "course_id": "C1002",
                    "completion_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U304",
                    "goal_description_keywords": "DesignOps"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U304",
                    "goal_id": "G304-1",
                    "updates": {
                        "progress_percent": 35,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "Course C1002 marked completed for user U304",
                "Goal G304-1 updated for user U304"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_04",
        "instruction": "For Alexander Adams, add the 'Web Accessibility Specialist' certification from IAAP to her profile, with the exam scheduled 9 months from today. Then, create a new high-priority goal for her to 'Obtain the Web Accessibility Specialist certification'. Finally, send her a confirmation email with 'Your New Certification Goal' as a subject and 'This email confirms that the 'Web Accessibility Specialist' certification has been added to your profile. A new goal has been created to track your progress.' to the body.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Scott"
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U307",
                    "cert": {
                        "cert_name": "Web Accessibility Specialist",
                        "issuer": "IAAP",
                        "scheduled_exam_date": "2026-04-04"
                    }
                },
            },
            {
                "name": "addUserGoal",
                "arguments": {
                    "user_id": "U307",
                    "goal": {
                        "goal_type": "Certification",
                        "goal_description": "Obtain the Web Accessibility Specialist certification",
                        "target_certification": "Web Accessibility Specialist",
                        "priority": "High",
                        "status": "Active",
                        "last_updated": "2025-07-04"
                    }
                },
            },
            {
                "name": "sendEmailToUser",
                "arguments": {
                    "user_id": "U307",
                    "subject": "Your New Certification Goal",
                    "body": "This email confirms that the 'Web Accessibility Specialist' certification has been added to your profile. A new goal has been created to track your progress."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_05",
        "instruction": "First, check the job market demand for a 'Product Manager' to see if the demand score is high (above 8.0), then proceed with the following for David Adams: enroll him in the 'Project Management Professional (PMP)' course to support his pivot to cloud-compliance. Then, update his 'cloud-compliance' goal to 25% progress and append to the description: 'Enrolled in PMP to build project leadership skills.' Finally, send him an email with the subject 'Your Cloud Compliance Career Path' and body 'Demand for roles like Product Manager is high. To support your goal, you have been enrolled in the PMP course. Your goal description has been updated to reflect this new step.'",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getJobMarketInsights",
                "arguments": {
                    "role": "Product Manager"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Project Management Professional (PMP)"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U303",
                    "course_id": "C1004",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U303",
                    "goal_description_keywords": "cloud-compliance"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 25,
                        "goal_description": "Pass AWS Security Specialty exam to pivot toward cloud-compliance. Enrolled in PMP to build project leadership skills.",
                        "last_updated": "2025-07-04"
                    }
                },
            },
            {
                "name": "sendEmailToUser",
                "arguments": {
                    "user_id": "U303",
                    "subject": "Your Cloud Compliance Career Path",
                    "body": "Demand for roles like Product Manager is high. To support your goal, you have been enrolled in the PMP course. Your goal description has been updated to reflect this new step."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_06",
        "instruction": "Add AWS Security Specialty certification for David Adams with exam scheduled 10 months from today, enroll him in Machine Learning Specialization, and update his goal to 15% progress.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U303",
                    "cert": {
                        "cert_name": "AWS Security Specialty",
                        "issuer": "AWS",
                        "scheduled_exam_date": "2026-05-04"
                    }
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U303",
                    "course_id": "C1005",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U303",
                    "goal_description_keywords": "AWS Security"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 15,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "User U303 enrolled in course C1005",
                "Goal G303-1 updated for user U303"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_07",
        "instruction": "Enroll Harper Bennett in Agile Product Management course and update her clinical analytics goal to 35% progress using today's date.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Agile Product Management"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U302",
                    "goal_description_keywords": "clinical-analytics"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1006",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 35,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "User U302 enrolled in course C1006",
                "Goal G302-1 updated for user U302"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_08",
        "instruction": "Enroll Robert Thompson in UX Design Fundamentals course and update his Staff SRE goal to 40% progress using today's date.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Alexander",
                    "last_name": "Adams"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "UX Design Fundamentals"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U306",
                    "course_id": "C1002",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U306",
                    "goal_description_keywords": "Staff SRE"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {
                        "progress_percent": 40,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "User U306 enrolled in course C1002",
                "Goal G306-1 updated for user U306"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_09",
        "instruction": "Add Major Business Administration degree from University of Milwaukee for David Adams with today's graduation date, add AWS Security Specialty certification with exam scheduled 10 months from today, enroll him in Climate Science & Policy course, and update his AWS Security goal to 15% progress.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "generateUniqueEduId",
                "arguments": {
                    "prefix": "ED"
                },
            },
            {
                "name": "addUserEducation",
                "arguments": {
                    "user_id": "U303",
                    "education": {
                        "degree": "MBA",
                        "school": "University of Chicago",
                        "major": "Business Administration",
                        "graduation_date": "2025-07-04"
                    }
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U303",
                    "cert": {
                        "cert_name": "AWS Security Specialty",
                        "issuer": "AWS",
                        "scheduled_exam_date": "2026-05-04"
                    }
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Climate Science & Policy"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U303",
                    "course_id": "C1007",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U303",
                    "goal_description_keywords": "AWS Security"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 15,
                        "status": "Active",
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "Education MBA added for user U303",
                "Certification AWS Security Specialty added for user U303",
                "User U303 enrolled in course C1007",
                "Goal G303-1 updated for user U303"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_10",
        "instruction": "Establish a new mentorship for Ava Nguyen with Mentor M100, focusing on Product Marketing. Then, update her Product Marketing Specialist goal to 30% progress as of today.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Harper",
                    "last_name": "King"
                },
            },
            {
                "name": "assignMentor",
                "arguments": {
                    "mentee_id": "U305",
                    "mentor_id": "M100",
                    "focus_areas": [
                        "Product Marketing"
                    ],
                    "start_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U305",
                    "goal_description_keywords": "Product Marketing Specialist"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U305",
                    "goal_id": "G305-1",
                    "updates": {
                        "progress_percent": 30,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_11",
        "instruction": "Update Ava Nguyen's Machine Learning Specialization course progress to 80%, log a leadership skill gap analysis showing he needs Advanced level from current Intermediate, and update his Data Science goal to 50% progress.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "updateCourseProgress",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005",
                    "progress_percent": 80
                },
            },
            {
                "name": "generateUniqueAnalysisId",
                "arguments": {
                    "prefix": "SGA"
                },
            },
            {
                "name": "logSoftSkillGap",
                "arguments": {
                    "user_id": "U301",
                    "analysis": {
                        "analysis_id": "SGA001",
                        "skill": "leadership",
                        "current_proficiency": "Intermediate",
                        "required_proficiency": "Advanced",
                        "recommended_courses": []
                    }
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U301",
                    "goal_description_keywords": "Data Science"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 50,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "Course C1005 progress updated to 80% for user U301",
                "Skill gap analysis logged for user U301",
                "Goal G301-1 updated for user U301"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_12",
        "instruction": "Log job application for external candidate EXT001 to Product Marketing Specialist role with skill match score 85, schedule interview for 6 days from today, and update application status to Interview Scheduled.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "searchTalentNetwork",
                "arguments": {
                    "candidate_id": "EXT001"
                },
            },
            {
                "name": "getJobByTitle",
                "arguments": {
                    "job_title": "Product Marketing Specialist"
                },
            },
            {
                "name": "generateUniqueApplicationId",
                "arguments": {
                    "prefix": "APP"
                },
            },
            {
                "name": "logJobApplication",
                "arguments": {
                    "candidate_id": "EXT001",
                    "job_id": "J004",
                    "apply_date": "2025-07-04",
                    "skill_match_score": 85
                },
            },
            {
                "name": "getJobMarketInsights",
                "arguments": {
                    "role": "Product Marketing Specialist"
                },
            },
            {
                "name": "scheduleInterview",
                "arguments": {
                    "candidate_id": "EXT001",
                    "application_id": "APP001",
                    "interview_date": "2025-07-10"
                },
            },
            {
                "name": "updateApplication",
                "arguments": {
                    "candidate_id": "EXT001",
                    "application_id": "APP001",
                    "updates": {
                        "status": "Interview Scheduled",
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "Application logged for candidate EXT001",
                "Interview scheduled for 2025-07-10",
                "Application updated to Interview Scheduled"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_13",
        "instruction": "Mark Logan Garcia's Climate Science & Policy course as completed today, log mentoring session with mentor M101 for today on policy expertise, and update his AR training goal to 65% progress.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Owen",
                    "last_name": "Walker"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Climate Science & Policy"
                },
            },
            {
                "name": "logCourseCompletion",
                "arguments": {
                    "user_id": "U309",
                    "course_id": "C1007",
                    "completion_date": "2025-07-04"
                },
            },
            {
                "name": "logMentoringSession",
                "arguments": {
                    "mentee_id": "U309",
                    "mentor_id": "M101",
                    "session_date": "2025-07-04",
                    "notes": "Policy expertise development"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U309",
                    "goal_description_keywords": "AR"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U309",
                    "goal_id": "G309-1",
                    "updates": {
                        "progress_percent": 65,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "Course C1007 marked completed for user U309",
                "Mentoring session logged for U309",
                "Goal G309-1 updated for user U309"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_14",
        "instruction": "Enroll Owen Walker in UX Design Fundamentals course and update his Learning Analytics goal to 45% progress using today's date.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Lucas",
                    "last_name": "Young"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "UX Design Fundamentals"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U311",
                    "course_id": "C1002",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U311",
                    "goal_description_keywords": "Learning Analytics"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U311",
                    "goal_id": "G311-1",
                    "updates": {
                        "progress_percent": 45,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "User U311 enrolled in course C1002",
                "Course progress logged for U311",
                "Goal G311-1 updated for user U311"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_15",
        "instruction": "Enroll Emily Johnson in Data Visualization with Tableau course and update his UX Writer goal to 15% progress using today's date.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Henry",
                    "last_name": "Hassan"
                },
            },
            {
                "name": "getSkillGapAnalysis",
                "arguments": {
                    "user_id": "U308"
                },
            },
            {
                "name": "computeSkillGapScore",
                "arguments": {
                    "user_id": "U308"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U308",
                    "course_id": "C1003",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U308",
                    "goal_description_keywords": "UX Writer"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U308",
                    "goal_id": "G308-1",
                    "updates": {
                        "progress_percent": 15,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "User U308 enrolled in course C1003",
                "Goal G308-1 updated for user U308"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_16",
        "instruction": "Begin by verifying whether Harper Bennett's 'clinical-analytics' goal progress falls below 50%. Should this be the case, increase her progress by 15%. Subsequently, register her for the 'Advanced Python' course as support for this objective. Conclude by sending an email to her manager, Ava Nguyen, with the subject line 'Progress Update for Harper Bennett' and message content 'This communication confirms that Harper Bennett\\'s clinical analytics goal progress has been updated. Additionally, she has been registered in the Advanced Python course (C1001) to facilitate her development.'",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U302",
                    "goal_description_keywords": "clinical-analytics"
                },
            },
            {
                "name": "checkGoalProgressThreshold",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "threshold": 50,
                    "comparison": "below"
                },
            },
            {
                "name": "calculateProgressIncrement",
                "arguments": {
                    "current_progress": 0,
                    "increment": 15
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 15,
                        "last_updated": "2025-07-04"
                    }
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Advanced Python"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1001",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "searchUsers",
                "arguments": {
                    "filters": {
                        "user_id": "U302"
                    }
                },
            },
            {
                "name": "sendEmailToUser",
                "arguments": {
                    "user_id": "U301",
                    "subject": "Progress Update for Harper Bennett",
                    "body": "This is to confirm that Harper Bennett's clinical analytics goal progress has been updated. She has also been enrolled in the Advanced Python course (C1001) to support her development."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_17",
        "instruction": "Enroll David Adams in Data Visualization with Tableau course and update his AWS Security goal to 50% progress using today's date.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U303",
                    "goal_description_keywords": "AWS Security"
                },
            },
            {
                "name": "checkGoalProgressThreshold",
                "arguments": {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "threshold": 50,
                    "comparison": "below"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U303",
                    "course_id": "C1003",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 50,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "User U303 enrolled in course C1003",
                "Goal G303-1 updated for user U303"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_18",
        "instruction": "For Ava Nguyen, first check if his 'Advanced Python' course, and mark it as complete as of today. Then, find his goal related to becoming 'Director of Data Science' and increase its progress by 25%. Also, add the 'Advanced Python Certificate' from 'Coursera' to his profile. Finally, send him an email with the subject 'Course and Goal Progress Update' and body 'Congratulations on completing the Advanced Python course (C1001)! Your goal to become Director of Data Science has been updated, and the new certificate has been added to your profile.'",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Advanced Python"
                },
            },
            {
                "name": "checkCourseCompletionStatus",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1001"
                },
            },
            {
                "name": "markCourseCompleted",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1001",
                    "completion_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U301",
                    "goal_description_keywords": "Director of Data Science"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 50,
                        "last_updated": "2025-07-04"
                    }
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U301",
                    "cert": {
                        "cert_name": "Advanced Python Certificate",
                        "issuer": "Coursera",
                        "issue_date": "2025-07-04"
                    }
                },
            },
            {
                "name": "sendEmailToUser",
                "arguments": {
                    "user_id": "U301",
                    "subject": "Course and Goal Progress Update",
                    "body": "Congratulations on completing the Advanced Python course (C1001)! Your goal to become Director of Data Science has been updated, and the new certificate has been added to your profile."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_19",
        "instruction": "Enroll Harper Bennett in Machine Learning Specialization and Agile Product Management courses, add Machine Learning Professional certification from Coursera with exam scheduled 14 months from today, and update her clinical analytics goal to 30% progress.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "getSkillGapAnalysis",
                "arguments": {
                    "user_id": "U302"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1005",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Agile Product Management"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1006",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U302",
                    "cert": {
                        "cert_name": "Machine Learning Professional",
                        "issuer": "Coursera",
                        "scheduled_exam_date": "2026-09-04"
                    }
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U302",
                    "goal_description_keywords": "clinical analytics"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 30,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "User U302 enrolled in course C1005",
                "User U302 enrolled in course C1006",
                "Certification Machine Learning Professional added for user U302",
                "Goal G302-1 updated for user U302"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_20",
        "instruction": "Alexander Adams just graduated today with an MA in Organizational Leadership from Northwestern University and also received her Leadership Coach certification from ICF. First, add these two credentials to her profile. Based on these new qualifications, create a new high-priority 'Role Transition' goal for her with the description 'Transition to a Design Lead role within 18 months'. Then, assign Mentor M102 to her for 'Leadership' and 'Career Strategy' coaching. Finally, send an email to her manager, Michael Rodriguez, with the subject 'Career Path Update for Alexander Adams' and body 'Alexander Adams has completed a new degree and certification in leadership. A new goal has been created to support her transition to a Design Lead role, and a Mentor has been assigned.'",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Scott"
                },
            },
            {
                "name": "addUserEducation",
                "arguments": {
                    "user_id": "U307",
                    "education": {
                        "degree": "MA",
                        "field": "Organizational Leadership",
                        "institution": "Northwestern University",
                        "grad_year": 2025
                    }
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U307",
                    "cert": {
                        "cert_name": "Leadership Coach",
                        "issuer": "ICF",
                        "issue_date": "2025-07-04"
                    }
                },
            },
            {
                "name": "addUserGoal",
                "arguments": {
                    "user_id": "U307",
                    "goal": {
                        "goal_type": "Role Transition",
                        "goal_description": "Transition to a Design Lead role within 18 months",
                        "priority": "High",
                        "status": "Active",
                        "last_updated": "2025-07-04"
                    }
                },
            },
            {
                "name": "assignMentor",
                "arguments": {
                    "mentee_id": "U307",
                    "mentor_id": "M102",
                    "focus_areas": [
                        "Leadership",
                        "Career Strategy"
                    ],
                    "start_date": "2025-07-04"
                },
            },
            {
                "name": "searchUsers",
                "arguments": {
                    "filters": {
                        "user_id": "U307"
                    }
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Adams"
                },
            },
            {
                "name": "sendEmailToUser",
                "arguments": {
                    "user_id": "U304",
                    "subject": "Career Path Update for Alexander Adams",
                    "body": "Alexander Adams has completed a new degree and certification in leadership. A new goal has been created to support her transition to a Design Lead role, and a Mentor has been assigned."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_21",
        "instruction": "Add MS in Data Engineering from Stanford University for Ava Nguyen with today's graduation date, enroll him in Machine Learning Specialization course, add Google Cloud Professional Data Engineer certification from Google with exam scheduled 13 months from today, and update his Data Science goal to 60% progress.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "generateUniqueEduId",
                "arguments": {
                    "prefix": "ED"
                },
            },
            {
                "name": "addUserEducation",
                "arguments": {
                    "user_id": "U301",
                    "education": {
                        "degree": "M.S.",
                        "school": "Stanford University",
                        "major": "Data Engineering",
                        "graduation_date": "2025-07-04"
                    }
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U301",
                    "cert": {
                        "cert_name": "Google Cloud Professional Data Engineer",
                        "issuer": "Google",
                        "scheduled_exam_date": "2026-08-04"
                    }
                },
            },
            {
                "name": "getAllGoals",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 60,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "Education M.S. added for user U301",
                "User U301 enrolled in course C1005",
                "Certification Google Cloud Professional Data Engineer added for user U301",
                "Goal G301-1 updated for user U301"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_22",
        "instruction": "Assign mentor M101 to Michael Rodriguez with focus on Interaction Design starting today, enroll him in Agile Product Management course, and update his DesignOps goal to 45% progress.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Adams"
                },
            },
            {
                "name": "getAllGoals",
                "arguments": {
                    "user_id": "U304"
                },
            },
            {
                "name": "assignMentor",
                "arguments": {
                    "user_id": "U304",
                    "mentor_id": "M101",
                    "focus_areas": [
                        "Interaction Design"
                    ],
                    "start_date": "2025-07-04"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Agile Product Management"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U304",
                    "course_id": "C1006",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U304",
                    "goal_id": "G304-1",
                    "updates": {
                        "progress_percent": 45,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "Mentor M101 assigned to U304",
                "User U304 enrolled in course C1006",
                "Goal G304-1 updated for user U304"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_23",
        "instruction": "Today is 2025-07-04 Mark Alexander Adams as completed in change management training session TS004 today, enroll her in the Agile Product Management course, add a Professional Scrum Master certification from Scrum.org with an exam scheduled on 2026-08-04, and update her Accessibility goal to 55% progress.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Scott"
                },
            },
            {
                "name": "updateTeamTrainingLog",
                "arguments": {
                    "training_session_id": "TS004",
                    "user_id": "U307",
                    "status": "Completed",
                    "completion_date": "2025-07-04",
                    "skills_gained": [
                        "Change Management"
                    ]
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Agile Product Management"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U307",
                    "course_id": "C1006",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U307",
                    "cert": {
                        "cert_name": "Professional Scrum Master",
                        "issuer": "Scrum.org",
                        "issue_date": null,
                        "expiry_date": null,
                        "scheduled_exam_date": "2026-08-04"
                    }
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U307",
                    "goal_description_keywords": "Accessibility"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "updates": {
                        "progress_percent": 55,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_24",
        "instruction": "Mark Emily Johnson as completed in training session TS010 today, enroll him in the UX Design Fundamentals course, add a Technical Writing Professional certification from STC, and update his UX Writer goal to 35% progress.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Henry",
                    "last_name": "Hassan"
                },
            },
            {
                "name": "updateTeamTrainingLog",
                "arguments": {
                    "training_session_id": "TS010",
                    "user_id": "U308",
                    "status": "Completed",
                    "completion_date": "2025-07-04",
                    "skills_gained": []
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "UX Design Fundamentals"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U308",
                    "course_id": "C1002",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U308",
                    "cert": {
                        "cert_name": "Technical Writing Professional",
                        "issuer": "STC",
                        "issue_date": "2025-07-04"
                    }
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U308",
                    "goal_description_keywords": "UX Writer"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U308",
                    "goal_id": "G308-1",
                    "updates": {
                        "progress_percent": 35,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_25",
        "instruction": "First, check the severity of Ava Nguyen's 'Machine Learning' skill gap. If the severity is 'High', enroll him in the 'Machine Learning Specialization' course. Then, find his goal related to becoming 'Director of Data Science' and update its progress to 50% and its metric to 'Complete course and publish 2 models'. Finally, notify his mentor, with the message: 'Action plan initiated for Ava Nguyen: Enrolled in Machine Learning Specialization to address a high-severity skill gap. Goal has been updated accordingly.'",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "checkSkillGapSeverity",
                "arguments": {
                    "user_id": "U301",
                    "skill": "Machine Learning"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U301",
                    "goal_description_keywords": "Director of Data Science"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 50,
                        "metric": "Complete C1005 and publish 2 models",
                        "last_updated": "2025-07-04"
                    }
                },
            },
            {
                "name": "listUserMentors",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "updateMentorshipNote",
                "arguments": {
                    "mentor_id": "M102",
                    "mentee_id": "U301",
                    "note": "Action plan initiated for Ava Nguyen: Enrolled in Machine Learning Specialization to address a high-severity skill gap. Goal has been updated accordingly."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_26",
        "instruction": "First, check if the Product Design Team's training hours are below the 150-hour threshold. If they are, schedule the 'Project Management Professional (PMP)' training for them on August 1, 2025, and bulk-enroll the entire team as of today. Then, to align with this new training, update the priority of all 'Role Transition' goals for this team to 'High'. Finally, notify HR with the message: 'Product Design Team (T002) scheduled for PMP training (C1004) and enrolled. Related Role Transition goals have been prioritized.'",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "searchTeams",
                "arguments": {
                    "filters": {
                        "team_name": "Product Design Team"
                    }
                },
            },
            {
                "name": "checkTeamTrainingThreshold",
                "arguments": {
                    "team_id": "T002",
                    "threshold": 150,
                    "comparison": "below"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Project Management Professional (PMP)"
                },
            },
            {
                "name": "scheduleTeamTraining",
                "arguments": {
                    "team_id": "T002",
                    "course_id": "C1004",
                    "session_date": "2025-08-01"
                },
            },
            {
                "name": "bulkEnrollTeam",
                "arguments": {
                    "team_id": "T002",
                    "course_id": "C1004",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "bulkUpdateTeamGoals",
                "arguments": {
                    "team_id": "T002",
                    "goal_type": "Role Transition",
                    "updates": {
                        "priority": "High"
                    }
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Product Design Team (T002) scheduled for PMP training (C1004) and enrolled. Related Role Transition goals have been prioritized."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_27",
        "instruction": "Assess Emily Johnson's skill gaps, enroll him in Data Visualization with Tableau course, and update his UX Writer goal to 20% progress using today's date.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Henry",
                    "last_name": "Hassan"
                },
            },
            {
                "name": "getSkillGapAnalysis",
                "arguments": {
                    "user_id": "U308"
                },
            },
            {
                "name": "computeSkillGapScore",
                "arguments": {
                    "user_id": "U308"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U308",
                    "goal_description_keywords": "UX Writer"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U308",
                    "course_id": "C1003",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U308",
                    "goal_id": "G308-1",
                    "updates": {
                        "progress_percent": 20,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "User U308 enrolled in course C1003",
                "Goal G308-1 updated for user U308"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_28",
        "instruction": "First, check if Harper Bennett has any existing certification goals related to 'Clinical Data'. If not, add the 'Clinical Data Management Professional' certification from SCDM to her profile, with an exam scheduled 9 months from today. Then, create a new high-priority certification goal for her with the description 'Achieve Clinical Data Management Professional certification to deepen domain expertise', a timeframe of 12 months. Also, assign Mentor M100 to her for 'Python' and 'Career Strategy' coaching. Finally, notify her manager, Ava Nguyen, with the message: 'A new certification goal for Clinical Data Management has been created for Harper Bennett. A Mentor has been assigned to support her.'",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U302",
                    "goal_type": "Certification",
                    "goal_description_keywords": "Clinical Data"
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U302",
                    "cert": {
                        "cert_name": "Clinical Data Management Professional",
                        "issuer": "SCDM",
                        "scheduled_exam_date": "2026-04-04"
                    }
                },
            },
            {
                "name": "addUserGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal": {
                        "goal_type": "Certification",
                        "goal_description": "Achieve Clinical Data Management Professional certification to deepen domain expertise",
                        "target_certification": "Clinical Data Management Professional",
                        "timeframe": "12 months",
                        "priority": "High",
                        "status": "Active",
                        "last_updated": "2025-07-04"
                    }
                },
            },
            {
                "name": "assignMentor",
                "arguments": {
                    "mentee_id": "U302",
                    "mentor_id": "M100",
                    "focus_areas": [
                        "Python",
                        "Career Strategy"
                    ],
                    "start_date": "2025-07-04"
                },
            },
            {
                "name": "searchUsers",
                "arguments": {
                    "filters": {
                        "user_id": "U302"
                    }
                },
            },
            {
                "name": "sendEmailToUser",
                "arguments": {
                    "user_id": "U301",
                    "subject": "New Development Plan for Harper Bennett",
                    "body": "A new certification goal for Clinical Data Management has been created for Harper Bennett. A Mentor has been assigned to support her."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_29",
        "instruction": "Begin by examining Logan Garcia's 'AR-based onboarding' goal to determine if it falls below 20% progress. Subsequently, adjust its progress to 20%. Next, register him for the 'Project Management Professional (PMP)' course to assist with this project management. Conclude by informing his manager, who is also Logan Garcia, using the subject 'Goal Update and New Enrollment for Logan Garcia' and message 'Logan Garcia\\'s AR onboarding goal has been adjusted to 20% progress. He has also been registered in the PMP course to support this initiative.'",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Owen",
                    "last_name": "Walker"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U309",
                    "goal_description_keywords": "AR-based onboarding"
                },
            },
            {
                "name": "checkGoalProgressThreshold",
                "arguments": {
                    "user_id": "U309",
                    "goal_id": "G309-1",
                    "threshold": 20,
                    "comparison": "below"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U309",
                    "goal_id": "G309-1",
                    "updates": {
                        "progress_percent": 20,
                        "last_updated": "2025-07-04"
                    }
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Project Management Professional (PMP)"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U309",
                    "course_id": "C1004",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "searchUsers",
                "arguments": {
                    "filters": {
                        "user_id": "U309"
                    }
                },
            },
            {
                "name": "sendEmailToUser",
                "arguments": {
                    "user_id": "U309",
                    "subject": "Goal Update and New Enrollment for Logan Garcia",
                    "body": "Logan Garcia's AR onboarding goal has been updated to 20% progress. He has also been enrolled in the PMP course to support this initiative."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_30",
        "instruction": "First, check if Mentor M102's current mentee load is below their capacity of 4. If it is, assign Alexander Adams to them for 'People Analytics' and 'Leadership' coaching. Then, create a new 'Role Transition' goal for Harper with the description 'Transition to People Analytics Lead' and enroll her in the 'Data Visualization with Tableau' course. Finally, send an email to Harper with the subject 'Your New Development Plan' and body 'You have been assigned to Mentor M102. A new goal has been created for your transition to People Analytics Lead, and you have been enrolled in the Data Visualization with Tableau course.'",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getMentor",
                "arguments": {
                    "mentor_id": "M102"
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M102"
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Harper",
                    "last_name": "Bennett"
                },
            },
            {
                "name": "assignMentor",
                "arguments": {
                    "mentee_id": "U310",
                    "mentor_id": "M102",
                    "focus_areas": [
                        "People Analytics",
                        "Leadership"
                    ],
                    "start_date": "2025-07-04"
                },
            },
            {
                "name": "addUserGoal",
                "arguments": {
                    "user_id": "U310",
                    "goal": {
                        "goal_type": "Role Transition",
                        "goal_description": "Transition to People Analytics Lead",
                        "target_role": "People Analytics Lead",
                        "status": "Active",
                        "last_updated": "2025-07-04"
                    }
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U310",
                    "course_id": "C1003",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "sendEmailToUser",
                "arguments": {
                    "user_id": "U310",
                    "subject": "Your New Development Plan",
                    "body": "You have been assigned to Mentor M102. A new goal has been created for your transition to People Analytics Lead, and you have been enrolled in the Data Visualization with Tableau course."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_31",
        "instruction": "First, check if the Data Analytics Team's average course progress is below 70%. If it is, schedule the 'Machine Learning Specialization' training for them on September 20, 2025. Then, bulk-enroll all team members in this new course. Also, update all of the team's 'Role Transition' goals to a 'High' priority. Finally, notify HR with the message: 'The Data Analytics Team (T001) has been scheduled for and enrolled in the Machine Learning Specialization (C1005) course. All related Role Transition goals have been prioritized.'",
        "actions": [
            {
                "name": "searchTeams",
                "arguments": {
                    "filters": {
                        "team_name": "Data Analytics Team"
                    }
                },
            },
            {
                "name": "checkTeamAverageThreshold",
                "arguments": {
                    "team_id": "T001",
                    "threshold": 70,
                    "comparison": "below"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "scheduleTeamTraining",
                "arguments": {
                    "team_id": "T001",
                    "course_id": "C1005",
                    "session_date": "2025-09-20"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "bulkEnrollTeam",
                "arguments": {
                    "team_id": "T001",
                    "course_id": "C1005",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "bulkUpdateTeamGoals",
                "arguments": {
                    "team_id": "T001",
                    "goal_type": "Role Transition",
                    "updates": {
                        "priority": "High"
                    }
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "The Data Analytics Team (T001) has been scheduled for and enrolled in the Machine Learning Specialization (C1005) course. All related Role Transition goals have been prioritized."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_32",
        "instruction": "Assess Alexander Adams's current progress, get UX Designer market insights, enroll her in Data Visualization with Tableau course, and update her Accessibility goal to 80% progress using today's date.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Scott"
                },
            },
            {
                "name": "computeAverageProgress",
                "arguments": {
                    "user_id": "U307"
                },
            },
            {
                "name": "getJobMarketInsights",
                "arguments": {
                    "role": "UX Designer"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U307",
                    "course_id": "C1003",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U307",
                    "goal_description_keywords": "Accessibility"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "updates": {
                        "progress_percent": 80,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "User U307 enrolled in course C1003",
                "Goal G307-1 updated for user U307"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_33",
        "instruction": "First, assess Ava Nguyen's readiness score for his 'Director of Data Science' goal. If his score is above 60, enroll him in the 'Project Management Professional (PMP)' course to build leadership skills and update his goal's metric to include 'Complete PMP certification'. Finally, notify his mentor, M102, with the message: 'Ava Nguyen has met the readiness threshold for his Director goal. He has been enrolled in the PMP course and his goal has been updated.'",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "getSkillGapAnalysis",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "checkReadinessThreshold",
                "arguments": {
                    "user_id": "U301",
                    "threshold": 60,
                    "comparison": "above"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Project Management Professional (PMP)"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1004",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U301",
                    "goal_description_keywords": "Director of Data Science"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "metric": "Complete PMP certification",
                        "last_updated": "2025-07-04"
                    }
                },
            },
            {
                "name": "listUserMentors",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "updateMentorshipNote",
                "arguments": {
                    "mentor_id": "M102",
                    "mentee_id": "U301",
                    "note": "Ava Nguyen has met the readiness threshold for his Director goal. He has been enrolled in the PMP course and his goal has been updated."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_34",
        "instruction": "Check Robert Thompson's AWS certification expiry, add AWS Solutions Architect Associate renewal certification with exam scheduled 4 months from today, enroll him in Project Management Professional course, update his Staff SRE goal to 35% progress, and notify HR of the certification renewal.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Alexander",
                    "last_name": "Adams"
                },
            },
            {
                "name": "listUserCertifications",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "computeCertExpiry",
                "arguments": {
                    "user_id": "U306",
                    "cert_id": "C7005"
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U306",
                    "cert": {
                        "cert_name": "AWS Solutions Architect Associate – Renewal",
                        "issuer": "AWS",
                        "scheduled_exam_date": "2025-11-04"
                    }
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Project Management Professional (PMP)"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U306",
                    "course_id": "C1004",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U306",
                    "goal_description_keywords": "Staff SRE"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {
                        "progress_percent": 35,
                        "last_updated": "2025-07-04"
                    }
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "AWS certification renewal scheduled for U306"
                }
            }
        ],
        "outputs": [
                "Certification AWS Solutions Architect Associate – Renewal added for user U306",
                "User U306 enrolled in course C1004",
                "Goal G306-1 updated for user U306"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_35",
        "instruction": "First, check if Mentor M103 has a current active mentee load below their capacity of 2. Then, assign Harper Bennett to them for 'Career Growth' and 'Skill Mastery' coaching as of today. After the assignment, create a new active 'Skill Mastery' goal for Ava with the description 'Master Python for clinical analytics with mentor guidance' and Python as a target skill to acquire. Finally, send an email to Ava with the subject 'New Mentor and Goal Assigned' and body 'You have been assigned to Mentor M103 for career growth. A new goal has been created to track your progress in mastering Python.'",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getMentor",
                "arguments": {
                    "mentor_id": "M103"
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M103"
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "assignMentor",
                "arguments": {
                    "mentee_id": "U302",
                    "mentor_id": "M103",
                    "focus_areas": [
                        "Career Growth",
                        "Skill Mastery"
                    ],
                    "start_date": "2025-07-04"
                },
            },
            {
                "name": "addUserGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal": {
                        "goal_type": "Skill Mastery",
                        "goal_description": "Master Python for clinical analytics with mentor guidance",
                        "target_skills_to_acquire": [
                            "Python"
                        ],
                        "status": "Active"
                    }
                },
            },
            {
                "name": "sendEmailToUser",
                "arguments": {
                    "user_id": "U302",
                    "subject": "New Mentor and Goal Assigned",
                    "body": "You have been assigned to Mentor M103 for career growth. A new goal has been created to track your progress in mastering Python."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_36",
        "instruction": "For Ava Nguyen of the Marketing Team, schedule Project Management Professional (PMP) training for August 15, 2025. Then, assign Mentor M102 for coaching on Product Marketing and Leadership. Finally, create a skill development plan for Harper focusing on Data Analytics and Brand Positioning, and notify HR that the optimization plan is complete.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Harper",
                    "last_name": "King"
                },
            },
            {
                "name": "searchTeams",
                "arguments": {
                    "filters": {
                        "team_name": "Marketing Team"
                    }
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Project Management Professional (PMP)"
                },
            },
            {
                "name": "scheduleTeamTraining",
                "arguments": {
                    "team_id": "T004",
                    "course_id": "C1004",
                    "session_date": "2025-08-15"
                },
            },
            {
                "name": "assignMentor",
                "arguments": {
                    "mentee_id": "U305",
                    "mentor_id": "M102",
                    "focus_areas": [
                        "Product Marketing",
                        "Leadership"
                    ],
                    "start_date": "2025-07-04"
                },
            },
            {
                "name": "createSkillDevelopmentPlan",
                "arguments": {
                    "user_id": "U305",
                    "focus_areas": [
                        "Data Analytics",
                        "Brand Positioning"
                    ]
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Team T004 performance optimization complete. Training scheduled for course C1004. Mentor M102 assigned to user U305. New skill plan created."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_37",
        "instruction": "First, check if the Compliance Team's average course progress is below 50%. Then, bulk-enroll the team in the 'Project Management Professional (PMP)' course as of today. Then, to align with this new training, perform a bulk update on all 'Certification' goals for this team, setting their priority to 'High'. Finally, notify the team lead, David Adams, with the subject 'Compliance Team Development Initiative' and body 'The Compliance team (T005) has been enrolled in PMP training (C1004) due to progress metrics. All related certification goals have been prioritized.'",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "searchTeams",
                "arguments": {
                    "filters": {
                        "team_name": "Compliance Team"
                    }
                },
            },
            {
                "name": "checkTeamAverageThreshold",
                "arguments": {
                    "team_id": "T005",
                    "threshold": 50,
                    "comparison": "below"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Project Management Professional (PMP)"
                },
            },
            {
                "name": "bulkEnrollTeam",
                "arguments": {
                    "team_id": "T005",
                    "course_id": "C1004",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "bulkUpdateTeamGoals",
                "arguments": {
                    "team_id": "T005",
                    "goal_type": "Certification",
                    "updates": {
                        "priority": "High"
                    }
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "sendEmailToUser",
                "arguments": {
                    "user_id": "U303",
                    "subject": "Compliance Team Development Initiative",
                    "body": "The Compliance team (T005) has been enrolled in PMP training (C1004) due to progress metrics. All related certification goals have been prioritized."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_38",
        "instruction": "Check Robert Thompson's Terraform skill gap severity, add a HashiCorp Terraform Associate certification with an issue date 2 months ago, enroll him in the Data Visualization with Tableau course, update his Staff SRE goal to 50% progress, and send a confirmation email with subject: 'Confirmation of your development plan updates' and body: 'This is to confirm the following updates to your career plan: A new certification (HashiCorp Terraform Associate) has been added. You have been enrolled in course C1003. Your goal G306-1 has been updated.'.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Alexander",
                    "last_name": "Adams"
                },
            },
            {
                "name": "getSkillGapAnalysis",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "checkSkillGapSeverity",
                "arguments": {
                    "user_id": "U306",
                    "skill": "Terraform"
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U306",
                    "cert": {
                        "cert_name": "HashiCorp Terraform Associate",
                        "issuer": "HashiCorp",
                        "issue_date": "2025-05-04"
                    }
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U306",
                    "course_id": "C1003",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U306",
                    "goal_description_keywords": "Staff SRE"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {
                        "progress_percent": 50,
                        "last_updated": "2025-07-04"
                    }
                },
            },
            {
                "name": "sendEmailToUser",
                "arguments": {
                    "user_id": "U306",
                    "subject": "Confirmation of your development plan updates",
                    "body": "This is to confirm the following updates to your career plan: A new certification (HashiCorp Terraform Associate) has been added. You have been enrolled in course C1003. Your goal G306-1 has been updated."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_39",
        "instruction": "Assess Emily Johnson's skill gaps and readiness against 85% threshold, enroll him in UX Design Fundamentals course, and update his UX Writer goal to 25% progress using today's date.",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Henry",
                    "last_name": "Hassan"
                },
            },
            {
                "name": "getSkillGapAnalysis",
                "arguments": {
                    "user_id": "U308"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "computeSkillGapScore",
                "arguments": {
                    "user_id": "U308"
                },
            },
            {
                "name": "checkReadinessThreshold",
                "arguments": {
                    "user_id": "U308",
                    "threshold": 85,
                    "comparison": "below"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "UX Design Fundamentals"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U308",
                    "course_id": "C1002",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "getUserGoalsByType",
                "arguments": {
                    "user_id": "U308",
                    "goal_description_keywords": "UX Writer"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U308",
                    "goal_id": "G308-1",
                    "updates": {
                        "progress_percent": 25,
                        "last_updated": "2025-07-04"
                    }
                }
            }
        ],
        "outputs": [
                "User U308 enrolled in course C1002",
                "Goal G308-1 updated for user U308"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_40",
        "instruction": "For Logan Garcia, first check if he is already enrolled in the 'Data Visualization with Tableau' course. Then, enroll him as of today. Then, create a new 'Skill Mastery' goal for him with the description 'Master Tableau for L&D reporting' and a timeframe of 6 months. Finally, send an email to his manager, who is also Logan Garcia, with the subject 'New Development Action for Logan Garcia' and body 'Logan Garcia has been enrolled in the Data Visualization with Tableau course and a new supporting goal has been created.'",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Owen",
                    "last_name": "Walker"
                },
            },
            {
                "name": "getCourseByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "listUserCourses",
                "arguments": {
                    "user_id": "U309"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U309",
                    "course_id": "C1003",
                    "enroll_date": "2025-07-04"
                },
            },
            {
                "name": "addUserGoal",
                "arguments": {
                    "user_id": "U309",
                    "goal": {
                        "goal_type": "Skill Mastery",
                        "goal_description": "Master Tableau for L&D reporting",
                        "target_skills_to_acquire": [
                            "Tableau"
                        ],
                        "timeframe": "6 months",
                        "status": "Active",
                        "last_updated": "2025-07-04"
                    }
                },
            },
            {
                "name": "searchUsers",
                "arguments": {
                    "filters": {
                        "user_id": "U309"
                    }
                },
            },
            {
                "name": "sendEmailToUser",
                "arguments": {
                    "user_id": "U309",
                    "subject": "New Development Action for Logan Garcia",
                    "body": "Logan Garcia has been enrolled in the Data Visualization with Tableau course and a new supporting goal has been created."
                }
            }
        ],
        "outputs": []
    }
]
