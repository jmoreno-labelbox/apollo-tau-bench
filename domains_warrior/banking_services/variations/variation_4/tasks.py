from domains.dto import Action, Task

# Edges = Input kwargs from prompt + Input kwargs sourced from API outputs
# Each edge represents a dependency where an API call uses data from the prompt or previous API results
# MEDIUM COMPLEXITY TASKS (7-12 edges)

TASKS = [
    Task(
        annotator="0",
        user_id="USER_001",
        instruction="You are onboarding John Doe's (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) new corporation, now represented by Hans Müller (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). Get risk profiles for both. Use 7,800 EUR from the business checking account (acc_chk_8001) to pay off his personal auto loan (loan_auto_002). Adjust the overdraft limit on that account to 2,500 EUR. Review scheduled payments. Deactivate the old personal checking account (acc_chk_1001). Enforce a KYC refresh for the business entity and reassign its relationship manager to 'rm-de-10'. Finally, report the new relationship manager",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_auto_002", "from_account_id": "acc_chk_8001", "amount": 7800}),
            Action(name="get_loan_details", kwargs={"loan_id": "loan_auto_002"}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_8001", "new_limit": 2500.00}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "relationship_manager_id": "rm-de-10"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
        ],
        outputs=['"new_relationship_manager": "rm-de-10"'],
    ),
    Task(
        annotator="0",
        user_id="USER_002",
        instruction="You are investigating a synthetic identity fraud case. The fraudster used the SSN last 4 digits '8765' belonging to your real customer, Noah Kim (now canonicalized as customer ID c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12). A fraudulent profile linked to Aisha Khan (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15) was merged into his real profile. First, get the risk profile of both Noah Kim and Aisha Khan. The fraudster took out a personal loan (loan_pers_013) which is now incorrectly linked to Noah Kim; pay off the full remaining balance of 3,500 KRW from his checking account (acc_chk_16001). Lock the account for security. Review his scheduled payments. Enforce an immediate KYC refresh. Reassign his relationship manager to 'rm-kr-03', a fraud specialist. Update his communication preference to 'Phone'. Create a support ticket for the paid-off loan to document the synthetic ID fraud for credit bureau reporting with the reason 'Synthetic Identity Fraud Remediation Report'. Report the status of the fraudulent loan and the status of the checking account.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15"}),
            Action(name="merge_duplicate_customers_by_ssn", kwargs={"ssn_last_4": "8765"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_pers_013", "from_account_id": "acc_chk_16001", "amount": 3500.00}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_chk_16001"}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_16001"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12", }),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12", "relationship_manager_id": "rm-kr-03"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12", "new_channel": "Phone"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12", "account_id": "acc_chk_16001", "reason": "Synthetic Identity Fraud Remediation Report"}),
        ],
        outputs=['"fraudulent_loan_status": "Paid Off"', '"checking_account_status": "Locked"'],
    ),
    Task(
        annotator="0",
        user_id="USER_003",
        instruction="You are a securities analyst investigating a potential insider trading red flag for David Chen (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). First, add employer to his profile which is 'City General Hospital'. Review the last 100 transactions on his investment account (acc_inv_3002), noting a recent large purchase ('txn_1h8i2k5m-9i2g-3h7k-7i1m-4k5i7j2l3h8h'). Calculate his total deposits into that account over the past 6 months (2023-05-01 to 2023-10-31) to check for unusual funding. Lock the investment account. To prevent capital flight, also lock his checking account (acc_chk_3001). Reassign his relationship manager to 'rm012', a compliance specialist. Enforce an immediate KYC refresh. Get his contact methods and update his preference to 'Mail' for legal correspondence. Create a high-priority support ticket linked to the investment account to formally escalate to the legal department with the reason 'Escalation to Legal: Potential Insider Trading'. Report the customer's employer, the status of his investment account, and his new relationship manager.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="add_employer_to_customer_profile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "employer": "City General Hospital"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_inv_3002"], "limit": 100}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_inv_3002"], "start_date": "2023-05-01", "end_date": "2023-10-31"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_inv_3002"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_chk_3001"}),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "relationship_manager_id": "rm012"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", }),
            Action(name="get_customer_contact_methods", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "new_channel": "Mail"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "account_id": "acc_inv_3002", "reason": "Escalation to Legal: Potential Insider Trading"}),
        ],
        outputs=['"employer": "City General Hospital"', '"investment_account_status": "Locked"', '"relationship_manager": "rm012"'],
    ),
    Task(
        annotator="0",
        user_id="USER_004",
        instruction="You are resolving an inheritance dispute for the estate of Anja Novak (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18). First, get her total balance. Immediately lock her checking account (acc_chk_19001). Review her active loans; the personal loan (loan_pers_013) must be paid. Pay off the 3,500 EUR balance from the checking account. Review her scheduled payments to identify any outgoing funds. Fetch all her 'Personal' beneficiaries. As per the legal settlement, the remaining funds in the checking account must be split: 50% to 'Marie Dubois' (bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c) and 50% to 'Klaus Schmidt' (bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a). Verify both beneficiaries exist first. Initiate the two transfers for the remaining balance. After the account is empty, deactivate it. Create a final support ticket for the loan to document the full estate settlement. Report the final balance of the checking account, the status of the loan, and the status of the checking account.",
        actions=[
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_chk_19001"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_pers_013", "from_account_id": "acc_chk_19001", "amount": 3500.00}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_19001"}),
            Action(name="fetch_beneficiaries_by_relationship", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "relationship": "Personal"}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c"}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="initiate_fund_transfer_to_beneficiary", kwargs={"source_account_id": "acc_chk_19001", "beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c", "amount": 0.00}), # Balance is now 0
            Action(name="initiate_fund_transfer_to_beneficiary", kwargs={"source_account_id": "acc_chk_19001", "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a", "amount": 0.00}), # Balance is still 0
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_chk_19001"}),
            Action(name="create_support_ticket_for_transaction", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "transaction_id": "loan_pers_013", "reason": "Final Estate Settlement Documentation"}),
        ],
        outputs=['"final_checking_balance": 0.00', '"loan_status": "Paid Off"', '"account_status": "Inactive"'],
    ),
    Task(
        annotator="0",
        user_id="USER_005",
        instruction = ("You are a dispute resolution officer. Customer Chloe Dubois (e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2) has reported an unauthorized transaction of -85.00 EUR on her credit card (acc_crd_9002). Start by checking her total balance and reviewing the last 20 transactions from that card. Check her risk profile and whether there are any similar past disputes by retrieving support tickets related to the credit category. Create a high-priority dispute ticket for transaction 'txn_f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15' with the reason 'Unauthorized charge on credit card'. Temporarily lock the credit card account for security. Apply a provisional credit adjustment of 85.00 to her account while the dispute is under review with the reason 'Provisional credit pending dispute resolution'. Report whether similar past disputes were found"),
        actions=[
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_crd_9002"], "limit": 20}
            ),
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="find_recent_support_tickets_by_category",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "category": "Credit"}
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "transaction_id": "txn_f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "reason": "Unauthorized charge on credit card"
                }
            ),
            Action(
                name="lock_account_manually",
                kwargs={"account_id": "acc_crd_9002"}
            ),
            Action(
                name="apply_transaction_adjustment",
                kwargs={
                    "account_id": "acc_crd_9002",
                    "amount": 85.00,
                    "reason": "Provisional credit pending dispute resolution"
                }
            ),
        ],
        outputs=[
            '"similar_past_disputes_found": false',
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_006",
        instruction="You are managing a merger between two clients: Kenji Tanaka (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3) and Adetokunbo Adebayor (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23), who share a business ID (simulated with SSN '6677'). First, get the risk profile for both. Merge their customer records. For the newly merged primary customer (Kenji Tanaka), get the combined total balance. Review all now-combined active loans. Make a 1,000,000 JPY overpayment on loan 'loan_auto_011' from account 'acc_chk_10001'. Adjust the overdraft limit on the primary business account (acc_chk_24001) to 200,000 NGN. Reassign a single relationship manager ('rm-jp-02') to the primary customer. Create a support ticket for the primary business account to document the merger with the reason 'Corporate merger documentation'. Report the credit scores of both original customers and the new overdraft limit.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="merge_duplicate_customers_by_ssn", kwargs={"ssn_last_4": "6677"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_auto_011", "from_account_id": "acc_chk_10001", "amount": 1000000.00}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_24001", "new_limit": 200000.00}),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "relationship_manager_id": "rm-jp-02"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "account_id": "acc_chk_24001", "reason": "Corporate merger documentation"}),
        ],
        outputs=['"kenji_tanaka_credit_score": 820', '"adetokunbo_adebayor_credit_score": 760', '"new_overdraft_limit": 200000.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_007",
        instruction="You are a loan officer. Customer David Chen (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) is requesting loan restructuring. First check their active loans and risk profile, then calculate their total balance across all accounts. The customer wants to make a $500 overpayment on their mortgage (loan_mort_001) from their checking account acc_chk_3001. After the overpayment, adjust the loan's maturity date to 2051-07-15. Report the loan balance after overpayment and the new maturity date.",
        actions=[
            Action(
                name="list_active_loans_with_balances",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="make_loan_overpayment",
                kwargs={
                    "loan_id": "loan_mort_001",
                    "amount": 500.00,
                    "from_account_id": "acc_chk_3001"
                }
            ),
            Action(
                name="adjust_loan_payment_due_date",
                kwargs={
                    "loan_id": "loan_mort_001",
                    "new_due_date": "2051-07-15"
                }
            ),
        ],
        outputs=['"loan_balance_after_overpayment": 714740.50', '"new_maturity_date": "2051-07-15"'],
    ),
    Task(
        annotator="0",
        user_id="USER_008",
        instruction="You are a compliance officer conducting a regulatory review. Customer Fatima Al-Fassi (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6) has been flagged for enhanced due diligence. Their accounts are 'acc_chk_7001', 'acc_sav_7002'. Check their risk profile and total balance across all accounts. Review their last 30 transactions. Enforce a KYC refresh due to 'Regulatory requirement for enhanced due diligence'. Adjust their overdraft limit on account acc_chk_7001 to $3,000 due to 'Compliance review - risk-based limit adjustment'. Update their communication preference to 'Email' for audit trail purposes. Report the AML risk level, the number of transactions reviewed, and the new overdraft limit.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_7001", "acc_sav_7002"], "limit": 30}
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                }
            ),
            Action(
                name="review_overdraft_activity_and_adjust_limit",
                kwargs={
                    "account_id": "acc_chk_7001",
                    "new_limit": 3000.00
                }
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "new_channel": "Email"
                }
            ),
        ],
        outputs=['"aml_risk_level": "Low"', '"transactions_reviewed": 1', '"new_overdraft_limit": 3000.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_009",
        instruction="You are a transaction analyst. Customer Lakshmi Narayanan (a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4) has reported a complex transaction issue. Check their total balance and review the last 25 transactions across their accounts. Transaction 'txn_b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11' for 50000 INR appears to be a business expense that should be split. Create a dispute ticket for this transaction with the reason 'Business expense incorrectly charged to personal account'. Then, split the transaction, allocating -30000 to the checking account (acc_chk_5002) and -20000 to the savings account (acc_sav_5001). Report the total balance, number of transactions reviewed, and the details of the new split transactions.",
        actions=[
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_sav_5001", "acc_chk_5002"], "limit": 25}
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "transaction_id": "txn_b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "reason": "Business expense incorrectly charged to personal account"
                }
            ),
            Action(
                name="split_transaction_between_accounts",
                kwargs={
                    "transaction_id": "txn_b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "splits": [
                        {"account_id": "acc_chk_5002", "amount": -30000.00},
                        {"account_id": "acc_sav_5001", "amount": -20000.00}
                    ]
                }
            ),
        ],
        outputs=['"total_balance": 2550000.0', '"transactions_reviewed": 1', '"split_transaction_count": 2'],
    ),
    Task(
        annotator="0",
        user_id="USER_010",
        instruction="You are a relationship manager handling a high-value customer recovery case. Customer Oliver Williams (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5) has requested account deactivation. This customer's account acc_chk_6001 is currently active. Check their risk profile and total balance first. Close their account. Reassign their relationship manager to 'rm_senior_001'. Update their communication preference to 'Email'. Add their new employer 'Advanced Electric Systems' to their profile. Report the customer's credit score, total balance, and new relationship manager assignment.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}
            ),
            Action(
                name="close_active_account",
                kwargs={
                    "account_id": "acc_chk_6001",
                }
            ),
            Action(
                name="reassign_relationship_manager",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "relationship_manager_id": "rm_senior_001"
                }
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "new_channel": "Email",
                }
            ),
            Action(
                name="add_employer_to_customer_profile",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "employer": "Advanced Electric Systems"
                }
            ),
        ],
        outputs=['"credit_score": 650', '"total_balance": 850.75', '"new_manager": "rm_senior_001"'],
    ),
    Task(
        annotator="0",
        user_id="USER_011",
        instruction="You are an international banking officer. Customer Fatima Al-Fassi (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6) is requesting a 5,000 AED international wire transfer. Check their risk profile and total balance. Review their last 25 transactions. Verify the beneficiary 'Dubai International School' (bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f) exists. Process the wire transfer from acc_chk_7001 to this beneficiary. Enforce a KYC refresh due to the large transfer. Report the customer's AML risk level, total balance after the transfer, and the transfer authorization status.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_7001"], "limit": 25}
            ),
            Action(
                name="verify_beneficiary_exists",
                kwargs={"beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f"}
            ),
            Action(
                name="initiate_fund_transfer_to_beneficiary",
                kwargs={
                    "source_account_id": "acc_chk_7001",
                    "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f",
                    "amount": 5000.00
                }
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                }
            ),
        ],
        outputs=['"aml_risk_level": "Low"', '"total_balance": 895000.00', '"transfer_authorized": true'],
    ),
    Task(
        annotator="0",
        user_id="USER_012",
        instruction="You are a senior loan officer. Customer Hans Müller (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1) is seeking to optimize their loan payment schedule. Check their active loans, risk profile, and total balance. The customer wants to make a 2,000 EUR overpayment on their mortgage (loan_mort_014) from their checking account acc_chk_8001. After the overpayment, adjust the loan's maturity date to 2035-11-01. Report the loan balance after overpayment, the new maturity date, and the customer's credit score.",
        actions=[
            Action(
                name="list_active_loans_with_balances",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="make_loan_overpayment",
                kwargs={
                    "loan_id": "loan_mort_014",
                    "amount": 2000.00,
                    "from_account_id": "acc_chk_8001"
                }
            ),
            Action(
                name="adjust_loan_payment_due_date",
                kwargs={
                    "loan_id": "loan_mort_014",
                    "new_due_date": "2035-11-01"
                }
            ),
        ],
        outputs=['"loan_balance_after_overpayment": 178000.00', '"new_maturity_date": "2035-11-01"', '"credit_score": 800'],
    ),
    Task(
        annotator="0",
        user_id="USER_013",
        instruction="You are a data analyst. It's been flagged that there might be duplicate records for customers with the SSN last 4 digits '1122'. Check the risk profile and total balance for customer David Chen (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a), who has this SSN. Then, execute a merge for all customers with this SSN. Update David Chen's communication preference to 'Email'. Ensure his employer is correctly listed as 'City General Hospital'. Finally, reassign his relationship manager to 'rm_consolidated_001'. Report the customer's credit score, final total balance, and the result of the merge operation.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="merge_duplicate_customers_by_ssn",
                kwargs={"ssn_last_4": "1122"}
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "new_channel": "Email"
                }
            ),
            Action(
                name="add_employer_to_customer_profile",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "employer": "City General Hospital"
                }
            ),
            Action(
                name="reassign_relationship_manager",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "relationship_manager_id": "rm_consolidated_001"
                }
            ),
        ],
        outputs=['"credit_score": 810', '"total_balance": 162540.25', '"merged_customer_ids": ["a1b2c3d4-e5f6-7890-1234-567890abcdef-16"]'],
    ),
    Task(
        annotator="0",
        user_id="USER_014",
        instruction="You are an account manager. Customer Kenji Tanaka (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3) has requested to deactivate their account temporarily, which is currently active. Check their risk profile and total balance. Close their checking account acc_chk_10001. Reassign their relationship manager to 'rm_premium_001'. Update their communication preference to 'Email'. Report the customer's credit score, total balance, and account status.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="close_active_account",
                kwargs={
                    "account_id": "acc_chk_10001"
                }
            ),
            Action(
                name="reassign_relationship_manager",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "relationship_manager_id": "rm_premium_001"
                }
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "new_channel": "Email"
                }
            ),
        ],
        outputs=['"credit_score": 820', '"total_balance": 17500000.00', '"reactivation_status": "Inactive"'],
    ),
    Task(
        annotator="0",
        user_id="USER_015",
        instruction=("You are a business banking officer; check Hans Müller's (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1) total balance and last 30 transactions, create a support ticket for transaction 'txn_e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14' citing 'Business expense allocation correction', then split the 2000 EUR by debiting 1400 EUR from checking (acc_chk_8001) and 600 EUR from savings (acc_sav_8002), update his communication preference to 'App', and report the total balance, number of transactions reviewed, and split amounts."),
        actions=[
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={
                    "account_ids": ["acc_chk_8001", "acc_sav_8002"],
                    "limit": 30
                }
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "transaction_id": "txn_e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "reason": "Business expense allocation correction"
                }
            ),
            Action(
                name="split_transaction_between_accounts",
                kwargs={
                    "transaction_id": "txn_e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "splits": [
                        {"account_id": "acc_chk_8001", "amount": -1400.00},
                        {"account_id": "acc_sav_8002", "amount": -600.00}
                    ]
                }
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "new_channel": "App"
                }
            ),
        ],
        outputs=['"total_balance": 132800.50', '"transactions_reviewed": 1', '"split_amounts": [-1400.00, -600.00]'],
    ),
    Task(
        annotator="0",
        user_id="USER_016",
        instruction="You are an agricultural lending officer. Customer Liam O'Connor (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11) is a farmer seeking seasonal payment adjustments. Check their active loans, risk profile, and total balance. The customer wants to make a 2,000 EUR overpayment on their business loan (loan_biz_005) from their checking account acc_chk_12001. After the overpayment, adjust the loan's maturity date to 2027-04-01. Report the loan balance after overpayment, the new maturity date, and customer's credit score.",
        actions=[
            Action(
                name="list_active_loans_with_balances",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}
            ),
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}
            ),
            Action(
                name="make_loan_overpayment",
                kwargs={
                    "loan_id": "loan_biz_005",
                    "amount": 2000.00,
                    "from_account_id": "acc_chk_12001"
                }
            ),
            Action(
                name="adjust_loan_payment_due_date",
                kwargs={
                    "loan_id": "loan_biz_005",
                    "new_due_date": "2027-04-01",
                }
            ),
        ],
        outputs=['"loan_balance_after_overpayment": 43150.90', '"new_maturity_date": "2027-04-01"', '"credit_score": 720'],
    ),
    Task(
        annotator="0",
        user_id="USER_017",
        instruction="You are a student banking officer. Customer Aisha Khan (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12) is requesting a 15,000 PKR international remittance. Check their risk profile and total balance from this account acc_chk_13001. Review their last 25 transactions. Customer said the beneficiary id is bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a. Verify the beneficiary exists, then initiate the transfer from acc_chk_13001. Enforce a KYC refresh. Report the customer's AML risk level",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_13001"], "limit": 25}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="initiate_fund_transfer_to_beneficiary", kwargs={
                "source_account_id": "acc_chk_13001",
                "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a",
                "amount": 15000.00
            }),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"})
        ],
        outputs=['"aml_risk_level": "Low"'],
    ),
    Task(
        annotator="0",
        user_id="USER_018",
        instruction="You are a commercial lending officer. Customer Isabella Rossi (a1b2c3d4-e5f6-7890-1234-567890abcdef-10) needs help categorizing a business transaction. Check their risk profile and total balance. Fetch their checking account(s). You get acc_chk_11001. Review their last 30 transactions from the checking account. Create a support ticket for transaction 'txn_b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17' with the reason 'Help categorize fashion industry business expense'. Then, update their communication preference to 'App'. Report the total balance, number of transactions reviewed, and the support ticket reason for confirmation.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10"}
            ),
            Action(
                name="get_customer_accounts_by_type",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10", "account_type": "Checking"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_11001"], "limit": 30}
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "transaction_id": "txn_b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "reason": "Help categorize fashion industry business expense"
                }
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "new_channel": "App"
                }
            ),
        ],
        outputs=['"total_balance": 12000.00', '"transactions_reviewed": 1', '"ticket_reason": "Help categorize fashion industry business expense"'],
    ),
    Task(
        annotator="0",
        user_id="USER_019",
        instruction="Customer Kenji Tanaka (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3) has been flagged for account inactivity. Check their risk profile and total balance. Review their last 20 transactions. Check if account acc_chk_10001 and acc_sav_10002 should be locked due to 90 days of inactivity (assume today is 2026-07-28). Update their communication preference to 'SMS'. Create a support ticket related to transaction 'txn_a1b2c3d4-e5f6-7890-1234-567890abcdef-16' for 'Account inactivity security review'. Report the customer's total balance, number of transactions reviewed, and the account lock status.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_10001", "acc_sav_10002"], "limit": 20}
            ),
            Action(
                name="lock_account_manually",
                kwargs={
                    "account_id": "acc_chk_10001"
                }
            ),
            Action(
                name="lock_account_manually",
                kwargs={
                    "account_id": "acc_sav_10002"
                }
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "new_channel": "SMS"
                }
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "transaction_id": "txn_a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "reason": "Account inactivity security review"
                }
            ),
        ],
        outputs=['"total_balance": 17500000.00', '"transactions_reviewed": 1', '"account_locked": true'],
    ),
    Task(
        annotator="0",
        user_id="USER_020",
        instruction="You are a private banking officer. Customer Lakshmi Narayanan (a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4) is eligible for a premium service upgrade. Their account ids are acc_sav_5001 and acc_chk_5002. Check their risk profile and total balance. Review their last 35 transactions. Reassign their relationship manager to 'rm_premium_001'. Update their communication preference to 'Email'. Verify their employer is 'Global Tech Services'. Create a support ticket related to transaction 'txn_b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11' to document the 'High-value customer service upgrade'. Report the customer's credit score, total balance, and new relationship manager.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_sav_5001", "acc_chk_5002"], "limit": 35}
            ),
            Action(
                name="reassign_relationship_manager",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "relationship_manager_id": "rm_premium_001"
                }
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "new_channel": "Email"
                }
            ),
            Action(
                name="add_employer_to_customer_profile",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "employer": "Global Tech Services"
                }
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "transaction_id": "txn_b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "reason": "High-value customer service upgrade"
                }
            ),
        ],
        outputs=['"credit_score": 790', '"total_balance": 2550000.00', '"new_manager": "rm_premium_001"'],
    ),
    Task(
        annotator="0",
        user_id="USER_021",
        instruction="You are a relationship manager for Chloe Dubois (e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2). Her personal loan (loan_pers_008) is marked 'Delinquent'. First, get her risk profile and total balance across all accounts to assess her financial situation. Review all her active loans and her recent transactions to understand spending patterns from 'acc_chk_9001' and 'acc_crd_9002'. From her checking account (acc_chk_9001), make a 300 EUR payment towards the delinquent loan to show good faith. Given the delinquency, adjust the overdraft limit on her checking account down to 100 EUR as a precaution. Update her communication preference to 'Phone' for more direct follow-up. Finally, create a support ticket for her latest transaction ('txn_f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15') to document your intervention, with the reason 'Customer outreach regarding delinquent loan'. Report the loan's new balance, the updated overdraft limit, and the customer's credit score.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="list_active_loans_with_balances",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_9001", "acc_crd_9002"]}
            ),
            Action(
                name="make_loan_overpayment",
                kwargs={
                    "loan_id": "loan_pers_008",
                    "from_account_id": "acc_chk_9001",
                    "amount": 300.00,
                },
            ),
            Action(
                name="review_overdraft_activity_and_adjust_limit",
                kwargs={"account_id": "acc_chk_9001", "new_limit": 100.00},
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "new_channel": "Phone",
                },
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "transaction_id": "txn_f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "reason": "Customer outreach regarding delinquent loan",
                },
            ),
        ],
        outputs=['"new_loan_balance": 4950.75', '"new_overdraft_limit": 100.00', '"credit_score": 710'],
    ),
    Task(
        annotator="0",
        user_id="USER_022",
        instruction="You are a compliance officer conducting a proactive review of Gabriel Silva (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17), whose AML risk is 'Medium'. Pull his risk profile and total balance. Review all transactions on his checking account (acc_chk_18001) in the last year. Calculate his total deposits over the past six months (e.g., 2023-05-01 to 2023-10-31). Check for any support tickets related to 'Security'. Review his active mortgage (loan_mort_006). Due to his risk level and high transaction volume, enforce a KYC refresh. Reassign his relationship manager to 'rm-br-02', who specializes in high-profile clients. Finally, update his employer in his profile to 'Rio FC'. Report the customer's AML risk level, total deposits found, and the new relationship manager ID.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_18001"]}
            ),
            Action(
                name="get_total_deposits_over_period",
                kwargs={
                    "account_ids": ["acc_chk_18001"],
                    "start_date": "2023-05-01",
                    "end_date": "2023-10-31",
                },
            ),
            Action(
                name="find_recent_support_tickets_by_category",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "category": "Security"}
            ),
            Action(
                name="list_active_loans_with_balances",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                },
            ),
            Action(
                name="reassign_relationship_manager",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "relationship_manager_id": "rm-br-02",
                },
            ),
             Action(
                name="add_employer_to_customer_profile",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "employer": "Rio FC",
                },
            ),
        ],
        outputs=['"aml_risk_level": "Medium"', '"total_deposits": 0', '"relationship_manager_id": "rm-br-02"'],
    ),
    Task(
        annotator="0",
        user_id="USER_023",
        instruction="You are a business banker for entrepreneur Adetokunbo Adebayor (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23). First, check his total balance across his business accounts. He needs to pay a contractor (represented by existing 'Personal' beneficiary 'Marie Dubois' with id 'bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c' belonging to another customer, which you need to verify first) an amount of 250,000 NGN from his checking account (acc_chk_24001). Also, he wants to make a 1,000,000 NGN overpayment on his business loan (loan_biz_009) from the same account. Review all scheduled payments on his account. To support growing operations, he requests an increase of his overdraft limit on his checking account to 100,000 NGN. Finally, update his communication preference to 'App'. Report the total balance after all transactions, the new loan balance, and the new overdraft limit.",
        actions=[
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}
            ),
            Action(
                name="verify_beneficiary_exists",
                kwargs={"beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c"}
            ),
            Action(
                name="initiate_fund_transfer_to_beneficiary",
                kwargs={
                    "source_account_id": "acc_chk_24001",
                    "beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c",
                    "amount": 250000.00,
                },
            ),
            Action(
                name="make_loan_overpayment",
                kwargs={
                    "loan_id": "loan_biz_009",
                    "from_account_id": "acc_chk_24001",
                    "amount": 1000000.00,
                },
            ),
            Action(
                name="get_payment_schedule_for_account",
                kwargs={"account_id": "acc_chk_24001"},
            ),
            Action(
                name="review_overdraft_activity_and_adjust_limit",
                kwargs={"account_id": "acc_chk_24001", "new_limit": 100000.00},
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "new_channel": "App",
                },
            ),
        ],
        outputs=['"total_balance": 28750000.00', '"new_loan_balance": 6500000.00', '"new_overdraft_limit": 100000.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_024",
        instruction="You are an advisor for Kenji Tanaka (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3), who has recently relocated. Check his risk profile and total balance. He wants to split the transaction 'txn_a1b2c3d4-e5f6-7890-1234-567890abcdef-16' by moving 1500 JPY from 'acc_chk_10001' to 'acc_sav_10002'. Before updating the scheduled payment, first verify this beneficiary bene_2b1c9d8e-7f6a-5b4c-3d2e-1f0a9b8c7d6e. Then, update his existing scheduled payment (sp_c1d9b3a2-a5b4-c3d2-e1f0-a9b8c7d6e5f4) to be 250,000 JPY. Review his recent 10 transactions for anomalies. Enforce a KYC refresh due to the change in residency status. Finally, create a support ticket on his account 'acc_sav_10002' with the reason 'Inquiry about international loan payment options'. Report his risk profile, total balance, the final balance of the savings account, the new scheduled payment amount, and the KYC status.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="split_transaction_between_accounts", kwargs={
                "transaction_id": "txn_a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                "splits": [
                    {"account_id": "acc_chk_10001", "amount": 1500.00},
                    {"account_id": "acc_sav_10002", "amount": 1500.00}
                ]
            }),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_10002"}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_2b1c9d8e-7f6a-5b4c-3d2e-1f0a9b8c7d6e"}),
            Action(name="update_scheduled_payment_amount", kwargs={
                "payment_id": "sp_c1d9b3a2-a5b4-c3d2-e1f0-a9b8c7d6e5f4",
                "amount": 250000.00
            }),
            Action(name="list_recent_transactions_by_category", kwargs={
                "account_ids": ["acc_chk_10001", "acc_sav_10002"], "limit": 10
            }),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"
            }),
            Action(name="create_support_ticket_for_account", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "account_id": "acc_sav_10002",
                "reason": "Inquiry about international loan payment options"
            })
        ],
        outputs=['"risk_profile": "Low"', '"total_balance": 17500000.00', '"savings_balance": 15000000.00', '"new_payment_amount": 250000.00', '"kyc_status": "Refresh Required"'],
    ),
    Task(
        annotator="0",
        user_id="USER_025",
        instruction="You are a private banker for David Chen (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). Check his risk profile and total balance. First, check his 'Investment' accounts. Then, from his investment account (acc_inv_3002), review his last 20 transactions for context. Calculate his total deposits over the last year (2022-11-01 to 2023-10-31) from 'acc_chk_3001' and 'acc_inv_3002'. Reassign his relationship manager to 'rm006' to reflect his status as an active high-value investor. Update his employer to 'City General Hospital'. Report his investment account balance and the new relationship manager.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="get_customer_accounts_by_type",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "account_type": "Investment"},
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_inv_3002"], "limit": 20},
            ),
            Action(
                name="get_total_deposits_over_period",
                kwargs={
                    "account_ids": ["acc_chk_3001", "acc_inv_3002"],
                    "start_date": "2022-11-01",
                    "end_date": "2023-10-31",
                },
            ),
            Action(
                name="reassign_relationship_manager",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "relationship_manager_id": "rm006",
                },
            ),
            Action(
                name="add_employer_to_customer_profile",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "employer": "City General Hospital",
                },
            ),
        ],
        outputs=[
            '"investment_balance": 150000.00',
            '"relationship_manager_id": "rm006"'
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_026",
        instruction="You are a fraud analyst for Lakshmi Narayanan (a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4) with checking account 'acc_chk_5002'. Her account has an open 'Security' ticket (tkt_c1d0e9f8-e9f8-g7h6-i5j4-k3l2m1n0o9p8). First, get her risk profile and total balance. Check her loan details for loan_auto_019. Review her recent transactions. Investigate her auto loan (loan_auto_019) for any signs of fraudulent activity. Enforce a KYC refresh. Update her communication preference to 'SMS' for urgent security alerts. Finally, create a support ticket documenting all actions taken for audit purposes with the reason 'Fraud investigation and account lock audit'. Report the status of her checking account, and the KYC status.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(name="get_all_accounts_for_customer", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}),
            Action(
                name="get_loan_details",
                kwargs={"loan_id": "loan_auto_019"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": "acc_chk_5002"},
            ),
            Action(
                name="lock_account_manually",
                kwargs={"account_id": "acc_chk_5002"}
            ),
            Action(
                name="list_active_loans_with_balances",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                },
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "new_channel": "SMS",
                },
            ),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4", "account_id": "acc_chk_5002", "reason": "Fraud investigation and account lock audit"}),
        ],
        outputs=['"account_status": "Locked"', '"kyc_status": "Refresh Required"'],
    ),
    Task(
        annotator="0",
        user_id="USER_027",
        instruction="You are an advisor for Mei Lin (a1b2c3d4-e5f6-7890-1234-567890abcdef-22), who is graduating. Check her risk profile and total balance. Review her student loan (loan_stud_012). As she has secured a job, add her new employer 'Global Innovations Inc.' to her profile. She wants to start paying off her loan aggressively. Make a 5000 CNY overpayment from her checking account (acc_chk_23001). Adjust the loan's maturity date to 2031-09-01. She also wants to start saving. Check her existing scheduled payments. Check the overdraft limit on her account. To encourage saving, update her communication preference to 'App'. Report her new loan balance, her employer, and her overdraft limit.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22"}
            ),
            Action(
                name="list_active_loans_with_balances",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22"}
            ),
            Action(
                name="add_employer_to_customer_profile",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "employer": "Global Innovations Inc.",
                },
            ),
            Action(
                name="make_loan_overpayment",
                kwargs={
                    "loan_id": "loan_stud_012",
                    "from_account_id": "acc_chk_23001",
                    "amount": 5000.00,
                },
            ),
            Action(
                name="adjust_loan_payment_due_date",
                kwargs={"loan_id": "loan_stud_012", "new_due_date": "2031-09-01"},
            ),
            Action(
                name="get_payment_schedule_for_account",
                kwargs={"account_id": "acc_chk_23001"},
            ),
            Action(
                name="get_account_overdraft_limit",
                kwargs={"account_id": "acc_chk_23001"},
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "new_channel": "App",
                },
            ),
        ],
        outputs=['"new_loan_balance": 90000.00', '"employer": "Global Innovations Inc."', '"overdraft_limit": 500.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_028",
        instruction="You are a dispute specialist handling a case for John Doe (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). He claims a transaction ('txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f') was a shared expense with Jane Smith. First, get his total balance and risk profile. Create a support ticket for the transaction, noting the dispute with the reason 'Shared expense dispute'. Verify the beneficiary 'Jane Smith' (bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d) exists. As a resolution, split the txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f 35.50 from John's checking (acc_chk_1001) and 40.00 from Jane's account (simulated as his savings acc_sav_1002). Review John's recent transactions. Update his communication preference to 'Email'. Report the new balance of his checking account, the new balance of his savings account, and confirmation of the support ticket.",
        actions=[
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="create_support_ticket_for_transaction", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "transaction_id": "txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f",
                "reason": "Shared expense dispute"
            }),
            Action(name="verify_beneficiary_exists", kwargs={
                "beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d"
            }),
            # Step: Split the charge as per instruction
            Action(name="split_transaction_between_accounts", kwargs={
                "transaction_id": "txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f",
                "splits": [
                    {"account_id": "acc_chk_1001", "amount": -35.50},
                    {"account_id": "acc_sav_1002", "amount": -40.00}
                ]
            }),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_1001"}),  # New
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_1002"}),  # New
            Action(name="list_recent_transactions_by_category", kwargs={
                "account_ids": ["acc_chk_1001", "acc_sav_1002"]
            }),
            Action(name="update_customer_communication_preference", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "new_channel": "Email"
            }),
        ],
        outputs=['"checking_balance": 5230.50', '"savings_balance": 15780.00', '"ticket_created": true'],
    ),
    Task(
        annotator="0",
        user_id="USER_029",
        instruction="You are a financial wellness agent for Elena Popescu (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24). Start by checking her total balance and risk profile. Get her scheduled payments between 2023-11-01 and 2024-01-31. For her payment 'sp_a3o5b4n6-m1n0-o9p8-q7r6-s5t4u3v2w1x0', check if she has sufficient funds. She does not have a checking account, only savings (acc_sav_25001), and the system flags this as a potential issue. Review her recent transactions. As a proactive measure, create a support ticket linked to her savings account to document outreach about setting up overdraft protection with the reason 'Proactive outreach re: overdraft protection'. You also notice her communication preference is 'Mail'. Update it to 'Phone' to offer more immediate assistance. Reassign her relationship manager to 'rm-ro-09' who specializes in senior client services. Report her total balance, fund sufficiency for her next payment, and the new communication channel.",
        actions=[
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}
            ),
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}
            ),
            Action(
                name="get_scheduled_payments_due_in_range",
                kwargs={"start_date": "2023-11-01", "end_date": "2024-01-31"},
            ),
            Action(
                name="check_funds_for_next_scheduled_payment",
                kwargs={"payment_id": "sp_a3o5b4n6-m1n0-o9p8-q7r6-s5t4u3v2w1x0"},
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_sav_25001"]},
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "transaction_id": "txn_2a3b4c5d-6e7f-8g9h-0i1j-2k3l4m5n6o7p",
                    "reason": "Proactive outreach re: overdraft protection",
                },
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "new_channel": "Phone",
                },
            ),
            Action(
                name="reassign_relationship_manager",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "relationship_manager_id": "rm-ro-09",
                },
            ),
        ],
        outputs=['"total_balance": 250000.00', '"sufficient_funds": true', '"new_channel": "Phone"'],
    ),
    Task(
        annotator="0",
        user_id="USER_030",
        instruction="You are a mortgage specialist assisting Hans Müller (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). He is considering refinancing his mortgage (loan_mort_014). Start by getting his risk profile and total balance. Review all his active loans. Calculate his total deposits over the past year (e.g., 2022-11-01 to 2023-10-31). He has decided to proceed with an initial step and wants to make a 5,000 EUR overpayment from his checking account (acc_chk_8001). After the payment, check the payment schedule for his checking account. Find any 'Cancelled' support tickets he may have. Enforce a KYC refresh as part of the pre-application process for refinancing. Finally, add his employer 'AutoFabrik GmbH' to his profile to ensure it is up-to-date. Report his credit score, the new loan balance, and his KYC status.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="list_active_loans_with_balances",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="get_total_deposits_over_period",
                kwargs={
                    "account_ids": ["acc_chk_8001"],
                    "start_date": "2022-11-01",
                    "end_date": "2023-10-31",
                },
            ),
            Action(
                name="make_loan_overpayment",
                kwargs={
                    "loan_id": "loan_mort_014",
                    "from_account_id": "acc_chk_8001",
                    "amount": 5000.00,
                },
            ),
            Action(
                name="get_payment_schedule_for_account",
                kwargs={"account_id": "acc_chk_8001"},
            ),
            Action(
                name="find_recent_support_tickets_by_category",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "category": "Cancelled"},
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                },
            ),
            Action(
                name="add_employer_to_customer_profile",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "employer": "AutoFabrik GmbH",
                },
            ),
        ],
        outputs=['"credit_score": 800', '"new_loan_balance": 175000.00', '"kyc_status": "Refresh Required"'],
    ),
    Task(
        annotator="0",
        user_id="USER_031",
        instruction="You are a fraud analyst handling a complex case for customer John Doe (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). Start by checking the customer's risk profile and total balance. Review recent transactions across all of the customer's accounts ('acc_chk_1001', 'acc_sav_1002', 'acc_crd_1003'). Look for existing 'Scheduled Payment' support tickets to understand case history. Get the customer's contact methods. Update their communication preference to 'Phone'. Enforce a KYC refresh. As a precaution, lock the primary checking account (acc_chk_1001). Finally, create a new support ticket for transaction 'txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f' to document the investigation. Report the final total balance, KYC status, and the new lock status of the checking account.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_1001", "acc_sav_1002", "acc_crd_1003"]}
            ),
            Action(
                name="find_recent_support_tickets_by_category",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "category": "Scheduled Payment"}
            ),
            Action(
                name="get_customer_contact_methods",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "new_channel": "Phone"
                }
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                }
            ),
            Action(
                name="lock_account_manually",
                kwargs={
                    "account_id": "acc_chk_1001",
                }
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "transaction_id": "txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f",
                    "reason": "Fraud investigation"
                }
            ),
        ],
        outputs=['"total_balance": 18510.50', '"kyc_status": "Refresh Required"', '"account_status": "Locked"'],
    ),
    Task(
        annotator="0",
        user_id="USER_032",
        instruction="You are a loan officer handling complex restructuring for customer Maria Garcia (f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9). Start by checking her risk profile and total balance. Get loan details for loan_stud_004. Check scheduled payments due between 2023-10-01 and 2023-12-31. For her scheduled payment 'sp_e2g4b3f5-e9f8-g7h6-i5j4-k3l2m1n0o9p5', verify if there are sufficient funds. Make a $500 overpayment on her student loan (loan_stud_004) from her checking account (acc_chk_4001). Adjust the maturity date for the same loan to 2032-09-25. Finally, update her communication preference to 'App'. Report the new loan balance, and the new maturity date.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}
            ),
            Action(
                name="get_loan_details",
                kwargs={"loan_id": "loan_stud_004"}
            ),
            Action(
                name="get_scheduled_payments_due_in_range",
                kwargs={
                    "start_date": "2023-10-01",
                    "end_date": "2023-12-31"
                }
            ),
            Action(
                name="check_funds_for_next_scheduled_payment",
                kwargs={
                    "payment_id": "sp_e2g4b3f5-e9f8-g7h6-i5j4-k3l2m1n0o9p5"
                }
            ),
            Action(
                name="make_loan_overpayment",
                kwargs={
                    "loan_id": "loan_stud_004",
                    "from_account_id": "acc_chk_4001",
                    "amount": 500.00
                }
            ),
            Action(
                name="adjust_loan_payment_due_date",
                kwargs={
                    "loan_id": "loan_stud_004",
                    "new_due_date": "2032-09-25"
                }
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "new_channel": "App"
                }
            ),
        ],
        outputs=['"new_loan_balance": 24500.00', '"new_maturity_date": "2032-09-25"'],
    ),
    Task(
        annotator="0",
        user_id="USER_033",
        instruction="You are a dispute resolution officer for customer David Chen (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). Start by checking his risk profile and total balance. Review his recent transactions from 'acc_inv_3002' and 'acc_chk_3001'. Look for existing support tickets in the 'Scheduled Payment' category. Calculate total deposits for his accounts between 2023-10-01 and 2023-10-31. Apply a partial refund of $150.00 to transaction 'txn_2g7h1j4l-8h1f-2g6j-6h9l-3j4h6i1k2g7g' to resolve an issue. Create a new support ticket for the same transaction to document the resolution with the reason 'Dispute resolution'. Update the customer's communication preference to 'SMS'. Report total deposits in the period, and confirmation of the refund.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_3001", "acc_inv_3002"]}
            ),
            Action(
                name="find_recent_support_tickets_by_category",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "category": "Scheduled Payment"}
            ),
            Action(
                name="get_total_deposits_over_period",
                kwargs={
                    "account_ids": ["acc_chk_3001", "acc_inv_3002"],
                    "start_date": "2023-10-01",
                    "end_date": "2023-10-31"
                }
            ),
            Action(
                name="apply_partial_refund_to_transaction",
                kwargs={
                    "transaction_id": "txn_2g7h1j4l-8h1f-2g6j-6h9l-3j4h6i1k2g7g",
                    "refund_amount": 150.00
                }
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "transaction_id": "txn_2g7h1j4l-8h1f-2g6j-6h9l-3j4h6i1k2g7g",
                    "reason": "Dispute resolution"
                }
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "new_channel": "SMS"
                }
            ),
        ],
        outputs=['"total_deposits": 150.0', '"refund_status": "Completed"'],
    ),
    Task(
        annotator="0",
        user_id="USER_034",
        instruction="You are an account manager for Jane Smith (a1b2c3d4-e5f6-7890-1234-567890abcdef). Start by checking her risk profile and total balance. Get all her checking and savings accounts to analyze her banking structure. Retrieve the payment schedule for her checking account (acc_chk_2001). Check for any scheduled payments due between 2023-11-01 and 2024-01-01. Update her scheduled payment 'sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f' to a new amount of $750.00. Finally, update her communication preference to 'Email'. Report her total balance, the number of checking accounts, and the new payment amount.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="get_customer_accounts_by_type",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "account_type": "Checking"}
            ),
            Action(
                name="get_customer_accounts_by_type",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "account_type": "Savings"}
            ),
            Action(
                name="get_payment_schedule_for_account",
                kwargs={"account_id": "acc_chk_2001"}
            ),
            Action(
                name="get_scheduled_payments_due_in_range",
                kwargs={
                    "start_date": "2023-11-01",
                    "end_date": "2024-01-01"
                }
            ),
            Action(
                name="update_scheduled_payment_amount",
                kwargs={
                    "payment_id": "sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f",
                    "amount": 750.00
                }
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "new_channel": "Email"
                }
            ),
        ],
        outputs=['"total_balance": 25100.75', '"checking_accounts_count": 1', '"new_payment_amount": 750.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_035",
        instruction="You are a wire transfer officer for customer Oliver Williams (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5). Start by checking his risk profile and total balance. Fetch all beneficiaries of type 'Personal' and 'Business', and verify that the beneficiary with ID 'bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d' exists. Once verified, initiate a fund transfer of 50.00 GBP from his checking account (acc_chk_6001) to this beneficiary. Review his recent transactions to ensure no anomalies. After the transaction, create a support ticket using his checking account, noting the completed transfer for audit purposes with the reason 'Wire transfer to verified beneficiary'. Report a confirmation that the transfer and ticket creation were successful.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}
            ),
            Action(
                name="fetch_beneficiaries_by_relationship",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "relationship": "Personal"}
            ),
            Action(
                name="fetch_beneficiaries_by_relationship",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "relationship": "Business"}
            ),
            Action(
                name="verify_beneficiary_exists",
                kwargs={
                    "beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d"
                }
            ),
            Action(
                name="initiate_fund_transfer_to_beneficiary",
                kwargs={
                    "source_account_id": "acc_chk_6001",
                    "beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d",
                    "amount": 50.00
                }
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_6001"]}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}
            ),
            Action(
                name="create_support_ticket_for_account",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_id": "acc_chk_6001",
                    "reason": "Wire transfer to verified beneficiary"
                }
            ),
        ],
        outputs=['"transfer_status": "Completed"'],
    ),
    Task(
        annotator="0",
        user_id="USER_036",
        instruction="You are a risk analyst handling a case for Chloe Dubois (e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2). Start by checking her risk profile and total balance. Get the overdraft limit for her checking account (acc_chk_9001). Also check for her next scheduled payment sp_a2c1d9b3-f6a5-b4c3-d2e1-f0a9b8c7d6e5 on her checking account . Review her recent transactions. Look for existing support tickets under the 'Beneficiary Management' category. Adjust her overdraft limit to $50.00. Then, deactivate her credit card account (acc_crd_9002). Finally, create a new support ticket for transaction 'txn_6e7f8g9h-0i1j-2k3l-4m5n-6o7p8q9r0s1t' to document the case with the reason 'Overdraft policy enforcement'. Report the final total balance, the new overdraft limit, and the status of the credit card account.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="get_account_overdraft_limit",
                kwargs={
                    "account_id": "acc_chk_9001"
                }
            ),
            Action(name="check_funds_for_next_scheduled_payment", kwargs={"payment_id": "sp_a2c1d9b3-f6a5-b4c3-d2e1-f0a9b8c7d6e5"}),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_9001", "acc_crd_9002"]}
            ),
            Action(
                name="find_recent_support_tickets_by_category",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "category": "Beneficiary Management"}
            ),
            Action(
                name="review_overdraft_activity_and_adjust_limit",
                kwargs={
                    "account_id": "acc_chk_9001",
                    "new_limit": 50.00
                }
            ),
            Action(
                name="deactivate_account_by_request",
                kwargs={
                    "account_id": "acc_crd_9002"
                }
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "transaction_id": "txn_6e7f8g9h-0i1j-2k3l-4m5n-6o7p8q9r0s1t",
                    "reason": "Overdraft policy enforcement"
                }
            ),
        ],
        outputs=['"total_balance": 2700.00', '"new_overdraft_limit": 50.00', '"credit_card_status": "Inactive"'],
    ),
    Task(
        annotator="0",
        user_id="USER_037",
        instruction="You are a supervisor handling a data consolidation case for Kenji Tanaka (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3). Start by checking his risk profile and total balance. Merge duplicate customer records using the SSN last 4 digits '6677'. Update his employer to 'Cybernetics Corp'. Reassign his relationship manager to 'rm_premium_001'. Get his current contact methods and then update his communication preference to 'App'. Finally, create a support ticket for transaction 'txn_a1b2c3d4-e5f6-7890-1234-567890abcdef-16' to document the profile consolidation. Report the total balance, the number of profiles merged, and the new relationship manager.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="merge_duplicate_customers_by_ssn",
                kwargs={
                    "ssn_last_4": "6677"
                }
            ),
            Action(
                name="add_employer_to_customer_profile",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "employer": "Cybernetics Corp"
                }
            ),
            Action(
                name="reassign_relationship_manager",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "relationship_manager_id": "rm_premium_001"
                }
            ),
            Action(
                name="get_customer_contact_methods",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "new_channel": "App"
                }
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "transaction_id": "txn_a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "reason": "Profile consolidation"
                }
            ),
        ],
        outputs=['"total_balance": 17500000.00', '"merged_customer_ids": ["b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"]', '"new_manager": "rm_premium_001"'],
    ),
    Task(
        annotator="0",
        user_id="USER_038",
        instruction="You are a compliance officer for customer Olivia Jones (a1b2c3d4-e5f6-7890-1234-567890abcdef-16). Check her risk profile and total balance. Review her recent transactions. Split transaction 'txn_5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8g9h0i' (-60.00 AUD) by debiting -40.00 from her checking account (acc_chk_17001) and -20.00 from her savings account (acc_sav_17002). Calculate her total deposits between 2023-01-01 and 2023-12-31. Get all her checking accounts. Create a support ticket for the original split transaction for documentation with the reason 'Transaction categorization'. Update her communication preference to 'SMS'. Report her total deposits and confirmation of the split.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_17001", "acc_sav_17002"]}
            ),
            Action(
                name="split_transaction_between_accounts",
                kwargs={
                    "transaction_id": "txn_5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8g9h0i",
                    "splits": [
                        {"account_id": "acc_chk_17001", "amount": -40.00},
                        {"account_id": "acc_sav_17002", "amount": -20.00}
                    ]
                }
            ),
            Action(
                name="get_total_deposits_over_period",
                kwargs={
                    "account_ids": ["acc_chk_17001", "acc_sav_17002"],
                    "start_date": "2023-01-01",
                    "end_date": "2023-12-31"
                }
            ),
            Action(
                name="get_customer_accounts_by_type",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16", "account_type": "Checking"}
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "transaction_id": "txn_5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8g9h0i",
                    "reason": "Transaction categorization"
                }
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "new_channel": "SMS"
                }
            ),
        ],
        outputs=['"total_deposits": 0', '"split_status": "Completed"'],
    ),
    Task(
        annotator="0",
        user_id="USER_039",
        instruction="You are an international banking officer for Fatima Al-Fassi (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6). Check her risk profile and total balance. Fetch her beneficiary if 'Dubai International School' (bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f) exists. Initiate a 3,500.00 AED transfer from her checking account (acc_chk_7001) to this beneficiary. Enforce a KYC refresh. Search for existing support tickets in the 'Account Management' category. Create a new support ticket for transaction 'txn_d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13' for compliance documentation with the reason 'International compliance'. Report the total balance after the transfer, number of beneficiaries, and compliance status.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="fetch_beneficiaries_by_relationship",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "relationship": "School"}
            ),
            Action(
                name="verify_beneficiary_exists",
                kwargs={
                    "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f"
                }
            ),
            Action(
                name="initiate_fund_transfer_to_beneficiary",
                kwargs={
                    "source_account_id": "acc_chk_7001",
                    "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f",
                    "amount": 3500.00,
                }
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                }
            ),
            Action(
                name="find_recent_support_tickets_by_category",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "category": "Account Management"}
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "transaction_id": "txn_d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13",
                    "reason": "International compliance"
                }
            ),
        ],
        outputs=['"total_balance": 896500.00', '"beneficiaries_count": 1', '"compliance_status": "Refresh Required"'],
    ),
    Task(
        annotator="0",
        user_id="USER_040",
        instruction="You are a senior loan officer for Alex Petrov (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13). Check his risk profile and total balance. Get all his active loans. Check scheduled payments between 2023-11-01 and 2024-02-01. For payment 'sp_b5d7c6a8-b2c1-d0e9-f8g7-h6i5j4k3l2m1', check if there are sufficient funds. Make a 75000 RUB overpayment on his auto loan (loan_auto_007) from his checking account (acc_chk_14001). Adjust the maturity date for the same loan to 2025-10-01. Retrieve the payment schedule for his checking account. Update his communication preference to 'Phone'. Report the new maturity date.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}
            ),
            Action(
                name="list_active_loans_with_balances",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}
            ),
            Action(
                name="get_scheduled_payments_due_in_range",
                kwargs={
                    "start_date": "2023-11-01",
                    "end_date": "2024-02-01"
                }
            ),
            Action(
                name="check_funds_for_next_scheduled_payment",
                kwargs={
                    "payment_id": "sp_b5d7c6a8-b2c1-d0e9-f8g7-h6i5j4k3l2m1"
                }
            ),
            Action(
                name="make_loan_overpayment",
                kwargs={
                    "loan_id": "loan_auto_007",
                    "from_account_id": "acc_chk_14001",
                    "amount": 75000.00
                }
            ),
            Action(
                name="adjust_loan_payment_due_date",
                kwargs={
                    "loan_id": "loan_auto_007",
                    "new_due_date": "2025-10-01"
                }
            ),
            Action(
                name="get_payment_schedule_for_account",
                kwargs={"account_id": "acc_chk_14001"}
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13",
                    "new_channel": "Phone"
                }
            ),
        ],
        outputs=['"new_maturity_date": "2025-10-01"'],
    ),
    Task(
        annotator="0",
        user_id="USER_041",
        instruction="You are a relationship manager for Chloe Dubois (e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2). Her personal loan (loan_pers_008) is 'Delinquent'. Get her risk profile and total balance. Review all active loans and recent transactions from 'acc_chk_9001' and 'acc_crd_9002'. From her checking account (acc_chk_9001), make a 300 EUR payment towards the delinquent loan. Given the delinquency, adjust the overdraft limit on her checking account to 100 EUR. Update her communication preference to 'Phone'. Finally, create a support ticket for her transaction 'txn_f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15' to document your intervention with the reason 'Customer outreach regarding delinquent loan'. Report the loan's new balance, the updated overdraft limit, and the customer's credit score.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="list_active_loans_with_balances",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_9001", "acc_crd_9002"]}
            ),
            Action(
                name="make_loan_overpayment",
                kwargs={
                    "loan_id": "loan_pers_008",
                    "from_account_id": "acc_chk_9001",
                    "amount": 300.00,
                },
            ),
            Action(
                name="review_overdraft_activity_and_adjust_limit",
                kwargs={"account_id": "acc_chk_9001", "new_limit": 100.00},
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "new_channel": "Phone",
                },
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "transaction_id": "txn_f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "reason": "Customer outreach regarding delinquent loan",
                },
            ),
        ],
        outputs=['"new_loan_balance": 4950.75', '"new_overdraft_limit": 100.00', '"credit_score": 710'],
    ),
    Task(
        annotator="0",
        user_id="USER_042",
        instruction="You are a compliance officer reviewing Gabriel Silva (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17), whose AML risk is 'Medium'. Pull his risk profile and total balance. Calculate his total deposits into his checking account (acc_chk_18001) over the past six months (2023-05-01 to 2023-10-31). Check for any support tickets related to 'Security'. Review his active mortgage (loan_mort_006). Due to his risk level, enforce a KYC refresh. Reassign his relationship manager to 'rm-br-02'. Finally, update his employer in his profile to 'Rio FC'. Report the customer's AML risk level, total deposits found, and the new relationship manager ID.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}
            ),
            Action(
                name="get_total_deposits_over_period",
                kwargs={
                    "account_ids": ["acc_chk_18001"],
                    "start_date": "2023-05-01",
                    "end_date": "2023-10-31",
                },
            ),
            Action(
                name="find_recent_support_tickets_by_category",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "category": "Security"}
            ),
            Action(
                name="list_active_loans_with_balances",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                },
            ),
            Action(
                name="reassign_relationship_manager",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "relationship_manager_id": "rm-br-02",
                },
            ),
             Action(
                name="add_employer_to_customer_profile",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "employer": "Rio FC",
                },
            ),
        ],
        outputs=['"aml_risk_level": "Medium"', '"total_deposits": 0.0', '"relationship_manager_id": "rm-br-02"'],
    ),
    Task(
        annotator="0",
        user_id="USER_043",
        instruction="You are a business banker assisting Zoltan Nagy (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21). He's facing a temporary cash flow crunch. Check his total business balance and risk profile. Review his active business loan (loan_biz_016). To provide relief, adjust the loan's maturity date to 2028-03-10. Review his recent transactions on his checking account (acc_chk_22001). To provide a liquidity buffer, increase his overdraft limit to 150,000 HUF. He needs to make a critical payment to his landlord, 'Klaus Schmidt' (beneficiary_id 'bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a', which you must first verify exists). Initiate a transfer of 200,000 HUF to this beneficiary. Create a support ticket for the loan adjustment to document the forbearance. Report the new loan maturity date and the new overdraft limit",
        actions=[
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}
            ),
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}
            ),
            Action(
                name="list_active_loans_with_balances",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}
            ),
            Action(
                name="adjust_loan_payment_due_date",
                kwargs={"loan_id": "loan_biz_016", "new_due_date": "2028-03-10"},
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_22001"]}
            ),
            Action(
                name="review_overdraft_activity_and_adjust_limit",
                kwargs={"account_id": "acc_chk_22001", "new_limit": 150000.00},
            ),
            Action(
                name="verify_beneficiary_exists",
                kwargs={"beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}
            ),
            Action(
                name="initiate_fund_transfer_to_beneficiary",
                kwargs={
                    "source_account_id": "acc_chk_22001",
                    "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a",
                    "amount": 200000.00,
                },
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21",
                    "transaction_id": "loan_biz_016",
                    "reason": "Loan forbearance documentation",
                },
            ),
        ],
        outputs=['"new_maturity_date": "2028-03-10"', '"new_overdraft_limit": 150000.0'],
    ),
    Task(
        annotator="0",
        user_id="USER_044",
        instruction="You are a security analyst for Hans Müller (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). He reports identity theft. First, get his total balance and lock both his checking (acc_chk_8001) and savings (acc_sav_8002) accounts immediately. Review his recent transactions. A fraudulent profile was created with his SSN last 4 digits '1123'; merge these duplicate customers. As part of the remediation, enforce a KYC refresh. Get his contact methods and update his preference to 'Phone'. Reassign his relationship manager to 'rm-de-09', a specialist in fraud cases. Finally, create a support ticket linked to his checking account to document the identity theft case with the reason 'Identity Theft and Account Remediation'. Report the customer's total balance, the locked status of his accounts, and his new relationship manager.",
        actions=[
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="lock_account_manually",
                kwargs={"account_id": "acc_chk_8001"},
            ),
            Action(
                name="lock_account_manually",
                kwargs={"account_id": "acc_sav_8002"},
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_8001", "acc_sav_8002"]}
            ),
            Action(
                name="merge_duplicate_customers_by_ssn",
                kwargs={"ssn_last_4": "1123"},
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                },
            ),
            Action(
                name="get_customer_contact_methods",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "new_channel": "Phone",
                },
            ),
            Action(
                name="reassign_relationship_manager",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "relationship_manager_id": "rm-de-09",
                },
            ),
            Action(
                name="create_support_ticket_for_account",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "account_id": "acc_chk_8001",
                    "reason": "Identity Theft and Account Remediation",
                },
             )
        ],
        outputs=['"total_balance": 132800.5', '"accounts_locked": true', '"relationship_manager_id": "rm-de-09"'],
    ),
   Task(
        annotator="0",
        user_id="USER_045",
        instruction="You are a financial wellness agent reviewing the profile of retiree Elena Popescu (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24). Get her risk profile and total balance. Calculate her total deposits over the last 3 months (2023-08-01 to 2023-10-31) to verify her fixed income. Review all scheduled payments on her savings account (acc_sav_25001). For her payment 'sp_a3o5b4n6-m1n0-o9p8-q7r6-s5t4u3v2w1x0', check if her current balance is sufficient. Get her contact methods and update her preference from 'Mail' to 'Phone'. Create a support ticket for her savings account to document the financial review and suggestions with the reason 'Financial wellness review documentation'. Report her total deposits and her credit score.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}
            ),
            Action(
                name="get_total_deposits_over_period",
                kwargs={
                    "account_ids": ["acc_sav_25001"],
                    "start_date": "2023-08-01",
                    "end_date": "2023-10-31",
                },
            ),
            Action(
                name="get_payment_schedule_for_account",
                kwargs={"account_id": "acc_sav_25001"},
            ),
            Action(
                name="check_funds_for_next_scheduled_payment",
                kwargs={"payment_id": "sp_a3o5b4n6-m1n0-o9p8-q7r6-s5t4u3v2w1x0"},
            ),
            Action(
                name="get_customer_contact_methods",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "new_channel": "Phone",
                },
            ),
            Action(
                name="create_support_ticket_for_account",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "account_id": "acc_sav_25001",
                    "reason": "Financial wellness review documentation",
                },
            ),
        ],
        outputs=['"total_deposits": 500.00', '"credit_score": 790'],
    ),
    Task(
        annotator="0",
        user_id="USER_046",
        instruction="You are a mortgage advisor for Olivia Jones (a1b2c3d4-e5f6-7890-1234-567890abcdef-16). She wants to apply for a new mortgage. Get her risk profile and total balance. Verify her income by calculating total deposits over the last 12 months (e.g., 2022-11-01 to 2023-10-31) for all her accounts (acc_chk_17001 and acc_sav_17002). Assess her current debt by listing all active loans. Note that she has a paid-off mortgage (loan_mort_010). Review her recent spending by listing transactions from all her accounts. To ensure her profile is complete, update her employer to 'Oceanic Institute'. Finally, create a support ticket linked to her savings account (acc_sav_17002) to document the pre-qualification analysis. Report her credit score, total active loan balance, and total deposits found.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}
            ),
            Action(
                name="get_total_deposits_over_period",
                kwargs={
                    "account_ids": ["acc_chk_17001", "acc_sav_17002"],
                    "start_date": "2022-11-01",
                    "end_date": "2023-10-31",
                },
            ),
            Action(
                name="list_active_loans_with_balances",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_17001", "acc_sav_17002"]},
            ),
            Action(
                name="add_employer_to_customer_profile",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "employer": "Oceanic Institute",
                },
            ),
            Action(
                name="create_support_ticket_for_account",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "account_id": "acc_sav_17002",
                    "reason": "Mortgage pre-qualification analysis",
                },
            ),
        ],
        outputs=['"credit_score": 810', '"active_loan_balance": 0.0', '"total_deposits": 0.0'],
    ),
    Task(
        annotator="0",
        user_id="USER_047",
        instruction="You are a wire transfer officer. Customer David Chen (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) is requesting a $2,500 international wire transfer. First check their risk profile and total balance across all accounts. Review their last 20 transactions for any suspicious patterns. Verify beneficiary 'Metropolis Power & Light' (bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a) exists. Process the international wire transfer from acc_chk_3001 to this beneficiary with description 'Business payment for overseas supplier'. Enforce KYC refresh due to 'International transfer requiring enhanced verification'. Create a support ticket linked to his checking account with the reason 'Wire transfer support'. Report the customer's AML risk level and the final transaction details.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_3001"], "limit": 20}
            ),
            Action(
                name="verify_beneficiary_exists",
                kwargs={"beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a"}
            ),
            Action(
                name="initiate_fund_transfer_to_beneficiary",
                kwargs={
                    "source_account_id": "acc_chk_3001",
                    "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a",
                    "amount": 2500.00,
                    "description": "Business payment for overseas supplier"
                }
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                }
            ),
            Action(
                name="create_support_ticket_for_account",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_chk_3001",
                    "reason": "Wire transfer support"
                }),
        ],
        outputs=[
            '"aml_risk_level": "Low"',
            '"transaction_status": "Completed"'
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_048",
        instruction="You are the private banker for David Chen (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). He is setting up his estate plan. First, check his total balance and risk profile. Fetch all his 'Business' type beneficiaries. Verify that his utility provider, 'Metropolis Power & Light' (bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a), is correctly listed. He wants to update his scheduled payment to this utility (sp_b3a2c1d9-e7f6-a5b4-c3d2-e1f0a9b8c7d6) to 400.00 USD. Review his investment account (acc_inv_3002) transactions. Reassign his relationship manager to 'rm008' for specialized estate planning services. Enforce a KYC refresh. Then, create a support ticket documenting the estate planning updates with the reason 'Estate plan beneficiary and payment update'. Report the number of business beneficiaries, the new scheduled payment amount, and the new relationship manager.",
        actions=[
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="fetch_beneficiaries_by_relationship",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "relationship": "Utility Provider"},
            ),
            Action(
                name="verify_beneficiary_exists",
                kwargs={"beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a"},
            ),
            Action(
                name="update_scheduled_payment_amount",
                kwargs={
                    "payment_id": "sp_b3a2c1d9-e7f6-a5b4-c3d2-e1f0a9b8c7d6",
                    "amount": 400.00,
                },
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_inv_3002"]},
            ),
            Action(
                name="reassign_relationship_manager",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "relationship_manager_id": "rm008",
                },
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                },
            ),
            Action(
                name="create_support_ticket_for_account",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_inv_3002",
                    "reason": "Estate plan beneficiary and payment update",
                },
            ),
        ],
        outputs=['"business_beneficiaries_count": 1', '"new_payment_amount": 400.00', '"relationship_manager_id": "rm008"'],
    ),
    Task(
        annotator="0",
        user_id="USER_049",
        instruction="You are a compliance officer acting on a legal order for Mohammed Al-Masri (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25). His personal loan (loan_pers_020) is delinquent. First, check his total balance and risk profile. Also check the loan details. Immediately lock his checking account (acc_chk_26001) to secure funds. He has no beneficiaries, so you cannot set up a payment. Review his recent transactions. As required by the legal order, deactivate his checking account. Update his communication preference to 'Mail' for official correspondence. Create a support ticket linked to the transaction 'txn_3b4c5d6e-7f8g-9h0i-1j2k-3l4m5n6o7p8q' to document the legal action with the reason 'Legal account garnishment documentation'. Enforce a KYC refresh. Also retrieve his registered contact methods for legal follow-up. Report the customer's total balance, the status of his checking account, and his KYC status.",
        actions=[
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"}
            ),
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"}
            ),
            Action(
                name="get_loan_details",
                kwargs={"loan_id": "loan_pers_020"}
            ),
            Action(
                name="lock_account_manually",
                kwargs={"account_id": "acc_chk_26001"},
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_26001"]},
            ),
            Action(
                name="deactivate_account_by_request",
                kwargs={
                    "account_id": "acc_chk_26001"
                },
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "new_channel": "Mail",
                },
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "transaction_id": "txn_3b4c5d6e-7f8g-9h0i-1j2k-3l4m5n6o7p8q",
                    "reason": "Legal account garnishment documentation",
                },
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                },
            ),
            Action(
                name="get_customer_contact_methods",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                },
            ),
        ],
        outputs=['"total_balance": 450000.00', '"account_status": "Inactive"', '"kyc_status": "Refresh Required"'],
    ),
    Task(
        annotator="0",
        user_id="USER_050",
        instruction="You are a specialist assisting Aisha Khan (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12) with digital wallet integration. Check her total balance and risk profile. Review recent transactions on her checking account (acc_chk_13001). Check her overdraft limit. As part of the new service agreement, enforce a KYC refresh. Also, update her communication preference to 'App'. She has one scheduled payment (sp_a6c8d7b9-a3b2-c1d0-e9f8-g7h6i5j4k3l2); check if she has sufficient funds for it and review its details. Retrieve her contact methods for app onboarding. Finally, create a support ticket for her checking account with the reason 'Digital wallet integration'. Report her total balance, overdraft limit, and KYC status.",
        actions=[
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}
            ),
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_13001"]},
            ),
            Action(
                name="get_account_overdraft_limit",
                kwargs={"account_id": "acc_chk_13001"},
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12",
                },
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12",
                    "new_channel": "App",
                },
            ),
            Action(
                name="check_funds_for_next_scheduled_payment",
                kwargs={"payment_id": "sp_a6c8d7b9-a3b2-c1d0-e9f8-g7h6i5j4k3l2"},
            ),
            Action(
                name="create_support_ticket_for_account",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12",
                    "account_id": "acc_chk_13001",
                    "reason": "Digital wallet integration"
                }
            ),
            Action(
                name="get_payment_schedule_for_account",
                kwargs={
                    "account_id": "acc_chk_13001"
                }
            ),
            Action(
                name="get_customer_contact_methods",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"
                }
            )
        ],
        outputs=['"total_balance": 150000.00', '"overdraft_limit": 25000.00', '"kyc_status": "Refresh Required"'],
    ),
    Task(
        annotator="0",
        user_id="USER_051",
        instruction="You are onboarding a new high-net-worth client, Santiago Muñoz (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19). Get his risk profile and total balance. Review all his accounts. Calculate his total deposits over the past year (2022-11-01 to 2023-10-31). He wants to open a new Investment account. Since we can't create accounts, check his existing 'Checking' accounts instead. He wants to set up a recurring transfer to his landlord 'Klaus Schmidt' (bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a), which you must verify. Update his scheduled payment 'sp_b8j1a9i2-h6i5-j4k3-l2m1-n0o9p8q7r6s5' to 80,000 CLP. Enforce a KYC refresh and reassign his relationship manager to 'rm-cl-01', a senior wealth advisor. Report his credit score, total deposits, and new relationship manager.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_chk_20001"], "start_date": "2022-11-01", "end_date": "2023-10-31"}),
            Action(name="get_customer_accounts_by_type", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "account_type": "Checking"}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="update_scheduled_payment_amount", kwargs={"payment_id": "sp_b8j1a9i2-h6i5-j4k3-l2m1-n0o9p8q7r6s5", "amount": 80000.00}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", }),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "relationship_manager_id": "rm-cl-01"}),
        ],
        outputs=['"credit_score": 800', '"total_deposits": 0.0', '"relationship_manager_id": "rm-cl-01"'],
    ),

    # TASK 32: Deceased Client Account Management
    # EDGES: 13
    Task(
        annotator="0",
        user_id="USER_052",
        instruction="You are handling the accounts of a deceased client, Anja Novak (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18). Get her total balance. Review all her active loans and recent transactions. Find all her 'Personal' beneficiaries. Her personal loan (loan_pers_013) needs to be settled. Make a 3,500 EUR payment on the loan from her checking account (acc_chk_19001) to close it out. After settling the loan, deactivate her checking account. Create a final support ticket for her checking account to document the estate closure process with the reason 'Estate closure process documentation'. Update her communication preference to 'Mail' for legal correspondence. Report the final balance before account closure and the status of the loan and checking account.",
        actions=[
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_19001"]}),
            Action(name="fetch_beneficiaries_by_relationship", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "relationship": "Personal"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_pers_013", "from_account_id": "acc_chk_19001", "amount": 3500.00}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_chk_19001"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "account_id": "acc_chk_19001", "reason": "Estate closure process documentation"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "new_channel": "Mail"}),
        ],
        outputs=['"final_balance": 0.0', '"loan_status": "Paid Off"', '"account_status": "Inactive"'],
    ),
    Task(
        annotator="0",
        user_id="USER_053",
        instruction="You are investigating an account takeover for John Doe (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). Get his risk profile. Lock all three of his accounts (acc_chk_1001, acc_sav_1002, acc_crd_1003). Review all recent transactions. The attackers made three fraudulent transactions: 'txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f', 'txn_8b1c4d6f-2b4f-5a9d-9b3f-6d7b9c4e5a1a', and 'txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c'. Apply full refunds for all three. Check for any 'Security' related support tickets. Enforce a KYC refresh. Reassign his relationship manager to a fraud specialist ('rm008'). Create a new high-priority support ticket linked to 'txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c' and put the reason as 'Account Takeover Investigation'. Report the total amount refunded, the status of his accounts, and his new relationship manager.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_1001", "acc_sav_1002", "acc_crd_1003"]}),
            Action(name="apply_partial_refund_to_transaction", kwargs={"transaction_id": "txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f", "refund_amount": 75.50}),
            Action(name="apply_partial_refund_to_transaction", kwargs={"transaction_id": "txn_8b1c4d6f-2b4f-5a9d-9b3f-6d7b9c4e5a1a", "refund_amount": 12.75}),
            Action(name="apply_partial_refund_to_transaction", kwargs={"transaction_id": "txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c", "refund_amount": 250.00}),
            Action(name="find_recent_support_tickets_by_category", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "category": "Security"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", }),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "relationship_manager_id": "rm008"}),
            Action(name="create_support_ticket_for_transaction", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "transaction_id": "txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c", "reason": "Account Takeover Investigation"}),
        ],
        outputs=['"total_refunded": 338.25', '"accounts_status": "Locked"', '"relationship_manager_id": "rm008"'],
    ),
    Task(
        annotator="0",
        user_id="USER_054",
        instruction="You are advising Adetokunbo Adebayor (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23) on divesting from a business. Check his total balance and risk profile. He needs to pay off his business loan (loan_biz_009) of 7,500,000 NGN from his savings (acc_sav_24002). After paying the loan, deactivate his business checking account (acc_chk_24001). His scheduled payment (sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w1) is now obsolete; you can't delete it but check its status. Review his personal beneficiaries. Finally, update his employer from 'Self-Employed' to 'Consultant'. Create a support ticket linked to his saving account 'acc_sav_24002' with the reason 'Business advising'. Report his final total balance, the status of the business loan, and the status of the checking account.",
        actions=[
            Action(name="get_customer_total_balance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_biz_009", "from_account_id": "acc_sav_24002", "amount": 7500000.00}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_chk_24001"}),
            Action(name="check_funds_for_next_scheduled_payment", kwargs={"payment_id": "sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w1"}),
            Action(name="fetch_beneficiaries_by_relationship", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "relationship": "Personal"}),
            Action(name="add_employer_to_customer_profile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "employer": "Consultant"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "account_id": "acc_sav_24002", "reason": "Business advising"}),
        ],
        outputs=['"final_total_balance": 22500000.00', '"loan_status": "Paid Off"', '"checking_account_status": "Inactive"'],
    ),
    Task(
        annotator="0",
        user_id="USER_055",
        instruction="You are an auditor reviewing the account of a potential high-frequency trader, David Chen (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). Get his risk profile. Get his total balance. Review all last 100 transactions for his investment account (acc_inv_3002). Calculate total deposits into this account over the last quarter (2023-08-01 to 2023-10-31). Review his active loans. Given the high-risk activity, enforce a KYC refresh. Check his scheduled payments for 'acc_chk_3001'. Reassign his relationship manager to 'rm009', a specialist in capital markets. Create a support ticket for his investment account to document the audit with the reason 'High-frequency trading audit'. Report total deposits, and KYC status.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_inv_3002"], "limit": 100}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_inv_3002"], "start_date": "2023-08-01", "end_date": "2023-10-31"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_3001"}),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "relationship_manager_id": "rm009"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "account_id": "acc_inv_3002", "reason": "High-frequency trading audit"}),
        ],
        outputs=['"total_deposits": 150.00', '"kyc_status": "Refresh Required"'],
    ),
    Task(
        annotator="0",
        user_id="USER_056",
        instruction="You are advising Santiago Muñoz (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19) on international expansion. Check his risk profile and total balance. Review his checking account (acc_chk_20001) transactions. He needs to pay an international supplier, represented by beneficiary 'Klaus Schmidt' (bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a). Verify this beneficiary. Then, initiate a 5,000,000 CLP transfer from his checking account. To support cash flow during expansion, adjust the maturity date of his mortgage to 2036-01-01 for loan_mort_014. As this is a major business change, enforce a KYC refresh. Update his employer to 'Atacama Observatory'. Create a support ticket on his checking account with the reason 'International expansion advice'. Report his credit score, the new loan maturity date",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_20001"]}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_20001"}),
            Action(name="initiate_fund_transfer_to_beneficiary", kwargs={"source_account_id": "acc_chk_20001", "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a", "amount": 5000000.00}),
            Action(name="adjust_loan_payment_due_date", kwargs={"loan_id": "loan_mort_014", "new_due_date": "2036-01-01"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", }),
            Action(name="add_employer_to_customer_profile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "employer": "Atacama Observatory"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "account_id": "acc_chk_20001", "reason": "International expansion advice"}),
        ],
        outputs=['"credit_score": 800', '"new_maturity_date": "2036-01-01"'],
    ),
    Task(
        annotator="0",
        user_id="USER_057",
        instruction="You are a fraud analyst investigating potential elder financial exploitation for Elena Popescu (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24). Get her risk profile and total balance. Immediately lock her savings account (acc_sav_25001). Create a support ticket linked to the saving account with the reason 'Fraud Investigation'. Review her recent transactions for unusual patterns. Calculate her total deposits over the past 6 months (2023-05-01 to 2023-10-31). Check her scheduled payments. A new, unverified beneficiary ('John Doe' - bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f) has been added recently; verify this beneficiary. Her communication preference is 'Mail'; update it to 'Phone' for urgent contact. Deactivate her savings account. Report the customer's total balance, the status of the savings account, and the number of scheduled payments.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_sav_25001"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_sav_25001"]}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_sav_25001"], "start_date": "2023-05-01", "end_date": "2023-10-31"}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_sav_25001"}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "new_channel": "Phone"}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_sav_25001"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "account_id": "acc_sav_25001", "reason": "Fraud Investigation"}),
        ],
        outputs=['"total_balance": 250000.00', '"account_status": "Inactive"', '"scheduled_payments_count": 1'],
    ),
    Task(
        annotator="0",
        user_id="USER_058",
        instruction="You are underwriting a joint mortgage for David Chen (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) and Olivia Jones (a1b2c3d4-e5f6-7890-1234-567890abcdef-16). First, get the risk profile for both customers. Calculate the total balance for each. It is discovered they share an SSN last 4 ('1122'), indicating a data duplication issue; merge these customer records. After merging, get all the account for David. Review all active loans under the canonical customer. Also David asked to change his communication preference to 'Email'. Enforce a KYC refresh for the primary applicant. Create a support ticket for David Chen's investment account (acc_inv_3002) to document the joint mortgage application. Report the credit scores of both original applicants",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}),
            Action(name="merge_duplicate_customers_by_ssn", kwargs={"ssn_last_4": "1122"}),
            Action(
                name="get_all_accounts_for_customer",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "new_channel": "Email"
                }
            ),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "account_id": "acc_inv_3002", "reason": "Joint mortgage application documentation"}),
        ],
        outputs=['"david_chen_credit_score": 810', '"olivia_jones_credit_score": 810'],
    ),
    Task(
        annotator="0",
        user_id="USER_059",
        instruction="You are assisting farmer Liam O'Connor (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11) with seasonal planning. Get his total balance and risk profile. He wants to make a 3000 EUR overpayment on his business loan (loan_biz_005) from his checking account (acc_chk_12001). After the payment, adjust the loan's maturity date to 2027-06-01 to align with the next harvest. Review his recent transactions. Increase his overdraft limit on the checking account to 500 EUR for operational flexibility. He needs to pay 'London Electricity Co.' (bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d); verify this beneficiary. Check his existing scheduled payments. Update his communication preference to 'Phone'. Report the new loan balance, the new overdraft limit, and his credit score.",
        actions=[
            Action(name="get_customer_total_balance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_biz_005", "from_account_id": "acc_chk_12001", "amount": 3000.00}),
            Action(name="adjust_loan_payment_due_date", kwargs={"loan_id": "loan_biz_005", "new_due_date": "2027-06-01"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_12001"]}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_12001", "new_limit": 500.00}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_12001"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "new_channel": "Phone"}),
        ],
        outputs=['"new_loan_balance": 42150.90', '"new_overdraft_limit": 500.00', '"credit_score": 720'],
    ),
    Task(
        annotator="0",
        user_id="USER_060",
        instruction=("You are a financial advisor for Alex Petrov (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13), who recently completed bankruptcy. Start by obtaining his risk profile and total balance. Review all loans from the account 'acc_chk_14001', noting current balances, especially verifying the status of the auto loan (loan_auto_015). Check scheduled payments on his checking account (acc_chk_14001) and identify any missed or overdue payments. Update his employer information to 'Global Analytics' and add this to his customer profile. Enforce a KYC refresh as part of his recovery plan. Additionally, review his account overdraft limits. Finally, update his communication preference to 'Email' and create a support ticket for the account summarizing the recovery plan with the reason 'Recovery plan summary'. Report his total balance, loans summary, scheduled payments details, employer info, overdraft limits, and confirmation of communication preference update."),
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="get_loan_details", kwargs={"loan_id": "loan_auto_015"}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_14001"}),
            Action(name="add_employer_to_customer_profile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "employer": "Global Analytics"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="get_account_overdraft_limit", kwargs={"account_id": "acc_chk_14001"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "new_channel": "Email"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "account_id": "acc_chk_14001", "reason": "Recovery plan summary"}),
        ],
        outputs=[
            '"total_balance": 3500000.00',
            '"loans_summary": "Auto loan paid off; other loans current"',
            '"scheduled_payments_status": "No overdue payments"',
            '"employer": "Global Analytics"',
            '"checking_overdraft_limit": 10000.0',
            '"communication_preference_updated": true'
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_061",
        instruction=("You are advising Jane Smith (a1b2c3d4-e5f6-7890-1234-567890abcdef), a Canadian graphic designer. Start by getting her risk profile and total balance. She has received a large deposit into her checking account (acc_chk_2001). Verify her 'Family' type beneficiary 'John Doe' (bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f). She has a scheduled payment 'sp_e5m7b6l8-k3l2-m1n0-o9p8-q7r6s5t4u3v2'; check for sufficient funds. Update this payment amount to 400 CAD. Enforce a KYC refresh since she is a retail customer. Create a support ticket for her student loan (loan_stud_012) with the reason 'Inquiry about student loan deferment options'. Report her total balance, the new scheduled payment amount, and her KYC status."),
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="verify_beneficiary_exists",
                kwargs={"beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}
            ),
            Action(
                name="check_funds_for_next_scheduled_payment",
                kwargs={"payment_id": "sp_e5m7b6l8-k3l2-m1n0-o9p8-q7r6s5t4u3v2"}
            ),
            Action(
                name="update_scheduled_payment_amount",
                kwargs={"payment_id": "sp_e5m7b6l8-k3l2-m1n0-o9p8-q7r6s5t4u3v2", "amount": 400.00}
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "transaction_id": "loan_stud_012",
                    "reason": "Inquiry about student loan deferment options"
                }
            ),
        ],
        outputs=[
            '"total_balance": 25100.75',  # sum of checking + savings: 3100.75 + 22000.00
            '"new_payment_amount": 400.00',
            '"kyc_status": "Refresh Required"'
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_062",
        instruction="You are proactively managing your relationship with Fatima Al-Fassi (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6). Get her risk profile and total balance. Review her recent transactions across all accounts (acc_chk_7001, acc_sav_7002) for the last 50 transactions. You notice fewer investment-related transactions. Review her active mortgage (loan_mort_018) to check its status. As a proactive gesture, increase the overdraft limit on her checking account to 7,500 AED. Check her scheduled payments. To personalize her service, reassign her to a senior private banker ('rm-ae-03'). Update her communication preference to 'App'. Create a support ticket related to her checking account with the reason 'Account consultation'. Report her total balance, the new overdraft limit, and her new relationship manager.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_7001", "acc_sav_7002"], "limit": 50}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_7001", "new_limit": 7500.00}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_7001"}),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "relationship_manager_id": "rm-ae-03"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "new_channel": "App"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "account_id": "acc_chk_7001", "reason": "Account consultation"}),
        ],
        outputs=['"total_balance": 900000.00', '"new_overdraft_limit": 7500.00', '"relationship_manager_id": "rm-ae-03"'],
    ),
    Task(
        annotator="0",
        user_id="USER_063",
        instruction="You are advising Anja Novak (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18) on debt consolidation. Get her risk profile and total balance. Review all her active loans. She wants to pay off her personal loan (loan_pers_013) immediately from her checking account (acc_chk_19001). After paying it off, review the scheduled payments on her checking account. She has no other loans to consolidate. To help her credit score, check the overdraft limit on her account. To finalize the plan, update her employer to 'Ljubljana High School' and communication preference to 'SMS'. Create a support ticket related to her checking account with the reason 'Debt consolidation'. Report her credit score and the status of the personal loan.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_pers_013", "from_account_id": "acc_chk_19001", "amount": 3500.00}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_19001"}),
            Action(name="get_account_overdraft_limit", kwargs={"account_id": "acc_chk_19001"}),
            Action(name="add_employer_to_customer_profile", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "employer": "Ljubljana High School"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "new_channel": "SMS"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "account_id": "acc_chk_19001", "reason": "Debt consolidation"}),
        ],
        outputs=['"credit_score": 740', '"loan_status": "Paid Off"'],
    ),
    Task(
        annotator="0",
        user_id="USER_064",
        instruction="You are conducting an AML audit for Jane Smith (a1b2c3d4-e5f6-7890-1234-567890abcdef), who holds accounts in multiple currencies (USD and CAD). Get her risk profile and total balance (be aware of different currencies). Review all transactions across all her accounts (acc_chk_2001, acc_sav_2002). Calculate her total deposits in the last quarter (2023-08-01 to 2023-10-31). Check her active loans. Due to cross-border activity, enforce a KYC refresh. She has a scheduled payment (sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f); check for sufficient funds. Finally, create a support ticket based on her checking account (acc_chk_2001) with the reason 'AML audit'. Retrieve her contact methods for escalation if needed. Report her AML risk level and her KYC status.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_2001", "acc_sav_2002"]}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_chk_2001", "acc_sav_2002"], "start_date": "2023-08-01", "end_date": "2023-10-31"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="check_funds_for_next_scheduled_payment", kwargs={"payment_id": "sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "account_id": "acc_chk_2001", "reason": "AML audit"}),
            Action(name="get_customer_contact_methods", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
        ],
        outputs=['"aml_risk_level": "Low"', '"kyc_status": "Refresh Required"'],
    ),
    Task(
        annotator="0",
        user_id="USER_065",
        instruction="You are a fraud analyst. Customer John Doe (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) has reported suspicious activity. First check their risk profile and review the last 25 transactions across all accounts. You've identified transaction 'txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c' for -$250 as potentially fraudulent. Create a high-priority fraud support ticket for this transaction with the reason 'Unauthorized online charge'. Enforce a KYC refresh for the customer. Immediately lock the checking account acc_chk_1001 due to the ongoing investigation. Report the number of transactions reviewed and the total amount of the suspicious transaction.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_1001", "acc_sav_1002", "acc_crd_1003"], "limit": 25}
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "transaction_id": "txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c",
                    "reason": "Unauthorized online charge"
                }
            ),
            Action(
                name="enforce_kyc_refresh_for_customer",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                }
            ),
            Action(
                name="lock_account_manually",
                kwargs={
                    "account_id": "acc_chk_1001"
                }
            ),
        ],
        outputs=['"transactions_reviewed": 8', '"suspicious_amount": -250.00', '"account_locked": true'],
    ),
    Task(
        annotator="0",
        user_id="USER_066",
        instruction="You are conducting an annual financial review for Hans Müller (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). Start by retrieving all his account details using his customer ID. Then, get his risk profile and total balance. Calculate his total deposits over the last 12 months (2022-11-01 to 2023-10-31) across all accounts. Review all his active loans. He wants to make a year-end overpayment of 5,000 EUR on his mortgage (loan_mort_014) from his savings account (acc_sav_8002). Review his scheduled payments on his checking account. Find any 'Resolved' support tickets from the past year. Enforce his annual KYC refresh. Finally, create a new support ticket for his checking account to summarize the annual review with reason 'Annual Financial Review Summary 2023'. Report his credit score, the new mortgage balance, and his total deposits for the year.",
        actions=[
            Action(name="get_all_accounts_for_customer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_chk_8001", "acc_sav_8002"], "start_date": "2022-11-01", "end_date": "2023-10-31"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_mort_014", "from_account_id": "acc_sav_8002", "amount": 5000.00}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="find_recent_support_tickets_by_category", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "category": "Resolved"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", }),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "account_id": "acc_chk_8001", "reason": "Annual Financial Review Summary 2023"}),
        ],
        outputs=['"credit_score": 800', '"new_mortgage_balance": 175000.00', '"total_deposits_2023": 0.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_067",
        instruction="You are a credit analyst processing a loan application. Customer Jane Smith (a1b2c3d4-e5f6-7890-1234-567890abcdef) has applied for a mortgage. Check their risk profile and total balance across all accounts. Review their existing active loan obligations and contact methods. Update their communication preference to 'Email'. Add 'Creative Minds LLC' as employer in their profile. Check their overdraft limit on acc_chk_2001 to assess creditworthiness. Report the customer's credit score, total balance, existing active loan count, and overdraft limit.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="list_active_loans_with_balances",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="get_customer_contact_methods",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "new_channel": "Email"
                }
            ),
            Action(
                name="add_employer_to_customer_profile",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "employer": "Creative Minds LLC"
                }
            ),
            Action(
                name="get_account_overdraft_limit",
                kwargs={"account_id": "acc_chk_2001"}
            ),
        ],
        outputs=['"credit_score": 820', '"total_balance": 25100.75', '"existing_loans_count": 0', '"overdraft_limit": 250.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_068",
        instruction="You are a financial planner for IT contractor Lakshmi Narayanan (a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4) with accounts of 'acc_chk_5002' for checking and 'acc_sav_5001' for saving. Check her risk profile and total balance. Calculate her total deposits for both 'acc_chk_5002' and 'acc_sav_5001' over the last 6 months (2023-05-01 to 2023-10-31) to analyze her income stream. Review her active auto loan (loan_auto_019). She wants to make a 200,000 INR overpayment on this loan from her savings account (acc_sav_5001). Check her scheduled payments on her checking account. She has an open ticket (tkt_c1d0e9f8-e9f8-g7h6-i5j4-k3l2m1n0o9p8) with the category 'Security'; check its details. Update her employer to 'Global Tech Services'. Reassign her relationship manager to 'rm-in-02'. Report her credit score.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_sav_5001", "acc_chk_5002"], "start_date": "2023-05-01", "end_date": "2023-10-31"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_auto_019", "from_account_id": "acc_sav_5001", "amount": 200000.00}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_5002"}),
            Action(name="find_recent_support_tickets_by_category", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4", "category": "Security"}),
            Action(name="add_employer_to_customer_profile", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4", "employer": "Global Tech Services"}),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4", "relationship_manager_id": "rm-in-02"}),
        ],
        outputs=['"credit_score": 790'],
    ),
    Task(
        annotator="0",
        user_id="USER_069",
        instruction="You are a credit counselor for Maria Garcia (f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9), who has a low credit score. Get her risk profile and total balance. Review her active loans using her customer id. Check her overdraft limit on her checking account (acc_chk_4001). Review her recent transactions. Her KYC status is 'Pending'; enforce a KYC refresh to get it updated. Update her employer to 'State University'. She has one scheduled payment ('sp_e2g4b3f5-e9f8-g7h6-i5j4-k3l2m1n0o9p5'); check if she has sufficient funds. Create a support ticket for her student loan (loan_stud_004) with the reason 'Inquiry about income-driven repayment plans'. Also update her communication preference to 'Email'. Report her credit score, KYC status, and the overdraft limit on her account.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}),
            Action(name="get_account_overdraft_limit", kwargs={"account_id": "acc_chk_4001"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_4001"]}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9", }),
            Action(name="add_employer_to_customer_profile", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9", "employer": "State University"}),
            Action(name="check_funds_for_next_scheduled_payment", kwargs={"payment_id": "sp_e2g4b3f5-e9f8-g7h6-i5j4-k3l2m1n0o9p5"}),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "new_channel": "Email"
                }
            ),
            Action(name="create_support_ticket_for_transaction", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9", "transaction_id": "loan_stud_004", "reason": "Inquiry about income-driven repayment plans"}),
        ],
        outputs=['"credit_score": 690', '"kyc_status": "Refresh Required"', '"overdraft_limit": 100.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_070",
        instruction="You are handling account closures for Sofia Andersson (e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14), who is moving abroad. Get her risk profile and total balance. She has a paid-off auto loan (loan_auto_015); review her other loans. She wants to transfer her entire checking balance (45000 SEK from acc_chk_15001) to 'Marie Dubois' (bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c), which you must first verify. After the transfer, deactivate her checking account. Review her scheduled payments. Find any support tickets related to 'Beneficiary Management'. Update her communication preference to 'Email' for final statements. Report her final checking account balance, the status of the account, and her credit score.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14"}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c"}),
            Action(name="initiate_fund_transfer_to_beneficiary", kwargs={"source_account_id": "acc_chk_15001", "beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c", "amount": 45000.00}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_chk_15001"}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_15001"}),
            Action(name="find_recent_support_tickets_by_category", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14", "category": "Beneficiary Management"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14", "new_channel": "Email"}),
        ],
        outputs=['"final_checking_balance": 0.00', '"account_status": "Inactive"', '"credit_score": 750'],
    ),
    Task(
        annotator="0",
        user_id="USER_071",
        instruction="You are settling the estate of Hans Müller (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). Get his risk profile and total balance; pay 125,000 EUR from savings (acc_sav_8002) to settle mortgage (loan_mort_014). Cancel landlord scheduled payment (sp_d9b3a2c1-b4c3-d2e1-f0a9-b8c7d6e5f4a3) on checking (acc_chk_8001) by setting amount to 0. Find all 'Resolved' support tickets; deactivate checking (acc_chk_8001), savings (acc_sav_8002), and investment (acc_inv_3002) accounts. Update communication preference to 'Mail'. Create a final support ticket for estate closure linked to acc_inv_3002 with the reason 'Estate Closure Documentation'. Report investment balance, all account statuses, and updated scheduled payment amount.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_mort_014", "from_account_id": "acc_sav_8002", "amount": 125000.00}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="update_scheduled_payment_amount", kwargs={"payment_id": "sp_d9b3a2c1-b4c3-d2e1-f0a9-b8c7d6e5f4a3", "amount": 0.00}),
            Action(name="find_recent_support_tickets_by_category", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "category": "Resolved"}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_sav_8002"}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_inv_3002"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "new_channel": "Mail"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "account_id": "acc_inv_3002", "reason": "Estate Closure Documentation"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_inv_3002"}),
        ],
        outputs=['"investment_balance": 150000.00', '"all_accounts_status": "Inactive"', '"scheduled_payment_amount": 0.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_072",
        instruction="You are auditing and consolidating the profiles of Jane Smith (a1b2c3d4-e5f6-7890-1234-567890abcdef) and John Doe (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), who are business partners. First get all their accounts. Get the risk profile and total balance for both. For the canonical profile, review all transactions across all accounts ('acc_chk_2001', 'acc_sav_2002', 'acc_chk_1001', 'acc_sav_1002', 'acc_crd_1003'). Calculate total deposits over the past year (2022-11-01 to 2023-10-31). Review all active loans for Jane Smith's account. Enforce a KYC refresh to Jane Smith's account and also assign the relationship manager to 'rm010', an international specialist. Check the schedulued payment for Jane's account. Deactivate John Doe's credit card (acc_crd_1003). Report the credit scores of both individuals, the new combined total balance, and the status of the deactivated account.",
        actions=[
            Action(name="get_all_accounts_for_customer", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="get_all_accounts_for_customer", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_2001", "acc_sav_2002", "acc_chk_1001", "acc_sav_1002", "acc_crd_1003"]}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_chk_2001", "acc_sav_2002", "acc_chk_1001", "acc_sav_1002", "acc_crd_1003"], "start_date": "2022-11-01", "end_date": "2023-10-31"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "relationship_manager_id": "rm010"}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_crd_1003"}),
        ],
        outputs=['"jane_smith_credit_score": 820', '"john_doe_credit_score": 780', '"new_combined_balance": 43611.25', '"account_acc_crd_1003_status": "Inactive"'],
    ),
    Task(
        annotator="0",
        user_id="USER_073",
        instruction="You are investigating potential money laundering for Mohammed Al-Masri (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25). His personal loan (loan_pers_020) is delinquent. Get his risk profile. Immediately lock his checking account (acc_chk_26001). Calculate his total deposits over the past 3 months (2023-08-01 to 2023-10-31). Review all his recent transactions. Check his scheduled payments. Get his contact methods and change his preference to 'Phone' for immediate contact. Deactivate his checking account. Reassign his manager to a high-risk specialist ('rm-eg-04'). Enforce an immediate KYC refresh. Create a high-priority support ticket for the account to formally document the case escalation with the reason 'AML Case Escalation'. Report the customer's AML risk level, the total deposits found, and the account status.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_chk_26001"}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_chk_26001"], "start_date": "2023-08-01", "end_date": "2023-10-31"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_26001"]}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_26001"}),
            Action(name="get_customer_contact_methods", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25", "new_channel": "Phone"}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_chk_26001"}),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25", "relationship_manager_id": "rm-eg-04"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25", }),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25", "account_id": "acc_chk_26001", "reason": "AML Case Escalation"}),
        ],
        outputs=['"aml_risk_level": "Low"', '"total_deposits": 0.0', '"account_status": "Inactive"'],
    ),
    Task(
        annotator="0",
        user_id="USER_074",
        instruction="You are managing the full portfolio exit for Fatima Al-Fassi (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6). Get her total balance and risk profile. First, pay off her mortgage (loan_mort_018) balance of 750000 AED from her savings account (acc_sav_7002). Then, she plans to send her remaining savings and checking balances to her external business, 'Dubai International School' (bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f), which you must verify. Initiate a transfer for 150000 from her checking account (acc_chk_7001) to the beneficiary account. After transfers, deactivate both accounts. Review her scheduled payments. Find any 'Security' related support tickets. Update her communication preference to 'Mail' for final legal notices. Report the final status of both accounts.",
        actions=[
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_mort_018", "from_account_id": "acc_sav_7002", "amount": 750000.00}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f"}),
            Action(name="initiate_fund_transfer_to_beneficiary", kwargs={"source_account_id": "acc_chk_7001", "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f", "amount": 150000.00}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_sav_7002"}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_chk_7001"}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_7001"}),
            Action(name="find_recent_support_tickets_by_category", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "category": "Security"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "new_channel": "Mail"}),
        ],
        outputs=['"savings_account_status": "Inactive"', '"checking_account_status": "Inactive"'],
    ),
    Task(
        annotator="0",
        user_id="USER_075",
        instruction="You are advising tech entrepreneur John Doe (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) on exercising stock options. Get his risk profile and total balance. First, he needs to free up capital by paying off his auto loan (loan_auto_002) of 5000.50 USD from his checking account (acc_chk_1001). He needs more liquidity; split payment from transaction 'txn_7a2b5e8g-3c5a-6b1e-1c4g-7e8c1d5f6b2b' such that 750 USD is reassigned from the savings account (acc_sav_1002) and the remaining 750 USD to the checking account (acc_chk_1001). Review the last 30 transactions on his credit card (acc_crd_1003). Check his scheduled payments on his checking account. Adjust the overdraft limit on his checking account to 1,000 USD to handle the large sums. Enforce a KYC refresh due to the significant change in financial status. Reassign his relationship manager to 'rm005', who handles high-net-worth tech clients. Report the status of his auto loan, and his new overdraft limit.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_auto_002", "from_account_id": "acc_chk_1001", "amount": 5000.50}),
            Action(name="split_transaction_between_accounts", kwargs={"transaction_id": "txn_7a2b5e8g-3c5a-6b1e-1c4g-7e8c1d5f6b2b", "splits": [{"account_id": "acc_sav_1002", "amount": 750.00}, {"account_id": "acc_chk_1001", "amount": 750.00}]}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_crd_1003"], "limit": 30}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_1001", "new_limit": 1000.00}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "relationship_manager_id": "rm005"}),
        ],
        outputs=['"loan_status": "Paid Off"', '"new_overdraft_limit": 1000.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_076",
        instruction=("You are managing asset consolidation for David Chen (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). Get his risk profile and total balance. Make a payment on his mortgage loan (loan_mort_001) from his investment account (acc_inv_3002), for 125,000.00 as specified. Check total deposits to investment account from 2023-10-22 to 2023-10-29. Review all scheduled payments on investment account (acc_inv_3002). Fetch his 'Business' beneficiaries and verify 'Metropolis Power & Light' (bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a). Reassign his relationship manager to 'rm010'. Enforce KYC refresh. Finally, report the mortgage loan status."),
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_mort_001", "from_account_id": "acc_inv_3002", "amount": 125000.00}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_inv_3002"], "start_date": "2023-10-22", "end_date": "2023-10-29"}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_inv_3002"}),
            Action(name="fetch_beneficiaries_by_relationship", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "relationship": "Business"}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a"}),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "relationship_manager_id": "rm010"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="get_loan_details", kwargs={"loan_id": "loan_mort_001"}),
        ],
        outputs=['"mortgage_status": "Active"'],
    ),
    Task(
        annotator="0",
        user_id="USER_077",
        instruction="You are investigating potential structured payments for Zoltan Nagy (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21). Get his risk profile and total balance. Review his last 50 transactions on his checking account (acc_chk_22001). Calculate his total deposits over the past year (2022-11-01 to 2023-10-31). He has a business loan (loan_biz_016); review its status. His profile shows many small, regular scheduled payments; review the payment schedule for his account. As a precaution, immediately lock his checking account. Due to the suspicious pattern, deactivate the account. Enforce an immediate KYC refresh. Reassign his relationship manager to 'rm-hu-02', a high-risk specialist. Update his communication preference to 'Mail' for legal notifications. Create a high-priority support ticket for the account 'acc_chk_22001' to formally document the case escalation with the reason 'AML Case Escalation: Structured Payments'. Report the customer's AML risk level, the number of scheduled payments found, and the account status.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_22001"], "limit": 50}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_chk_22001"], "start_date": "2022-11-01", "end_date": "2023-10-31"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_22001"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_chk_22001"}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_chk_22001"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", }),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", "relationship_manager_id": "rm-hu-02"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", "new_channel": "Mail"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", "account_id": "acc_chk_22001", "reason": "AML Case Escalation: Structured Payments"}),
        ],
        outputs=['"aml_risk_level": "Low"', '"scheduled_payments_count": 1', '"account_status": "Inactive"'],
    ),
    Task(
        annotator="0",
        user_id="USER_078",
        instruction="You are a payment processor. Customer John Doe (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) with these accounts acc_chk_1001, acc_sav_1002, acc_crd_1003 has requested changes to their scheduled payments. Check their total balance and review the last 20 transactions across all accounts. Get scheduled payments due between 2023-11-01 and 2023-11-30. Check if they have sufficient funds for the payment 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d'. Update that same scheduled payment to $350. Finally, update the customer's communication preference to 'SMS'. Report the total balance and the fund availability status for the specified payment.",
        actions=[
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_1001", "acc_sav_1002", "acc_crd_1003"], "limit": 20}
            ),
            Action(
                name="get_scheduled_payments_due_in_range",
                kwargs={"start_date": "2023-11-01", "end_date": "2023-11-30"}
            ),
            Action(
                name="check_funds_for_next_scheduled_payment",
                kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}
            ),
            Action(
                name="update_scheduled_payment_amount",
                kwargs={
                    "payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d",
                    "amount": 350.00
                }
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "new_channel": "SMS"
                }
            ),
        ],
        outputs=['"total_balance": 18510.50', '"sufficient_funds": true'],
    ),
    Task(
        annotator="0",
        user_id="USER_079",
        instruction="You are assisting Adetokunbo Adebayor (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23), whose business has failed. Get his risk profile and total balance. Review all his active loans. He will use his savings (acc_sav_24002) to make a partial overpayment of 5,000,000 NGN on his business loan (loan_biz_009). Adjust the maturity date of the loan to 2028-03-20 to lower his payments. Review his scheduled payment ('sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w1'); since the business is closed, update its amount to 0. Reduce his checking account (acc_chk_24001) overdraft limit to the minimum (5000 NGN). Deactivate his business savings account (acc_sav_24002). Update his employer from 'Self-Employed' to 'Unemployed'. Create a support ticket linked to acc_sav_24002 to document the restructuring agreement with the reason 'Debt restructuring and forbearance plan'. Report the remaining loan balance, and the new overdraft limit.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_biz_009", "from_account_id": "acc_sav_24002", "amount": 5000000.00}),
            Action(name="adjust_loan_payment_due_date", kwargs={"loan_id": "loan_biz_009", "new_due_date": "2028-03-20"}),
            Action(name="update_scheduled_payment_amount", kwargs={"payment_id": "sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w1", "amount": 0.00}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_24001", "new_limit": 5000.00}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_sav_24002"}),
            Action(name="add_employer_to_customer_profile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "employer": "Unemployed"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "account_id": "acc_sav_24002", "reason": "Debt restructuring and forbearance plan"}),
        ],
        outputs=['"remaining_loan_balance": 2500000.00', '"new_overdraft_limit": 5000.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_080",
        instruction="You are managing the profile of newly identified Politically Exposed Person (PEP), Fatima Al-Fassi (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6). Get her risk profile. Immediately enforce a KYC refresh. Reassign her to 'rm-ae-04', a PEP specialist. Temporarily lock her savings account (acc_sav_7002) for a security review. Review all transactions on her checking account (acc_chk_7001) for the last 100 transactions. Calculate total deposits over the period of '2023-05-01' to '2023-10-31.  Reduce her checking overdraft limit to zero. Fetch and review all her 'Business' beneficiaries. After review, update her communication preference to 'Email' for a clear audit trail. Create a high-priority support ticket for her account acc_chk_7001 to document the PEP status change and actions taken where the reason is 'PEP Status Change and Profile Security Enhancement'. Report her AML risk level and the new overdraft limit.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", }),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "relationship_manager_id": "rm-ae-04"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_sav_7002"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_7001"], "limit": 100}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_chk_7001"], "start_date": "2023-05-01", "end_date": "2023-10-31"}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_7001", "new_limit": 0.00}),
            Action(name="fetch_beneficiaries_by_relationship", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "relationship": "Business"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "new_channel": "Email"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "account_id": "acc_chk_7001", "reason": "PEP Status Change and Profile Security Enhancement"}),
        ],
        outputs=['"aml_risk_level": "Low"', '"new_overdraft_limit": 0.0'],
    ),
    Task(
        annotator="0",
        user_id="USER_081",
        instruction="You are investigating a fraud ring involving customers John Doe (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) and Jane Smith (a1b2c3d4-e5f6-7890-1234-567890abcdef). Get the risk profiles and total balances for both. A suspicious P2P transfer between them has been flagged ('txn_7b8c9d0e-1f2a-3b4c-5d6e-7f8g9h0i1j2k'). Immediately lock all accounts for both customers (John: acc_chk_1001, acc_sav_1002; Jane: acc_chk_2001, acc_sav_2002). Review all recent transactions for both to identify other collusion. You've confirmed the P2P transfer was fraudulent. As the primary fraudster, deactivate all of John Doe's accounts. For Jane Smith, enforce an immediate KYC refresh. Reassign both customers to a high-risk specialist ('rm011'). Create support ticket for both customer documenting the fraud ring takedown with the reason 'Fraud Ring Takedown Documentation'. Report Jane Smith's new total balance, the status of John Doe's accounts, and the new relationship manager.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_sav_2002"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_1001", "acc_sav_1002"]}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_2001", "acc_sav_2002"]}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", }),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "relationship_manager_id": "rm011"}),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "relationship_manager_id": "rm011"}),
            Action(name="create_support_ticket_for_transaction", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "transaction_id": "txn_7b8c9d0e-1f2a-3b4c-5d6e-7f8g9h0i1j2k", "reason": "Fraud Ring Takedown Documentation"}),
            Action(name="create_support_ticket_for_transaction", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "transaction_id": "txn_7b8c9d0e-1f2a-3b4c-5d6e-7f8g9h0i1j2k", "reason": "Fraud Ring Takedown Documentation"}),
        ],
        outputs=['"jane_smith_total_balance": 25100.75', '"john_doe_accounts_status": "Inactive"', '"new_relationship_manager": "rm011"'],
    ),
    Task(
        annotator="0",
        user_id="USER_082",
        instruction="You are advising Adetokunbo Adebayor (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23) on a corporate divestiture. Get his risk profile and total balance. To free up capital, he must pay off his 7,500,000 NGN business loan (loan_biz_009). Make a 7,500,000 NGN payment from his business savings (acc_sav_24002). After the loan is paid, deactivate the now-empty savings account. Review his scheduled payment (sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w1) and pause it. Check his 'Business' type beneficiaries. Check his overdraft limit on acc_chk_24001; reduce it to 50,000 NGN. Update his employer to 'A.A. Consulting'. Create a support ticket for the account 'acc_chk_24001' to document the divestiture payoff with the reason 'Loan Payoff During Corporate Divestiture'. Report the status of the business loan, and the new overdraft limit.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_biz_009", "from_account_id": "acc_sav_24002", "amount": 7500000.00}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_sav_24002"}),
            Action(name="update_scheduled_payment_amount", kwargs={"payment_id": "sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w1", "amount": 0.00}), # Simulating pause
            Action(name="fetch_beneficiaries_by_relationship", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "relationship": "Business"}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_24001", "new_limit": 50000.00}),
            Action(name="add_employer_to_customer_profile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "employer": "A.A. Consulting"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "account_id": "acc_chk_24001", "reason": "Loan Payoff During Corporate Divestiture"}),
        ],
        outputs=['"loan_status": "Paid Off"', '"new_overdraft_limit": 50000.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_083",
        instruction="You are assisting Gabriel Silva (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17), who has been affected by a natural disaster in Rio. Get his risk profile and total balance. Immediately lock his checking account (acc_chk_18001) for security. Review his active mortgage (loan_mort_006). To provide forbearance, adjust the loan's maturity date forward by three months to 2039-02-10. Review his recent transactions; you find a recent transaction 'txn_6a7b8c9d-0e1f-2a3b-4c5d-6e7f8g9h0i1j' for -200.00 BRL which can be refunded to help him. Increase his overdraft limit to 20,000 BRL for emergency funds. Get his contact methods and update his preference to 'SMS' for critical alerts. Find any 'Security' related support tickets. After the initial actions, create a new support ticket documenting all disaster relief actions taken with the reason 'Natural Disaster Financial Relief Package Applied'. Report the new loan maturity date, the new overdraft limit",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_chk_18001"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="adjust_loan_payment_due_date", kwargs={"loan_id": "loan_mort_006", "new_due_date": "2039-02-10"}),
            Action(name="apply_partial_refund_to_transaction", kwargs={"transaction_id": "txn_6a7b8c9d-0e1f-2a3b-4c5d-6e7f8g9h0i1j", "refund_amount": 200.00}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_18001", "new_limit": 20000.00}),
            Action(name="get_customer_contact_methods", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "new_channel": "SMS"}),
            Action(name="find_recent_support_tickets_by_category", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "category": "Security"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "account_id": "acc_chk_18001", "reason": "Natural Disaster Financial Relief Package Applied"}),
        ],
        outputs=['"new_maturity_date": "2039-02-10"', '"new_overdraft_limit": 20000.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_084",
        instruction="You are a specialist handling a Power of Attorney (POA) request. Hans Müller (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1) has POA for his mother, Elena Popescu (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24). Get the risk profiles and total balances for both. Verify Elena's beneficiary, 'Marie Dubois' (bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c), which Hans needs to pay. Initiate a 500 RON transfer from Elena's savings (acc_sav_25001) to this beneficiary. Hans also requests to update her scheduled payment (sp_a3o5b4n6-m1n0-o9p8-q7r6-s5t4u3v2w1x0) to 250 RON. Review Elena's recent transactions. As per the POA, update Elena's communication preference to 'Email'. Reassign her relationship manager to 'rm-ro-10', a POA specialist. Enforce a KYC refresh for Elena. Report Elena's new relationship manager, and the updated scheduled payment amount.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c"}),
            Action(name="initiate_fund_transfer_to_beneficiary", kwargs={"source_account_id": "acc_sav_25001", "beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c", "amount": 500.00}),
            Action(name="update_scheduled_payment_amount", kwargs={"payment_id": "sp_a3o5b4n6-m1n0-o9p8-q7r6-s5t4u3v2w1x0", "amount": 250.00}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_sav_25001"]}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "new_channel": "Email"}),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "relationship_manager_id": "rm-ro-10"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
        ],
        outputs=['"new_relationship_manager": "rm-ro-10"', '"new_payment_amount": 250.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_085",
        instruction="You are investigating a large crypto off-ramp for Santiago Muñoz (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19). Get his risk profile. A 50,000,000 CLP deposit was just made to his checking account (acc_chk_20001); lock this account. Calculate his total deposits over the past 30 days (2023-09-28 to 2023-10-28) to confirm this is an anomaly. Review his recent transactions. Review his active loans. Enforce an immediate KYC refresh due to the high-risk transaction. Fetch his 'Personal' beneficiaries. Deactivate his account. Find support tickets related to 'Security' connected to his customer id 'd4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19'. Create a high-priority support ticket to document the AML investigation. Update his communication preference to 'Mail' for formal requests. Report the customer's AML risk level, his total balance (pre-lock), and the account status.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_chk_20001"}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_chk_20001"], "start_date": "2023-09-28", "end_date": "2023-10-28"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_20001"]}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", }),
            Action(name="fetch_beneficiaries_by_relationship", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "relationship": "Personal"}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_chk_20001"}),
            Action(name="find_recent_support_tickets_by_category", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "category": "Security"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "account_id": "acc_chk_20001", "reason": "AML Investigation: Large Crypto Off-Ramp"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "new_channel": "Mail"}),
        ],
        outputs=['"aml_risk_level": "Low"', '"total_balance": 8500000.00', '"account_status": "Inactive"'],
    ),
    Task(
        annotator="0",
        user_id="USER_086",
        instruction="You are an account manager. Customer Maria Garcia (f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9) has requested to close their account due to relocation. Check their risk profile and total balance across all accounts. Review their last 15 transactions for any pending obligations. Deactivate account acc_chk_4001. Update their communication preference to 'Email' for 'Account closure documentation'. Create a support ticket related to transaction 'txn_a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4-10' to document the 'Account closure assistance'. Report the customer's total balance, number of transactions reviewed, and account closure status.",
        actions=[
            Action(
                name="get_customer_risk_profile_summary",
                kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}
            ),
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_4001"], "limit": 15}
            ),
            Action(
                name="deactivate_account_by_request",
                kwargs={
                    "account_id": "acc_chk_4001"
                }
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "new_channel": "Email"
                }
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "transaction_id": "txn_a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4-10",
                    "reason": "Account closure assistance"
                }
            ),
        ],
        outputs=['"total_balance": 1200.50', '"transactions_reviewed": 1', '"account_status": "Inactive"'],
    ),
    Task(
        annotator="0",
        user_id="USER_087",
        instruction="You are a compliance officer responding to a legal subpoena for all records of Alex Petrov (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13). First, get his risk profile and total balance. Retrieve all his accounts ('Checking' and 'Savings'). List the last 100 transactions for all his accounts. List all his active loans. Fetch all his 'Personal' beneficiaries. Retrieve all his scheduled payments. Find all support tickets associated with his profile. After gathering all information, lock his checking (acc_chk_14001) and savings (acc_sav_14002) accounts. Then, deactivate the checking account as per the legal order. Update his communication preference to 'Mail'. Create a final, comprehensive support ticket linked to his customer ID (use loan 'loan_auto_007' as a proxy) to confirm compliance with the subpoena with the reason 'Full Account Data Compilation for Subpoena'. Report the total number of transactions found, the number of active loans, and the final status of his checking account.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="get_customer_accounts_by_type", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "account_type": "Checking"}),
            Action(name="get_customer_accounts_by_type", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "account_type": "Savings"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_14001", "acc_sav_14002"], "limit": 100}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="fetch_beneficiaries_by_relationship", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "relationship": "Personal"}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_14001"}),
            Action(name="find_recent_support_tickets_by_category", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_chk_14001"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_sav_14002"}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_chk_14001"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "new_channel": "Mail"}),
            Action(name="create_support_ticket_for_transaction", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "transaction_id": "loan_auto_007", "reason": "Full Account Data Compilation for Subpoena"}),
        ],
        outputs=['"transaction_count": 1', '"active_loan_count": 1', '"checking_account_status": "Inactive"'],
    ),
    Task(
        annotator="0",
        user_id="USER_088",
        instruction="You are remediating a phishing attack for Jane Smith (a1b2c3d4-e5f6-7890-1234-567890abcdef). Get her risk profile and total balance. The attacker made a fraudulent transaction ('txn_4e5f8h2j-6f8d-9e4h-4f7j-1h2f4g8i9e5e'). Apply a refund with the amount of 120. The attacker also set up a recurring payment (sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f); update its amount to 0 to cancel it. Lock her checking (acc_chk_2001) and savings (acc_sav_2002) accounts. Review all her 'Family' beneficiaries for any unauthorized additions. Review all her active loans; thankfully, her paid-off loan (loan_pers_003) was not affected. Enforce an immediate KYC refresh. Update her communication preference to 'Phone'. Create a support ticket to document the phishing remediation. Report the total amount refunded, the new scheduled payment amount, and the status of her checking account.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="apply_partial_refund_to_transaction", kwargs={"transaction_id": "txn_4e5f8h2j-6f8d-9e4h-4f7j-1h2f4g8i9e5e", "refund_amount": 120.00}),
            Action(name="update_scheduled_payment_amount", kwargs={"payment_id": "sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f", "amount": 0.00}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_sav_2002"}),
            Action(name="fetch_beneficiaries_by_relationship", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "relationship": "Family"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", }),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "new_channel": "Phone"}),
            Action(name="create_support_ticket_for_transaction", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "transaction_id": "txn_4e5f8h2j-6f8d-9e4h-4f7j-1h2f4g8i9e5e", "reason": "Phishing Attack Remediation"}),
        ],
        outputs=['"total_refunded": 120.00', '"new_payment_amount": 0.00', '"checking_account_status": "Inactive"'],
    ),
    Task(
        annotator="0",
        user_id="USER_089",
        instruction="You are a specialist for vulnerable clients, handling the account of Elena Popescu (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24). Get her risk profile and total balance. Review her recent transactions for unusual spending. Review her scheduled payments on her savings account (acc_sav_25001). Check all her 'Personal' beneficiaries for recent additions. To protect her assets, immediately lock her savings account. Update her communication preference to 'Mail' for a legal paper trail. Reassign her relationship manager to 'rm-ro-11', a specialist in vulnerable client affairs. Enforce an immediate KYC refresh. Create a detailed support ticket for her savings account to document all protective measures taken with the reason 'Protective measures for vulnerable client'. Report the customer's total balance, the status of her savings account, and her new relationship manager.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_sav_25001"]}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_sav_25001"}),
            Action(name="fetch_beneficiaries_by_relationship", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "relationship": "Personal"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_sav_25001"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "new_channel": "Mail"}),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "relationship_manager_id": "rm-ro-11"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", }),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "account_id": "acc_sav_25001", "reason": "Protective measures for vulnerable client"}),
        ],
        outputs=['"total_balance": 250000.00', '"savings_account_status": "Locked"', '"new_relationship_manager": "rm-ro-11"'],
    ),
    Task(
        annotator="0",
        user_id="USER_090",
        instruction="You are advising David Chen (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) on tax optimization. Get his risk profile and total balance. Calculate his total income by checking deposits into his checking (acc_chk_3001) and investment (acc_inv_3002) accounts for the last year (2022-11-01 to 2023-10-31). Review his investment transactions. To reduce taxable income, he wants to make a 50,000 USD overpayment on his mortgage (loan_mort_001) from his investment account. Verify his beneficiary 'Metropolis Power & Light' (bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a). Enforce his annual KYC refresh. Reassign his relationship manager to 'rm006', a tax specialist. Create a support ticket for the investment account to document the tax optimization strategy with the reason 'Annual Tax Optimization Strategy Documentation'. Report his total deposits, the new mortgage balance",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_chk_3001", "acc_inv_3002"], "start_date": "2022-11-01", "end_date": "2023-10-31"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_inv_3002"]}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_mort_001", "from_account_id": "acc_inv_3002", "amount": 50000.00}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", }),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "relationship_manager_id": "rm006"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "account_id": "acc_inv_3002", "reason": "Annual Tax Optimization Strategy Documentation"}),
        ],
        outputs=['"total_deposits": 150.00', '"new_mortgage_balance": 665240.50'],
    ),
    Task(
        annotator="0",
        user_id="USER_091",
        instruction="Liam O'Connor (customer ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11) disputes a transaction 'txn_c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18' for 1200.00 EUR on his loan account (acc_loan_12002), claiming it was a mis-categorized capital expense. First, retrieve his total balance and review recent transactions on his checking account (acc_chk_12001) and loan account (acc_loan_12002). Transfer 600.00 EUR from his checking account (acc_chk_12001) to his loan account (acc_loan_12002) as partial payment towards the disputed transaction with the reason 'Dispute resolution partial payment'. Check for any existing support tickets in the 'Security' category. Create a support ticket for the disputed transaction with reason 'Mis-categorized capital expense'. Finally, update his communication preference to 'App'. Report the updated balances for both the checking and loan accounts.",
        actions=[
            Action(
                name="get_customer_total_balance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}
            ),
            Action(
                name="list_recent_transactions_by_category",
                kwargs={"account_ids": ["acc_chk_12001", "acc_loan_12002"]}
            ),
            Action(
                name="transfer_funds_between_accounts",
                kwargs={
                    "from_account_id": "acc_chk_12001",
                    "to_account_id": "acc_loan_12002",
                    "amount": 600.00,
                    "reason": "Dispute resolution partial payment"
                }
            ),
            Action(
                name="find_recent_support_tickets_by_category",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "category": "Security"
                }
            ),
            Action(
                name="create_support_ticket_for_transaction",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "transaction_id": "txn_c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "reason": "Mis-categorized capital expense"
                },
            ),
            Action(
                name="update_customer_communication_preference",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "new_channel": "App"
                }
            ),
        ],
        outputs=[
            '"checking_account_balance": 3900.00',
            '"loan_account_balance": -49400.00'
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_092",
        instruction="You are auditing a high-risk business client, Liam O'Connor (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11). Get his risk profile and total balance. Retrieve all his accounts ('Checking' and 'Loan'). List all transactions for his accounts for the last year with the limit of 1000. Review all active loans. Fetch all his 'Business' and 'Personal' beneficiaries. Verify his key vendor, 'London Electricity Co.' (bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d). Calculate total deposits into his checking account (acc_chk_12001) for the last 6 months (2023-05-01 to 2023-10-31). As part of the audit, temporarily lock his checking account. Enforce a KYC refresh. Reassign his relationship manager to an audit specialist ('rm-ie-03'). Create a master support ticket for him related to the account 'acc_chk_12001' to document the audit's initiation with the reason 'Comprehensive Audit Initiation'. Report the customer's credit score, and the status of the checking account.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="get_customer_accounts_by_type", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "account_type": "Checking"}),
            Action(name="get_customer_accounts_by_type", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "account_type": "Loan"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_12001", "acc_loan_12002"], "limit": 1000}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="fetch_beneficiaries_by_relationship", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "relationship": "Business"}),
            Action(name="fetch_beneficiaries_by_relationship", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "relationship": "Personal"}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_chk_12001"], "start_date": "2023-05-01", "end_date": "2023-10-31"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_chk_12001"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", }),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "relationship_manager_id": "rm-ie-03"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "account_id": "acc_chk_12001", "reason": "Comprehensive Audit Initiation"}),
        ],
        outputs=['"credit_score": 720', '"checking_account_status": "Locked"'],
    ),
    Task(
        annotator="0",
        user_id="USER_093",
        instruction="You are assisting Hans Müller (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). Get his risk profile and total balance. Rebalance his funds by splitting the transaction 'txn_e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14' to allocate 1,000 EUR to savings (acc_sav_8002) and 1,000 EUR to checking (acc_chk_8001). Then, verify beneficiary John Doe (bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f) and send him 1,000 EUR from the checking account. Review recent transactions on the checking account. Adjust its overdraft limit to 1,000 EUR. Retrieve the scheduled payment 'sp_d9b3a2c1-b4c3-d2e1-f0a9-b8c7d6e5f4a3'. Finally, report the updated savings balance, checking balance, and new overdraft limit.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(
                name="split_transaction_between_accounts",
                kwargs={
                    "transaction_id": "txn_e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "splits": [
                        {"account_id": "acc_sav_8002", "amount": 1000.00},
                        {"account_id": "acc_chk_8001", "amount": 1000.00}
                    ]
                }
            ),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(
                name="initiate_fund_transfer_to_beneficiary",
                kwargs={
                    "source_account_id": "acc_chk_8001",
                    "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f",
                    "amount": 1000.00
                }
            ),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_8001"]}),
            Action(
                name="review_overdraft_activity_and_adjust_limit",
                kwargs={"account_id": "acc_chk_8001", "new_limit": 1000.00}
            ),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_8002"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_chk_8001"}),
        ],
        outputs=['"saving_balance": 125000.00', '"checking_balance": 7800.50', '"new_overdraft_limit": 1000.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_094",
        instruction="You are the trust officer for student Maria Garcia (f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9), with her guardian being John Doe. Get Maria's risk profile and total balance. You must verify the guardian's identity (John Doe – c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) by checking his risk profile. Review Maria's student loan (loan_stud_004). Update her scheduled payment ('sp_e2g4b3f5-e9f8-g7h6-i5j4-k3l2m1n0o9p5') to 100 USD for her monthly tuition. Check the overdraft limit on her account (acc_chk_4001) and reduce it to 0 for safety. Enforce a KYC refresh. Update her communication preference to 'Mail' for official trust correspondence. Finally, create a support ticket linked to her checking account documenting the trust-related changes with the reason 'Guardian Verified and Trust Account Adjustments'. Report the new scheduled payment amount, and the overdraft limit.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}),
            Action(name="get_loan_details", kwargs={"loan_id": "loan_stud_004"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}),
            Action(name="update_scheduled_payment_amount", kwargs={"payment_id": "sp_e2g4b3f5-e9f8-g7h6-i5j4-k3l2m1n0o9p5", "amount": 100.00}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_4001", "new_limit": 0.00}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9", }),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9", "new_channel": "Mail"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9", "account_id": "acc_chk_4001", "reason": "Guardian Verified and Trust Account Adjustments"}),
        ],
        outputs=['"new_payment_amount": 100.00', '"overdraft_limit": 0.0'],
    ),
    Task(
        annotator="0",
        user_id="USER_095",
        instruction="You are advising John Doe (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) after he received a large inheritance, which is now in his savings account. Get his risk profile and total balance. First, pay off his auto loan (loan_auto_002) from his savings (acc_sav_1002). Verify his beneficiary 'Jane Smith' (bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d) and update his scheduled payment 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d' to 500 USD for a new family trust. Upgrade his relationship manager to 'rm005', a senior wealth advisor. Enforce a KYC refresh. Create a new support ticket linked to acc_sav_1002 with the reason 'Inheritance consultation'. Report the status of his auto loan, and his new relationship manager.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="get_loan_details", kwargs={"loan_id": "loan_auto_002"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_auto_002", "from_account_id": "acc_sav_1002", "amount": 15670.80}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d"}),
            Action(name="update_scheduled_payment_amount", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d", "amount": 500.00}),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "relationship_manager_id": "rm005"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "account_id": "acc_sav_1002", "reason": "Inheritance consultation"}),
        ],
        outputs=['"loan_status": "Paid Off"', '"new_relationship_manager": "rm005"'],
    ),
    Task(
        annotator="0",
        user_id="USER_096",
        instruction="You are assisting Fatima Al-Fassi (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6) with a real estate purchase in Germany. Get her risk profile and total balance. Verify the international beneficiary 'Klaus Schmidt' (bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a). She needs to make a down payment of 700,000 AED from her savings (acc_sav_7002). After the transfer, retrieve her updated savings balance and immediately lock the account for security. Increase the overdraft limit on her checking account (acc_chk_7001) to 10,000 AED to cover legal fees. Review her existing mortgage (loan_mort_018) and adjust its maturity date to 2045-01-01 to restructure her finances. Enforce a KYC refresh due to the large international transaction. After the security check period, create a support ticket to document the property purchase with the reason 'International Property Purchase Documentation'. Report the new overdraft limit, and the new loan maturity date.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="initiate_fund_transfer_to_beneficiary", kwargs={"source_account_id": "acc_sav_7002", "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a", "amount": 700000.00}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_sav_7002"}),
            Action(name="get_account_balance", kwargs={"account_id": "acc_sav_7002"}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_7001", "new_limit": 10000.00}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="adjust_loan_payment_due_date", kwargs={"loan_id": "loan_mort_018", "new_due_date": "2045-01-01"}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", }),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "account_id": "acc_sav_7002", "reason": "International Property Purchase Documentation"}),
        ],
        outputs=['"new_overdraft_limit": 10000.00', '"new_maturity_date": "2045-01-01"'],
    ),
    Task(
        annotator="0",
        user_id="USER_097",
        instruction="You are assisting Zoltan Nagy (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21), whose restaurant business was hit by ransomware. Get his risk profile and total balance. The attacker demands 2,000,000 HUF. Immediately lock his checking account (acc_chk_22001). To facilitate the payment, temporarily increase his overdraft limit to 2,500,000 HUF. Initiate the transfer to a new beneficiary (use 'Klaus Schmidt' - bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a - as a proxy for the attacker's account). After the transfer, enforce an immediate KYC refresh. Reassign his relationship manager to a cybercrime specialist ('rm-hu-03'). Update his communication to 'Phone'. Deactivate the compromised checking account. Create a detailed support ticket documenting the ransomware event for law enforcement with the reason 'Ransomware Payment and Account Compromise Report'. Report the checking account's final status and the new relationship manager.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}),
            Action(name="lock_account_manually", kwargs={"account_id": "acc_chk_22001"}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_22001", "new_limit": 2500000.00}),
            Action(name="initiate_fund_transfer_to_beneficiary", kwargs={"source_account_id": "acc_chk_22001", "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a", "amount": 2000000.00}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", }),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", "relationship_manager_id": "rm-hu-03"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", "new_channel": "Phone"}),
            Action(name="deactivate_account_by_request", kwargs={"account_id": "acc_chk_22001"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", "account_id": "acc_chk_22001", "reason": "Ransomware Payment and Account Compromise Report"}),
        ],
        outputs=['"account_status": "Inactive"', '"new_relationship_manager": "rm-hu-03"'],
    ),
    Task(
        annotator="0",
        user_id="USER_098",
        instruction="You are managing the finances of professional athlete Gabriel Silva (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17). Get his risk profile and total balance. He wants to use his signing bonus to pay off a student loan held by Maria Garcia (loan_stud_004); make a full payment of 25,000 USD (simulated as BRL) from his checking account (acc_chk_18001). He is buying a car, so review his auto loans. Review all scheduled payments. Increase his overdraft limit to 50,000 BRL. Enforce a KYC refresh. Reassign him to a top private banker ('rm-br-02'). Update his communication preference to 'App'. Create a support ticket to document his new financial plan with the reason 'Athlete Financial Plan Implementation'. Report the status of the student loan and his new overdraft limit.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="make_loan_overpayment", kwargs={"loan_id": "loan_stud_004", "from_account_id": "acc_chk_18001", "amount": 25000.00}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_18001"}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_18001", "new_limit": 50000.00}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", }),
            Action(name="reassign_relationship_manager", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "relationship_manager_id": "rm-br-02"}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "new_channel": "App"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "account_id": "acc_chk_18001", "reason": "Athlete Financial Plan Implementation"}),
        ],
        outputs=['"student_loan_status": "Paid Off"', '"new_overdraft_limit": 50000.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_099",
        instruction="You are managing the account for a foundation represented by Kenji Tanaka (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3). Get his risk profile and total balance. Calculate total deposits into his savings account (acc_sav_10002) for the last year (2022-11-01 to 2023-10-31) to track donations. Review the payment schedule on his checking account (acc_chk_10001) to see outgoing grants. Update the scheduled payment 'sp_c1d9b3a2-a5b4-c3d2-e1f0-a9b8c7d6e5f4' to a new grant amount of 300,000 JPY. Verify his key beneficiary 'Yuki Tanaka' (bene_2b1c9d8e-7f6a-5b4c-3d2e-1f0a9b8c7d6e). Review his active auto loan (loan_auto_011). Increase the overdraft limit on the checking account to 250,000 JPY to manage grant payment timing. Enforce the foundation's annual KYC refresh. Create a support ticket for the savings account to document the annual financial review. Report total donations, the new grant payment amount, and the new overdraft limit.",
        actions=[
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="get_customer_total_balance", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="get_total_deposits_over_period", kwargs={"account_ids": ["acc_sav_10002"], "start_date": "2022-11-01", "end_date": "2023-10-31"}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_10001"}),
            Action(name="update_scheduled_payment_amount", kwargs={"payment_id": "sp_c1d9b3a2-a5b4-c3d2-e1f0-a9b8c7d6e5f4", "amount": 300000.00}),
            Action(name="verify_beneficiary_exists", kwargs={"beneficiary_id": "bene_2b1c9d8e-7f6a-5b4c-3d2e-1f0a9b8c7d6e"}),
            Action(name="list_active_loans_with_balances", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_10001", "new_limit": 250000.00}),
            Action(name="enforce_kyc_refresh_for_customer", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", }),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "account_id": "acc_sav_10002", "reason": "Annual Foundation Financial Review"}),
        ],
        outputs=['"total_donations": 0.0', '"new_grant_amount": 300000.00', '"new_overdraft_limit": 250000.00'],
    ),
    Task(
        annotator="0",
        user_id="USER_100",
        instruction="You are in fraud operations, resolving a false alert for Oliver Williams (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5). His account (acc_chk_6001) got a false ticket (tkt_f8c7d6e5-d6e5-f4a3-b2c1-d0e9f8g7h6i5). Get his total balance and risk profile. Review his recent transactions to confirm legitimacy. Check his scheduled payments on that account. Retrieve any recent support tickets under the 'Security' category to validate the original alert. Oliver also wants to change the communication method to 'SMS'. To compensate for the inconvenience, increase his overdraft limit to 200 GBP. Create a new support ticket for his checking account with the reason 'Resolution of false fraud alert.'. Report the new overdraft limit, and the customer's credit score.",
        actions=[
            Action(name="get_customer_total_balance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}),
            Action(name="get_customer_risk_profile_summary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}),
            Action(name="list_recent_transactions_by_category", kwargs={"account_ids": ["acc_chk_6001"]}),
            Action(name="get_payment_schedule_for_account", kwargs={"account_id": "acc_chk_6001"}),
            Action(name="review_overdraft_activity_and_adjust_limit", kwargs={"account_id": "acc_chk_6001", "new_limit": 200.00}),
            Action(name="update_customer_communication_preference", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "new_channel": "SMS"}),
            Action(name="create_support_ticket_for_account", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "account_id": "acc_chk_6001", "reason": "Resolution of false fraud alert"}),
            Action(name="find_recent_support_tickets_by_category", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "category": "Security"}),
            Action(name="get_customer_contact_methods", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}),
        ],
        outputs=['"new_overdraft_limit": 200.00', '"credit_score": 650'],
    ),
]
