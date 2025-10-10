from tau_bench.types import Action, Task

# Edges = Input parameters from the prompt + Input parameters obtained from API responses
# Every edge signifies a dependency indicating that an API call relies on data from the prompt or earlier API responses.
# MODERATE COMPLEXITY TASKS (7-12 edges)

TASKS = [
    Task(
        annotator="0",
        user_id="USER_001",
        instruction="Initiate the onboarding process for Kenji Tanaka's (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) new corporation, now under the management of Chloe Dubois (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). Obtain risk profiles for both individuals. Allocate 7,800 EUR from the business checking account (acc_chk_8001) to clear his personal auto loan (loan_auto_002). Adjust the overdraft limit of that account to 2,500 EUR. Check the scheduled payments. Close the previous personal checking account (acc_chk_1001). Require a KYC update for the corporation and designate 'rm-de-10' as its relationship manager. Finish by reporting the newly assigned relationship manager.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_auto_002", "from_account_id": "acc_chk_8001", "amount": 7800}),
            Action(name="GetLoanDetails", kwargs={"loan_id": "loan_auto_002"}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_8001", "new_limit": 2500.00}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "relationship_manager_id": "rm-de-10"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_002",
        instruction="Examine a synthetic identity fraud case. The SSN with last 4 digits '8765' was fraudulently used in connection with legitimate customer Sofia Andersson (indexed as customer ID c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12). A fake profile linked to Gabriel Silva (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15) was merged into her legitimate profile. Start by retrieving the risk profiles for both Sofia Andersson and Gabriel Silva. The fraudster acquired a personal loan (loan_pers_013) wrongfully linked to Sofia Andersson; pay off the remaining 3,500 KRW from her checking account (acc_chk_16001). Secure the account to ensure safety. Review her scheduled payments. Start an immediate KYC update. Assign 'rm-kr-03', a fraud expert, as her relationship manager. Update her communication to 'Phone'. Create a support ticket detailing the synthetic ID fraud for the credit bureau under the reason 'Synthetic Identity Fraud Remediation Report'. Report the status of the fraudulent loan and the checking account.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15"}),
            Action(name="mergeDuplicateCustomersBySsn", kwargs={"ssn_last_4": "8765"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_pers_013", "from_account_id": "acc_chk_16001", "amount": 3500.00}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_chk_16001"}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_16001"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12", }),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12", "relationship_manager_id": "rm-kr-03"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12", "new_channel": "Phone"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12", "account_id": "acc_chk_16001", "reason": "Synthetic Identity Fraud Remediation Report"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_003",
        instruction="Conduct an investigation into a potential insider trading alert for Zoltan Nagy (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). Include 'City General Hospital' under his employer profile. Analyze the past 100 transactions on his investment account (acc_inv_3002), especially the recent notable purchase ('txn_1h8i2k5m-9i2g-3h7k-7i1m-4k5i7j2l3h8h'). Calculate his total deposits into that account over the span of the last 6 months (2023-05-01 to 2023-10-31) to spot any unusual inflows. Lock the investment account. Also, secure his checking account (acc_chk_3001) to prevent asset movement. Reassign 'rm012', a compliance expert, as his relationship manager. Initiate an immediate KYC update. Collect his contact preferences and shift his communication method to 'Mail' for legal purposes. Set up a high-priority support ticket tied to the investment account for escalation to the legal department, with the explanation 'Escalation to Legal: Potential Insider Trading'. Provide details about the customer's employer, the investment account status, and the new relationship manager.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="addEmployerToCustomerProfile", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "employer": "City General Hospital"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_inv_3002"], "limit": 100}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_inv_3002"], "start_date": "2023-05-01", "end_date": "2023-10-31"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_inv_3002"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_chk_3001"}),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "relationship_manager_id": "rm012"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", }),
            Action(name="getCustomerContactMethods", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "new_channel": "Mail"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "account_id": "acc_inv_3002", "reason": "Escalation to Legal: Potential Insider Trading"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_004",
        instruction="Address an inheritance dispute involving Santiago Muñoz's (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18) estate. Determine her total balance first. Quickly lock her checking account (acc_chk_19001). Analyze her outstanding debts; the personal loan (loan_pers_013) requires payment. Utilize 3,500 EUR from her checking account for settlement. Examine scheduled payments to identify outflows. Extract information on her 'Personal' beneficiaries. Based on the legal agreement, equally divide the remaining funds in the checking account: 50% to 'Marie Dubois' (bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c) and 50% to 'Klaus Schmidt' (bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a). First, verify both beneficiaries. Conduct the transfers for the remaining balance. Deactivate the account after emptying it. Create a final support ticket for the loan to document estate settlement completion. Report the final balance of the checking account, loan status, and the status of the checking account.",
        actions=[
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_chk_19001"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_pers_013", "from_account_id": "acc_chk_19001", "amount": 3500.00}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_19001"}),
            Action(name="fetchBeneficiariesByRelationship", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "relationship": "Personal"}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c"}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="initiateFundTransferToBeneficiary", kwargs={"source_account_id": "acc_chk_19001", "beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c", "amount": 0.00}), # The current balance is zero.
            Action(name="initiateFundTransferToBeneficiary", kwargs={"source_account_id": "acc_chk_19001", "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a", "amount": 0.00}), # Balance remains at 0.
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_chk_19001"}),
            Action(name="createSupportTicketForTransaction", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "transaction_id": "loan_pers_013", "reason": "Final Estate Settlement Documentation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_005",
        instruction = ("As a dispute resolution officer, manage a report regarding an unauthorized transaction from customer Kenji Tanaka (e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2) involving a -85.00 EUR charge on his credit card (acc_crd_9002). Start by confirming his total balance and checking the latest 20 transactions on that card. Evaluate his risk profile and research similar previous disputes by accessing related credit category support tickets. Set up a high-priority dispute ticket for transaction 'txn_f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15' with the reason 'Unauthorized charge on credit card'. Temporarily lock the credit card account for security measures. Apply a provisional credit of 85.00 to his account pending dispute resolution, with the reason 'Provisional credit pending dispute resolution'. Indicate if any similar past disputes have been detected."),
        actions=[
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_crd_9002"], "limit": 20}
            ),
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="findRecentSupportTicketsByCategory",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "category": "Credit"}
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "transaction_id": "txn_f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "reason": "Unauthorized charge on credit card"
                }
            ),
            Action(
                name="lockAccountManually",
                kwargs={"account_id": "acc_crd_9002"}
            ),
            Action(
                name="ApplyTransactionAdjustment",
                kwargs={
                    "account_id": "acc_crd_9002",
                    "amount": 85.00,
                    "reason": "Provisional credit pending dispute resolution"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_006",
        instruction="Supervise the merger process between two clients: Adetokunbo Adebayor (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3) and Oliver Williams (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23), who share a business ID (represented as SSN '6677'). Begin by obtaining the risk profile for both clients. Integrate their customer records. For the newly formed primary customer (Adetokunbo Adebayor), calculate the combined total balance. Examine all newly consolidated active loans. Handle a 1,000,000 JPY overpayment on loan 'loan_auto_011' from account 'acc_chk_10001'. Adjust the overdraft limit on the primary business account (acc_chk_24001) to 200,000 NGN. Appoint a single relationship manager ('rm-jp-02') to the main client. Generate a support ticket for the primary business account to document the merger with the reason 'Corporate merger documentation'. Compile a report of credit scores for both initial clients and detail the new overdraft limit.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="mergeDuplicateCustomersBySsn", kwargs={"ssn_last_4": "6677"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_auto_011", "from_account_id": "acc_chk_10001", "amount": 1000000.00}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_24001", "new_limit": 200000.00}),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "relationship_manager_id": "rm-jp-02"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "account_id": "acc_chk_24001", "reason": "Corporate merger documentation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_007",
        instruction="As a loan officer, assist Customer Zoltan Nagy (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) in loan restructuring. Initially, verify their current loans and risk profile, then assess their total balance across all accounts. The customer intends to carry out a $500 overpayment on their mortgage (loan_mort_001) from their checking account acc_chk_3001. After overpayment, alter the loan's maturity date to 2051-07-15. Provide a report showcasing the loan balance after overpayment and the updated maturity date.",
        actions=[
            Action(
                name="listActiveLoansWithBalances",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="makeLoanOverpayment",
                kwargs={
                    "loan_id": "loan_mort_001",
                    "amount": 500.00,
                    "from_account_id": "acc_chk_3001"
                }
            ),
            Action(
                name="adjustLoanPaymentDueDate",
                kwargs={
                    "loan_id": "loan_mort_001",
                    "new_due_date": "2051-07-15"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_008",
        instruction="As a compliance officer conducting a regulatory review, investigate Customer Oliver Williams (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6) who requires enhanced due diligence. Their account identifiers are 'acc_chk_7001', 'acc_sav_7002'. Analyze their risk profile and calculate the total balance for all accounts. Review their preceding 30 transactions. Implement a KYC refresh due to a 'Regulatory requirement for enhanced due diligence'. Adjust their overdraft limit on account acc_chk_7001 to $3,000 attributed to a 'Compliance review - risk-based limit adjustment'. Update their communication preference to 'Email' for audit purposes. Report the AML risk level, the quantity of reviewed transactions, and the updated overdraft limit.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_7001", "acc_sav_7002"], "limit": 30}
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                }
            ),
            Action(
                name="reviewOverdraftActivityAndAdjustLimit",
                kwargs={
                    "account_id": "acc_chk_7001",
                    "new_limit": 3000.00
                }
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "new_channel": "Email"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_009",
        instruction="As a transaction analyst, resolve a complex transaction issue reported by Customer Zoltan Nagy (a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4). Verify their total balance and examine the last 25 transactions across their accounts. Transaction 'txn_b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11' valued at 50000 INR seems to be a business expense needing division. Initiate a dispute ticket for this transaction with the reason 'Business expense incorrectly charged to personal account'. Proceed to divide the transaction, allocating -30000 to the checking account (acc_chk_5002) and -20000 to the savings account (acc_sav_5001). Provide a report specifying the total balance, number of transactions reviewed, and elaborate on the new split transactions.",
        actions=[
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_sav_5001", "acc_chk_5002"], "limit": 25}
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "transaction_id": "txn_b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "reason": "Business expense incorrectly charged to personal account"
                }
            ),
            Action(
                name="splitTransactionBetweenAccounts",
                kwargs={
                    "transaction_id": "txn_b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "splits": [
                        {"account_id": "acc_chk_5002", "amount": -30000.00},
                        {"account_id": "acc_sav_5001", "amount": -20000.00}
                    ]
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_010",
        instruction="As the relationship manager, oversee a high-value customer recovery case for Customer Sofia Andersson (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5) who has requested account deactivation. The customer's account acc_chk_6001 is currently operational. Initially, evaluate their risk profile and overall balance. Proceed to deactivate their account. Change their relationship manager to 'rm_senior_001'. Adjust their communication preference to 'Email'. Add their new employer 'Advanced Electric Systems' to the client's profile. Produce a report detailing the customer's credit score, total balance, and newly assigned relationship manager.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}
            ),
            Action(
                name="closeActiveAccount",
                kwargs={
                    "account_id": "acc_chk_6001",
                }
            ),
            Action(
                name="reassignRelationshipManager",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "relationship_manager_id": "rm_senior_001"
                }
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "new_channel": "Email",
                }
            ),
            Action(
                name="addEmployerToCustomerProfile",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "employer": "Advanced Electric Systems"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_011",
        instruction="In your role as an international banking officer, handle a request from Customer Oliver Williams (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6) for a 5,000 AED international wire transfer. Review their risk profile and total balance. Investigate their most recent 25 transactions. Verify the existence of the beneficiary 'Dubai International School' (bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f). Facilitate the wire transfer from acc_chk_7001 to this beneficiary. Implement a KYC refresh due to the significant transfer. Provide a report on the customer's AML risk level, total balance following the transfer, and transfer authorization status.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_7001"], "limit": 25}
            ),
            Action(
                name="verifyBeneficiaryExists",
                kwargs={"beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f"}
            ),
            Action(
                name="initiateFundTransferToBeneficiary",
                kwargs={
                    "source_account_id": "acc_chk_7001",
                    "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f",
                    "amount": 5000.00
                }
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_012",
        instruction="In your responsibility as a senior loan officer, aid Customer Chloe Dubois (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1) in optimizing their loan payment schedule. Check their active loans, risk profile, and total balance. The customer plans to make a 2,000 EUR overpayment on their mortgage (loan_mort_014) using their checking account acc_chk_8001. After the overpayment, adjust the loan's maturity date to 2035-11-01. Provide details on the loan balance after the overpayment, the updated maturity date, and the customer's credit score.",
        actions=[
            Action(
                name="listActiveLoansWithBalances",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="makeLoanOverpayment",
                kwargs={
                    "loan_id": "loan_mort_014",
                    "amount": 2000.00,
                    "from_account_id": "acc_chk_8001"
                }
            ),
            Action(
                name="adjustLoanPaymentDueDate",
                kwargs={
                    "loan_id": "loan_mort_014",
                    "new_due_date": "2035-11-01"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_013",
        instruction="As a data analyst, handle the potential duplicate records flagged for customers with the SSN last 4 digits '1122'. Assess the risk profile and total balance for customer Zoltan Nagy (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) linked with this SSN. Proceed with a merge of all customers with this SSN. Update Zoltan Nagy's communication preference to 'Email'. Ensure his employer is accurately listed as 'City General Hospital'. Lastly, assign his relationship manager to 'rm_consolidated_001'. Deliver a report on the customer's credit score, the final total balance, and the merge operation outcome.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="mergeDuplicateCustomersBySsn",
                kwargs={"ssn_last_4": "1122"}
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "new_channel": "Email"
                }
            ),
            Action(
                name="addEmployerToCustomerProfile",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "employer": "City General Hospital"
                }
            ),
            Action(
                name="reassignRelationshipManager",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "relationship_manager_id": "rm_consolidated_001"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_014",
        instruction="As an account manager, manage Customer Adetokunbo Adebayor's (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3) request to temporarily deactivate their account, which is currently active. Evaluate their risk profile and total balance. Close their checking account acc_chk_10001. Change their relationship manager to 'rm_premium_001'. Modify their communication preference to 'Email'. Present findings on the customer's credit score, total balance, and account status.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="closeActiveAccount",
                kwargs={
                    "account_id": "acc_chk_10001"
                }
            ),
            Action(
                name="reassignRelationshipManager",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "relationship_manager_id": "rm_premium_001"
                }
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "new_channel": "Email"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_015",
        instruction="In your duty as a business banking officer, confirm Chloe Dubois's (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1) total balance and the most recent 30 transactions. Initiate a support ticket for transaction 'txn_e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14' referencing 'Business expense allocation correction'. Proceed by dividing the 2000 EUR by withdrawing 1400 EUR from checking (acc_chk_8001) and 600 EUR from savings (acc_sav_8002), adjust his communication preference to 'App', and provide a report on the total balance, number of transactions reviewed, and the divided amounts.",
        actions=[
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={
                    "account_ids": ["acc_chk_8001", "acc_sav_8002"],
                    "limit": 30
                }
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "transaction_id": "txn_e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "reason": "Business expense allocation correction"
                }
            ),
            Action(
                name="splitTransactionBetweenAccounts",
                kwargs={
                    "transaction_id": "txn_e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "splits": [
                        {"account_id": "acc_chk_8001", "amount": -1400.00},
                        {"account_id": "acc_sav_8002", "amount": -600.00}
                    ]
                }
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "new_channel": "App"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_016",
        instruction="Manage the duties of an agricultural lending officer. Customer Zoltan Nagy (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11) needs seasonal payment adjustments for farming. Review their ongoing loans, risk profile, and complete balance. The customer plans to overpay 2,000 EUR on their business loan (loan_biz_005) through their checking account acc_chk_12001. Subsequently, adjust the loan's maturity date to 2027-04-01. Compile a report on the loan balance following overpayment, the adjusted maturity date, and the customer's credit score.",
        actions=[
            Action(
                name="listActiveLoansWithBalances",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}
            ),
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}
            ),
            Action(
                name="makeLoanOverpayment",
                kwargs={
                    "loan_id": "loan_biz_005",
                    "amount": 2000.00,
                    "from_account_id": "acc_chk_12001"
                }
            ),
            Action(
                name="adjustLoanPaymentDueDate",
                kwargs={
                    "loan_id": "loan_biz_005",
                    "new_due_date": "2027-04-01",
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_017",
        instruction="Supervise the role of a student banking officer. Customer Gabriel Silva (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12) requested a 15,000 PKR remittance internationally. Analyze their risk profile and full balance using the account acc_chk_13001. Review their last 25 transactions. The customer identified the beneficiary id as bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a. Verify the beneficiary's existence, then carry out the transfer from acc_chk_13001. Ensure a KYC update is performed. Provide the customer's AML risk level in a report.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_13001"], "limit": 25}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="initiateFundTransferToBeneficiary", kwargs={
                "source_account_id": "acc_chk_13001",
                "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a",
                "amount": 15000.00
            }),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_018",
        instruction="Support as a commercial lending officer. Customer Santiago Muñoz (a1b2c3d4-e5f6-7890-1234-567890abcdef-10) requires help in sorting a particular business transaction. Evaluate their risk profile and overall balance. Look into their checking account(s), particularly acc_chk_11001. Analyze their most recent 30 transactions from this account. Generate a support ticket for transaction 'txn_b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17' citing the reason 'Help categorize fashion industry business expense'. Then, modify their communication preference to 'App'. Present a report summarizing the total balance, the number of transactions inspected, and the reason for the support ticket for confirmation.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10"}
            ),
            Action(
                name="getCustomerAccountsByType",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10", "account_type": "Checking"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_11001"], "limit": 30}
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "transaction_id": "txn_b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "reason": "Help categorize fashion industry business expense"
                }
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "new_channel": "App"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_019",
        instruction="Customer Adetokunbo Adebayor (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3) is due for a check because of account inactivity. Investigate their risk profile and full balance. Review their previous 20 transactions. Ascertain if account acc_chk_10001 and acc_sav_10002 should be locked due to 90 days of inactivity (assume today's date is 2026-07-28). Change their communication preference to 'SMS'. Create a support ticket linked to transaction 'txn_a1b2c3d4-e5f6-7890-1234-567890abcdef-16' for 'Account inactivity security review'. Deliver a report on the customer's total balance, the count of transactions reviewed, and the account lock status.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_10001", "acc_sav_10002"], "limit": 20}
            ),
            Action(
                name="lockAccountManually",
                kwargs={
                    "account_id": "acc_chk_10001"
                }
            ),
            Action(
                name="lockAccountManually",
                kwargs={
                    "account_id": "acc_sav_10002"
                }
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "new_channel": "SMS"
                }
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "transaction_id": "txn_a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "reason": "Account inactivity security review"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_020",
        instruction="Function as a private banking officer. Customer Zoltan Nagy (a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4) is eligible for a premium service upgrade. Their account numbers are acc_sav_5001 and acc_chk_5002. Examine their risk profile and total balance. Scrutinize their previous 35 transactions. Appoint their relationship manager to 'rm_premium_001'. Adjust their communication preference to 'Email'. Confirm their employer as 'Global Tech Services'. Initiate a support ticket concerning transaction 'txn_b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11' to record the 'High-value customer service upgrade'. Compile the customer's credit score, entire balance, and new relationship manager in a report.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_sav_5001", "acc_chk_5002"], "limit": 35}
            ),
            Action(
                name="reassignRelationshipManager",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "relationship_manager_id": "rm_premium_001"
                }
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "new_channel": "Email"
                }
            ),
            Action(
                name="addEmployerToCustomerProfile",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "employer": "Global Tech Services"
                }
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "transaction_id": "txn_b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "reason": "High-value customer service upgrade"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_021",
        instruction="In your capacity as a relationship manager for Kenji Tanaka (e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2), note that his personal loan (loan_pers_008) is listed as 'Delinquent'. Start by collecting his risk profile and assess his total balance from all accounts to understand his financial condition. Analyze all his existing loans and his recent transactions to identify his spending trends using 'acc_chk_9001' and 'acc_crd_9002'. From his checking account (acc_chk_9001), execute a 300 EUR payment towards the delinquent loan to show goodwill. Because of the delinquency, adjust the overdraft limit on his checking account to 100 EUR for protection. Change his communication preference to 'Phone' for closer follow-up. Lastly, create a support ticket regarding his latest transaction ('txn_f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15') to document your actions, indicating the reason as 'Customer outreach regarding delinquent loan'. Provide a report on the loan's new balance, the updated overdraft limit, and the customer's credit score.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="listActiveLoansWithBalances",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_9001", "acc_crd_9002"]}
            ),
            Action(
                name="makeLoanOverpayment",
                kwargs={
                    "loan_id": "loan_pers_008",
                    "from_account_id": "acc_chk_9001",
                    "amount": 300.00,
                },
            ),
            Action(
                name="reviewOverdraftActivityAndAdjustLimit",
                kwargs={"account_id": "acc_chk_9001", "new_limit": 100.00},
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "new_channel": "Phone",
                },
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "transaction_id": "txn_f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "reason": "Customer outreach regarding delinquent loan",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_022",
        instruction="As a compliance officer, conduct a preemptive review of Mohammed Al-Masri (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17), whose AML risk is designated as 'Medium'. Retrieve his risk profile and total balance. Inspect all transactions on his checking account (acc_chk_18001) from the past year. Compile a summary of his total deposits from the previous six months (e.g., 2023-05-01 to 2023-10-31). Investigate any support tickets marked with 'Security'. Scrutinize his active mortgage (loan_mort_006). Considering his risk level and the high volume of transactions, effectuate a KYC update. Reallocate his relationship manager to 'rm-br-02', who is skilled in handling high-profile clients. Finally, update his employment status to 'Rio FC'. Submit a report outlining the customer's AML risk level, total identified deposits, and the new relationship manager ID.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_18001"]}
            ),
            Action(
                name="getTotalDepositsOverPeriod",
                kwargs={
                    "account_ids": ["acc_chk_18001"],
                    "start_date": "2023-05-01",
                    "end_date": "2023-10-31",
                },
            ),
            Action(
                name="findRecentSupportTicketsByCategory",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "category": "Security"}
            ),
            Action(
                name="listActiveLoansWithBalances",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                },
            ),
            Action(
                name="reassignRelationshipManager",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "relationship_manager_id": "rm-br-02",
                },
            ),
             Action(
                name="addEmployerToCustomerProfile",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "employer": "Rio FC",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_023",
        instruction="As a business banker for entrepreneur Oliver Williams (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23), initiate by verifying his total balance across his business accounts. He plans to make a payment to a contractor (current 'Personal' beneficiary 'Marie Dubois' with id 'bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c', needing initial verification) in the amount of 250,000 NGN from his checking account (acc_chk_24001). Additionally, he aims to process a 1,000,000 NGN overpayment on his business loan (loan_biz_009) through the same account. Examine all scheduled payments on his account. To support expanding operations, request an increase in his overdraft limit on the checking account to 100,000 NGN. Finally, update his communication preference to 'App'. Provide a report detailing the total balance after the transactions, the updated loan balance, and the new overdraft limit.",
        actions=[
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}
            ),
            Action(
                name="verifyBeneficiaryExists",
                kwargs={"beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c"}
            ),
            Action(
                name="initiateFundTransferToBeneficiary",
                kwargs={
                    "source_account_id": "acc_chk_24001",
                    "beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c",
                    "amount": 250000.00,
                },
            ),
            Action(
                name="makeLoanOverpayment",
                kwargs={
                    "loan_id": "loan_biz_009",
                    "from_account_id": "acc_chk_24001",
                    "amount": 1000000.00,
                },
            ),
            Action(
                name="getPaymentScheduleForAccount",
                kwargs={"account_id": "acc_chk_24001"},
            ),
            Action(
                name="reviewOverdraftActivityAndAdjustLimit",
                kwargs={"account_id": "acc_chk_24001", "new_limit": 100000.00},
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "new_channel": "App",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_024",
        instruction="As an advisor for Adetokunbo Adebayor (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3), who has recently relocated, start by assessing his risk profile and total balance. He intends to allocate the transaction 'txn_a1b2c3d4-e5f6-7890-1234-567890abcdef-16' by moving 1500 JPY from 'acc_chk_10001' to 'acc_sav_10002'. Before altering the scheduled payment, authenticate this beneficiary bene_2b1c9d8e-7f6a-5b4c-3d2e-1f0a9b8c7d6e. Following this, update his existing scheduled payment (sp_c1d9b3a2-a5b4-c3d2-e1f0-a9b8c7d6e5f4) to 250,000 JPY. Review his recent 10 transactions for any irregularities. Due to his change in residency status, execute a KYC update. Lastly, initiate a support ticket on his account 'acc_sav_10002' with the reason 'Inquiry about international loan payment options'. Report his risk profile, total balance, the final savings account balance, the new scheduled payment amount, and the KYC status.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="splitTransactionBetweenAccounts", kwargs={
                "transaction_id": "txn_a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                "splits": [
                    {"account_id": "acc_chk_10001", "amount": 1500.00},
                    {"account_id": "acc_sav_10002", "amount": 1500.00}
                ]
            }),
            Action(name="getAccountBalance", kwargs={"account_id": "acc_sav_10002"}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_2b1c9d8e-7f6a-5b4c-3d2e-1f0a9b8c7d6e"}),
            Action(name="updateScheduledPaymentAmount", kwargs={
                "payment_id": "sp_c1d9b3a2-a5b4-c3d2-e1f0-a9b8c7d6e5f4",
                "amount": 250000.00
            }),
            Action(name="listRecentTransactionsByCategory", kwargs={
                "account_ids": ["acc_chk_10001", "acc_sav_10002"], "limit": 10
            }),
            Action(name="enforceKycRefreshForCustomer", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"
            }),
            Action(name="createSupportTicketForAccount", kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "account_id": "acc_sav_10002",
                "reason": "Inquiry about international loan payment options"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_025",
        instruction="Take on the role of a private banker for Zoltan Nagy (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). Access his risk profile and entire balance. Begin by reviewing his 'Investment' accounts. Proceed to analyze his last 20 transactions to gain insight into his investment account (acc_inv_3002). Determine his total deposits over the past year (2022-11-01 to 2023-10-31) from 'acc_chk_3001' and 'acc_inv_3002'. Adjust his relationship manager assignment to 'rm006' to better suit his status as an active high-value investor and update his employer to 'City General Hospital'. Deliver a report that encompasses his investment account balance and details the new relationship manager.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="getCustomerAccountsByType",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "account_type": "Investment"},
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_inv_3002"], "limit": 20},
            ),
            Action(
                name="getTotalDepositsOverPeriod",
                kwargs={
                    "account_ids": ["acc_chk_3001", "acc_inv_3002"],
                    "start_date": "2022-11-01",
                    "end_date": "2023-10-31",
                },
            ),
            Action(
                name="reassignRelationshipManager",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "relationship_manager_id": "rm006",
                },
            ),
            Action(
                name="addEmployerToCustomerProfile",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "employer": "City General Hospital",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_026",
        instruction="In the role of a fraud analyst for Zoltan Nagy (a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4) with checking account 'acc_chk_5002', your task is to address an open 'Security' ticket (tkt_c1d0e9f8-e9f8-g7h6-i5j4-k3l2m1n0o9p8). Start by retrieving his risk profile and total balance. Investigate his loan details, with a focus on loan_auto_019. Analyze his recent transactions. Check the auto loan (loan_auto_019) for any fraudulent signs. Require a KYC update. Alter his communication preference to 'SMS' for urgent security alerts. Finish by logging all actions in a support ticket for audit purposes, mentioning 'Fraud investigation and account lock audit'. Provide a report on his checking account status and KYC condition.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(name="getAllAccountsForCustomer", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}),
            Action(
                name="GetLoanDetails",
                kwargs={"loan_id": "loan_auto_019"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": "acc_chk_5002"},
            ),
            Action(
                name="lockAccountManually",
                kwargs={"account_id": "acc_chk_5002"}
            ),
            Action(
                name="listActiveLoansWithBalances",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                },
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "new_channel": "SMS",
                },
            ),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4", "account_id": "acc_chk_5002", "reason": "Fraud investigation and account lock audit"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_027",
        instruction="Acting as an advisor for Adetokunbo Adebayor (a1b2c3d4-e5f6-7890-1234-567890abcdef-22), who is graduating, commence the process by checking her risk profile and total balance. Review her student loan (loan_stud_012). Due to her recent job offer, update her profile with 'Global Innovations Inc.' as her new employer. She is determined to increase her loan payments. Organize a 5000 CNY overpayment from her checking account (acc_chk_23001). Update the loan's maturity date to 2031-09-01. Furthermore, she plans to save funds. Evaluate her scheduled payments. Examine the overdraft limit on her account. To promote savings, change her communication preference to 'App'. Deliver a report on her adjusted loan balance, her employer, and her overdraft limit.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22"}
            ),
            Action(
                name="listActiveLoansWithBalances",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22"}
            ),
            Action(
                name="addEmployerToCustomerProfile",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "employer": "Global Innovations Inc.",
                },
            ),
            Action(
                name="makeLoanOverpayment",
                kwargs={
                    "loan_id": "loan_stud_012",
                    "from_account_id": "acc_chk_23001",
                    "amount": 5000.00,
                },
            ),
            Action(
                name="adjustLoanPaymentDueDate",
                kwargs={"loan_id": "loan_stud_012", "new_due_date": "2031-09-01"},
            ),
            Action(
                name="getPaymentScheduleForAccount",
                kwargs={"account_id": "acc_chk_23001"},
            ),
            Action(
                name="getAccountOverdraftLimit",
                kwargs={"account_id": "acc_chk_23001"},
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "new_channel": "App",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_028",
        instruction="As a dispute specialist managing Kenji Tanaka's case (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), handle her claim that a transaction ('txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f') was a shared cost with Elena Popescu. Initiate by obtaining her total balance and risk profile. Establish a support ticket for the transaction, addressing the dispute over 'Shared expense dispute'. Verify the beneficiary 'Elena Popescu' (bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d). Resolve by allocating the txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f 35.50 from John's checking (acc_chk_1001) and 40.00 from Jane's savings (simulating as her acc_sav_1002). Analyze John's recent transactions. Change her communication preference to 'Email'. Report the updated balance of her checking account, savings account, and confirm the support ticket creation.",
        actions=[
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="createSupportTicketForTransaction", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "transaction_id": "txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f",
                "reason": "Shared expense dispute"
            }),
            Action(name="verifyBeneficiaryExists", kwargs={
                "beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d"
            }),
            # Action: Divide the charge according to the guidelines.
            Action(name="splitTransactionBetweenAccounts", kwargs={
                "transaction_id": "txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f",
                "splits": [
                    {"account_id": "acc_chk_1001", "amount": -35.50},
                    {"account_id": "acc_sav_1002", "amount": -40.00}
                ]
            }),
            Action(name="getAccountBalance", kwargs={"account_id": "acc_chk_1001"}),  # Fresh
            Action(name="getAccountBalance", kwargs={"account_id": "acc_sav_1002"}),  # Recent
            Action(name="listRecentTransactionsByCategory", kwargs={
                "account_ids": ["acc_chk_1001", "acc_sav_1002"]
            }),
            Action(name="updateCustomerCommunicationPreference", kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "new_channel": "Email"
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_029",
        instruction="In the capacity of a financial wellness agent for Lakshmi Narayanan (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24), start by assessing her total balance and risk profile. Extract her scheduled payments ranging from 2023-11-01 to 2024-01-31. For payment 'sp_a3o5b4n6-m1n0-o9p8-q7r6-s5t4u3v2w1x0', ensure her funds are sufficient. She does not possess a checking account and depends solely on savings (acc_sav_25001), which is flagged as a possible issue. Review her recent transactions. Preemptively open a support ticket linked to her savings to trigger outreach about overdraft protection, citing 'Proactive outreach re: overdraft protection'. Note her communication preference is 'Mail'; switch it to 'Phone' for quicker assistance. Designate her new relationship manager to 'rm-ro-09', experienced in senior client matters. Deliver a report on her total balance, funds for her upcoming payment, and revised communication method.",
        actions=[
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}
            ),
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}
            ),
            Action(
                name="getScheduledPaymentsDueInRange",
                kwargs={"start_date": "2023-11-01", "end_date": "2024-01-31"},
            ),
            Action(
                name="checkFundsForNextScheduledPayment",
                kwargs={"payment_id": "sp_a3o5b4n6-m1n0-o9p8-q7r6-s5t4u3v2w1x0"},
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_sav_25001"]},
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "transaction_id": "txn_2a3b4c5d-6e7f-8g9h-0i1j-2k3l4m5n6o7p",
                    "reason": "Proactive outreach re: overdraft protection",
                },
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "new_channel": "Phone",
                },
            ),
            Action(
                name="reassignRelationshipManager",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "relationship_manager_id": "rm-ro-09",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_030",
        instruction="Serving as a mortgage specialist assisting Chloe Dubois (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1), who is considering mortgage refinancing (loan_mort_014), start by reviewing his risk profile and total balance. Check his active loans. Calculate his total deposits from the previous year (e.g., 2022-11-01 to 2023-10-31). He plans to proceed with a 5,000 EUR overpayment from his checking account (acc_chk_8001). After payment, review the payment schedule of his checking account. Identify if there are any 'Cancelled' support tickets. Require a KYC refresh during the pre-application stage for refinancing. Lastly, update his profile by adding his employer 'AutoFabrik GmbH' for record accuracy. Compile a report on his credit score, newly adjusted loan balance, and KYC outcome.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="listActiveLoansWithBalances",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="getTotalDepositsOverPeriod",
                kwargs={
                    "account_ids": ["acc_chk_8001"],
                    "start_date": "2022-11-01",
                    "end_date": "2023-10-31",
                },
            ),
            Action(
                name="makeLoanOverpayment",
                kwargs={
                    "loan_id": "loan_mort_014",
                    "from_account_id": "acc_chk_8001",
                    "amount": 5000.00,
                },
            ),
            Action(
                name="getPaymentScheduleForAccount",
                kwargs={"account_id": "acc_chk_8001"},
            ),
            Action(
                name="findRecentSupportTicketsByCategory",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "category": "Cancelled"},
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                },
            ),
            Action(
                name="addEmployerToCustomerProfile",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "employer": "AutoFabrik GmbH",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_031",
        instruction="As a fraud analyst managing a complex case for customer Kenji Tanaka (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), start by evaluating the customer's risk profile and total balance. Investigate recent transactions across all accounts ('acc_chk_1001', 'acc_sav_1002', 'acc_crd_1003'). Search for any existing 'Scheduled Payment' support tickets to gather information about the case history. Retrieve the customer's contact methods and update their communication preference to 'Phone'. Execute a KYC refresh. For precautionary measures, lock the primary checking account (acc_chk_1001). Finally, initiate a new support ticket for transaction 'txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f' to record the investigation process. Report the final total balance, KYC status, and the updated lock status of the checking account.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_1001", "acc_sav_1002", "acc_crd_1003"]}
            ),
            Action(
                name="findRecentSupportTicketsByCategory",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "category": "Scheduled Payment"}
            ),
            Action(
                name="getCustomerContactMethods",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "new_channel": "Phone"
                }
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                }
            ),
            Action(
                name="lockAccountManually",
                kwargs={
                    "account_id": "acc_chk_1001",
                }
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "transaction_id": "txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f",
                    "reason": "Fraud investigation"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_032",
        instruction="As a loan officer coordinating complex restructuring for customer Sofia Andersson (f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9), begin by assessing her risk profile and total balance. Retrieve loan details for loan_stud_004. Examine scheduled payments due between 2023-10-01 and 2023-12-31. For her scheduled payment 'sp_e2g4b3f5-e9f8-g7h6-i5j4-k3l2m1n0o9p5', check if there are sufficient funds. Make a $500 overpayment on her student loan (loan_stud_004) from her checking account (acc_chk_4001). Adjust the maturity date for the same loan to 2032-09-25. Finally, update her communication preference to 'App'. Report the updated loan balance and the new maturity date.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}
            ),
            Action(
                name="GetLoanDetails",
                kwargs={"loan_id": "loan_stud_004"}
            ),
            Action(
                name="getScheduledPaymentsDueInRange",
                kwargs={
                    "start_date": "2023-10-01",
                    "end_date": "2023-12-31"
                }
            ),
            Action(
                name="checkFundsForNextScheduledPayment",
                kwargs={
                    "payment_id": "sp_e2g4b3f5-e9f8-g7h6-i5j4-k3l2m1n0o9p5"
                }
            ),
            Action(
                name="makeLoanOverpayment",
                kwargs={
                    "loan_id": "loan_stud_004",
                    "from_account_id": "acc_chk_4001",
                    "amount": 500.00
                }
            ),
            Action(
                name="adjustLoanPaymentDueDate",
                kwargs={
                    "loan_id": "loan_stud_004",
                    "new_due_date": "2032-09-25"
                }
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "new_channel": "App"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_033",
        instruction="As a dispute resolution officer for customer Zoltan Nagy (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a), commence by reviewing his risk profile and total balance. Check his recent transactions from 'acc_inv_3002' and 'acc_chk_3001'. Search for any existing support tickets in the 'Scheduled Payment' category. Calculate the total deposits for his accounts between 2023-10-01 and 2023-10-31. Implement a partial refund of $150.00 to transaction 'txn_2g7h1j4l-8h1f-2g6j-6h9l-3j4h6i1k2g7g' to resolve the issue. Open a new support ticket for the same transaction to document the resolution, stating the reason 'Dispute resolution'. Change the customer's communication preference to 'SMS'. Report total deposits during the period and confirmation of the refund.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_3001", "acc_inv_3002"]}
            ),
            Action(
                name="findRecentSupportTicketsByCategory",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "category": "Scheduled Payment"}
            ),
            Action(
                name="getTotalDepositsOverPeriod",
                kwargs={
                    "account_ids": ["acc_chk_3001", "acc_inv_3002"],
                    "start_date": "2023-10-01",
                    "end_date": "2023-10-31"
                }
            ),
            Action(
                name="applyPartialRefundToTransaction",
                kwargs={
                    "transaction_id": "txn_2g7h1j4l-8h1f-2g6j-6h9l-3j4h6i1k2g7g",
                    "refund_amount": 150.00
                }
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "transaction_id": "txn_2g7h1j4l-8h1f-2g6j-6h9l-3j4h6i1k2g7g",
                    "reason": "Dispute resolution"
                }
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "new_channel": "SMS"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_034",
        instruction="As an account manager for Elena Popescu (a1b2c3d4-e5f6-7890-1234-567890abcdef), begin by assessing her risk profile and total balance. Retrieve all her checking and savings accounts to evaluate her banking structure. Acquire the payment schedule for her checking account (acc_chk_2001). Review any scheduled payments due between 2023-11-01 and 2024-01-01. Update her scheduled payment 'sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f' to a new amount of $750.00. Lastly, modify her communication preference to 'Email'. Report her total balance, the count of checking accounts, and the updated payment amount.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="getCustomerAccountsByType",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "account_type": "Checking"}
            ),
            Action(
                name="getCustomerAccountsByType",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "account_type": "Savings"}
            ),
            Action(
                name="getPaymentScheduleForAccount",
                kwargs={"account_id": "acc_chk_2001"}
            ),
            Action(
                name="getScheduledPaymentsDueInRange",
                kwargs={
                    "start_date": "2023-11-01",
                    "end_date": "2024-01-01"
                }
            ),
            Action(
                name="updateScheduledPaymentAmount",
                kwargs={
                    "payment_id": "sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f",
                    "amount": 750.00
                }
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "new_channel": "Email"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_035",
        instruction="As a wire transfer officer for customer Sofia Andersson (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5), commence by assessing her risk profile and total balance. Collect all beneficiaries categorized as 'Personal' and 'Business', verifying the existence of the beneficiary with ID 'bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d'. Once verified, coordinate a fund transfer of 50.00 GBP from her checking account (acc_chk_6001) to this beneficiary. Review her recent transactions to ensure no irregularities. Following the transaction, set up a support ticket using her checking account to note the completed transfer for audit purposes, stating the reason 'Wire transfer to verified beneficiary'. Report a confirmation of the successful transfer and ticket creation.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}
            ),
            Action(
                name="fetchBeneficiariesByRelationship",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "relationship": "Personal"}
            ),
            Action(
                name="fetchBeneficiariesByRelationship",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "relationship": "Business"}
            ),
            Action(
                name="verifyBeneficiaryExists",
                kwargs={
                    "beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d"
                }
            ),
            Action(
                name="initiateFundTransferToBeneficiary",
                kwargs={
                    "source_account_id": "acc_chk_6001",
                    "beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d",
                    "amount": 50.00
                }
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_6001"]}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}
            ),
            Action(
                name="createSupportTicketForAccount",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_id": "acc_chk_6001",
                    "reason": "Wire transfer to verified beneficiary"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_036",
        instruction="As a risk analyst handling a case about Kenji Tanaka (e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2), start by reviewing his risk profile and total balance. Retrieve the overdraft limit on his checking account (acc_chk_9001). Additionally, identify his upcoming scheduled payment sp_a2c1d9b3-f6a5-b4c3-d2e1-f0a9b8c7d6e5 on the same account. Look into his recent transaction history. Search for any support tickets listed under 'Beneficiary Management'. Adjust his overdraft limit to $50.00. Move on to deactivate his credit card account (acc_crd_9002). Finally, log the case by generating a support ticket for transaction 'txn_6e7f8g9h-0i1j-2k3l-4m5n-6o7p8q9r0s1t', using 'Overdraft policy enforcement' as the explanation. Report the final total balance, the revised overdraft limit, and the status of the credit card account.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="getAccountOverdraftLimit",
                kwargs={
                    "account_id": "acc_chk_9001"
                }
            ),
            Action(name="checkFundsForNextScheduledPayment", kwargs={"payment_id": "sp_a2c1d9b3-f6a5-b4c3-d2e1-f0a9b8c7d6e5"}),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_9001", "acc_crd_9002"]}
            ),
            Action(
                name="findRecentSupportTicketsByCategory",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "category": "Beneficiary Management"}
            ),
            Action(
                name="reviewOverdraftActivityAndAdjustLimit",
                kwargs={
                    "account_id": "acc_chk_9001",
                    "new_limit": 50.00
                }
            ),
            Action(
                name="deactivateAccountByRequest",
                kwargs={
                    "account_id": "acc_crd_9002"
                }
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "transaction_id": "txn_6e7f8g9h-0i1j-2k3l-4m5n-6o7p8q9r0s1t",
                    "reason": "Overdraft policy enforcement"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_037",
        instruction="In your role as a supervisor overseeing a data consolidation for Adetokunbo Adebayor (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3), commence by analyzing his risk profile and total balance. Combine duplicate customer records by utilizing the last 4 digits of his SSN '6677'. Update his employer to 'Cybernetics Corp'. Reassign his relationship manager to 'rm_premium_001'. Retrieve his current contact methods and thereafter change his communication preference to 'App'. To finalize, document the profile consolidation by creating a support ticket for transaction 'txn_a1b2c3d4-e5f6-7890-1234-567890abcdef-16'. Provide a summary of the total balance, count of profiles merged, and the new relationship manager.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="mergeDuplicateCustomersBySsn",
                kwargs={
                    "ssn_last_4": "6677"
                }
            ),
            Action(
                name="addEmployerToCustomerProfile",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "employer": "Cybernetics Corp"
                }
            ),
            Action(
                name="reassignRelationshipManager",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "relationship_manager_id": "rm_premium_001"
                }
            ),
            Action(
                name="getCustomerContactMethods",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "new_channel": "App"
                }
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "transaction_id": "txn_a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "reason": "Profile consolidation"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_038",
        instruction="As a compliance officer for customer Kenji Tanaka (a1b2c3d4-e5f6-7890-1234-567890abcdef-16), evaluate his risk profile and total balance. Review his recent transaction activities. Segment transaction 'txn_5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8g9h0i' (-60.00 AUD) by applying -40.00 to his checking account (acc_chk_17001) and -20.00 to his savings account (acc_sav_17002). Determine his total deposit amount within the period from 2023-01-01 to 2023-12-31. Collect data on all his checking accounts. For record-keeping, initiate a support ticket for the initial split transaction with 'Transaction categorization' stated as the purpose. Shift his communication preference to 'SMS'. Communicate his total deposits and confirm the transaction division.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_17001", "acc_sav_17002"]}
            ),
            Action(
                name="splitTransactionBetweenAccounts",
                kwargs={
                    "transaction_id": "txn_5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8g9h0i",
                    "splits": [
                        {"account_id": "acc_chk_17001", "amount": -40.00},
                        {"account_id": "acc_sav_17002", "amount": -20.00}
                    ]
                }
            ),
            Action(
                name="getTotalDepositsOverPeriod",
                kwargs={
                    "account_ids": ["acc_chk_17001", "acc_sav_17002"],
                    "start_date": "2023-01-01",
                    "end_date": "2023-12-31"
                }
            ),
            Action(
                name="getCustomerAccountsByType",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16", "account_type": "Checking"}
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "transaction_id": "txn_5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8g9h0i",
                    "reason": "Transaction categorization"
                }
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "new_channel": "SMS"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_039",
        instruction="As an officer in international banking working with Oliver Williams (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6), start by assessing her risk profile and total balance. Establish whether her beneficiary 'Dubai International School' (bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f) is registered. Execute a transfer of 3,500.00 AED from her checking account (acc_chk_7001) to this beneficiary. Proceed with updating her KYC. Check any support tickets under the 'Account Management' category. Log the international compliance by setting up a support ticket for transaction 'txn_d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13'. Provide a report on her post-transfer total balance, number of beneficiaries, and compliance checks.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="fetchBeneficiariesByRelationship",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "relationship": "School"}
            ),
            Action(
                name="verifyBeneficiaryExists",
                kwargs={
                    "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f"
                }
            ),
            Action(
                name="initiateFundTransferToBeneficiary",
                kwargs={
                    "source_account_id": "acc_chk_7001",
                    "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f",
                    "amount": 3500.00,
                }
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                }
            ),
            Action(
                name="findRecentSupportTicketsByCategory",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "category": "Account Management"}
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "transaction_id": "txn_d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13",
                    "reason": "International compliance"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_040",
        instruction="Your responsibility as a senior loan officer for Zoltan Nagy (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13) involves investigating his risk profile and total balance. Collect details on all his current loans. Identify scheduled payments due between 2023-11-01 and 2024-02-01. For payment 'sp_b5d7c6a8-b2c1-d0e9-f8g7-h6i5j4k3l2m1', ensure there are sufficient funds. Proceed with a 75000 RUB additional payment on his auto loan (loan_auto_007) via his checking account (acc_chk_14001). Update the maturity date for this loan to 2025-10-01. Review the payment schedule linked to his checking account. Change his communication preference to 'Phone'. Conclude with a report on the updated maturity date.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}
            ),
            Action(
                name="listActiveLoansWithBalances",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}
            ),
            Action(
                name="getScheduledPaymentsDueInRange",
                kwargs={
                    "start_date": "2023-11-01",
                    "end_date": "2024-02-01"
                }
            ),
            Action(
                name="checkFundsForNextScheduledPayment",
                kwargs={
                    "payment_id": "sp_b5d7c6a8-b2c1-d0e9-f8g7-h6i5j4k3l2m1"
                }
            ),
            Action(
                name="makeLoanOverpayment",
                kwargs={
                    "loan_id": "loan_auto_007",
                    "from_account_id": "acc_chk_14001",
                    "amount": 75000.00
                }
            ),
            Action(
                name="adjustLoanPaymentDueDate",
                kwargs={
                    "loan_id": "loan_auto_007",
                    "new_due_date": "2025-10-01"
                }
            ),
            Action(
                name="getPaymentScheduleForAccount",
                kwargs={"account_id": "acc_chk_14001"}
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13",
                    "new_channel": "Phone"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_041",
        instruction="As Kenji Tanaka's relationship manager (e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2), his personal loan (loan_pers_008) is currently 'Delinquent'. Retrieve his risk assessment and overall balance. Examine all active loans and recent transactions from 'acc_chk_9001' and 'acc_crd_9002'. From his checking account (acc_chk_9001), process a payment of 300 EUR to lessen the delinquent loan. Given the delinquency, adjust the overdraft limit on his checking account to 100 EUR. Update his communication preference to 'Phone'. Finally, open a support ticket for his transaction 'txn_f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15' to document your actions with the note 'Customer outreach regarding delinquent loan'. Provide details on the loan's new balance, the revised overdraft limit, and the customer's credit score in your report.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="listActiveLoansWithBalances",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_9001", "acc_crd_9002"]}
            ),
            Action(
                name="makeLoanOverpayment",
                kwargs={
                    "loan_id": "loan_pers_008",
                    "from_account_id": "acc_chk_9001",
                    "amount": 300.00,
                },
            ),
            Action(
                name="reviewOverdraftActivityAndAdjustLimit",
                kwargs={"account_id": "acc_chk_9001", "new_limit": 100.00},
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "new_channel": "Phone",
                },
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "transaction_id": "txn_f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "reason": "Customer outreach regarding delinquent loan",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_042",
        instruction="You oversee compliance for Mohammed Al-Masri (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17), whose AML risk is classified as 'Medium'. Gather his risk profile and total account balance. Calculate his total deposits into his checking account (acc_chk_18001) over the six-month period (2023-05-01 to 2023-10-31). Review any support tickets marked for 'Security'. Evaluate his current mortgage (loan_mort_006). Due to his risk level, require a KYC update. Assign 'rm-br-02' as his new relationship manager. Lastly, revise his employment information in his profile to 'Rio FC'. Report back on the customer's AML risk tier, the calculated total deposits, and the new relationship manager ID.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}
            ),
            Action(
                name="getTotalDepositsOverPeriod",
                kwargs={
                    "account_ids": ["acc_chk_18001"],
                    "start_date": "2023-05-01",
                    "end_date": "2023-10-31",
                },
            ),
            Action(
                name="findRecentSupportTicketsByCategory",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "category": "Security"}
            ),
            Action(
                name="listActiveLoansWithBalances",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                },
            ),
            Action(
                name="reassignRelationshipManager",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "relationship_manager_id": "rm-br-02",
                },
            ),
             Action(
                name="addEmployerToCustomerProfile",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "employer": "Rio FC",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_043",
        instruction="As a business banker supporting Gabriel Silva (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21), he is experiencing a temporary cash flow shortfall. Acquire his total business balance and risk profile. Inspect his active business loan (loan_biz_016). To aid him, extend the loan's maturity date to 2028-03-10. Review his latest account activities in his checking account (acc_chk_22001). To ensure liquidity, increase his overdraft limit to 150,000 HUF. He must make an urgent payment to his landlord, 'Klaus Schmidt' (beneficiary_id 'bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a', necessitating verification). Proceed with transferring 200,000 HUF to this beneficiary. Create a support ticket for the loan modification to document the forbearance action. Communicate the updated loan maturity date and new overdraft limit.",
        actions=[
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}
            ),
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}
            ),
            Action(
                name="listActiveLoansWithBalances",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}
            ),
            Action(
                name="adjustLoanPaymentDueDate",
                kwargs={"loan_id": "loan_biz_016", "new_due_date": "2028-03-10"},
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_22001"]}
            ),
            Action(
                name="reviewOverdraftActivityAndAdjustLimit",
                kwargs={"account_id": "acc_chk_22001", "new_limit": 150000.00},
            ),
            Action(
                name="verifyBeneficiaryExists",
                kwargs={"beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}
            ),
            Action(
                name="initiateFundTransferToBeneficiary",
                kwargs={
                    "source_account_id": "acc_chk_22001",
                    "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a",
                    "amount": 200000.00,
                },
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21",
                    "transaction_id": "loan_biz_016",
                    "reason": "Loan forbearance documentation",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_044",
        instruction="In your role as a security analyst for Chloe Dubois (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1), he has reported an incident of identity theft. Begin by obtaining his total balance and quickly secure both his checking (acc_chk_8001) and savings (acc_sav_8002) accounts. Review his recent activities. A fraudulent identity was created using his SSN's last four digits '1123'; consolidate these duplicate records. As part of the resolution, initiate a KYC refresh. Retrieve his communication methods and switch his preference to 'Phone'. Assign 'rm-de-09', an expert in fraud matters, as his new relationship manager. Lastly, create a support ticket related to his checking account to document the identity theft case with the note 'Identity Theft and Account Remediation'. Provide a report on his total balance, the locked status of his accounts, and his new relationship manager.",
        actions=[
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="lockAccountManually",
                kwargs={"account_id": "acc_chk_8001"},
            ),
            Action(
                name="lockAccountManually",
                kwargs={"account_id": "acc_sav_8002"},
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_8001", "acc_sav_8002"]}
            ),
            Action(
                name="mergeDuplicateCustomersBySsn",
                kwargs={"ssn_last_4": "1123"},
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                },
            ),
            Action(
                name="getCustomerContactMethods",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "new_channel": "Phone",
                },
            ),
            Action(
                name="reassignRelationshipManager",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "relationship_manager_id": "rm-de-09",
                },
            ),
            Action(
                name="createSupportTicketForAccount",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "account_id": "acc_chk_8001",
                    "reason": "Identity Theft and Account Remediation",
                },
             )
        ],
        outputs=[]
    ),
   Task(
        annotator="0",
        user_id="USER_045",
        instruction="As a financial wellness agent assessing the profile of retiree Lakshmi Narayanan (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24), collect her risk assessment and total balance. Evaluate her total deposits over the last 3 months (2023-08-01 to 2023-10-31) to verify her fixed income. Check all scheduled payments in her savings account (acc_sav_25001). For her payment 'sp_a3o5b4n6-m1n0-o9p8-q7r6-s5t4u3v2w1x0', ensure her current balance is sufficient. Gather her communication methods and change her preference from 'Mail' to 'Phone'. Open a support ticket for her savings account to document the financial review and recommendations with the reason 'Financial wellness review documentation'. Present her total deposits and credit score in the report.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}
            ),
            Action(
                name="getTotalDepositsOverPeriod",
                kwargs={
                    "account_ids": ["acc_sav_25001"],
                    "start_date": "2023-08-01",
                    "end_date": "2023-10-31",
                },
            ),
            Action(
                name="getPaymentScheduleForAccount",
                kwargs={"account_id": "acc_sav_25001"},
            ),
            Action(
                name="checkFundsForNextScheduledPayment",
                kwargs={"payment_id": "sp_a3o5b4n6-m1n0-o9p8-q7r6-s5t4u3v2w1x0"},
            ),
            Action(
                name="getCustomerContactMethods",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "new_channel": "Phone",
                },
            ),
            Action(
                name="createSupportTicketForAccount",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "account_id": "acc_sav_25001",
                    "reason": "Financial wellness review documentation",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_046",
        instruction="Act as the mortgage advisor for Kenji Tanaka (a1b2c3d4-e5f6-7890-1234-567890abcdef-16), who seeks to apply for a new mortgage. Ascertain his risk profile and aggregate balance. Calculate his income by adding up total deposits over the last 12 months (e.g., 2022-11-01 to 2023-10-31) from all his accounts (acc_chk_17001 and acc_sav_17002). Assess his current debt by compiling a list of all active loans, noting that he has a settled mortgage (loan_mort_010). Analyze his recent expenditures by reviewing transactions across all accounts. To finalize his profile, update his employer information to 'Oceanic Institute'. Subsequently, open a support ticket tied to his savings account (acc_sav_17002) to document the pre-qualification analysis. Provide his credit score, total active loan balance, and total deposits identified.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}
            ),
            Action(
                name="getTotalDepositsOverPeriod",
                kwargs={
                    "account_ids": ["acc_chk_17001", "acc_sav_17002"],
                    "start_date": "2022-11-01",
                    "end_date": "2023-10-31",
                },
            ),
            Action(
                name="listActiveLoansWithBalances",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_17001", "acc_sav_17002"]},
            ),
            Action(
                name="addEmployerToCustomerProfile",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "employer": "Oceanic Institute",
                },
            ),
            Action(
                name="createSupportTicketForAccount",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "account_id": "acc_sav_17002",
                    "reason": "Mortgage pre-qualification analysis",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_047",
        instruction="Operate as the wire transfer officer. Zoltan Nagy (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) is executing a $2,500 international wire transfer. Start by confirming his risk profile and total balance across all accounts. Examine his last 20 transactions for any signs of suspicious activity. Verify that the beneficiary, 'Metropolis Power & Light' (bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a), is valid. Proceed with the international wire transfer from acc_chk_3001 to this beneficiary using the description 'Business payment for overseas supplier'. Initiate a KYC refresh due to 'International transfer requiring enhanced verification'. Create a support ticket for his checking account for 'Wire transfer support'. Share the customer's AML risk level and detailed transaction information.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_3001"], "limit": 20}
            ),
            Action(
                name="verifyBeneficiaryExists",
                kwargs={"beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a"}
            ),
            Action(
                name="initiateFundTransferToBeneficiary",
                kwargs={
                    "source_account_id": "acc_chk_3001",
                    "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a",
                    "amount": 2500.00,
                    "description": "Business payment for overseas supplier"
                }
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                }
            ),
            Action(
                name="createSupportTicketForAccount",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_chk_3001",
                    "reason": "Wire transfer support"
                }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_048",
        instruction="Serve as the private banker for Zoltan Nagy (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a), who is organizing his estate plan. Begin by evaluating his total balance and risk profile. Retrieve all his beneficiaries under the 'Business' category. Ensure that his utility provider, 'Metropolis Power & Light' (bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a), is correctly documented. His intended action is to alter his scheduled payment to this utility (sp_b3a2c1d9-e7f6-a5b4-c3d2-e1f0a9b8c7d6) to 400.00 USD. Investigate transactions from his investment account (acc_inv_3002). Shift his relationship management to 'rm008' for focused estate planning support. Implement a KYC refresh. Next, establish a support ticket related to estate planning updates with the reason 'Estate plan beneficiary and payment update'. Report the number of business beneficiaries, the revised scheduled payment, and the new relationship manager.",
        actions=[
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="fetchBeneficiariesByRelationship",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "relationship": "Utility Provider"},
            ),
            Action(
                name="verifyBeneficiaryExists",
                kwargs={"beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a"},
            ),
            Action(
                name="updateScheduledPaymentAmount",
                kwargs={
                    "payment_id": "sp_b3a2c1d9-e7f6-a5b4-c3d2-e1f0a9b8c7d6",
                    "amount": 400.00,
                },
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_inv_3002"]},
            ),
            Action(
                name="reassignRelationshipManager",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "relationship_manager_id": "rm008",
                },
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                },
            ),
            Action(
                name="createSupportTicketForAccount",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_inv_3002",
                    "reason": "Estate plan beneficiary and payment update",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_049",
        instruction="Function as a compliance officer upon a legal mandate regarding Isabella Rossi (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25). His personal loan (loan_pers_020) is in arrears. First, assess his total balance and risk profile, along with the loan details. Immediately secure his checking account (acc_chk_26001) to protect funds. Since there are no beneficiaries, payment setup is unattainable. Review his recent transactions. In response to the legal instruction, deactivate his checking account. Change his communication mode to 'Mail' for official correspondence. Create a support ticket associated with the transaction 'txn_3b4c5d6e-7f8g-9h0i-1j2k-3l4m5n6o7p8q' for legal procedures citing 'Legal account garnishment documentation'. Execute a KYC refresh. Additionally, obtain his registered contact information for legal communication. Report the customer's total balance, the current status of his checking account, and his KYC status.",
        actions=[
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"}
            ),
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"}
            ),
            Action(
                name="GetLoanDetails",
                kwargs={"loan_id": "loan_pers_020"}
            ),
            Action(
                name="lockAccountManually",
                kwargs={"account_id": "acc_chk_26001"},
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_26001"]},
            ),
            Action(
                name="deactivateAccountByRequest",
                kwargs={
                    "account_id": "acc_chk_26001"
                },
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "new_channel": "Mail",
                },
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "transaction_id": "txn_3b4c5d6e-7f8g-9h0i-1j2k-3l4m5n6o7p8q",
                    "reason": "Legal account garnishment documentation",
                },
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                },
            ),
            Action(
                name="getCustomerContactMethods",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_050",
        instruction="Support Gabriel Silva (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12) with her digital wallet connection. Confirm her total balance and risk profile. Review recent transactions on her checking account (acc_chk_13001) and assess her overdraft limit. As required by the updated service terms, perform a KYC refresh and update her communication mode to 'App'. She has one scheduled payment (sp_a6c8d7b9-a3b2-c1d0-e9f8-g7h6i5j4k3l2); ensure the availability of funds and examine its specifics. Acquire her contact methods for app configuration. Finally, open a support ticket for her checking account regarding 'Digital wallet integration'. Report her total balance, overdraft limit, and KYC status.",
        actions=[
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}
            ),
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_13001"]},
            ),
            Action(
                name="getAccountOverdraftLimit",
                kwargs={"account_id": "acc_chk_13001"},
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12",
                },
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12",
                    "new_channel": "App",
                },
            ),
            Action(
                name="checkFundsForNextScheduledPayment",
                kwargs={"payment_id": "sp_a6c8d7b9-a3b2-c1d0-e9f8-g7h6i5j4k3l2"},
            ),
            Action(
                name="createSupportTicketForAccount",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12",
                    "account_id": "acc_chk_13001",
                    "reason": "Digital wallet integration"
                }
            ),
            Action(
                name="getPaymentScheduleForAccount",
                kwargs={
                    "account_id": "acc_chk_13001"
                }
            ),
            Action(
                name="getCustomerContactMethods",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_051",
        instruction="Facilitate the onboarding of Elena Popescu (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19), a new high-net-worth client. Gather her risk profile and total balance. Review all of her accounts. Calculate her total deposits for the previous year (2022-11-01 to 2023-10-31). She wishes to open a new Investment account. Since creation is not possible, review her current 'Checking' accounts instead. Check her recurring transfer setup to her landlord 'Klaus Schmidt' (bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a). Change her scheduled payment 'sp_b8j1a9i2-h6i5-j4k3-l2m1-n0o9p8q7r6s5' to 80,000 CLP. Implement a KYC update and assign her relationship manager to 'rm-cl-01', a senior wealth advisor. Present her credit score, total deposits, and new relationship manager.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_chk_20001"], "start_date": "2022-11-01", "end_date": "2023-10-31"}),
            Action(name="getCustomerAccountsByType", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "account_type": "Checking"}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="updateScheduledPaymentAmount", kwargs={"payment_id": "sp_b8j1a9i2-h6i5-j4k3-l2m1-n0o9p8q7r6s5", "amount": 80000.00}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", }),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "relationship_manager_id": "rm-cl-01"}),
        ],
        outputs=[]
    ),

    # TASK 32: Management of Accounts for Deceased Clients
    # NUMBER OF EDGES: 13
    Task(
        annotator="0",
        user_id="USER_052",
        instruction="Arrange the accounts of a deceased client, Santiago Muñoz (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18). Determine her total balance. Review all her active loans and recent transactions. Identify all her 'Personal' beneficiaries. Her personal loan (loan_pers_013) must be settled. Carry out a 3,500 EUR payment on the loan from her checking account (acc_chk_19001) to complete it. Post loan settlement, deactivate her checking account. Open a final support ticket for her checking account to document the estate closure process citing 'Estate closure process documentation' as the reason. Switch her communication preference to 'Mail' for legal correspondence. Provide the final balance report before account closure and assess the loan and checking account status.",
        actions=[
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_19001"]}),
            Action(name="fetchBeneficiariesByRelationship", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "relationship": "Personal"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_pers_013", "from_account_id": "acc_chk_19001", "amount": 3500.00}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_chk_19001"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "account_id": "acc_chk_19001", "reason": "Estate closure process documentation"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "new_channel": "Mail"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_053",
        instruction="Examine an account takeover for Kenji Tanaka (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). Access his risk profile. Secure all three of his accounts (acc_chk_1001, acc_sav_1002, acc_crd_1003). Evaluate all recent transactions. Fraudulent parties executed three unauthorized transactions: 'txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f', 'txn_8b1c4d6f-2b4f-5a9d-9b3f-6d7b9c4e5a1a', and 'txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c'. Make full reimbursements for all three. Check for any 'Security' related support tickets. Enforce a KYC update. Reassign his relationship manager to a fraud specialist ('rm008'). Generate a new high-priority support ticket referencing 'txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c' with the explanation 'Account Takeover Investigation'. Provide a report on the refunded amount, the current status of his accounts, and his updated relationship manager.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_crd_1003"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_1001", "acc_sav_1002", "acc_crd_1003"]}),
            Action(name="applyPartialRefundToTransaction", kwargs={"transaction_id": "txn_9c2a3b7e-1a3e-4b8c-8a2e-5c6a8b3d4e9f", "refund_amount": 75.50}),
            Action(name="applyPartialRefundToTransaction", kwargs={"transaction_id": "txn_8b1c4d6f-2b4f-5a9d-9b3f-6d7b9c4e5a1a", "refund_amount": 12.75}),
            Action(name="applyPartialRefundToTransaction", kwargs={"transaction_id": "txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c", "refund_amount": 250.00}),
            Action(name="findRecentSupportTicketsByCategory", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "category": "Security"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", }),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "relationship_manager_id": "rm008"}),
            Action(name="createSupportTicketForTransaction", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "transaction_id": "txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c", "reason": "Account Takeover Investigation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_054",
        instruction="Assist Oliver Williams (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23) with divesting from a business. Verify his total balance and risk profile. He must pay off his business loan (loan_biz_009) which is 7,500,000 NGN using his savings (acc_sav_24002). Once the loan is repaid, suspend his business checking account (acc_chk_24001). Although deletion is not feasible, verify the status of his scheduled payment (sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w1) as it is no longer needed. Inspect his personal beneficiaries. Lastly, amend his employment status from 'Self-Employed' to 'Consultant'. Create a support ticket linked with his savings account 'acc_sav_24002' with the purpose 'Business advising'. Report his final total balance, the business loan status, and the checking account situation.",
        actions=[
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_biz_009", "from_account_id": "acc_sav_24002", "amount": 7500000.00}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_chk_24001"}),
            Action(name="checkFundsForNextScheduledPayment", kwargs={"payment_id": "sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w1"}),
            Action(name="fetchBeneficiariesByRelationship", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "relationship": "Personal"}),
            Action(name="addEmployerToCustomerProfile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "employer": "Consultant"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "account_id": "acc_sav_24002", "reason": "Business advising"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_055",
        instruction="Oversee an audit on the account of a likely high-frequency trader, Zoltan Nagy (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). Obtain his risk profile. Establish his total balance. Review the last 100 transactions for his investment account (acc_inv_3002). Total the deposits into this account over the previous quarter (2023-08-01 to 2023-10-31). Evaluate his active loans. Due to heightened risk behaviors, impose a KYC refresh. Inspect his scheduled payments for 'acc_chk_3001'. Designate 'rm009', a capital markets specialist, as his new relationship manager. Open a support ticket for his investment account to record the audit with the reason 'High-frequency trading audit'. Report the total deposits and update the KYC status.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_inv_3002"], "limit": 100}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_inv_3002"], "start_date": "2023-08-01", "end_date": "2023-10-31"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_3001"}),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "relationship_manager_id": "rm009"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "account_id": "acc_inv_3002", "reason": "High-frequency trading audit"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_056",
        instruction="Counsel Elena Popescu (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19) on global expansion strategies. Manage her risk profile assessment and ascertain her total balance. Review transactions in her checking account (acc_chk_20001). She needs to fulfill a payment to an overseas supplier, identified as the beneficiary 'Klaus Schmidt' (bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a). Validate this beneficiary. Then, execute a 5,000,000 CLP transfer from her checking account. Modify her mortgage's maturity date to 2036-01-01 for loan_mort_014 to assist in cash flow for expansion. Conduct a KYC update due to this crucial business transition. Update her employer to 'Atacama Observatory'. Open a support ticket concerning her checking account with the note 'International expansion advice'. Display her credit score and the adjusted loan maturity date.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_20001"]}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="getAccountBalance", kwargs={"account_id": "acc_chk_20001"}),
            Action(name="initiateFundTransferToBeneficiary", kwargs={"source_account_id": "acc_chk_20001", "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a", "amount": 5000000.00}),
            Action(name="adjustLoanPaymentDueDate", kwargs={"loan_id": "loan_mort_014", "new_due_date": "2036-01-01"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", }),
            Action(name="addEmployerToCustomerProfile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "employer": "Atacama Observatory"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "account_id": "acc_chk_20001", "reason": "International expansion advice"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_057",
        instruction="As a fraud analyst, look into potential elder financial exploitation for Lakshmi Narayanan (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24). Obtain his risk profile and confirm his total balance. Immediately protect his savings account (acc_sav_25001). Initiate a support ticket linked to the savings account with the statement 'Fraud Investigation'. Assess his recent transaction records for any anomalies. Summarize his total deposits for the past six months (2023-05-01 to 2023-10-31). Review planned payments. A new, unverified beneficiary ('Kenji Tanaka' - bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f) requires confirmation. Since his communication preference is 'Mail', switch it to 'Phone' for prompt contact. Deactivate his savings account. Provide a report detailing the customer's total balance, the current state of the savings account, and the number of scheduled payments.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_sav_25001"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_sav_25001"]}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_sav_25001"], "start_date": "2023-05-01", "end_date": "2023-10-31"}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_sav_25001"}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "new_channel": "Phone"}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_sav_25001"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "account_id": "acc_sav_25001", "reason": "Fraud Investigation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_058",
        instruction="Oversee the underwriting process for a joint mortgage for Zoltan Nagy (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) and Kenji Tanaka (a1b2c3d4-e5f6-7890-1234-567890abcdef-16). Start by collecting the risk profiles for both applicants. Calculate each applicant's total balance. There appears to be a shared SSN suffix ('1122') between them, indicating a possible data duplication issue; merge these customer profiles. After merging, retrieve all accounts for David. Examine every active loan under the merged customer profile. Moreover, David requests his communication preference be updated to 'Email'. Conduct a KYC upgrade for the primary applicant. Create a support ticket for Zoltan Nagy's investment account (acc_inv_3002) noting the joint mortgage process. Produce a report with the credit scores of both original applicants.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}),
            Action(name="mergeDuplicateCustomersBySsn", kwargs={"ssn_last_4": "1122"}),
            Action(
                name="getAllAccountsForCustomer",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "new_channel": "Email"
                }
            ),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "account_id": "acc_inv_3002", "reason": "Joint mortgage application documentation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_059",
        instruction="Support farmer Zoltan Nagy (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11) with his seasonal preparations. Determine his total balance and evaluate his risk profile. He wants to perform a 3000 EUR overpayment on his business loan (loan_biz_005) using his checking account (acc_chk_12001). After the payment, adjust the loan maturity date to 2027-06-01 to align with the next harvesting season. Inspect his recent financial transactions. Raise his checking account's overdraft limit to 500 EUR for operational flexibility. He must pay 'London Electricity Co.' (bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d); ensure this beneficiary is confirmed. Review his current scheduled payments. Change his communication preference to 'Phone'. Submit a report detailing the new loan balance, updated overdraft limit, and his credit score.",
        actions=[
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_biz_005", "from_account_id": "acc_chk_12001", "amount": 3000.00}),
            Action(name="adjustLoanPaymentDueDate", kwargs={"loan_id": "loan_biz_005", "new_due_date": "2027-06-01"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_12001"]}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_12001", "new_limit": 500.00}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_12001"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "new_channel": "Phone"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_060",
        instruction="In the capacity of a financial consultant for Zoltan Nagy (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13), who just completed bankruptcy proceedings, begin with accessing his risk profile and total balance. Investigate each loan associated with the account 'acc_chk_14001', emphasizing the auto loan (loan_auto_015) status review. Examine scheduled payments on his checking account (acc_chk_14001) for any lapses or delinquency. Update his employer information to 'Global Analytics' and record this change in his customer profile. A KYC update is mandatory as part of the rehabilitation strategy. Furthermore, evaluate his overdraft limits on the account. Finally, change his communication preference to 'Email' and create a support ticket within the account, summarizing the rehabilitation strategy with the note 'Recovery plan summary'. Provide a comprehensive report on his total balance, loan overview, scheduled payments analysis, employer details, overdraft limits, and confirmation of the modified communication preference.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="GetLoanDetails", kwargs={"loan_id": "loan_auto_015"}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_14001"}),
            Action(name="addEmployerToCustomerProfile", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "employer": "Global Analytics"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="getAccountOverdraftLimit", kwargs={"account_id": "acc_chk_14001"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "new_channel": "Email"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "account_id": "acc_chk_14001", "reason": "Recovery plan summary"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_061",
        instruction="Manage the advisory responsibilities for Elena Popescu (a1b2c3d4-e5f6-7890-1234-567890abcdef), a graphic designer located in Canada. Start by evaluating her risk profile and total balance. She holds a significant deposit in her checking account (acc_chk_2001); confirm verification of her 'Family' type beneficiary 'Kenji Tanaka' (bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f). Ensure there are sufficient funds for her scheduled payment 'sp_e5m7b6l8-k3l2-m1n0-o9p8-q7r6s5t4u3v2' and adjust the payment amount to 400 CAD. Being a retail customer, carry out a KYC update. Produce a support ticket related to her student loan (loan_stud_012) with the issue 'Inquiry about student loan deferment options'. Assemble her total balance, the modified scheduled payment amount, and her KYC status in a report.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="verifyBeneficiaryExists",
                kwargs={"beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}
            ),
            Action(
                name="checkFundsForNextScheduledPayment",
                kwargs={"payment_id": "sp_e5m7b6l8-k3l2-m1n0-o9p8-q7r6s5t4u3v2"}
            ),
            Action(
                name="updateScheduledPaymentAmount",
                kwargs={"payment_id": "sp_e5m7b6l8-k3l2-m1n0-o9p8-q7r6s5t4u3v2", "amount": 400.00}
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "transaction_id": "loan_stud_012",
                    "reason": "Inquiry about student loan deferment options"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_062",
        instruction="Supervise proactive relationship management for Oliver Williams (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6). Compile her risk profile and full balance. Review her recent transactions covering the last 50 entries for all accounts (acc_chk_7001, acc_sav_7002); observe a reduction in investment-related transactions. Check on her active mortgage (loan_mort_018) to ascertain its current standing. Proactively, increase the overdraft limit on her checking account to 7,500 AED. Confirm her scheduled payments. To enhance personalized service, assign her to a senior private banker ('rm-ae-03'). Modify her communication preference to 'App'. Prepare a support ticket about her checking account with the justification 'Account consultation'. Include her full balance, the new overdraft limit, and her designated relationship manager in your report.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_7001", "acc_sav_7002"], "limit": 50}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_7001", "new_limit": 7500.00}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_7001"}),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "relationship_manager_id": "rm-ae-03"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "new_channel": "App"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "account_id": "acc_chk_7001", "reason": "Account consultation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_063",
        instruction="Oversee the advisory process for Santiago Muñoz (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18) regarding debt consolidation. Access her risk profile and total balance. Analyze all of her active loans. She aims to settle her personal loan (loan_pers_013) immediately from her checking account (acc_chk_19001). After payment, reassess the scheduled payments in her checking account. Verify she has no other loans for consolidation. To improve her credit score, evaluate the overdraft limit on her account. Finalize the plan by updating her employer to 'Ljubljana High School' and switching her communication preference to 'SMS'. Log a support ticket related to her checking account with the reason 'Debt consolidation'. Present her credit score and personal loan status in the report.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_pers_013", "from_account_id": "acc_chk_19001", "amount": 3500.00}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_19001"}),
            Action(name="getAccountOverdraftLimit", kwargs={"account_id": "acc_chk_19001"}),
            Action(name="addEmployerToCustomerProfile", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "employer": "Ljubljana High School"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "new_channel": "SMS"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "account_id": "acc_chk_19001", "reason": "Debt consolidation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_064",
        instruction="Organize an AML audit for Elena Popescu (a1b2c3d4-e5f6-7890-1234-567890abcdef), with accounts in different currencies (USD and CAD). Gather her risk profile and total balance, taking into account the diverse currencies. Review all transactions across her accounts (acc_chk_2001, acc_sav_2002). Calculate her total deposits for the past quarter (2023-08-01 to 2023-10-31). Review her active loans. Due to cross-border activities, ensure a KYC refresh is implemented. Check the funds for her scheduled payment (sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f). Conclude by creating a support ticket linked to her checking account (acc_chk_2001) for the reason 'AML audit'. Acquire her contact methods for possible escalation. Deliver a report detailing her AML risk level and KYC status.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_2001", "acc_sav_2002"]}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_chk_2001", "acc_sav_2002"], "start_date": "2023-08-01", "end_date": "2023-10-31"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="checkFundsForNextScheduledPayment", kwargs={"payment_id": "sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "account_id": "acc_chk_2001", "reason": "AML audit"}),
            Action(name="getCustomerContactMethods", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_065",
        instruction="Conduct an investigation into the suspicious activity reported by customer Kenji Tanaka (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e). Initially, confirm their risk profile and closely examine the last 25 transactions across all accounts. You have identified transaction 'txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c' with an amount of -$250 as potentially fraudulent. File a high-priority support ticket for fraud concerning this transaction stating 'Unauthorized online charge'. Execute a necessary KYC refresh for the customer. Secure the checking account acc_chk_1001 without delay as part of the investigation. Report the number of transactions reviewed and the total of the suspicious transaction.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_1001", "acc_sav_1002", "acc_crd_1003"], "limit": 25}
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "transaction_id": "txn_6c3d6f9h-4d6b-7c2f-2d5h-8f9d2e6g7c3c",
                    "reason": "Unauthorized online charge"
                }
            ),
            Action(
                name="enforceKycRefreshForCustomer",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                }
            ),
            Action(
                name="lockAccountManually",
                kwargs={
                    "account_id": "acc_chk_1001"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_066",
        instruction="Your task is to manage an annual financial assessment for Chloe Dubois (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). Start by retrieving all account details using his customer ID. Proceed to obtain his risk profile and current total balance. Ascertain his overall deposits for the past 12 months (2022-11-01 to 2023-10-31) from every account. Review his active loans. He proposes a year-end overpayment of 5,000 EUR on his mortgage (loan_mort_014) through his savings account (acc_sav_8002). Appraise his scheduled payments linked to his checking account. Identify any 'Resolved' support tickets from the preceding year. Handle his annual KYC update. Finally, file a new support ticket concerning his checking account, summarizing the annual review with the explanation 'Annual Financial Review Summary 2023'. Record his credit score, the revised mortgage balance, and total annual deposits.",
        actions=[
            Action(name="getAllAccountsForCustomer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_chk_8001", "acc_sav_8002"], "start_date": "2022-11-01", "end_date": "2023-10-31"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_mort_014", "from_account_id": "acc_sav_8002", "amount": 5000.00}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="findRecentSupportTicketsByCategory", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "category": "Resolved"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", }),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "account_id": "acc_chk_8001", "reason": "Annual Financial Review Summary 2023"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_067",
        instruction="Your role as a credit analyst involves processing a loan application. Elena Popescu (a1b2c3d4-e5f6-7890-1234-567890abcdef) is applying for a mortgage. Verify her risk profile and total balance across all accounts. Examine her existing loan commitments and available contact options. Change her communication preference to 'Email'. Add 'Creative Minds LLC' as her employer in the profile. Review her overdraft limit on acc_chk_2001 to determine creditworthiness. Deliver the customer's credit score, aggregate balance, current active loan count, and overdraft limit.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="listActiveLoansWithBalances",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="getCustomerContactMethods",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "new_channel": "Email"
                }
            ),
            Action(
                name="addEmployerToCustomerProfile",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "employer": "Creative Minds LLC"
                }
            ),
            Action(
                name="getAccountOverdraftLimit",
                kwargs={"account_id": "acc_chk_2001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_068",
        instruction="Coordinate as a financial planner for IT contractor Zoltan Nagy (a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4) with accounts 'acc_chk_5002' for checking and 'acc_sav_5001' for savings. Assess his risk profile and combined balance. Calculate his total deposits for both 'acc_chk_5002' and 'acc_sav_5001' over the past 6 months (2023-05-01 to 2023-10-31) to evaluate his income stream. Examine his active auto loan (loan_auto_019). He plans a 200,000 INR overpayment on this loan from his savings account (acc_sav_5001). Verify his scheduled payments involving his checking account. Review the open ticket (tkt_c1d0e9f8-e9f8-g7h6-i5j4-k3l2m1n0o9p8) under 'Security'; analyze its specifics. Update his employer to 'Global Tech Services'. Modify his relationship manager to 'rm-in-02'. Document his credit score.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_sav_5001", "acc_chk_5002"], "start_date": "2023-05-01", "end_date": "2023-10-31"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_auto_019", "from_account_id": "acc_sav_5001", "amount": 200000.00}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_5002"}),
            Action(name="findRecentSupportTicketsByCategory", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4", "category": "Security"}),
            Action(name="addEmployerToCustomerProfile", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4", "employer": "Global Tech Services"}),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4", "relationship_manager_id": "rm-in-02"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_069",
        instruction="Your duty as a credit counselor is to support Sofia Andersson (f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9), who possesses a low credit rating. Retrieve her risk profile and full balance. Investigate her active loans using her customer ID. Confirm her checking account's (acc_chk_4001) overdraft limit. Review her most recent transactions. Her KYC status is 'Pending'; perform a KYC refresh to renew it. Change her employer to 'State University'. Verify sufficient funds for her scheduled payment ('sp_e2g4b3f5-e9f8-g7h6-i5j4-k3l2m1n0o9p5'). Generate a support ticket for her student loan (loan_stud_004) with the reason 'Inquiry about income-driven repayment plans'. Alter her communication preference to 'Email'. Provide her credit score, updated KYC status, and the account overdraft limit.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}),
            Action(name="getAccountOverdraftLimit", kwargs={"account_id": "acc_chk_4001"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_4001"]}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9", }),
            Action(name="addEmployerToCustomerProfile", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9", "employer": "State University"}),
            Action(name="checkFundsForNextScheduledPayment", kwargs={"payment_id": "sp_e2g4b3f5-e9f8-g7h6-i5j4-k3l2m1n0o9p5"}),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "new_channel": "Email"
                }
            ),
            Action(name="createSupportTicketForTransaction", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9", "transaction_id": "loan_stud_004", "reason": "Inquiry about income-driven repayment plans"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_070",
        instruction="Your responsibility is to facilitate account closures for Chloe Dubois (e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14), who is moving abroad. Obtain her risk profile and total balance. She has a settled auto loan (loan_auto_015); examine her other loans. She wishes to transfer her checking account balance (45000 SEK from acc_chk_15001) to 'Marie Dubois' (bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c), which requires verification first. Deactivate her checking account after the transfer. Evaluate her scheduled payments. Identify any support tickets associated with 'Beneficiary Management'. Update her communication preference to 'Email' for the final account statements. Report her closing checking account balance, account status, and credit score.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14"}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c"}),
            Action(name="initiateFundTransferToBeneficiary", kwargs={"source_account_id": "acc_chk_15001", "beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c", "amount": 45000.00}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_chk_15001"}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_15001"}),
            Action(name="findRecentSupportTicketsByCategory", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14", "category": "Beneficiary Management"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14", "new_channel": "Email"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_071",
        instruction="Handle the completion of the estate belonging to Chloe Dubois (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). Acquire his risk profile and total balance; settle the mortgage (loan_mort_014) by disbursing 125,000 EUR from savings (acc_sav_8002). Adjust the landlord's scheduled payment (sp_d9b3a2c1-b4c3-d2e1-f0a9-b8c7d6e5f4a3) on checking (acc_chk_8001) to an amount of 0. Identify all 'Resolved' support tickets; deactivate checking (acc_chk_8001), savings (acc_sav_8002), and investment (acc_inv_3002) accounts. Update communication preference to 'Mail'. Launch a final support ticket for estate closure associated with acc_inv_3002 with the reason 'Estate Closure Documentation'. Share the investment balance, statuses of all accounts, and the amended scheduled payment amount.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_mort_014", "from_account_id": "acc_sav_8002", "amount": 125000.00}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="updateScheduledPaymentAmount", kwargs={"payment_id": "sp_d9b3a2c1-b4c3-d2e1-f0a9-b8c7d6e5f4a3", "amount": 0.00}),
            Action(name="findRecentSupportTicketsByCategory", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "category": "Resolved"}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_sav_8002"}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_inv_3002"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "new_channel": "Mail"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1", "account_id": "acc_inv_3002", "reason": "Estate Closure Documentation"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="getAccountBalance", kwargs={"account_id": "acc_inv_3002"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_072",
        instruction="Oversee the audit and consolidation of profiles for Elena Popescu (a1b2c3d4-e5f6-7890-1234-567890abcdef) and Kenji Tanaka (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e), who are business partners. First, collate all their accounts. Extract the risk profile and total balance for both. For the joint profile, review all transactions across all accounts ('acc_chk_2001', 'acc_sav_2002', 'acc_chk_1001', 'acc_sav_1002', 'acc_crd_1003'). Calculate the total deposits from the past year (2022-11-01 to 2023-10-31). Investigate all active loans for Elena Popescu's account. Implement a KYC refresh on Elena Popescu's account and appoint 'rm010', an international specialist, as the relationship manager. Confirm the scheduled payment for Jane's account. Disable Kenji Tanaka's credit card (acc_crd_1003). Provide the credit scores of both individuals, the updated combined total balance, and the status of the deactivated account.",
        actions=[
            Action(name="getAllAccountsForCustomer", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="getAllAccountsForCustomer", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_2001", "acc_sav_2002", "acc_chk_1001", "acc_sav_1002", "acc_crd_1003"]}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_chk_2001", "acc_sav_2002", "acc_chk_1001", "acc_sav_1002", "acc_crd_1003"], "start_date": "2022-11-01", "end_date": "2023-10-31"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "relationship_manager_id": "rm010"}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_crd_1003"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_073",
        instruction="Take on the investigation into potential money laundering for Isabella Rossi (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25). His personal loan (loan_pers_020) is overdue. Obtain his risk profile. Immediately lock his checking account (acc_chk_26001). Calculate his total deposits over the last 3 months (2023-08-01 to 2023-10-31). Review all recent transactions. Analyze his scheduled payments. Retrieve his contact methods and change his preference to 'Phone' for prompt contact. Deactivate his checking account. Change his manager to a high-risk specialist ('rm-eg-04'). Conduct an urgent KYC refresh. Initiate a high-priority support ticket for the account to formally document the case escalation using 'AML Case Escalation' as the reason. Present the customer's AML risk level, the total deposits calculated, and the account’s status.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_chk_26001"}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_chk_26001"], "start_date": "2023-08-01", "end_date": "2023-10-31"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_26001"]}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_26001"}),
            Action(name="getCustomerContactMethods", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25", "new_channel": "Phone"}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_chk_26001"}),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25", "relationship_manager_id": "rm-eg-04"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25", }),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25", "account_id": "acc_chk_26001", "reason": "AML Case Escalation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_074",
        instruction="Manage the comprehensive portfolio exit for Oliver Williams (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6). Obtain her total balance and risk profile. Start with clearing her mortgage (loan_mort_018) balance of 750000 AED from her savings account (acc_sav_7002). Subsequently, she intends to transfer her remaining savings and checking balances to her external business, 'Dubai International School' (bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f), requiring verification. Process a transfer for 150000 from her checking account (acc_chk_7001) to the beneficiary account. After the transfers, deactivate both accounts. Review her scheduled payments. Check for any 'Security' related support tickets. Change her communication preference to 'Mail' for final legal notices. Provide the final status of both accounts.",
        actions=[
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_mort_018", "from_account_id": "acc_sav_7002", "amount": 750000.00}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f"}),
            Action(name="initiateFundTransferToBeneficiary", kwargs={"source_account_id": "acc_chk_7001", "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f", "amount": 150000.00}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_sav_7002"}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_chk_7001"}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_7001"}),
            Action(name="findRecentSupportTicketsByCategory", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "category": "Security"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "new_channel": "Mail"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_075",
        instruction="Guide tech entrepreneur Kenji Tanaka (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) on his stock options exercise strategy. Obtain his risk profile and total balance. Begin by releasing capital through settling his auto loan (loan_auto_002) of 5000.50 USD from his checking account (acc_chk_1001). He needs additional liquidity; allocate 750 USD from transaction 'txn_7a2b5e8g-3c5a-6b1e-1c4g-7e8c1d5f6b2b' to the savings account (acc_sav_1002), while the remaining 750 USD should go to the checking account (acc_chk_1001). Review the last 30 transactions on his credit card (acc_crd_1003). Verify his scheduled payments on the checking account. Amend the overdraft limit on his checking account to 1,000 USD to handle substantial transactions. Initiate a KYC refresh in response to the major change in financial status. Reassign his relationship manager to 'rm005', a specialist in high-net-worth tech clients. Provide the status of his auto loan and his updated overdraft limit.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_auto_002", "from_account_id": "acc_chk_1001", "amount": 5000.50}),
            Action(name="splitTransactionBetweenAccounts", kwargs={"transaction_id": "txn_7a2b5e8g-3c5a-6b1e-1c4g-7e8c1d5f6b2b", "splits": [{"account_id": "acc_sav_1002", "amount": 750.00}, {"account_id": "acc_chk_1001", "amount": 750.00}]}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_crd_1003"], "limit": 30}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_1001", "new_limit": 1000.00}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "relationship_manager_id": "rm005"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_076",
        instruction="Supervise the integration of assets for Zoltan Nagy (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a). Obtain his risk profile and total balance. Address a payment on his mortgage loan (loan_mort_001) from his investment account (acc_inv_3002) amounting to 125,000.00 as specified. Confirm all deposits made to the investment account from 2023-10-22 to 2023-10-29. Analyze all scheduled payments from the investment account (acc_inv_3002). Access his 'Business' beneficiaries and validate 'Metropolis Power & Light' (bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a). Reassign his relationship manager to 'rm010'. Perform a KYC update. Finally, generate a report on the mortgage loan status.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_mort_001", "from_account_id": "acc_inv_3002", "amount": 125000.00}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_inv_3002"], "start_date": "2023-10-22", "end_date": "2023-10-29"}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_inv_3002"}),
            Action(name="fetchBeneficiariesByRelationship", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "relationship": "Business"}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a"}),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "relationship_manager_id": "rm010"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="GetLoanDetails", kwargs={"loan_id": "loan_mort_001"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_077",
        instruction="Evaluate possible structured payments for Gabriel Silva (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21). Gather his risk profile and overall balance. Scrutinize the last 50 transactions on his checking account (acc_chk_22001). Calculate his total deposits from the past year (2022-11-01 to 2023-10-31). Assess the status of his business loan (loan_biz_016). His profile indicates numerous minor, regular scheduled payments; review the payment schedule for his account. As a precautionary measure, promptly lock his checking account. Due to the suspicious activity pattern, disable the account. Immediately proceed with a KYC update. Allocate a new relationship manager 'rm-hu-02', specialized in high-risk cases. Alter his communication preference to 'Mail' for legal matters. Initiate a high-priority support ticket for the account 'acc_chk_22001' to officially document the case escalation with the reason 'AML Case Escalation: Structured Payments'. Record the customer's AML risk level, the number of scheduled payments identified, and the account status.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_22001"], "limit": 50}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_chk_22001"], "start_date": "2022-11-01", "end_date": "2023-10-31"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_22001"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_chk_22001"}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_chk_22001"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", }),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", "relationship_manager_id": "rm-hu-02"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", "new_channel": "Mail"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", "account_id": "acc_chk_22001", "reason": "AML Case Escalation: Structured Payments"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_078",
        instruction="As a payment processor, adjust scheduled payments for customer Kenji Tanaka (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) who has accounts acc_chk_1001, acc_sav_1002, acc_crd_1003. Review their total balance and assess the last 20 transactions across all accounts. Identify scheduled payments set for 2023-11-01 to 2023-11-30. Confirm if they have sufficient funds for the payment 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d'. Update that specific scheduled payment to $350. In conclusion, modify the customer's communication preference to 'SMS'. Document the total balance and verify fund availability for the specified payment.",
        actions=[
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_1001", "acc_sav_1002", "acc_crd_1003"], "limit": 20}
            ),
            Action(
                name="getScheduledPaymentsDueInRange",
                kwargs={"start_date": "2023-11-01", "end_date": "2023-11-30"}
            ),
            Action(
                name="checkFundsForNextScheduledPayment",
                kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}
            ),
            Action(
                name="updateScheduledPaymentAmount",
                kwargs={
                    "payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d",
                    "amount": 350.00
                }
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "new_channel": "SMS"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_079",
        instruction="Assist Oliver Williams (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23) following his business downfall. Source his risk profile and total balance. Evaluate all his active loans. He seeks to apply his savings (acc_sav_24002) for a partial overpayment of 5,000,000 NGN on his business loan (loan_biz_009). Adjust the loan's maturity date to 2028-03-20 to reduce his payments. Review his scheduled payment ('sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w1'); since the business is no longer operational, set its amount to 0. Minimize his checking account (acc_chk_24001) overdraft limit to the minimum (5000 NGN). Deactivate his business savings account (acc_sav_24002). Transition his employment status from 'Self-Employed' to 'Unemployed'. Create a support ticket linked to acc_sav_24002 to document the restructuring agreement with the explanation 'Debt restructuring and forbearance plan'. Present the remaining loan balance and the updated overdraft limit.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_biz_009", "from_account_id": "acc_sav_24002", "amount": 5000000.00}),
            Action(name="adjustLoanPaymentDueDate", kwargs={"loan_id": "loan_biz_009", "new_due_date": "2028-03-20"}),
            Action(name="updateScheduledPaymentAmount", kwargs={"payment_id": "sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w1", "amount": 0.00}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_24001", "new_limit": 5000.00}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_sav_24002"}),
            Action(name="addEmployerToCustomerProfile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "employer": "Unemployed"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "account_id": "acc_sav_24002", "reason": "Debt restructuring and forbearance plan"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_080",
        instruction="Administer the profile of newly identified Politically Exposed Person (PEP), Oliver Williams (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6). Secure her risk profile immediately. Execute a KYC refresh. Reassign her to 'rm-ae-04', an expert in PEP cases. Temporarily lock her savings account (acc_sav_7002) for a security review. Examine all transactions on her checking account (acc_chk_7001) for the last 100 entries. Calculate total deposits from '2023-05-01' to '2023-10-31'. Reduce her checking overdraft limit to zero. Review all her 'Business' beneficiaries. Following the assessment, change her communication preference to 'Email' for a clear audit trail. Generate an urgent support ticket for her account acc_chk_7001 to document the PEP status change and actions taken with the reason 'PEP Status Change and Profile Security Enhancement'. Summarize her AML risk level and the updated overdraft limit.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", }),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "relationship_manager_id": "rm-ae-04"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_sav_7002"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_7001"], "limit": 100}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_chk_7001"], "start_date": "2023-05-01", "end_date": "2023-10-31"}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_7001", "new_limit": 0.00}),
            Action(name="fetchBeneficiariesByRelationship", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "relationship": "Business"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "new_channel": "Email"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "account_id": "acc_chk_7001", "reason": "PEP Status Change and Profile Security Enhancement"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_081",
        instruction="Coordinate an investigation into a fraud ring that includes customers Kenji Tanaka (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) and Elena Popescu (a1b2c3d4-e5f6-7890-1234-567890abcdef). Retrieve the risk profiles and total balances for both individuals. A questionable P2P transfer ('txn_7b8c9d0e-1f2a-3b4c-5d6e-7f8g9h0i1j2k') has been identified between them. Secure all accounts for both clients immediately (John: acc_chk_1001, acc_sav_1002; Jane: acc_chk_2001, acc_sav_2002). Scrutinize all recent transactions for both to detect further collusion. Upon verifying the P2P transfer as fraudulent, terminate all of Kenji Tanaka's accounts as the primary fraudster. For Elena Popescu, require an immediate KYC update. Assign both customers to a high-risk specialist ('rm011'). Create a support ticket for both customers detailing the dismantling of the fraud ring with the reason 'Fraud Ring Takedown Documentation'. Report on Elena Popescu's updated total balance, the status of Kenji Tanaka's accounts, and the new relationship manager.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_sav_2002"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_1001", "acc_sav_1002"]}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_2001", "acc_sav_2002"]}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_chk_1001"}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_sav_1002"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", }),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "relationship_manager_id": "rm011"}),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "relationship_manager_id": "rm011"}),
            Action(name="createSupportTicketForTransaction", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "transaction_id": "txn_7b8c9d0e-1f2a-3b4c-5d6e-7f8g9h0i1j2k", "reason": "Fraud Ring Takedown Documentation"}),
            Action(name="createSupportTicketForTransaction", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "transaction_id": "txn_7b8c9d0e-1f2a-3b4c-5d6e-7f8g9h0i1j2k", "reason": "Fraud Ring Takedown Documentation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_082",
        instruction="Facilitate Oliver Williams (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23) in a corporate divestiture process. Obtain his risk profile and total balance. As part of capital release, he needs to settle his 7,500,000 NGN business loan (loan_biz_009). Make a 7,500,000 NGN payment from his business savings (acc_sav_24002). Post loan repayment, close the savings account now at zero balance. Assess his scheduled payment (sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w1) and suspend it. Verify his 'Business' type beneficiaries. Review the overdraft limit on acc_chk_24001 and adjust it to 50,000 NGN. Update his employer information to 'A.A. Consulting'. Create a support ticket for account 'acc_chk_24001' to record the divestiture payoff with the reason 'Loan Payoff During Corporate Divestiture'. Provide a report on the status of the business loan and the updated overdraft limit.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_biz_009", "from_account_id": "acc_sav_24002", "amount": 7500000.00}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_sav_24002"}),
            Action(name="updateScheduledPaymentAmount", kwargs={"payment_id": "sp_f4n6a5m7-l2m1-n0o9-p8q7-r6s5t4u3v2w1", "amount": 0.00}), # Imitating a delay
            Action(name="fetchBeneficiariesByRelationship", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "relationship": "Business"}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_24001", "new_limit": 50000.00}),
            Action(name="addEmployerToCustomerProfile", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "employer": "A.A. Consulting"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23", "account_id": "acc_chk_24001", "reason": "Loan Payoff During Corporate Divestiture"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_083",
        instruction="Aid Mohammed Al-Masri (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17), who is facing challenges due to a natural disaster in Rio. Retrieve his risk profile and total balance. Promptly secure his checking account (acc_chk_18001) for protection. Review his current mortgage (loan_mort_006). To offer forbearance, extend the loan's termination date by three months to 2039-02-10. Analyze his recent transactions, identifying a transaction 'txn_6a7b8c9d-0e1f-2a3b-4c5d-6e7f8g9h0i1j' of -200.00 BRL suitable for a refund as assistance. Increase his overdraft limit to 20,000 BRL for emergency purposes. Obtain his contact options and set his preferred method to 'SMS' for urgent notifications. Investigate any 'Security' related support tickets. Once initial actions are done, create a new support ticket documenting all disaster relief efforts with the reason 'Natural Disaster Financial Relief Package Applied'. Report the rescheduled loan maturity date and the adjusted overdraft limit.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_chk_18001"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="adjustLoanPaymentDueDate", kwargs={"loan_id": "loan_mort_006", "new_due_date": "2039-02-10"}),
            Action(name="applyPartialRefundToTransaction", kwargs={"transaction_id": "txn_6a7b8c9d-0e1f-2a3b-4c5d-6e7f8g9h0i1j", "refund_amount": 200.00}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_18001", "new_limit": 20000.00}),
            Action(name="getCustomerContactMethods", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "new_channel": "SMS"}),
            Action(name="findRecentSupportTicketsByCategory", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "category": "Security"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "account_id": "acc_chk_18001", "reason": "Natural Disaster Financial Relief Package Applied"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_084",
        instruction="Oversee a Power of Attorney (POA) request for Chloe Dubois (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1), who is managing her mother Lakshmi Narayanan's (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24) affairs. Retrieve and review the risk profiles and total balances of both parties. Confirm Elena's beneficiary, 'Marie Dubois' (bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c), to whom Hans needs to make a payment. Initiate a 500 RON transfer from Elena's savings (acc_sav_25001) to the beneficiary. Hans also seeks to revise her scheduled payment (sp_a3o5b4n6-m1n0-o9p8-q7r6-s5t4u3v2w1x0) to 250 RON. Examine Elena's recent transactions. With the POA authority, change Elena's communication preference to 'Email'. Assign her to 'rm-ro-10', a specialist in POA matters. Conduct a KYC update for Elena. Report on Elena's new relationship manager and the updated scheduled payment.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c"}),
            Action(name="initiateFundTransferToBeneficiary", kwargs={"source_account_id": "acc_sav_25001", "beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c", "amount": 500.00}),
            Action(name="updateScheduledPaymentAmount", kwargs={"payment_id": "sp_a3o5b4n6-m1n0-o9p8-q7r6-s5t4u3v2w1x0", "amount": 250.00}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_sav_25001"]}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "new_channel": "Email"}),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "relationship_manager_id": "rm-ro-10"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_085",
        instruction="Initiate an inquiry into a notable crypto off-ramp for Elena Popescu (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19). Retrieve her risk profile. A recent 50,000,000 CLP deposit has been made to her checking account (acc_chk_20001); secure this account. Calculate her total deposits over the past 30 days (2023-09-28 to 2023-10-28) to determine irregularities. Review her latest transactions. Assess her existing loans. Due to this high-risk transaction, carry out an immediate KYC update. Retrieve her 'Personal' beneficiaries. Deactivate her account. Search for support tickets associated with 'Security' connected to her customer ID 'd4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19'. Create a high-priority support ticket for the AML investigation. Alter her communication preference to 'Mail' for formal communications. Provide a report detailing the customer's AML risk level, overall balance before account lock, and current account status.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_chk_20001"}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_chk_20001"], "start_date": "2023-09-28", "end_date": "2023-10-28"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_20001"]}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", }),
            Action(name="fetchBeneficiariesByRelationship", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "relationship": "Personal"}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_chk_20001"}),
            Action(name="findRecentSupportTicketsByCategory", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "category": "Security"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "account_id": "acc_chk_20001", "reason": "AML Investigation: Large Crypto Off-Ramp"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19", "new_channel": "Mail"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_086",
        instruction="In your role as an account manager, manage the request from Customer Sofia Andersson (f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9) to close their account because of relocation. Evaluate their risk profile and summarize the total balance across all accounts. Review their last 15 transactions for any outstanding obligations. Continue to deactivate account acc_chk_4001. Update their communication preference to 'Email' regarding 'Account closure documentation'. Record a support ticket concerning transaction 'txn_a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4-10' to note 'Account closure assistance'. Deliver a report on the customer's total balance, the number of transactions reviewed, and the account closure status.",
        actions=[
            Action(
                name="getCustomerRiskProfileSummary",
                kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}
            ),
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_4001"], "limit": 15}
            ),
            Action(
                name="deactivateAccountByRequest",
                kwargs={
                    "account_id": "acc_chk_4001"
                }
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "new_channel": "Email"
                }
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "transaction_id": "txn_a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4-10",
                    "reason": "Account closure assistance"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_087",
        instruction="Acting as a compliance officer, address a legal subpoena concerning Zoltan Nagy's records (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13). Firstly, obtain his risk profile and total balance. Collect all his accounts ('Checking' and 'Savings'). Assemble a list of the last 100 transactions across his accounts. Identify every active loan he holds. Secure details of all his 'Personal' beneficiaries. Acquire data on all scheduled payments. Discover all support tickets linked to his profile. Once all information is gathered, proceed to lock his checking (acc_chk_14001) and savings (acc_sav_14002) accounts. Then, deactivate the checking account as mandated by the legal order. Adjust his communication preference to 'Mail'. Document the entire process in a thorough support ticket, using loan 'loan_auto_007' for reference, to verify compliance with the subpoena for 'Full Account Data Compilation for Subpoena'. Provide a summary of the total number of transactions retrieved, the count of active loans, and the checking account's final status.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="getCustomerAccountsByType", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "account_type": "Checking"}),
            Action(name="getCustomerAccountsByType", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "account_type": "Savings"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_14001", "acc_sav_14002"], "limit": 100}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="fetchBeneficiariesByRelationship", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "relationship": "Personal"}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_14001"}),
            Action(name="findRecentSupportTicketsByCategory", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_chk_14001"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_sav_14002"}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_chk_14001"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "new_channel": "Mail"}),
            Action(name="createSupportTicketForTransaction", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13", "transaction_id": "loan_auto_007", "reason": "Full Account Data Compilation for Subpoena"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_088",
        instruction="To counter a phishing attack on Elena Popescu (a1b2c3d4-e5f6-7890-1234-567890abcdef), obtain her risk profile and total balance. Since the attacker conducted a fraudulent transaction ('txn_4e5f8h2j-6f8d-9e4h-4f7j-1h2f4g8i9e5e'), initiate a refund for the amount of 120. Additionally, the attacker set up a recurring payment (sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f); adjust it to 0 to cancel effectively. Continue to lock her checking (acc_chk_2001) and savings (acc_sav_2002) accounts. Check all her 'Family' beneficiaries for unauthorized entries. Verify all active loans, while her paid-off loan (loan_pers_003) remains unaffected. Insist on an immediate KYC refresh. Alter her communication preference to 'Phone'. Generate a support ticket to document the phishing remediation actions. Present the total refunded amount, the updated schedule payment amount, and the checking account's status.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="applyPartialRefundToTransaction", kwargs={"transaction_id": "txn_4e5f8h2j-6f8d-9e4h-4f7j-1h2f4g8i9e5e", "refund_amount": 120.00}),
            Action(name="updateScheduledPaymentAmount", kwargs={"payment_id": "sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f", "amount": 0.00}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_chk_2001"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_sav_2002"}),
            Action(name="fetchBeneficiariesByRelationship", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "relationship": "Family"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", }),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "new_channel": "Phone"}),
            Action(name="createSupportTicketForTransaction", kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", "transaction_id": "txn_4e5f8h2j-6f8d-9e4h-4f7j-1h2f4g8i9e5e", "reason": "Phishing Attack Remediation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_089",
        instruction="Functioning as a specialist for vulnerable clients, oversee the account of Lakshmi Narayanan (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24). Assess her risk profile and total balance. Examine her recent transactions for atypical spending behaviors. Look into her scheduled payments tied to her savings account (acc_sav_25001). Check all 'Personal' beneficiaries for any new additions. To ensure her asset protection, promptly lock her savings account. Change her communication preference to 'Mail' to maintain a legal paper trail. Assign her a new relationship manager 'rm-ro-11', a specialist skilled in handling vulnerable clients. Implement an immediate KYC refresh. Start a detailed support ticket for her savings account to log all protective actions, citing 'Protective measures for vulnerable client'. Provide a report on her total balance, her savings account status, and her new relationship manager.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_sav_25001"]}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_sav_25001"}),
            Action(name="fetchBeneficiariesByRelationship", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "relationship": "Personal"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_sav_25001"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "new_channel": "Mail"}),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "relationship_manager_id": "rm-ro-11"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", }),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24", "account_id": "acc_sav_25001", "reason": "Protective measures for vulnerable client"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_090",
        instruction="As you advise Zoltan Nagy (d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a) on tax optimization, obtain his risk profile and total balance. Determine his overall income by analyzing deposits into his checking (acc_chk_3001) and investment (acc_inv_3002) accounts over the previous year (2022-11-01 to 2023-10-31). Review his investment transactions for accuracy. To reduce taxable income, he intends to overpay 50,000 USD on his mortgage (loan_mort_001) using funds from his investment account. Verify his beneficiary 'Metropolis Power & Light' (bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a). Enforce his annual KYC refresh. Reassign his relationship manager to 'rm006', an expert in tax matters. Generate a support ticket related to the investment account to record the tax optimization strategy, noting 'Annual Tax Optimization Strategy Documentation'. Report his total deposits and the new mortgage balance.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_chk_3001", "acc_inv_3002"], "start_date": "2022-11-01", "end_date": "2023-10-31"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_inv_3002"]}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_mort_001", "from_account_id": "acc_inv_3002", "amount": 50000.00}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", }),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "relationship_manager_id": "rm006"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a", "account_id": "acc_inv_3002", "reason": "Annual Tax Optimization Strategy Documentation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_091",
        instruction="Handle a claim by Zoltan Nagy (customer ID: b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11) concerning transaction 'txn_c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18' for 1200.00 EUR on his loan account (acc_loan_12002), stating it was mistakenly classified as a capital expense. Start by retrieving his total balance and reviewing recent transactions on his checking account (acc_chk_12001) and loan account (acc_loan_12002). Transfer 600.00 EUR from his checking account (acc_chk_12001) to his loan account (acc_loan_12002) to partly resolve the disputed transaction, noting 'Dispute resolution partial payment' as the reason. Search for any existing support tickets under the 'Security' category. Open a new support ticket for the disputed transaction citing 'Mis-categorized capital expense' as the reason. Finally, change his communication preference to 'App'. Report back with updates on the balances of both checking and loan accounts.",
        actions=[
            Action(
                name="getCustomerTotalBalance",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}
            ),
            Action(
                name="listRecentTransactionsByCategory",
                kwargs={"account_ids": ["acc_chk_12001", "acc_loan_12002"]}
            ),
            Action(
                name="TransferFundsBetweenAccounts",
                kwargs={
                    "from_account_id": "acc_chk_12001",
                    "to_account_id": "acc_loan_12002",
                    "amount": 600.00,
                    "reason": "Dispute resolution partial payment"
                }
            ),
            Action(
                name="findRecentSupportTicketsByCategory",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "category": "Security"
                }
            ),
            Action(
                name="createSupportTicketForTransaction",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "transaction_id": "txn_c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "reason": "Mis-categorized capital expense"
                },
            ),
            Action(
                name="updateCustomerCommunicationPreference",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "new_channel": "App"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_092",
        instruction="Coordinate an audit on a high-risk business client, Zoltan Nagy (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11). Acquire his risk profile and overall balance. Access all his accounts ('Checking' and 'Loan'). List all transactions for his accounts over the past year capped at 1000. Review all current loans. Gather all his 'Business' and 'Personal' beneficiaries. Verify his main vendor, 'London Electricity Co.' (bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d). Calculate the total deposits made into his checking account (acc_chk_12001) over the last 6 months (2023-05-01 to 2023-10-31). As part of the audit, temporarily lock his checking account. Implement a KYC update. Reassign his relationship management to an audit specialist ('rm-ie-03'). Create a primary support ticket related to account 'acc_chk_12001' to document the start of the audit with the reason 'Comprehensive Audit Initiation'. Produce a report on the customer's credit score and the status of the checking account.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="getCustomerAccountsByType", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "account_type": "Checking"}),
            Action(name="getCustomerAccountsByType", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "account_type": "Loan"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_12001", "acc_loan_12002"], "limit": 1000}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}),
            Action(name="fetchBeneficiariesByRelationship", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "relationship": "Business"}),
            Action(name="fetchBeneficiariesByRelationship", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "relationship": "Personal"}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d"}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_chk_12001"], "start_date": "2023-05-01", "end_date": "2023-10-31"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_chk_12001"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", }),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "relationship_manager_id": "rm-ie-03"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11", "account_id": "acc_chk_12001", "reason": "Comprehensive Audit Initiation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_093",
        instruction="Deliver assistance to Chloe Dubois (d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1). Retrieve his risk profile and complete balance. Reallocate his finances by allocating transaction 'txn_e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14' to assign 1,000 EUR to savings (acc_sav_8002) and 1,000 EUR to checking (acc_chk_8001). Then, confirm beneficiary Kenji Tanaka (bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f) and send 1,000 EUR to him from the checking account. Inspect recent transactions in the checking account. Adjust its overdraft limit to 1,000 EUR. Obtain details of the scheduled payment 'sp_d9b3a2c1-b4c3-d2e1-f0a9-b8c7d6e5f4a3'. Finally, provide information on the updated savings balance, checking balance, and new overdraft limit.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}),
            Action(
                name="splitTransactionBetweenAccounts",
                kwargs={
                    "transaction_id": "txn_e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "splits": [
                        {"account_id": "acc_sav_8002", "amount": 1000.00},
                        {"account_id": "acc_chk_8001", "amount": 1000.00}
                    ]
                }
            ),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f"}),
            Action(
                name="initiateFundTransferToBeneficiary",
                kwargs={
                    "source_account_id": "acc_chk_8001",
                    "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f",
                    "amount": 1000.00
                }
            ),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_8001"]}),
            Action(
                name="reviewOverdraftActivityAndAdjustLimit",
                kwargs={"account_id": "acc_chk_8001", "new_limit": 1000.00}
            ),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_8001"}),
            Action(name="getAccountBalance", kwargs={"account_id": "acc_sav_8002"}),
            Action(name="getAccountBalance", kwargs={"account_id": "acc_chk_8001"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_094",
        instruction="Act as the trust officer for student Sofia Andersson (f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9), whose guardian is Kenji Tanaka. Obtain Maria's risk profile and overall balance. You must confirm the guardian's identity (Kenji Tanaka – c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) by verifying her risk profile. Evaluate Maria's student loan (loan_stud_004). Adjust her scheduled payment ('sp_e2g4b3f5-e9f8-g7h6-i5j4-k3l2m1n0o9p5') to 100 USD for her monthly tuition. Review the overdraft limit on her account (acc_chk_4001) and secure it to 0 for safety. Carry out a KYC update. Change her communication preference to 'Mail' for formal trust correspondence. Finally, create a support ticket associated with her checking account to describe the trust-related modifications with the reason 'Guardian Verified and Trust Account Adjustments'. Report the new scheduled payment amount and the overdraft limit.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}),
            Action(name="GetLoanDetails", kwargs={"loan_id": "loan_stud_004"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}),
            Action(name="updateScheduledPaymentAmount", kwargs={"payment_id": "sp_e2g4b3f5-e9f8-g7h6-i5j4-k3l2m1n0o9p5", "amount": 100.00}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_4001", "new_limit": 0.00}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9", }),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9", "new_channel": "Mail"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9", "account_id": "acc_chk_4001", "reason": "Guardian Verified and Trust Account Adjustments"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_095",
        instruction="Provide advice to Kenji Tanaka (c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e) following the receipt of a substantial inheritance now placed in her savings account. Retrieve her risk profile and total balance. Start by settling her auto loan (loan_auto_002) using her savings (acc_sav_1002). Confirm her beneficiary 'Elena Popescu' (bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d) and modify her scheduled payment 'sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d' to 500 USD for a new family trust. Elevate her relationship manager to 'rm005', an experienced wealth advisor. Perform a KYC update. Set up a new support ticket linked to acc_sav_1002 with the reason 'Inheritance consultation'. Present a status report on her auto loan and her updated relationship manager.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="GetLoanDetails", kwargs={"loan_id": "loan_auto_002"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_auto_002", "from_account_id": "acc_sav_1002", "amount": 15670.80}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d"}),
            Action(name="updateScheduledPaymentAmount", kwargs={"payment_id": "sp_b3a2c1d9-8e7f-6a5b-4c3d-2e1f0a9b8c7d", "amount": 500.00}),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "relationship_manager_id": "rm005"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "account_id": "acc_sav_1002", "reason": "Inheritance consultation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_096",
        instruction="Handle Oliver Williams (c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6) in her property purchase endeavor in Germany. Obtain her risk profile and complete balance overview. Confirm the international beneficiary 'Klaus Schmidt' (bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a). She requires transferring a down payment of 700,000 AED from her savings (acc_sav_7002). Once the transfer is complete, fetch her updated savings balance and quickly secure the account. Raise the overdraft limit on her checking account (acc_chk_7001) to 10,000 AED for legal fees. Review her ongoing mortgage (loan_mort_018) and adjust the maturity date to 2045-01-01 for financial restructuring purposes. Implement a KYC refresh due to the significant international transaction. Upon finishing the security verification, create a support ticket to document the property acquisition with 'International Property Purchase Documentation' as the rationale. Provide the new overdraft limit and mortgage maturity date details.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a"}),
            Action(name="initiateFundTransferToBeneficiary", kwargs={"source_account_id": "acc_sav_7002", "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a", "amount": 700000.00}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_sav_7002"}),
            Action(name="getAccountBalance", kwargs={"account_id": "acc_sav_7002"}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_7001", "new_limit": 10000.00}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}),
            Action(name="adjustLoanPaymentDueDate", kwargs={"loan_id": "loan_mort_018", "new_due_date": "2045-01-01"}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", }),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6", "account_id": "acc_sav_7002", "reason": "International Property Purchase Documentation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_097",
        instruction="Assist Gabriel Silva (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21) after his restaurant experienced a ransomware incident. Obtain his risk assessment and account total. The ransom is set at 2,000,000 HUF. Immediately limit his checking account (acc_chk_22001) access. For payment facilitation, temporarily elevate the overdraft limit to 2,500,000 HUF. Execute the transfer using 'Klaus Schmidt' - bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a - as a proxy for the attacker's account. Following the transfer, quickly initiate a KYC refresh. Assign him a cybercrime-focused relationship manager ('rm-hu-03'). Change his communication method to 'Phone'. Terminate the affected checking account. Produce a detailed support ticket regarding the ransomware event citing 'Ransomware Payment and Account Compromise Report' as the explanation. Provide an update on the checking account's closure and newly assigned relationship manager.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21"}),
            Action(name="lockAccountManually", kwargs={"account_id": "acc_chk_22001"}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_22001", "new_limit": 2500000.00}),
            Action(name="initiateFundTransferToBeneficiary", kwargs={"source_account_id": "acc_chk_22001", "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a", "amount": 2000000.00}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", }),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", "relationship_manager_id": "rm-hu-03"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", "new_channel": "Phone"}),
            Action(name="deactivateAccountByRequest", kwargs={"account_id": "acc_chk_22001"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21", "account_id": "acc_chk_22001", "reason": "Ransomware Payment and Account Compromise Report"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_098",
        instruction="Coordinate the financial affairs of sports professional Mohammed Al-Masri (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17). Retrieve her risk profile and overall balance. Her objective is to repay a student loan for Sofia Andersson (loan_stud_004) using her signing bonus, making a full payment of 25,000 USD (converted to BRL) from her checking account (acc_chk_18001). She is acquiring a vehicle, so review her auto loans. Inspect all imminent payments. Enhance her overdraft limit to 50,000 BRL. Proceed with a KYC update. Appoint her to an elite private banking adviser ('rm-br-02'). Modify her communication preference to 'App'. Draft a ticket to capture her updated financial strategy citing 'Athlete Financial Plan Implementation' as the justification. Report the student loan status and the new overdraft limit.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="makeLoanOverpayment", kwargs={"loan_id": "loan_stud_004", "from_account_id": "acc_chk_18001", "amount": 25000.00}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_18001"}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_18001", "new_limit": 50000.00}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", }),
            Action(name="reassignRelationshipManager", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "relationship_manager_id": "rm-br-02"}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "new_channel": "App"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17", "account_id": "acc_chk_18001", "reason": "Athlete Financial Plan Implementation"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_099",
        instruction="Coordinate the financial oversight of a foundation under Adetokunbo Adebayor's representation (f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3). Obtain his risk assessment and complete balance profile. Calculate all savings account (acc_sav_10002) deposits from the previous year (2022-11-01 to 2023-10-31) for donation analysis. Review the checking account (acc_chk_10001) payment schedule related to grant releases. Update the scheduled payment 'sp_c1d9b3a2-a5b4-c3d2-e1f0-a9b8c7d6e5f4' with a revised grant value of 300,000 JPY. Verify his primary beneficiary 'Yuki Tanaka' (bene_2b1c9d8e-7f6a-5b4c-3d2e-1f0a9b8c7d6e). Evaluate his current auto loan (loan_auto_011). Increase the checking account overdraft limit to 250,000 JPY for grant payment timing management. Conduct the foundation's yearly KYC refresh. Write a support ticket for the savings account to document the yearly financial assessment. Report donation totals, adjusted grant payment, and the enhanced overdraft limit.",
        actions=[
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="getTotalDepositsOverPeriod", kwargs={"account_ids": ["acc_sav_10002"], "start_date": "2022-11-01", "end_date": "2023-10-31"}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_10001"}),
            Action(name="updateScheduledPaymentAmount", kwargs={"payment_id": "sp_c1d9b3a2-a5b4-c3d2-e1f0-a9b8c7d6e5f4", "amount": 300000.00}),
            Action(name="verifyBeneficiaryExists", kwargs={"beneficiary_id": "bene_2b1c9d8e-7f6a-5b4c-3d2e-1f0a9b8c7d6e"}),
            Action(name="listActiveLoansWithBalances", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_10001", "new_limit": 250000.00}),
            Action(name="enforceKycRefreshForCustomer", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", }),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "account_id": "acc_sav_10002", "reason": "Annual Foundation Financial Review"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_100",
        instruction="Manage a corrective action for a false alert concerning Sofia Andersson (b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5) in her account (acc_chk_6001) having a mistaken ticket (tkt_f8c7d6e5-d6e5-f4a3-b2c1-d0e9f8g7h6i5). Obtain her total account balance and risk analysis. Review her latest transactions for authenticity verification. Examine the scheduled payments on this account. Retrieve any recent support tickets labeled under the 'Security' category to assess the alert's legitimacy. Oliver prefers to shift her communication to 'SMS'. To alleviate the issue, raise her overdraft limit to 200 GBP. Initiate a new support ticket for her checking account citing 'Resolution of false fraud alert' as the reason. Report the updated overdraft limit and Oliver's credit score.",
        actions=[
            Action(name="getCustomerTotalBalance", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}),
            Action(name="getCustomerRiskProfileSummary", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}),
            Action(name="listRecentTransactionsByCategory", kwargs={"account_ids": ["acc_chk_6001"]}),
            Action(name="getPaymentScheduleForAccount", kwargs={"account_id": "acc_chk_6001"}),
            Action(name="reviewOverdraftActivityAndAdjustLimit", kwargs={"account_id": "acc_chk_6001", "new_limit": 200.00}),
            Action(name="updateCustomerCommunicationPreference", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "new_channel": "SMS"}),
            Action(name="createSupportTicketForAccount", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "account_id": "acc_chk_6001", "reason": "Resolution of false fraud alert"}),
            Action(name="findRecentSupportTicketsByCategory", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5", "category": "Security"}),
            Action(name="getCustomerContactMethods", kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}),
        ],
        outputs=[]
    ),
]
