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
            actions=[Action(name="get_customer_profile", kwargs={...}), ...],
            outputs=[...]
        ),
        ...
    ]
"""

from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="user_001",
        instruction=(
            "You’re assisting Oliver Williams (customer ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) with a joint account setup. "
            "Start by verifying his identity using passport 'passport_10000001'. "
            "Update his contact details to email 'oliver.williams@example.com' and phone '+1-202-555-0143'. "
            "Enable notifications. Then check the balance and linked beneficiaries on account 'acc_chk_1001'. "
            "Finally, submit a medium-priority support ticket via Web under category 'Joint Account', using ticket ID 'tkt_d6e5f4a3-f4a3-b2c1-d0e9-f8g7h6i5j4k3', "
            "and include the note: 'Setup joint account for customer_id=c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e on account acc_chk_1001'."
        ),
        actions=[
            Action(
                name="verify_customer_identity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "passport_10000001",
                },
            ),
            Action(
                name="update_customer_email",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "new_email": "oliver.williams@example.com",
                    "new_phone": "+1-202-555-0143",
                },
            ),
            Action(
                name="update_account_preferences",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "notifications_enabled": True,
                },
            ),
            Action(
                name="get_account_balance",
                kwargs={"account_id": "acc_chk_1001"},
            ),
            Action(
                name="list_linked_beneficiaries",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            Action(
                name="submit_support_ticket",
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
            "Joint account setup initiated for Oliver Williams: identity confirmed, preferences saved, and support ticket tkt_d6e5f4a3-f4a3-b2c1-d0e9-f8g7h6i5j4k3 submitted."
        ],
    ),
    Task(
        annotator="0",
        user_id="user_002",
        instruction=(
            "Assist Oliver Williams (customer ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) in performing a January 2023 financial review. "
            "Start by verifying his identity using the document 'passport_10000002'. "
            "Analyze spending activity on account 'acc_chk_1001', flag any suspicious activity, "
            "then update his email to 'oliver.williams@example.com' and phone to '+44 7700 900125', "
            "enable notifications and file a support ticket on the Web Portal with category 'Security', "
            "priority 'High', and request to escalate issues found on account 'acc_chk_1001'. "
            "The ticket should receive the ID 'ticket_static_002' to ensure traceability."
        ),
        actions=[
            Action(
                name="verify_customer_identity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "passport_10000002",
                },
            ),
            Action(
                name="aggregate_monthly_expenses",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "month": "2023-01",
                },
            ),
            Action(
                name="detect_suspicious_activity_and_alert",
                kwargs={
                    "account_id": "acc_chk_1001",
                },
            ),
            Action(
                name="update_account_preferences",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "preferences": {
                        "notifications": True
                    },
                },
            ),
            Action(
                name="update_customer_email",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "new_email": "oliver.williams@example.com",
                    "new_phone": "+44 7700 900125",
                },
            ),
            Action(
                name="submit_support_ticket",
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
            "January 2023 financial review completed for Oliver Williams: expenses analyzed, account flagged for security, preferences updated, and support ticket 'ticket_static_002' submitted successfully."
        ],
    ),
    Task(
        annotator="0",
        user_id="user_003",
        instruction=(
            "You're reviewing John Doe’s (customer ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) support interactions. "
            "Start by verifying his identity using his passport 'lF146011'. "
            "Check his profile, enable notifications, set language to 'en-US', "
            "and update his email to 'john.doe@example.com' and phone to '+1-202-555-0199'. "
            "Then list his current beneficiaries and delete the existing record for Jane Smith (ID: bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d). "
            "Immediately re-register Jane Smith as a 'Spouse' linked to account '9876543210' at City National Bank (routing 122000661, USA), using the beneficiary ID 'bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d'. "
            "Finally, submit a support ticket with ID 'ticket_003' to the 'Escalation' category with 'High' priority via 'Internal System', "
            "using the request details: 'Customer profile, preferences, and beneficiary list updated. Jane Smith re-registered as Spouse.'"
        ),
        actions=[
            Action(
                name="verify_customer_identity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "lF146011",
                },
            ),
            Action(
                name="get_customer_profile",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            ),
            Action(
                name="update_account_preferences",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "preferences": {
                        "notifications": True,
                        "language": "en-US"
                    },
                },
            ),
            Action(
                name="update_customer_email",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "new_email": "john.doe@example.com",
                    "new_phone": "+1-202-555-0199"
                },
            ),
            Action(
                name="list_linked_beneficiaries",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            ),
            Action(
                name="delete_existing_beneficiary",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d"
                },
            ),
            Action(
                name="register_new_beneficiary",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d",
                    "beneficiary_name": "Jane Smith",
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
                name="submit_support_ticket",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "category": "Escalation",
                    "priority": "High",
                    "channel": "Internal System",
                    "ticket_id": "ticket_003",
                    "request_details": "Customer profile, preferences, and beneficiary list updated. Jane Smith re-registered as Spouse."
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
            "For customer ID c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e, verify identity using document passport_10000004. "
            "Then review their account acc_sav_2001 activity and loan application statuses, "
            "download the February 2023 account statement for that account, "
            "and submit a high-priority support ticket ID ticket_004 under category 'Account Review' via Internal System, "
            "logging the following steps: IDENTITY_VERIFIED, ACCOUNT_ACTIVITY_REVIEWED, LOANS_CHECKED, STATEMENT_DOWNLOADED."
        ),
        actions=[
            Action(
                name="verify_customer_identity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "passport_10000004"
                },
            ),
            Action(
                name="get_account_transaction_history",
                kwargs={
                    "account_id": "acc_sav_2001"
                },
            ),
            Action(
                name="summarize_loan_applications_by_status",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            ),
            Action(
                name="download_statement_by_date",
                kwargs={
                    "account_id": "acc_sav_2001",
                    "month": "2023-02"
                },
            ),
            Action(
                name="submit_support_ticket",
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
            "As a compliance officer, conduct a full audit for customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e): "
            "verify his identity using document passport_10000005, "
            "update contact email to john.doe@example.com and phone to +55 21 98765-4321, "
            "enable notifications, "
            "review transactions and monthly expenses on account acc_chk_1001 for the period January to March 2023, "
            "download monthly statements for those months, "
            "check for suspicious activity, "
            "and submit a complete audit log to support with category Compliance, priority High, via Internal System."
        ),
        actions=[
            Action(
                name="verify_customer_identity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "passport_10000005"
                }
            ),
            Action(
                name="update_customer_email",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "new_email": "john.doe@example.com",
                    "new_phone": "+55 21 98765-4321"
                }
            ),
            Action(
                name="update_account_preferences",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "preferences": {
                        "notifications": True
                    }
                }
            ),
            Action(
                name="get_account_transaction_history",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "start_date": "2023-01-01",
                    "end_date": "2023-03-31"
                }
            ),
            Action(
                name="aggregate_monthly_expenses",
                kwargs={"account_id": "acc_chk_1001", "month": "2023-01"}
            ),
            Action(
                name="aggregate_monthly_expenses",
                kwargs={"account_id": "acc_chk_1001", "month": "2023-02"}
            ),
            Action(
                name="aggregate_monthly_expenses",
                kwargs={"account_id": "acc_chk_1001", "month": "2023-03"}
            ),
            Action(
                name="download_statement_by_date",
                kwargs={"account_id": "acc_chk_1001", "month": "2023-01"}
            ),
            Action(
                name="download_statement_by_date",
                kwargs={"account_id": "acc_chk_1001", "month": "2023-02"}
            ),
            Action(
                name="download_statement_by_date",
                kwargs={"account_id": "acc_chk_1001", "month": "2023-03"}
            ),
            Action(
                name="detect_suspicious_activity_and_alert",
                kwargs={"account_id": "acc_chk_1001"}
            ),
            Action(
                name="submit_support_ticket",
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
            "You are handling a security issue for customer ID a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4. "
            "First, verify their identity using document passport_10000006. "
            "Then freeze their account acc_chk_1001 due to fraud alert: 'Multiple failed login attempts'. "
            "Update the customer's contact email to secure.jane.doe@example.com and phone to +55 21 99876-5432. "
            "Finally, submit support ticket ticket_006 with category 'Security Alert', priority High, via Internal System, "
            "targeting the Customer entity, with operation SECURITY_ESCALATION_LOG, logging steps: IDENTITY_VERIFIED, ACCOUNT_FROZEN, CONTACT_UPDATED."
        ),
        actions=[
            Action(
                name="verify_customer_identity",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "id_document": "passport_10000006"
                }
            ),
            Action(
                name="freeze_account_on_fraud_alert",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "alert_reason": "Multiple failed login attempts"
                }
            ),
            Action(
                name="update_customer_email",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "new_email": "secure.jane.doe@example.com",
                    "new_phone": "+55 21 99876-5432"
                }
            ),
            Action(
                name="submit_support_ticket",
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
            "Assist customer ID f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9 with a joint account update on account acc_chk_2001: "
            "remove joint account holder cust_joint_005, "
            "review transactions between 2023-01-01 and 2023-03-31, "
            "register beneficiary Carlos Silva (ID ben_007_xyz123), Personal, Partner, account 5566778899 at Unity Bank (routing 110000000, USA), "
            "then submit support ticket ticket_007 with category 'Account Update', priority High, via Internal System, "
            "logging: JOINT_HOLDER_REMOVED, TRANSACTIONS_REVIEWED_Q1, BENEFICIARY_REGISTERED."
        ),
        actions=[
            Action(
                name="remove_joint_account_holder",
                kwargs={
                    "account_id": "acc_chk_2001",
                    "holder_id": "cust_joint_005"
                }
            ),
            Action(
                name="get_account_transaction_history",
                kwargs={
                    "account_id": "acc_chk_2001",
                    "start_date": "2023-01-01",
                    "end_date": "2023-03-31"
                }
            ),
            Action(
                name="register_new_beneficiary",
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
                name="submit_support_ticket",
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
            "Support customer ID a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4 with a financial health check on account acc_sav_5001: "
            "review transactions from January to March 2023, summarize January expenses, "
            "replace the beneficiary with ID bene_5e4f3a2b-1c9d-8e7f-6a5b-4c3d2e1f0a9b (Global ISP) by Jane Smith "
            "(Personal, Friend), account 9876543210 at City National Bank (routing 122000661, USA), "
            "download the March 2023 statement, and submit support ticket ID ticket_008 "
            "with category 'Financial Health Check', priority Medium, via Internal System, "
            "logging all steps completed as: TRANSACTION_REVIEW_JAN_TO_MAR, EXPENSES_SUMMARIZED_JAN, "
            "BENEFICIARY_REPLACED, MARCH_STATEMENT_DOWNLOADED."
        ),
        actions=[
            Action(
                name="get_account_transaction_history",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "start_date": "2023-01-01",
                    "end_date": "2023-03-31",
                },
            ),
            Action(
                name="aggregate_monthly_expenses",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "month": "2023-01",
                },
            ),
            Action(
                name="delete_existing_beneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_id": "bene_5e4f3a2b-1c9d-8e7f-6a5b-4c3d2e1f0a9b",
                },
            ),
            Action(
                name="register_new_beneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "Jane Smith",
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
                name="download_statement_by_date",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "month": "2023-03"
                },
            ),
            Action(
                name="submit_support_ticket",
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
            "beneficiary replaced with Jane Smith, March statement downloaded, and ticket ticket_008 submitted successfully."
        ],
    ),
    Task(
        annotator="0",
        user_id="user_009",
        instruction=(
            "Complete onboarding check for customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) on account acc_chk_1001. "
            "Start by verifying identity using his passport 'lF146011'. "
            "Then analyze January 2023 spending on the account and check for suspicious activity. "
            "Register beneficiary Carlos Silva (ID: ben_009_carlossilva), of type Personal and relationship Partner, "
            "with account number 5566778899 at Unity Bank (routing 110000000, USA). "
            "Finally, submit a high-priority support ticket (ID: ticket_009) via Internal System under category 'Onboarding', "
            "targeting the customer and including the summary ONBOARDING_PASS."
        ),
        actions=[
            Action(
                name="verify_customer_identity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "lF146011",
                },
            ),
            Action(
                name="aggregate_monthly_expenses",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "month": "2023-01",
                },
            ),
            Action(
                name="detect_suspicious_activity_and_alert",
                kwargs={
                    "account_id": "acc_chk_1001"
                },
            ),
            Action(
                name="register_new_beneficiary",
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
                name="submit_support_ticket",
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
            "Review the balance of account acc_sav_2002 for savings evaluation, "
            "then escalate a medium-priority support request via Internal System to increase overdraft protection on "
            "account acc_chk_2001 using justification code OD_PROTECT_SAVINGS_LINKED, "
            "and list all beneficiaries linked to the customer a1b2c3d4-e5f6-7890-1234-567890abcdef."
        ),
        actions=[
            Action(
                name="get_account_balance",
                kwargs={"account_id": "acc_sav_2002"},
            ),
            Action(
                name="submit_support_ticket",
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
                name="list_linked_beneficiaries",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
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
            "Authenticate customer John Doe using his ID document ending in 6789 for customer ID "
            "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e. Then, retrieve his profile and the balance of his checking account acc_chk_1001. "
            "Submit a medium-priority support ticket via the Web Portal in the 'Account Issues' category with the request: "
            "'Customer reports incorrect charges in transaction history', and assign it the ID tkt_d6e5f4a3-f4a3-b2c1-d0e9-f8g7h6i5j4k3. "
            "Next, classify this same ticket (tkt_d6e5f4a3-f4a3-b2c1-d0e9-f8g7h6i5j4k3) using the same message. Finally, review the customer's ticket history "
            "and update their account preferences to receive alerts via Email."
        ),
        actions=[
            Action(
                name='verify_customer_identity',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'id_document': '6789'
                }
            ),
            Action(
                name='get_customer_profile',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e'
                }
            ),
            Action(
                name='get_account_balance',
                kwargs={
                    'account_id': 'acc_chk_1001'
                }
            ),
            Action(
                name='submit_support_ticket',
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
                name='auto_classify_support_ticket_priority',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'ticket_id': 'tkt_d6e5f4a3-f4a3-b2c1-d0e9-f8g7h6i5j4k3',
                    'message': 'Customer reports incorrect charges in transaction history.'
                }
            ),
            Action(
                name='review_ticket_history',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e'
                }
            ),
            Action(
                name='update_account_preferences',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'preferences': {
                        'communication_channel': 'Email'
                    }
                }
            )
        ],
        outputs=[
            'Identity verified for John Doe using ID ending in 6789.',
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
            "Verify the identity of customer John Doe using ID document ending in 6789 for customer ID "
            "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e. Once verified, file a high-priority support ticket via the Mobile App "
            "under the category 'Card Services', reporting a delay in receiving his debit card after account approval. "
            "Use ticket ID ticket_002 for this submission. Then, confirm that his checking account acc_chk_1001 is active "
            "by retrieving its balance. Once the account is verified as operational, download the September 2023 statement "
            "for that account."
        ),
        actions=[
            Action(
                name="verify_customer_identity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "6789"
                }
            ),
            Action(
                name="submit_support_ticket",
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
                name="get_account_balance",
                kwargs={
                    "account_id": "acc_chk_1001"
                }
            ),
            Action(
                name="download_statement_by_date",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "month": "2023-09"
                }
            )
        ],
        outputs=[
            "Identity verified for John Doe using ID ending in 6789.",
            "Support ticket ticket_002 filed under Card Services with high priority.",
            "Balance confirmed for account acc_chk_1001.",
            "September 2023 statement downloaded for acc_chk_1001."
        ]
    ),
    Task(
        annotator='0',
        user_id='user_013',
        instruction=(
            "Authenticate customer John Doe using customer ID c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e and ID document ending in 6789. "
            "Then retrieve the full transaction history of his checking account acc_chk_1001. "
            "Generate a breakdown of his monthly expenses for September 2023. "
            "Finally, update his notification preferences to receive alerts via Email."
        ),
        actions=[
            Action(
                name='verify_customer_identity',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'id_document': '6789'
                }
            ),
            Action(
                name='get_account_transaction_history',
                kwargs={
                    'account_id': 'acc_chk_1001'
                }
            ),
            Action(
                name='aggregate_monthly_expenses',
                kwargs={
                    'account_id': 'acc_chk_1001',
                    'month': '2023-09'
                }
            ),
            Action(
                name='update_account_preferences',
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
            "Authenticate customer John Doe using his ID document ending in 6789 for customer ID "
            "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e. Then retrieve his full profile and check the balance of "
            "his checking account acc_chk_1001. Download the September 2023 statement and review all transactions from that month. "
            "Generate a summary of monthly expenses for the same account and period. "
            "After confirming the account is active and linked, update John’s account preferences to receive alerts via SMS. "
            "Finally, unlock his account using the same ID document and the security code '123456'."
        ),
        actions=[
            Action(
                name='verify_customer_identity',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'id_document': '6789'
                }
            ),
            Action(
                name='get_customer_profile',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e'
                }
            ),
            Action(
                name='get_account_balance',
                kwargs={
                    'account_id': 'acc_chk_1001'
                }
            ),
            Action(
                name='download_statement_by_date',
                kwargs={
                    'account_id': 'acc_chk_1001',
                    'month': '2023-09'
                }
            ),
            Action(
                name='get_account_transaction_history',
                kwargs={
                    'account_id': 'acc_chk_1001'
                }
            ),
            Action(
                name='aggregate_monthly_expenses',
                kwargs={
                    'account_id': 'acc_chk_1001',
                    'month': '2023-09'
                }
            ),
            Action(
                name='update_account_preferences',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'preferences': {
                        'communication_channel': 'SMS'
                    }
                }
            ),
            Action(
                name='unlock_account_by_security_check',
                kwargs={
                    'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                    'id_document': '6789',
                    'security_code': '123456'
                }
            )
        ],
        outputs=[
            'Identity verified for John Doe using ID ending in 6789.',
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
            "Guide customer John Doe through an advanced banking workflow. "
            "Begin by verifying his identity using customer ID c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e and ID document ending in 6789. "
            "Then retrieve the balance and transaction history of his checking account acc_chk_1001, and aggregate his expenses for September 2023. "
            "Submit a high-priority support ticket via Mobile App in the 'Card Services' category, using the message: 'Lost debit card, requesting new one', "
            "and assign it the ID ticket_555abcde. "
            "After that, review his support ticket history, update his preferences to receive alerts via Email, "
            "download his statement for September 2023, and finally unlock his account using the same ID and the security code 123456."
        ),
        actions=[
            Action(name='verify_customer_identity', kwargs={
                'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                'id_document': '6789'
            }),
            Action(name='get_account_balance', kwargs={
                'account_id': 'acc_chk_1001'
            }),
            Action(name='get_account_transaction_history', kwargs={
                'account_id': 'acc_chk_1001'
            }),
            Action(name='aggregate_monthly_expenses', kwargs={
                'account_id': 'acc_chk_1001',
                'month': '2023-09'
            }),
            Action(name='submit_support_ticket', kwargs={
                'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                'category': 'Card Services',
                'priority': 'High',
                'channel': 'Mobile App',
                'request_details': 'Lost debit card, requesting new one',
                'ticket_id': 'ticket_555abcde'
            }),
            Action(name='review_ticket_history', kwargs={
                'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e'
            }),
            Action(name='update_account_preferences', kwargs={
                'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                'preferences': {
                    'communication_channel': 'Email'
                }
            }),
            Action(name='download_statement_by_date', kwargs={
                'account_id': 'acc_chk_1001',
                'month': '2023-09'
            }),
            Action(name='unlock_account_by_security_check', kwargs={
                'customer_id': 'c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e',
                'id_document': '6789',
                'security_code': '123456'
            })
        ],
        outputs=[
            'Identity verified for customer John Doe.',
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
            "You are tasked with auditing financial operations for customer Jane Smith "
            "(Customer ID: a1b2c3d4-e5f6-7890-1234-567890abcdef), holder of checking account acc_chk_2001. "
            "Begin by retrieving her profile and verifying her identity using national ID 'jd195515'. "
            "Next, review all transactions from acc_chk_2001 and check for any suspicious activity. "
            "After that, schedule a payment of $150.00 USD from acc_chk_2001 to account 9876543210 on 2025-08-01. "
            "Then, submit a support ticket with ID 'ticket_user_016_jane_recurring_gym' under category 'Recurring Payment', "
            "priority 'Medium', via 'Web Portal', targeting entity 'Account', and operation 'VERIFY_RECURRING'. "
            "Include the following note: 'Recurring payment of $150.00 USD to 9876543210 for Gym Membership verified from account acc_chk_2001'. "
            "Finally, review the full ticket history for Jane Smith. Current date is 2025-07-24."
        ),
        actions=[
            Action(
                name="get_customer_profile",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
            ),
            Action(
                name="verify_customer_identity",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "id_document": "jd195515",
                },
            ),
            Action(
                name="get_account_transaction_history",
                kwargs={"account_id": "acc_chk_2001"},
            ),
            Action(
                name="detect_suspicious_activity_and_alert",
                kwargs={"account_id": "acc_chk_2001"},
            ),
            Action(
                name="schedule_payment_with_validation",
                kwargs={
                    "from_account": "acc_chk_2001",
                    "to_account": "9876543210",
                    "amount": 150.00,
                    "currency": "USD",
                    "date": "2025-08-01"
                },
            ),
            Action(
                name="submit_support_ticket",
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
                name="review_ticket_history",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
            ),
        ],
        outputs=[
            "Customer profile for Jane Smith retrieved.",
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
            "You need to assist John Doe (customer ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), the customer linked to account acc_chk_1001, "
            "in updating his list of beneficiaries. Start by retrieving his full profile. Then verify his identity using his passport 'lF146011'. "
            "List all currently linked beneficiaries and remove the one named 'Anytown Utility Services'. "
            "Register a new beneficiary using the ID 'bene_user_017_clara_james' for 'Clara James' with account number '1234567890123456' at 'Federal Bank' "
            "(routing: '012345678') in the 'USA', with the relationship 'Sister'. After that, download his latest statement for July 2025. "
            "Then, submit a support ticket using ID 'ticket_user_017_bene_audit' with category 'Account Management' and priority 'Medium' via 'Web Portal'. "
            "This ticket must target the 'Beneficiary' entity for an 'AUDIT' operation and include the note: 'Validate beneficiary update request and confirm legitimacy'. "
            "Finally, review his full ticket history to ensure the process was properly recorded."
        ),
        actions=[
            Action(
                name="get_customer_profile",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            Action(
                name="verify_customer_identity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "lF146011",
                },
            ),
            Action(
                name="list_linked_beneficiaries",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            Action(
                name="delete_existing_beneficiary",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e",
                },
            ),
            Action(
                name="register_new_beneficiary",
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
                name="download_statement_by_date",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "month": "2025-07",
                },
            ),
            Action(
                name="submit_support_ticket",
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
                name="review_ticket_history",
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
            "As a financial analyst, you are required to perform a full audit for the customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), "
            "linked to account acc_sav_1002. Begin by retrieving his profile and verifying his identity using his passport 'lF146011'. "
            "Aggregate the monthly expenses for this account for July 2025 and download the corresponding monthly statement. "
            "Then, submit a support ticket using ID 'ticket_user_018_audit' with category 'Compliance', priority 'High', via 'Internal System', "
            "and with the request details: 'Complete audit trail for monthly expenses and compliance log for July 2025.' "
            "Finally, review the entire ticket history for quality assurance."
        ),
        actions=[
            Action(
                name="get_customer_profile",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            Action(
                name="verify_customer_identity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "lF146011",
                },
            ),
            Action(
                name="aggregate_monthly_expenses",
                kwargs={
                    "account_id": "acc_sav_1002",
                    "month": "2025-07",
                },
            ),
            Action(
                name="download_statement_by_date",
                kwargs={
                    "account_id": "acc_sav_1002",
                    "month": "2025-07",
                },
            ),
            Action(
                name="submit_support_ticket",
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
                name="review_ticket_history",
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
            "You're handling a time-sensitive transfer operation for the customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), linked to account acc_chk_1001. "
            "First, retrieve his profile and verify his identity using his passport 'lF146011'. "
            "Then, list all linked beneficiaries and select the one labeled 'Anytown Utility Services'. "
            "Transfer $300.00 from account acc_chk_1001 to this beneficiary's account '5555666677'. "
            "Immediately after, schedule another payment of the same amount for the date 2025-08-01. "
            "Finally, submit a support ticket using ID 'ticket_user_019_payment_confirm' with category 'Payment', priority 'Medium' via 'Web Portal' "
            "and using the request details: 'Confirmation of immediate transfer and scheduled payment to Anytown Utility Services.'"
        ),
        actions=[
            Action(
                name="get_customer_profile",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            Action(
                name="verify_customer_identity",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "id_document": "lF146011",
                },
            ),
            Action(
                name="list_linked_beneficiaries",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            Action(
                name="transfer_funds_with_limit_check",
                kwargs={
                    "from_account": "acc_chk_1001",
                    "to_account": "5555666677",
                    "amount": 300.00,
                },
            ),
            Action(
                name="schedule_payment_with_validation",
                kwargs={
                    "from_account": "acc_chk_1001",
                    "to_account": "5555666677",
                    "amount": 300.00,
                    "currency": "USD",
                    "date": "2025-08-01",
                },
            ),
            Action(
                name="submit_support_ticket",
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
            "The customer Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef), associated with account acc_chk_2001, needs to update her list of beneficiaries. "
            "Start by retrieving her profile and verifying her identity using her national ID 'jd195515'. "
            "Then, list her current beneficiaries and remove the one named 'John Doe'. "
            "Next, register a new beneficiary using the ID 'bene_user_020_clara_james' for 'Clara James' with account number '5566778899' at 'Unity Bank' "
            "(routing: '110000000') in the 'USA'. Download her latest statement for July 2025. "
            "Finally, submit a support ticket using ID 'ticket_user_020_bene_add' with category 'Account Update', priority 'Medium', via 'Web Portal', "
            "and the request details: 'Please confirm that the beneficiary John Doe has been removed and Clara James has been added for account acc_chk_2001.'"
        ),
        actions=[
            Action(
                name="get_customer_profile",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
            ),
            Action(
                name="verify_customer_identity",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "id_document": "jd195515",
                },
            ),
            Action(
                name="list_linked_beneficiaries",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
            ),
            Action(
                name="delete_existing_beneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f",
                },
            ),
            Action(
                name="register_new_beneficiary",
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
                name="download_statement_by_date",
                kwargs={
                    "account_id": "acc_chk_2001",
                    "month": "2025-07",
                },
            ),
            Action(
                name="submit_support_ticket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "ticket_id": "ticket_user_020_bene_add",
                    "category": "Account Update",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "request_details": "Please confirm that the beneficiary John Doe has been removed and Clara James has been added for account acc_chk_2001.",
                },
            ),
        ],
        outputs=[
            "Beneficiary 'John Doe' successfully removed.",
            "New beneficiary 'Clara James' registered with account 5566778899.",
            "July 2025 statement downloaded for acc_chk_2001.",
            "Support ticket logged for beneficiary update verification.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_021",
        instruction=(
            "Execute a high-priority fraud response protocol for customer Hans Müller (ID: d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). "
            "Current date is 2025-07-24. Start by retrieving his profile and verifying his identity using his driver's license 'Kt516858'. "
            "Immediately run a check for suspicious activity on his checking account 'acc_chk_8001' and then freeze the account with the reason 'Unauthorized access reported by customer'. "
            "Update his contact information to the new email 'h.muller.secure@example.de' and new phone '+49 171 7654321'. "
            "Next, create a new, secure checking account for him of type 'Checking', currency 'EUR', and with an initial limit of 0.0. "
            "Finally, submit a support ticket with ID 'ticket_user_021_fraud_response' under category 'Security', priority 'High', via 'Internal System', "
            "with the request details: 'Fraud protocol executed for customer d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1. Old account frozen and new secure account created. Customer must be contacted for next steps.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "id_document": "Kt516858"}),
            Action(name="detect_suspicious_activity_and_alert", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_chk_8001", "alert_reason": "Unauthorized access reported by customer"}),
            Action(name="update_customer_email", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "new_email": "h.muller.secure@example.de", "new_phone": "+49 171 7654321"}),
            Action(name="create_customer_account", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "account_type": "Checking", "currency": "EUR", "initial_limit": 0.0}),
            Action(name="submit_support_ticket", kwargs={
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
            "Assist customer Liam O'Connor (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11) with a new loan application. "
            "Current date is 2025-07-24. First, get his profile and verify his identity using his passport 'Se620000'. "
            "Review his transaction history on his checking account 'acc_chk_12001' for the last 90 days to assess cash flow. "
            "Check his existing loan history, then submit a new application for a personal loan of 5000 EUR for the purpose 'Home Improvement'. "
            "Next, register a new beneficiary using the ID 'bene_user_022_dublin_reno' for 'Dublin Renovations' with account number 'IE29AIBK93118212345678' at 'AIB' (routing: 'AIBKIE2D') in 'Ireland'. "
            "Then, schedule a one-time payment of 250 EUR to this new beneficiary's account for an initial consultation, with the payment date set for '2025-08-01'. "
            "Finally, submit a support ticket with ID 'ticket_user_022_loan_app' under category 'Loan Application', priority 'Medium', via 'Web Portal', "
            "with the request details 'New personal loan application submitted for Home Improvement. Consultation payment scheduled to contractor.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "id_document": "Se620000"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_12001", "days": 90}),
            Action(name="summarize_loan_applications_by_status", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="apply_for_loan_with_check", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "amount": 5000.0, "purpose": "Home Improvement"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "beneficiary_id": "bene_user_022_dublin_reno",
                "beneficiary_name": "Dublin Renovations",
                "country": "Ireland",
                "bank_details": {"account_number": "IE29AIBK93118212345678", "bank_name": "AIB", "routing_info": "AIBKIE2D"}
            }),
            Action(name="schedule_payment_with_validation", kwargs={
                "from_account": "acc_chk_12001",
                "to_account": "IE29AIBK93118212345678",
                "amount": 250.0,
                "currency": "EUR",
                "date": "2025-08-01"
            }),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "ticket_id": "ticket_user_022_loan_app",
                "category": "Loan Application",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "New personal loan application submitted for Home Improvement. Consultation payment scheduled to contractor."
            }),
        ],
        outputs=[
            "Identity of Liam O'Connor verified and financial history reviewed.",
            "New loan application for 5000 EUR submitted for 'Home Improvement'.",
            "New beneficiary 'Dublin Renovations' registered and consultation payment scheduled.",
            "Support ticket logged for the loan application.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_023",
        instruction=(
            "Perform a complex account management and quarterly audit for customer Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef) on her account acc_chk_2001. "
            "Start by getting her profile and verifying her identity with her national ID 'jd195515'. "
            "Add David Chen (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) as a new joint account holder. "
            "Next, list all her beneficiaries and delete the one named 'John Doe' (ID: bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f). "
            "Then, register a new beneficiary using ID 'bene_user_023_metro_power' for 'Metropolis Power & Light' with account number '9988776655' at 'First National Bank of Metropolis' (routing: '021200339') in the 'USA'. "
            "After managing the beneficiaries, perform a Q2 2023 financial audit on account acc_chk_2001: aggregate monthly expenses for April, May, and June 2023. "
            "Finally, submit a support ticket with ID 'ticket_user_023_q2_audit' under category 'Audit', priority 'Medium', via 'Internal System', "
            "with the request details: 'Q2 2023 audit and account holder update complete for account acc_chk_2001.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="add_joint_account_holder", kwargs={"account_id": "acc_chk_2001", "holder_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_user_023_metro_power",
                "beneficiary_name": "Metropolis Power & Light",
                "country": "USA",
                "bank_details": {"account_number": "9988776655", "bank_name": "First National Bank of Metropolis", "routing_info": "021200339"}
            }),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_2001", "month": "2023-04"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_2001", "month": "2023-05"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_2001", "month": "2023-06"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_023_q2_audit",
                "category": "Audit",
                "priority": "Medium",
                "channel": "Internal System",
                "request_details": "Q2 2023 audit and account holder update complete for account acc_chk_2001."
            }),
        ],
        outputs=[
            "Identity verified for Jane Smith and David Chen added as joint account holder.",
            "Beneficiary 'John Doe' removed and 'Metropolis Power & Light' added.",
            "Q2 2023 financial audit completed: expenses aggregated for April, May, and June.",
            "An audit ticket was logged to document the account updates.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_024",
        instruction=(
            "Conduct a simple financial review for customer Chloe Dubois (ID: e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2). "
            "First, get her profile and verify her identity using her driver's license 'im665671'. "
            "Then, check the current balances of her checking account 'acc_chk_9001' and her credit card 'acc_crd_9002'. "
            "Retrieve the transaction history for her checking account for the last 60 days. "
            "Aggregate her monthly expenses for October 2023 on the same checking account and download the statement for that month. "
            "Finally, update her account preferences to set the language to 'fr-FR' and ensure notifications are enabled."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "id_document": "im665671"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_9001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_crd_9002"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_9001", "days": 60}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_9001", "month": "2023-10"}),
            Action(name="download_statement_by_date", kwargs={"account_id": "acc_chk_9001", "month": "2023-10"}),
            Action(name="update_account_preferences", kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "preferences": {"language": "fr-FR", "notifications": True}
            }),
        ],
        outputs=[
            "Identity verified for Chloe Dubois.",
            "Balances for checking account acc_chk_9001 and credit card acc_crd_9002 retrieved.",
            "Transaction history and October 2023 expenses for checking account reviewed and statement downloaded.",
            "Account preferences updated to French language and notifications enabled.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_025",
        instruction=(
            "Handle a support case for international customer Kenji Tanaka (ID: f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3). "
            "Current date is 2025-07-24. Begin by retrieving his profile and verifying his identity with his national ID 'nh464131'. "
            "He has reported a change of contact information; update his email to 'kenji.tanaka.new@example.jp' and phone to '+81 90-8765-4321'. "
            "Next, list his beneficiaries. He wants to cancel his bi-weekly scheduled payment with ID 'sp_d9b3a2c1-d6e5-f4a3-b2c1-d0e9f8g7h6i5'. "
            "After canceling, schedule a new one-time payment of 75000 JPY from his account 'acc_chk_10001' to his beneficiary Yuki Tanaka's account '87654321' for '2025-08-15'. "
            "Finally, submit a support ticket with ID 'ticket_user_025_payment_update' under category 'Scheduled Payment', priority 'Medium', via 'Email' with the request details: "
            "'Customer updated contact info, canceled recurring payment sp_d9b3a2c1-d6e5-f4a3-b2c1-d0e9f8g7h6i5, and scheduled a new one-time payment.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "id_document": "nh464131"}),
            Action(name="update_customer_email", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "new_email": "kenji.tanaka.new@example.jp", "new_phone": "+81 90-8765-4321"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_d9b3a2c1-d6e5-f4a3-b2c1-d0e9f8g7h6i5"}),
            Action(name="schedule_payment_with_validation", kwargs={
                "from_account": "acc_chk_10001",
                "to_account": "87654321",
                "amount": 75000.0,
                "currency": "JPY",
                "date": "2025-08-15"
            }),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "ticket_id": "ticket_user_025_payment_update",
                "category": "Scheduled Payment",
                "priority": "Medium",
                "channel": "Email",
                "request_details": "Customer updated contact info, canceled recurring payment sp_d9b3a2c1-d6e5-f4a3-b2c1-d0e9f8g7h6i5, and scheduled a new one-time payment."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka and contact information updated.",
            "Bi-weekly payment 'sp_d9b3a2c1-d6e5-f4a3-b2c1-d0e9f8g7h6i5' was successfully canceled.",
            "New one-time payment of 75000 JPY scheduled for 2025-08-15.",
            "Support ticket logged to confirm all changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_026",
        instruction=(
            "A compliance officer is conducting a detailed Q1 2023 financial audit for the international customer Fatima Al-Fassi (ID: c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6). "
            "Begin by fetching her profile and verifying her identity using her national ID 'IJ758739'. "
            "Next, manage her beneficiaries: list them and then remove her existing beneficiary 'Dubai International School' (ID: bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f). "
            "After removal, register a new beneficiary using the ID 'bene_user_026_art_gallery' for 'Global Art Gallery', with account IBAN 'FR7630006000011234567890189' at 'BNP Paribas' (BIC: 'BNPAFRPP') in 'France'. "
            "Then, for her checking account 'acc_chk_7001', aggregate monthly expenses and download the statements for January, February, and March of 2023. "
            "Conclude by running a suspicious activity check on the account and submitting a support ticket with ID 'ticket_user_026_q1_audit_log' under category 'Audit', priority 'High', via 'Internal System', "
            "with the request details: 'Q1 2023 compliance audit completed for customer. Beneficiary list updated and financial activity reviewed.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "id_document": "IJ758739"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "beneficiary_id": "bene_user_026_art_gallery",
                "beneficiary_name": "Global Art Gallery",
                "country": "France",
                "bank_details": {"account_number": "FR7630006000011234567890189", "bank_name": "BNP Paribas", "routing_info": "BNPAFRPP"}
            }),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_7001", "month": "2023-01"}),
            Action(name="download_statement_by_date", kwargs={"account_id": "acc_chk_7001", "month": "2023-01"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_7001", "month": "2023-02"}),
            Action(name="download_statement_by_date", kwargs={"account_id": "acc_chk_7001", "month": "2023-02"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_7001", "month": "2023-03"}),
            Action(name="download_statement_by_date", kwargs={"account_id": "acc_chk_7001", "month": "2023-03"}),
            Action(name="detect_suspicious_activity_and_alert", kwargs={"account_id": "acc_chk_7001"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "ticket_id": "ticket_user_026_q1_audit_log",
                "category": "Audit",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Q1 2023 compliance audit completed for customer. Beneficiary list updated and financial activity reviewed."
            }),
        ],
        outputs=[
            "Identity verified for Fatima Al-Fassi and beneficiary list updated.",
            "Q1 2023 expenses for account acc_chk_7001 aggregated for Jan, Feb, and Mar.",
            "Q1 2023 statements for account acc_chk_7001 downloaded for Jan, Feb, and Mar.",
            "Suspicious activity check completed and a high-priority audit ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_027",
        instruction=(
            "Handle a credit card dispute for Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef). "
            "First, get her profile and verify her identity using her national ID 'jd195515'. "
            "She is reporting an unauthorized transaction on her checking account 'acc_chk_2001'. "
            "Retrieve the transaction history for the last two years to locate the charge. "
            "Run a suspicious activity check on the account. "
            "Then, submit a support ticket with ID 'ticket_user_027_dispute' for a 'Dispute' with 'High' priority via the 'Mobile App'. "
            "The ticket must target the 'Transaction' entity with ID 'txn_0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d', for the operation 'DISPUTE_CHARGE', and include the parameter note: 'Customer reports this charge of 45.50 CAD to The Bistro is fraudulent and unauthorized.' "
            "Immediately after submitting the ticket, freeze the account 'acc_chk_2001' with the reason 'Fraudulent activity reported; dispute process initiated.' "
            "Finally, update her account preferences to ensure all notifications are enabled."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_2001", "days": 730}),
            Action(name="detect_suspicious_activity_and_alert", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="submit_support_ticket", kwargs={
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
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_chk_2001", "alert_reason": "Fraudulent activity reported; dispute process initiated."}),
            Action(name="update_account_preferences", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "preferences": {"notifications": True}}),
        ],
        outputs=[
            "Identity of Jane Smith verified and transaction history reviewed.",
            "Suspicious activity check performed.",
            "High-priority dispute ticket 'ticket_user_027_dispute' submitted for transaction 'txn_0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d'.",
            "Account 'acc_chk_2001' frozen and notification preferences updated.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_028",
        instruction=(
            "Onboard and set up accounts for high-net-worth client David Chen (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "Start by getting his profile and verifying his identity with his driver's license 'VI933872'. "
            "First, create a new Savings account for him with currency 'USD', and an initial limit of 0.0. "
            "Then, list his current beneficiaries and register a new international beneficiary with ID 'bene_user_028_uk_art' for 'London Fine Arts Ltd', "
            "with account number 'GB29NWBK60161331926819' at 'NatWest' (routing: 'NWBKGB2L') in the 'United Kingdom'. "
            "Schedule a one-time payment of $5,000 USD from his checking account 'acc_chk_3001' to this new UK beneficiary for '2025-09-01'. "
            "Update his account preferences to enable paperless billing and set 'SMS' as his communication channel. "
            "Finally, submit a support ticket with ID 'ticket_user_028_onboarding' under category 'Onboarding', priority 'High', via 'Internal System', "
            "with the request details: 'Onboarding for high-net-worth client David Chen complete. New accounts and beneficiaries configured as requested.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "VI933872"}),
            Action(name="create_customer_account", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "account_type": "Savings", "currency": "USD", "initial_limit": 0.0}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_id": "bene_user_028_uk_art",
                "beneficiary_name": "London Fine Arts Ltd",
                "country": "United Kingdom",
                "bank_details": {"account_number": "GB29NWBK60161331926819", "bank_name": "NatWest", "routing_info": "NWBKGB2L"}
            }),
            Action(name="schedule_payment_with_validation", kwargs={"from_account": "acc_chk_3001", "to_account": "GB29NWBK60161331926819", "amount": 5000.00, "currency": "USD", "date": "2025-09-01"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "preferences": {"paperless_billing": True, "communication_channel": "SMS"}}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "ticket_user_028_onboarding",
                "category": "Onboarding",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Onboarding for high-net-worth client David Chen complete. New accounts and beneficiaries configured as requested."
            }),
        ],
        outputs=[
            "Identity verified for David Chen and a new savings account was created.",
            "New international beneficiary 'London Fine Arts Ltd' registered.",
            "Payment of $5,000 USD to new beneficiary scheduled for 2025-09-01.",
            "Preferences updated and high-priority onboarding ticket logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_029",
        instruction=(
            "Perform simple account maintenance for customer Oliver Williams (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5). "
            "Retrieve his profile and verify his identity with his driver's license 'fo611864'. "
            "Check the balance of his checking account 'acc_chk_6001'. "
            "Update his contact information to email 'oliver.w.main@example.co.uk' and phone '+44 7700 900555'. "
            "Then update his account preferences to use 'Email' as his communication channel and enable paperless billing. "
            "Afterward, list his current beneficiaries to confirm his setup. "
            "Finally, download his account statement for October 2023 for his records."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "id_document": "fo611864"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_6001"}),
            Action(name="update_customer_email", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "new_email": "oliver.w.main@example.co.uk", "new_phone": "+44 7700 900555"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "preferences": {"communication_channel": "Email", "paperless_billing": True}}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}),
            Action(name="download_statement_by_date", kwargs={"account_id": "acc_chk_6001", "month": "2023-10"}),
        ],
        outputs=[
            "Identity verified for Oliver Williams and account balance checked.",
            "Customer email and phone number have been updated.",
            "Account preferences set to Email and paperless billing.",
            "Beneficiary list checked and October 2023 statement downloaded.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_030",
        instruction=(
            "Manage loan and payment details for customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "Current date is 2025-07-24. Start by getting his profile and verifying his identity with his passport 'lF146011'. "
            "First, summarize the status of his loan applications. "
            "Next, list his current beneficiaries. "
            "He wishes to cancel his monthly scheduled payment to 'Anytown Utility Services', which has the ID 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d'. "
            "After canceling that payment, schedule a new one-time payment of $250.00 from his checking account 'acc_chk_1001' to his other beneficiary, "
            "Jane Smith (account: '9876543210'), for the date '2025-08-20'. "
            "Download the latest monthly statement for his savings account 'acc_sav_1002' for July 2025. "
            "Finally, submit a support ticket with ID 'ticket_user_030_payment_changes' under category 'Account Management', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Canceled scheduled payment sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d and scheduled new payment to Jane Smith.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="summarize_loan_applications_by_status", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="schedule_payment_with_validation", kwargs={
                "from_account": "acc_chk_1001",
                "to_account": "9876543210",
                "amount": 250.00,
                "currency": "USD",
                "date": "2025-08-20"
            }),
            Action(name="download_statement_by_date", kwargs={"account_id": "acc_sav_1002", "month": "2025-07"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_030_payment_changes",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Canceled scheduled payment sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d and scheduled new payment to Jane Smith."
            }),
        ],
        outputs=[
            "Identity verified for John Doe and loan status summarized.",
            "Scheduled payment 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d' to Anytown Utility Services canceled.",
            "New one-time payment of $250.00 to Jane Smith scheduled for 2025-08-20.",
            "Savings account statement for July 2025 downloaded and support ticket logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_031",
        instruction=(
            "Execute a full account consolidation for customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "First, get his profile and verify his identity using his passport 'lF146011'. "
            "He wants to close his credit card 'acc_crd_1003'. Check the balance of the credit card. The balance is -$2500.00. "
            "Also, check the balance of his checking account 'acc_chk_1001'. The balance is $5230.50. "
            "Transfer $2500.00 from the checking account to the credit card account 'acc_crd_1003' to pay off the debt. "
            "Once paid off, submit a request to close the credit card account. "
            "Next, transfer the entire remaining balance of $2730.50 from the checking account 'acc_chk_1001' to his savings account 'acc_sav_1002'. "
            "After the transfer, submit a request to close the now-empty checking account 'acc_chk_1001'. "
            "Finally, submit a support ticket with ID 'ticket_user_031_consolidation' under category 'Account Management', priority 'High', via 'Web Portal', "
            "with the request details: 'Customer has completed account consolidation. Closed credit card acc_crd_1003 and checking acc_chk_1001 after transferring all funds to savings acc_sav_1002.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_crd_1003", "amount": 2500.00}),
            Action(name="close_account_request", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_sav_1002", "amount": 2730.50}),
            Action(name="close_account_request", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_031_consolidation",
                "category": "Account Management",
                "priority": "High",
                "channel": "Web Portal",
                "request_details": "Customer has completed account consolidation. Closed credit card acc_crd_1003 and checking acc_chk_1001 after transferring all funds to savings acc_sav_1002."
            }),
        ],
        outputs=[
            "Identity verified for John Doe and balances for accounts acc_crd_1003 and acc_chk_1001 checked.",
            "Credit card acc_crd_1003 paid off and submitted for closure.",
            "Remaining funds from checking acc_chk_1001 transferred to savings acc_sav_1002.",
            "Checking account acc_chk_1001 submitted for closure and a high-priority ticket was logged to document the consolidation.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_032",
        instruction=(
            "Assist small business owner Liam O'Connor (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11) with managing his supplier list from his account acc_chk_12001. "
            "First, get his profile and verify his identity using passport 'Se620000'. "
            "He needs to set up two new suppliers. First, register a new beneficiary with ID 'bene_user_032_farm_supplies' for 'Farm Supplies Co.' "
            "with account IBAN 'IE29AIBK93118212345678' at 'AIB' (routing: 'AIBKIE2D') in 'Ireland'. "
            "Second, register another beneficiary with ID 'bene_user_032_vet_services' for 'Veterinary Services Inc.' with account IBAN 'IE89BOFI90332112345678' "
            "at 'Bank of Ireland' (routing: 'BOFIIE2D') in 'Ireland'. "
            "Finally, submit a support ticket with ID 'ticket_user_032_supplier_setup' under category 'Account Management', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Set up two new beneficiaries for supplier payments: Farm Supplies Co. and Veterinary Services Inc.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "id_document": "Se620000"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "beneficiary_id": "bene_user_032_farm_supplies",
                "beneficiary_name": "Farm Supplies Co.",
                "country": "Ireland",
                "bank_details": {"account_number": "IE29AIBK93118212345678", "bank_name": "AIB", "routing_info": "AIBKIE2D"}
            }),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "beneficiary_id": "bene_user_032_vet_services",
                "beneficiary_name": "Veterinary Services Inc.",
                "country": "Ireland",
                "bank_details": {"account_number": "IE89BOFI90332112345678", "bank_name": "Bank of Ireland", "routing_info": "BOFIIE2D"}
            }),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "ticket_id": "ticket_user_032_supplier_setup",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Set up two new beneficiaries for supplier payments: Farm Supplies Co. and Veterinary Services Inc."
            }),
        ],
        outputs=[
            "Identity of Liam O'Connor verified.",
            "Two new beneficiaries, 'Farm Supplies Co.' and 'Veterinary Services Inc.', were successfully registered.",
            "A support ticket was logged to confirm the setup of the new supplier beneficiaries.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_033",
        instruction=(
            "Execute a security and relocation protocol for customer Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef). "
            "She is reporting an international move and wants to secure her account 'acc_chk_2001' during the transition. "
            "First, get her profile. Freeze her account with the reason 'Customer request during international move for security'. "
            "Then, verify her identity using her national ID 'jd195515' to authorize the upcoming changes. "
            "Update her contact information to the new email 'jane.smith.uk@example.com' and a new UK phone number '+44 7700 900888'. "
            "Update her preferences to the language 'en-GB' and communication channel to 'Email'. "
            "After the updates, unlock her account using the security code 'UKMOVE25'. "
            "Next, manage her beneficiaries: list them and delete her existing beneficiary 'John Doe' (ID: bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f). "
            "Register a new UK-based beneficiary with ID 'bene_user_033_uk_landlord' for 'UK Property Masters' with account number 'GB29NWBK60161331926819' at 'NatWest' (routing: 'NWBKGB2L'). "
            "Finally, submit a ticket with ID 'ticket_user_033_relocation' under category 'Account Management', priority 'High', via 'Internal System', "
            "with the request details: 'Customer relocation protocol complete. Account secured, contact info and beneficiaries updated. Address update must be handled by mail.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_chk_2001", "alert_reason": "Customer request during international move for security"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="update_customer_email", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "new_email": "jane.smith.uk@example.com", "new_phone": "+44 7700 900888"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "preferences": {"language": "en-GB", "communication_channel": "Email"}}),
            Action(name="unlock_account_by_security_check", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "security_code": "UKMOVE25"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_user_033_uk_landlord",
                "beneficiary_name": "UK Property Masters",
                "country": "United Kingdom",
                "bank_details": {"account_number": "GB29NWBK60161331926819", "bank_name": "NatWest", "routing_info": "NWBKGB2L"}
            }),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_033_relocation",
                "category": "Account Management",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Customer relocation protocol complete. Account secured, contact info and beneficiaries updated. Address update must be handled by mail."
            }),
        ],
        outputs=[
            "Account for Jane Smith frozen for security and identity verified.",
            "Contact info and preferences updated for UK residency.",
            "Account unlocked and beneficiary list updated to remove old contact and add new UK landlord.",
            "High-priority ticket logged to confirm all changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_034",
        instruction=(
            "Assist IT Consultant Lakshmi Narayanan (ID: a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4) with a loan inquiry and profile update. "
            "First, get her profile and verify her identity using her passport 'hI566779'. "
            "Then, summarize her loan application history. "
            "She would like to apply for a new, smaller loan; submit an application for $2,000 for the purpose of 'Educational Supplies'. "
            "Check the balance on her checking account 'acc_chk_5002'. "
            "Next, update her contact info to the new email 'l.narayanan.consulting@example.com' and new phone number '444-555-7777'. "
            "Finally, list her current beneficiaries to confirm her setup."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4", "id_document": "hI566779"}),
            Action(name="summarize_loan_applications_by_status", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}),
            Action(name="apply_for_loan_with_check", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4", "amount": 2000.0, "purpose": "Educational Supplies"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_5002"}),
            Action(name="update_customer_email", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4", "new_email": "l.narayanan.consulting@example.com", "new_phone": "444-555-7777"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}),
        ],
        outputs=[
            "Identity verified for Lakshmi Narayanan and her loan history was summarized.",
            "A new loan application for $2,000 for 'Educational Supplies' was submitted.",
            "Her checking account balance was checked.",
            "Her contact information was updated and her beneficiary list was confirmed.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_035",
        instruction=(
            "Help student Mei Lin (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef-22) manage her finances from her checking account 'acc_chk_23001'. "
            "Current date is 2025-07-24. First, get her profile and verify her identity using her driver's license 'Qb140023'. "
            "Retrieve her transaction history for the last 30 days and aggregate her monthly expenses for June 2025 to help her create a budget. "
            "Download her statement for June 2025 for her records. "
            "Next, she needs to set up a recurring rent payment. Register a new beneficiary with ID 'bene_user_035_landlord' for 'Beijing Property Management' "
            "with account number '622848001002003004' at 'Agricultural Bank of China' (routing: 'ABOCCNBJ') in 'China'. "
            "Then, schedule a one-time payment of 2000 CNY to this new beneficiary for '2025-08-01'. "
            "Finally, submit a support ticket with ID 'ticket_user_035_budget' under category 'Payments', priority 'Low', via 'Mobile App', "
            "with the request details: 'Assisted student with budget review and set up first rent payment to new landlord beneficiary.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22", "id_document": "Qb140023"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_23001", "days": 30}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_23001", "month": "2025-06"}),
            Action(name="download_statement_by_date", kwargs={"account_id": "acc_chk_23001", "month": "2025-06"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                "beneficiary_id": "bene_user_035_landlord",
                "beneficiary_name": "Beijing Property Management",
                "country": "China",
                "bank_details": {"account_number": "622848001002003004", "bank_name": "Agricultural Bank of China", "routing_info": "ABOCCNBJ"}
            }),
            Action(name="schedule_payment_with_validation", kwargs={"from_account": "acc_chk_23001", "to_account": "622848001002003004", "amount": 2000.0, "currency": "CNY", "date": "2025-08-01"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                "ticket_id": "ticket_user_035_budget",
                "category": "Payments",
                "priority": "Low",
                "channel": "Mobile App",
                "request_details": "Assisted student with budget review and set up first rent payment to new landlord beneficiary."
            }),
        ],
        outputs=[
            "Identity verified for Mei Lin and her financial history for June 2025 was reviewed.",
            "June 2025 statement downloaded.",
            "New beneficiary 'Beijing Property Management' was registered.",
            "A rent payment of 2000 CNY was scheduled for 2025-08-01 and a support ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_036",
        instruction=(
            "Execute a complex joint account setup and security protocol involving two customers. "
            "The primary customer is Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef) and she wants to add John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) as a joint holder to her account 'acc_chk_2001'. "
            "First, retrieve the profile for Jane Smith and verify her identity using her national ID 'jd195515'. "
            "Then, retrieve the profile for John Doe and verify his identity using his passport 'lF146011'. "
            "Add John Doe as a joint account holder to Jane Smith's checking account 'acc_chk_2001'. "
            "Next, list the beneficiaries for Jane Smith and remove the one named 'John Doe' (ID: bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f), as he is now a joint holder. "
            "Register a new beneficiary with ID 'bene_user_036_family_trust' for 'Smith Family Trust', with account number '5555' at 'CAD Bank' (routing: 'N/A') in 'Canada'. "
            "Update the account preferences for Jane Smith to enable paperless billing. "
            "As a final security measure, freeze the account 'acc_chk_2001' with the reason 'Awaiting verbal confirmation of new joint holder setup from both parties.' "
            "Submit a ticket with ID 'ticket_user_036_joint_setup' under category 'Account Management', priority 'High', via 'Internal System', "
            "with the request details: 'Joint holder John Doe added to account acc_chk_2001. Beneficiary list updated. Account frozen pending verbal confirmation.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="add_joint_account_holder", kwargs={"account_id": "acc_chk_2001", "holder_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_user_036_family_trust",
                "beneficiary_name": "Smith Family Trust",
                "country": "Canada",
                "bank_details": {"account_number": "5555", "bank_name": "CAD Bank", "routing_info": "N/A"}
            }),
            Action(name="update_account_preferences", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "preferences": {"paperless_billing": True}}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_chk_2001", "alert_reason": "Awaiting verbal confirmation of new joint holder setup from both parties."}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_036_joint_setup",
                "category": "Account Management",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Joint holder John Doe added to account acc_chk_2001. Beneficiary list updated. Account frozen pending verbal confirmation."
            }),
        ],
        outputs=[
            "Identities of Jane Smith and John Doe verified.",
            "John Doe added as joint holder to account acc_chk_2001.",
            "Beneficiary list for Jane Smith updated: 'John Doe' removed, 'Smith Family Trust' added.",
            "Account preferences updated and account frozen with a high-priority ticket logged for follow-up.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_037",
        instruction=(
            "A customer, Fatima Al-Fassi (ID: c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6), needs to update her recurring payments and beneficiaries. "
            "First, get her profile and verify her identity using her national ID 'IJ758739'. "
            "She wants to cancel her quarterly scheduled payment of 10000 AED, which has the ID 'sp_a2c1d9b3-d2e1-f0a9-b8c7-d6e5f4a3b2c1'. "
            "Next, list her beneficiaries and remove her current beneficiary 'Dubai International School' (ID: bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f). "
            "Then, register a new beneficiary with ID 'bene_user_037_art_foundation' for 'Abu Dhabi Art Foundation', with account IBAN 'AE420260001014567890555' at 'Emirates NBD' (BIC: 'EBILAEAD') in 'United Arab Emirates'. "
            "Update her contact information to the new email 'fatima.art@example.ae' and phone number '+971 50 765 4321'. "
            "Finally, submit a support ticket with ID 'ticket_user_037_payment_update' under category 'Payments', priority 'Medium', via 'Email', with the "
            "request details: 'Canceled scheduled payment sp_a2c1d9b3-d2e1-f0a9-b8c7-d6e5f4a3b2c1 and updated beneficiary list as per customer request.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "id_document": "IJ758739"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_a2c1d9b3-d2e1-f0a9-b8c7-d6e5f4a3b2c1"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "beneficiary_id": "bene_user_037_art_foundation",
                "beneficiary_name": "Abu Dhabi Art Foundation",
                "country": "United Arab Emirates",
                "bank_details": {"account_number": "AE420260001014567890555", "bank_name": "Emirates NBD", "routing_info": "EBILAEAD"}
            }),
            Action(name="update_customer_email", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "new_email": "fatima.art@example.ae", "new_phone": "+971 50 765 4321"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "ticket_id": "ticket_user_037_payment_update",
                "category": "Payments",
                "priority": "Medium",
                "channel": "Email",
                "request_details": "Canceled scheduled payment sp_a2c1d9b3-d2e1-f0a9-b8c7-d6e5f4a3b2c1 and updated beneficiary list as per customer request."
            }),
        ],
        outputs=[
            "Identity verified for Fatima Al-Fassi.",
            "Scheduled payment 'sp_a2c1d9b3-d2e1-f0a9-b8c7-d6e5f4a3b2c1' has been canceled.",
            "Beneficiary list updated: 'Dubai International School' removed and 'Abu Dhabi Art Foundation' added.",
            "Customer contact information updated and a support ticket was logged to confirm all changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_038",
        instruction=(
            "Perform a full security audit and profile update for high-net-worth client David Chen (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "Current date is 2023-11-15. Get his profile and verify his identity using his driver's license 'VI933872'. "
            "Retrieve the full transaction history for both his checking account 'acc_chk_3001' and his investment account 'acc_inv_3002'. "
            "Aggregate his monthly expenses from his checking account for October 2023. "
            "Update his primary contact details to email 'david.chen.primary@example.com' and phone '555-987-1111'. "
            "Update his account preferences to language 'en-US' and enable all notifications. "
            "Then, freeze his checking account 'acc_chk_3001' with the reason 'Security audit in progress. Customer notified.' "
            "Finally, submit a ticket with ID 'ticket_user_038_sec_audit' under category 'Security', priority 'Critical', via 'Internal System', "
            "with the request details: 'Full security audit complete for David Chen. Profile and accounts updated. Checking account temporarily frozen.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "VI933872"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_3001"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_inv_3002"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_3001", "month": "2023-10"}),
            Action(name="update_customer_email", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "new_email": "david.chen.primary@example.com", "new_phone": "555-987-1111"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "preferences": {"language": "en-US", "notifications": True}}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_chk_3001", "alert_reason": "Security audit in progress. Customer notified."}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "ticket_user_038_sec_audit",
                "category": "Security",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Full security audit complete for David Chen. Profile and accounts updated. Checking account temporarily frozen."
            }),
        ],
        outputs=[
            "Identity verified for David Chen and transaction histories for two accounts retrieved.",
            "October 2023 expenses aggregated and contact info updated.",
            "The customer's preferences were updated.",
            "Checking account frozen and a critical security audit ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_039",
        instruction=(
            "Perform a simple profile and multi-account balance check for customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "First, get his profile and verify his identity using his passport 'lF146011'. "
            "Then, retrieve the balances for all three of his accounts: checking 'acc_chk_1001', savings 'acc_sav_1002', and credit card 'acc_crd_1003'. "
            "After confirming the balances, update his account preferences to enable paperless billing and set the primary communication channel to 'App'. "
            "Finally, update his email address to 'john.doe.main@example.com' and his primary phone number to '123-456-8888'."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "preferences": {"paperless_billing": True, "communication_channel": "App"}}),
            Action(name="update_customer_email", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "new_email": "john.doe.main@example.com", "new_phone": "123-456-8888"}),
        ],
        outputs=[
            "Identity verified for John Doe.",
            "Balances for checking, savings, and credit card accounts were successfully retrieved.",
            "Account preferences were updated to use the App and paperless billing.",
            "Customer's email and phone number were updated.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_040",
        instruction=(
            "Handle a sensitive loan management case for customer Mohammed Al-Masri (ID: d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25), "
            "who has a delinquent personal loan 'loan_pers_020'. First, get his profile and verify his identity using his national ID 'fy088462'. "
            "To understand his financial situation, retrieve the transaction history for his checking account 'acc_chk_26001' for the last 90 days "
            "and aggregate his expenses for October 2023. "
            "Ensure the bank has the correct contact information by updating his email to 'mo.almasri.updates@example.eg' and his phone to '+20 100 765 4321'. "
            "Finally, submit a support ticket with ID 'ticket_user_040_payment_plan' to the 'Loan Support' category with 'High' priority via the 'Phone' channel. "
            "The request details must be: 'Customer is requesting to negotiate a new payment plan for delinquent loan loan_pers_020 due to recent financial hardship. Please have an agent contact him.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25", "id_document": "fy088462"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_26001", "days": 90}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_26001", "month": "2023-10"}),
            Action(name="update_customer_email", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25", "new_email": "mo.almasri.updates@example.eg", "new_phone": "+20 100 765 4321"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                "ticket_id": "ticket_user_040_payment_plan",
                "category": "Loan Support",
                "priority": "High",
                "channel": "Phone",
                "request_details": "Customer is requesting to negotiate a new payment plan for delinquent loan loan_pers_020 due to recent financial hardship. Please have an agent contact him."
            }),
        ],
        outputs=[
            "Identity verified for Mohammed Al-Masri.",
            "Transaction history and recent expenses have been reviewed to assess financial hardship.",
            "Customer's contact information has been updated.",
            "A high-priority support ticket has been logged to initiate a payment plan negotiation for his delinquent loan.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_041",
        instruction=(
            "Execute an account recovery and security enhancement protocol for Chloe Dubois (ID: e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2), who suspects her credentials were compromised. "
            "First, get her profile and verify her identity using her driver's license 'im665671'. "
            "Immediately freeze both of her accounts for security: checking 'acc_chk_9001' and credit card 'acc_crd_9002', with the reason 'Customer-reported potential unauthorized access.' "
            "Update her contact information to the new secure email 'chloe.dubois.sec@example.com' and new phone number '+33 6 87 65 43 21'. "
            "Finally, submit a support ticket with ID 'ticket_user_041_recovery' under category 'Security', priority 'Critical', via 'Internal System'. "
            "The request details must be: 'Account recovery protocol executed. Contact info updated. Please manually unlock checking account acc_chk_9001 with security code RECOVERY2025. Credit card to remain frozen.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "id_document": "im665671"}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_chk_9001", "alert_reason": "Customer-reported potential unauthorized access."}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_crd_9002", "alert_reason": "Customer-reported potential unauthorized access."}),
            Action(name="update_customer_email", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "new_email": "chloe.dubois.sec@example.com", "new_phone": "+33 6 87 65 43 21"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "ticket_id": "ticket_user_041_recovery",
                "category": "Security",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Account recovery protocol executed. Contact info updated. Please manually unlock checking account acc_chk_9001 with security code RECOVERY2025. Credit card to remain frozen."
            }),
        ],
        outputs=[
            "Identity verified for Chloe Dubois and both of her accounts were frozen.",
            "Customer's contact information was updated to a new secure email and phone.",
            "A critical security ticket was logged to document the incident and request a manual account unlock.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_042",
        instruction=(
            "Assist customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) with managing his credit card and scheduled payments. "
            "First, get his profile and verify his identity using passport 'lF146011'. "
            "Retrieve the current balances for his checking account 'acc_chk_1001' and his credit card 'acc_crd_1003'. The credit card balance is -$2500. "
            "Make a payment of $1000.00 from his checking account to his credit card 'acc_crd_1003'. "
            "Next, he wants to cancel a monthly scheduled payment of $75.00; its ID is 'sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w2'. "
            "After handling the payments, update his account preferences to enable paperless billing. "
            "Finally, submit a support ticket with ID 'ticket_user_042_payments' under category 'Payments', priority 'Low', via 'Web Portal', "
            "with the request details: 'Customer made a $1000 payment to credit card acc_crd_1003 and canceled scheduled payment sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w2.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_crd_1003", "amount": 1000.00}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w2"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "preferences": {"paperless_billing": True}}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_042_payments",
                "category": "Payments",
                "priority": "Low",
                "channel": "Web Portal",
                "request_details": "Customer made a $1000 payment to credit card acc_crd_1003 and canceled scheduled payment sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w2."
            }),
        ],
        outputs=[
            "Identity verified for John Doe and account balances retrieved.",
            "A payment of $1000.00 was transferred from checking to the credit card.",
            "Scheduled payment 'sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w2' was canceled.",
            "Account preferences were updated and a support ticket was logged confirming the actions.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_043",
        instruction=(
            "Perform a detailed financial review for international customer Hans Müller (ID: d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). "
            "Get his profile and verify his identity using his driver's license 'Kt516858'. "
            "Retrieve the transaction history for his checking account 'acc_chk_8001' for the last 90 days, then aggregate his expenses for October 2023. "
            "Also, get the current balance of his savings account 'acc_sav_8002'. "
            "Next, he needs to update the details for his landlord beneficiary, Klaus Schmidt (ID: bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a). "
            "Delete the existing beneficiary record. Then, re-register the beneficiary using the same ID 'bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a' and name 'Klaus Schmidt', "
            "but with new bank details: account IBAN 'DE89370400440532013999' at 'Commerzbank' (BIC: 'COBADEFF') in 'Germany'. "
            "Update his secondary contact information to email 'hans.mueller.secondary@example.de' and phone '+49 171 1112223'. "
            "Finally, submit a ticket with ID 'ticket_user_043_review' under category 'Audit', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Financial review complete. Beneficiary details for Klaus Schmidt updated as per new information provided.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "id_document": "Kt516858"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_8001", "days": 90}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_8001", "month": "2023-10"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_8002"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a",
                "beneficiary_name": "Klaus Schmidt",
                "country": "Germany",
                "bank_details": {"account_number": "DE89370400440532013999", "bank_name": "Commerzbank", "routing_info": "COBADEFF"}
            }),
            Action(name="update_customer_email", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "new_email": "hans.mueller.secondary@example.de", "new_phone": "+49 171 1112223"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "ticket_id": "ticket_user_043_review",
                "category": "Audit",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Financial review complete. Beneficiary details for Klaus Schmidt updated as per new information provided."
            }),
        ],
        outputs=[
            "Identity verified for Hans Müller and financial review of his accounts performed.",
            "Beneficiary 'Klaus Schmidt' was deleted and re-registered with new bank details.",
            "Customer's secondary contact information was updated.",
            "An audit ticket was logged to document the review and all changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_044",
        instruction=(
            "Perform a simple beneficiary management task for David Chen (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "First, get his profile and verify his identity using his national ID 'pI260068'. "
            "List his current beneficiaries. He wants to remove his existing utility provider, 'Metropolis Power & Light' (ID: bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a). "
            "After removing the old one, register a new beneficiary with ID 'bene_user_044_gotham_cable' for 'Gotham Cable', "
            "with account number '123123123' at 'Bank of Gotham' (routing: '021000021') in the 'USA'. "
            "Check the balance of his checking account 'acc_chk_3001'. "
            "Finally, submit a support ticket with ID 'ticket_user_044_bene_update' under category 'Account Management', priority 'Low', via 'Mobile App', "
            "with the request details: 'Beneficiary Metropolis Power & Light removed and Gotham Cable added.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "pI260068"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_id": "bene_user_044_gotham_cable",
                "beneficiary_name": "Gotham Cable",
                "country": "USA",
                "bank_details": {"account_number": "123123123", "bank_name": "Bank of Gotham", "routing_info": "021000021"}
            }),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_3001"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "ticket_user_044_bene_update",
                "category": "Account Management",
                "priority": "Low",
                "channel": "Mobile App",
                "request_details": "Beneficiary Metropolis Power & Light removed and Gotham Cable added."
            }),
        ],
        outputs=[
            "Identity verified for David Chen and beneficiaries listed.",
            "Beneficiary 'Metropolis Power & Light' was successfully removed.",
            "New beneficiary 'Gotham Cable' was registered.",
            "Checking account balance was confirmed and a support ticket was logged for the changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_045",
        instruction=(
            "Handle a request from Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef) to reconfigure her joint checking account 'acc_chk_2001' to a single-user account. "
            "First, get her profile and verify her identity using her national ID 'jd195515'. "
            "Remove the joint account holder with ID 'cust_joint_005' from the account. "
            "After the removal, retrieve the transaction history for the last 90 days to ensure there are no outstanding transactions related to the removed holder. "
            "Then, update the account preferences to reflect single ownership by setting the communication channel to 'App' and disabling paperless billing. "
            "Update Jane's personal contact info to the email 'jane.smith.primary@example.com' and phone '555-123-9999'. "
            "List her beneficiaries to confirm they are still correct for her as the sole account holder. "
            "Finally, submit a ticket with ID 'ticket_user_045_joint_removal' under category 'Account Management', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Joint account holder cust_joint_005 removed from acc_chk_2001. Account preferences and customer contact info updated for single ownership.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="remove_joint_account_holder", kwargs={"account_id": "acc_chk_2001", "holder_id": "cust_joint_005"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_2001", "days": 90}),
            Action(name="update_account_preferences", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "preferences": {"communication_channel": "App", "paperless_billing": False}}),
            Action(name="update_customer_email", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "new_email": "jane.smith.primary@example.com", "new_phone": "555-123-9999"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_045_joint_removal",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Joint account holder cust_joint_005 removed from acc_chk_2001. Account preferences and customer contact info updated for single ownership."
            }),
        ],
        outputs=[
            "Identity verified for Jane Smith and joint holder 'cust_joint_005' removed from account acc_chk_2001.",
            "Transaction history reviewed to confirm no outstanding joint transactions.",
            "Account preferences and customer contact information updated for single ownership.",
            "Beneficiary list confirmed and a support ticket was logged to document the changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_046",
        instruction=(
            "Execute a multi-customer operation. The primary customer, David Chen (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a), wants to send $1500 to Maria Garcia (ID: f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9). "
            "First, get the profile for the sender, David Chen, and verify his identity using his national ID 'pI260068'. "
            "Next, get the profile for the recipient, Maria Garcia, and update her contact information to email 'maria.garcia.updates@example.com' and phone '555-444-3333'. "
            "Then, on David Chen's profile, list his current beneficiaries. Register Maria Garcia as a new beneficiary with ID 'bene_user_046_m_garcia', "
            "using her checking account number '8888' at 'State University Bank' (routing: '011000015') in the 'USA'. "
            "After registration, transfer $1500.00 from David's checking account 'acc_chk_3001' to Maria's account '8888'. "
            "Check the new balance of David's account 'acc_chk_3001' after the transfer. "
            "Finally, submit a support ticket from David's profile with ID 'ticket_user_046_transfer' under category 'Transfers', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Registered new beneficiary Maria Garcia and completed a one-time transfer of $1500.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "pI260068"}),
            Action(name="get_customer_profile", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}),
            Action(name="update_customer_email", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9", "new_email": "maria.garcia.updates@example.com", "new_phone": "555-444-3333"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_id": "bene_user_046_m_garcia",
                "beneficiary_name": "Maria Garcia",
                "country": "USA",
                "bank_details": {"account_number": "8888", "bank_name": "State University Bank", "routing_info": "011000015"}
            }),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_3001", "to_account": "8888", "amount": 1500.00}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_3001"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "ticket_user_046_transfer",
                "category": "Transfers",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Registered new beneficiary Maria Garcia and completed a one-time transfer of $1500."
            }),
        ],
        outputs=[
            "Identity of sender David Chen verified and profile of recipient Maria Garcia updated.",
            "Maria Garcia registered as a new beneficiary on David Chen's profile.",
            "A transfer of $1500.00 was completed from David's account to Maria's.",
            "The sender's account balance was checked post-transfer and a support ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_047",
        instruction=(
            "A customer, John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), is inquiring about paying off his auto loan early. "
            "Current date is 2023-11-20. First, get his profile and verify his identity using passport 'lF146011'. "
            "Retrieve the current balance of his checking account 'acc_chk_1001' to assess his available funds. "
            "Then, summarize his loan application history to review his existing loans. "
            "To understand his payment history, retrieve all transactions from his checking account for the last 180 days. "
            "Aggregate his expenses for October 2023 to review his recent budget. "
            "Finally, submit a support ticket with ID 'ticket_user_047_loan_inquiry' to the 'Loan Support' category with 'Medium' priority via 'Email', "
            "with the request details: 'Inquiry regarding early payoff amount and procedure for auto loan loan_auto_002.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="summarize_loan_applications_by_status", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_1001", "days": 180}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_1001", "month": "2023-10"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_047_loan_inquiry",
                "category": "Loan Support",
                "priority": "Medium",
                "channel": "Email",
                "request_details": "Inquiry regarding early payoff amount and procedure for auto loan loan_auto_002."
            }),
        ],
        outputs=[
            "Identity verified for John Doe and his checking account balance was retrieved.",
            "Loan history was summarized and transaction history reviewed for past payments.",
            "October 2023 expenses were aggregated to analyze recent budget.",
            "A support ticket was submitted to inquire about the early loan payoff procedure.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_048",
        instruction=(
            "Perform a full security audit and profile update for international client Fatima Al-Fassi (ID: c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6). "
            "Current date is 2023-11-20. First, get her profile and verify her identity using her national ID 'IJ758739'. "
            "Retrieve the full transaction history for her checking account 'acc_chk_7001' and get the current balance of her savings account 'acc_sav_7002'. "
            "Aggregate her expenses from the checking account for October 2023. "
            "Update her contact details to the email 'fatima.alfassi.secure@example.ae' and phone '+971 50 111 2222'. "
            "Update her account preferences to language 'ar-AE' and enable all notifications. "
            "Temporarily freeze her checking account 'acc_chk_7001' with the reason 'Comprehensive security audit in progress.' "
            "Finally, submit a ticket with ID 'ticket_user_048_audit' under category 'Security', priority 'Critical', via 'Internal System', "
            "with the request details: 'Full security audit for Fatima Al-Fassi complete. Profile and preferences updated. Checking account is temporarily frozen.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "id_document": "IJ758739"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_7001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_7002"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_7001", "month": "2023-10"}),
            Action(name="update_customer_email", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "new_email": "fatima.alfassi.secure@example.ae", "new_phone": "+971 50 111 2222"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "preferences": {"language": "ar-AE", "notifications": True}}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_chk_7001", "alert_reason": "Comprehensive security audit in progress."}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "ticket_id": "ticket_user_048_audit",
                "category": "Security",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Full security audit for Fatima Al-Fassi complete. Profile and preferences updated. Checking account is temporarily frozen."
            }),
        ],
        outputs=[
            "Identity verified for Fatima Al-Fassi and account activities reviewed.",
            "Customer contact info and preferences were updated.",
            "The checking account was frozen for a security audit.",
            "A critical security ticket was logged to document the process.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_049",
        instruction=(
            "Perform a simple information retrieval and update task for customer Hans Müller (ID: d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). "
            "First, get his profile and verify his identity using his driver's license 'Kt516858'. "
            "Then, retrieve the current balances for both of his accounts: checking 'acc_chk_8001' and savings 'acc_sav_8002'. "
            "Update his contact info to the new email address 'hans.m.primary@example.de' and new phone number '+49 171 9998887'. "
            "Next, list his beneficiaries to confirm his current setup. "
            "Finally, submit a low-priority support ticket with ID 'ticket_user_049_contact_update' under category 'Account Management' via 'Email' "
            "with the request details: 'Customer contact information has been updated as requested.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "id_document": "Kt516858"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_8002"}),
            Action(name="update_customer_email", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "new_email": "hans.m.primary@example.de", "new_phone": "+49 171 9998887"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "ticket_id": "ticket_user_049_contact_update",
                "category": "Account Management",
                "priority": "Low",
                "channel": "Email",
                "request_details": "Customer contact information has been updated as requested."
            }),
        ],
        outputs=[
            "Identity verified for Hans Müller.",
            "Balances for checking and savings accounts were successfully retrieved.",
            "Customer's email and phone number were updated.",
            "Beneficiary list was confirmed and a low-priority ticket was logged to document the update.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_050",
        instruction=(
            "Assist customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) with closing his savings account 'acc_sav_1002' and consolidating funds. "
            "First, get his profile and verify his identity using his passport 'lF146011'. "
            "Before closing the account, you must handle an annual payment of $1000.00 sourced from it. Cancel the scheduled payment with ID 'sp_d9b3a2c1-f0a9-b8c7-d6e5-f4a3b2c1d0e9'. "
            "After the payment is canceled, get the full balance of the savings account 'acc_sav_1002'. The balance is $15780.00. "
            "To comply with the daily transfer limit, transfer the entire balance of $15780.00 from the savings account to his checking account 'acc_chk_1001' in two separate transactions: one for $10000.00 and a second for $5780.00. "
            "Once the savings account is empty, submit a request to close it. "
            "Finally, submit a support ticket with ID 'ticket_user_050_closure' under category 'Account Closure', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Canceled scheduled payment from savings, transferred full balance to checking, and submitted savings account acc_sav_1002 for closure.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_d9b3a2c1-f0a9-b8c7-d6e5-f4a3b2c1d0e9"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_sav_1002", "to_account": "acc_chk_1001", "amount": 10000.00}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_sav_1002", "to_account": "acc_chk_1001", "amount": 5780.00}),
            Action(name="close_account_request", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_050_closure",
                "category": "Account Closure",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Canceled scheduled payment from savings, transferred full balance to checking, and submitted savings account acc_sav_1002 for closure."
            }),
        ],
        outputs=[
            "Identity verified for John Doe.",
            "Scheduled payment 'sp_d9b3a2c1-f0a9-b8c7-d6e5-f4a3b2c1d0e9' was successfully canceled.",
            "The full balance from savings account acc_sav_1002 was transferred to checking in two transactions.",
            "Savings account submitted for closure and a support ticket was logged to document the process.",
        ],
    ),
     Task(
        annotator="0",
        user_id="user_051",
        instruction=(
            "Execute a detailed financial audit for the joint account 'acc_chk_2001'. The primary holder is Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef) and the joint holder is John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "First, retrieve the profile for Jane Smith and verify her identity using her national ID 'jd195515'. "
            "Then, retrieve the profile for John Doe and verify his identity using his passport 'lF146011'. "
            "Perform a Q1 2023 audit on the joint account 'acc_chk_2001' by retrieving the full transaction history and then aggregating the monthly expenses for January, February, and March of 2023. "
            "After the audit, update the primary holder's (Jane Smith) contact information to the new email 'jane.smith.joint@example.com' and phone '555-123-7788'. "
            "Finally, submit a support ticket with ID 'ticket_user_051_joint_audit' under category 'Audit', priority 'Medium', via 'Internal System', "
            "with the request details: 'Q1 2023 audit completed for joint account acc_chk_2001. Both holders verified. Primary holder contact information updated.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_2001", "start_date": "2023-01-01", "end_date": "2023-03-31"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_2001", "month": "2023-01"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_2001", "month": "2023-02"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_2001", "month": "2023-03"}),
            Action(name="update_customer_email", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "new_email": "jane.smith.joint@example.com", "new_phone": "555-123-7788"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_051_joint_audit",
                "category": "Audit",
                "priority": "Medium",
                "channel": "Internal System",
                "request_details": "Q1 2023 audit completed for joint account acc_chk_2001. Both holders verified. Primary holder contact information updated."
            }),
        ],
        outputs=[
            "Profiles retrieved and identities verified for both joint account holders Jane Smith and John Doe.",
            "Q1 2023 financial audit completed, including transaction history review and expense aggregation for three months.",
            "Primary holder's contact information was updated.",
            "A medium-priority audit ticket was logged to document the review and updates.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_052",
        instruction=(
            "Assist customer Chloe Dubois (ID: e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2) with updating her account 'acc_chk_9001' after her recent marriage. "
            "First, get her profile and verify her identity using her driver's license 'im665671'. "
            "She wants to remove her mother, Marie Dubois (ID: bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c), from her list of beneficiaries. List her beneficiaries and then delete the specified record. "
            "Next, register her new spouse, David Chen (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a), as a new beneficiary with ID 'bene_user_052_d_chen', "
            "using his checking account number '6666' at 'City General Bank' (routing: 'N/A') in the 'USA'. "
            "Update her account preferences to set the communication channel to 'App'. "
            "Finally, submit a support ticket with ID 'ticket_user_052_marital_update' under category 'Account Management', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Marital status update: Removed previous beneficiary and added spouse as new beneficiary.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "id_document": "im665671"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "beneficiary_id": "bene_user_052_d_chen",
                "beneficiary_name": "David Chen",
                "country": "USA",
                "bank_details": {"account_number": "6666", "bank_name": "City General Bank", "routing_info": "N/A"}
            }),
            Action(name="update_account_preferences", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "preferences": {"communication_channel": "App"}}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "ticket_id": "ticket_user_052_marital_update",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Marital status update: Removed previous beneficiary and added spouse as new beneficiary."
            }),
        ],
        outputs=[
            "Identity verified for Chloe Dubois.",
            "Beneficiary Marie Dubois was successfully removed from the account.",
            "Spouse David Chen was added as a new beneficiary.",
            "Account preferences were updated and a ticket was logged to confirm the changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_053",
        instruction=(
            "Execute a lost card security protocol for customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "He has reported his credit card as lost. First, get his profile and verify his identity using his passport 'lF146011'. "
            "Immediately freeze his credit card account 'acc_crd_1003' with the reason 'Customer reported lost card'. "
            "Retrieve the transaction history for the credit card for the last 7 days to check for recent fraudulent activity. "
            "Aggregate the expenses on the card for the current month (July 2025) to help identify any unusual spending patterns. "
            "As a security precaution, update the customer's primary contact info to the email 'john.doe.secure@example.com' and phone '123-456-7777'. "
            "Finally, submit a support ticket with ID 'ticket_user_053_lost_card' to the 'Card Services' category with 'Critical' priority via the 'Phone' channel. "
            "The request details must be: 'Customer lost credit card acc_crd_1003. Account is frozen. Please issue a new card to the address on file and cancel the old one. Customer will review transactions for fraud.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_crd_1003", "alert_reason": "Customer reported lost card."}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_crd_1003", "days": 7}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_crd_1003", "month": "2025-07"}),
            Action(name="update_customer_email", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "new_email": "john.doe.secure@example.com", "new_phone": "123-456-7777"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_053_lost_card",
                "category": "Card Services",
                "priority": "Critical",
                "channel": "Phone",
                "request_details": "Customer lost credit card acc_crd_1003. Account is frozen. Please issue a new card to the address on file and cancel the old one. Customer will review transactions for fraud."
            }),
        ],
        outputs=[
            "Identity verified for John Doe and his credit card account acc_crd_1003 was frozen.",
            "Recent transaction history and monthly expenses were reviewed for fraudulent activity.",
            "Customer's primary contact information was updated as a security measure.",
            "A critical priority ticket was submitted to issue a new credit card.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_054",
        instruction=(
            "Perform a simple information retrieval task for customer Gabriel Silva (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17) for his financial planning. "
            "First, get his profile and verify his identity using his driver's license 'mQ002650'. "
            "Retrieve the current balance of his checking account 'acc_chk_18001'. "
            "Then, list his current beneficiaries to confirm his setup. "
            "Update his account preferences to enable all notifications. "
            "Finally, submit a support ticket with ID 'ticket_user_054_fi_plan' under category 'General Inquiry', priority 'Low', via 'Web Portal', "
            "with the request details: 'Customer requests information on available financial planning and budgeting tools.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "id_document": "mQ002650"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_18001"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "preferences": {"notifications": True}}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                "ticket_id": "ticket_user_054_fi_plan",
                "category": "General Inquiry",
                "priority": "Low",
                "channel": "Web Portal",
                "request_details": "Customer requests information on available financial planning and budgeting tools."
            }),
        ],
        outputs=[
            "Identity verified for Gabriel Silva.",
            "The customer's checking account balance was retrieved.",
            "Beneficiary list was checked and notification preferences were updated.",
            "A low-priority ticket was logged with a general inquiry about financial planning tools.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_055",
        instruction=(
            "Assist customer David Chen (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) with transferring a portion of his investment funds. "
            "First, get his profile and verify his identity using his national ID 'pI260068'. "
            "Retrieve the current balance of his investment account 'acc_inv_3002' and his checking account 'acc_chk_3001'. "
            "He wants to move funds for a down payment, so transfer $9,500.00 from his investment account to his checking account. "
            "After the transfer, update his preferences for the investment account to set the communication channel to 'Email'. "
            "Then, list his beneficiaries to ensure no changes are needed for his estate plan. "
            "Finally, submit a support ticket with ID 'ticket_user_055_inv_transfer' under category 'Transfers', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Completed partial transfer of $9,500.00 from investment account acc_inv_3002 to checking acc_chk_3001 as requested.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "pI260068"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_inv_3002"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_3001"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_inv_3002", "to_account": "acc_chk_3001", "amount": 9500.00}),
            Action(name="update_account_preferences", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "preferences": {"communication_channel": "Email"}}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "ticket_user_055_inv_transfer",
                "category": "Transfers",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Completed partial transfer of $9,500.00 from investment account acc_inv_3002 to checking acc_chk_3001 as requested."
            }),
        ],
        outputs=[
            "Identity verified for David Chen and balances for his investment and checking accounts were retrieved.",
            "A transfer of $9,500.00 from his investment to his checking account was completed.",
            "Preferences for the investment account were updated.",
            "Beneficiary list was confirmed and a ticket was logged to document the transfer.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_056",
        instruction=(
            "Execute a complex separation of the joint account 'acc_chk_2001'. The primary holder is Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef), and the joint holder to be removed is John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), listed as holder ID 'cust_joint_005'. "
            "First, get the profiles for both Jane Smith and John Doe, and verify their identities using their respective documents: national ID 'jd195515' for Jane and passport 'lF146011' for John. "
            "After verification, get the current balance of the joint account 'acc_chk_2001', which is 3100.75 CAD. "
            "Transfer 50% of the balance, exactly 1550.38 CAD, from the joint account 'acc_chk_2001' to John Doe's personal checking account, which has the account number '1111'. "
            "After splitting the funds, remove John Doe ('cust_joint_005') as a joint account holder from 'acc_chk_2001'. "
            "Update the primary account holder's (Jane Smith) preferences to set the communication channel to 'App' to reflect single ownership. "
            "Finally, submit a ticket with ID 'ticket_user_056_joint_split' under category 'Account Management', priority 'High', via 'Internal System', "
            "with the request details: 'Joint account acc_chk_2001 separation complete. Funds split and holder John Doe (cust_joint_005) removed.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_2001", "to_account": "1111", "amount": 1550.38}),
            Action(name="remove_joint_account_holder", kwargs={"account_id": "acc_chk_2001", "holder_id": "cust_joint_005"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "preferences": {"communication_channel": "App"}}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_056_joint_split",
                "category": "Account Management",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Joint account acc_chk_2001 separation complete. Funds split and holder John Doe (cust_joint_005) removed."
            }),
        ],
        outputs=[
            "Identities of both account holders, Jane Smith and John Doe, were verified.",
            "The balance of the joint account was checked.",
            "50% of the funds were transferred to John Doe's personal account.",
            "John Doe was removed as joint holder, preferences were updated, and a high-priority ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_057",
        instruction=(
            "Assist customer Kenji Tanaka (ID: f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3) in preparing his finances before a long trip. "
            "First, get his profile and verify his identity using his national ID 'nh464131'. "
            "He wants to temporarily suspend a large monthly payment; cancel the scheduled payment with ID 'sp_c1d9b3a2-a5b4-c3d2-e1f0-a9b8c7d6e5f4'. "
            "Next, list his beneficiaries and register a new temporary beneficiary with ID 'bene_user_057_travel_assist' for 'Global Travel Assist', "
            "with account number 'JP89370400440532013999' at 'Global Bank' (routing: 'GLBLJPJ1') in 'Japan'. "
            "Update his account preferences to disable paperless billing and set the communication channel to 'SMS' to receive important alerts while traveling. "
            "As a security measure, freeze his savings account 'acc_sav_10002' while he is away, using the exact reason: 'Customer request for security during travel.'. "
            "Finally, submit a support ticket with ID 'ticket_user_057_travel_prep' under category 'Account Management', priority 'Medium', via 'Email', "
            "with the request details: 'Travel Preparation: Canceled one scheduled payment, added temporary beneficiary, updated preferences to SMS, and froze savings account.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "id_document": "nh464131"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_c1d9b3a2-a5b4-c3d2-e1f0-a9b8c7d6e5f4"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "beneficiary_id": "bene_user_057_travel_assist",
                "beneficiary_name": "Global Travel Assist",
                "country": "Japan",
                "bank_details": {"account_number": "JP89370400440532013999", "bank_name": "Global Bank", "routing_info": "GLBLJPJ1"}
            }),
            Action(name="update_account_preferences", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "preferences": {"paperless_billing": False, "communication_channel": "SMS"}}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_sav_10002", "alert_reason": "Customer request for security during travel."}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "ticket_id": "ticket_user_057_travel_prep",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Email",
                "request_details": "Travel Preparation: Canceled one scheduled payment, added temporary beneficiary, updated preferences to SMS, and froze savings account."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "Scheduled payment 'sp_c1d9b3a2-a5b4-c3d2-e1f0-a9b8c7d6e5f4' was successfully canceled.",
            "A new temporary beneficiary was added and account preferences were updated for travel.",
            "The savings account was frozen as a security measure and a ticket was logged to document all changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_058",
        instruction=(
            "Perform a detailed annual financial audit for the business account of customer Adetokunbo Adebayor (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23). "
            "Current date is 2024-01-15. Get his profile and verify his identity using his national ID 'uY143801'. "
            "Retrieve the full transaction history for his business checking account 'acc_chk_24001' for the last 365 days. "
            "Then, perform a Q1 2023 review by aggregating the monthly expenses for January, February, and March of 2023. "
            "Get the current balance of his business savings account 'acc_sav_24002'. "
            "Update his business contact information to the email 'ade.adebayor.biz@example.ng' and phone '+234 801 999 8888'. "
            "Next, register a new key supplier as a beneficiary with ID 'bene_user_058_lagos_port' for 'Lagos Port Services', "
            "with account number '0123456789' at 'GTBank' (routing: 'N/A') in 'Nigeria'. "
            "Finally, submit a ticket with ID 'ticket_user_058_annual_audit' under category 'Audit', priority 'High', via 'Internal System', "
            "with the request details: 'Annual audit for business account acc_chk_24001 complete. Full history and Q1 expenses reviewed. Contact info and beneficiary list updated.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "id_document": "uY143801"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_24001", "days": 365}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_24001", "month": "2023-01"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_24001", "month": "2023-02"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_24001", "month": "2023-03"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_24002"}),
            Action(name="update_customer_email", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "new_email": "ade.adebayor.biz@example.ng", "new_phone": "+234 801 999 8888"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                "beneficiary_id": "bene_user_058_lagos_port",
                "beneficiary_name": "Lagos Port Services",
                "country": "Nigeria",
                "bank_details": {"account_number": "0123456789", "bank_name": "GTBank", "routing_info": "N/A"}
            }),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                "ticket_id": "ticket_user_058_annual_audit",
                "category": "Audit",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Annual audit for business account acc_chk_24001 complete. Full history and Q1 expenses reviewed. Contact info and beneficiary list updated."
            }),
        ],
        outputs=[
            "Identity verified for Adetokunbo Adebayor and full year transaction history retrieved.",
            "Q1 2023 expenses aggregated and savings account balance checked.",
            "Business contact information was updated.",
            "A new supplier beneficiary was registered and a high-priority audit ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_059",
        instruction=(
            "Perform a simple information and update task for the retired customer Elena Popescu (ID: c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24). "
            "First, get her profile and verify her identity using her passport 'eE125799'. "
            "Retrieve the current balance of her savings account 'acc_sav_25001'. "
            "Update her contact information to the new email 'elena.p.retired@example.ro' and a new phone number '+40 21 987 65 43'. "
            "Next, update her account preferences to set her communication channel to 'Mail', as requested. "
            "List her beneficiaries to confirm she has none set up. "
            "Finally, submit a low-priority support ticket with ID 'ticket_user_059_profile_update' under category 'Account Management' via 'Internal System' "
            "with the request details: 'Customer contact info and preferences updated as per request.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "id_document": "eE125799"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_25001"}),
            Action(name="update_customer_email", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "new_email": "elena.p.retired@example.ro", "new_phone": "+40 21 987 65 43"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "preferences": {"communication_channel": "Mail"}}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                "ticket_id": "ticket_user_059_profile_update",
                "category": "Account Management",
                "priority": "Low",
                "channel": "Internal System",
                "request_details": "Customer contact info and preferences updated as per request."
            }),
        ],
        outputs=[
            "Identity verified for Elena Popescu and savings account balance retrieved.",
            "Customer's email and phone number were updated.",
            "Account preferences were set to 'Mail' communication.",
            "Beneficiary list was confirmed to be empty and a low-priority ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_060",
        instruction=(
            "Handle a transaction dispute for customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "He is disputing a charge on his credit card 'acc_crd_1003'. First, get his profile and verify his identity using his passport 'lF146011'. "
            "Retrieve the transaction history for the credit card for the past two years. The customer identifies the fraudulent transaction as 'txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c', a charge of $250.00 from Amazon. "
            "Aggregate the expenses for the credit card for October 2023 to provide context. "
            "Next, submit a detailed dispute ticket with ID 'ticket_user_060_dispute' to the 'Dispute' category with 'High' priority via 'Web Portal'. "
            "The request must target 'Transaction' entity 'txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c' for operation 'CHARGEBACK', with the note: 'Customer states they did not authorize this $250.00 purchase from Amazon.' "
            "As a precaution, freeze the credit card account 'acc_crd_1003' with the reason 'Dispute filed for fraudulent charge. Awaiting investigation.' "
            "Finally, update the customer's contact information to the email 'john.doe.dispute@example.com' and confirm his existing phone number '123-456-7890' to ensure he receives all communication regarding this case."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_crd_1003", "days": 730}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_crd_1003", "month": "2023-10"}),
            Action(name="submit_support_ticket", kwargs={
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
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_crd_1003", "alert_reason": "Dispute filed for fraudulent charge. Awaiting investigation."}),
            Action(name="update_customer_email", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "new_email": "john.doe.dispute@example.com", "new_phone": "123-456-7890"}),
        ],
        outputs=[
            "Identity verified for John Doe and credit card history reviewed.",
            "A high-priority dispute ticket was submitted for transaction 'txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c'.",
            "The credit card account 'acc_crd_1003' was frozen as a security precaution.",
            "The customer's contact information was updated to ensure communication on the dispute case.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_061",
        instruction=(
            "Execute a full account consolidation and closure for customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "First, get his profile and verify his identity using his passport 'lF146011'. "
            "He wants to close his credit card and checking accounts, and consolidate all funds into his savings account 'acc_sav_1002'. "
            "Get the balances of his credit card 'acc_crd_1003' (-$2500) and checking account 'acc_chk_1001' ($5230.50). "
            "First, transfer $2500.00 from the checking account to pay off the credit card. "
            "After the debt is clear, transfer the entire remaining balance of $2730.50 from the checking account to the savings account 'acc_sav_1002'. "
            "Cancel his scheduled payment with ID 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d'. "
            "Once the accounts have a zero balance, submit requests to close the credit card 'acc_crd_1003' and the checking account 'acc_chk_1001'. "
            "Finally, submit a ticket with ID 'ticket_user_061_closure' under category 'Account Closure', priority 'Critical', via 'Internal System', "
            "with the request details: 'Full relationship closure process started. Credit and checking accounts closed. Customer requests an agent call to close the final savings account and disburse remaining funds.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_crd_1003", "amount": 2500.00}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_sav_1002", "amount": 2730.50}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="close_account_request", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="close_account_request", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_061_closure",
                "category": "Account Closure",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Full relationship closure process started. Credit and checking accounts closed. Customer requests an agent call to close the final savings account and disburse remaining funds."
            }),
        ],
        outputs=[
            "Identity verified for John Doe and account balances checked.",
            "Credit card debt of $2500 was paid off using funds from the checking account.",
            "The remaining balance from the checking account was consolidated into savings.",
            "The credit card and checking accounts were submitted for closure and a critical ticket was logged for final steps.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_062",
        instruction=(
            "Execute the protocol for a deceased customer, John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "First, get his profile. A death certificate has been provided; verify the customer's status using the document number 'DE-CERT-123456'. "
            "Immediately freeze all of the customer's accounts to secure the estate: checking 'acc_chk_1001', savings 'acc_sav_1002', and credit card 'acc_crd_1003'. "
            "The reason for all freezes should be 'Account holder deceased. Pending estate settlement.' "
            "Next, cancel all active scheduled payments associated with his accounts. This includes the payment with ID 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d' and "
            "the payment with ID 'sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e'. "
            "Finally, submit a support ticket with ID 'ticket_user_062_deceased' to the 'Estate Management' category with 'Critical' priority via 'Internal System', "
            "with the request details: 'Deceased customer protocol executed for John Doe. All accounts frozen and scheduled payments canceled. Awaiting contact from executor.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "DE-CERT-123456"}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_chk_1001", "alert_reason": "Account holder deceased. Pending estate settlement."}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_sav_1002", "alert_reason": "Account holder deceased. Pending estate settlement."}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_crd_1003", "alert_reason": "Account holder deceased. Pending estate settlement."}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_062_deceased",
                "category": "Estate Management",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Deceased customer protocol executed for John Doe. All accounts frozen and scheduled payments canceled. Awaiting contact from executor."
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
            "Perform a detailed beneficiary audit for customer David Chen (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) on his checking account 'acc_chk_3001'. "
            "First, get his profile and verify his identity using his driver's license 'VI933872'. "
            "Next, list the beneficiaries for David Chen. He has one, 'Metropolis Power & Light' (ID: bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a); remove this beneficiary. "
            "After removal, register two new beneficiaries. The first has ID 'bene_user_063_ny_invest' for 'New York Investments', with account number '987654321' at 'Bank of NY' (routing: '021000018') in the 'USA'. "
            "The second has ID 'bene_user_063_chen_trust' for 'Chen Family Trust', with account number '112233445' at 'Chase Bank' (routing: '021000021') in the 'USA'. "
            "Finally, submit a ticket with ID 'ticket_user_063_restructure' under category 'Account Management', priority 'High', via 'Internal System', "
            "with the request details: 'Beneficiary audit complete: beneficiary Metropolis Power & Light replaced with New York Investments and Chen Family Trust.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "VI933872"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_id": "bene_user_063_ny_invest",
                "beneficiary_name": "New York Investments",
                "country": "USA",
                "bank_details": {"account_number": "987654321", "bank_name": "Bank of NY", "routing_info": "021000018"}
            }),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_id": "bene_user_063_chen_trust",
                "beneficiary_name": "Chen Family Trust",
                "country": "USA",
                "bank_details": {"account_number": "112233445", "bank_name": "Chase Bank", "routing_info": "021000021"}
            }),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "ticket_user_063_restructure",
                "category": "Account Management",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Beneficiary audit complete: beneficiary Metropolis Power & Light replaced with New York Investments and Chen Family Trust."
            }),
        ],
        outputs=[
            "Identity of primary holder David Chen verified.",
            "Beneficiary list was updated: 'Metropolis Power & Light' was removed.",
            "Two new beneficiaries, 'New York Investments' and 'Chen Family Trust', were registered.",
            "A high-priority ticket was logged to document the beneficiary audit.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_064",
        instruction=(
            "Perform a simple profile update and loan check for customer Liam O'Connor (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11). "
            "First, get his profile and verify his identity using his passport 'Se620000'. "
            "Update his contact information to the new email 'liam.oconnor.farm@example.ie' and new phone number '+353 87 999 8888'. "
            "Next, summarize the status of his loan applications to check on his active business loan 'loan_biz_005'. "
            "Get the current balance of his checking account 'acc_chk_12001'. "
            "List his current beneficiaries to confirm his setup. "
            "Finally, update his account preferences to enable paperless billing."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "id_document": "Se620000"}),
            Action(name="update_customer_email", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "new_email": "liam.oconnor.farm@example.ie", "new_phone": "+353 87 999 8888"}),
            Action(name="summarize_loan_applications_by_status", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_12001"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "preferences": {"paperless_billing": True}}),
        ],
        outputs=[
            "Identity verified for Liam O'Connor.",
            "Customer's contact information was updated.",
            "Loan status was summarized and checking account balance was retrieved.",
            "Beneficiary list was checked and account preferences were updated to paperless billing.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_065",
        instruction=(
            "Assist customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) with consolidating his beneficiary list and reviewing his recent spending from account 'acc_chk_1001'. "
            "Current date is 2025-07-24. First, get his profile and verify his identity using his passport 'lF146011'. "
            "List his beneficiaries. He wants to remove his two existing beneficiaries: 'Jane Smith' (ID: bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d) and 'Anytown Utility Services' (ID: bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e). "
            "After removing them, register one new consolidated beneficiary with ID 'bene_user_065_doe_trust' for the 'Doe Family Trust', "
            "with account number '102030405' at 'Bank of America' (routing: '026009593') in the 'USA'. "
            "Next, retrieve his transaction history for the last 60 days from his checking account 'acc_chk_1001'. "
            "Aggregate his expenses for the last full month, June 2025. "
            "Finally, submit a ticket with ID 'ticket_user_065_bene_consolidation' under category 'Account Management', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Beneficiary list consolidated to single Doe Family Trust. Recent spending review also provided to customer.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "beneficiary_id": "bene_user_065_doe_trust",
                "beneficiary_name": "Doe Family Trust",
                "country": "USA",
                "bank_details": {"account_number": "102030405", "bank_name": "Bank of America", "routing_info": "026009593"}
            }),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_1001", "days": 60}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_1001", "month": "2025-06"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_065_bene_consolidation",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Beneficiary list consolidated to single Doe Family Trust. Recent spending review also provided to customer."
            }),
        ],
        outputs=[
            "Identity verified for John Doe.",
            "Both existing beneficiaries, Jane Smith and Anytown Utility Services, were removed.",
            "A new consolidated beneficiary, 'Doe Family Trust', was successfully registered.",
            "Recent spending was reviewed and a ticket was logged to confirm the beneficiary consolidation.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_066",
        instruction=(
            "Execute a full financial and security review for the high-net-worth client David Chen (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "First, get his profile and verify his identity using his driver's license 'VI933872'. "
            "Retrieve the transaction history for his checking account 'acc_chk_3001' for the last 180 days and aggregate his expenses for October 2023. "
            "Also, get the current balance of his investment account 'acc_inv_3002'. "
            "As a security measure, temporarily freeze the investment account 'acc_inv_3002' with the reason 'Pending customer confirmation for annual review.' "
            "Update David Chen's primary contact information to email 'd.chen.office@example.com' and phone '555-987-2222'. "
            "Finally, submit a ticket with ID 'ticket_user_066_annual_review' under category 'Audit', priority 'High', via 'Internal System', "
            "with the request details: 'Annual review complete. Financials reviewed, investment account temporarily frozen, and contact info updated.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "VI933872"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_3001", "days": 180}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_3001", "month": "2023-10"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_inv_3002"}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_inv_3002", "alert_reason": "Pending customer confirmation for annual review."}),
            Action(name="update_customer_email", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "new_email": "d.chen.office@example.com", "new_phone": "555-987-2222"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "ticket_user_066_annual_review",
                "category": "Audit",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Annual review complete. Financials reviewed, investment account temporarily frozen, and contact info updated."
            }),
        ],
        outputs=[
            "Identity verified for David Chen and a 180-day financial review of his checking account was completed.",
            "The balance of his investment account was retrieved and the account was temporarily frozen for security.",
            "The customer's contact information was updated and a high-priority audit ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_067",
        instruction=(
            "Assist international customer Chloe Dubois (ID: e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2) with updating her payment arrangements. "
            "First, get her profile and verify her identity using her driver's license 'im665671'. "
            "She wants to cancel the monthly scheduled payment to her mother, which has the ID 'sp_a2c1d9b3-f6a5-b4c3-d2e1-f0a9b8c7d6e5'. "
            "Next, update her beneficiary list. List her current beneficiaries and then remove her mother, Marie Dubois (ID: bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c). "
            "After that, register a new international beneficiary with ID 'bene_user_067_nyc_school' for the 'NYC Art School', "
            "with account number '987654321' at 'Bank of NY' (routing: '021000018') in the 'USA'. "
            "Update her account preferences to use the 'App' as her primary communication channel. "
            "Finally, submit a support ticket with ID 'ticket_user_067_bene_update' under category 'Beneficiary Management', priority 'Medium', via 'Email', "
            "with the request details: 'Canceled scheduled payment to Marie Dubois and updated beneficiary list to replace her with NYC Art School.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "id_document": "im665671"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_a2c1d9b3-f6a5-b4c3-d2e1-f0a9b8c7d6e5"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "beneficiary_id": "bene_user_067_nyc_school",
                "beneficiary_name": "NYC Art School",
                "country": "USA",
                "bank_details": {"account_number": "987654321", "bank_name": "Bank of NY", "routing_info": "021000018"}
            }),
            Action(name="update_account_preferences", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "preferences": {"communication_channel": "App"}}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "ticket_id": "ticket_user_067_bene_update",
                "category": "Beneficiary Management",
                "priority": "Medium",
                "channel": "Email",
                "request_details": "Canceled scheduled payment to Marie Dubois and updated beneficiary list to replace her with NYC Art School."
            }),
        ],
        outputs=[
            "Identity verified for Chloe Dubois.",
            "The scheduled payment to her mother was successfully canceled.",
            "Beneficiary list was updated: Marie Dubois was removed and 'NYC Art School' was added.",
            "Account preferences were updated and a support ticket was logged to confirm the changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_068",
        instruction=(
            "Reconfigure the joint account 'acc_chk_2001' by swapping one of the holders. The primary holder is Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef). "
            "The holder to be removed is represented by the ID 'cust_joint_005'. The new holder to be added is David Chen (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "First, get Jane Smith's profile and verify her identity using her national ID 'jd195515'. "
            "Then, get David Chen's profile and verify his identity using his national ID 'pI260068'. "
            "Proceed to remove the joint holder 'cust_joint_005' and then add David Chen as the new joint holder. "
            "After updating the holders, list Jane Smith's beneficiaries. Her beneficiary is John Doe (ID: bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f); remove him. "
            "Register the new joint holder, David Chen, as the primary beneficiary with ID 'bene_user_068_d_chen', using his account number '6666' at 'City General Bank' (routing: 'N/A') in the 'USA'. "
            "Update the account preferences to use 'SMS' for notifications. "
            "Finally, submit a ticket with ID 'ticket_user_068_reconfig' under category 'Account Management', priority 'High', via 'Internal System', "
            "with the request details: 'Joint account acc_chk_2001 reconfigured. Holder cust_joint_005 replaced with David Chen. Beneficiary list updated.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="get_customer_profile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "pI260068"}),
            Action(name="remove_joint_account_holder", kwargs={"account_id": "acc_chk_2001", "holder_id": "cust_joint_005"}),
            Action(name="add_joint_account_holder", kwargs={"account_id": "acc_chk_2001", "holder_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_user_068_d_chen",
                "beneficiary_name": "David Chen",
                "country": "USA",
                "bank_details": {"account_number": "6666", "bank_name": "City General Bank", "routing_info": "N/A"}
            }),
            Action(name="update_account_preferences", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "preferences": {"communication_channel": "SMS"}}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_068_reconfig",
                "category": "Account Management",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Joint account acc_chk_2001 reconfigured. Holder cust_joint_005 replaced with David Chen. Beneficiary list updated."
            }),
        ],
        outputs=[
            "Identities of primary holder Jane Smith and new joint holder David Chen verified.",
            "Joint holder for account acc_chk_2001 was successfully swapped.",
            "Beneficiary John Doe was removed and replaced with the new joint holder, David Chen.",
            "Account preferences were updated and a high-priority ticket was logged to document the reconfiguration.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_069",
        instruction=(
            "Perform a simple information retrieval task for customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) for his personal records. "
            "First, get his profile and verify his identity using his passport 'lF146011'. "
            "Retrieve the balances for his checking account 'acc_chk_1001' and his savings account 'acc_sav_1002'. "
            "Next, summarize the status of his loan applications. "
            "Then, list all his current beneficiaries. "
            "Finally, submit a low-priority support ticket with ID 'ticket_user_069_info_review' under category 'General Inquiry' via 'Web Portal' "
            "with the request details: 'Customer requested a full summary of his accounts, loans, and beneficiaries for his records. Review complete.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="summarize_loan_applications_by_status", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_069_info_review",
                "category": "General Inquiry",
                "priority": "Low",
                "channel": "Web Portal",
                "request_details": "Customer requested a full summary of his accounts, loans, and beneficiaries for his records. Review complete."
            }),
        ],
        outputs=[
            "Identity verified for John Doe.",
            "Balances for his checking and savings accounts were retrieved.",
            "A summary of his loan status was provided.",
            "A list of his current beneficiaries was retrieved and a ticket was logged to confirm the review.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_070",
        instruction=(
            "Assist customer Liam O'Connor (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11) with making an extra payment on his business loan. "
            "First, get his profile and verify his identity using his passport 'Se620000'. "
            "Summarize his loan application status to confirm details of his active loan. "
            "Retrieve the current balances of his checking account 'acc_chk_12001' and his loan account 'acc_loan_12002'. "
            "He wishes to make an extra payment of 2000 EUR. Transfer this amount from his checking account 'acc_chk_12001' to his loan account 'acc_loan_12002'. "
            "After the transfer, update his primary contact information to email 'liam.o.updates@example.ie' and phone '+353 87 111 2222'. "
            "Finally, submit a support ticket with ID 'ticket_user_070_loan_payment' under category 'Loan Support', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Customer made a one-time extra payment of 2000 EUR to business loan account acc_loan_12002.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "id_document": "Se620000"}),
            Action(name="summarize_loan_applications_by_status", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_12001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_loan_12002"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_12001", "to_account": "acc_loan_12002", "amount": 2000.00}),
            Action(name="update_customer_email", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "new_email": "liam.o.updates@example.ie", "new_phone": "+353 87 111 2222"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "ticket_id": "ticket_user_070_loan_payment",
                "category": "Loan Support",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Customer made a one-time extra payment of 2000 EUR to business loan account acc_loan_12002."
            }),
        ],
        outputs=[
            "Identity verified for Liam O'Connor and loan status confirmed.",
            "Balances for checking and loan accounts were retrieved.",
            "An extra payment of 2000 EUR was successfully transferred to the loan account.",
            "Customer contact information was updated and a ticket was logged to document the payment.",
        ],
    ),
     Task(
        annotator="0",
        user_id="user_071",
        instruction=(
            "Execute a full account consolidation for customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "Current date is 2025-07-24. First, get his profile and verify his identity using his passport 'lF146011'. "
            "He wants to consolidate funds from his checking account 'acc_chk_1001' into his savings account 'acc_sav_1002' and then close the checking account. "
            "Begin by retrieving the transaction history for the checking account for the last 60 days and aggregating his expenses for June 2025. "
            "Next, get the current balance of both the checking account 'acc_chk_1001' (balance is $5230.50) and the savings account 'acc_sav_1002'. "
            "Transfer the entire balance of $5230.50 from the checking account to the savings account. "
            "Once the transfer is complete and the checking account is empty, submit a request to close the checking account 'acc_chk_1001'. "
            "Finally, submit a ticket with ID 'ticket_user_071_consolidation' under category 'Account Closure', priority 'High', via 'Web Portal', "
            "with the request details: 'Customer account consolidation complete. Full balance from acc_chk_1001 transferred to acc_sav_1002. Checking account submitted for closure.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_1001", "days": 60}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_1001", "month": "2025-06"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_sav_1002", "amount": 5230.50}),
            Action(name="close_account_request", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_071_consolidation",
                "category": "Account Closure",
                "priority": "High",
                "channel": "Web Portal",
                "request_details": "Customer account consolidation complete. Full balance from acc_chk_1001 transferred to acc_sav_1002. Checking account submitted for closure."
            }),
        ],
        outputs=[
            "Identity verified for John Doe and a spending review on his checking account was performed.",
            "Balances for both checking and savings accounts were retrieved.",
            "The full balance from the checking account was successfully transferred to the savings account.",
            "The checking account was submitted for closure and a high-priority ticket was logged to document the consolidation.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_072",
        instruction=(
            "Update security settings and international beneficiaries for customer Hans Müller (ID: d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). "
            "First, get his profile and verify his identity using his driver's license 'Kt516858'. "
            "Update his account preferences to enable all notifications and set his language preference to 'de-DE'. "
            "Next, he wants to update his beneficiary list. List his current beneficiaries and then remove the existing one, 'Klaus Schmidt' (ID: bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a). "
            "After removal, register a new international beneficiary with ID 'bene_user_072_paris_art' for 'Paris Art Supplies', "
            "with account IBAN 'FR7630002005500000157845Z25' at 'Societe Generale' (BIC: 'SOGEFRPP') in 'France'. "
            "Get the current balance of his checking account 'acc_chk_8001'. "
            "Finally, submit a ticket with ID 'ticket_user_072_updates' under category 'Account Management', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Customer security preferences and language updated. Beneficiary list updated to replace Klaus Schmidt with Paris Art Supplies.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "id_document": "Kt516858"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "preferences": {"notifications": True, "language": "de-DE"}}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "beneficiary_id": "bene_user_072_paris_art",
                "beneficiary_name": "Paris Art Supplies",
                "country": "France",
                "bank_details": {"account_number": "FR7630002005500000157845Z25", "bank_name": "Societe Generale", "routing_info": "SOGEFRPP"}
            }),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "ticket_id": "ticket_user_072_updates",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Customer security preferences and language updated. Beneficiary list updated to replace Klaus Schmidt with Paris Art Supplies."
            }),
        ],
        outputs=[
            "Identity verified for Hans Müller and his account preferences were updated.",
            "Beneficiary 'Klaus Schmidt' was successfully removed.",
            "New international beneficiary 'Paris Art Supplies' was registered.",
            "Checking account balance was confirmed and a ticket was logged to document the updates.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_073",
        instruction=(
            "Execute an emergency security protocol for a suspected account takeover for customer Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef). "
            "A security alert has been triggered. First, get her profile. Then, to protect her assets, immediately freeze both her checking ('acc_chk_2001') and savings ('acc_sav_2002') accounts "
            "with the reason 'Urgent security review due to suspected account takeover.' "
            "After freezing, verify her identity using her national ID 'jd195515' to ensure you are speaking with the real customer. "
            "Once verified, retrieve the transaction history for her checking account 'acc_chk_2001' for the last 7 days to identify potential fraudulent charges. "
            "Her contact info may be compromised, so update it to a new secure email 'jane.smith.recovery@example.com' and phone '555-999-0000'. "
            "Finally, submit a ticket with ID 'ticket_user_073_takeover' under category 'Security', priority 'Critical', via 'Internal System', "
            "with the request details: 'Account takeover protocol initiated. All accounts frozen, contact info secured. Awaiting fraud investigation results.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_chk_2001", "alert_reason": "Urgent security review due to suspected account takeover."}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_sav_2002", "alert_reason": "Urgent security review due to suspected account takeover."}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_2001", "days": 7}),
            Action(name="update_customer_email", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "new_email": "jane.smith.recovery@example.com", "new_phone": "555-999-0000"}),
            Action(name="submit_support_ticket", kwargs={
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
            "Identity of Jane Smith was verified to proceed with recovery.",
            "Recent transaction history was retrieved for fraud analysis.",
            "Customer's contact info was updated to secure channels and a critical security ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_074",
        instruction=(
            "Perform a simple information check and contact update for customer Fatima Al-Fassi (ID: c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6). "
            "First, get her profile and verify her identity using her national ID 'IJ758739'. "
            "Retrieve the current balances for her checking account 'acc_chk_7001' and her savings account 'acc_sav_7002'. "
            "Update her contact information to the new email 'f.alfassi.contact@example.ae' and a new phone number '+971 50 222 3333'. "
            "Then, list her current beneficiaries to provide her with a record. "
            "Finally, submit a low-priority support ticket with ID 'ticket_user_074_info_check' under category 'General Inquiry' via 'Web Portal' "
            "with the request details: 'Customer requested a check of her account balances and beneficiary list. Contact info also updated.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "id_document": "IJ758739"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_7001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_7002"}),
            Action(name="update_customer_email", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "new_email": "f.alfassi.contact@example.ae", "new_phone": "+971 50 222 3333"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "ticket_id": "ticket_user_074_info_check",
                "category": "General Inquiry",
                "priority": "Low",
                "channel": "Web Portal",
                "request_details": "Customer requested a check of her account balances and beneficiary list. Contact info also updated."
            }),
        ],
        outputs=[
            "Identity verified for Fatima Al-Fassi.",
            "Balances for her checking and savings accounts were successfully retrieved.",
            "Her contact information was updated to a new email and phone number.",
            "Her beneficiary list was retrieved and a ticket was logged to confirm the actions.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_075",
        instruction=(
            "Assist customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) with updating his scheduled payments and beneficiaries. "
            "First, get his profile and verify his identity using his passport 'lF146011'. "
            "He wants to cancel two scheduled payments: the one with ID 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d' and the one with ID 'sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e'. "
            "Next, he wants to update his beneficiaries. List his current beneficiaries and then remove 'Anytown Utility Services' (ID: bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e). "
            "After removal, register a new beneficiary with ID 'bene_user_075_new_utility' for 'Metropolis Water Co', "
            "with account number '123456789' at 'Metropolis Bank' (routing: '021200339') in the 'USA'. "
            "Update his account preferences to receive alerts via the 'App'. "
            "Finally, submit a ticket with ID 'ticket_user_075_updates' under category 'Account Management', priority 'Medium', via 'Mobile App', "
            "with the request details: 'Canceled two scheduled payments and updated beneficiary list from Anytown Utility to Metropolis Water Co.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "beneficiary_id": "bene_user_075_new_utility",
                "beneficiary_name": "Metropolis Water Co",
                "country": "USA",
                "bank_details": {"account_number": "123456789", "bank_name": "Metropolis Bank", "routing_info": "021200339"}
            }),
            Action(name="update_account_preferences", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "preferences": {"communication_channel": "App"}}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_075_updates",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Mobile App",
                "request_details": "Canceled two scheduled payments and updated beneficiary list from Anytown Utility to Metropolis Water Co."
            }),
        ],
        outputs=[
            "Identity verified for John Doe.",
            "Two scheduled payments were successfully canceled.",
            "Beneficiary 'Anytown Utility Services' was removed and replaced with 'Metropolis Water Co'.",
            "Account preferences were updated and a ticket was logged to confirm all changes.",
        ],
    ),
     Task(
        annotator="0",
        user_id="user_076",
        instruction=(
            "Execute a complex separation of the joint account 'acc_chk_2001' following a divorce settlement. The primary holder is Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef), and the joint holder to be removed is John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), listed as holder ID 'cust_joint_005'. "
            "First, get the profiles for both Jane Smith and John Doe, and verify their identities using their respective documents: national ID 'jd195515' for Jane and passport 'lF146011' for John. "
            "After verification, get the current balance of the joint account 'acc_chk_2001', which is 3100.75 CAD. "
            "Transfer the settlement amount of 1500.00 CAD from 'acc_chk_2001' to John Doe's personal account number '1111'. "
            "Then, remove John Doe ('cust_joint_005') as a joint holder from 'acc_chk_2001'. "
            "Next, update Jane Smith's beneficiary list: list her beneficiaries, then delete the record for John Doe (ID: bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f). "
            "Finally, submit a ticket with ID 'ticket_user_076_divorce_settlement' under category 'Legal', priority 'High', via 'Internal System', "
            "with the request details: 'Divorce settlement protocol executed for account acc_chk_2001. Joint holder cust_joint_005 removed, funds split, and beneficiary list updated as per legal agreement.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_2001", "to_account": "1111", "amount": 1500.00}),
            Action(name="remove_joint_account_holder", kwargs={"account_id": "acc_chk_2001", "holder_id": "cust_joint_005"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_076_divorce_settlement",
                "category": "Legal",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Divorce settlement protocol executed for account acc_chk_2001. Joint holder cust_joint_005 removed, funds split, and beneficiary list updated as per legal agreement."
            }),
        ],
        outputs=[
            "Identities of both Jane Smith and John Doe were successfully verified.",
            "A settlement amount of 1500.00 CAD was transferred from the joint account to John Doe's personal account.",
            "John Doe was removed as a joint holder from account acc_chk_2001.",
            "John Doe was removed from Jane Smith's beneficiary list and a high-priority legal ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_077",
        instruction=(
            "Assist customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) in setting up a new international payment arrangement from his account 'acc_chk_1001'. "
            "First, get his profile and verify his identity using his passport 'lF146011'. "
            "He is replacing a domestic bill payment. Cancel his scheduled monthly payment to Anytown Utility, which has the ID 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d'. "
            "Next, list his beneficiaries and remove the 'Anytown Utility Services' beneficiary (ID: bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e). "
            "Then, register a new international supplier with ID 'bene_user_077_uk_supplier' for 'London Imports Ltd', "
            "with account number 'GB29NWBK60161331926819' at 'NatWest' (routing: 'NWBKGB2L') in the 'United Kingdom'. "
            "Check the balance of the source account 'acc_chk_1001' to ensure funds are available for future payments. "
            "Finally, submit a ticket with ID 'ticket_user_077_intl_setup' under category 'Payments', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Replaced domestic beneficiary Anytown Utility with international beneficiary London Imports Ltd and canceled original scheduled payment.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "beneficiary_id": "bene_user_077_uk_supplier",
                "beneficiary_name": "London Imports Ltd",
                "country": "United Kingdom",
                "bank_details": {"account_number": "GB29NWBK60161331926819", "bank_name": "NatWest", "routing_info": "NWBKGB2L"}
            }),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_077_intl_setup",
                "category": "Payments",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Replaced domestic beneficiary Anytown Utility with international beneficiary London Imports Ltd and canceled original scheduled payment."
            }),
        ],
        outputs=[
            "Identity verified for John Doe.",
            "The scheduled payment to 'Anytown Utility' was canceled and the beneficiary was removed.",
            "A new international beneficiary, 'London Imports Ltd', was successfully registered.",
            "The checking account balance was confirmed and a ticket was logged documenting the changes.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_078",
        instruction=(
            "Execute a detailed security audit for customer Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef) following a small suspicious transaction alert. "
            "Current date is 2025-07-24. First, get her profile and verify her identity using her national ID 'jd195515'. "
            "Immediately freeze her checking account 'acc_chk_2001' with the reason 'Suspicious transaction detected, account under review.' "
            "Then, conduct a review of her spending patterns by retrieving the full transaction history for 'acc_chk_2001' and aggregating her expenses for April, May, and June of 2025. "
            "As a security precaution, update her contact info to a secure secondary email 'jane.smith.sec.2@example.com' and phone '555-222-1111'. "
            "Finally, submit a ticket with ID 'ticket_user_078_sec_audit' under category 'Security', priority 'Critical', via 'Internal System', "
            "with the request details: 'Security audit triggered. Account acc_chk_2001 frozen, spending patterns reviewed, and contact info secured.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_chk_2001", "alert_reason": "Suspicious transaction detected, account under review."}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_2001", "month": "2025-04"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_2001", "month": "2025-05"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_2001", "month": "2025-06"}),
            Action(name="update_customer_email", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "new_email": "jane.smith.sec.2@example.com", "new_phone": "555-222-1111"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_078_sec_audit",
                "category": "Security",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Security audit triggered. Account acc_chk_2001 frozen, spending patterns reviewed, and contact info secured."
            }),
        ],
        outputs=[
            "Identity verified for Jane Smith and her checking account was frozen.",
            "A 3-month spending review was conducted on the checking account.",
            "Customer's contact information was updated to secure channels.",
            "A critical security ticket was logged to document the audit and security measures taken.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_079",
        instruction=(
            "Perform a simple information retrieval task for customer David Chen (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "First, get his profile and verify his identity using his national ID 'pI260068'. "
            "Then, retrieve the current balances of his checking account 'acc_chk_3001' and his investment account 'acc_inv_3002'. "
            "Next, summarize the status of his loan applications; he has an active mortgage with ID 'loan_mort_001'. "
            "List his current beneficiaries for his review. "
            "Finally, update his account preferences to ensure notifications are enabled."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "pI260068"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_3001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_inv_3002"}),
            Action(name="summarize_loan_applications_by_status", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "preferences": {"notifications": True}}),
        ],
        outputs=[
            "Identity verified for David Chen.",
            "Balances for his checking and investment accounts were successfully retrieved.",
            "His loan application status was summarized and his beneficiaries were listed.",
            "His account preferences were updated to enable notifications.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_080",
        instruction=(
            "Assist customer Chloe Dubois (ID: e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2) with managing her credit card account 'acc_crd_9002'. "
            "First, get her profile and verify her identity using her driver's license 'im665671'. "
            "Retrieve the balance of her credit card 'acc_crd_9002', which is -500.00 EUR. "
            "Also retrieve the balance of her checking account 'acc_chk_9001'. "
            "She wants to pay the credit card in full. Transfer 500.00 EUR from her checking account to her credit card account. "
            "After the payment is made, update her primary contact information to email 'chloe.d.primary@example.fr' and phone '+33 6 12 34 55 55'. "
            "Finally, submit a ticket with ID 'ticket_user_080_cc_payment' under category 'Payments', priority 'Low', via 'Mobile App', "
            "with the request details: 'Customer paid off credit card acc_crd_9002 in full and updated primary contact details.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "id_document": "im665671"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_crd_9002"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_9001"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_9001", "to_account": "acc_crd_9002", "amount": 500.00}),
            Action(name="update_customer_email", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "new_email": "chloe.d.primary@example.fr", "new_phone": "+33 6 12 34 55 55"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "ticket_id": "ticket_user_080_cc_payment",
                "category": "Payments",
                "priority": "Low",
                "channel": "Mobile App",
                "request_details": "Customer paid off credit card acc_crd_9002 in full and updated primary contact details."
            }),
        ],
        outputs=[
            "Identity verified for Chloe Dubois and account balances were checked.",
            "A payment of 500.00 EUR was transferred from checking to pay off the credit card.",
            "Customer's primary contact information was updated.",
            "A ticket was logged to confirm the payment and contact update.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_081",
        instruction=(
            "Handle a transaction dispute on the joint account 'acc_chk_2001'. The primary holder, Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef), has reported a fraudulent charge. The other joint holder is John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "First, get the profiles for both Jane Smith and John Doe. Verify Jane's identity with her national ID 'jd195515' and John's identity with his passport 'lF146011'. "
            "Immediately freeze the joint account 'acc_chk_2001' with the reason 'Dispute filed by primary holder; account under investigation.' "
            "Retrieve the transaction history for the account for the last 30 days. The disputed transaction is identified as 'txn_0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d'. "
            "Submit a detailed dispute ticket with ID 'ticket_user_081_joint_dispute' to the 'Dispute' category with 'Critical' priority via 'Internal System'. "
            "The request must target 'Transaction' entity 'txn_0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d' for operation 'CHARGEBACK', with the note: 'Primary holder Jane Smith disputes this charge on the joint account.' "
            "As a final step, update Jane Smith's primary contact information to email 'jane.s.dispute@example.com' and phone '555-123-1122'."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_chk_2001", "alert_reason": "Dispute filed by primary holder; account under investigation."}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_2001", "days": 30}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_081_joint_dispute",
                "category": "Dispute",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": {
                    "target_entity": "Transaction",
                    "target_id": "txn_0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
                    "operation": "CHARGEBACK",
                    "parameters": {"note": "Primary holder Jane Smith disputes this charge on the joint account."}
                }
            }),
            Action(name="update_customer_email", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "new_email": "jane.s.dispute@example.com", "new_phone": "555-123-1122"}),
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
            "Assist customer Fatima Al-Fassi (ID: c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6) in preparing her accounts for a long vacation. "
            "First, get her profile and verify her identity using her national ID 'IJ758739'. "
            "She wants to suspend a large quarterly payment; cancel the scheduled payment with ID 'sp_a2c1d9b3-d2e1-f0a9-b8c7-d6e5f4a3b2c1'. "
            "As an additional security measure, freeze her savings account 'acc_sav_7002' with the exact reason: 'Customer on extended travel; account frozen for security.' "
            "Update her account preferences to use 'SMS' for critical alerts. "
            "Finally, submit a ticket with ID 'ticket_user_082_travel' under category 'Account Management', priority 'High', via 'Internal System', "
            "with the request details: 'Travel Notice: Canceled scheduled payment and froze savings account for security during travel.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "id_document": "IJ758739"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_a2c1d9b3-d2e1-f0a9-b8c7-d6e5f4a3b2c1"}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_sav_7002", "alert_reason": "Customer on extended travel; account frozen for security."}),
            Action(name="update_account_preferences", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "preferences": {"communication_channel": "SMS"}}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "ticket_id": "ticket_user_082_travel",
                "category": "Account Management",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Travel Notice: Canceled scheduled payment and froze savings account for security during travel."
            }),
        ],
        outputs=[
            "Identity verified for Fatima Al-Fassi.",
            "A large scheduled payment was successfully canceled.",
            "Her savings account was frozen for security and preferences were updated for travel alerts.",
            "A high-priority travel notice ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_083",
        instruction=(
            "Perform a detailed Q2 2025 financial audit for the business account of customer Adetokunbo Adebayor (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23). "
            "Current date is 2025-07-24. Get his profile and verify his identity using his national ID 'uY143801'. "
            "Retrieve the transaction history for his business checking account 'acc_chk_24001' for the last 90 days. "
            "Then, aggregate the monthly expenses for that account for April, May, and June of 2025. "
            "List his beneficiaries. He has none. Register a new key supplier with ID 'bene_user_083_logistics' for 'Nigerian Logistics Corp', "
            "with account number '9876543210' at 'Zenith Bank' (routing: 'N/A') in 'Nigeria'. "
            "Update the primary business contact information to email 'adebayor.biz.primary@example.ng' and phone '+234 801 222 3333'. "
            "Finally, submit a ticket with ID 'ticket_user_083_q2_audit' under category 'Audit', priority 'High', via 'Internal System', "
            "with the request details: 'Q2 2025 audit for business account acc_chk_24001 complete. Expenses for 3 months aggregated. New supplier beneficiary added and contact info updated.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "id_document": "uY143801"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_24001", "days": 90}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_24001", "month": "2025-04"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_24001", "month": "2025-05"}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_24001", "month": "2025-06"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                "beneficiary_id": "bene_user_083_logistics",
                "beneficiary_name": "Nigerian Logistics Corp",
                "country": "Nigeria",
                "bank_details": {"account_number": "9876543210", "bank_name": "Zenith Bank", "routing_info": "N/A"}
            }),
            Action(name="update_customer_email", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "new_email": "adebayor.biz.primary@example.ng", "new_phone": "+234 801 222 3333"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                "ticket_id": "ticket_user_083_q2_audit",
                "category": "Audit",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Q2 2025 audit for business account acc_chk_24001 complete. Expenses for 3 months aggregated. New supplier beneficiary added and contact info updated."
            }),
        ],
        outputs=[
            "Identity verified for Adetokunbo Adebayor and a Q2 2025 financial review was conducted.",
            "Expenses for April, May, and June were aggregated.",
            "A new supplier beneficiary was added to the business profile.",
            "The primary business contact information was updated and a high-priority audit ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_084",
        instruction=(
            "Perform a simple profile update and balance check for customer Kenji Tanaka (ID: f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3). "
            "First, get his profile and verify his identity using his national ID 'nh464131'. "
            "Update his email to 'kenji.t.personal@example.jp' and his phone number to '+81 90-1111-2222'. "
            "Then, update his account preferences to set his language to 'ja-JP'. "
            "Retrieve the current balances of his checking account 'acc_chk_10001' and his savings account 'acc_sav_10002'. "
            "Finally, submit a low-priority support ticket with ID 'ticket_user_084_profile_updates' under category 'Account Management' via 'Email' "
            "with the request details: 'Customer profile updated with new contact info and language preference.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "id_document": "nh464131"}),
            Action(name="update_customer_email", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "new_email": "kenji.t.personal@example.jp", "new_phone": "+81 90-1111-2222"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "preferences": {"language": "ja-JP"}}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_10001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_10002"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "ticket_id": "ticket_user_084_profile_updates",
                "category": "Account Management",
                "priority": "Low",
                "channel": "Email",
                "request_details": "Customer profile updated with new contact info and language preference."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka.",
            "The customer's contact email and phone number were successfully updated.",
            "The customer's language preference was set to Japanese.",
            "Balances for checking and savings accounts were retrieved and a ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_085",
        instruction=(
            "Assist customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) with consolidating his beneficiaries and making a payment from his account 'acc_chk_1001'. "
            "First, get his profile and verify his identity using his passport 'lF146011'. "
            "List his beneficiaries, then remove his two existing ones: 'Jane Smith' (ID: bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d) and 'Anytown Utility Services' (ID: bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e). "
            "After removing them, register one new consolidated beneficiary with ID 'bene_user_085_doe_trust' for the 'Doe Family Trust', "
            "with account number '102030405' at 'Bank of America' (routing: '026009593') in the 'USA'. "
            "Get the current balance of the checking account 'acc_chk_1001'. "
            "Then, transfer $2,500.00 from the checking account to the new 'Doe Family Trust' beneficiary's account number '102030405'. "
            "Finally, submit a ticket with ID 'ticket_user_085_consolidation' under category 'Beneficiary Management', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Beneficiary list consolidated to the Doe Family Trust and an initial transfer of $2500 was completed.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "beneficiary_id": "bene_user_085_doe_trust",
                "beneficiary_name": "Doe Family Trust",
                "country": "USA",
                "bank_details": {"account_number": "102030405", "bank_name": "Bank of America", "routing_info": "026009593"}
            }),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_1001", "to_account": "102030405", "amount": 2500.00}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_085_consolidation",
                "category": "Beneficiary Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Beneficiary list consolidated to the Doe Family Trust and an initial transfer of $2500 was completed."
            }),
        ],
        outputs=[
            "Identity verified for John Doe.",
            "His two existing beneficiaries were successfully removed.",
            "A new consolidated beneficiary, 'Doe Family Trust', was registered.",
            "A transfer of $2,500.00 was made to the new beneficiary and a ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_086",
        instruction=(
            "Execute the full closure of a business account for John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), who is winding down his operations. The account to be closed is 'acc_chk_1001'. "
            "First, get his profile and verify his identity using his passport 'lF146011'. "
            "Before closure, all recurring payments must be stopped. Cancel the scheduled payment with ID 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d' and the one with ID 'sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e'. "
            "Next, remove all business beneficiaries. List his beneficiaries, then delete 'Jane Smith' (ID: bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d) and 'Anytown Utility Services' (ID: bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e). "
            "Get the final balance of the business account 'acc_chk_1001', which is $5230.50. "
            "Transfer the full balance to his designated personal external account, with account number '999888777'. "
            "Once the account is empty, submit a request to close the business account 'acc_chk_1001'. "
            "Finally, submit a ticket with ID 'ticket_user_086_biz_closure' under category 'Account Closure', priority 'High', via 'Internal System', "
            "with the request details: 'Business account acc_chk_1001 closure process initiated. All payments and beneficiaries removed, funds transferred, and account submitted for final closure.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "beneficiary_id": "bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_1001", "to_account": "999888777", "amount": 5230.50}),
            Action(name="close_account_request", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_086_biz_closure",
                "category": "Account Closure",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Business account acc_chk_1001 closure process initiated. All payments and beneficiaries removed, funds transferred, and account submitted for final closure."
            }),
        ],
        outputs=[
            "Identity verified for John Doe.",
            "All scheduled payments from the business account have been canceled.",
            "All beneficiaries linked to the business account have been removed.",
            "The remaining balance was transferred and the business account was submitted for closure, with a ticket logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_087",
        instruction=(
            "Assist customer Liam O'Connor (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11) with managing his business loan. "
            "First, get his profile and verify his identity using his passport 'Se620000'. "
            "Summarize his loan application status to confirm the details of his active loan. "
            "Then, get the current balances of his checking account 'acc_chk_12001' and his loan account 'acc_loan_12002'. "
            "He wants to make an extra payment of 4000.00 EUR. Transfer this amount from his checking account to his loan account. "
            "After the payment, update his contact information to email 'liam.oconnor.loan@example.ie' and phone '+353 87 333 4444' for all future loan communications. "
            "Finally, submit a support ticket with ID 'ticket_user_087_refi_inquiry' under category 'Loan Support', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Customer made a 4000 EUR extra payment on loan associated with account acc_loan_12002. Inquiring about refinancing options.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "id_document": "Se620000"}),
            Action(name="summarize_loan_applications_by_status", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_12001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_loan_12002"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_12001", "to_account": "acc_loan_12002", "amount": 4000.00}),
            Action(name="update_customer_email", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "new_email": "liam.oconnor.loan@example.ie", "new_phone": "+353 87 333 4444"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "ticket_id": "ticket_user_087_refi_inquiry",
                "category": "Loan Support",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Customer made a 4000 EUR extra payment on loan associated with account acc_loan_12002. Inquiring about refinancing options."
            }),
        ],
        outputs=[
            "Identity verified for Liam O'Connor and his loan status was confirmed.",
            "Balances for checking and loan accounts were retrieved.",
            "An extra payment of 4000.00 EUR was successfully transferred to his loan account.",
            "The customer's contact information was updated and a ticket was logged with his refinancing inquiry.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_088",
        instruction=(
            "Perform a detailed audit and reconfiguration of the joint account 'acc_chk_2001'. The primary holder is Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef), and the joint holder is John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), listed as holder ID 'cust_joint_005'. "
            "First, get the profiles and verify the identities for both Jane Smith (using national ID 'jd195515') and John Doe (using passport 'lF146011'). "
            "Retrieve the transaction history for the joint account for the last 90 days and aggregate expenses for June 2025. "
            "The account holders are separating. Remove John Doe ('cust_joint_005') as a joint holder. "
            "Next, update Jane Smith's beneficiaries. List them, then remove her only beneficiary, John Doe (ID: bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f). "
            "Register two new beneficiaries for her: the first, with ID 'bene_user_088_parents', is 'Smith Parents Trust' on account '111222333' at 'TD Bank' (routing: 'N/A') in 'Canada'. "
            "The second, with ID 'bene_user_088_charity', is 'Canadian Wildlife Fund' on account '444555666' at 'RBC' (routing: 'N/A') in 'Canada'. "
            "Finally, submit a ticket with ID 'ticket_user_088_reconfig' under category 'Account Management', priority 'High', via 'Internal System', "
            "with the request details: 'Joint account acc_chk_2001 reconfigured to single owner. Holder cust_joint_005 removed. All beneficiaries updated.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_2001", "days": 90}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_2001", "month": "2025-06"}),
            Action(name="remove_joint_account_holder", kwargs={"account_id": "acc_chk_2001", "holder_id": "cust_joint_005"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_user_088_parents", "beneficiary_name": "Smith Parents Trust", "country": "Canada",
                "bank_details": {"account_number": "111222333", "bank_name": "TD Bank", "routing_info": "N/A"}
            }),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_user_088_charity", "beneficiary_name": "Canadian Wildlife Fund", "country": "Canada",
                "bank_details": {"account_number": "444555666", "bank_name": "RBC", "routing_info": "N/A"}
            }),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_088_reconfig",
                "category": "Account Management", "priority": "High", "channel": "Internal System",
                "request_details": "Joint account acc_chk_2001 reconfigured to single owner. Holder cust_joint_005 removed. All beneficiaries updated."
            }),
        ],
        outputs=[
            "Identities of both Jane Smith and John Doe were verified.",
            "A financial review of the joint account was completed.",
            "John Doe was removed as a joint holder and as a beneficiary.",
            "Two new beneficiaries were registered for Jane Smith and a ticket was logged documenting the account reconfiguration.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_089",
        instruction=(
            "Perform a simple security and information update for customer Hans Müller (ID: d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). "
            "First, get his profile and verify his identity using his driver's license 'Kt516858'. "
            "Retrieve the current balances for his checking account 'acc_chk_8001' and his savings account 'acc_sav_8002'. "
            "Then, update his account preferences to set his language to 'de-DE' and ensure notifications are enabled. "
            "Update his primary email address to 'hans.muller.primary@example.de' and his phone to '+49 171 555 4444'. "
            "Finally, submit a ticket with ID 'ticket_user_089_updates' under category 'Account Management', priority 'Low', via 'Web Portal', "
            "with the request details: 'Customer preferences and primary contact information updated as requested.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "id_document": "Kt516858"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_8002"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "preferences": {"language": "de-DE", "notifications": True}}),
            Action(name="update_customer_email", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "new_email": "hans.muller.primary@example.de", "new_phone": "+49 171 555 4444"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "ticket_id": "ticket_user_089_updates",
                "category": "Account Management",
                "priority": "Low",
                "channel": "Web Portal",
                "request_details": "Customer preferences and primary contact information updated as requested."
            }),
        ],
        outputs=[
            "Identity verified for Hans Müller.",
            "Balances for his checking and savings accounts were successfully retrieved.",
            "Account preferences were updated to German and to enable notifications.",
            "The customer's primary contact information was updated and a ticket was logged.",
        ],
    ),
     Task(
        annotator="0",
        user_id="user_090",
        instruction=(
            "Handle a transaction dispute for customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) on his checking account 'acc_chk_1001'. "
            "First, get his profile and verify his identity using his passport 'lF146011'. "
            "Retrieve the transaction history for the account for the last 30 days. He is disputing the transaction with ID 'txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f', a charge of $75.50 at FoodMart. "
            "Submit a detailed dispute ticket with ID 'ticket_user_090_dispute' to the 'Dispute' category with 'High' priority via 'Web Portal', "
            "targeting 'Transaction' entity 'txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f' for operation 'CHARGEBACK', "
            "with the note: 'Customer claims this charge from FoodMart was a duplicate charge and should be reversed.' "
            "As a precaution, freeze the checking account 'acc_chk_1001' with the reason 'Customer disputing transaction; account frozen pending investigation.' "
            "After freezing the account, update the customer's contact information to email 'j.doe.disputes@example.com' and phone '123-456-1111' to ensure he receives updates on the case. "
            "Finally, list the customer's beneficiaries to check for any that might be related to the dispute."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_1001", "days": 30}),
            Action(name="submit_support_ticket", kwargs={
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
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_chk_1001", "alert_reason": "Customer disputing transaction; account frozen pending investigation."}),
            Action(name="update_customer_email", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "new_email": "j.doe.disputes@example.com", "new_phone": "123-456-1111"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
        ],
        outputs=[
            "Identity verified for John Doe and transaction history reviewed.",
            "A high-priority dispute ticket was submitted for transaction 'txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f'.",
            "The checking account 'acc_chk_1001' was frozen as a security precaution.",
            "The customer's contact information was updated and his beneficiaries were listed.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_091",
        instruction=(
            "Execute a complex account closure for John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), who wants to close his checking account 'acc_chk_1001' and consolidate into his savings 'acc_sav_1002'. "
            "First, get his profile and verify his identity using his passport 'lF146011'. "
            "Two scheduled payments are sourced from the checking account and must be stopped before closure. Cancel the payment with ID 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d' and the payment with ID 'sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e'. "
            "After the payments are canceled, get the full balance of the checking account 'acc_chk_1001', which is $5230.50. "
            "Transfer the entire balance to his savings account 'acc_sav_1002'. "
            "Once the checking account is empty, submit a request to close it. "
            "Finally, submit a ticket with ID 'ticket_user_091_closure' under category 'Account Closure', priority 'High', via 'Internal System', "
            "with the request details: 'Closed acc_chk_1001 after fund consolidation. IMPORTANT: Customer requests that canceled payments (sp_b3a2c1d9... and sp_c1d9b3a2...) be manually recreated by an agent, now sourced from savings acc_sav_1002.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_c1d9b3a2-7f6a-5b4c-3d2e-1f0a9b8c7d6e"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_sav_1002", "amount": 5230.50}),
            Action(name="close_account_request", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_091_closure",
                "category": "Account Closure",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Closed acc_chk_1001 after fund consolidation. IMPORTANT: Customer requests that canceled payments (sp_b3a2c1d9... and sp_c1d9b3a2...) be manually recreated by an agent, now sourced from savings acc_sav_1002."
            }),
        ],
        outputs=[
            "Identity verified for John Doe.",
            "Two scheduled payments were successfully canceled from the checking account.",
            "The full balance of the checking account was transferred to savings.",
            "The checking account was submitted for closure and a high-priority ticket was logged with instructions for an agent.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_092",
        instruction=(
            "Assist international customer Kenji Tanaka (ID: f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3) with updating his security preferences and beneficiaries. "
            "First, get his profile and verify his identity using his national ID 'nh464131'. "
            "Update his account preferences to enable paperless billing and set the communication channel to 'App'. "
            "Next, he wants to replace his primary beneficiary. List his current beneficiaries and then remove the existing one, 'Yuki Tanaka' (ID: bene_2b1c9d8e-7f6a-5b4c-3d2e-1f0a9b8c7d6e). "
            "After removal, register a new international beneficiary with ID 'bene_user_092_global_tech' for 'Global Tech Inc.', "
            "with account number '9876543210' at 'City National Bank' (routing: '122000661') in the 'USA'. "
            "Get the current balance of his primary checking account 'acc_chk_10001'. "
            "Finally, submit a ticket with ID 'ticket_user_092_updates' under category 'Account Management', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Customer preferences updated. Beneficiary Yuki Tanaka replaced with new international beneficiary Global Tech Inc.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "id_document": "nh464131"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "preferences": {"paperless_billing": True, "communication_channel": "App"}}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "beneficiary_id": "bene_2b1c9d8e-7f6a-5b4c-3d2e-1f0a9b8c7d6e"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "beneficiary_id": "bene_user_092_global_tech",
                "beneficiary_name": "Global Tech Inc.",
                "country": "USA",
                "bank_details": {"account_number": "9876543210", "bank_name": "City National Bank", "routing_info": "122000661"}
            }),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_10001"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "ticket_id": "ticket_user_092_updates",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Customer preferences updated. Beneficiary Yuki Tanaka replaced with new international beneficiary Global Tech Inc."
            }),
        ],
        outputs=[
            "Identity verified for Kenji Tanaka and his account preferences were updated.",
            "The beneficiary 'Yuki Tanaka' was successfully removed.",
            "The new international beneficiary 'Global Tech Inc.' was registered.",
            "The customer's checking account balance was checked and a ticket was logged to document the updates.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_093",
        instruction=(
            "Perform a detailed audit of both the checking and credit card accounts for customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "Current date is 2023-11-20. First, get his profile and verify his identity using his passport 'lF146011'. "
            "Retrieve the transaction history for his checking account 'acc_chk_1001' for the last 90 days, and aggregate his expenses for October 2023. "
            "Then, retrieve the transaction history for his credit card 'acc_crd_1003' for the last 90 days, and aggregate his expenses for October 2023. "
            "As a preventative security measure while the customer reviews the audit, freeze the credit card account 'acc_crd_1003' with the reason 'Preventative security freeze while customer reviews audit results.' "
            "Update the customer's contact information to the secure secondary email 'j.doe.audit@example.com' and phone '123-555-4321'. "
            "Finally, submit a comprehensive audit ticket with ID 'ticket_user_093_audit' under category 'Audit', priority 'High', via 'Internal System', "
            "with the request details: '90-day audit complete for checking and credit accounts. October expenses aggregated. Credit card preventatively frozen. Contact info updated.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_1001", "days": 90}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_chk_1001", "month": "2023-10"}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_crd_1003", "days": 90}),
            Action(name="aggregate_monthly_expenses", kwargs={"account_id": "acc_crd_1003", "month": "2023-10"}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_crd_1003", "alert_reason": "Preventative security freeze while customer reviews audit results."}),
            Action(name="update_customer_email", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "new_email": "j.doe.audit@example.com", "new_phone": "123-555-4321"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_093_audit",
                "category": "Audit",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "90-day audit complete for checking and credit accounts. October expenses aggregated. Credit card preventatively frozen. Contact info updated."
            }),
        ],
        outputs=[
            "Identity verified for John Doe.",
            "A 90-day financial audit was performed on both his checking and credit card accounts.",
            "October 2023 expenses were aggregated for both accounts.",
            "The credit card was preventatively frozen, contact info was updated, and a high-priority audit ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_094",
        instruction=(
            "Perform a simple profile update and loan check for customer David Chen (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "First, get his profile and verify his identity using his driver's license 'VI933872'. "
            "Update his email to 'david.chen.student@example.edu' and his phone number to '555-111-4444'. "
            "Next, summarize the status of his loan applications. "
            "Then, list his beneficiaries. "
            "Finally, update his account preferences to enable notifications."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "VI933872"}),
            Action(name="update_customer_email", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "new_email": "david.chen.student@example.edu", "new_phone": "555-111-4444"}),
            Action(name="summarize_loan_applications_by_status", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="update_account_preferences", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "preferences": {"notifications": True}}),
        ],
        outputs=[
            "Identity verified for David Chen.",
            "His contact information (email and phone) was successfully updated.",
            "His loan application status was summarized.",
            "His beneficiary list was checked and his account preferences were updated to enable notifications.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_095",
        instruction=(
            "A customer, Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef), is removing a joint holder from her account 'acc_chk_2001' and transferring a final settlement. "
            "The joint holder to be removed is John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), listed as holder ID 'cust_joint_005'. "
            "First, get the profiles for both Jane Smith and John Doe and verify their identities using their respective documents: national ID 'jd195515' for Jane and passport 'lF146011' for John. "
            "After verification, remove John Doe ('cust_joint_005') as a joint account holder from 'acc_chk_2001'. "
            "Get the current balance of the account to confirm funds. "
            "Then, transfer a final settlement amount of 1000.00 CAD to John Doe's personal checking account, which has the account number '1111'. "
            "Finally, submit a ticket with ID 'ticket_user_095_settlement' under category 'Legal', priority 'High', via 'Internal System', "
            "with the request details: 'Joint holder cust_joint_005 (John Doe) removed from account acc_chk_2001. Final settlement of 1000.00 CAD transferred.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="remove_joint_account_holder", kwargs={"account_id": "acc_chk_2001", "holder_id": "cust_joint_005"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_2001", "to_account": "1111", "amount": 1000.00}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_095_settlement",
                "category": "Legal",
                "priority": "High",
                "channel": "Internal System",
                "request_details": "Joint holder cust_joint_005 (John Doe) removed from account acc_chk_2001. Final settlement of 1000.00 CAD transferred."
            }),
        ],
        outputs=[
            "Identities of both Jane Smith and John Doe were successfully verified.",
            "John Doe was removed as a joint holder from account acc_chk_2001.",
            "The account balance was confirmed.",
            "A final settlement of 1000.00 CAD was transferred to John Doe and a high-priority legal ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_096",
        instruction=(
            "Execute the full closure of customer John Doe's relationship with the bank (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). "
            "First, get his profile and verify his identity using his passport 'lF146011'. "
            "The customer has already paid off his credit card, so submit a request to close the credit card account 'acc_crd_1003'. "
            "Next, he wants to consolidate his funds before final closure. Get the balance of his checking account 'acc_chk_1001' ($5230.50) and his savings account 'acc_sav_1002'. "
            "Transfer the full balance of $5230.50 from his checking account to his savings account. "
            "After consolidating the funds, submit a request to close the now-empty checking account 'acc_chk_1001'. "
            "Before the final step, cancel all of his scheduled payments to prevent future transactions; cancel 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d' and 'sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w2'. "
            "Finally, submit a ticket with ID 'ticket_user_096_final_closure' under category 'Account Closure', priority 'Critical', via 'Internal System', "
            "with the request details: 'Full relationship closure initiated. Credit and checking accounts closed. All funds consolidated into savings account acc_sav_1002. Customer requests an agent to call for final closure and disbursement of remaining funds.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="close_account_request", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="transfer_funds_with_limit_check", kwargs={"from_account": "acc_chk_1001", "to_account": "acc_sav_1002", "amount": 5230.50}),
            Action(name="close_account_request", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="cancel_scheduled_payment", kwargs={"payment_id": "sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w2"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_096_final_closure",
                "category": "Account Closure",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Full relationship closure initiated. Credit and checking accounts closed. All funds consolidated into savings account acc_sav_1002. Customer requests an agent to call for final closure and disbursement of remaining funds."
            }),
        ],
        outputs=[
            "Identity verified for John Doe and his credit card account was submitted for closure.",
            "Funds from his checking account were consolidated into his savings account.",
            "The now-empty checking account was submitted for closure.",
            "All scheduled payments were canceled and a critical ticket was logged to complete the final steps of closing the relationship.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_097",
        instruction=(
            "Assist customer Jane Smith (ID: a1b2c3d4-e5f6-7890-1234-567890abcdef) with adding her spouse to her checking account 'acc_chk_2001' and updating her beneficiaries. "
            "Her spouse is David Chen (ID: d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). "
            "First, get the profile for Jane Smith and verify her identity using her national ID 'jd195515'. "
            "Next, add David Chen as a joint account holder. After he is added, verify his identity using his national ID 'pI260068'. "
            "Then, update Jane's beneficiary list. List her current beneficiaries and remove the existing one, John Doe (ID: bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f). "
            "Register her new spouse, David Chen, as the new primary beneficiary with ID 'bene_user_097_d_chen', using his account number '6666' at 'City General Bank' (routing: 'N/A') in the 'USA'. "
            "Finally, submit a ticket with ID 'ticket_user_097_spouse_add' under category 'Account Management', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Added spouse David Chen as joint holder and primary beneficiary to account acc_chk_2001. Removed previous beneficiary.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "id_document": "jd195515"}),
            Action(name="add_joint_account_holder", kwargs={"account_id": "acc_chk_2001", "holder_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "id_document": "pI260068"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_user_097_d_chen",
                "beneficiary_name": "David Chen",
                "country": "USA",
                "bank_details": {"account_number": "6666", "bank_name": "City General Bank", "routing_info": "N/A"}
            }),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "ticket_id": "ticket_user_097_spouse_add",
                "category": "Account Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Added spouse David Chen as joint holder and primary beneficiary to account acc_chk_2001. Removed previous beneficiary."
            }),
        ],
        outputs=[
            "Identity of primary account holder Jane Smith was verified.",
            "David Chen was added as a joint account holder and his identity was also verified.",
            "The previous beneficiary, John Doe, was removed.",
            "The new spouse, David Chen, was registered as the new primary beneficiary and a ticket was logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_098",
        instruction=(
            "Execute a full security lockdown and investigation for customer John Doe (ID: c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) following a major fraud alert. "
            "First, get his profile and verify his identity using his passport 'lF146011'. "
            "Immediately freeze all three of his accounts: checking 'acc_chk_1001', savings 'acc_sav_1002', and credit card 'acc_crd_1003', with the reason 'Major fraud alert; all accounts locked pending investigation.' "
            "Once the accounts are secure, retrieve the full transaction history for the checking account and the credit card account for the last 30 days for analysis. "
            "His contact info is believed to be compromised. Update his information to a new secure email 'j.doe.secure.recovery@example.com' and a new secure phone '123-555-0000'. "
            "Finally, submit a support ticket with ID 'ticket_user_098_lockdown' to the 'Security' category with 'Critical' priority via 'Internal System', "
            "with the request details: 'Full account lockdown for John Doe due to major fraud alert. All accounts frozen, transaction history pulled for investigation, and contact info secured.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "id_document": "lF146011"}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_chk_1001", "alert_reason": "Major fraud alert; all accounts locked pending investigation."}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_sav_1002", "alert_reason": "Major fraud alert; all accounts locked pending investigation."}),
            Action(name="freeze_account_on_fraud_alert", kwargs={"account_id": "acc_crd_1003", "alert_reason": "Major fraud alert; all accounts locked pending investigation."}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_chk_1001", "days": 30}),
            Action(name="get_account_transaction_history", kwargs={"account_id": "acc_crd_1003", "days": 30}),
            Action(name="update_customer_email", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "new_email": "j.doe.secure.recovery@example.com", "new_phone": "123-555-0000"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "ticket_id": "ticket_user_098_lockdown",
                "category": "Security",
                "priority": "Critical",
                "channel": "Internal System",
                "request_details": "Full account lockdown for John Doe due to major fraud alert. All accounts frozen, transaction history pulled for investigation, and contact info secured."
            }),
        ],
        outputs=[
            "Identity verified for John Doe.",
            "All three of the customer's accounts have been frozen due to a major fraud alert.",
            "Transaction histories for the checking and credit card accounts have been retrieved for investigation.",
            "The customer's contact information has been updated and a critical security ticket has been logged.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_099",
        instruction=(
            "Perform a simple profile update and loan status check for customer Liam O'Connor (ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11). "
            "First, get his profile and verify his identity using his passport 'Se620000'. "
            "Update his email to 'liam.oconnor.profile@example.ie' and his phone number to '+353 87 555 6666'. "
            "Next, summarize the status of his loan applications to provide him with an update on his active loan. "
            "Then, get the current balance of his primary checking account 'acc_chk_12001'. "
            "Finally, submit a low-priority support ticket with ID 'ticket_user_099_profile_update' under category 'General Inquiry' via 'Web Portal', "
            "with the request details: 'Customer contact information updated. Loan and account status provided as requested.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "id_document": "Se620000"}),
            Action(name="update_customer_email", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "new_email": "liam.oconnor.profile@example.ie", "new_phone": "+353 87 555 6666"}),
            Action(name="summarize_loan_applications_by_status", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_12001"}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                "ticket_id": "ticket_user_099_profile_update",
                "category": "General Inquiry",
                "priority": "Low",
                "channel": "Web Portal",
                "request_details": "Customer contact information updated. Loan and account status provided as requested."
            }),
        ],
        outputs=[
            "Identity verified for Liam O'Connor.",
            "The customer's email and phone number were successfully updated.",
            "A summary of his loan status was retrieved.",
            "His checking account balance was checked and a ticket was logged to confirm the updates.",
        ],
    ),
    Task(
        annotator="0",
        user_id="user_100",
        instruction=(
            "Assist customer Hans Müller (ID: d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1) with reconfiguring his international beneficiaries and account preferences. "
            "First, get his profile and verify his identity using his driver's license 'Kt516858'. "
            "He wants to overhaul his beneficiary list. List his current beneficiaries, then remove the existing one: 'Klaus Schmidt' (ID: bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a). "
            "Next, register two new international beneficiaries. The first is in France, with ID 'bene_user_100_fr' for 'French Connection Supplies', "
            "with account IBAN 'FR7630002005500000157845Z25' at 'Societe Generale' (BIC: 'SOGEFRPP'). "
            "The second is in the UK, with ID 'bene_user_100_uk' for 'British Imports Co.', "
            "with account number 'GB29NWBK60161331926819' at 'NatWest' (BIC: 'NWBKGB2L'). "
            "After updating the beneficiaries, update his account preferences to set his language to 'de-DE' and ensure notifications are enabled. "
            "Finally, submit a ticket with ID 'ticket_user_100_bene_reconfig' under category 'Beneficiary Management', priority 'Medium', via 'Web Portal', "
            "with the request details: 'Beneficiary list reconfigured. Klaus Schmidt removed. French and UK beneficiaries added. Preferences updated.'"
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="verify_customer_identity", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "id_document": "Kt516858"}),
            Action(name="list_linked_beneficiaries", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="delete_existing_beneficiary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "beneficiary_id": "bene_user_100_fr",
                "beneficiary_name": "French Connection Supplies",
                "country": "France",
                "bank_details": {"account_number": "FR7630002005500000157845Z25", "bank_name": "Societe Generale", "routing_info": "SOGEFRPP"}
            }),
            Action(name="register_new_beneficiary", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "beneficiary_id": "bene_user_100_uk",
                "beneficiary_name": "British Imports Co.",
                "country": "United Kingdom",
                "bank_details": {"account_number": "GB29NWBK60161331926819", "bank_name": "NatWest", "routing_info": "NWBKGB2L"}
            }),
            Action(name="update_account_preferences", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "preferences": {"language": "de-DE", "notifications": True}}),
            Action(name="submit_support_ticket", kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "ticket_id": "ticket_user_100_bene_reconfig",
                "category": "Beneficiary Management",
                "priority": "Medium",
                "channel": "Web Portal",
                "request_details": "Beneficiary list reconfigured. Klaus Schmidt removed. French and UK beneficiaries added. Preferences updated."
            }),
        ],
        outputs=[
            "Identity verified for Hans Müller.",
            "His beneficiary list was reconfigured: one beneficiary was removed.",
            "Two new international beneficiaries in France and the UK were successfully registered.",
            "Account preferences were updated and a ticket was logged to document the changes.",
        ],
    )
]
