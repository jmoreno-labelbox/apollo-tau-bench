"""
This module defines a comprehensive list of 100 single-turn task instances
for the banking_services_interface_1 domain.

Each task represents a realistic user interaction scenario involving one or more
API tools. Tasks include a natural language instruction, a sequence of actions
(invocations of specific tools with parameters), and expected outputs.

The tasks are used for validating tool composition, API correctness,
and grounding behavior in a multi-step interaction simulation.

All actions use only the 26 officially supported tools in this interface.

Attributes:
    TASKS (List[Task]): A list of 100 annotated task instances used
                        for toolchain evaluation and benchmarking.

Example:
    TASKS = [
        Task(
            annotator="0",
            user_id="account_recovery_unit",
            instruction="Retrieve statements and summarize loan activity...",
            actions=[Action(name="GetCustomerProfile", kwargs={...}), ...],
            outputs=[...]
        ),
        ...
    ]
"""

from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="user_001",
        instruction=(
            "Handle the setup of a joint account for Sofia Andersson (customer ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "Begin by confirming her identity with passport 'passport_10000001'. "
            "Update her contact details to email 'sofia.andersson@example.com' and phone '+1-202-555-0143'. "
            "Enable notifications. "
            "Following this, review the balance and linked beneficiaries on account 'acc_chk_1001'. "
            "Lastly, coordinate the submission of a medium-priority support ticket through Web under the category 'Joint Account', using ticket ID 'tkt_d6e5f4a3-f4a3-b2c1-d0e9-f8g7h6i5j4k3', including the note: 'Setup joint account for customer_id=c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e on account acc_chk_1001'."
        ),
        actions=[
            Action(
                name="VerifyCustomerIdentity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "passport_10000001",
                },
            ),
            Action(
                name="UpdateCustomerEmail",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "new_email": "sofia.andersson@example.com",
                    "new_phone": "+1-202-555-0143",
                },
            ),
            Action(
                name="UpdateAccountPreferences",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "notifications_enabled": True,
                },
            ),
            Action(
                name="GetAccountBalance",
                kwargs={"account_id": "acc_chk_1001"},
            ),
            Action(
                name="GetAccountTransactionHistory",
                kwargs={"account_id": "acc_chk_1001"},
            ),
            Action(
                name="ListLinkedBeneficiaries",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "category": "Joint Account",
                    "priority": "Medium",
                    "channel": "Web",
                    "ticket_id": "tkt_d6e5f4a3-f4a3-b2c1-d0e9-f8g7h6i5j4k3",
                    "request_details": {
                        "target_entity": "Customer",
                        "target_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                        "parameters": {
                            "note": "Setup joint account for customer_id=c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e on account acc_chk_1001"
                        },
                    },
                },
            ),
        ],
        outputs=[
            "Joint account setup initiated for Sofia Andersson: identity confirmed, preferences saved, and support ticket tkt_d6e5f4a3-f4a3-b2c1-d0e9-f8g7h6i5j4k3 submitted."
        ],
    ),
    Task(
        annotator="0",
        user_id="user_002",
        instruction=(
            "Conduct Sofia Andersson' (customer ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) January 2023 financial review. "
            "Start by authenticating her identity with the document 'passport_10000002'. "
            "Analyze her spending activity on account 'acc_chk_1001', identify any suspicious actions, then update her email to 'sofia.andersson@example.com' and phone to '+44 7700 900125', enable notifications, and arrange a support ticket on the Web Portal within the 'Security' category, at 'High' priority, and request escalation of issues located on account 'acc_chk_1001'. "
            "The ticket needs to be assigned ID 'ticket_static_002' for traceability."
        ),
        actions=[
            Action(
                name="VerifyCustomerIdentity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "passport_10000002",
                },
            ),
            Action(
                name="AggregateMonthlyExpenses",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "month": "2023-01",
                },
            ),
            Action(
                name="DetectSuspiciousActivityAndAlert",
                kwargs={
                    "account_id": "acc_chk_1001",
                },
            ),
            Action(
                name="UpdateAccountPreferences",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "preferences": {
                        "notifications": True
                    },
                },
            ),
            Action(
                name="UpdateCustomerEmail",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "new_email": "sofia.andersson@example.com",
                    "new_phone": "+44 7700 900125",
                },
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "category": "Security",
                    "priority": "High",
                    "channel": "Web Portal",
                    "request_details": {
                        "target_entity": "Account",
                        "target_id": "acc_chk_1001",
                        "operation": "ESCALATE",
                        "parameters": {
                            "note": "Request to escalate issues found on account acc_chk_1001"
                        },
                    },
                    "ticket_id": "ticket_static_002",
                },
            ),
        ],
        outputs=[
            "January 2023 financial review completed for Sofia Andersson: expenses analyzed, account flagged for security, preferences updated, and support ticket 'ticket_static_002' submitted successfully."
        ],
    ),
    Task(
        annotator="0",
        user_id="user_003",
        instruction=(
            "Review Kenji Tanaka’s (customer ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) support interactions. "
            "Start with verifying his identity via passport 'lF146011'. "
            "Check his profile, enable notifications, set his language preference to 'en-US', and revise his email to 'kenji.tanaka@example.com' and phone to '+1-202-555-0199'. "
            "List current beneficiaries and delete Elena Popescu's existing record (ID: bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d). "
            "Re-register Elena Popescu immediately as a 'Spouse' linked to account '9876543210' at City National Bank (routing 122000661, USA), utilizing the beneficiary ID 'bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d'. "
            "Lastly, organize a support ticket with ID 'ticket_003' to the 'Escalation' category with 'High' priority through 'Internal System', detailing: 'Customer profile, preferences, and beneficiary list updated. "
            "Elena Popescu re-registered as Spouse.'."
        ),
        actions=[
            Action(
                name="VerifyCustomerIdentity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "lF146011",
                },
            ),
            Action(
                name="GetCustomerProfile",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            ),
            Action(
                name="UpdateAccountPreferences",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "preferences": {
                        "notifications": True,
                        "language": "en-US"
                    },
                },
            ),
            Action(
                name="UpdateCustomerEmail",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "new_email": "kenji.tanaka@example.com",
                    "new_phone": "+1-202-555-0199"
                },
            ),
            Action(
                name="ListLinkedBeneficiaries",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            ),
            Action(
                name="DeleteExistingBeneficiary",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d"
                },
            ),
            Action(
                name="RegisterNewBeneficiary",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d",
                    "beneficiary_name": "Elena Popescu",
                    "beneficiary_type": "Personal",
                    "relationship": "Spouse",
                    "country": "USA",
                    "bank_details": {
                        "account_number": "9876543210",
                        "bank_name": "City National Bank",
                        "routing_info": "122000661"
                    }
                },
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "category": "Escalation",
                    "priority": "High",
                    "channel": "Internal System",
                    "ticket_id": "ticket_003",
                    "request_details": "Customer profile, preferences, and beneficiary list updated. Elena Popescu re-registered as Spouse."
                }
            ),
        ],
        outputs=[
            "Customer verified, profile and preferences updated, beneficiary replaced, and escalation ticket ticket_003 submitted."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_004",
        instruction=(
            "For customer ID c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e, confirm identity via document passport_10000004. "
            "Then inspect their account acc_sav_2001 activity and loan application statuses, obtain the February 2023 account statement for that account, and organize a high-priority support ticket ID ticket_004 under category 'Account Review' via Internal System, documenting these steps: IDENTITY_VERIFIED, ACCOUNT_ACTIVITY_REVIEWED, LOANS_CHECKED, STATEMENT_DOWNLOADED."
        ),
        actions=[
            Action(
                name="VerifyCustomerIdentity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "passport_10000004"
                },
            ),
            Action(
                name="GetAccountTransactionHistory",
                kwargs={
                    "account_id": "acc_sav_2001"
                },
            ),
            Action(
                name="SummarizeLoanApplicationsByStatus",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            ),
            Action(
                name="DownloadStatementByDate",
                kwargs={
                    "account_id": "acc_sav_2001",
                    "month": "2023-02"
                },
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "category": "Account Review",
                    "priority": "High",
                    "channel": "Internal System",
                    "ticket_id": "ticket_004",
                    "request_details": {
                        "target_entity": "Customer",
                        "target_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                        "operation": "ACCOUNT_REVIEW_LOG",
                        "parameters": {
                            "steps_completed": [
                                "IDENTITY_VERIFIED",
                                "ACCOUNT_ACTIVITY_REVIEWED",
                                "LOANS_CHECKED",
                                "STATEMENT_DOWNLOADED"
                            ]
                        }
                    }
                }
            )
        ],
        outputs=[
            "All review steps completed for customer c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e and ticket ticket_004 logged successfully."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_005",
        instruction=(
            "As a compliance officer, carry out a comprehensive audit for customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e): authenticate his identity using document passport_10000005, modify contact email to kenji.tanaka@example.com and phone to +55 21 98765-4321, enable notifications, evaluate transactions and monthly expenses on account acc_chk_1001 for the duration January to March 2023, download monthly statements for these months, search for any suspicious activities, and arrange a complete audit log submission to support under the 'Compliance' category, with 'High' priority, through Internal System."
        ),
        actions=[
            Action(
                name="VerifyCustomerIdentity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "passport_10000005"
                }
            ),
            Action(
                name="UpdateCustomerEmail",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "new_email": "kenji.tanaka@example.com",
                    "new_phone": "+55 21 98765-4321"
                }
            ),
            Action(
                name="UpdateAccountPreferences",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "preferences": {
                        "notifications": True
                    }
                }
            ),
            Action(
                name="GetAccountTransactionHistory",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "start_date": "2023-01-01",
                    "end_date": "2023-03-31"
                }
            ),
            Action(
                name="AggregateMonthlyExpenses",
                kwargs={"account_id": "acc_chk_1001", "month": "2023-01"}
            ),
            Action(
                name="AggregateMonthlyExpenses",
                kwargs={"account_id": "acc_chk_1001", "month": "2023-02"}
            ),
            Action(
                name="AggregateMonthlyExpenses",
                kwargs={"account_id": "acc_chk_1001", "month": "2023-03"}
            ),
            Action(
                name="DownloadStatementByDate",
                kwargs={"account_id": "acc_chk_1001", "month": "2023-01"}
            ),
            Action(
                name="DownloadStatementByDate",
                kwargs={"account_id": "acc_chk_1001", "month": "2023-02"}
            ),
            Action(
                name="DownloadStatementByDate",
                kwargs={"account_id": "acc_chk_1001", "month": "2023-03"}
            ),
            Action(
                name="DetectSuspiciousActivityAndAlert",
                kwargs={"account_id": "acc_chk_1001"}
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "category": "Compliance",
                    "priority": "High",
                    "channel": "Internal System",
                    "ticket_id": "ticket_005",
                    "request_details": {
                        "target_entity": "Customer",
                        "target_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                        "operation": "COMPLIANCE_AUDIT_LOG",
                        "parameters": {
                            "steps_completed": [
                                "IDENTITY_VERIFIED",
                                "CONTACT_UPDATED",
                                "NOTIFICATIONS_ENABLED",
                                "TRANSACTIONS_REVIEWED",
                                "EXPENSES_ANALYZED",
                                "STATEMENTS_DOWNLOADED",
                                "SUSPICIOUS_ACTIVITY_CHECKED"
                            ],
                            "document_used": "passport_10000005",
                            "account_id": "acc_chk_1001",
                            "months": ["2023-01", "2023-02", "2023-03"]
                        }
                    }
                }
            )
        ],
        outputs=[
            "Compliance audit finalized: all steps completed and logged in ticket_005 for customer c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_006",
        instruction=(
            "Handle a security concern for customer ID a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4. "
            "Start by verifying their identity using document passport_10000006. "
            "Subsequently, freeze their account acc_chk_1001 due to fraud alert: 'Multiple failed login attempts'. "
            "Modify the customer's contact email to secure.jane.doe@example.com and update the phone number to +55 21 99876-5432. "
            "In conclusion, submit a support ticket ticket_006 with category 'Security Alert', priority High, via Internal System, directed at the Customer entity, with operation SECURITY_ESCALATION_LOG, documenting steps: IDENTITY_VERIFIED, ACCOUNT_FROZEN, CONTACT_UPDATED."
        ),
        actions=[
            Action(
                name="VerifyCustomerIdentity",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "id_document": "passport_10000006"
                }
            ),
            Action(
                name="FreezeAccountOnFraudAlert",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "alert_reason": "Multiple failed login attempts"
                }
            ),
            Action(
                name="UpdateCustomerEmail",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "new_email": "secure.jane.doe@example.com",
                    "new_phone": "+55 21 99876-5432"
                }
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "category": "Security Alert",
                    "priority": "High",
                    "channel": "Internal System",
                    "ticket_id": "ticket_006",
                    "request_details": {
                        "target_entity": "Customer",
                        "target_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                        "operation": "SECURITY_ESCALATION_LOG",
                        "parameters": {
                            "steps_completed": [
                                "IDENTITY_VERIFIED",
                                "ACCOUNT_FROZEN",
                                "CONTACT_UPDATED"
                            ]
                        }
                    }
                }
            )
        ],
        outputs=[
            "Security escalation completed: identity verified, acc_chk_1001 frozen, contact info updated, ticket ticket_006 created."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_007",
        instruction=(
            "Aid customer ID f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9 with a joint account modification on account acc_chk_2001: remove joint account holder cust_joint_005, evaluate transactions from 2023-01-01 to 2023-03-31, register beneficiary Carlos Silva (ID ben_007_xyz123), Personal, Partner, account 5566778899 at Unity Bank (routing 110000000, USA), then submit support ticket ticket_007 with category 'Account Update', priority High, via Internal System, logging: JOINT_HOLDER_REMOVED, TRANSACTIONS_REVIEWED_Q1, BENEFICIARY_REGISTERED."
        ),
        actions=[
            Action(
                name="RemoveJointAccountHolder",
                kwargs={
                    "account_id": "acc_chk_2001",
                    "holder_id": "cust_joint_005"
                }
            ),
            Action(
                name="GetAccountTransactionHistory",
                kwargs={
                    "account_id": "acc_chk_2001",
                    "start_date": "2023-01-01",
                    "end_date": "2023-03-31"
                }
            ),
            Action(
                name="RegisterNewBeneficiary",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "beneficiary_name": "Carlos Silva",
                    "beneficiary_type": "Personal",
                    "relationship": "Partner",
                    "country": "USA",
                    "beneficiary_id": "ben_007_xyz123",
                    "bank_details": {
                        "account_number": "5566778899",
                        "bank_name": "Unity Bank",
                        "routing_info": "110000000"
                    }
                }
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "category": "Account Update",
                    "priority": "High",
                    "channel": "Internal System",
                    "ticket_id": "ticket_007",
                    "request_details": {
                        "target_entity": "Account",
                        "target_id": "acc_chk_2001",
                        "operation": "UPDATE",
                        "parameters": {
                            "steps_completed": [
                                "JOINT_HOLDER_REMOVED",
                                "TRANSACTIONS_REVIEWED_Q1",
                                "BENEFICIARY_REGISTERED"
                            ]
                        }
                    }
                }
            )
        ],
        outputs=[
            "Joint account holder removed, transactions reviewed, beneficiary ben_007_xyz123 registered, and ticket ticket_007 submitted."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_008",
        instruction=(
            "Assist customer ID a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4 with a financial health assessment on account acc_sav_5001: review transactions between January and March 2023, summarize January expenses, replace the beneficiary with ID bene_5e4f3a2b-1c9d-8e7f-6a5b-4c3d2e1f0a9b (Global ISP) by Elena Popescu (Personal, Friend), account 9876543210 at City National Bank (routing 122000661, USA), download the statement for March 2023, and submit support ticket ID ticket_008 with category 'Financial Health Check', priority Medium, via Internal System, recording all steps as completed: TRANSACTION_REVIEW_JAN_TO_MAR, EXPENSES_SUMMARIZED_JAN, BENEFICIARY_REPLACED, MARCH_STATEMENT_DOWNLOADED."
        ),
        actions=[
            Action(
                name="GetAccountTransactionHistory",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "start_date": "2023-01-01",
                    "end_date": "2023-03-31",
                },
            ),
            Action(
                name="AggregateMonthlyExpenses",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "month": "2023-01",
                },
            ),
            Action(
                name="DeleteExistingBeneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_id": "bene_5e4f3a2b-1c9d-8e7f-6a5b-4c3d2e1f0a9b",
                },
            ),
            Action(
                name="RegisterNewBeneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "Elena Popescu",
                    "beneficiary_type": "Personal",
                    "relationship": "Friend",
                    "country": "USA",
                    "bank_details": {
                        "account_number": "9876543210",
                        "bank_name": "City National Bank",
                        "routing_number": "122000661",
                    },
                },
            ),
            Action(
                name="DownloadStatementByDate",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "month": "2023-03"
                },
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "category": "Financial Health Check",
                    "priority": "Medium",
                    "channel": "Internal System",
                    "ticket_id": "ticket_008",
                    "request_details": {
                        "target_entity": "Customer",
                        "target_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                        "operation": "REVIEW",
                        "parameters": {
                            "steps_completed": [
                                "TRANSACTION_REVIEW_JAN_TO_MAR",
                                "EXPENSES_SUMMARIZED_JAN",
                                "BENEFICIARY_REPLACED",
                                "MARCH_STATEMENT_DOWNLOADED"
                            ]
                        },
                    },
                },
            ),
        ],
        outputs=[
            "Financial health check complete: transaction history reviewed, January expenses summarized, "
            "beneficiary replaced with Elena Popescu, March statement downloaded, and ticket ticket_008 submitted successfully."
        ],
    ),
    Task(
        annotator="0",
        user_id="user_009",
        instruction=(
            "Conduct an onboarding check for customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) on account acc_chk_1001. "
            "Begin by confirming identity using his passport 'lF146011'. "
            "Following this, analyze the account's January 2023 spending and check for any suspicious activity. "
            "Register beneficiary Carlos Silva (ID: ben_009_carlossilva), of type Personal and relationship Partner, with account number 5566778899 at Unity Bank (routing 110000000, USA). "
            "Conclude by submitting a high-priority support ticket (ID: ticket_009) via Internal System under category 'Onboarding', focusing on the customer and incorporating the report ONBOARDING_PASS."
        ),
        actions=[
            Action(
                name="VerifyCustomerIdentity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "lF146011",
                },
            ),
            Action(
                name="AggregateMonthlyExpenses",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "month": "2023-01",
                },
            ),
            Action(
                name="DetectSuspiciousActivityAndAlert",
                kwargs={
                    "account_id": "acc_chk_1001"
                },
            ),
            Action(
                name="RegisterNewBeneficiary",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "ben_009_carlossilva",
                    "beneficiary_name": "Carlos Silva",
                    "beneficiary_type": "Personal",
                    "relationship": "Partner",
                    "country": "USA",
                    "bank_details": {
                        "account_number": "5566778899",
                        "bank_name": "Unity Bank",
                        "routing_info": "110000000",
                    },
                },
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "category": "Onboarding",
                    "priority": "High",
                    "channel": "Internal System",
                    "ticket_id": "ticket_009",
                    "request_details": {
                        "target_entity": "Customer",
                        "target_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                        "parameters": {
                            "summary": "ONBOARDING_PASS"
                        }
                    }
                }
            )
        ],
        outputs=[
            "Customer onboarding complete: identity verified with passport 'lF146011', January 2023 expenses analyzed, "
            "suspicious activity checked, beneficiary ben_009_carlossilva registered, and support ticket ticket_009 submitted."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_010",
        instruction=(
            "Evaluate the balance of account acc_sav_2002 for savings evaluation, then coordinate a medium-priority support request via Internal System to enhance overdraft protection on account acc_chk_2001 using justification code OD_PROTECT_SAVINGS_LINKED, and enumerate all beneficiaries linked to the customer a1b2c3d4-e5f6-7890-1234-567890abcdef."
        ),
        actions=[
            Action(
                name="GetCustomerProfile",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
            ),
            Action(
                name="VerifyCustomerIdentity",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "passport_10000010"},
            ),
            Action(
                name="GetAccountBalance",
                kwargs={"account_id": "acc_sav_2002"},
            ),
            Action(
                name="GetAccountBalance",
                kwargs={"account_id": "acc_chk_2001"},
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "category": "Overdraft Protection",
                    "priority": "Medium",
                    "channel": "Internal System",
                    "request_details": {
                        "target_entity": "Account",
                        "target_id": "acc_chk_2001",
                        "operation": "REQUEST_INCREASE",
                        "parameters": {
                            "justification_code": "OD_PROTECT_SAVINGS_LINKED"
                        },
                    },
                },
            ),
            Action(
                name="ListLinkedBeneficiaries",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
            ),
            Action(
                name="UpdateAccountPreferences",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "preferences": {"notifications": True}},
            ),
        ],
        outputs=[
            "Savings balance reviewed. Overdraft request submitted with justification code OD_PROTECT_SAVINGS_LINKED and beneficiaries listed."
        ],
    ),
    Task(
        annotator='0',
        user_id='user_011',
        instruction=(
            "Authenticate customer Kenji Tanaka using his ID document ending in 6789 for customer ID "
            "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e. Then, retrieve his profile and the balance of his checking account acc_chk_1001. "
            "Submit a medium-priority support ticket via the Web Portal in the 'Account Issues' category with the request: "
            "'Customer reports incorrect charges in transaction history', and assign it the ID tkt_d6e5f4a3-f4a3-b2c1-d0e9-f8g7h6i5j4k3. "
            "Next, classify this same ticket (tkt_d6e5f4a3-f4a3-b2c1-d0e9-f8g7h6i5j4k3) using the same message. Finally, review the customer's ticket history "
            "and update their account preferences to receive alerts via Email."
        ),
        actions=[
            Action(
                name='VerifyCustomerIdentity',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'id_document': '6789'
                }
            ),
            Action(
                name='GetCustomerProfile',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e'
                }
            ),
            Action(
                name='GetAccountBalance',
                kwargs={
                    'account_id': 'acc_chk_1001'
                }
            ),
            Action(
                name='SubmitSupportTicket',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'category': 'Account Issues',
                    'priority': 'Medium',
                    'channel': 'Web Portal',
                    'request_details': 'Customer reports incorrect charges in transaction history.',
                    'ticket_id': 'tkt_d6e5f4a3-f4a3-b2c1-d0e9-f8g7h6i5j4k3'
                }
            ),
            Action(
                name='autoClassifySupportTicketPriority',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'ticket_id': 'tkt_d6e5f4a3-f4a3-b2c1-d0e9-f8g7h6i5j4k3',
                    'message': 'Customer reports incorrect charges in transaction history.'
                }
            ),
            Action(
                name='ReviewTicketHistory',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e'
                }
            ),
            Action(
                name='UpdateAccountPreferences',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'preferences': {
                        'communication_channel': 'Email'
                    }
                }
            )
        ],
        outputs=[
            'Identity verified for Kenji Tanaka using ID ending in 6789.',
            'Customer profile successfully retrieved.',
            'Balance retrieved for account acc_chk_1001.',
            'Support ticket tkt_d6e5f4a3-f4a3-b2c1-d0e9-f8g7h6i5j4k3 submitted via Web Portal under Account Issues.',
            'Support ticket tkt_d6e5f4a3-f4a3-b2c1-d0e9-f8g7h6i5j4k3 classified as Normal priority.'
            'Support ticket history reviewed.',
            'Notification preferences updated to Email.'
        ]
    ),
    Task(
        annotator="0",
        user_id="user_012",
        instruction=(
            "Validate the identity of customer Kenji Tanaka utilizing ID document ending in 6789 for customer ID c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e. "
            "Upon verification, register a high-priority support ticket through the Mobile App in the 'Card Services' category with priority High, detailing a delay in the receipt of his debit card following account approval using ticket ID ticket_002. "
            "Following this, ensure his checking account acc_chk_1001 is operational by retrieving its balance. "
            "Once confirmed, download the 2023-09 statement for that account and aggregate monthly expenses for 2023-09."
        ),
        actions=[
            Action(
                name="GetCustomerProfile",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="VerifyCustomerIdentity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "6789"
                }
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "category": "Card Services",
                    "priority": "High",
                    "channel": "Mobile App",
                    "ticket_id": "ticket_002",
                    "request_details": "Delay in receiving debit card after account approval"
                }
            ),
            Action(
                name="GetAccountBalance",
                kwargs={
                    "account_id": "acc_chk_1001"
                }
            ),
            Action(
                name="GetAccountTransactionHistory",
                kwargs={
                    "account_id": "acc_chk_1001"
                }
            ),
            Action(
                name="DownloadStatementByDate",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "month": "2023-09"
                }
            ),
            Action(
                name="AggregateMonthlyExpenses",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "month": "2023-09"
                }
            )
        ],
        outputs=[
            "Identity verified for Kenji Tanaka using ID ending in 6789.",
            "Support ticket ticket_002 filed under Card Services with high priority.",
            "Balance confirmed for account acc_chk_1001.",
            "September 2023 statement downloaded for acc_chk_1001."
        ]
    ),
    Task(
        annotator='0',
        user_id='user_013',
        instruction=(
            "Authenticate customer Kenji Tanaka using customer ID c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e and ID document ending in 6789. "
            "Then retrieve the full transaction history of his checking account acc_chk_1001. "
            "Generate a breakdown of his monthly expenses for 2023-09. "
            "Finally, update his notification preferences to receive alerts via Email."
        ),
        actions=[
            Action(
                name='VerifyCustomerIdentity',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'id_document': '6789'
                }
            ),
            Action(
                name='GetAccountTransactionHistory',
                kwargs={
                    'account_id': 'acc_chk_1001'
                }
            ),
            Action(
                name='AggregateMonthlyExpenses',
                kwargs={
                    'account_id': 'acc_chk_1001',
                    'month': '2023-09'
                }
            ),
            Action(
                name='UpdateAccountPreferences',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'preferences': {
                        'communication_channel': 'Email'
                    }
                }
            )
        ],
        outputs=[
            'Identity verified using customer ID and document.',
            'Transaction history retrieved for account acc_chk_1001.',
            'September 2023 expenses aggregated.',
            'Preferences updated to receive alerts via Email.'
        ]
    ),
    Task(
        annotator='0',
        user_id='user_014',
        instruction=(
            "Authenticate customer Kenji Tanaka using his ID document ending in 6789 for customer ID "
            "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e. Then retrieve his full profile and check the balance of "
            "his checking account acc_chk_1001. Download the September 2023 statement and review all transactions from that month. "
            "Generate a summary of monthly expenses for the same account and period. "
            "After confirming the account is active and linked, update John’s account preferences to receive alerts via SMS. "
            "Finally, unlock his account using the same ID document and the security code '123456'."
        ),
        actions=[
            Action(
                name='VerifyCustomerIdentity',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'id_document': '6789'
                }
            ),
            Action(
                name='GetCustomerProfile',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e'
                }
            ),
            Action(
                name='GetAccountBalance',
                kwargs={
                    'account_id': 'acc_chk_1001'
                }
            ),
            Action(
                name='DownloadStatementByDate',
                kwargs={
                    'account_id': 'acc_chk_1001',
                    'month': '2023-09'
                }
            ),
            Action(
                name='GetAccountTransactionHistory',
                kwargs={
                    'account_id': 'acc_chk_1001'
                }
            ),
            Action(
                name='AggregateMonthlyExpenses',
                kwargs={
                    'account_id': 'acc_chk_1001',
                    'month': '2023-09'
                }
            ),
            Action(
                name='UpdateAccountPreferences',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'preferences': {
                        'communication_channel': 'SMS'
                    }
                }
            ),
            Action(
                name='UnlockAccountBySecurityCheck',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'id_document': '6789',
                    'security_code': '123456'
                }
            )
        ],
        outputs=[
            'Identity verified for Kenji Tanaka using ID ending in 6789.',
            'Customer profile retrieved.',
            'Balance checked for account acc_chk_1001.',
            'Statement for September 2023 downloaded.',
            'Transaction history reviewed for September 2023.',
            'Monthly expenses aggregated.',
            'Preferences updated to SMS.',
            'Account successfully unlocked.'
        ]
    ),
    Task(
        annotator='0',
        user_id='user_015',
        instruction=(
            "Guide customer Kenji Tanaka through an advanced banking workflow. "
            "Begin by verifying his identity using customer ID c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e and ID document ending in 6789. "
            "Then retrieve the balance and transaction history of his checking account acc_chk_1001, and aggregate his expenses for September 2023. "
            "Submit a high-priority support ticket via Mobile App in the 'Card Services' category, using the message: 'Lost debit card, requesting new one', "
            "and assign it the ID ticket_555abcde. "
            "After that, review his support ticket history, update his preferences to receive alerts via Email, "
            "download his statement for September 2023, and finally unlock his account using the same ID and the security code 123456."
        ),
        actions=[
            Action(name='VerifyCustomerIdentity', kwargs={
                'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                'id_document': '6789'
            }),
            Action(name='GetAccountBalance', kwargs={
                'account_id': 'acc_chk_1001'
            }),
            Action(name='GetAccountTransactionHistory', kwargs={
                'account_id': 'acc_chk_1001'
            }),
            Action(name='AggregateMonthlyExpenses', kwargs={
                'account_id': 'acc_chk_1001',
                'month': '2023-09'
            }),
            Action(name='SubmitSupportTicket', kwargs={
                'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                'category': 'Card Services',
                'priority': 'High',
                'channel': 'Mobile App',
                'request_details': 'Lost debit card, requesting new one',
                'ticket_id': 'ticket_555abcde'
            }),
            Action(name='ReviewTicketHistory', kwargs={
                'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e'
            }),
            Action(name='UpdateAccountPreferences', kwargs={
                'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                'preferences': {
                    'communication_channel': 'Email'
                }
            }),
            Action(name='DownloadStatementByDate', kwargs={
                'account_id': 'acc_chk_1001',
                'month': '2023-09'
            }),
            Action(name='UnlockAccountBySecurityCheck', kwargs={
                'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                'id_document': '6789',
                'security_code': '123456'
            })
        ],
        outputs=[
            'Identity verified for customer Kenji Tanaka.',
            'Balance retrieved for checking account acc_chk_1001.',
            'Transaction history successfully retrieved.',
            'September 2023 expenses aggregated.',
            'Support ticket ticket_555abcde submitted under Card Services.',
            'Support ticket history reviewed.',
            'Notification preferences updated to Email.',
            'Statement for September 2023 downloaded.',
            'Account unlocked successfully.'
        ]
    ),
    Task(
        annotator="0",
        user_id="user_016",
        instruction=(
            "Handle the auditing of financial operations for customer Elena Popescu (Customer ID: a1b2c3d4-e5f6-7890-1234-567890abcdef), who holds checking account acc_chk_2001. "
            "Start by retrieving her profile and authenticating her identity with national ID 'jd195515'. "
            "Following this, examine all transactions from acc_chk_2001 for any suspicious activity. "
            "Subsequently, coordinate a payment of $150.00 USD from acc_chk_2001 to account 9876543210 on 2025-08-01. "
            "Then, create a support ticket with ID 'ticket_user_016_jane_recurring_gym' under the category 'Recurring Payment', with priority 'Medium', via 'Web Portal', targeting the 'Account' entity, and operation 'VERIFY_RECURRING'. "
            "Ensure to include the note: 'Recurring payment of $150.00 USD to 9876543210 for Gym Membership verified from account acc_chk_2001'. "
            "Conclusively, review the entire ticket history for Elena Popescu. "
            "Current date is 2025-07-24."
        ),
        actions=[
            Action(
                name="GetCustomerProfile",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
            ),
            Action(
                name="VerifyCustomerIdentity",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "id_document": "jd195515",
                },
            ),
            Action(
                name="GetAccountTransactionHistory",
                kwargs={"account_id": "acc_chk_2001"},
            ),
            Action(
                name="DetectSuspiciousActivityAndAlert",
                kwargs={"account_id": "acc_chk_2001"},
            ),
            Action(
                name="SchedulePaymentWithValidation",
                kwargs={
                    "from_account": "acc_chk_2001",
                    "to_account": "9876543210",
                    "amount": 150.00,
                    "currency": "USD",
                    "date": "2025-08-01"
                },
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "ticket_id": "ticket_user_016_jane_recurring_gym",
                    "category": "Recurring Payment",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "request_details": {
                        "target_entity": "Account",
                        "target_id": "acc_chk_2001",
                        "operation": "VERIFY_RECURRING",
                        "parameters": {
                            "note": (
                                "Recurring payment of $150.00 USD to 9876543210 for Gym Membership "
                                "verified from account acc_chk_2001"
                            )
                        },
                    },
                },
            ),
            Action(
                name="ReviewTicketHistory",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
            ),
        ],
        outputs=[
            "Customer profile for Elena Popescu retrieved.",
            "Identity verified using national ID jd195515.",
            "Transaction history for acc_chk_2001 reviewed and no suspicious activity found.",
            "Payment of $150.00 USD scheduled to account 9876543210 on 2025-08-01.",
            "Support ticket ticket_user_016_jane_recurring_gym submitted and history reviewed.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_017",
        instruction=(
            "Assist Kenji Tanaka (customer ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), linked with account acc_chk_1001, to update his list of beneficiaries. "
            "Begin by obtaining his full profile. "
            "Ensure to verify his identity with his passport 'lF146011'. "
            "Enumerate all presently linked beneficiaries and eliminate the one labeled 'Anytown Utility Services'. "
            "Add a new beneficiary using the ID 'bene_user_017_clara_james' for 'Clara James' with account number '1234567890123456' at 'Federal Bank' (routing: '012345678') in the 'USA', with the relationship 'Sister'. "
            "Afterward, download his latest statement for July 2025. "
            "Subsequently, log a support ticket with ID 'ticket_user_017_bene_audit', under 'Account Management' category, and 'Medium' priority via 'Web Portal'. "
            "Focus the ticket on the 'Beneficiary' entity for an 'AUDIT' operation, including the note: 'Validate beneficiary update request and confirm legitimacy'. "
            "Finally, examine his complete ticket history to confirm the process was properly recorded."
        ),
        actions=[
            Action(
                name="GetCustomerProfile",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            Action(
                name="VerifyCustomerIdentity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "lF146011",
                },
            ),
            Action(
                name="ListLinkedBeneficiaries",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            Action(
                name="DeleteExistingBeneficiary",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e",
                },
            ),
            Action(
                name="RegisterNewBeneficiary",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_user_017_clara_james",
                    "beneficiary_name": "Clara James",
                    "country": "USA",
                    "relationship": "Sister",
                    "bank_details": {
                        "account_number": "1234567890123456",
                        "bank_name": "Federal Bank",
                        "routing_info": "012345678",
                    },
                },
            ),
            Action(
                name="DownloadStatementByDate",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "month": "2025-07",
                },
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "ticket_id": "ticket_user_017_bene_audit",
                    "category": "Account Management",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "request_details": {
                        "target_entity": "Beneficiary",
                        "target_id": "bene_user_017_clara_james",
                        "operation": "AUDIT",
                        "parameters": {
                            "note": "Validate beneficiary update request and confirm legitimacy"
                        },
                    },
                },
            ),
            Action(
                name="ReviewTicketHistory",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
        ],
        outputs=[
            "Beneficiary 'Anytown Utility Services' successfully removed.",
            "New beneficiary 'Clara James' registered.",
            "Statement for July 2025 downloaded for account acc_chk_1001.",
            "Support ticket submitted for audit and history reviewed.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_018",
        instruction=(
            "As a financial analyst, coordinate a comprehensive audit for the customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), associated with account acc_sav_1002. "
            "Initially, retrieve his profile and authenticate his identity using his passport 'lF146011'. "
            "Aggregate the monthly expenses for this account for July 2025 and procure the corresponding monthly statement. "
            "Following this, submit a support ticket utilizing ID 'ticket_user_018_audit' under the 'Compliance' category, with 'High' priority, through 'Internal System', accompanied by the request particulars: 'Complete audit trail for monthly expenses and compliance log for July 2025.' Lastly, assess the whole ticket history for quality assurance."
        ),
        actions=[
            Action(
                name="GetCustomerProfile",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            Action(
                name="VerifyCustomerIdentity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "lF146011",
                },
            ),
            Action(
                name="AggregateMonthlyExpenses",
                kwargs={
                    "account_id": "acc_sav_1002",
                    "month": "2025-07",
                },
            ),
            Action(
                name="DownloadStatementByDate",
                kwargs={
                    "account_id": "acc_sav_1002",
                    "month": "2025-07",
                },
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "ticket_id": "ticket_user_018_audit",
                    "category": "Compliance",
                    "priority": "High",
                    "channel": "Internal System",
                    "request_details": "Complete audit trail for monthly expenses and compliance log for July 2025."
                },
            ),
            Action(
                name="ReviewTicketHistory",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
        ],
        outputs=[
            "Monthly expenses aggregated for July 2025 for account acc_sav_1002.",
            "Statement for account acc_sav_1002 downloaded.",
            "Compliance support ticket submitted successfully.",
            "Ticket history reviewed for audit assurance."
        ],
    ),
    Task(
        annotator="0",
        user_id="user_019",
        instruction=(
            "Manage a time-critical transfer operation for the customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) linked to account acc_chk_1001. "
            "Start by accessing his profile and verifying his identity using his passport 'lF146011'. "
            "Next, enumerate all linked beneficiaries and choose the one titled 'Anytown Utility Services'. "
            "Move $300.00 from account acc_chk_1001 to this beneficiary's account '5555666677'. "
            "Immediately afterwards, set up another payment of the same amount for 2025-08-01. "
            "Lastly, register a support ticket using ID 'ticket_user_019_payment_confirm', under the 'Payment' category, with 'Medium' priority via 'Web Portal', including the request details: 'Confirmation of immediate transfer and scheduled payment to Anytown Utility Services.'."
        ),
        actions=[
            Action(
                name="GetCustomerProfile",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            Action(
                name="VerifyCustomerIdentity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "lF146011",
                },
            ),
            Action(
                name="ListLinkedBeneficiaries",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            Action(
                name="TransferFundsWithLimitCheck",
                kwargs={
                    "from_account": "acc_chk_1001",
                    "to_account": "5555666677",
                    "amount": 300.00,
                },
            ),
            Action(
                name="SchedulePaymentWithValidation",
                kwargs={
                    "from_account": "acc_chk_1001",
                    "to_account": "5555666677",
                    "amount": 300.00,
                    "currency": "USD",
                    "date": "2025-08-01",
                },
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "ticket_id": "ticket_user_019_payment_confirm",
                    "category": "Payment",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "request_details": "Confirmation of immediate transfer and scheduled payment to Anytown Utility Services.",
                },
            ),
        ],
        outputs=[
            "Customer identity verified with passport 'lF146011'.",
            "Funds transferred to Anytown Utility Services.",
            "A new payment for 2025-08-01 has been scheduled.",
            "Support ticket submitted for payment confirmations.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_020",
        instruction=(
            "Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef), connected to account acc_chk_2001, needs her list of beneficiaries updated. "
            "Start by retrieving her profile and confirming her identity using national ID 'jd195515'. "
            "Subsequently, list his current beneficiaries and remove the one designated 'Kenji Tanaka'. "
            "Afterward, register a new beneficiary with ID 'bene_user_020_clara_james' for 'Clara James' with account number '5566778899' at 'Unity Bank' (routing: '110000000') in the 'USA'. "
            "Download his latest statement for July 2025. "
            "Finally, file a support ticket using ID 'ticket_user_020_bene_add' with 'Account Update' category, 'Medium' priority, through 'Web Portal', and request details: 'Please confirm that the beneficiary Kenji Tanaka has been removed and Clara James has been added for account acc_chk_2001.'."
        ),
        actions=[
            Action(
                name="GetCustomerProfile",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
            ),
            Action(
                name="VerifyCustomerIdentity",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "id_document": "jd195515",
                },
            ),
            Action(
                name="ListLinkedBeneficiaries",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
            ),
            Action(
                name="DeleteExistingBeneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f",
                },
            ),
            Action(
                name="RegisterNewBeneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_id": "bene_user_020_clara_james",
                    "beneficiary_name": "Clara James",
                    "country": "USA",
                    "bank_details": {
                        "account_number": "5566778899",
                        "bank_name": "Unity Bank",
                        "routing_info": "110000000",
                    },
                },
            ),
            Action(
                name="DownloadStatementByDate",
                kwargs={
                    "account_id": "acc_chk_2001",
                    "month": "2025-07",
                },
            ),
            Action(
                name="SubmitSupportTicket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "ticket_id": "ticket_user_020_bene_add",
                    "category": "Account Update",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "request_details": "Please confirm that the beneficiary Kenji Tanaka has been removed and Clara James has been added for account acc_chk_2001.",
                },
            ),
        ],
        outputs=[
            "Beneficiary 'Kenji Tanaka' successfully removed.",
            "New beneficiary 'Clara James' registered with account 5566778899.",
            "July 2025 statement downloaded for acc_chk_2001.",
            "Support ticket logged for beneficiary update verification.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_021",
        instruction=(
            "Handle a high-priority fraud response protocol for customer Chloe Dubois (ID: d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). "
            "Current date is 2025-07-24. "
            "Begin by retrieving his profile and verifying his identity using his driver's license 'Kt516858'. "
            "Quickly run a check for suspicious activity on his checking account 'acc_chk_8001' and consequently freeze the account with the reason 'Unauthorized access reported by customer'. "
            "Update his contact information to the new email 'h.muller.secure@example.de' and new phone '+49 171 7654321'. "
            "Next, create a new, secure checking account for him of type 'Checking', currency 'EUR', and with an initial limit of 0.0. "
            "Lastly, submit a support ticket with ID 'ticket_user_021_fraud_response' under category 'Security', priority 'High', via 'Internal System', with the request details: 'Fraud protocol executed for customer d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1. "
            "Old account frozen and new secure account created. "
            "Customer must be contacted for next steps.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "id_document": "Kt516858"}),
            Action(name="DetectSuspiciousActivityAndAlert", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_chk_8001", "alert_reason": "Unauthorized access reported by customer"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "new_email": "h.muller.secure@example.de", "new_phone": "+49 171 7654321"}),
            Action(name="CreateCustomerAccount", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "account_type": "Checking", "currency": "EUR", "initial_limit": 0.0}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "ticket_id": "ticket_user_021_fraud_response",
                "category": "Security",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Fraud protocol executed for customer d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1. Old account frozen and new secure account created. Customer must be contacted for next steps."
            }),
        ],
        outputs=[
            "Fraud response initiated: identity verified, account frozen, and contact info updated.",
            "A new secure account has been created for the customer.",
            "High-priority security ticket logged to document the incident and required follow-up.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_022",
        instruction=(
            "Assist customer Zoltan Nagy (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11) with starting a new loan application. "
            "Current date is 2025-07-24. "
            "Initially, get his profile and verify his identity using his passport 'Se620000'. "
            "Review his transaction history on his checking account 'acc_chk_12001' for the last 90 days to assess cash flow. "
            "Check his existing loan history, then submit a new application for a personal loan of 5000 EUR for the purpose 'Home Improvement'. "
            "Next, register a new beneficiary using the ID 'bene_user_022_dublin_reno' for 'Dublin Renovations' with account number 'IE29AIBK93118212345678' at 'AIB' (routing: 'AIBKIE2D') in 'Ireland'. "
            "Then, schedule a one-time payment of 250 EUR to this new beneficiary's account for an initial consultation, with the payment date set for '2025-08-01'. "
            "Lastly, submit a support ticket with ID 'ticket_user_022_loan_app' under category 'Loan Application', priority 'Medium', via 'Web Portal', with the request details 'New personal loan application submitted for Home Improvement. "
            "Consultation payment scheduled to contractor.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "id_document": "Se620000"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_12001", "days": 90}),
            Action(name="SummarizeLoanApplicationsByStatus", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="ApplyForLoanWithCheck", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "amount": 5000.0, "purpose": "Home Improvement"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "beneficiary_id": "bene_user_022_dublin_reno",
                "beneficiary_name": "Dublin Renovations",
                "country": "Ireland",
                "bank_details": {"account_number": "IE29AIBK93118212345678", "bank_name": "AIB", "routing_info": "AIBKIE2D"}
            }),
            Action(name="SchedulePaymentWithValidation", kwargs={
                "from_account": "acc_chk_12001",
                "to_account": "IE29AIBK93118212345678",
                "amount": 250.0,
                "currency": "EUR",
                "date": "2025-08-01"
            }),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "ticket_id": "ticket_user_022_loan_app",
                "category": "Loan Application",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "New personal loan application submitted for Home Improvement. Consultation payment scheduled to contractor."
            }),
        ],
        outputs=[
            "Identity of Zoltan Nagy verified and financial history reviewed.",
            "New loan application for 5000 EUR submitted for 'Home Improvement'.",
            "New beneficiary 'Dublin Renovations' registered and consultation payment scheduled.",
            "Support ticket logged for the loan application.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_023",
        instruction=(
            "Coordinate a comprehensive account management and quarterly audit for customer Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef) on her account acc_chk_2001. "
            "Initiate by obtaining her profile and verifying her identity with her national ID 'jd195515'. "
            "Add Zoltan Nagy (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) as a new joint account holder. "
            "Next, list all his beneficiaries and delete the one named 'Kenji Tanaka' (ID: bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f). "
            "Then, register a new beneficiary using ID 'bene_user_023_metro_power' for 'Metropolis Power & Light' with account number '9988776655' at 'First National Bank of Metropolis' (routing: '021200339') in the 'USA'. "
            "Following the beneficiary management, execute a Q2 2023 financial audit on account acc_chk_2001: aggregate monthly expenses for April, May, and June 2023. "
            "Finally, submit a support ticket with ID 'ticket_user_023_q2_audit' under category 'Audit', priority 'Medium', via 'Internal System', with the request details: 'Q2 2023 audit and account holder update complete for account acc_chk_2001.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="AddJointAccountHolder", kwargs={"account_id": "acc_chk_2001", "holder_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_user_023_metro_power",
                "beneficiary_name": "Metropolis Power & Light",
                "country": "USA",
                "bank_details": {"account_number": "9988776655", "bank_name": "First National Bank of Metropolis", "routing_info": "021200339"}
            }),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_2001", "month": "2023-04"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_2001", "month": "2023-05"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_2001", "month": "2023-06"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_023_q2_audit",
                "category": "Audit",
                "priority": "Medium",
                "channel": "Internal System",
                "request_details": "Q2 2023 audit and account holder update complete for account acc_chk_2001."
            }),
        ],
        outputs=[
            "Identity verified for Elena Popescu and Zoltan Nagy added as joint account holder.",
            "Beneficiary 'Kenji Tanaka' removed and 'Metropolis Power & Light' added.",
            "Q2 2023 financial audit completed: expenses aggregated for April, May, and June.",
            "An audit ticket was logged to document the account updates.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_024",
        instruction=(
            "Conduct a straightforward financial review for customer Kenji Tanaka (ID: e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2). "
            "First, obtain his profile and verify his identity using his driver's license 'im665671'. "
            "Following this, check the current balances of his checking account 'acc_chk_9001' and his credit card 'acc_crd_9002'. "
            "Retrieve the transaction history for his checking account for the last 60 days. "
            "Aggregate his monthly expenses for October 2023 on the same checking account and download the statement for that month. "
            "Finally, update his account preferences to set the language to 'fr-FR' and ensure notifications are enabled."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "id_document": "im665671"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_9001"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_crd_9002"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_9001", "days": 60}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_9001", "month": "2023-10"}),
            Action(name="DownloadStatementByDate", kwargs={"account_id": "acc_chk_9001", "month": "2023-10"}),
            Action(name="UpdateAccountPreferences", kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "preferences": {"language": "fr-FR", "notifications": True}
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "Balances for checking account acc_chk_9001 and credit card acc_crd_9002 retrieved.",
            "Transaction history and October 2023 expenses for checking account reviewed and statement downloaded.",
            "Account preferences updated to French language and notifications enabled.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_025",
        instruction=(
            "Manage a support case for international customer Adetokunbo Adebayor (ID: f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3). "
            "Current date is 2025-07-24. "
            "Begin by retrieving his profile and verifying his identity with his national ID 'nh464131'. "
            "He has reported a change of contact information; update his email to 'kenji.tanaka.new@example.jp' and phone to '+81 90-8765-4321'. "
            "Next, list his beneficiaries. "
            "He wants to cancel his bi-weekly scheduled payment with ID 'sp_d9b3a2c1-d6e5-f4a3-b2c1-d0e9f8g7h6i5'. "
            "After canceling, arrange a new one-time payment of 75000 JPY from his account 'acc_chk_10001' to his beneficiary Yuki Tanaka's account '87654321' for '2025-08-15'. "
            "Lastly, submit a support ticket with ID 'ticket_user_025_payment_update' under category 'Scheduled Payment', priority 'Medium', via 'Email' with the request details: 'Customer updated contact info, canceled recurring payment sp_d9b3a2c1-d6e5-f4a3-b2c1-d0e9f8g7h6i5, and scheduled a new one-time payment.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "id_document": "nh464131"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "new_email": "kenji.tanaka.new@example.jp", "new_phone": "+81 90-8765-4321"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_d9b3a2c1-d6e5-f4a3-b2c1-d0e9f8g7h6i5"}),
            Action(name="SchedulePaymentWithValidation", kwargs={
                "from_account": "acc_chk_10001",
                "to_account": "87654321",
                "amount": 75000.0,
                "currency": "JPY",
                "date": "2025-08-15"
            }),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "ticket_id": "ticket_user_025_payment_update",
                "category": "Scheduled Payment",
                "priority": "Medium",
                "channel": "Email",
                "request_details": "Customer updated contact info, canceled recurring payment sp_d9b3a2c1-d6e5-f4a3-b2c1-d0e9f8g7h6i5, and scheduled a new one-time payment."
            }),
        ],
        outputs=[
            "Identity verified for Adetokunbo Adebayor and contact information updated.",
            "Bi-weekly payment 'sp_d9b3a2c1-d6e5-f4a3-b2c1-d0e9f8g7h6i5' was successfully canceled.",
            "New one-time payment of 75000 JPY scheduled for 2025-08-15.",
            "Support ticket logged to confirm all changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_026",
        instruction=(
            "A compliance officer is carrying out a detailed Q1 2023 financial audit for the international customer Oliver Williams (ID: c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6). "
            "Begin by retrieving her profile and confirming her identity using her national ID 'IJ758739'. "
            "Subsequently, manage her beneficiaries: list them and then remove her existing beneficiary 'Dubai International School' (ID: bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f). "
            "Following the removal, register a new beneficiary using the ID 'bene_user_026_art_gallery' for 'Global Art Gallery', with account IBAN 'FR7630006000011234567890189' at 'BNP Paribas' (BIC: 'BNPAFRPP') in 'France'. "
            "Then, for her checking account 'acc_chk_7001', compile monthly expenses and download the statements for January, February, and March of 2023. "
            "Conclude by conducting a suspicious activity check on the account and submitting a support ticket with ID 'ticket_user_026_q1_audit_log' under category 'Audit', priority 'High', via 'Internal System', with the request details: 'Q1 2023 compliance audit completed for customer. "
            "Beneficiary list updated and financial activity reviewed.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "id_document": "IJ758739"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "beneficiary_id": "bene_user_026_art_gallery",
                "beneficiary_name": "Global Art Gallery",
                "country": "France",
                "bank_details": {"account_number": "FR7630006000011234567890189", "bank_name": "BNP Paribas", "routing_info": "BNPAFRPP"}
            }),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_7001", "month": "2023-01"}),
            Action(name="DownloadStatementByDate", kwargs={"account_id": "acc_chk_7001", "month": "2023-01"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_7001", "month": "2023-02"}),
            Action(name="DownloadStatementByDate", kwargs={"account_id": "acc_chk_7001", "month": "2023-02"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_7001", "month": "2023-03"}),
            Action(name="DownloadStatementByDate", kwargs={"account_id": "acc_chk_7001", "month": "2023-03"}),
            Action(name="DetectSuspiciousActivityAndAlert", kwargs={"account_id": "acc_chk_7001"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "ticket_id": "ticket_user_026_q1_audit_log",
                "category": "Audit",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Q1 2023 compliance audit completed for customer. Beneficiary list updated and financial activity reviewed."
            }),
        ],
        outputs=[
            "Identity verified for Oliver Williams and beneficiary list updated.",
            "Q1 2023 expenses for account acc_chk_7001 aggregated for Jan, Feb, and Mar.",
            "Q1 2023 statements for account acc_chk_7001 downloaded for Jan, Feb, and Mar.",
            "Suspicious activity check completed and a high-priority audit ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_027",
        instruction=(
            "Coordinate a credit card dispute for Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef). "
            "Initially, access her profile and validate her identity using her national ID 'jd195515'. "
            "She is reporting an unauthorized transaction on her checking account 'acc_chk_2001'. "
            "Obtain the transaction history for the last two years to identify the charge. "
            "Conduct a suspicious activity check on the account. "
            "Then, lodge a support ticket with ID 'ticket_user_027_dispute' for a 'Dispute' with 'High' priority through the 'Mobile App'. "
            "The ticket must pertain to the 'Transaction' entity with ID 'txn_0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d', for the operation 'DISPUTE_CHARGE', and include the parameter note: 'Customer reports this charge of 45.50 CAD to The Bistro is fraudulent and unauthorized.' Immediately following the ticket submission, freeze the account 'acc_chk_2001' citing 'Fraudulent activity reported; dispute process initiated' as the reason. "
            "Finally, modify her account preferences to ensure all notifications are enabled."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_2001", "days": 730}),
            Action(name="DetectSuspiciousActivityAndAlert", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_027_dispute",
                "category": "Dispute",
                "priority": "High",
                "channel": "Mobile App",
                "request_details": {
                    "target_entity": "Transaction",
                    "target_id": "txn_0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
                    "operation": "DISPUTE_CHARGE",
                    "parameters": {"note": "Customer reports this charge of 45.50 CAD to The Bistro is fraudulent and unauthorized."}
                }
            }),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_chk_2001", "alert_reason": "Fraudulent activity reported; dispute process initiated."}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "preferences": {"notifications": True}}),
        ],
        outputs=[
            "Identity of Elena Popescu verified and transaction history reviewed.",
            "Suspicious activity check performed.",
            "High-priority dispute ticket 'ticket_user_027_dispute' submitted for transaction 'txn_0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d'.",
            "Account 'acc_chk_2001' frozen and notification preferences updated.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_028",
        instruction=(
            "Onboard and establish accounts for high-net-worth client Zoltan Nagy (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "Begin by accessing his profile and confirming his identity with his driver's license 'VI933872'. "
            "Initially, establish a new Savings account for him using currency 'USD', with an initial limit of 0.0. "
            "Then, present his current beneficiaries and register a new international beneficiary with ID 'bene_user_028_uk_art' for 'London Fine Arts Ltd', with account number 'GB29NWBK60161331926819' at 'NatWest' (routing: 'NWBKGB2L') in the 'United Kingdom'. "
            "Arrange a one-time payment of $5,000 USD from his checking account 'acc_chk_3001' to this new UK beneficiary for '2025-09-01'. "
            "Adjust his account preferences to activate paperless billing and designate 'SMS' as his communication channel. "
            "Finally, generate a support ticket with ID 'ticket_user_028_onboarding' under category 'Onboarding', priority 'High', via 'Internal System', with the request details: 'Onboarding for high-net-worth client Zoltan Nagy complete. "
            "New accounts and beneficiaries configured as requested.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "VI933872"}),
            Action(name="CreateCustomerAccount", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "account_type": "Savings", "currency": "USD", "initial_limit": 0.0}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_id": "bene_user_028_uk_art",
                "beneficiary_name": "London Fine Arts Ltd",
                "country": "United Kingdom",
                "bank_details": {"account_number": "GB29NWBK60161331926819", "bank_name": "NatWest", "routing_info": "NWBKGB2L"}
            }),
            Action(name="SchedulePaymentWithValidation", kwargs={"from_account": "acc_chk_3001", "to_account": "GB29NWBK60161331926819", "amount": 5000.00, "currency": "USD", "date": "2025-09-01"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "preferences": {"paperless_billing": True, "communication_channel": "SMS"}}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "ticket_user_028_onboarding",
                "category": "Onboarding",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Onboarding for high-net-worth client Zoltan Nagy complete. New accounts and beneficiaries configured as requested."
            }),
        ],
        outputs=[
            "Identity verified for Zoltan Nagy and a new savings account was created.",
            "New international beneficiary 'London Fine Arts Ltd' registered.",
            "Payment of $5,000 USD to new beneficiary scheduled for 2025-09-01.",
            "Preferences updated and high-priority onboarding ticket logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_029",
        instruction=(
            "Conduct simple account maintenance for customer Sofia Andersson (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5). "
            "Acquire her profile and verify her identity with her driver's license 'fo611864'. "
            "Inspect the balance of her checking account 'acc_chk_6001'. "
            "Amend her contact information to email 'oliver.w.main@example.co.uk' and phone '+44 7700 900555'. "
            "Then modify her account preferences to utilize 'Email' as her communication channel and enable paperless billing. "
            "Subsequently, list her current beneficiaries to verify her setup. "
            "Finally, download her account statement for October 2023 for her records."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "id_document": "fo611864"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_6001"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "new_email": "oliver.w.main@example.co.uk", "new_phone": "+44 7700 900555"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "preferences": {"communication_channel": "Email", "paperless_billing": True}}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}),
            Action(name="DownloadStatementByDate", kwargs={"account_id": "acc_chk_6001", "month": "2023-10"}),
        ],
        outputs=[
            "Identity verified for Sofia Andersson and account balance checked.",
            "Customer email and phone number have been updated.",
            "Account preferences set to Email and paperless billing.",
            "Beneficiary list checked and October 2023 statement downloaded.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_030",
        instruction=(
            "Oversee loan and payment details for customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "Current date is 2025-07-24. "
            "Begin by retrieving his profile and confirming his identity with his passport 'lF146011'. "
            "First, briefly summarize the status of his loan applications. "
            "Next, present his current beneficiaries. "
            "He wishes to halt his monthly scheduled payment to 'Anytown Utility Services', which has the ID 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d'. "
            "After canceling that payment, arrange a new one-time payment of $250.00 from her checking account 'acc_chk_1001' to her other beneficiary, Elena Popescu (account: '9876543210'), for the date '2025-08-20'. "
            "Procure the latest monthly statement for her savings account 'acc_sav_1002' for July 2025. "
            "Finally, create a support ticket with ID 'ticket_user_030_payment_changes' under category 'Account Management', priority 'Medium', via 'Web Portal', with the request details: 'Canceled scheduled payment sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d and scheduled new payment to Elena Popescu.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="SummarizeLoanApplicationsByStatus", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="SchedulePaymentWithValidation", kwargs={
                "from_account": "acc_chk_1001",
                "to_account": "9876543210",
                "amount": 250.00,
                "currency": "USD",
                "date": "2025-08-20"
            }),
            Action(name="DownloadStatementByDate", kwargs={"account_id": "acc_sav_1002", "month": "2025-07"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_030_payment_changes",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Canceled scheduled payment sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d and scheduled new payment to Elena Popescu."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka and loan status summarized.",
            "Scheduled payment 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d' to Anytown Utility Services canceled.",
            "New one-time payment of $250.00 to Elena Popescu scheduled for 2025-08-20.",
            "Savings account statement for July 2025 downloaded and support ticket logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_031",
        instruction=(
            "Handle a comprehensive account consolidation for customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "Start by retrieving his profile and confirming his identity using his passport 'lF146011'. "
            "He intends to terminate his credit card 'acc_crd_1003'. "
            "Verify the credit card's balance, which stands at -$2500.00. "
            "Additionally, inspect the balance of his checking account 'acc_chk_1001', which is $5230.50. "
            "Move $2500.00 from the checking account to the credit card account 'acc_crd_1003' to settle the debt. "
            "Once settled, submit a closure request for the credit card account. "
            "Proceed by transferring the full remaining balance of $2730.50 from the checking account 'acc_chk_1001' to the savings account 'acc_sav_1002'. "
            "Post-transfer, file a request to terminate the now-empty checking account 'acc_chk_1001'. "
            "Lastly, lodge a support ticket with ID 'ticket_user_031_consolidation' under the category 'Account Management', with high priority, via 'Web Portal', detailing the request: 'Customer has completed account consolidation. "
            "Closed credit card acc_crd_1003 and checking acc_chk_1001 after transferring all funds to savings acc_sav_1002.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_crd_1003", "amount": 2500.00}),
            Action(name="CloseAccountRequest", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_sav_1002", "amount": 2730.50}),
            Action(name="CloseAccountRequest", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_031_consolidation",
                "category": "Account Management",
                "priority": "High",
                "channel": "Web Portal",
                "request_details": "Customer has completed account consolidation. Closed credit card acc_crd_1003 and checking acc_chk_1001 after transferring all funds to savings acc_sav_1002."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka and balances for accounts acc_crd_1003 and acc_chk_1001 checked.",
            "Credit card acc_crd_1003 paid off and submitted for closure.",
            "Remaining funds from checking acc_chk_1001 transferred to savings acc_sav_1002.",
            "Checking account acc_chk_1001 submitted for closure and a high-priority ticket was logged to document the consolidation.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_032",
        instruction=(
            "Assist small business owner Zoltan Nagy (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11) in managing his supplier list from his account acc_chk_12001. "
            "Begin by accessing his profile and verifying his identity with passport 'Se620000'. "
            "He needs to establish two new suppliers. "
            "First, set up a new beneficiary with ID 'bene_user_032_farm_supplies' for 'Farm Supplies Co.' and account IBAN 'IE29AIBK93118212345678' at 'AIB' (routing: 'AIBKIE2D') in 'Ireland'. "
            "Then, create another beneficiary with ID 'bene_user_032_vet_services' for 'Veterinary Services Inc.' with account IBAN 'IE89BOFI90332112345678' at 'Bank of Ireland' (routing: 'BOFIIE2D') in 'Ireland'. "
            "Lastly, file a support ticket with ID 'ticket_user_032_supplier_setup' under 'Account Management', with medium priority, via 'Web Portal', specifying: 'Set up two new beneficiaries for supplier payments: Farm Supplies Co. "
            "and Veterinary Services Inc.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "id_document": "Se620000"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "beneficiary_id": "bene_user_032_farm_supplies",
                "beneficiary_name": "Farm Supplies Co.",
                "country": "Ireland",
                "bank_details": {"account_number": "IE29AIBK93118212345678", "bank_name": "AIB", "routing_info": "AIBKIE2D"}
            }),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "beneficiary_id": "bene_user_032_vet_services",
                "beneficiary_name": "Veterinary Services Inc.",
                "country": "Ireland",
                "bank_details": {"account_number": "IE89BOFI90332112345678", "bank_name": "Bank of Ireland", "routing_info": "BOFIIE2D"}
            }),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "ticket_id": "ticket_user_032_supplier_setup",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Set up two new beneficiaries for supplier payments: Farm Supplies Co. and Veterinary Services Inc."
            }),
        ],
        outputs=[
            "Identity of Zoltan Nagy verified.",
            "Two new beneficiaries, 'Farm Supplies Co.' and 'Veterinary Services Inc.', were successfully registered.",
            "A support ticket was logged to confirm the setup of the new supplier beneficiaries.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_033",
        instruction=(
            "Coordinate a security and relocation protocol for customer Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef). "
            "She reports an international relocation and intends to secure her account 'acc_chk_2001' during the process. "
            "Initially, retrieve her profile. "
            "Suspend her account citing the reason 'Customer request during international move for security'. "
            "Confirm her identity using national ID 'jd195515' to approve upcoming modifications. "
            "Revise her contact details to the new email 'jane.smith.uk@example.com' and updated UK phone number '+44 7700 900888'. "
            "Alter her preferences to 'en-GB' language and set the communication channel to 'Email'. "
            "Following the updates, reactivate her account using security code 'UKMOVE25'. "
            "Next, manage his beneficiaries: enumerate them and remove the existing beneficiary 'Kenji Tanaka' (ID: bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f). "
            "Establish a new UK-based beneficiary with ID 'bene_user_033_uk_landlord' for 'UK Property Masters' and account number 'GB29NWBK60161331926819' at 'NatWest' (routing: 'NWBKGB2L'). "
            "Finally, issue a ticket with ID 'ticket_user_033_relocation' under 'Account Management', with high priority, via 'Internal System', detailing: 'Customer relocation protocol complete. "
            "Account secured, contact info and beneficiaries updated. "
            "Address update must be handled by mail.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_chk_2001", "alert_reason": "Customer request during international move for security"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "new_email": "jane.smith.uk@example.com", "new_phone": "+44 7700 900888"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "preferences": {"language": "en-GB", "communication_channel": "Email"}}),
            Action(name="UnlockAccountBySecurityCheck", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "security_code": "UKMOVE25"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_user_033_uk_landlord",
                "beneficiary_name": "UK Property Masters",
                "country": "United Kingdom",
                "bank_details": {"account_number": "GB29NWBK60161331926819", "bank_name": "NatWest", "routing_info": "NWBKGB2L"}
            }),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_033_relocation",
                "category": "Account Management",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Customer relocation protocol complete. Account secured, contact info and beneficiaries updated. Address update must be handled by mail."
            }),
        ],
        outputs=[
            "Account for Elena Popescu frozen for security and identity verified.",
            "Contact info and preferences updated for UK residency.",
            "Account unlocked and beneficiary list updated to remove old contact and add new UK landlord.",
            "High-priority ticket logged to confirm all changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_034",
        instruction=(
            "Facilitate IT Consultant Zoltan Nagy (ID: a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4) with a loan inquiry and profile update. "
            "Begin by fetching his profile and confirm his identity using passport 'hI566779'. "
            "Then, provide a summary of his loan application history. "
            "He wishes to apply for a new, smaller loan; therefore, submit an application for $2,000 designated for 'Educational Supplies'. "
            "Check the balance on his checking account 'acc_chk_5002'. "
            "Subsequently, update his contact details to the new email 'l.narayanan.consulting@example.com' and new phone number '444-555-7777'. "
            "Lastly, document his current beneficiaries to ensure his setup is correct."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4", "id_document": "hI566779"}),
            Action(name="SummarizeLoanApplicationsByStatus", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}),
            Action(name="ApplyForLoanWithCheck", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4", "amount": 2000.0, "purpose": "Educational Supplies"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_5002"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4", "new_email": "l.narayanan.consulting@example.com", "new_phone": "444-555-7777"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}),
        ],
        outputs=[
            "Identity verified for Zoltan Nagy and his loan history was summarized.",
            "A new loan application for $2,000 for 'Educational Supplies' was submitted.",
            "His checking account balance was checked.",
            "His contact information was updated and his beneficiary list was confirmed.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_035",
        instruction=(
            "Assist student Adetokunbo Adebayor (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef-22) in managing his finances from his checking account 'acc_chk_23001'. "
            "The current date is 2025-07-24. "
            "Begin by accessing her profile and authenticate her identity using her driver's license 'Qb140023'. "
            "Obtain her transaction history for the past 30 days and compile her June 2025 monthly expenses to aid in budget creation. "
            "Download her statement for June 2025 for her records. "
            "She then needs to configure a recurring rent payment. "
            "Register a new beneficiary with ID 'bene_user_035_landlord' for 'Beijing Property Management' with account number '622848001002003004' at 'Agricultural Bank of China' (routing: 'ABOCCNBJ') in 'China'. "
            "Next, arrange a one-time payment of 2000 CNY to this new beneficiary set for '2025-08-01'. "
            "Conclude by filing a support ticket with ID 'ticket_user_035_budget' under 'Payments', with low priority, via 'Mobile App', specifying: 'Assisted student with budget review and set up first rent payment to new landlord beneficiary.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22", "id_document": "Qb140023"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_23001", "days": 30}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_23001", "month": "2025-06"}),
            Action(name="DownloadStatementByDate", kwargs={"account_id": "acc_chk_23001", "month": "2025-06"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                "beneficiary_id": "bene_user_035_landlord",
                "beneficiary_name": "Beijing Property Management",
                "country": "China",
                "bank_details": {"account_number": "622848001002003004", "bank_name": "Agricultural Bank of China", "routing_info": "ABOCCNBJ"}
            }),
            Action(name="SchedulePaymentWithValidation", kwargs={"from_account": "acc_chk_23001", "to_account": "622848001002003004", "amount": 2000.0, "currency": "CNY", "date": "2025-08-01"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                "ticket_id": "ticket_user_035_budget",
                "category": "Payments",
                "priority": "Low",
                "channel": "Mobile App",
                "request_details": "Assisted student with budget review and set up first rent payment to new landlord beneficiary."
            }),
        ],
        outputs=[
            "Identity verified for Adetokunbo Adebayor and her financial history for June 2025 was reviewed.",
            "June 2025 statement downloaded.",
            "New beneficiary 'Beijing Property Management' was registered.",
            "A rent payment of 2000 CNY was scheduled for 2025-08-01 and a support ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_036",
        instruction=(
            "Handle a complex joint account setup and security protocol involving two customers. "
            "The primary customer is Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef) and she wants to add Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) as a joint holder to her account 'acc_chk_2001'. "
            "Initially, retrieve Elena Popescu's profile and verify her identity using her national ID 'jd195515'. "
            "Then, fetch Kenji Tanaka's profile and confirm his identity with his passport 'lF146011'. "
            "Add Kenji Tanaka as a joint account holder to Elena Popescu's checking account 'acc_chk_2001'. "
            "Proceed by listing Elena Popescu's beneficiaries and remove 'Kenji Tanaka' (ID: bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f) from the list as she is now a joint holder. "
            "Register a new beneficiary with ID 'bene_user_036_family_trust' for 'Smith Family Trust', with account number '5555' at 'CAD Bank' (routing: 'N/A') in 'Canada'. "
            "Update Elena Popescu's account preferences to enable paperless billing. "
            "As a final security step, freeze the account 'acc_chk_2001' with the explanation 'Awaiting verbal confirmation of new joint holder setup from both parties.' Submit a ticket with ID 'ticket_user_036_joint_setup' under the category 'Account Management', priority 'High', via 'Internal System', with the request details: 'Joint holder Kenji Tanaka added to account acc_chk_2001. "
            "Beneficiary list updated. "
            "Account frozen pending verbal confirmation.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="AddJointAccountHolder", kwargs={"account_id": "acc_chk_2001", "holder_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_user_036_family_trust",
                "beneficiary_name": "Smith Family Trust",
                "country": "Canada",
                "bank_details": {"account_number": "5555", "bank_name": "CAD Bank", "routing_info": "N/A"}
            }),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "preferences": {"paperless_billing": True}}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_chk_2001", "alert_reason": "Awaiting verbal confirmation of new joint holder setup from both parties."}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_036_joint_setup",
                "category": "Account Management",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Joint holder Kenji Tanaka added to account acc_chk_2001. Beneficiary list updated. Account frozen pending verbal confirmation."
            }),
        ],
        outputs=[
            "Identities of Elena Popescu and Kenji Tanaka verified.",
            "Kenji Tanaka added as joint holder to account acc_chk_2001.",
            "Beneficiary list for Elena Popescu updated: 'Kenji Tanaka' removed, 'Smith Family Trust' added.",
            "Account preferences updated and account frozen with a high-priority ticket logged for follow-up.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_037",
        instruction=(
            "Coordinate an update for recurring payments and beneficiaries for customer, Oliver Williams (ID: c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6). "
            "Start by accessing her profile and verifying her identity using her national ID 'IJ758739'. "
            "She needs to cancel her quarterly scheduled payment of 10000 AED, which is identified by 'sp_a2c1d9b3-d2e1-f0a9-b8c7-d6e5f4a3b2c1'. "
            "Subsequently, display her beneficiaries and remove 'Dubai International School' (ID: bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f). "
            "Then, register a new beneficiary with ID 'bene_user_037_art_foundation' for 'Abu Dhabi Art Foundation', with IBAN 'AE420260001014567890555' at 'Emirates NBD' (BIC: 'EBILAEAD') in the 'United Arab Emirates'. "
            "Update her contact details to the new email 'fatima.art@example.ae' and phone number '+971 50 765 4321'. "
            "Lastly, initiate a support ticket with ID 'ticket_user_037_payment_update' under the category 'Payments', prioritized as 'Medium', via 'Email', with the request details: 'Canceled scheduled payment sp_a2c1d9b3-d2e1-f0a9-b8c7-d6e5f4a3b2c1 and updated beneficiary list as per customer request.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "id_document": "IJ758739"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_a2c1d9b3-d2e1-f0a9-b8c7-d6e5f4a3b2c1"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "beneficiary_id": "bene_user_037_art_foundation",
                "beneficiary_name": "Abu Dhabi Art Foundation",
                "country": "United Arab Emirates",
                "bank_details": {"account_number": "AE420260001014567890555", "bank_name": "Emirates NBD", "routing_info": "EBILAEAD"}
            }),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "new_email": "fatima.art@example.ae", "new_phone": "+971 50 765 4321"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "ticket_id": "ticket_user_037_payment_update",
                "category": "Payments",
                "priority": "Medium",
                "channel": "Email",
                "request_details": "Canceled scheduled payment sp_a2c1d9b3-d2e1-f0a9-b8c7-d6e5f4a3b2c1 and updated beneficiary list as per customer request."
            }),
        ],
        outputs=[
            "Identity verified for Oliver Williams.",
            "Scheduled payment 'sp_a2c1d9b3-d2e1-f0a9-b8c7-d6e5f4a3b2c1' has been canceled.",
            "Beneficiary list updated: 'Dubai International School' removed and 'Abu Dhabi Art Foundation' added.",
            "Customer contact information updated and a support ticket was logged to confirm all changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_038",
        instruction=(
            "Coordinate a comprehensive security audit and profile update for high-net-worth client Zoltan Nagy (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "Current date is 2023-11-15. "
            "Access his profile and verify his identity using his driver's license 'VI933872'. "
            "Retrieve the complete transaction history for his checking account 'acc_chk_3001' and investment account 'acc_inv_3002'. "
            "Compile his monthly expenses from the checking account for October 2023. "
            "Update his primary contact information to 'david.chen.primary@example.com' and phone '555-987-1111'. "
            "Adjust his account preferences to language 'en-US' and activate all notifications. "
            "Then, freeze his checking account 'acc_chk_3001' with the note 'Security audit in progress. "
            "Customer notified.' Finally, generate a ticket with ID 'ticket_user_038_sec_audit' under the category 'Security', marked as 'Critical', via 'Internal System', including the request details: 'Full security audit complete for Zoltan Nagy. "
            "Profile and accounts updated. "
            "Checking account temporarily frozen.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "VI933872"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_3001"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_inv_3002"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_3001", "month": "2023-10"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "new_email": "david.chen.primary@example.com", "new_phone": "555-987-1111"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "preferences": {"language": "en-US", "notifications": True}}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_chk_3001", "alert_reason": "Security audit in progress. Customer notified."}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "ticket_user_038_sec_audit",
                "category": "Security",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Full security audit complete for Zoltan Nagy. Profile and accounts updated. Checking account temporarily frozen."
            }),
        ],
        outputs=[
            "Identity verified for Zoltan Nagy and transaction histories for two accounts retrieved.",
            "October 2023 expenses aggregated and contact info updated.",
            "The customer's preferences were updated.",
            "Checking account frozen and a critical security audit ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_039",
        instruction=(
            "Manage a straightforward profile and multi-account balance check for customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "Start by accessing his profile and verifying his identity using his passport 'lF146011'. "
            "Next, obtain the balances for all three of his accounts: checking 'acc_chk_1001', savings 'acc_sav_1002', and credit card 'acc_crd_1003'. "
            "After validating the balances, modify his account preferences to enable paperless billing and set the primary communication channel to 'App'. "
            "Update his email address to 'john.doe.main@example.com' and his primary phone number to '123-456-8888'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "preferences": {"paperless_billing": True, "communication_channel": "App"}}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "new_email": "john.doe.main@example.com", "new_phone": "123-456-8888"}),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "Balances for checking, savings, and credit card accounts were successfully retrieved.",
            "Account preferences were updated to use the App and paperless billing.",
            "Customer's email and phone number were updated.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_040",
        instruction=(
            "Handle a delicate loan management case for customer Isabella Rossi (ID: d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25), who has a delinquent personal loan 'loan_pers_020'. "
            "First, retrieve his profile and verify his identity with his national ID 'fy088462'. "
            "To gauge his financial state, collect the transaction history for his checking account 'acc_chk_26001' for the past 90 days and calculate his expenses for October 2023. "
            "Ensure his contact details are up-to-date by changing his email to 'mo.almasri.updates@example.eg' and his phone to '+20 100 765 4321'. "
            "Lastly, draft a support ticket with ID 'ticket_user_040_payment_plan' under the 'Loan Support' category, marked with 'High' priority, using the 'Phone' channel. "
            "The request details should state: 'Customer is requesting to negotiate a new payment plan for delinquent loan loan_pers_020 due to recent financial hardship. "
            "Please have an agent contact him.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25", "id_document": "fy088462"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_26001", "days": 90}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_26001", "month": "2023-10"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25", "new_email": "mo.almasri.updates@example.eg", "new_phone": "+20 100 765 4321"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                "ticket_id": "ticket_user_040_payment_plan",
                "category": "Loan Support",
                "priority": "High",
                "channel": "Phone",
                "request_details": "Customer is requesting to negotiate a new payment plan for delinquent loan loan_pers_020 due to recent financial hardship. Please have an agent contact him."
            }),
        ],
        outputs=[
            "Identity verified for Isabella Rossi.",
            "Transaction history and recent expenses have been reviewed to assess financial hardship.",
            "Customer's contact information has been updated.",
            "A high-priority support ticket has been logged to initiate a payment plan negotiation for his delinquent loan.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_041",
        instruction=(
            "Handle an account recovery and security enhancement protocol for Kenji Tanaka (ID: e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2), who suspects his credentials are compromised. "
            "Firstly, obtain his profile and verify his identity using his driver's license 'im665671'. "
            "Immediately freeze both of his accounts for security: checking 'acc_chk_9001' and credit card 'acc_crd_9002', citing the reason 'Customer-reported potential unauthorized access.' Update his contact information to the new secure email 'chloe.dubois.sec@example.com' and new phone number '+33 6 87 65 43 21'. "
            "Finally, submit a support ticket with ID 'ticket_user_041_recovery' under category 'Security', priority 'Critical', via 'Internal System'. "
            "The request details should be: 'Account recovery protocol executed. "
            "Contact info updated. "
            "Please manually unlock checking account acc_chk_9001 with security code RECOVERY2025. "
            "Credit card to remain frozen.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "id_document": "im665671"}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_chk_9001", "alert_reason": "Customer-reported potential unauthorized access."}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_crd_9002", "alert_reason": "Customer-reported potential unauthorized access."}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "new_email": "chloe.dubois.sec@example.com", "new_phone": "+33 6 87 65 43 21"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "ticket_id": "ticket_user_041_recovery",
                "category": "Security",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Account recovery protocol executed. Contact info updated. Please manually unlock checking account acc_chk_9001 with security code RECOVERY2025. Credit card to remain frozen."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka and both of his accounts were frozen.",
            "Customer's contact information was updated to a new secure email and phone.",
            "A critical security ticket was logged to document the incident and request a manual account unlock.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_042",
        instruction=(
            "Facilitate customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) with managing his credit card and scheduled payments. "
            "Begin by obtaining his profile and confirm his identity using passport 'lF146011'. "
            "Retrieve the current balances for his checking account 'acc_chk_1001' and his credit card 'acc_crd_1003'. "
            "The credit card shows a balance of -$2500. "
            "Execute a payment of $1000.00 from his checking account to his credit card 'acc_crd_1003'. "
            "Subsequently, he wishes to cancel a monthly scheduled payment of $75.00; its ID is 'sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w2'. "
            "After addressing the payments, update his account preferences to enable paperless billing. "
            "Finally, file a support ticket with ID 'ticket_user_042_payments' under category 'Payments', priority 'Low', via 'Web Portal', with the request details: 'Customer made a $1000 payment to credit card acc_crd_1003 and canceled scheduled payment sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w2.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_crd_1003", "amount": 1000.00}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w2"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "preferences": {"paperless_billing": True}}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_042_payments",
                "category": "Payments",
                "priority": "Low",
                "channel": "Web Portal",
                "request_details": "Customer made a $1000 payment to credit card acc_crd_1003 and canceled scheduled payment sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w2."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka and account balances retrieved.",
            "A payment of $1000.00 was transferred from checking to the credit card.",
            "Scheduled payment 'sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w2' was canceled.",
            "Account preferences were updated and a support ticket was logged confirming the actions.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_043",
        instruction=(
            "Coordinate a detailed financial review for international customer Chloe Dubois (ID: d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). "
            "Acquire his profile and confirm his identity using his driver's license 'Kt516858'. "
            "Retrieve the transaction history for his checking account 'acc_chk_8001' for the past 90 days, then sum up his expenses for October 2023. "
            "Additionally, retrieve the current balance of his savings account 'acc_sav_8002'. "
            "Then, he needs to update the details for his landlord beneficiary, Klaus Schmidt (ID: bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a). "
            "Delete the existing beneficiary record. "
            "Following this, re-register the beneficiary with the same ID 'bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a' and name 'Klaus Schmidt', but with new bank details: account IBAN 'DE89370400440532013999' at 'Commerzbank' (BIC: 'COBADEFF') in 'Germany'. "
            "Update his secondary contact details to email 'hans.mueller.secondary@example.de' and phone '+49 171 1112223'. "
            "Finally, submit a ticket with ID 'ticket_user_043_review' under category 'Audit', priority 'Medium', via 'Web Portal', with the request details: 'Financial review complete. "
            "Beneficiary details for Klaus Schmidt updated as per new information provided.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "id_document": "Kt516858"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_8001", "days": 90}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_8001", "month": "2023-10"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_sav_8002"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a",
                "beneficiary_name": "Klaus Schmidt",
                "country": "Germany",
                "bank_details": {"account_number": "DE89370400440532013999", "bank_name": "Commerzbank", "routing_info": "COBADEFF"}
            }),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "new_email": "hans.mueller.secondary@example.de", "new_phone": "+49 171 1112223"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "ticket_id": "ticket_user_043_review",
                "category": "Audit",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Financial review complete. Beneficiary details for Klaus Schmidt updated as per new information provided."
            }),
        ],
        outputs=[
            "Identity verified for Chloe Dubois and financial review of his accounts performed.",
            "Beneficiary 'Klaus Schmidt' was deleted and re-registered with new bank details.",
            "Customer's secondary contact information was updated.",
            "An audit ticket was logged to document the review and all changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_044",
        instruction=(
            "Carry out a simple beneficiary management task for Zoltan Nagy (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "Initially, retrieve his profile and confirm his identity using his national ID 'pI260068'. "
            "List his current beneficiaries. "
            "He wants to remove his current utility provider, 'Metropolis Power & Light' (ID: bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a). "
            "After removing the previous one, register a new beneficiary with ID 'bene_user_044_gotham_cable' for 'Gotham Cable', with account number '123123123' at 'Bank of Gotham' (routing: '021000021') in the 'USA'. "
            "Check the balance of his checking account 'acc_chk_3001'. "
            "Finally, lodge a support ticket with ID 'ticket_user_044_bene_update' under category 'Account Management', priority 'Low', via 'Mobile App', with the request details: 'Beneficiary Metropolis Power & Light removed and Gotham Cable added.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "pI260068"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_id": "bene_user_044_gotham_cable",
                "beneficiary_name": "Gotham Cable",
                "country": "USA",
                "bank_details": {"account_number": "123123123", "bank_name": "Bank of Gotham", "routing_info": "021000021"}
            }),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_3001"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "ticket_user_044_bene_update",
                "category": "Account Management",
                "priority": "Low",
                "channel": "Mobile App",
                "request_details": "Beneficiary Metropolis Power & Light removed and Gotham Cable added."
            }),
        ],
        outputs=[
            "Identity verified for Zoltan Nagy and beneficiaries listed.",
            "Beneficiary 'Metropolis Power & Light' was successfully removed.",
            "New beneficiary 'Gotham Cable' was registered.",
            "Checking account balance was confirmed and a support ticket was logged for the changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_045",
        instruction=(
            "Oversee a request from Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef) to reconfigure her joint checking account 'acc_chk_2001' to a single-user account. "
            "Firstly, procure her profile and affirm her identity using her national ID 'jd195515'. "
            "Remove the joint account holder with ID 'cust_joint_005' from the account. "
            "After the removal, fetch the transaction history for the past 90 days to ensure there are no outstanding transactions related to the removed holder. "
            "Then, adjust the account preferences to reflect single ownership by setting the communication channel to 'App' and disabling paperless billing. "
            "Update Jane's personal contact information to the email 'jane.smith.primary@example.com' and phone '555-123-9999'. "
            "List her beneficiaries to confirm they remain accurate for her as the sole account holder. "
            "Finally, submit a ticket with ID 'ticket_user_045_joint_removal' under category 'Account Management', priority 'Medium', via 'Web Portal', with the request details: 'Joint account holder cust_joint_005 removed from acc_chk_2001. "
            "Account preferences and customer contact info updated for single ownership.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="RemoveJointAccountHolder", kwargs={"account_id": "acc_chk_2001", "holder_id": "cust_joint_005"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_2001", "days": 90}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "preferences": {"communication_channel": "App", "paperless_billing": False}}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "new_email": "jane.smith.primary@example.com", "new_phone": "555-123-9999"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_045_joint_removal",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Joint account holder cust_joint_005 removed from acc_chk_2001. Account preferences and customer contact info updated for single ownership."
            }),
        ],
        outputs=[
            "Identity verified for Elena Popescu and joint holder 'cust_joint_005' removed from account acc_chk_2001.",
            "Transaction history reviewed to confirm no outstanding joint transactions.",
            "Account preferences and customer contact information updated for single ownership.",
            "Beneficiary list confirmed and a support ticket was logged to document the changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_046",
        instruction=(
            "Handle a multi-customer operation. "
            "The main customer, Zoltan Nagy (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a), intends to transfer $1500 to Sofia Andersson (ID: f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9). "
            "Begin by retrieving the profile for the sender, Zoltan Nagy, and confirming his identity with his national ID 'pI260068'. "
            "After that, access the profile for the recipient, Sofia Andersson, and revise her contact details to include email 'maria.garcia.updates@example.com' and phone '555-444-3333'. "
            "Then, enumerate Zoltan Nagy's current beneficiaries on his profile. "
            "Add Sofia Andersson as a new beneficiary under ID 'bene_user_046_m_garcia', utilizing her checking account number '8888' at 'State University Bank' (routing: '011000015') in the 'USA'. "
            "Following her registration, move $1500.00 from David's checking account 'acc_chk_3001' to Maria's account '8888'. "
            "Verify the updated balance of David's account 'acc_chk_3001' after the transaction. "
            "Conclude by filing a support ticket from David's profile with ID 'ticket_user_046_transfer' in 'Transfers' category, with 'Medium' priority, through 'Web Portal', detailing: 'Registered new beneficiary Sofia Andersson and completed a one-time transfer of $1500.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "pI260068"}),
            Action(name="GetCustomerProfile", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9", "new_email": "maria.garcia.updates@example.com", "new_phone": "555-444-3333"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_id": "bene_user_046_m_garcia",
                "beneficiary_name": "Sofia Andersson",
                "country": "USA",
                "bank_details": {"account_number": "8888", "bank_name": "State University Bank", "routing_info": "011000015"}
            }),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_3001", "to_account": "8888", "amount": 1500.00}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_3001"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "ticket_user_046_transfer",
                "category": "Transfers",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Registered new beneficiary Sofia Andersson and completed a one-time transfer of $1500."
            }),
        ],
        outputs=[
            "Identity of sender Zoltan Nagy verified and profile of recipient Sofia Andersson updated.",
            "Sofia Andersson registered as a new beneficiary on Zoltan Nagy's profile.",
            "A transfer of $1500.00 was completed from David's account to Maria's.",
            "The sender's account balance was checked post-transfer and a support ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_047",
        instruction=(
            "Coordinate an inquiry for a customer, Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), who is exploring the option to prepay his auto loan. "
            "The date is 2023-11-20. "
            "Initially, obtain his profile and validate his identity with passport 'lF146011'. "
            "Consult the current balance of his checking account 'acc_chk_1001' to evaluate available funds. "
            "Next, compile his loan application history to examine active loans. "
            "To gain insight into his spending patterns, gather all transactions from his checking account over the last 180 days. "
            "Summarize his expenditures for October 2023 to gauge recent financial activity. "
            "Finally, generate a support ticket with ID 'ticket_user_047_loan_inquiry' in the 'Loan Support' category, marked 'Medium' priority, via 'Email', detailing: 'Inquiry regarding early payoff amount and procedure for auto loan loan_auto_002.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="SummarizeLoanApplicationsByStatus", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_1001", "days": 180}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_1001", "month": "2023-10"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_047_loan_inquiry",
                "category": "Loan Support",
                "priority": "Medium",
                "channel": "Email",
                "request_details": "Inquiry regarding early payoff amount and procedure for auto loan loan_auto_002."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka and his checking account balance was retrieved.",
            "Loan history was summarized and transaction history reviewed for past payments.",
            "October 2023 expenses were aggregated to analyze recent budget.",
            "A support ticket was submitted to inquire about the early loan payoff procedure.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_048",
        instruction=(
            "Coordinate a comprehensive security audit and profile revision for the international client Oliver Williams (ID: c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6). "
            "The current date is 2023-11-20. "
            "Start by accessing her profile and confirming her identity using her national ID 'IJ758739'. "
            "Retrieve the entire transaction history for her checking account 'acc_chk_7001' and ascertain the current balance of her savings account 'acc_sav_7002'. "
            "Summarize her expenditures from the checking account in October 2023. "
            "Update her contact information to email 'fatima.alfassi.secure@example.ae' and phone '+971 50 111 2222'. "
            "Adjust her account preferences to language 'ar-AE' and activate all notifications. "
            "Temporarily place a hold on her checking account 'acc_chk_7001' due to 'Comprehensive security audit in progress.' Lastly, log a ticket with ID 'ticket_user_048_audit' under the 'Security' category, with 'Critical' priority, through 'Internal System', including the request details: 'Full security audit for Oliver Williams complete. "
            "Profile and preferences updated. "
            "Checking account is temporarily frozen.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "id_document": "IJ758739"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_7001"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_sav_7002"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_7001", "month": "2023-10"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "new_email": "fatima.alfassi.secure@example.ae", "new_phone": "+971 50 111 2222"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "preferences": {"language": "ar-AE", "notifications": True}}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_chk_7001", "alert_reason": "Comprehensive security audit in progress."}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "ticket_id": "ticket_user_048_audit",
                "category": "Security",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Full security audit for Oliver Williams complete. Profile and preferences updated. Checking account is temporarily frozen."
            }),
        ],
        outputs=[
            "Identity verified for Oliver Williams and account activities reviewed.",
            "Customer contact info and preferences were updated.",
            "The checking account was frozen for a security audit.",
            "A critical security ticket was logged to document the process.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_049",
        instruction=(
            "Coordinate a straightforward information retrieval and update task for customer Chloe Dubois (ID: d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). "
            "Initially, obtain his profile and verify his identity with his driver's license 'Kt516858'. "
            "Then, check the current balances for both his accounts: checking 'acc_chk_8001' and savings 'acc_sav_8002'. "
            "Update his contact details to the new email 'hans.m.primary@example.de' and new phone '+49 171 9998887'. "
            "Following that, list his beneficiaries to verify his current arrangements. "
            "Conclude by submitting a low-priority support ticket with ID 'ticket_user_049_contact_update' in 'Account Management' via 'Email', including the request details: 'Customer contact information has been updated as requested.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "id_document": "Kt516858"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_sav_8002"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "new_email": "hans.m.primary@example.de", "new_phone": "+49 171 9998887"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "ticket_id": "ticket_user_049_contact_update",
                "category": "Account Management",
                "priority": "Low",
                "channel": "Email",
                "request_details": "Customer contact information has been updated as requested."
            }),
        ],
        outputs=[
            "Identity verified for Chloe Dubois.",
            "Balances for checking and savings accounts were successfully retrieved.",
            "Customer's email and phone number were updated.",
            "Beneficiary list was confirmed and a low-priority ticket was logged to document the update.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_050",
        instruction=(
            "Assist customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) with the closure of his savings account 'acc_sav_1002' and consolidation of funds. "
            "Begin by accessing his profile and confirming his identity with his passport 'lF146011'. "
            "Before proceeding with the account closure, address an annual payment of $1000.00 due from it. "
            "Terminate the scheduled payment identified by 'sp_d9b3a2c1-f0a9-b8c7-d6e5-f4a3b2c1d0e9'. "
            "After terminating the payment, retrieve the full balance of the savings account 'acc_sav_1002'. "
            "The balance stands at $15780.00. "
            "To observe the daily transfer limit, move the complete balance of $15780.00 from the savings account to his checking account 'acc_chk_1001' using two distinct transactions: one for $10000.00 and another for $5780.00. "
            "Once the savings account is devoid of funds, request its closure. "
            "Finally, register a support ticket with ID 'ticket_user_050_closure' in the 'Account Closure' category, with 'Medium' priority, via 'Web Portal', detailing: 'Canceled scheduled payment from savings, transferred full balance to checking, and submitted savings account acc_sav_1002 for closure.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_d9b3a2c1-f0a9-b8c7-d6e5-f4a3b2c1d0e9"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_sav_1002", "to_account": "acc_chk_1001", "amount": 10000.00}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_sav_1002", "to_account": "acc_chk_1001", "amount": 5780.00}),
            Action(name="CloseAccountRequest", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_050_closure",
                "category": "Account Closure",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Canceled scheduled payment from savings, transferred full balance to checking, and submitted savings account acc_sav_1002 for closure."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "Scheduled payment 'sp_d9b3a2c1-f0a9-b8c7-d6e5-f4a3b2c1d0e9' was successfully canceled.",
            "The full balance from savings account acc_sav_1002 was transferred to checking in two transactions.",
            "Savings account submitted for closure and a support ticket was logged to document the process.",
        ],
    ),
     Task(
        annotator="0",
        user_id="user_051",
        instruction=(
            "Handle a comprehensive financial audit for the joint account 'acc_chk_2001'. "
            "The primary holder is Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef) and the joint holder is Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "Initially, access the profile for Elena Popescu and confirm her identity using her national ID 'jd195515'. "
            "Subsequently, obtain the profile for Kenji Tanaka and verify his identity with his passport 'lF146011'. "
            "Conduct a Q1 2023 audit on the joint account 'acc_chk_2001' by acquiring the full transaction history and summarizing the monthly expenditures for January, February, and March of 2023. "
            "Following the audit, amend the primary holder's (Elena Popescu) contact information to the new email 'jane.smith.joint@example.com' and phone '555-123-7788'. "
            "Conclusively, log a support ticket with ID 'ticket_user_051_joint_audit' under category 'Audit', priority 'Medium', via 'Internal System', detailing the request: 'Q1 2023 audit completed for joint account acc_chk_2001. "
            "Both holders verified. "
            "Primary holder contact information updated.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_2001", "start_date": "2023-01-01", "end_date": "2023-03-31"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_2001", "month": "2023-01"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_2001", "month": "2023-02"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_2001", "month": "2023-03"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "new_email": "jane.smith.joint@example.com", "new_phone": "555-123-7788"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_051_joint_audit",
                "category": "Audit",
                "priority": "Medium",
                "channel": "Internal System",
                "request_details": "Q1 2023 audit completed for joint account acc_chk_2001. Both holders verified. Primary holder contact information updated."
            }),
        ],
        outputs=[
            "Profiles retrieved and identities verified for both joint account holders Elena Popescu and Kenji Tanaka.",
            "Q1 2023 financial audit completed, including transaction history review and expense aggregation for three months.",
            "Primary holder's contact information was updated.",
            "A medium-priority audit ticket was logged to document the review and updates.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_052",
        instruction=(
            "Facilitate assistance for customer Kenji Tanaka (ID: e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2) with modifications to his account 'acc_chk_9001' following his recent marriage. "
            "Initially, gather his profile and confirm his identity with his driver's license 'im665671'. "
            "He intends to remove his mother, Marie Dubois (ID: bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c), as a beneficiary. "
            "Display his beneficiaries and expunge the specified record. "
            "Next, enlist his new spouse, Zoltan Nagy (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a), as a new beneficiary with ID 'bene_user_052_d_chen', utilizing his checking account number '6666' at 'City General Bank' (routing: 'N/A') in the 'USA'. "
            "Modify his account preferences to designate 'App' as the communication channel. "
            "Finally, file a support ticket with ID 'ticket_user_052_marital_update' under category 'Account Management', priority 'Medium', via 'Web Portal', stating the request details: 'Marital status update: Removed previous beneficiary and added spouse as new beneficiary.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "id_document": "im665671"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "beneficiary_id": "bene_user_052_d_chen",
                "beneficiary_name": "Zoltan Nagy",
                "country": "USA",
                "bank_details": {"account_number": "6666", "bank_name": "City General Bank", "routing_info": "N/A"}
            }),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "preferences": {"communication_channel": "App"}}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "ticket_id": "ticket_user_052_marital_update",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Marital status update: Removed previous beneficiary and added spouse as new beneficiary."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "Beneficiary Marie Dubois was successfully removed from the account.",
            "Spouse Zoltan Nagy was added as a new beneficiary.",
            "Account preferences were updated and a ticket was logged to confirm the changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_053",
        instruction=(
            "Handle a lost card security procedure for customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "He has reported his credit card as lost. "
            "Firstly, acquire his profile and confirm his identity using his passport 'lF146011'. "
            "Immediately deactivate his credit card account 'acc_crd_1003' citing the reason 'Customer reported lost card'. "
            "Obtain the transaction history for the credit card covering the last 7 days to detect any fraudulent activities. "
            "Summarize the expenses on the card for the current month (July 2025) to identify any irregular spending behavior. "
            "As a security measure, revise the customer's primary contact details to the email 'john.doe.secure@example.com' and phone '123-456-7777'. "
            "Finally, record a support ticket with ID 'ticket_user_053_lost_card' in the 'Card Services' category with 'Critical' priority via the 'Phone' channel. "
            "The request details should be: 'Customer lost credit card acc_crd_1003. "
            "Account is frozen. "
            "Please issue a new card to the address on file and cancel the old one. "
            "Customer will review transactions for fraud.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_crd_1003", "alert_reason": "Customer reported lost card."}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_crd_1003", "days": 7}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_crd_1003", "month": "2025-07"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "new_email": "john.doe.secure@example.com", "new_phone": "123-456-7777"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_053_lost_card",
                "category": "Card Services",
                "priority": "Critical",
                "channel": "Phone",
                "request_details": "Customer lost credit card acc_crd_1003. Account is frozen. Please issue a new card to the address on file and cancel the old one. Customer will review transactions for fraud."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka and his credit card account acc_crd_1003 was frozen.",
            "Recent transaction history and monthly expenses were reviewed for fraudulent activity.",
            "Customer's primary contact information was updated as a security measure.",
            "A critical priority ticket was submitted to issue a new credit card.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_054",
        instruction=(
            "Coordinate a straightforward information retrieval task for customer Mohammed Al-Masri (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17) concerning his financial planning. "
            "Begin by obtaining his profile and confirming his identity with his driver's license 'mQ002650'. "
            "Access the current balance of his checking account 'acc_chk_18001'. "
            "Next, enumerate his current beneficiaries to verify their status. "
            "Adjust his account preferences to enable all notifications. "
            "Finally, initiate a support ticket with ID 'ticket_user_054_fi_plan' under category 'General Inquiry', priority 'Low', via 'Web Portal', with the request details: 'Customer requests information on available financial planning and budgeting tools.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "id_document": "mQ002650"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_18001"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "preferences": {"notifications": True}}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                "ticket_id": "ticket_user_054_fi_plan",
                "category": "General Inquiry",
                "priority": "Low",
                "channel": "Web Portal",
                "request_details": "Customer requests information on available financial planning and budgeting tools."
            }),
        ],
        outputs=[
            "Identity verified for Mohammed Al-Masri.",
            "The customer's checking account balance was retrieved.",
            "Beneficiary list was checked and notification preferences were updated.",
            "A low-priority ticket was logged with a general inquiry about financial planning tools.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_055",
        instruction=(
            "Assist customer Zoltan Nagy (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) in transferring a segment of his investment funds. "
            "Initially, procure his profile and verify his identity using his national ID 'pI260068'. "
            "Check the current balance of his investment account 'acc_inv_3002' and his checking account 'acc_chk_3001'. "
            "He wants to relocate funds for a down payment, so transfer $9,500.00 from his investment account to his checking account. "
            "After the transfer, modify his investment account preferences to set the communication channel to 'Email'. "
            "Then, list his beneficiaries to confirm that no adjustments are needed for his estate plan. "
            "Conclusively, lodge a support ticket with ID 'ticket_user_055_inv_transfer' under category 'Transfers', priority 'Medium', via 'Web Portal', explaining the request details: 'Completed partial transfer of $9,500.00 from investment account acc_inv_3002 to checking acc_chk_3001 as requested.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "pI260068"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_inv_3002"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_3001"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_inv_3002", "to_account": "acc_chk_3001", "amount": 9500.00}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "preferences": {"communication_channel": "Email"}}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "ticket_user_055_inv_transfer",
                "category": "Transfers",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Completed partial transfer of $9,500.00 from investment account acc_inv_3002 to checking acc_chk_3001 as requested."
            }),
        ],
        outputs=[
            "Identity verified for Zoltan Nagy and balances for his investment and checking accounts were retrieved.",
            "A transfer of $9,500.00 from his investment to his checking account was completed.",
            "Preferences for the investment account were updated.",
            "Beneficiary list was confirmed and a ticket was logged to document the transfer.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_056",
        instruction=(
            "Handle a detailed separation of the joint account 'acc_chk_2001'. "
            "The primary holder is Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef), and the joint holder to be removed is Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), listed as holder ID 'cust_joint_005'. "
            "First, obtain the profiles for both Elena Popescu and Kenji Tanaka, and verify their identities using their respective documents: national ID 'jd195515' for Jane and passport 'lF146011' for John. "
            "Once verified, access the current balance of the joint account 'acc_chk_2001', which is 3100.75 CAD. "
            "Transfer 50% of the balance, exactly 1550.38 CAD, from the joint account 'acc_chk_2001' to Kenji Tanaka's personal checking account, which has the account number '1111'. "
            "After distributing the funds, remove Kenji Tanaka ('cust_joint_005') as a joint account holder from 'acc_chk_2001'. "
            "Update the primary account holder's (Elena Popescu) preferences to set the communication channel to 'App' to indicate single ownership. "
            "Finally, initiate a ticket with ID 'ticket_user_056_joint_split' under category 'Account Management', priority 'High', via 'Internal System', with the request details: 'Joint account acc_chk_2001 separation complete. "
            "Funds split and holder Kenji Tanaka (cust_joint_005) removed.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_2001", "to_account": "1111", "amount": 1550.38}),
            Action(name="RemoveJointAccountHolder", kwargs={"account_id": "acc_chk_2001", "holder_id": "cust_joint_005"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "preferences": {"communication_channel": "App"}}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_056_joint_split",
                "category": "Account Management",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Joint account acc_chk_2001 separation complete. Funds split and holder Kenji Tanaka (cust_joint_005) removed."
            }),
        ],
        outputs=[
            "Identities of both account holders, Elena Popescu and Kenji Tanaka, were verified.",
            "The balance of the joint account was checked.",
            "50% of the funds were transferred to Kenji Tanaka's personal account.",
            "Kenji Tanaka was removed as joint holder, preferences were updated, and a high-priority ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_057",
        instruction=(
            "Coordinate with customer Adetokunbo Adebayor (ID: f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3) to prepare his finances before a long trip. "
            "First, access his profile and verify his identity using his national ID 'nh464131'. "
            "He wants to suspend a large monthly payment temporarily; cancel the scheduled payment with ID 'sp_c1d9b3a2-a5b4-c3d2-e1f0-a9b8c7d6e5f4'. "
            "Next, list his beneficiaries and register a new temporary beneficiary with ID 'bene_user_057_travel_assist' for 'Global Travel Assist', with account number 'JP89370400440532013999' at 'Global Bank' (routing: 'GLBLJPJ1') in 'Japan'. "
            "Modify his account preferences to disable paperless billing and set the communication channel to 'SMS' to receive important alerts while traveling. "
            "As a precaution, freeze his savings account 'acc_sav_10002' while he is away, using the exact reason: 'Customer request for security during travel.'. "
            "Finally, create a support ticket with ID 'ticket_user_057_travel_prep' under category 'Account Management', priority 'Medium', via 'Email', with the request details: 'Travel Preparation: Canceled one scheduled payment, added temporary beneficiary, updated preferences to SMS, and froze savings account.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "id_document": "nh464131"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_c1d9b3a2-a5b4-c3d2-e1f0-a9b8c7d6e5f4"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "beneficiary_id": "bene_user_057_travel_assist",
                "beneficiary_name": "Global Travel Assist",
                "country": "Japan",
                "bank_details": {"account_number": "JP89370400440532013999", "bank_name": "Global Bank", "routing_info": "GLBLJPJ1"}
            }),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "preferences": {"paperless_billing": False, "communication_channel": "SMS"}}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_sav_10002", "alert_reason": "Customer request for security during travel."}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "ticket_id": "ticket_user_057_travel_prep",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Email",
                "request_details": "Travel Preparation: Canceled one scheduled payment, added temporary beneficiary, updated preferences to SMS, and froze savings account."
            }),
        ],
        outputs=[
            "Identity verified for Adetokunbo Adebayor.",
            "Scheduled payment 'sp_c1d9b3a2-a5b4-c3d2-e1f0-a9b8c7d6e5f4' was successfully canceled.",
            "A new temporary beneficiary was added and account preferences were updated for travel.",
            "The savings account was frozen as a security measure and a ticket was logged to document all changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_058",
        instruction=(
            "Conduct a thorough annual financial audit for the business account of customer Oliver Williams (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23). "
            "Current date is 2024-01-15. "
            "Access his profile and verify his identity using his national ID 'uY143801'. "
            "Retrieve the complete transaction history for his business checking account 'acc_chk_24001' for the past 365 days. "
            "Then, execute a Q1 2023 review by aggregating the monthly expenses for January, February, and March of 2023. "
            "Check the current balance of his business savings account 'acc_sav_24002'. "
            "Update his business contact information to the email 'ade.adebayor.biz@example.ng' and phone '+234 801 999 8888'. "
            "Next, register a new key supplier as a beneficiary with ID 'bene_user_058_lagos_port' for 'Lagos Port Services', with account number '0123456789' at 'GTBank' (routing: 'N/A') in 'Nigeria'. "
            "Finally, file a ticket with ID 'ticket_user_058_annual_audit' under category 'Audit', priority 'High', via 'Internal System', with the request details: 'Annual audit for business account acc_chk_24001 complete. "
            "Full history and Q1 expenses reviewed. "
            "Contact info and beneficiary list updated.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "id_document": "uY143801"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_24001", "days": 365}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_24001", "month": "2023-01"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_24001", "month": "2023-02"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_24001", "month": "2023-03"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_sav_24002"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "new_email": "ade.adebayor.biz@example.ng", "new_phone": "+234 801 999 8888"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                "beneficiary_id": "bene_user_058_lagos_port",
                "beneficiary_name": "Lagos Port Services",
                "country": "Nigeria",
                "bank_details": {"account_number": "0123456789", "bank_name": "GTBank", "routing_info": "N/A"}
            }),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                "ticket_id": "ticket_user_058_annual_audit",
                "category": "Audit",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Annual audit for business account acc_chk_24001 complete. Full history and Q1 expenses reviewed. Contact info and beneficiary list updated."
            }),
        ],
        outputs=[
            "Identity verified for Oliver Williams and full year transaction history retrieved.",
            "Q1 2023 expenses aggregated and savings account balance checked.",
            "Business contact information was updated.",
            "A new supplier beneficiary was registered and a high-priority audit ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_059",
        instruction=(
            "Handle a straightforward information and update task for the retired customer Lakshmi Narayanan (ID: c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24). "
            "First, retrieve her profile and verify her identity using her passport 'eE125799'. "
            "Access the current balance of her savings account 'acc_sav_25001'. "
            "Update her contact information to the new email 'elena.p.retired@example.ro' and a new phone number '+40 21 987 65 43'. "
            "Next, adjust her account preferences to set her communication channel to 'Mail', as requested. "
            "List her beneficiaries to confirm she has none set up. "
            "Finally, submit a low-priority support ticket with ID 'ticket_user_059_profile_update' under category 'Account Management' via 'Internal System' with the request details: 'Customer contact info and preferences updated as per request.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "id_document": "eE125799"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_sav_25001"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "new_email": "elena.p.retired@example.ro", "new_phone": "+40 21 987 65 43"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "preferences": {"communication_channel": "Mail"}}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                "ticket_id": "ticket_user_059_profile_update",
                "category": "Account Management",
                "priority": "Low",
                "channel": "Internal System",
                "request_details": "Customer contact info and preferences updated as per request."
            }),
        ],
        outputs=[
            "Identity verified for Lakshmi Narayanan and savings account balance retrieved.",
            "Customer's email and phone number were updated.",
            "Account preferences were set to 'Mail' communication.",
            "Beneficiary list was confirmed to be empty and a low-priority ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_060",
        instruction=(
            "Address a transaction dispute for customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "He is disputing a charge on his credit card 'acc_crd_1003'. "
            "First, access his profile and verify his identity using his passport 'lF146011'. "
            "Retrieve the transaction history for the credit card over the past two years. "
            "The customer identifies the fraudulent transaction as 'txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c', a charge of $250.00 from Amazon. "
            "Aggregate the expenses for the credit card for October 2023 to provide context. "
            "Next, file a detailed dispute ticket with ID 'ticket_user_060_dispute' to the 'Dispute' category with 'High' priority via 'Web Portal'. "
            "The request must target 'Transaction' entity 'txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c' for operation 'CHARGEBACK', with the note: 'Customer states they did not authorize this $250.00 purchase from Amazon.' As a precaution, freeze the credit card account 'acc_crd_1003' with the reason 'Dispute filed for fraudulent charge. "
            "Awaiting investigation.' Finally, update the customer's contact information to the email 'john.doe.dispute@example.com' and confirm his existing phone number '123-456-7890' to ensure he receives all communication regarding this case."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_crd_1003", "days": 730}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_crd_1003", "month": "2023-10"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_060_dispute",
                "category": "Dispute",
                "priority": "High",
                "channel": "Web Portal",
                "request_details": {
                    "target_entity": "Transaction",
                    "target_id": "txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c",
                    "operation": "CHARGEBACK",
                    "parameters": {"note": "Customer states they did not authorize this $250.00 purchase from Amazon."}
                }
            }),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_crd_1003", "alert_reason": "Dispute filed for fraudulent charge. Awaiting investigation."}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "new_email": "john.doe.dispute@example.com", "new_phone": "123-456-7890"}),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka and credit card history reviewed.",
            "A high-priority dispute ticket was submitted for transaction 'txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c'.",
            "The credit card account 'acc_crd_1003' was frozen as a security precaution.",
            "The customer's contact information was updated to ensure communication on the dispute case.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_061",
        instruction=(
            "Handle a comprehensive account consolidation and closure for customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "Begin by obtaining his profile and confirming his identity using his passport 'lF146011'. "
            "He desires to terminate his credit card and checking accounts, consolidating all funds into his savings account 'acc_sav_1002'. "
            "Retrieve the balances of his credit card 'acc_crd_1003' (-$2500) and checking account 'acc_chk_1001' ($5230.50). "
            "Initially, transfer $2500.00 from the checking account to settle the credit card debt. "
            "Once the obligation is cleared, move the remaining balance of $2730.50 from the checking to the savings account 'acc_sav_1002'. "
            "Cancel the pending payment with ID 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d'. "
            "After both accounts reflect zero balances, initiate requests to close the credit card 'acc_crd_1003' and the checking account 'acc_chk_1001'. "
            "To conclude, submit a ticket with ID 'ticket_user_061_closure' under category 'Account Closure', marking it as 'Critical', via 'Internal System', detailing the request: 'Full relationship closure process initiated. "
            "Credit and checking accounts terminated. "
            "Customer requests an agent call to finalize the savings account closure and disburse residual funds.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_crd_1003", "amount": 2500.00}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_sav_1002", "amount": 2730.50}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="CloseAccountRequest", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="CloseAccountRequest", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_061_closure",
                "category": "Account Closure",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Full relationship closure process started. Credit and checking accounts closed. Customer requests an agent call to close the final savings account and disburse remaining funds."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka and account balances checked.",
            "Credit card debt of $2500 was paid off using funds from the checking account.",
            "The remaining balance from the checking account was consolidated into savings.",
            "The credit card and checking accounts were submitted for closure and a critical ticket was logged for final steps.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_062",
        instruction=(
            "Coordinate the procedure for a deceased customer, Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "Start by retrieving his profile. "
            "A death certificate is available; use document number 'DE-CERT-123456' to verify the customer's status. "
            "Instantly freeze all accounts to secure the estate: checking 'acc_chk_1001', savings 'acc_sav_1002', and credit card 'acc_crd_1003'. "
            "Note the reason for all freezes as 'Account holder deceased. "
            "Pending estate settlement.' Subsequently, cancel all active scheduled payments linked to his accounts. "
            "This includes the payment with ID 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d' and the payment with ID 'sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e'. "
            "In conclusion, file a support ticket with ID 'ticket_user_062_deceased' to the 'Estate Management' category with 'Critical' priority via 'Internal System', including the request details: 'Executed deceased customer protocol for Kenji Tanaka. "
            "All accounts frozen and scheduled payments canceled. "
            "Awaiting contact from executor.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "DE-CERT-123456"}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_chk_1001", "alert_reason": "Account holder deceased. Pending estate settlement."}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_sav_1002", "alert_reason": "Account holder deceased. Pending estate settlement."}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_crd_1003", "alert_reason": "Account holder deceased. Pending estate settlement."}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_062_deceased",
                "category": "Estate Management",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Deceased customer protocol executed for Kenji Tanaka. All accounts frozen and scheduled payments canceled. Awaiting contact from executor."
            }),
        ],
        outputs=[
            "Customer status verified as deceased.",
            "All three of the customer's accounts (checking, savings, credit card) have been frozen.",
            "All active scheduled payments have been successfully canceled.",
            "A critical priority ticket has been submitted to the Estate Management department.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_063",
        instruction=(
            "Coordinate a detailed audit of beneficiaries for customer Zoltan Nagy (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) concerning his checking account 'acc_chk_3001'. "
            "Start by retrieving his profile and confirming his identity using his driver's license 'VI933872'. "
            "Next, produce a list of beneficiaries for Zoltan Nagy. "
            "He has one, 'Metropolis Power & Light' (ID: bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a), which needs to be removed. "
            "Post-removal, register two new beneficiaries. "
            "The first, identified by ID 'bene_user_063_ny_invest', is 'New York Investments', connected to account number '987654321' at 'Bank of NY' (routing: '021000018') in the 'USA'. "
            "The second has ID 'bene_user_063_chen_trust' for 'Chen Family Trust', with account number '112233445' at 'Chase Bank' (routing: '021000021') in the 'USA'. "
            "To finish, lodge a ticket with ID 'ticket_user_063_restructure' under 'Account Management', priority 'High', via 'Internal System', including the request details: 'Beneficiary audit completed: Metropolis Power & Light replaced with Providence Investments and Chen Family Trust.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "VI933872"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_id": "bene_user_063_ny_invest",
                "beneficiary_name": "New York Investments",
                "country": "USA",
                "bank_details": {"account_number": "987654321", "bank_name": "Bank of NY", "routing_info": "021000018"}
            }),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_id": "bene_user_063_chen_trust",
                "beneficiary_name": "Chen Family Trust",
                "country": "USA",
                "bank_details": {"account_number": "112233445", "bank_name": "Chase Bank", "routing_info": "021000021"}
            }),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "ticket_user_063_restructure",
                "category": "Account Management",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Beneficiary audit complete: beneficiary Metropolis Power & Light replaced with Providence Investments and Chen Family Trust."
            }),
        ],
        outputs=[
            "Identity of primary holder Zoltan Nagy verified.",
            "Beneficiary list was updated: 'Metropolis Power & Light' was removed.",
            "Two new beneficiaries, 'New York Investments' and 'Chen Family Trust', were registered.",
            "A high-priority ticket was logged to document the beneficiary audit.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_064",
        instruction=(
            "Handle a straightforward profile update and loan review for customer Zoltan Nagy (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11). "
            "First, access his profile and confirm identity using his passport 'Se620000'. "
            "Update his contact details to the new email 'liam.oconnor.farm@example.ie' and phone number '+353 87 999 8888'. "
            "Following that, provide a summary of the status of his loan applications to review his active business loan 'loan_biz_005'. "
            "Acquire the current balance of his checking account 'acc_chk_12001'. "
            "List his present beneficiaries to affirm his setup. "
            "Finally, modify his account preferences to enable paperless billing."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "id_document": "Se620000"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "new_email": "liam.oconnor.farm@example.ie", "new_phone": "+353 87 999 8888"}),
            Action(name="SummarizeLoanApplicationsByStatus", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_12001"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "preferences": {"paperless_billing": True}}),
        ],
        outputs=[
            "Identity verified for Zoltan Nagy.",
            "Customer's contact information was updated.",
            "Loan status was summarized and checking account balance was retrieved.",
            "Beneficiary list was checked and account preferences were updated to paperless billing.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_065",
        instruction=(
            "Assist customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) in consolidating his beneficiary list and examining his recent spending from account 'acc_chk_1001'. "
            "The current date is 2025-07-24. "
            "Begin by accessing his profile and verifying his identity with his passport 'lF146011'. "
            "Compile a list of his beneficiaries. "
            "She aims to remove her two existing beneficiaries: 'Elena Popescu' (ID: bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d) and 'Anytown Utility Services' (ID: bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e). "
            "Post-removal, register a single new consolidated beneficiary with ID 'bene_user_065_doe_trust' for the 'Doe Family Trust', holding account number '102030405' at 'Bank of America' (routing: '026009593') in the 'USA'. "
            "Subsequently, obtain transaction history for the last 60 days from her checking account 'acc_chk_1001'. "
            "Compile her expenses for the last complete month, June 2025. "
            "In closing, file a ticket with ID 'ticket_user_065_bene_consolidation' under category 'Account Management', priority 'Medium', through 'Web Portal', including the request details: 'Beneficiary list consolidated to single Doe Family Trust. "
            "Recent expenditure review also provided to customer.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "beneficiary_id": "bene_user_065_doe_trust",
                "beneficiary_name": "Doe Family Trust",
                "country": "USA",
                "bank_details": {"account_number": "102030405", "bank_name": "Bank of America", "routing_info": "026009593"}
            }),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_1001", "days": 60}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_1001", "month": "2025-06"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_065_bene_consolidation",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Beneficiary list consolidated to single Doe Family Trust. Recent spending review also provided to customer."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "Both existing beneficiaries, Elena Popescu and Anytown Utility Services, were removed.",
            "A new consolidated beneficiary, 'Doe Family Trust', was successfully registered.",
            "Recent spending was reviewed and a ticket was logged to confirm the beneficiary consolidation.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_066",
        instruction=(
            "Handle a comprehensive financial and security evaluation for the high-net-worth client Zoltan Nagy (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "Begin by accessing his profile and confirming his identity with his driver's license 'VI933872'. "
            "Acquire the transaction history for his checking account 'acc_chk_3001' over the past 180 days and consolidate his expenditures for October 2023. "
            "Additionally, retrieve the current balance of his investment account 'acc_inv_3002'. "
            "As a security precaution, place a temporary freeze on the investment account 'acc_inv_3002' citing 'Pending customer confirmation for annual review' as the reason. "
            "Update Zoltan Nagy's main contact details to email 'd.chen.office@example.com' and phone '555-987-2222'. "
            "Lastly, file a ticket with ID 'ticket_user_066_annual_review' under category 'Audit', priority 'High', via 'Internal System', with the request specifics: 'Annual review complete. "
            "Financials reviewed, investment account temporarily frozen, and contact info updated.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "VI933872"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_3001", "days": 180}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_3001", "month": "2023-10"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_inv_3002"}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_inv_3002", "alert_reason": "Pending customer confirmation for annual review."}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "new_email": "d.chen.office@example.com", "new_phone": "555-987-2222"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "ticket_user_066_annual_review",
                "category": "Audit",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Annual review complete. Financials reviewed, investment account temporarily frozen, and contact info updated."
            }),
        ],
        outputs=[
            "Identity verified for Zoltan Nagy and a 180-day financial review of his checking account was completed.",
            "The balance of his investment account was retrieved and the account was temporarily frozen for security.",
            "The customer's contact information was updated and a high-priority audit ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_067",
        instruction=(
            "Coordinate assistance for international customer Kenji Tanaka (ID: e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2) concerning his payment arrangements update. "
            "Initially, retrieve his profile and authenticate his identity with his driver's license 'im665671'. "
            "He intends to cancel the monthly scheduled payment directed to his mother, identified by 'sp_a2c1d9b3-f6a5-b4c3-d2e1-f0a9b8c7d6e5'. "
            "Subsequently, modify his list of beneficiaries. "
            "Enumerate his existing beneficiaries and eliminate his mother, Marie Dubois (ID: bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c). "
            "Following this, register a new international beneficiary with ID 'bene_user_067_nyc_school' for the 'NYC Art School', with account number '987654321' at 'Bank of NY' (routing: '021000018') in the 'USA'. "
            "Adjust his account preferences to designate the 'App' as his primary communication channel. "
            "Finally, generate a support ticket with ID 'ticket_user_067_bene_update' under category 'Beneficiary Management', priority 'Medium', via 'Email', with the request outline: 'Canceled scheduled payment to Marie Dubois and updated beneficiary list to replace his with NYC Art School.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "id_document": "im665671"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_a2c1d9b3-f6a5-b4c3-d2e1-f0a9b8c7d6e5"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "beneficiary_id": "bene_user_067_nyc_school",
                "beneficiary_name": "NYC Art School",
                "country": "USA",
                "bank_details": {"account_number": "987654321", "bank_name": "Bank of NY", "routing_info": "021000018"}
            }),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "preferences": {"communication_channel": "App"}}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "ticket_id": "ticket_user_067_bene_update",
                "category": "Beneficiary Management",
                "priority": "Medium",
                "channel": "Email",
                "request_details": "Canceled scheduled payment to Marie Dubois and updated beneficiary list to replace her with NYC Art School."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "The scheduled payment to his mother was successfully canceled.",
            "Beneficiary list was updated: Marie Dubois was removed and 'NYC Art School' was added.",
            "Account preferences were updated and a support ticket was logged to confirm the changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_068",
        instruction=(
            "Supervise the reconfiguration of the joint account 'acc_chk_2001' by exchanging one of the account holders. "
            "The primary holder is Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef). "
            "Remove the holder represented by ID 'cust_joint_005' and substitute with Zoltan Nagy (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "Start by obtaining Elena Popescu's profile and validating her identity with her national ID 'jd195515'. "
            "Then, procure Zoltan Nagy's profile and confirm his identity using his national ID 'pI260068'. "
            "Remove the joint holder 'cust_joint_005', then incorporate Zoltan Nagy as the new joint holder. "
            "After these holder changes, enumerate Elena Popescu's beneficiaries, including Kenji Tanaka (ID: bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f); proceed to delete her. "
            "Register Zoltan Nagy as the primary beneficiary with ID 'bene_user_068_d_chen', using account number '6666' at 'City General Bank' (routing: 'N/A') in the 'USA'. "
            "Modify account preferences to utilize 'SMS' for notifications. "
            "Lastly, create a ticket with ID 'ticket_user_068_reconfig' under category 'Account Management', priority 'High', via 'Internal System', detailing the request: 'Joint account acc_chk_2001 reconfigured. "
            "Holder cust_joint_005 replaced with Zoltan Nagy. "
            "Beneficiary list updated.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "pI260068"}),
            Action(name="RemoveJointAccountHolder", kwargs={"account_id": "acc_chk_2001", "holder_id": "cust_joint_005"}),
            Action(name="AddJointAccountHolder", kwargs={"account_id": "acc_chk_2001", "holder_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_user_068_d_chen",
                "beneficiary_name": "Zoltan Nagy",
                "country": "USA",
                "bank_details": {"account_number": "6666", "bank_name": "City General Bank", "routing_info": "N/A"}
            }),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "preferences": {"communication_channel": "SMS"}}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_068_reconfig",
                "category": "Account Management",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Joint account acc_chk_2001 reconfigured. Holder cust_joint_005 replaced with Zoltan Nagy. Beneficiary list updated."
            }),
        ],
        outputs=[
            "Identities of primary holder Elena Popescu and new joint holder Zoltan Nagy verified.",
            "Joint holder for account acc_chk_2001 was successfully swapped.",
            "Beneficiary Kenji Tanaka was removed and replaced with the new joint holder, Zoltan Nagy.",
            "Account preferences were updated and a high-priority ticket was logged to document the reconfiguration.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_069",
        instruction=(
            "Conduct a simple data retrieval operation for customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) regarding his personal documentation. "
            "First, obtain his profile and confirm his identity with his passport 'lF146011'. "
            "Gather the balances for his checking account 'acc_chk_1001' and his savings account 'acc_sav_1002'. "
            "Afterward, provide an overview of the status of his loan applications. "
            "Lastly, list all current beneficiaries attached to his account. "
            "Conclude by submitting a low-priority support ticket with ID 'ticket_user_069_info_review' under category 'General Inquiry' via 'Web Portal', including the request specifics: 'Customer requested a full summary of his accounts, loans, and beneficiaries for his records. "
            "Review complete.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="SummarizeLoanApplicationsByStatus", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_069_info_review",
                "category": "General Inquiry",
                "priority": "Low",
                "channel": "Web Portal",
                "request_details": "Customer requested a full summary of his accounts, loans, and beneficiaries for his records. Review complete."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "Balances for his checking and savings accounts were retrieved.",
            "A summary of his loan status was provided.",
            "A list of his current beneficiaries was retrieved and a ticket was logged to confirm the review.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_070",
        instruction=(
            "Facilitate customer Zoltan Nagy (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11) in processing an additional payment towards his business loan. "
            "Start by acquiring his profile and verifying his identity using his passport 'Se620000'. "
            "Evaluate his loan application status to authenticate details of his ongoing loan. "
            "Acquire the present balances of his checking account 'acc_chk_12001' and his loan account 'acc_loan_12002'. "
            "He aims to make an extra payment amounting to 2000 EUR. "
            "Facilitate a transfer of this amount from 'acc_chk_12001' to 'acc_loan_12002'. "
            "Following the transaction, update his core contact details to email 'liam.o.updates@example.ie' and phone '+353 87 111 2222'. "
            "Conclude by recording a support ticket with ID 'ticket_user_070_loan_payment' under category 'Loan Support', priority 'Medium', via 'Web Portal', containing the request details: 'Customer made a one-time extra payment of 2000 EUR to business loan account acc_loan_12002.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "id_document": "Se620000"}),
            Action(name="SummarizeLoanApplicationsByStatus", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_12001"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_loan_12002"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_12001", "to_account": "acc_loan_12002", "amount": 2000.00}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "new_email": "liam.o.updates@example.ie", "new_phone": "+353 87 111 2222"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "ticket_id": "ticket_user_070_loan_payment",
                "category": "Loan Support",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Customer made a one-time extra payment of 2000 EUR to business loan account acc_loan_12002."
            }),
        ],
        outputs=[
            "Identity verified for Zoltan Nagy and loan status confirmed.",
            "Balances for checking and loan accounts were retrieved.",
            "An extra payment of 2000 EUR was successfully transferred to the loan account.",
            "Customer contact information was updated and a ticket was logged to document the payment.",
        ],
    ),
     Task(
        annotator="0",
        user_id="user_071",
        instruction=(
            "Handle a complete account consolidation for customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "Current date is 2025-07-24. "
            "Begin by obtaining his profile and confirming his identity with his passport 'lF146011'. "
            "He intends to transfer funds from his checking account 'acc_chk_1001' to his savings account 'acc_sav_1002' and subsequently close the checking account. "
            "Start by obtaining the transaction history for the checking account for the past 60 days and summarizing his June 2025 expenses. "
            "Then, acquire the current balance of both the checking account 'acc_chk_1001' (with a balance of $5230.50) and the savings account 'acc_sav_1002'. "
            "Move the entire amount of $5230.50 from the checking account to the savings account. "
            "Once the transfer is executed and the checking account holds no funds, process a request to close the checking account 'acc_chk_1001'. "
            "In conclusion, file a ticket with ID 'ticket_user_071_consolidation' under category 'Account Closure', priority 'High', via 'Web Portal', including the request details: 'Customer account consolidation complete. "
            "Full balance from acc_chk_1001 transferred to acc_sav_1002. "
            "Checking account submitted for closure.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_1001", "days": 60}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_1001", "month": "2025-06"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_sav_1002", "amount": 5230.50}),
            Action(name="CloseAccountRequest", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_071_consolidation",
                "category": "Account Closure",
                "priority": "High",
                "channel": "Web Portal",
                "request_details": "Customer account consolidation complete. Full balance from acc_chk_1001 transferred to acc_sav_1002. Checking account submitted for closure."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka and a spending review on his checking account was performed.",
            "Balances for both checking and savings accounts were retrieved.",
            "The full balance from the checking account was successfully transferred to the savings account.",
            "The checking account was submitted for closure and a high-priority ticket was logged to document the consolidation.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_072",
        instruction=(
            "Coordinate updates to security settings and international beneficiaries for customer Chloe Dubois (ID: d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). "
            "Begin by obtaining his profile and confirming his identity using his driver's license 'Kt516858'. "
            "Modify his account preferences to activate all notifications and adjust his language setting to 'de-DE'. "
            "Following this, he wants to revise his beneficiary list. "
            "Display his current beneficiaries and remove the existing one, 'Klaus Schmidt' (ID: bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a). "
            "Upon removal, register a new international beneficiary with ID 'bene_user_072_paris_art' for 'Paris Art Supplies', using account IBAN 'FR7630002005500000157845Z25' at 'Societe Generale' (BIC: 'SOGEFRPP') in 'France'. "
            "Retrieve the current balance of his checking account 'acc_chk_8001'. "
            "At last, submit a ticket with ID 'ticket_user_072_updates' under category 'Account Management', priority 'Medium', via 'Web Portal', incorporating the request details: 'Customer security preferences and language updated. "
            "Beneficiary list updated to replace Klaus Schmidt with Lyon Art Supplies.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "id_document": "Kt516858"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "preferences": {"notifications": True, "language": "de-DE"}}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "beneficiary_id": "bene_user_072_paris_art",
                "beneficiary_name": "Paris Art Supplies",
                "country": "France",
                "bank_details": {"account_number": "FR7630002005500000157845Z25", "bank_name": "Societe Generale", "routing_info": "SOGEFRPP"}
            }),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "ticket_id": "ticket_user_072_updates",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Customer security preferences and language updated. Beneficiary list updated to replace Klaus Schmidt with Lyon Art Supplies."
            }),
        ],
        outputs=[
            "Identity verified for Chloe Dubois and his account preferences were updated.",
            "Beneficiary 'Klaus Schmidt' was successfully removed.",
            "New international beneficiary 'Paris Art Supplies' was registered.",
            "Checking account balance was confirmed and a ticket was logged to document the updates.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_073",
        instruction=(
            "Initiate an emergency security protocol for a suspected account takeover for customer Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef). "
            "A security alert requires immediate action. "
            "Begin by acquiring her profile. "
            "To safeguard her assets, quickly suspend activity on both her checking ('acc_chk_2001') and savings ('acc_sav_2002') accounts stating the reason 'Urgent security review due to suspected account takeover.' Following the freeze, confirm her identity using her national ID 'jd195515' to ensure communication is with the actual customer. "
            "After verification, access the transaction history for her checking account 'acc_chk_2001' covering the last 7 days to examine potential fraudulent activities. "
            "Her contact information may need updating, so adjust it to a new secure email 'jane.smith.recovery@example.com' and phone '555-999-0000'. "
            "Conclude with submitting a ticket with ID 'ticket_user_073_takeover' under category 'Security', priority 'Critical', via 'Internal System', noting the request details: 'Account takeover protocol initiated. "
            "All accounts frozen, contact info secured. "
            "Awaiting fraud investigation results.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_chk_2001", "alert_reason": "Urgent security review due to suspected account takeover."}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_sav_2002", "alert_reason": "Urgent security review due to suspected account takeover."}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_2001", "days": 7}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "new_email": "jane.smith.recovery@example.com", "new_phone": "555-999-0000"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_073_takeover",
                "category": "Security",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Account takeover protocol initiated. All accounts frozen, contact info secured. Awaiting fraud investigation results."
            }),
        ],
        outputs=[
            "Customer profile retrieved and both checking and savings accounts were immediately frozen.",
            "Identity of Elena Popescu was verified to proceed with recovery.",
            "Recent transaction history was retrieved for fraud analysis.",
            "Customer's contact info was updated to secure channels and a critical security ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_074",
        instruction=(
            "Execute a routine information check and contact update for customer Oliver Williams (ID: c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6). "
            "First, access her profile and affirm her identity through her national ID 'IJ758739'. "
            "Retrieve the current balances for her checking account 'acc_chk_7001' and her savings account 'acc_sav_7002'. "
            "Amend her contact details to the new email 'f.alfassi.contact@example.ae' and a new phone number '+971 50 222 3333'. "
            "Then, provide a list of her current beneficiaries for her records. "
            "Conclude by submitting a low-priority support ticket with ID 'ticket_user_074_info_check' under category 'General Inquiry' via 'Web Portal' with the request details: 'Customer requested a check of her account balances and beneficiary list. "
            "Contact info also updated.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "id_document": "IJ758739"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_7001"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_sav_7002"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "new_email": "f.alfassi.contact@example.ae", "new_phone": "+971 50 222 3333"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "ticket_id": "ticket_user_074_info_check",
                "category": "General Inquiry",
                "priority": "Low",
                "channel": "Web Portal",
                "request_details": "Customer requested a check of her account balances and beneficiary list. Contact info also updated."
            }),
        ],
        outputs=[
            "Identity verified for Oliver Williams.",
            "Balances for her checking and savings accounts were successfully retrieved.",
            "Her contact information was updated to a new email and phone number.",
            "Her beneficiary list was retrieved and a ticket was logged to confirm the actions.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_075",
        instruction=(
            "Facilitate updates to scheduled payments and beneficiaries for customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "First, obtain his profile and confirm his identity using his passport 'lF146011'. "
            "He wishes to cancel two scheduled payments: one with ID 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d' and another with ID 'sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e'. "
            "Following that, he desires to amend his beneficiaries. "
            "Display his current beneficiaries and remove 'Anytown Utility Services' (ID: bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e). "
            "Subsequently, register a new beneficiary with ID 'bene_user_075_new_utility' for 'Metropolis Water Co', with account number '123456789' at 'Metropolis Bank' (routing: '021200339') in the 'USA'. "
            "Change his account preferences to send alerts via the 'App'. "
            "Finally, submit a ticket with ID 'ticket_user_075_updates' under category 'Account Management', priority 'Medium', via 'Mobile App', detailing the request: 'Canceled two scheduled payments and updated beneficiary list from Anytown Utility to Metropolis Water Co.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "beneficiary_id": "bene_user_075_new_utility",
                "beneficiary_name": "Metropolis Water Co",
                "country": "USA",
                "bank_details": {"account_number": "123456789", "bank_name": "Metropolis Bank", "routing_info": "021200339"}
            }),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "preferences": {"communication_channel": "App"}}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_075_updates",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Mobile App",
                "request_details": "Canceled two scheduled payments and updated beneficiary list from Anytown Utility to Metropolis Water Co."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "Two scheduled payments were successfully canceled.",
            "Beneficiary 'Anytown Utility Services' was removed and replaced with 'Metropolis Water Co'.",
            "Account preferences were updated and a ticket was logged to confirm all changes.",
        ],
    ),
     Task(
        annotator="0",
        user_id="user_076",
        instruction=(
            "Handle the detailed separation of the joint account 'acc_chk_2001' due to a divorce settlement. "
            "The main holder is Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef), and the joint holder to be eliminated is Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), identified as holder ID 'cust_joint_005'. "
            "Initially, retrieve the profiles for both Elena Popescu and Kenji Tanaka, and confirm their identities using their respective documents: national ID 'jd195515' for Jane and passport 'lF146011' for John. "
            "Upon verification, obtain the current balance of the joint account 'acc_chk_2001', which is 3100.75 CAD. "
            "Move the settlement amount of 1500.00 CAD from 'acc_chk_2001' to Kenji Tanaka's personal account number '1111'. "
            "Then, eliminate Kenji Tanaka ('cust_joint_005') as a joint holder from 'acc_chk_2001'. "
            "Subsequently, update Elena Popescu's beneficiary list: enumerate her beneficiaries, then erase the record for Kenji Tanaka (ID: bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f). "
            "Ultimately, submit a ticket with ID 'ticket_user_076_divorce_settlement' under category 'Legal', priority 'High', via 'Internal System', with the request details: 'Divorce settlement protocol executed for account acc_chk_2001. "
            "Joint holder cust_joint_005 removed, funds split, and beneficiary list updated as per legal agreement.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_2001", "to_account": "1111", "amount": 1500.00}),
            Action(name="RemoveJointAccountHolder", kwargs={"account_id": "acc_chk_2001", "holder_id": "cust_joint_005"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_076_divorce_settlement",
                "category": "Legal",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Divorce settlement protocol executed for account acc_chk_2001. Joint holder cust_joint_005 removed, funds split, and beneficiary list updated as per legal agreement."
            }),
        ],
        outputs=[
            "Identities of both Elena Popescu and Kenji Tanaka were successfully verified.",
            "A settlement amount of 1500.00 CAD was transferred from the joint account to Kenji Tanaka's personal account.",
            "Kenji Tanaka was removed as a joint holder from account acc_chk_2001.",
            "Kenji Tanaka was removed from Elena Popescu's beneficiary list and a high-priority legal ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_077",
        instruction=(
            "Support customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) in establishing a new international payment arrangement from his account 'acc_chk_1001'. "
            "Initially, access his profile and authenticate his identity via his passport 'lF146011'. "
            "He intends to replace a domestic bill payment. "
            "Nullify his scheduled monthly payment to Anytown Utility, which holds the ID 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d'. "
            "Next, itemize his beneficiaries and remove the 'Anytown Utility Services' beneficiary (ID: bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e). "
            "Subsequently, register a new international supplier with ID 'bene_user_077_uk_supplier' for 'London Imports Ltd', with account number 'GB29NWBK60161331926819' at 'NatWest' (routing: 'NWBKGB2L') in the 'United Kingdom'. "
            "Verify the balance of the source account 'acc_chk_1001' to ensure funds are available for future remittances. "
            "Ultimately, submit a ticket with ID 'ticket_user_077_intl_setup' under category 'Payments', priority 'Medium', via 'Web Portal', incorporating the request details: 'Replaced domestic beneficiary Anytown Utility with international beneficiary Manchester Imports Ltd and canceled original scheduled payment.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "beneficiary_id": "bene_user_077_uk_supplier",
                "beneficiary_name": "London Imports Ltd",
                "country": "United Kingdom",
                "bank_details": {"account_number": "GB29NWBK60161331926819", "bank_name": "NatWest", "routing_info": "NWBKGB2L"}
            }),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_077_intl_setup",
                "category": "Payments",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Replaced domestic beneficiary Anytown Utility with international beneficiary Manchester Imports Ltd and canceled original scheduled payment."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "The scheduled payment to 'Anytown Utility' was canceled and the beneficiary was removed.",
            "A new international beneficiary, 'London Imports Ltd', was successfully registered.",
            "The checking account balance was confirmed and a ticket was logged documenting the changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_078",
        instruction=(
            "Coordinate a comprehensive security audit for customer Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef) following the alert of a minor suspicious transaction. "
            "The current date is 2025-07-24. "
            "First, gather her profile and confirm her identity using her national ID 'jd195515'. "
            "Promptly lock her checking account 'acc_chk_2001' stating the reason 'Suspicious transaction detected, account under review.' Then, scrutinize her spending patterns by retrieving the full transaction history for 'acc_chk_2001' and compiling her expenditures for April, May, and June of 2025. "
            "As a preventive measure, revise her contact information to a secure secondary email 'jane.smith.sec.2@example.com' and phone '555-222-1111'. "
            "Ultimately, file a ticket with ID 'ticket_user_078_sec_audit' under category 'Security', priority 'Critical', via 'Internal System', detailing: 'Security audit triggered. "
            "Account acc_chk_2001 frozen, spending patterns reviewed, and contact info secured.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_chk_2001", "alert_reason": "Suspicious transaction detected, account under review."}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_2001", "month": "2025-04"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_2001", "month": "2025-05"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_2001", "month": "2025-06"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "new_email": "jane.smith.sec.2@example.com", "new_phone": "555-222-1111"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_078_sec_audit",
                "category": "Security",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Security audit triggered. Account acc_chk_2001 frozen, spending patterns reviewed, and contact info secured."
            }),
        ],
        outputs=[
            "Identity verified for Elena Popescu and her checking account was frozen.",
            "A 3-month spending review was conducted on the checking account.",
            "Customer's contact information was updated to secure channels.",
            "A critical security ticket was logged to document the audit and security measures taken.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_079",
        instruction=(
            "Coordinate a straightforward information retrieval task for customer Zoltan Nagy (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "Start by obtaining his profile and confirming his identity with his national ID 'pI260068'. "
            "Then, fetch the real-time balances of his checking account 'acc_chk_3001' and his investment account 'acc_inv_3002'. "
            "Next, compile the status of his loan applications; he has an active mortgage with ID 'loan_mort_001'. "
            "Enumerate his current beneficiaries for his review. "
            "Finally, adjust his account preferences to ensure notifications are activated."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "pI260068"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_3001"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_inv_3002"}),
            Action(name="SummarizeLoanApplicationsByStatus", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "preferences": {"notifications": True}}),
        ],
        outputs=[
            "Identity verified for Zoltan Nagy.",
            "Balances for his checking and investment accounts were successfully retrieved.",
            "His loan application status was summarized and his beneficiaries were listed.",
            "His account preferences were updated to enable notifications.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_080",
        instruction=(
            "Assist customer Kenji Tanaka (ID: e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2) with the management of his credit card account 'acc_crd_9002'. "
            "First, acquire his profile and validate his identity using his driver's license 'im665671'. "
            "Retrieve the balance of his credit card 'acc_crd_9002', which stands at -500.00 EUR. "
            "Also obtain the balance of his checking account 'acc_chk_9001'. "
            "He wishes to fully pay his credit card. "
            "Move 500.00 EUR from his checking account to his credit card account. "
            "Following the payment, revise his primary contact information to email 'chloe.d.primary@example.fr' and phone '+33 6 12 34 55 55'. "
            "Ultimately, submit a ticket with ID 'ticket_user_080_cc_payment' under category 'Payments', priority 'Low', via 'Mobile App', specifying: 'Customer paid off credit card acc_crd_9002 in full and updated primary contact details.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "id_document": "im665671"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_crd_9002"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_9001"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_9001", "to_account": "acc_crd_9002", "amount": 500.00}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "new_email": "chloe.d.primary@example.fr", "new_phone": "+33 6 12 34 55 55"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "ticket_id": "ticket_user_080_cc_payment",
                "category": "Payments",
                "priority": "Low",
                "channel": "Mobile App",
                "request_details": "Customer paid off credit card acc_crd_9002 in full and updated primary contact details."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka and account balances were checked.",
            "A payment of 500.00 EUR was transferred from checking to pay off the credit card.",
            "Customer's primary contact information was updated.",
            "A ticket was logged to confirm the payment and contact update.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_081",
        instruction=(
            "Manage a transaction dispute for the joint account 'acc_chk_2001'. "
            "The primary holder, Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef), reported a fraudulent charge. "
            "The other joint holder is Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "Begin by retrieving the profiles for both Elena Popescu and Kenji Tanaka. "
            "Confirm Jane's identity with her national ID 'jd195515' and John's identity with her passport 'lF146011'. "
            "Promptly freeze the joint account 'acc_chk_2001' for the reason 'Dispute filed by primary holder; account under investigation.' Obtain the transaction history for the account from the past 30 days. "
            "The transaction in question is marked as 'txn_0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d'. "
            "Prepare a detailed dispute ticket with ID 'ticket_user_081_joint_dispute' in the 'Dispute' category, prioritize it as 'Critical', and process it through 'Internal System'. "
            "The operation should focus on 'Transaction' entity 'txn_0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d' for 'CHARGEBACK', including the note: 'Primary holder Elena Popescu disputes this charge on the joint account.' Lastly, update Elena Popescu's main contact details to email 'jane.s.dispute@example.com' and phone '555-123-1122'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_chk_2001", "alert_reason": "Dispute filed by primary holder; account under investigation."}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_2001", "days": 30}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_081_joint_dispute",
                "category": "Dispute",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": {
                    "target_entity": "Transaction",
                    "target_id": "txn_0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
                    "operation": "CHARGEBACK",
                    "parameters": {"note": "Primary holder Elena Popescu disputes this charge on the joint account."}
                }
            }),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "new_email": "jane.s.dispute@example.com", "new_phone": "555-123-1122"}),
        ],
        outputs=[
            "Profiles retrieved and identities verified for both joint account holders.",
            "The joint account 'acc_chk_2001' was frozen due to a dispute.",
            "Transaction history was retrieved for investigation.",
            "A critical dispute ticket was submitted and the primary holder's contact information was updated.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_082",
        instruction=(
            "Support customer Oliver Williams (ID: c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6) in organizing her accounts for an extended vacation. "
            "Start by accessing her profile and confirming her identity using her national ID 'IJ758739'. "
            "She wants to postpone a significant quarterly payment; annul the scheduled payment with ID 'sp_a2c1d9b3-d2e1-f0a9-b8c7-d6e5f4a3b2c1'. "
            "For additional security, freeze her savings account 'acc_sav_7002' stating precisely: 'Customer on extended travel; account frozen for security.' Adjust her account preferences to utilize 'SMS' for vital alerts. "
            "Finally, generate a ticket with ID 'ticket_user_082_travel' filed under category 'Account Management', rated 'High' in priority, executed via 'Internal System', presenting the request: 'Travel Notice: Canceled scheduled payment and froze savings account for security during travel.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "id_document": "IJ758739"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_a2c1d9b3-d2e1-f0a9-b8c7-d6e5f4a3b2c1"}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_sav_7002", "alert_reason": "Customer on extended travel; account frozen for security."}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "preferences": {"communication_channel": "SMS"}}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "ticket_id": "ticket_user_082_travel",
                "category": "Account Management",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Travel Notice: Canceled scheduled payment and froze savings account for security during travel."
            }),
        ],
        outputs=[
            "Identity verified for Oliver Williams.",
            "A large scheduled payment was successfully canceled.",
            "Her savings account was frozen for security and preferences were updated for travel alerts.",
            "A high-priority travel notice ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_083",
        instruction=(
            "Coordinate a thorough Q2 2025 financial audit for the business account belonging to customer Oliver Williams (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23). "
            "The date is 2025-07-24. "
            "Acquire his profile and verify his identity with his national ID 'uY143801'. "
            "Collect the transaction history for his business checking account 'acc_chk_24001' over the previous 90 days. "
            "Subsequently, summarize the monthly expenditures for April, May, and June of 2025 from that account. "
            "List his beneficiaries; he currently has none. "
            "Register a new key supplier under ID 'bene_user_083_logistics' for 'Nigerian Logistics Corp', with the account number '9876543210' at 'Zenith Bank' (routing: 'N/A') in 'Nigeria'. "
            "Update the primary business contact information to email 'adebayor.biz.primary@example.ng' and phone '+234 801 222 3333'. "
            "In conclusion, submit a ticket with ID 'ticket_user_083_q2_audit' under the category 'Audit', labelled 'High' priority, via 'Internal System', providing the request details: 'Q2 2025 audit for business account acc_chk_24001 complete. "
            "Expenses for 3 months aggregated. "
            "New supplier beneficiary added and contact info updated.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "id_document": "uY143801"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_24001", "days": 90}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_24001", "month": "2025-04"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_24001", "month": "2025-05"}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_24001", "month": "2025-06"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                "beneficiary_id": "bene_user_083_logistics",
                "beneficiary_name": "Nigerian Logistics Corp",
                "country": "Nigeria",
                "bank_details": {"account_number": "9876543210", "bank_name": "Zenith Bank", "routing_info": "N/A"}
            }),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "new_email": "adebayor.biz.primary@example.ng", "new_phone": "+234 801 222 3333"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                "ticket_id": "ticket_user_083_q2_audit",
                "category": "Audit",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Q2 2025 audit for business account acc_chk_24001 complete. Expenses for 3 months aggregated. New supplier beneficiary added and contact info updated."
            }),
        ],
        outputs=[
            "Identity verified for Oliver Williams and a Q2 2025 financial review was conducted.",
            "Expenses for April, May, and June were aggregated.",
            "A new supplier beneficiary was added to the business profile.",
            "The primary business contact information was updated and a high-priority audit ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_084",
        instruction=(
            "Facilitate a straightforward profile update and balance verification for customer Adetokunbo Adebayor (ID: f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3). "
            "Begin by retrieving his profile and confirming his identity using his national ID 'nh464131'. "
            "Change his email to 'kenji.t.personal@example.jp' and update his phone number to '+81 90-1111-2222'. "
            "Then, adjust his account preferences to set the language to 'ja-JP'. "
            "Acquire the current balances of his checking account 'acc_chk_10001' and his savings account 'acc_sav_10002'. "
            "Lastly, dispatch a low-priority support ticket with ID 'ticket_user_084_profile_updates' under the 'Account Management' category through 'Email' with the request narrative: 'Customer profile updated with new contact info and language preference.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "id_document": "nh464131"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "new_email": "kenji.t.personal@example.jp", "new_phone": "+81 90-1111-2222"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "preferences": {"language": "ja-JP"}}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_10001"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_sav_10002"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "ticket_id": "ticket_user_084_profile_updates",
                "category": "Account Management",
                "priority": "Low",
                "channel": "Email",
                "request_details": "Customer profile updated with new contact info and language preference."
            }),
        ],
        outputs=[
            "Identity verified for Adetokunbo Adebayor.",
            "The customer's contact email and phone number were successfully updated.",
            "The customer's language preference was set to Japanese.",
            "Balances for checking and savings accounts were retrieved and a ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_085",
        instruction=(
            "Help customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) with organizing his beneficiaries and executing a payment from his account 'acc_chk_1001'. "
            "Start by retrieving his profile and verifying his identity using his passport 'lF146011'. "
            "Enumerate her current beneficiaries, and then remove 'Elena Popescu' (ID: bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d) and 'Anytown Utility Services' (ID: bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e). "
            "Following their removal, register a new unified beneficiary with ID 'bene_user_085_doe_trust' for 'Doe Family Trust', featuring the account number '102030405' at 'Bank of America' (routing: '026009593') located in the 'USA'. "
            "Fetch the current balance of the checking account 'acc_chk_1001'. "
            "Then, transfer $2,500.00 from the checking account to the 'Doe Family Trust' beneficiary's account number '102030405'. "
            "Finally, file a ticket with ID 'ticket_user_085_consolidation' under the 'Beneficiary Management' category, assign a 'Medium' priority, process it via 'Web Portal', with accompanying request details: 'Beneficiary list consolidated to the Doe Family Trust and an initial transfer of $2500 was completed.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "beneficiary_id": "bene_user_085_doe_trust",
                "beneficiary_name": "Doe Family Trust",
                "country": "USA",
                "bank_details": {"account_number": "102030405", "bank_name": "Bank of America", "routing_info": "026009593"}
            }),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_1001", "to_account": "102030405", "amount": 2500.00}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_085_consolidation",
                "category": "Beneficiary Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Beneficiary list consolidated to the Doe Family Trust and an initial transfer of $2500 was completed."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "His two existing beneficiaries were successfully removed.",
            "A new consolidated beneficiary, 'Doe Family Trust', was registered.",
            "A transfer of $2,500.00 was made to the new beneficiary and a ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_086",
        instruction=(
            "Handle the complete closure of a business account for Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), as he is ceasing operations. "
            "The account to be closed is 'acc_chk_1001'. "
            "Initially, obtain his profile and confirm his identity using his passport 'lF146011'. "
            "Prior to closure, ensure all recurring payments are terminated. "
            "Cancel the scheduled payments with IDs 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d' and 'sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e'. "
            "Subsequently, delete all business beneficiaries. "
            "List her beneficiaries, then remove 'Elena Popescu' (ID: bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d) and 'Anytown Utility Services' (ID: bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e). "
            "Determine the final balance of the business account 'acc_chk_1001', which is $5230.50. "
            "Transfer the entire balance to her designated personal external account, with account number '999888777'. "
            "Once the account has been depleted, submit a request to close the business account 'acc_chk_1001'. "
            "Ultimately, submit a ticket with ID 'ticket_user_086_biz_closure' under category 'Account Closure', priority 'High', via 'Internal System', detailing the request: 'Business account acc_chk_1001 closure process initiated. "
            "All payments and beneficiaries removed, funds transferred, and account submitted for final closure.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_1001", "to_account": "999888777", "amount": 5230.50}),
            Action(name="CloseAccountRequest", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_086_biz_closure",
                "category": "Account Closure",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Business account acc_chk_1001 closure process initiated. All payments and beneficiaries removed, funds transferred, and account submitted for final closure."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "All scheduled payments from the business account have been canceled.",
            "All beneficiaries linked to the business account have been removed.",
            "The remaining balance was transferred and the business account was submitted for closure, with a ticket logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_087",
        instruction=(
            "Assist customer Zoltan Nagy (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11) with business loan administration. "
            "First, retrieve his profile and authenticate his identity using his passport 'Se620000'. "
            "Summarize his loan application status to confirm the active loan details. "
            "Then, obtain the current balances of his checking account 'acc_chk_12001' and loan account 'acc_loan_12002'. "
            "He intends to make an additional payment of 4000.00 EUR. "
            "Move this amount from his checking to his loan account. "
            "After processing the payment, update his contact details to email 'liam.oconnor.loan@example.ie' and phone '+353 87 333 4444' for all future loan-related communications. "
            "Finally, file a support ticket with ID 'ticket_user_087_refi_inquiry' under category 'Loan Support', priority 'Medium', via 'Web Portal', containing the request details: 'Customer made a 4000 EUR extra payment on loan associated with account acc_loan_12002. "
            "Inquiring about refinancing options.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "id_document": "Se620000"}),
            Action(name="SummarizeLoanApplicationsByStatus", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_12001"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_loan_12002"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_12001", "to_account": "acc_loan_12002", "amount": 4000.00}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "new_email": "liam.oconnor.loan@example.ie", "new_phone": "+353 87 333 4444"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "ticket_id": "ticket_user_087_refi_inquiry",
                "category": "Loan Support",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Customer made a 4000 EUR extra payment on loan associated with account acc_loan_12002. Inquiring about refinancing options."
            }),
        ],
        outputs=[
            "Identity verified for Zoltan Nagy and his loan status was confirmed.",
            "Balances for checking and loan accounts were retrieved.",
            "An extra payment of 4000.00 EUR was successfully transferred to his loan account.",
            "The customer's contact information was updated and a ticket was logged with his refinancing inquiry.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_088",
        instruction=(
            "Coordinate a comprehensive audit and restructuring of the joint account 'acc_chk_2001'. "
            "Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef) is the primary holder, with Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) as the joint holder, identified as holder ID 'cust_joint_005'. "
            "To begin, access the profiles and verify the identities for both Elena Popescu (using national ID 'jd195515') and Kenji Tanaka (using passport 'lF146011'). "
            "Retrieve the account's transaction history for the past 90 days and compile the expenses for June 2025. "
            "As the account holders are parting ways, remove Kenji Tanaka ('cust_joint_005') as a joint holder. "
            "Then, update Elena Popescu's beneficiaries. "
            "List them first, then remove his sole beneficiary, Kenji Tanaka (ID: bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f). "
            "Register two new beneficiaries for his: firstly, with ID 'bene_user_088_parents', is 'Smith Parents Trust' on account '111222333' at 'TD Bank' (routing: 'N/A') in 'Canada'. "
            "Secondly, with ID 'bene_user_088_charity', is 'Canadian Wildlife Fund' on account '444555666' at 'RBC' (routing: 'N/A') in 'Canada'. "
            "Ultimately, submit a ticket with ID 'ticket_user_088_reconfig' under category 'Account Management', priority 'High', via 'Internal System', containing the request details: 'Joint account acc_chk_2001 reconfigured to single owner. "
            "Holder cust_joint_005 removed. "
            "All beneficiaries updated.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_2001", "days": 90}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_2001", "month": "2025-06"}),
            Action(name="RemoveJointAccountHolder", kwargs={"account_id": "acc_chk_2001", "holder_id": "cust_joint_005"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_user_088_parents", "beneficiary_name": "Smith Parents Trust", "country": "Canada",
                "bank_details": {"account_number": "111222333", "bank_name": "TD Bank", "routing_info": "N/A"}
            }),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_user_088_charity", "beneficiary_name": "Canadian Wildlife Fund", "country": "Canada",
                "bank_details": {"account_number": "444555666", "bank_name": "RBC", "routing_info": "N/A"}
            }),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_088_reconfig",
                "category": "Account Management", "priority": "High", "channel": "Internal System",
                "request_details": "Joint account acc_chk_2001 reconfigured to single owner. Holder cust_joint_005 removed. All beneficiaries updated."
            }),
        ],
        outputs=[
            "Identities of both Elena Popescu and Kenji Tanaka were verified.",
            "A financial review of the joint account was completed.",
            "Kenji Tanaka was removed as a joint holder and as a beneficiary.",
            "Two new beneficiaries were registered for Elena Popescu and a ticket was logged documenting the account reconfiguration.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_089",
        instruction=(
            "Oversee a straightforward security and information update for customer Chloe Dubois (ID: d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). "
            "Initially, access her profile and confirm her identity using her driver's license 'Kt516858'. "
            "Obtain the current balances for her checking account 'acc_chk_8001' and savings account 'acc_sav_8002'. "
            "Then, modify her account preferences to switch her language to 'de-DE' and verify notifications are activated. "
            "Update his primary email to 'hans.muller.primary@example.de' and his phone contact to '+49 171 555 4444'. "
            "Ultimately, submit a ticket with ID 'ticket_user_089_updates' under category 'Account Management', priority 'Low', via 'Web Portal', containing the request details: 'Customer preferences and primary contact information updated as requested.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "id_document": "Kt516858"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_sav_8002"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "preferences": {"language": "de-DE", "notifications": True}}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "new_email": "hans.muller.primary@example.de", "new_phone": "+49 171 555 4444"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "ticket_id": "ticket_user_089_updates",
                "category": "Account Management",
                "priority": "Low",
                "channel": "Web Portal",
                "request_details": "Customer preferences and primary contact information updated as requested."
            }),
        ],
        outputs=[
            "Identity verified for Chloe Dubois.",
            "Balances for his checking and savings accounts were successfully retrieved.",
            "Account preferences were updated to German and to enable notifications.",
            "The customer's primary contact information was updated and a ticket was logged.",
        ],
    ),
     Task(
        annotator="0",
        user_id="user_090",
        instruction=(
            "Execute a transaction dispute process for customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) on his checking account 'acc_chk_1001'. "
            "Begin by accessing his profile and verifying his identity with his passport 'lF146011'. "
            "Retrieve the account's transaction history for the previous 30 days. "
            "He contests the transaction with ID 'txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f', which is a charge of $75.50 at FoodMart. "
            "Submit an elaborate dispute ticket with ID 'ticket_user_090_dispute' under category 'Dispute', priority 'High', via 'Web Portal', specifying 'Transaction' entity 'txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f' for operation 'CHARGEBACK', noting: 'Customer claims this charge from FoodMart was a duplicate charge and should be reversed.' As a caution, freeze the checking account 'acc_chk_1001' with the note 'Customer disputing transaction; account frozen pending investigation.' Following the account freeze, update the customer's contact details to email 'j.doe.disputes@example.com' and phone '123-456-1111' to ensure he receives case updates. "
            "Lastly, list the customer’s beneficiaries to identify any possible connections to the dispute."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_1001", "days": 30}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_090_dispute",
                "category": "Dispute",
                "priority": "High",
                "channel": "Web Portal",
                "request_details": {
                    "target_entity": "Transaction",
                    "target_id": "txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f",
                    "operation": "CHARGEBACK",
                    "parameters": {"note": "Customer claims this charge from FoodMart was a duplicate charge and should be reversed."}
                }
            }),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_chk_1001", "alert_reason": "Customer disputing transaction; account frozen pending investigation."}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "new_email": "j.doe.disputes@example.com", "new_phone": "123-456-1111"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka and transaction history reviewed.",
            "A high-priority dispute ticket was submitted for transaction 'txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f'.",
            "The checking account 'acc_chk_1001' was frozen as a security precaution.",
            "The customer's contact information was updated and his beneficiaries were listed.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_091",
        instruction=(
            "Handle a complex account closure for Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), who wishes to close his checking account 'acc_chk_1001' and consolidate it into his savings 'acc_sav_1002'. "
            "Initially, retrieve his profile and confirm his identity using his passport 'lF146011'. "
            "There are two scheduled payments sourced from the checking account that must be stopped before the closure. "
            "Cancel the payment with ID 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d' and the payment with ID 'sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e'. "
            "After these cancellations, obtain the total balance of the checking account 'acc_chk_1001', which is $5230.50. "
            "Transfer this full balance to his savings account 'acc_sav_1002'. "
            "Upon emptying the checking account, initiate a request to close it. "
            "Finally, lodge a ticket with ID 'ticket_user_091_closure' under the category of 'Account Closure', with priority 'High', via 'Internal System', detailing the request as follows: 'Closed acc_chk_1001 after fund consolidation. "
            "IMPORTANT: Customer requests that canceled payments (sp_b3a2c1d9.."
            "and sp_c1d9b3a2...) be manually recreated by an agent, now sourced from savings acc_sav_1002.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_sav_1002", "amount": 5230.50}),
            Action(name="CloseAccountRequest", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_091_closure",
                "category": "Account Closure",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Closed acc_chk_1001 after fund consolidation. IMPORTANT: Customer requests that canceled payments (sp_b3a2c1d9... and sp_c1d9b3a2...) be manually recreated by an agent, now sourced from savings acc_sav_1002."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "Two scheduled payments were successfully canceled from the checking account.",
            "The full balance of the checking account was transferred to savings.",
            "The checking account was submitted for closure and a high-priority ticket was logged with instructions for an agent.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_092",
        instruction=(
            "Assist international customer Adetokunbo Adebayor (ID: f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3) with updating his security settings and beneficiaries. "
            "Start by obtaining his profile and verify his identity through his national ID 'nh464131'. "
            "Modify his account preferences to enable paperless billing and set the communication channel to 'App'. "
            "He also intends to replace his primary beneficiary. "
            "Display his current beneficiaries and remove the existing one, 'Yuki Tanaka' (ID: bene_2b1c9d8e-7f6a-5b4c-3d2e-1f0a9b8c7d6e). "
            "Following the removal, register a new international beneficiary with ID 'bene_user_092_global_tech' for 'WorldWide Systems', having account number '9876543210' at 'City National Bank' (routing: '122000661') in the 'USA'. "
            "Gather the current balance of his primary checking account 'acc_chk_10001'. "
            "Conclusively, submit a ticket with ID 'ticket_user_092_updates' under 'Account Management' category, priority 'Medium', using 'Web Portal', with request details: 'Customer preferences updated. "
            "Beneficiary Yuki Tanaka replaced with new international beneficiary Global Tech Inc.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "id_document": "nh464131"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "preferences": {"paperless_billing": True, "communication_channel": "App"}}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "beneficiary_id": "bene_2b1c9d8e-7f6a-5b4c-3d2e-1f0a9b8c7d6e"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "beneficiary_id": "bene_user_092_global_tech",
                "beneficiary_name": "WorldWide Systems",
                "country": "USA",
                "bank_details": {"account_number": "9876543210", "bank_name": "City National Bank", "routing_info": "122000661"}
            }),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_10001"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "ticket_id": "ticket_user_092_updates",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Customer preferences updated. Beneficiary Yuki Tanaka replaced with new international beneficiary Global Tech Inc."
            }),
        ],
        outputs=[
            "Identity verified for Adetokunbo Adebayor and his account preferences were updated.",
            "The beneficiary 'Yuki Tanaka' was successfully removed.",
            "The new international beneficiary 'WorldWide Systems' was registered.",
            "The customer's checking account balance was checked and a ticket was logged to document the updates.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_093",
        instruction=(
            "Coordinate a detailed audit of both the checking and credit card accounts for customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "The current date is 2023-11-20. "
            "Begin by retrieving his profile and verifying his identity using his passport 'lF146011'. "
            "Obtain the transaction history for his checking account 'acc_chk_1001' covering the last 90 days and compile his expenses for October 2023. "
            "Next, gather the transaction history for his credit card 'acc_crd_1003' over the past 90 days, and compile his expenses for October 2023. "
            "As a security precaution during the customer's audit review, place a freeze on the credit card account 'acc_crd_1003' citing the reason 'Preventative security freeze while customer reviews audit results.' Update the customer's contact details to the secure secondary email 'j.doe.audit@example.com' and phone '123-555-4321'. "
            "Finally, submit a thorough audit ticket with ID 'ticket_user_093_audit' under the 'Audit' category, priority 'High', via 'Internal System', including the request details: '90-day audit complete for checking and credit accounts. "
            "October expenses aggregated. "
            "Credit card preventatively frozen. "
            "Contact information updated.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_1001", "days": 90}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_chk_1001", "month": "2023-10"}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_crd_1003", "days": 90}),
            Action(name="AggregateMonthlyExpenses", kwargs={"account_id": "acc_crd_1003", "month": "2023-10"}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_crd_1003", "alert_reason": "Preventative security freeze while customer reviews audit results."}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "new_email": "j.doe.audit@example.com", "new_phone": "123-555-4321"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_093_audit",
                "category": "Audit",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "90-day audit complete for checking and credit accounts. October expenses aggregated. Credit card preventatively frozen. Contact info updated."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "A 90-day financial audit was performed on both his checking and credit card accounts.",
            "October 2023 expenses were aggregated for both accounts.",
            "The credit card was preventatively frozen, contact info was updated, and a high-priority audit ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_094",
        instruction=(
            "Manage a simple profile update and loan status check for customer Zoltan Nagy (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "To start, retrieve his profile and authenticate his identity using his driver's license 'VI933872'. "
            "Update his email address to 'david.chen.student@example.edu' and change his phone number to '555-111-4444'. "
            "Proceed to summarize the status of his loan applications and list his beneficiaries. "
            "Lastly, adjust his account preferences to enable notifications."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "VI933872"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "new_email": "david.chen.student@example.edu", "new_phone": "555-111-4444"}),
            Action(name="SummarizeLoanApplicationsByStatus", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "preferences": {"notifications": True}}),
        ],
        outputs=[
            "Identity verified for Zoltan Nagy.",
            "His contact information (email and phone) was successfully updated.",
            "His loan application status was summarized.",
            "His beneficiary list was checked and his account preferences were updated to enable notifications.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_095",
        instruction=(
            "Facilitate a joint holder removal and final settlement transfer for customer Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef), who is removing a joint holder from her account 'acc_chk_2001'. "
            "The joint holder to be removed is Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), listed as holder ID 'cust_joint_005'. "
            "First, acquire the profiles for both Elena Popescu and Kenji Tanaka and confirm their identities using their respective documents: national ID 'jd195515' for Jane and passport 'lF146011' for John. "
            "Following verification, remove Kenji Tanaka ('cust_joint_005') as a joint account holder from 'acc_chk_2001'. "
            "Retrieve the current account balance to confirm available funds. "
            "Subsequently, transfer a final settlement amount of 1000.00 CAD to Kenji Tanaka's personal checking account with the account number '1111'. "
            "Finally, register a ticket with ID 'ticket_user_095_settlement' under the 'Legal' category, priority 'High', via 'Internal System', including the request specifics: 'Joint holder cust_joint_005 (Kenji Tanaka) removed from account acc_chk_2001. "
            "Final settlement of 1000.00 CAD transferred.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="RemoveJointAccountHolder", kwargs={"account_id": "acc_chk_2001", "holder_id": "cust_joint_005"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_2001", "to_account": "1111", "amount": 1000.00}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_095_settlement",
                "category": "Legal",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Joint holder cust_joint_005 (Kenji Tanaka) removed from account acc_chk_2001. Final settlement of 1000.00 CAD transferred."
            }),
        ],
        outputs=[
            "Identities of both Elena Popescu and Kenji Tanaka were successfully verified.",
            "Kenji Tanaka was removed as a joint holder from account acc_chk_2001.",
            "The account balance was confirmed.",
            "A final settlement of 1000.00 CAD was transferred to Kenji Tanaka and a high-priority legal ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_096",
        instruction=(
            "Handle the complete termination of customer Kenji Tanaka's engagement with the bank (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "Initially, obtain his profile and confirm his identity using his passport 'lF146011'. "
            "Since the customer has already settled his credit card, place a request to shut down the credit card account 'acc_crd_1003'. "
            "Subsequently, he intends to consolidate his funds before the final closure. "
            "Retrieve the balance of his checking account 'acc_chk_1001' ($5230.50) and his savings account 'acc_sav_1002'. "
            "Transfer the total amount of $5230.50 from his checking account to his savings account. "
            "After consolidating the funds, lodge a request to close the now-empty checking account 'acc_chk_1001'. "
            "Prior to the last step, cancel all of his scheduled payments to prevent future transactions; cancel 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d' and 'sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w2'. "
            "Finally, enter a ticket with ID 'ticket_user_096_final_closure' under category 'Account Closure', priority 'Critical', via 'Internal System', outlining: 'Full relationship closure initiated. "
            "Credit and checking accounts closed. "
            "All funds consolidated into savings account acc_sav_1002. "
            "Customer requests an agent to call for final closure and disbursement of remaining funds.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="CloseAccountRequest", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="TransferFundsWithLimitCheck", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_sav_1002", "amount": 5230.50}),
            Action(name="CloseAccountRequest", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="CancelScheduledPayment", kwargs={"payment_id": "sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w2"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_096_final_closure",
                "category": "Account Closure",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Full relationship closure initiated. Credit and checking accounts closed. All funds consolidated into savings account acc_sav_1002. Customer requests an agent to call for final closure and disbursement of remaining funds."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka and his credit card account was submitted for closure.",
            "Funds from his checking account were consolidated into his savings account.",
            "The now-empty checking account was submitted for closure.",
            "All scheduled payments were canceled and a critical ticket was logged to complete the final steps of closing the relationship.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_097",
        instruction=(
            "Coordinate assistance for customer Elena Popescu (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef) with integrating her spouse into her checking account 'acc_chk_2001' and revising her beneficiaries. "
            "His spouse is Zoltan Nagy (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "Start by acquiring Elena Popescu's profile and verifying her identity with her national ID 'jd195515'. "
            "Next, include Zoltan Nagy as a joint account holder. "
            "Once added, authenticate his identity using his national ID 'pI260068'. "
            "Subsequently, revise Jane's beneficiary list. "
            "Display his current beneficiaries and remove the existing one, Kenji Tanaka (ID: bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f). "
            "Record his new spouse, Zoltan Nagy, as the new primary beneficiary with ID 'bene_user_097_d_chen', using his account number '6666' at 'City General Bank' (routing: 'N/A') in the 'USA'. "
            "Finally, register a ticket with ID 'ticket_user_097_spouse_add' under category 'Account Management', priority 'Medium', via 'Web Portal', detailing: 'Added spouse Zoltan Nagy as joint holder and primary beneficiary to account acc_chk_2001. "
            "Removed previous beneficiary.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="AddJointAccountHolder", kwargs={"account_id": "acc_chk_2001", "holder_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "pI260068"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_user_097_d_chen",
                "beneficiary_name": "Zoltan Nagy",
                "country": "USA",
                "bank_details": {"account_number": "6666", "bank_name": "City General Bank", "routing_info": "N/A"}
            }),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_097_spouse_add",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Added spouse Zoltan Nagy as joint holder and primary beneficiary to account acc_chk_2001. Removed previous beneficiary."
            }),
        ],
        outputs=[
            "Identity of primary account holder Elena Popescu was verified.",
            "Zoltan Nagy was added as a joint account holder and his identity was also verified.",
            "The previous beneficiary, Kenji Tanaka, was removed.",
            "The new spouse, Zoltan Nagy, was registered as the new primary beneficiary and a ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_098",
        instruction=(
            "Conduct a full security lockdown and investigation for customer Kenji Tanaka (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) following significant fraud detection. "
            "Start by retrieving his profile and confirming his identity with his passport 'lF146011'. "
            "Instantly freeze all his three accounts: checking 'acc_chk_1001', savings 'acc_sav_1002', and credit card 'acc_crd_1003', citing 'Major fraud alert; all accounts locked pending investigation.' Once secured, extract the complete transaction history for both the checking and credit card accounts for the last 30 days for scrutiny. "
            "His contact information is believed to be compromised. "
            "Update his details to a new secure email 'j.doe.secure.recovery@example.com' and a new secure phone '123-555-0000'. "
            "Lastly, file a support ticket with ID 'ticket_user_098_lockdown' to the 'Security' category marked 'Critical' priority via 'Internal System', explaining: 'Full account lockdown for Kenji Tanaka due to major fraud alert. "
            "All accounts frozen, transaction history pulled for investigation, and contact info secured.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_chk_1001", "alert_reason": "Major fraud alert; all accounts locked pending investigation."}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_sav_1002", "alert_reason": "Major fraud alert; all accounts locked pending investigation."}),
            Action(name="FreezeAccountOnFraudAlert", kwargs={"account_id": "acc_crd_1003", "alert_reason": "Major fraud alert; all accounts locked pending investigation."}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_chk_1001", "days": 30}),
            Action(name="GetAccountTransactionHistory", kwargs={"account_id": "acc_crd_1003", "days": 30}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "new_email": "j.doe.secure.recovery@example.com", "new_phone": "123-555-0000"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_098_lockdown",
                "category": "Security",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Full account lockdown for Kenji Tanaka due to major fraud alert. All accounts frozen, transaction history pulled for investigation, and contact info secured."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "All three of the customer's accounts have been frozen due to a major fraud alert.",
            "Transaction histories for the checking and credit card accounts have been retrieved for investigation.",
            "The customer's contact information has been updated and a critical security ticket has been logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_099",
        instruction=(
            "Facilitate a straightforward profile update and loan status examination for customer Zoltan Nagy (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11). "
            "Start by accessing his profile and verifying his identity through his passport 'Se620000'. "
            "Update his email to 'liam.oconnor.profile@example.ie' and his contact number to '+353 87 555 6666'. "
            "Subsequently, summarize the status of his loan applications to provide him with progress on his active loan. "
            "Then, retrieve the current balance of his primary checking account 'acc_chk_12001'. "
            "In conclusion, raise a low-priority support ticket with ID 'ticket_user_099_profile_update' under category 'General Inquiry' via 'Web Portal', summarizing: 'Customer contact information updated. "
            "Loan and account status provided as requested.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "id_document": "Se620000"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "new_email": "liam.oconnor.profile@example.ie", "new_phone": "+353 87 555 6666"}),
            Action(name="SummarizeLoanApplicationsByStatus", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="GetAccountBalance", kwargs={"account_id": "acc_chk_12001"}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "ticket_id": "ticket_user_099_profile_update",
                "category": "General Inquiry",
                "priority": "Low",
                "channel": "Web Portal",
                "request_details": "Customer contact information updated. Loan and account status provided as requested."
            }),
        ],
        outputs=[
            "Identity verified for Zoltan Nagy.",
            "The customer's email and phone number were successfully updated.",
            "A summary of his loan status was retrieved.",
            "His checking account balance was checked and a ticket was logged to confirm the updates.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_100",
        instruction=(
            "Support customer Chloe Dubois (ID: d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1) in reconfiguring his international beneficiaries and account settings. "
            "Begin by retrieving his profile and confirming his identity using his driver's license 'Kt516858'. "
            "He wishes to overhaul his beneficiary list. "
            "Enumerate his current beneficiaries, then remove the existing one: 'Klaus Schmidt' (ID: bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a). "
            "Next, register two new international beneficiaries. "
            "The first is in France, identified as 'bene_user_100_fr' for 'French Connection Supplies', with account IBAN 'FR7630002005500000157845Z25' at 'Societe Generale' (BIC: 'SOGEFRPP'). "
            "The second is in the UK, identified as 'bene_user_100_uk' for 'British Imports Co.', with account number 'GB29NWBK60161331926819' at 'NatWest' (BIC: 'NWBKGB2L'). "
            "After updating the beneficiaries, edit his account settings to establish his language as 'de-DE' and ensure notifications are activated. "
            "Conclude by filing a ticket with ID 'ticket_user_100_bene_reconfig' under category 'Beneficiary Management', priority 'Medium', via 'Web Portal', detailing: 'Beneficiary list reconfigured. "
            "Klaus Schmidt removed. "
            "French and UK beneficiaries added. "
            "Preferences updated.'."
        ),
        actions=[
            Action(name="GetCustomerProfile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="VerifyCustomerIdentity", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "id_document": "Kt516858"}),
            Action(name="ListLinkedBeneficiaries", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="DeleteExistingBeneficiary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "beneficiary_id": "bene_user_100_fr",
                "beneficiary_name": "French Connection Supplies",
                "country": "France",
                "bank_details": {"account_number": "FR7630002005500000157845Z25", "bank_name": "Societe Generale", "routing_info": "SOGEFRPP"}
            }),
            Action(name="RegisterNewBeneficiary", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "beneficiary_id": "bene_user_100_uk",
                "beneficiary_name": "British Imports Co.",
                "country": "United Kingdom",
                "bank_details": {"account_number": "GB29NWBK60161331926819", "bank_name": "NatWest", "routing_info": "NWBKGB2L"}
            }),
            Action(name="UpdateAccountPreferences", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "preferences": {"language": "de-DE", "notifications": True}}),
            Action(name="SubmitSupportTicket", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "ticket_id": "ticket_user_100_bene_reconfig",
                "category": "Beneficiary Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Beneficiary list reconfigured. Klaus Schmidt removed. French and UK beneficiaries added. Preferences updated."
            }),
        ],
        outputs=[
            "Identity verified for Chloe Dubois.",
            "His beneficiary list was reconfigured: one beneficiary was removed.",
            "Two new international beneficiaries in France and the UK were successfully registered.",
            "Account preferences were updated and a ticket was logged to document the changes.",
        ],
    )
]
