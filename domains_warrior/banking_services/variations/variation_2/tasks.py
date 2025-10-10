from domains.dto import Task, Action

TASKS = [


    Task(
        annotator=0,
        user_id="BANK_001",
        instruction=(
            "You are John Doe and you want to transfer $500 from your checking account to your savings account."
            "You need to verify your current balances before and after the transfer."
            "After the transfer, tell me what your new checking account balance is."
            "Lastly, Add Jane Smith as a new beneficiary with account number 9876543210, "
            "routing number 122000661, at City National Bank."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "John", "last_name": "Doe"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_1001"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_sav_1002"}
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_1001",
                    "to_account_id": "acc_sav_1002",
                    "amount": 500
                }
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_1001"}
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Jane Smith",
                    "account_number": "9876543210",
                    "routing_number": "122000661",
                    "bank_name": "City National Bank"
                }
            )
        ],
        outputs=["4730.50"]
    ),

    Task(
        annotator=0,
        user_id="BANK_002",
        instruction=(
            "You are Jane Smith and you want to apply for a $25000 personal loan for home renovation."
            "Your annual income is $75000. After applying, create a support ticket asking about the status."
            "Then check your credit utilization across all accounts. Report your overall credit utilization percentage."
            "Then add ATX, Inc. as a beneficiary with account number A23d45fg at Barclays."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Jane", "last_name": "Smith"}
            ),
            Action(
                name="apply_for_loan",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "loan_type": "Personal",
                    "requested_amount": 25000,
                    "purpose": "Home renovation",
                    "annual_income": 75000
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "subject": "Loan Application Status",
                    "description": "Loan Application Status"
                }
            ),
            Action(
                name="calculate_credit_utilization",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_name": "ATX, Inc.",
                    "account_number": "A23d45fg",
                    "bank_name": "Barclays"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_003",
        instruction=(
            "You are Hans Müller and you want to schedule a monthly payment of €1500 to Klaus Schmidt for your apartment rent."
            "First, find your checking account. Then, confirm Klaus Schmidt is your beneficiary and set up the monthly payment starting 2024-08-01."
            "Then check your current mortgage loan balance."
            "Finally add Soft Solutions, LLC. as a beneficiary with account number BGT543456 at Barclays."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Hans", "last_name": "Müller"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="get_customer_beneficiaries",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="setup_scheduled_payment",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "from_account_id": "acc_chk_8001",
                    "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a",
                    "amount": 1500,
                    "frequency": "Monthly",
                    "start_date": "2024-08-01"
                }
            ),
            Action(
                name="get_customer_loans",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "beneficiary_name": "Soft Solutions, LLC.",
                    "account_number": "BGT543456",
                    "bank_name": "Barclays"
                }
            ),
        ],
        outputs=["180000"]
    ),

    Task(
        annotator=0,
        user_id="BANK_004",
        instruction=(
            "You are Sofia Andersson and you want to pay your business partner after he made a sale. "
            "As a business owner, you need to check for large payments made from your checking account last month. "
            "Find your customer record. Retrieve your checking account. "
            "Also find John Doe's records. "
            "Search for all transactions over $500 in June 2025. "
            "Make a payment to your partner who is John Doe for $200 to his checking account. "
            "Open a support ticket asking about how you can get notified when beneficiary payments occur. "
            "Then add Patty Gordon as a beneficiary, account number VCG552431 at CitiBank. "
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Sofia", "last_name": "Andersson"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14"}
            ),
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "John", "last_name": "Doe"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 500
                }
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_15001",
                    "to_account_id": "acc_chk_1001",
                    "amount": 200
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "subject": "Notifications of beneficiary payments",
                    "description": "get notified when beneficiary payments occur"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "beneficiary_name": "Patty Gordon",
                    "account_number": "VCG552431",
                    "bank_name": "CitiBank"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_005",
        instruction=(
            "You are Adetokunbo Adebayor and you want to add a new beneficiary Jane Smith who is your insurance specialist."
            "First, find your customer record and retrieve your business checking account."
            "Search for all outgoing withdrawal transactions over $1,000 in July 2025."
            "Add Jane Smith as a new beneficiary with account number 9876543210, routing number 122000661, at City National Bank."
            "Then, generate an account statement for July 2025 and report the total number of outgoing transactions over $1,000."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Adetokunbo", "last_name": "Adebayor"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "min_amount": 1000,
                    "transaction_type": "Withdrawal"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "beneficiary_name": "Jane Smith",
                    "account_number": "9876543210",
                    "routing_number": "122000661",
                    "bank_name": "City National Bank"
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_006",
        instruction=(
            "You are Chloe Dubois and you want to remodel your kitchen and review your credit card transactions for the past month."
            "Your annual income is $45000. First, find your customer profile and retrieve your credit card account."
            "Find all charges that are expensive and over $200 in June 2025."
            "Apply for a personal loan in the amount of $10,000 to remodel your kitchen."
            "Then, generate a statement for your credit card for June 2025 and report the number of transactions above $200."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Chloe", "last_name": "Dubois"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_crd_9002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 200
                }
            ),
            Action(
                name="apply_for_loan",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "loan_type": "Personal",
                    "requested_amount": 10000,
                    "purpose": "Remodel kitchen",
                    "annual_income": 45000
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_crd_9002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_007",
        instruction=(
            "You are Aisha Khan and you want to get an overview of your recent checking account activity."
            "You also need to cancel your scheduled payment to Jane Smith since her service contract ended."
            "First, find your customer profile and retrieve your checking account."
            "Search for all incoming transactions over $300 in June 2025."
            "Cancel your scheduled payment with payment_id sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f."
            "Then, generate a statement for your checking account for June 2025 and report the number of incoming transactions above $300."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Aisha", "last_name": "Khan"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_13001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 300,
                    "transaction_type": "Incoming"
                }
            ),
            Action(
                name="cancel_scheduled_payment",
                kwargs={
                    "payment_id": "sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f"
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_chk_13001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_008",
        instruction=(
            "You are Hans Müller and you want to review your savings account activity for the past month."
            "First, find your customer profile and retrieve your savings account."
            "Search for any deposits over $1,000 in June 2025."
            "Cancel your scheduled payment with payment_id sp_f1h3a2g4-f8g7-h6i5-j4k3-l2m1n0o9p8q6."
            "You have concerns about how to do a scheduled payment cancellation and would like to get help."
            "Open a new support ticket asking for help with this payment cancellation."
            "Finally, generate a statement for your savings account for June 2025 and report the total number of deposits above $1,000."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Hans", "last_name": "Müller"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_sav_8002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 1000,
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="cancel_scheduled_payment",
                kwargs={
                    "payment_id": "sp_f1h3a2g4-f8g7-h6i5-j4k3-l2m1n0o9p8q6"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "subject": "Payment cancellation",
                    "description": "Payment cancellation"
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_sav_8002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_009",
        instruction=(
            "You are Elena Popescu and you want to review your savings account for recent interest earnings. "
            "Your annual income is $36000. First, find your customer profile and retrieve your savings account. "
            "Search for all interest-earned transactions in June 2025. "
            "Apply for a personal loan for $1,000 for your small business. "
            "Then, generate a statement for your savings account for June 2025 and report the total interest credited to your account. "
            "Finally add Soft Solutions, LLC. as a beneficiary with account number BGT543456 at Barclays."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Elena", "last_name": "Popescu"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Interest"
                }
            ),
            Action(
                name="apply_for_loan",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "loan_type": "Personal",
                    "requested_amount": 1000,
                    "purpose": "Small business loan",
                    "annual_income": 36000
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "beneficiary_name": "Soft Solutions, LLC.",
                    "account_number": "BGT543456",
                    "bank_name": "Barclays"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_010",
        instruction=(
            "You are Lakshmi Narayanan and you want to transfer $2000 from your checking account to your savings account."
            "You need to verify your current balances before and after the transfer."
            "After the transfer, tell me what your new checking account balance is."
            "Finally add Soft Solutions, LLC. as a beneficiary with account number BGT543456 at Barclays."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_5002"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_sav_5001"}
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_5002",
                    "to_account_id": "acc_sav_5001",
                    "amount": 2000
                }
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_5002"}
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "Soft Solutions, LLC.",
                    "account_number": "BGT543456",
                    "bank_name": "Barclays"
                }
            ),
        ],
        outputs=["48000"]
    ),

    Task(
        annotator=0,
        user_id="BANK_011",
        instruction=(
            "You are Lakshmi Narayanan and you want to review your checking account for high-value transactions."
            "Your annual income is $350000. First, find your customer profile and retrieve your checking account."
            "Search for all transactions over $5,000 in June 2025."
            "Apply for a student loan of $10,000 for your son's college tuition."
            "Then, generate a statement for your checking account for June 2025 and report the number of transactions above $5,000."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_5002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 5000
                }
            ),
            Action(
                name="apply_for_loan",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "loan_type": "Student",
                    "requested_amount": 10000,
                    "purpose": "Son's college tuition",
                    "annual_income": 350000
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_chk_5002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_012",
        instruction=(
            "You are Oliver Williams and want a summary of all incoming payments to your checking account last month."
            "First, find your customer profile. Retrieve your checking account."
            "Search for all incoming transactions in June 2025. Create a support ticket about your account review."
            "Then, generate a statement for your checking account for June 2025 and report the total number of incoming transactions.",
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Oliver", "last_name": "Williams"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_6001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "subject": "Account review",
                    "description": "Account review"
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_chk_6001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_013",
        instruction="You are Fatima Al-Fassi and want to review withdrawals from your savings account in June 2025. First, find your customer profile. Retrieve your savings account. Search for all withdrawal transactions in June 2025. Create a support ticket about your withdrawal review. Then, generate a statement for your savings account for June 2025 and report the total number of withdrawal transactions.",
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Fatima", "last_name": "Al-Fassi"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_sav_7002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "subject": "Withdrawal review",
                    "description": "Withdrawal review"
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_sav_7002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_014",
        instruction="You are Maria Garcia and want to check your checking account for any payments over $200 made in the month of June. First, find your customer profile. Retrieve your checking account. Search for all transactions over $200 in June 2025. Create a support ticket about your payment review. Then, generate a statement for your checking account for June 2025 and report the number of transactions above $200.",
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Maria", "last_name": "Garcia"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 200
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "subject": "Payment review",
                    "description": "Payment review"
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_015",
        instruction="You are Isabella Rossi and you want to check for purchases equal to or over $300 made on your checking account last month. First, find your customer profile. Retrieve your checking account. Search for all transactions over $300 in June 2025. Update your contact information with a new email address isabella.rossi.updated@email.com. Then, generate a statement for your checking account for June 2025 and report the number of purchases above $300.",
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Isabella", "last_name": "Rossi"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_11001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 300,
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "email": "isabella.rossi.updated@email.com"
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_chk_11001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_016",
        instruction="You are Liam O'Connor and want to review outgoing payments from your checking account for last month. First, find your customer profile. Retrieve your checking account. Search for all outgoing withdrawal transactions equal to or over $500 in June 2025. Update your contact information with a new phone number 555-123-9999. Then, generate a statement for your checking account for June 2025 and report the total number of outgoing transactions above $500.",
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Liam", "last_name": "O'Connor"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_12001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 500,
                    "transaction_type": "Withdrawal"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "phone": "555-123-9999"
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_chk_12001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_017",
        instruction="You are Kenji Tanaka and you want to summarize all deposits made to your savings account in June 2025. First, find your customer profile. Retrieve your savings account. Search for all deposit transactions in June 2025. Update your contact information with a new email address kenji.tanaka.updated@email.com. Then, generate a statement for your savings account for June 2025 and report the total number of deposits.",
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Kenji", "last_name": "Tanaka"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_sav_10002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "email": "kenji.tanaka.updated@email.com"
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_sav_10002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_018",
        instruction=(
            "You are Anja Novak and want to check your checking account activity for June 2025. "
            "First, find your customer profile and retrieve your checking account (acc_chk_19001)."
            "1. Search for all purchase transactions in June 2025 for your checking account.\n"
            "2. Calculate the total spent for the month."
            "3. Retrieve any scheduled payments from your checking account for June 2025."
            "4. Update your contact information with a new email address anja.novak.updated@email.com."
            "5. Generate a summary showing total purchases and scheduled payments for June."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Anja", "last_name": "Novak"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_19001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_19001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "source_account_id": "acc_chk_19001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "email": "anja.novak.updated@email.com"
                }
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_chk_19001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Summary for Anja Novak: total purchase amount and scheduled payments for acc_chk_19001 in June 2025."
        ]
    ),
    Task(
        annotator=0,
        user_id="BANK_019",
        instruction=(
            "You are Santiago Muñoz and want to review your checking account activity for June 2025."
            "First, find your customer profile and retrieve your checking account (acc_chk_20001)."
            "1. Search for all purchase transactions in June 2025 for your checking account."
            "2. Calculate the total spent for the month."
            "3. Retrieve any scheduled payments from your checking account for June 2025."
            "4. Update your contact information with a new phone number 555-789-1234."
            "5. Generate a summary showing total purchases and scheduled payments for June."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Santiago", "last_name": "Muñoz"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_20001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_20001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19",
                    "source_account_id": "acc_chk_20001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19",
                    "phone": "555-789-1234"
                }
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_chk_20001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Summary for Santiago Muñoz: total purchase amount and scheduled payments for acc_chk_20001 in June 2025."
        ]
    ),
    Task(
        annotator=0,
        user_id="BANK_020",
        instruction=(
            "You are Yara Haddad and want to review your checking account activity for June 2025."
            "First, find your customer profile and retrieve your checking account (acc_chk_21001)."
            "1. Search for all purchase transactions in June 2025 for your checking account."
            "2. Calculate the total spent for the month."
            "3. Retrieve any scheduled payments from your checking account for June 2025."
            "4. Update your contact information with a new email address yara.haddad.updated@email.com."
            "5. Generate a summary showing total purchases and scheduled payments for June."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Yara", "last_name": "Haddad"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_21001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_21001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "source_account_id": "acc_chk_21001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "email": "yara.haddad.updated@email.com"
                }
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_chk_21001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Summary for Yara Haddad: total purchase amount and scheduled payments for acc_chk_21001 in June 2025."
        ]
    ),


    Task(
        annotator=0,
        user_id="BANK_021",
        instruction=(
            "You are Fatima Al-Fassi and want to analyze account activity and handle transactions. "
            "Find your profile, search for purchase and deposit transactions for your checking account in July 2025, "
            "calculate combined spending, and then generate a detailed monthly report."
            "Then create a support ticket and get help setting up automated payments to your water provider."
            "Then add ATX, Inc. as a beneficiary with account number A23d45fg at Barclays."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Fatima", "last_name": "Al-Fassi"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="calculate_total_event_and_purchase_spending",
                kwargs={
                    "account_id": "acc_chk_7001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_chk_7001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            ),
            Action(
                name="generate_detailed_monthly_report",
                kwargs={
                    "account_id": "acc_chk_7001",
                    "month": "2025-07"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "subject": "setting up automated payments to your water provider",
                    "description": "setting up automated payments to your water provider"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "beneficiary_name": "ATX, Inc.",
                    "account_number": "A23d45fg",
                    "bank_name": "Barclays"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_022",
        instruction=(
            "You are Oliver Williams and want to check your financial activity for June 2025. "
            "First, find your customer profile. Retrieve your checking account (acc_chk_6001). "
            "1. Search for all purchase transactions in June 2025."
            "2. Calculate the total amount spent on these purchases."
            "3. Retrieve any scheduled payments from your checking account for June 2025."
            "4. Find any support tickets related to your checking account opened or resolved in June 2025."
            "5. Update your contact information with a new phone number 555-456-7890."
            "Finally, generate a summary that includes total purchases, scheduled payments, and support tickets involving your checking account for June."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Oliver", "last_name": "Williams"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_6001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_6001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "source_account_id": "acc_chk_6001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "account_id": "acc_chk_6001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "phone": "555-456-7890"
                }
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_chk_6001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Summary for Oliver Williams: total purchase amount, scheduled payments, and support tickets for acc_chk_6001 in June 2025."
        ]
    ),



    Task(
        annotator=0,
        user_id="BANK_023",
        instruction=(
            "You are John Doe and you want to transfer $1500 from your checking account to your savings account."
            "You need to verify your current balances before and after the transfer."
            "After the transfer, tell me what your new checking account balance is."
            "Finally add Soft Solutions, LLC. as a beneficiary with account number BGT543456 at Barclays."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "John", "last_name": "Doe"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_1001"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_sav_1002"}
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_1001",
                    "to_account_id": "acc_sav_1002",
                    "amount": 1500
                }
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_1001"}
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Soft Solutions, LLC.",
                    "account_number": "BGT543456",
                    "bank_name": "Barclays"
                }
            ),
        ],
        outputs=["3730.50"]
    ),


    Task(
        annotator=0,
        user_id="BANK_024",
        instruction=(
            "You are Chloe Dubois and want to review your financial activity for June 2025. "
            "First, find your customer profile and retrieve all your accounts."
            "For your checking account (acc_chk_9001):"
            "  1. Search for all purchase transactions in June 2025."
            "  2. Calculate the total amount spent on purchases for the month."
            "  3. Retrieve any scheduled payments made from your checking account in June 2025."
            "Additionally:"
            "  4. Find any support tickets related to your customer ID opened or resolved in June 2025."
            "  5. Update your contact information with a new phone number 555-321-6789."
            "Finally, generate a summary showing:"
            "  - Total purchases from checking"
            "  - Scheduled payments from checking"
            "  - Support tickets involving your customer ID in June"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Chloe", "last_name": "Dubois"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_9001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_9001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "source_account_id": "acc_chk_9001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="get_support_tickets_for_account",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "phone": "555-321-6789"
                }
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_chk_9001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Summary for Chloe Dubois: total purchase amount, scheduled payments, and support tickets for acc_chk_9001 in June 2025."
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_025",
        instruction=(
            "You are Lakshmi Narayanan and want to review your savings and checking activity for June 2025. "
            "First, find your customer profile and retrieve your savings account (acc_sav_5001) and checking account (acc_chk_5002).\n"
            "1. Search for all deposit transactions in June 2025 for your savings account.\n"
            "2. Calculate the total deposits for the month.\n"
            "3. Search for all purchase transactions in June 2025 for your checking account.\n"
            "4. Calculate the total amount spent on purchases from your checking account for the month.\n"
            "5. Retrieve any scheduled payments from your checking account for June 2025.\n"
            "6. Find any support tickets related to status changes for your savings or checking account opened or resolved in June 2025.\n"
            "7. Update your contact information with a new email address lakshmi.narayanan.newupdated@email.com.\n"
            "Finally, generate summaries showing:\n"
            " - Total deposits into savings\n"
            " - Total purchases from checking\n"
            " - Scheduled payments from checking\n"
            " - Support tickets for status changes in June"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_5002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_5002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "source_account_id": "acc_chk_5002",
                    "month": "2025-06"
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "account_ids": ["acc_sav_5001", "acc_chk_5002"],
                    "fields": ["status"],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "email": "lakshmi.narayanan.newupdated@email.com"
                }
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_chk_5002",
                    "month": "2025-06"
                }
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Reviewed total deposits, purchases, scheduled payments, and made a support tickets"
        ]
    ),


    Task(
        annotator=0,
        user_id="BANK_026",
        instruction=(
            "You are Liam O'Connor and want to review your business loan and checking account activity for June 2025."
            "First, find your customer profile and retrieve your business loan account (acc_loan_12002) and checking account (acc_chk_12001)."
            "1. Search for all loan payment transactions in June 2025 for your business loan account."
            "2. Calculate the total paid on the loan for the month."
            "3. Search for all purchase transactions in June 2025 for your checking account."
            "4. Calculate the total amount spent on purchases from your checking account for the month."
            "5. Retrieve any scheduled payments from your checking account for June 2025."
            "6. Find any support tickets related to your loan or checking account opened or resolved in June 2025."
            "7. Update your contact information with a new phone number 555-987-6543."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Liam", "last_name": "O'Connor"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_loan_12002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Payment"
                }
            ),
            Action(
                name="calculate_total_payments",
                kwargs={
                    "account_id": "acc_loan_12002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Payment"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_12001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_12001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "source_account_id": "acc_chk_12001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "account_ids": ["acc_loan_12002", "acc_chk_12001"],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "phone": "555-987-6543"
                }
            )
        ],
        outputs=[
            "Updated contact phone number for Liam O'Connor."
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_027",
        instruction=(
            "You are David Chen and want to review your investment and checking account activity for June 2025. "
            "Start by finding your customer profile and retrieving your investment account (acc_inv_3002) and checking account (acc_chk_3001)."
            "1. Search for all deposit and purchase transactions in June 2025 for your investment account."
            "2. Calculate the total amount deposited and total spent on purchases in your investment account for the month."
            "3. Search for all ATM withdrawal transactions in June 2025 for your checking account."
            "4. Calculate the total withdrawn from your checking account via ATM for the month."
            "5. Retrieve any scheduled payments from your checking account for June 2025."
            "6. Find any support tickets related to your accounts opened or resolved in June 2025."
            "7. Update your contact information with a new email address david.chen.updated@email.com."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "David", "last_name": "Chen"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_inv_3002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": ["Deposit", "Purchase"]
                }
            ),
            Action(
                name="calculate_total_deposits_and_purchases",
                kwargs={
                    "account_id": "acc_inv_3002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "ATM Withdrawal"
                }
            ),
            Action(
                name="calculate_total_atm_withdrawals",
                kwargs={
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "source_account_id": "acc_chk_3001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_ids": ["acc_inv_3002", "acc_chk_3001"],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "email": "david.chen.updated@email.com"
                }
            )
        ],
        outputs=[
            "0"
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_028",
        instruction=(
            "You are Adetokunbo Adebayor and want to analyze account activity and handle transactions. "
            "Find your profile, search for purchase and deposit transactions in July 2025, "
            "calculate combined spending, and generate detailed monthly report."
            "Then create a support ticket and get help setting up automated payments to your utility provider."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Adetokunbo", "last_name": "Adebayor"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}
            ),
            Action(
                name="calculate_total_event_and_purchase_spending",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_sav_24002",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            ),
            Action(
                name="generate_detailed_monthly_report",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "month": "2025-07"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "subject": "setting up automated payments to your utility provider",
                    "description": "setting up automated payments to your utility provider"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_029",
        instruction=(
            "You are Hans Müller and want to review your checking account activity for June 2025."
            "First, find your customer profile and retrieve your checking account (acc_chk_8001)."
            "1. Search for all purchase transactions in June 2025 for your checking account."
            "2. Calculate the total paid on purchases for the month."
            "3. Retrieve any scheduled payments from your checking account for June 2025."
            "4. Find any support tickets related to your checking account opened or resolved in June 2025."
            "5. Update your contact information with a new email address hans.muller.updated@email.com."
            "Finally, generate a summary showing:"
            "  - Total purchases from checking"
            "  - Scheduled payments from checking"
            "  - Support tickets for checking account in June"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Hans", "last_name": "Müller"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_8001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_8001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "source_account_id": "acc_chk_8001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "account_ids": ["acc_chk_8001"],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "email": "hans.muller.updated@email.com"
                }
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_chk_8001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Total purchases from checking: [amount]",
            "Scheduled payments from checking: [count/details]",
            "Support tickets for checking account in June: [count/details]"
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_030",
        instruction=(
            "You are Sofia Andersson and want a comprehensive review of your banking and financial activity for June 2025. "
            "Start by finding your customer profile and retrieving your checking account (acc_chk_15001)."
            "1. Search for all purchase transactions and concert/event ticket purchases in June 2025 for your checking account. "
            "2. Calculate the total amount spent on purchases and tickets for the month."
            "3. Search for all deposit transactions in June 2025 for your checking account."
            "4. Calculate total deposits for the month."
            "5. Retrieve any scheduled payments from your checking account for June 2025."
            "6. Identify any support tickets related to your checking account opened or resolved in June 2025. "
            "7. Retrieve your loan application history prior to July 2025 and their statuses."
            "8. Identify any changes to your account status, nickname, or beneficiary details via support tickets in June 2025. "
            "9. Search for any bill payment transactions in June 2025 for your checking account."
            "10. Calculate the total bill payments for the month."
            "11. Update your contact information with a new phone number 555-111-2222."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Sofia", "last_name": "Andersson"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": ["Purchase"],
                    "description_keywords": ["Concert", "Ticket", "Event"]
                }
            ),
            Action(
                name="calculate_total_event_and_purchase_spending",
                kwargs={
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": ["Deposit"]
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "source_account_id": "acc_chk_15001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="get_loan_applications_for_customer",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "before_date": "2025-07-01T00:00:00Z"
                }
            ),
            Action(
                name="get_account_changes_from_tickets",
                kwargs={
                    "account_id": "acc_chk_15001"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": ["Bill Payment"]
                }
            ),
            Action(
                name="calculate_total_bill_payments",
                kwargs={
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "phone": "555-111-2222"
                }
            )
        ],
        outputs=[
            "0"
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_031",
        instruction=(
            "You are Kenji Tanaka and want a comprehensive review of your banking activity for June 2025. "
            "Finding your customer profile."
            "Your checking account is acc_chk_10001 and savings account is acc_sav_10002."
            "1. Search for all purchase transactions in June 2025 for your checking account."
            "2. Calculate the total amount spent on purchases for the month."
            "3. Search for all deposit transactions in June 2025 for your savings account."
            "4. Calculate total deposits for the month."
            "5. Retrieve any scheduled payments from both accounts for June 2025."
            "6. Find any support tickets related to status changes or beneficiary management for either account opened or resolved in June 2025."
            "7. Retrieve your loan application history prior to July 2025 and their statuses."
            "8. Search for all bi-weekly or monthly scheduled payments from your savings account in June 2025."
            "9. Identify any changes to your account status or beneficiary details via support tickets in June 2025."
            "10. Update your contact information with a new phone number 555-444-7777."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Kenji", "last_name": "Tanaka"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_10001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_10001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_sav_10002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_sav_10002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "source_account_ids": ["acc_chk_10001", "acc_sav_10002"],
                    "month": "2025-06"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "source_account_id": "acc_sav_10002",
                    "month": "2025-06",
                    "frequency": ["Bi-Weekly", "Monthly"]
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "account_ids": ["acc_chk_10001", "acc_sav_10002"],
                    "fields": ["status", "beneficiaries"],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="get_loan_applications_for_customer",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "before_date": "2025-07-01T00:00:00Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "phone": "555-444-7777"
                }
            )
        ],
        outputs=[
            "0"
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_032",
        instruction=(
            "You are Mei Lin and want a comprehensive review of your checking account (acc_chk_23001) activity for June 2025."
            "First, locate your customer profile and account. Next:"
            "1. Search for all purchase transactions in June 2025 for acc_chk_23001. "
            "2. Calculate the total spent for purchases in June."
            "3. Search for all deposit transactions in June 2025 for acc_chk_23001."
            "4. Calculate the total deposited for the month."
            "5. Retrieve any scheduled payments from acc_chk_23001 for June 2025, and highlight any recurring (monthly or weekly) payments."
            "6. Find any support tickets related to payment issues or account inquiries for acc_chk_23001 opened or resolved in June 2025."
            "7. Update your contact information with a new email address mei.lin.updated@email.com."
            "8. Generate a summary showing: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for June."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Mei", "last_name": "Lin"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_23001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_23001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_23001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_chk_23001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "source_account_id": "acc_chk_23001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "source_account_id": "acc_chk_23001",
                    "month": "2025-06",
                    "frequency": ["Monthly", "Weekly"]
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "account_id": "acc_chk_23001",
                    "fields": ["payment issues", "account inquiries"],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "email": "mei.lin.updated@email.com"
                }
            ),
            Action(
                name="generate_detailed_monthly_summary",
                kwargs={
                    "account_id": "acc_chk_23001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Comprehensive summary for Mei Lin: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for acc_chk_23001 in June 2025."
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_033",
        instruction=(
            "You are Adetokunbo Adebayor and want a comprehensive review of your checking account (acc_chk_24001) activity for June 2025. "
            "First, locate your customer profile and account. Next: "
            "1. Search for all purchase transactions in June 2025 for acc_chk_24001."
            "2. Calculate the total spent for purchases in June."
            "3. Search for all deposit transactions in June 2025 for acc_chk_24001."
            "4. Calculate the total deposited for the month. "
            "5. Retrieve any scheduled payments from acc_chk_24001 for June 2025, and highlight any recurring (monthly or weekly) payments."
            "6. Find any support tickets related to payment issues or account inquiries for acc_chk_24001 opened or resolved in June 2025."
            "7. Update your contact information with a new phone number 555-888-9999."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Adetokunbo", "last_name": "Adebayor"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "source_account_id": "acc_chk_24001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "source_account_id": "acc_chk_24001",
                    "month": "2025-06",
                    "frequency": ["Monthly", "Weekly"]
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "fields": ["payment issues", "account inquiries"],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "phone": "555-888-9999"
                }
            )
        ],
        outputs=[
            "0"
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_034",
        instruction=(
            "You are Elena Popescu and want a comprehensive review of your savings account (acc_sav_25001) activity for June 2025."
            "First, locate your customer profile and account. Next:  "
            "1. Search for all withdrawal transactions in June 2025 for acc_sav_25001."
            "2. Calculate the total withdrawn for the month."
            "3. Search for all deposit transactions in June 2025 for acc_sav_25001."
            "4. Calculate the total deposited for the month."
            "5. Retrieve any scheduled payments from acc_sav_25001 for June 2025, and highlight any recurring (monthly or weekly) payments."
            "6. Find any support tickets related to withdrawal or deposit issues for acc_sav_25001 opened or resolved in June 2025."
            "7. Update your contact information with a new email address elena.popescu.updated@email.com. "
            "8. Generate a summary for your savings for June."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Elena", "last_name": "Popescu"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Withdrawal"
                }
            ),
            Action(
                name="calculate_total_withdrawal",
                kwargs={
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "source_account_id": "acc_sav_25001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "source_account_id": "acc_sav_25001",
                    "month": "2025-06",
                    "frequency": ["Monthly", "Weekly"]
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "account_id": "acc_sav_25001",
                    "fields": ["withdrawal issues", "deposit issues"],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "email": "elena.popescu.updated@email.com"
                }
            ),
            Action(
                name="generate_detailed_monthly_report",
                kwargs={
                    "account_id": "acc_sav_25001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Comprehensive summary for Elena Popescu: total withdrawals, total deposits, scheduled payments (with recurring details), and support tickets for acc_sav_25001 in June 2025."
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_035",
        instruction=(
            "You are Mohammed Al-Masri and want a comprehensive review of your checking account (acc_chk_26001) activity for June 2025. "
            "First, locate your customer profile and account. Next:"
            "1. Search for all purchase transactions in June 2025 for acc_chk_26001."
            "2. Calculate the total spent for purchases in June."
            "3. Search for all deposit transactions in June 2025 for acc_chk_26001."
            "4. Calculate the total deposited for the month."
            "5. Retrieve any scheduled payments from acc_chk_26001 for June 2025, and highlight any recurring (monthly or weekly) payments."
            "6. Find any support tickets related to payment issues or account inquiries for acc_chk_26001 opened or resolved in June 2025."
            "7. Update your contact information with a new phone number 555-777-3333."
            "8. Generate a summary showing: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for June."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Mohammed", "last_name": "Al-Masri"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_26001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_26001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_26001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_chk_26001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "source_account_id": "acc_chk_26001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "source_account_id": "acc_chk_26001",
                    "month": "2025-06",
                    "frequency": ["Monthly", "Weekly"]
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "account_id": "acc_chk_26001",
                    "fields": ["payment issues", "account inquiries"],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "phone": "555-777-3333"
                }
            ),
            Action(
                name="generate_detailed_monthly_summary",
                kwargs={
                    "account_id": "acc_chk_26001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Comprehensive summary for Mohammed Al-Masri: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for acc_chk_26001 in June 2025."
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_036",
        instruction=(
            "You are John Doe and want a comprehensive review of your checking account (acc_chk_1001) activity for June 2025. "
            "First, locate your customer profile and account. Next:"
            "1. Search for all purchase transactions in June 2025 for acc_chk_1001."
            "2. Calculate the total spent for purchases in June."
            "3. Search for all deposit transactions in June 2025 for acc_chk_1001."
            "4. Calculate the total deposited for the month."
            "5. Retrieve any scheduled payments from acc_chk_1001 for June 2025, and highlight any recurring (monthly or weekly) payments."
            "6. Find any support tickets related to payment issues or account inquiries for acc_chk_1001 opened or resolved in June 2025."
            "7. Update your contact information with a new email address john.doe.updated@email.com."
            "8. Generate a summary showing: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for June."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "John", "last_name": "Doe"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_chk_1001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_chk_1001",
                    "month": "2025-06",
                    "frequency": ["Monthly", "Weekly"]
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "fields": ["payment issues", "account inquiries"],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "email": "john.doe.updated@email.com"
                }
            ),
            Action(
                name="generate_detailed_monthly_summary",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Comprehensive summary for John Doe: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for acc_chk_1001 in June 2025."
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_037",
        instruction=(
            "You are Jane Smith and want a comprehensive review of your checking account (acc_chk_2001) activity for June 2025."
            "First, locate your customer profile and account. Next:"
            "1. Search for all purchase transactions in June 2025 for acc_chk_2001."
            "2. Calculate the total spent for purchases in June."
            "3. Search for all deposit transactions in June 2025 for acc_chk_2001."
            "4. Calculate the total deposited for the month."
            "5. Retrieve any scheduled payments from acc_chk_2001 for June 2025, and highlight any recurring (monthly or weekly) payments."
            "6. Find any support tickets related to payment issues or account inquiries for acc_chk_2001 opened or resolved in June 2025."
            "7. Update your contact information with a new phone number 555-222-3333."
            "8. Generate a summary showing: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for June."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Jane", "last_name": "Smith"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_2001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_2001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_2001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_chk_2001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "source_account_id": "acc_chk_2001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "source_account_id": "acc_chk_2001",
                    "month": "2025-06",
                    "frequency": ["Monthly", "Weekly"]
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "account_id": "acc_chk_2001",
                    "fields": ["payment issues", "account inquiries"],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "phone": "555-222-3333"
                }
            ),
            Action(
                name="generate_detailed_monthly_summary",
                kwargs={
                    "account_id": "acc_chk_2001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Comprehensive summary for Jane Smith: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for acc_chk_2001 in June 2025."
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_038",
        instruction=(
            "You are David Chen and want a comprehensive review of your checking account (acc_chk_3001) activity for June 2025."
            "First, locate your customer profile and account. Next:"
            "1. Search for all purchase transactions in June 2025 for acc_chk_3001."
            "2. Calculate the total spent for purchases in June."
            "3. Search for all deposit transactions in June 2025 for acc_chk_3001."
            "4. Calculate the total deposited for the month."
            "5. Retrieve any scheduled payments from acc_chk_3001 for June 2025, and highlight any recurring (monthly or weekly) payments."
            "6. Find any support tickets related to payment issues or account inquiries for acc_chk_3001 opened or resolved in June 2025."
            "7. Update your contact information with a new email address david.chen.updated2@email.com."
            "8. Generate a summary showing: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for June."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "David", "last_name": "Chen"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "source_account_id": "acc_chk_3001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "source_account_id": "acc_chk_3001",
                    "month": "2025-06",
                    "frequency": ["Monthly", "Weekly"]
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "account_id": "acc_chk_3001",
                    "fields": ["payment issues", "account inquiries"],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "email": "david.chen.updated2@email.com"
                }
            ),
            Action(
                name="generate_detailed_monthly_summary",
                kwargs={
                    "account_id": "acc_chk_3001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Comprehensive summary for David Chen: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for acc_chk_3001 in June 2025."
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_039",
        instruction=(
            "You are Maria Garcia and want a comprehensive review of your checking account (acc_chk_4001) activity for June 2025."
            "First, locate your customer profile and account. Next:"
            "1. Search for all purchase transactions in June 2025 for acc_chk_4001."
            "2. Calculate the total spent for purchases in June."
            "3. Search for all deposit transactions in June 2025 for acc_chk_4001."
            "4. Calculate the total deposited for the month."
            "5. Retrieve any scheduled payments from acc_chk_4001 for June 2025, and highlight any recurring (monthly or weekly) payments."
            "6. Find any support tickets related to payment issues or account inquiries for acc_chk_4001 opened or resolved in June 2025."
            "7. Update your contact information with a new phone number 555-333-4444."
            "8. Generate a summary showing: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for June."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Maria", "last_name": "Garcia"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "source_account_id": "acc_chk_4001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "source_account_id": "acc_chk_4001",
                    "month": "2025-06",
                    "frequency": ["Monthly", "Weekly"]
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "account_id": "acc_chk_4001",
                    "fields": ["payment issues", "account inquiries"],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "phone": "555-333-4444"
                }
            ),
            Action(
                name="generate_detailed_monthly_summary",
                kwargs={
                    "account_id": "acc_chk_4001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Comprehensive summary for Maria Garcia: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for acc_chk_4001 in June 2025."
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_040",
        instruction=(
            "You are Lakshmi Narayanan and want a comprehensive review of your savings account (acc_sav_5001) activity for June 2025."
            "First, locate your customer profile and account. Next:"
            "1. Search for all withdrawal transactions in June 2025 for acc_sav_5001."
            "2. Calculate the total withdrawn for the month."
            "3. Search for all deposit transactions in June 2025 for acc_sav_5001."
            "4. Calculate the total deposited for the month."
            "5. Retrieve any scheduled payments from acc_sav_5001 for June 2025, and highlight any recurring (monthly or weekly) payments."
            "6. Find any support tickets related to withdrawal, deposit, or payment issues for acc_sav_5001 opened or resolved in June 2025."
            "7. Update your contact information with a new email address lakshmi.narayanan.final@email.com."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Withdrawal"
                }
            ),
            Action(
                name="calculate_total_withdrawal",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "source_account_id": "acc_sav_5001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "source_account_id": "acc_sav_5001",
                    "month": "2025-06",
                    "frequency": ["Monthly", "Weekly"]
                }
            ),
            Action(
                name="get_support_tickets_for_accounts",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "fields": ["withdrawal issues", "deposit issues", "payment issues"],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "email": "lakshmi.narayanan.final@email.com"
                }
            )
        ],
        outputs=[
            "0"
        ]
    ),

    Task(
        annotator=0,
        user_id="BANK_041",
        instruction=(
            "You are John Doe and you want to transfer $2000 from your checking account to your savings account."
            "You need to verify your current balances before and after the transfer."
            "After the transfer, tell me what your new checking account balance is."
            "Finally add Soft Solutions, LLC. as a beneficiary with account number SFGTY65466 at CitiBank."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "John", "last_name": "Doe"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_1001"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_sav_1002"}
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_1001",
                    "to_account_id": "acc_sav_1002",
                    "amount": 2000
                }
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_1001"}
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Soft Solutions, LLC.",
                    "account_number": "SFGTY65466",
                    "bank_name": "CitiBank"
                }
            ),
        ],
        outputs=["3230.50"]
    ),


    Task(
        annotator=0,
        user_id="BANK_042",
        instruction=(
            "You are John Doe and you want to transfer $2500 from your checking account to your savings account."
            "You need to verify your current balances before and after the transfer."
            "After the transfer, tell me what your new checking account balance is."
            "Add Patty Gordon as a beneficiary with account number VCG552431 at CitiBank."
            "Update your contact email to john.newdoe@example.usa"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "John", "last_name": "Doe"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_1001"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_sav_1002"}
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_1001",
                    "to_account_id": "acc_sav_1002",
                    "amount": 2500
                }
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_1001"}
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Patty Gordon",
                    "account_number": "VCG552431",
                    "bank_name": "CitiBank"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "email": "john.newdoe@example.usa"
                }
            )
        ],
        outputs=["2730.50"]
    ),


    Task(
        annotator=0,
        user_id="BANK_043",
        instruction=(
            "You are Liam O'Connor and need to update your email address to liam.oconnornew@example.ie."
            "First find your customer profile, then update your contact information."
            "Add Patty Gordon as a beneficiary with account number VCG552431 at CitiBank."
            "Last, create a high-priority support ticket with subject 'Billing Inquiry' and description 'Question about monthly fees.' "
            "Do these actions today, since they are of high priority."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Liam", "last_name": "O'Connor"}
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "email": "liam.oconnornew@example.ie"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "beneficiary_name": "Patty Gordon",
                    "account_number": "VCG552431",
                    "bank_name": "CitiBank"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                }
            )
        ],
        outputs=["Contact information updated successfully"]
    ),


    Task(
        annotator=0,
        user_id="BANK_044",
        instruction=(
            "You are Alex Petrov and want to search for all purchase transactions over $100 from your checking account in July 2025."
            "You also are interested in a new car loan."
            "For the amount of $25,000 apply for a personal loan. Your annual income is $4,000,000."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Alex", "last_name": "Petrov"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_14001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "min_amount": 100.01,
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="apply_for_loan",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13",
                    "loan_type": "Personal",
                    "requested_amount": 25000,
                    "purpose": "New car",
                    "annual_income": 4000000
                }
            ),
        ],
        outputs=["0"]
    ),


    Task(
        annotator=0,
        user_id="BANK_045",
        instruction=(
            "You are Olivia Jones and want to transfer $500 from your checking account to your savings account. "
            "Find your customer profile, get your accounts, and perform the transfer."
            "Add Patty Gordon as a beneficiary with account number VCG552431 at CitiBank."
            "Last, create a high-priority support ticket with subject 'Billing Inquiry' and description 'Question about monthly fees'"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Olivia", "last_name": "Jones"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_17001",
                    "to_account_id": "acc_sav_17002",
                    "amount": 500
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "beneficiary_name": "Patty Gordon",
                    "account_number": "VCG552431",
                    "bank_name": "CitiBank"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                }
            )
        ],
        outputs=["Transfer completed successfully"]
    ),

    Task(
        annotator=0,
        user_id="BANK_046",
        instruction=(
            "You are Zoltan Nagy and want to create a support ticket about a billing issue. "
            "Find your customer profile and create a high-priority support ticket with subject 'Billing Inquiry' and description 'Question about monthly fees'."
            "Add Patty Gordon as a beneficiary with account number VCG552431 at CitiBank."
            "Then, due to suspected fraud, freeze your checking account, which is acc_chk_22001."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Zoltan", "last_name": "Nagy"}
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21",
                    "beneficiary_name": "Patty Gordon",
                    "account_number": "VCG552431",
                    "bank_name": "CitiBank"
                }
            ),
            Action(
                name="freeze_account",
                kwargs={
                    "account_id": "acc_chk_22001",
                    "reason": "Suspected fraud"
                }
            )
        ],
        outputs=["Support ticket created"]
    ),

    Task(
        annotator=0,
        user_id="BANK_047",
        instruction=(
            "You are Mei Lin and want to check your credit card utilization and apply for a loan to be able to invest in a company."
            "Find your customer profile and calculate your credit utilization across all credit cards."
            "Then apply for an investment loan in the amont of $1,000. Your annual income used for the loan is 0"
            "Finally, add Patty Gordon as a beneficiary with account number VCG552431 at CitiBank."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Mei", "last_name": "Lin"}
            ),
            Action(
                name="calculate_credit_utilization",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22"}
            ),
            Action(
                name="apply_for_loan",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "loan_type": "Investment",
                    "requested_amount": 1000,
                    "purpose": "To invest in a company",
                    "annual_income": 0
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "beneficiary_name": "Patty Gordon",
                    "account_number": "VCG552431",
                    "bank_name": "CitiBank"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_048",
        instruction=(
            "You are Aisha Khan and want to add a new beneficiary named Lisa Davis with account number 9876543210, "
            "routing number 111000025, at Bank of America."
            "Create a high-priority support ticket with subject 'Billing Inquiry' and description 'Question about monthly fees'."
            "Lastly, freeze your checking account due to possible hacking breaches. Your checking number is acc_chk_13001"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Aisha", "last_name": "Khan"}
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12",
                    "beneficiary_name": "Lisa Davis",
                    "account_number": "9876543210",
                    "routing_number": "111000025",
                    "bank_name": "Bank of America"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                }
            ),
            Action(
                name="freeze_account",
                kwargs={
                    "account_id": "acc_chk_13001",
                    "reason": "Possible hacking breeches"
                }
            )
        ],
        outputs=["Beneficiary added successfully"]
    ),


    Task(
        annotator=0,
        user_id="BANK_049",
        instruction=(
            "You are David Chen and want to see all your current loans."
            "You also are interested in taking out a new loan to start a business."
            "Find your customer profile and retrieve all loans associated with your account."
            "Then apply for a loan for $1,000,000. Your annual income is $250,000"
            "Add a new beneficiary Ben Harris, account number 34AD567, routing number 1243Df34, and banking at Bank of America. "
            "Create a support ticket asking for help setting up an apointment at a branch office with a retirement planner."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "David", "last_name": "Chen"}
            ),
            Action(
                name="get_customer_loans",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="apply_for_loan",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "loan_type": "Business",
                    "requested_amount": 1000000,
                    "purpose": "Start a business",
                    "annual_income": 250000
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Ben Harris",
                    "account_number": "34AD567",
                    "routing_number": "1243Df34",
                    "bank_name": "Bank of America"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "subject": "setting up an apointment at a branch office with a retirement planner",
                    "description": "setting up an apointment at a branch office with a retirement planner"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_050",
        instruction=(
            "You are Lakshmi Narayanan and want to generate financial reports for both accounts, and then seek help from a financial advisor. "
            "Find your profile, get accounts, and generate financial reports for checking and savings for June 2025."
            "Then create a new support ticket asking for a financial advisor to help with retirement planning."
            "Finally, freeze your accounts to protect against hackers."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="generate_financial_report",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_chk_5002",
                    "month": "2025-06"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "subject": "help with retirement planning",
                    "description": "help with retirement planning"
                }
            ),
            Action(
                name="freeze_account",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "reason": "Protect against hackers"
                }
            ),
            Action(
                name="freeze_account",
                kwargs={
                    "account_id": "acc_chk_5002",
                    "reason": "Protect against hackers"
                }
            )
        ],
        outputs=["0"]
    ),


    Task(
        annotator=0,
        user_id="BANK_051",
        instruction=(
            "You are Gabriel Silva and want to freeze your checking account due to suspected fraud. "
            "Find your customer profile, get your checking account. "
            "Add a new beneficiary named Lisa Davis with account number 9876543210, "
            "routing number 111000025, at Bank of America."
            "Create a high-priority support ticket with subject 'Billing Inquiry' and description 'Question about monthly fees.' "
            "Then freeze your checkings with reason 'Suspected fraud'."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Gabriel", "last_name": "Silva"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"}
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "beneficiary_name": "Lisa Davis",
                    "account_number": "9876543210",
                    "routing_number": "111000025",
                    "bank_name": "Bank of America"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                }
            ),
            Action(
                name="freeze_account",
                kwargs={
                    "account_id": "acc_chk_18001",
                    "reason": "Suspected fraud"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_052",
        instruction=(
            "You are John Doe and want to review your financial activity for June 2025. "
            "First, find your customer profile and retrieve all your accounts."
            "For your checking account (acc_chk_1001):"
            " 1. Search for all purchase transactions in June 2025."
            " 2. Calculate the total amount spent on purchases for the month."
            " 3. Retrieve any scheduled payments made from your checking account in June 2025."
            "Additionally:"
            " 4. Find any support tickets related to your customer ID opened or resolved in June 2025."
            " 5. Update your contact information with a new phone number 555-321-6789."
            "Finally, generate a summary showing:"
            " - Total purchases from checking"
            " - Scheduled payments from checking"
            " - Support tickets involving your customer ID in June"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "John", "last_name": "Doe"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_chk_1001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="get_support_tickets_for_account",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "phone": "555-321-6789"
                }
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "month": "2025-06"
                }
            )
        ],
        outputs=[
            "Summary for John Doe: total purchase amount, scheduled payments, and support tickets for acc_chk_1001 in June 2025."
        ]
    ),


    Task(
        annotator=0,
        user_id="BANK_053",
        instruction=(
            "You are Isabella Rossi and want to create a support ticket asking for help making a payment to a foreign country, "
            "which is required by your employer."
            "Update your contact information with a new phone number 555-111-2222."
            "Add Soft Solutions, LLC. as a beneficiary with account number SFGTY65466 at CitiBank. "
            "Before you finish, freeze your account checking account acc_chk_11001 to protect from hackers."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Isabella", "last_name": "Rossi"}
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "subject": "help making a payment to a foreign country",
                    "description": "help making a payment to a foreign country as required by my employer."
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "phone": "555-111-2222"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "beneficiary_name": "Soft Solutions, LLC.",
                    "account_number": "SFGTY65466",
                    "bank_name": "CitiBank"
                }
            ),
            Action(
                name="freeze_account",
                kwargs={
                    "account_id": "acc_chk_11001",
                    "reason": "Protect from hackers"
                }
            )
        ],
        outputs=["0"]
    ),


    Task(
        annotator=0,
        user_id="BANK_054",
        instruction=(
            "You are Noah Kim and want to get details about a specific transaction."
            "Find your customer profile and get details for transaction ID txn_4e5f6a7b-8c9d-0e1f-2a3b-4c5d6e7f8g9h."
            "Then add your customer support rep Lakshmi Narayanan as a beneficiary. Look her up by name."
            "She banks at India National Bank with the account number IN3456789012"
            "Create a high-priority support ticket with subject 'Billing Inquiry' and description 'Question about monthly fees'."
            "Before you go, update your customer contact phone number to 555-321-6789"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Noah", "last_name": "Kim"}
            ),
            Action(
                name="get_transaction_details",
                kwargs={"transaction_id": "txn_4e5f6a7b-8c9d-0e1f-2a3b-4c5d6e7f8g9h"}
            ),
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"}
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "beneficiary_name": "Lakshmi Narayanan",
                    "account_number": "IN3456789012",
                    "bank_name": "India National Bank"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "phone": "555-321-6789"
                }
            ),
        ],
        outputs=["0"]
    ),


    Task(
        annotator=0,
        user_id="BANK_055",
        instruction=(
            "You are Adetokunbo Adebayor and want to calculate your monthly spending for July 2025 on your checking account."
            "You also need to add Lakshmi Narayanan as your beneficiary."
            "She has an account number IN3456789012 and uses India National Bank"
            "Create a high-priority support ticket with subject 'Billing Inquiry' and description 'Question about monthly fees'."
            "Before you go, update your customer contact ohone number to 555-321-6789"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Adetokunbo", "last_name": "Adebayor"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}
            ),
            Action(
                name="calculate_monthly_spending",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "month": 7,
                    "year": 2025
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "beneficiary_name": "Lakshmi Narayanan",
                    "account_number": "IN3456789012",
                    "bank_name": "India National Bank"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "phone": "555-321-6789"
                }
            ),
        ],
        outputs=["0"]
    ),


    Task(
        annotator=0,
        user_id="BANK_056",
        instruction=(
            "You are Anja Novak and want to update your phone number to 555-987-6543. "
            "Find your customer profile and update your contact information."
            "You are interested in getting a loan for personal spending."
            "Apply for a new loan for $10,000. Your annual income is $40,000"
            "Generate a monthly report for your checkings account acc_chk_19001 for July"
            "Create a high-priority support ticket with subject 'Loan Inquiry' and description 'Question about a loan'."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Anja", "last_name": "Novak"}
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "phone": "555-987-6543"
                }
            ),
            Action(
                name="apply_for_loan",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "loan_type": "Personal",
                    "requested_amount": 10000,
                    "purpose": "Personal spending",
                    "annual_income": 40000
                }
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_chk_19001",
                    "month": "2025-07"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "subject": "Loan Inquiry",
                    "description": "Question about a loan",
                    "priority": "High"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_057",
        instruction=(
            "You are Zoltan Nagy and want to search for customers with the email dupont.fr domains."
            "You also need to add Marie Dubois as your beneficiary. Her IBAN is FR7630006000011234567890189, "
            "and her bank is BNP Paribas"
            "Create a high-priority support ticket with subject 'Billing Inquiry' and description 'Question about monthly fees.' "
            "Update your phone contact to 415-667-9999 and your email to newegg@aol.com"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Zoltan", "last_name": "Nagy"}
            ),
            Action(
                name="search_customers_by_email",
                kwargs={"email_domain": "dupont.fr"}
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21",
                    "beneficiary_name": "Marie Dubois",
                    "iban": "FR7630006000011234567890189",
                    "bank_name": "BNP Paribas"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21",
                    "phone": "415-667-9999",
                    "email": "newegg@aol.com"
                }
            ),
        ],
        outputs=["0"]
    ),


    Task(
        annotator=0,
        user_id="BANK_058",
        instruction=(
            "You are Mei Lin and want to see your support tickets. "
            "Find your customer profile and retrieve all your support tickets."
            "Then add London Electricity Co. as your beneficiary. The account number is 12345678 and the bank is Barclays"
            "Create a support ticket asking if you can track beneficiary activity on the mobile app. "
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Mei", "last_name": "Lin"}
            ),
            Action(
                name="get_customer_support_tickets",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22"}
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "beneficiary_name": "London Electricity Co.",
                    "account_number": "12345678",
                    "bank_name": "Barclays"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "subject": "tracking beneficiary activity on the mobile app",
                    "description": "asking how to track beneficiary activity on the mobile app"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_059",
        instruction=(
            "You are Adetokunbo Adebayor and want to calculate total deposits to your savings account in June 2025. "
            "Then create a support ticket for bugs in the mobile app. "
            "Then add London Electricity Co. as your beneficiary. The account number is 12345678 and the bank is Barclays. "
            "Transfer $50 from your checkings to savings account. "
            "Then add Nana Piccao as another new beneficiary with account number 46746fd45 and at the Bank of Egypt."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Adetokunbo", "last_name": "Adebayor"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_sav_24002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "subject": "Bugs In Mobile App",
                    "description": "Bugs In Mobile App"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "beneficiary_name": "London Electricity Co.",
                    "account_number": "12345678",
                    "bank_name": "Barclays"
                }
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_24001",
                    "to_account_id": "acc_sav_24002",
                    "amount": 50
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "beneficiary_name": "Nana Piccao",
                    "account_number": "46746fd45",
                    "bank_name": "Bank of Egypt"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_060",
        instruction=(
            "You are Elena Popescu and want to calculate total withdrawals from your savings account in July 2025. "
            "Then create a support ticket to get help understanding loan applications. "
            "Add Nana Piccao as a new beneficiary with account number 46746fd45 and at the Bank of Egypt. "
            "Update your phone number to 415-445-1212 and email to fastapi@aol.com."
            "Finally generate an account statement for savings in June."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Elena", "last_name": "Popescu"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"}
            ),
            Action(
                name="calculate_total_withdrawal",
                kwargs={
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "subject": "Understanding loan applications",
                    "description": "Needs help understanding loan applications"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "beneficiary_name": "Nana Piccao",
                    "account_number": "46746fd45",
                    "bank_name": "Bank of Egypt"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "phone": "415-445-1212",
                    "email": "fastapi@aol.com"
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_061",
        instruction=(
            "You are Mohammed Al-Masri and want to generate an account statement for your checking account for June 2025. "
            "Then add ATX, Inc. as a beneficiary with account number A23d45fg at Barclays. "
            "Open a customer support ticket asking for help adding a backup email to your account. "
            "Change your phone number to 415-1234-8888 and change your email to slowapi@aol.com."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Mohammed", "last_name": "Al-Masri"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"}
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_chk_26001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "beneficiary_name": "ATX, Inc.",
                    "account_number": "A23d45fg",
                    "bank_name": "Barclays"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "subject": "Help adding a backup email",
                    "description": "Help adding a backup email"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "phone": "415-1234-8888",
                    "email": "slowapi@aol.com"
                }
            ),
        ],
        outputs=["0"]
    ),


    Task(
        annotator=0,
        user_id="BANK_062",
        instruction=(
            "You are John Doe and want to see withdrawal transactions from your checking account and calculate the total amount for July 2025."
            "Then open a customer support ticket asking for help adding a backup email to your account."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "John", "last_name": "Doe"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "transaction_type": "Withdrawal"
                }
            ),
            Action(
                name="calculate_total_withdrawal",
                kwargs={
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "subject": "Help adding a backup email",
                    "description": "Help adding a backup email"
                }
            ),
        ],
        outputs=["0"]
    ),


    Task(
        annotator=0,
        user_id="BANK_063",
        instruction=(
            "You are Jane Smith and want to search for deposit transactions in your savings account for June 2025 and calculate the total."
            "Get help from the customer support for setting up automated notifications on your mobile app."
            "Then transfer $500 from your checking account into your savings"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Jane", "last_name": "Smith"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_sav_2002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_sav_2002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "subject": "setting up automated notifications",
                    "description": "setting up automated notifications"
                }
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_2001",
                    "to_account_id": "acc_sav_2002",
                    "amount": 500
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_064",
        instruction=(
            "You are David Chen and want to update your email to david.chen.updated@email.com, "
            "and also check your checking account balance."
            "Transfer $1,000 from your checkings to investment account."
            "Add Anna O'Connor as a beneficiary with account number 6754FG6894 at the Bank of Dublin"
            "Finally, add John Doe as a beneficiary with account number As234fdg and routing number 126579823."
            "His bank is City National Bank"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "David", "last_name": "Chen"}
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "email": "david.chen.updated@email.com"
                }
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_3001"}
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_3001",
                    "to_account_id": "acc_inv_3002",
                    "amount": 1000
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Anna O'Connor",
                    "account_number": "6754FG6894",
                    "bank_name": "Bank of Dublin"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "John Doe",
                    "account_number": "As234fdg",
                    "routing_number": "126579823",
                    "bank_name": "City National Bank"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_065",
        instruction=(
            "You are Maria Garcia and want to see purchase transactions over $250 from your checking account in July 2025."
            "Then freeze your account as a way to protect against suspected hackers."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Maria", "last_name": "Garcia"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "min_amount": 250.01,
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="freeze_account",
                kwargs={
                    "account_id": "acc_chk_4001",
                    "reason": "Suspected hackers"
                }
            )
        ],
        outputs=["0"]
    ),


    Task(
        annotator=0,
        user_id="BANK_066",
        instruction=(
            "You are Lakshmi Narayanan and want to generate a monthly account summary for your savings account for July 2025."
            "You moved for a job and need to update your phone contact to 415-921-6543"
            "Then add Lisa Davis as a new beneficiary with account number 9876543210, routing number 111000025, "
            "who banks with Bank of America. "
            "Also add BMX Trips, LLC. as a beneficiary with account number CDF456378 and banking with Barclays."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "month": "2025-07"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "phone": "415-921-6543"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "Lisa Davis",
                    "account_number": "9876543210",
                    "routing_number": "111000025",
                    "bank_name": "Bank of America"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "BMX Trips, LLC.",
                    "account_number": "CDF456378",
                    "bank_name": "Barclays"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_067",
        instruction=(
            "You are Oliver Williams and want to create a support ticket about account access issues. "
            "Create a medium priority ticket with subject 'Account Access' and description 'Unable to login to online banking'."
            "Add John Doe as a beneficiary with account number As234fdg and routing number 126579823."
            "His bank is City National Bank"
            "Update your phone number to 552-345-6111"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Oliver", "last_name": "Williams"}
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "subject": "Account Access",
                    "description": "Unable to login to online banking",
                    "priority": "Medium"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_name": "John Doe",
                    "account_number": "As234fdg",
                    "routing_number": "126579823",
                    "bank_name": "City National Bank"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "phone": "552-345-6111"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_068",
        instruction=(
            "You are Fatima Al-Fassi and want to calculate total ATM withdrawals from your checking account in June 2025."
            "Then you need to transfer $200 from your savings into your checking."
            "Afterwars calculate your checking balance."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Fatima", "last_name": "Al-Fassi"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="calculate_total_atm_withdrawals",
                kwargs={
                    "account_id": "acc_chk_7001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_sav_7002",
                    "to_account_id": "acc_chk_7001",
                    "amount": 200
                }
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_7001"}
            )
        ],
        outputs=["150200"]
    ),


    Task(
        annotator=0,
        user_id="BANK_069",
        instruction=(
            "You are Hans Müller and want to check for any scheduled payments from your checking account for August 2025. "
            "Then you need to transfer $1000 from your savings acc_sav_8002 into your checking acc_chk_8001. "
            "Then add Lisa Davis as a new beneficiary with account number 9876543210, routing number 111000025, "
            "and with Bank of America. "
            "Apply for a $10,000 personal loan to help pay for your car mechanic hobbies; your annual income is $95,000."
            "Before you are done, calculate your checking balance."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Hans", "last_name": "Müller"}
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "source_account_id": "acc_chk_8001",
                    "month": "2025-08"
                }
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_sav_8002",
                    "to_account_id": "acc_chk_8001",
                    "amount": 1000
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "beneficiary_name": "Lisa Davis",
                    "account_number": "9876543210",
                    "routing_number": "111000025",
                    "bank_name": "Bank of America"
                }
            ),
            Action(
                name="apply_for_loan",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "loan_type": "Personal",
                    "requested_amount": 10000,
                    "purpose": "Car mechanic hobbies",
                    "annual_income": 95000
                }
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_8001"}
            )
        ],
        outputs=[8800.5]
    ),

    Task(
        annotator=0,
        user_id="BANK_070",
        instruction=(
            "You are Chloe Dubois and want to search for all transactions from your checking account between June 1-15, 2025."
            "Then you need to pay your friend Kenji Tanaka $150 as a gift from your checking."
            "Kenji's account number is acc_chk_10001."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Chloe", "last_name": "Dubois"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_9001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-15T23:59:59Z"
                }
            ),
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Kenji", "last_name": "Tanaka"}
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_9001",
                    "to_account_id": "acc_chk_10001",
                    "amount": 150
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_071",
        instruction=(
            "You are Kenji Tanaka and want to review your checking account activity for July 2025. "
            "Find your customer profile, retrieve your checking account, search for all purchase transactions in July 2025, "
            "and calculate the total amount spent on purchases."
            "Finally you need to send $50 from your checkings to your savings. "
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Kenji", "last_name": "Tanaka"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_10001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_10001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_10001",
                    "to_account_id": "acc_sav_10002",
                    "amount": 50
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_072",
        instruction=(
            "You are Isabella Rossi and want to transfer money and update your contact info. "
            "Find your customer profile, transfer $150 from checking to your business associate Liam O'Connor's checking acc_chk_12001, "
            "and update your email to isabella.rossi.new@email.com. "
            "Add BMX Trips, LLC. as a beneficiary with account number CDF456378 and banking with Barclays. "
            "Then create a support ticket for your checking account review."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Isabella", "last_name": "Rossi"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10"}
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_11001",
                    "to_account_id": "acc_chk_12001",
                    "amount": 150
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "email": "isabella.rossi.new@email.com"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "beneficiary_name": "BMX Trips, LLC.",
                    "account_number": "CDF456378",
                    "bank_name": "Barclays"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "subject": "Checking account review",
                    "description": "Checking account review"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_073",
        instruction=(
            "You are Liam O'Connor and want to review deposits to your checking account. "
            "Find your profile, get your checking account, search for deposits in June 2025, "
            "calculate total deposits, and generate a monthly summary."
            "Then add your sister Anna O'Connor as a beneficiary with account number 6754FG6894 at the Bank of Dublin"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Liam", "last_name": "O'Connor"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_12001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_chk_12001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_chk_12001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "beneficiary_name": "Anna O'Connor",
                    "account_number": "6754FG6894",
                    "bank_name": "Bank of Dublin"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_074",
        instruction="You are Santiago Muñoz and want a summary of all incoming payments to your checking account last month. First, find your customer profile. Retrieve your checking account. Search for all incoming transactions in June 2025. Create a support ticket about your account review. Then, generate a statement for your checking account for June 2025 and report the total number of incoming transactions.",
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Santiago", "last_name": "Muñoz"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_20001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19",
                    "subject": "Account review",
                    "description": "Account review"
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_chk_20001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_075",
        instruction=(
            "You are Alex Petrov and want to review your loan status and make a payment. "
            "Find your profile, get your loans, and make a $300 loan payment from your checking account."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Alex", "last_name": "Petrov"}
            ),
            Action(
                name="get_customer_loans",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}
            ),
            Action(
                name="process_loan_payment",
                kwargs={
                    "loan_id": "loan_auto_007",
                    "payment_amount": 300,
                    "from_account_id": "acc_chk_14001"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_076",
        instruction=(
            "You are Sofia Andersson and want to check support tickets and create a new one. "
            "Find your profile, check existing support tickets, then create a new ticket about card replacement "
            "with high priority and description 'Lost credit card, need replacement'. "
            "Add Jane Smith as a new beneficiary with account number 9876543210, "
            "routing number 122000661, at City National Bank. "
            "Finally, update your email contact to fasttrack@email.com."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Sofia", "last_name": "Andersson"}
            ),
            Action(
                name="get_customer_support_tickets",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14"}
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "subject": "Card Replacement",
                    "description": "Lost credit card, need replacement",
                    "priority": "High"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "beneficiary_name": "Jane Smith",
                    "account_number": "9876543210",
                    "routing_number": "122000661",
                    "bank_name": "City National Bank"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "email": "fasttrack@email.com"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_077",
        instruction=(
            "You are Noah Kim and want to calculate spending and check credit utilization. "
            "Find your profile, calculate monthly spending for July 2025 on checking account, "
            "and check your credit card utilization."
            "Then update your account email to new.noah.kim@hotmail.com."
            "Add Jane Smith as a new beneficiary with account number 9876543210, "
            "routing number 122000661, at City National Bank. "
            "Then add BMX Trips, LLC. as a beneficiary with account number CDF456378 and banking with Barclays. "
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Noah", "last_name": "Kim"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15"}
            ),
            Action(
                name="calculate_monthly_spending",
                kwargs={
                    "account_id": "acc_chk_16001",
                    "month": 7,
                    "year": 2025
                }
            ),
            Action(
                name="calculate_credit_utilization",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15"}
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "email": "new.noah.kim@hotmail.com"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "beneficiary_name": "Jane Smith",
                    "account_number": "9876543210",
                    "routing_number": "122000661",
                    "bank_name": "City National Bank"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "beneficiary_name": "BMX Trips, LLC.",
                    "account_number": "CDF456378",
                    "bank_name": "Barclays"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_078",
        instruction=(
            "You are Olivia Jones and want to generate financial reports for both accounts, and then seek help from a financial advisor. "
            "Find your profile, get accounts, and generate financial reports for checking and savings for June 2025."
            "Then create a new support ticket asking for a financial advisor to help with retirement planning."
            "Finally, freeze your accounts to protect against hackers."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Olivia", "last_name": "Jones"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"}
            ),
            Action(
                name="generate_financial_report",
                kwargs={
                    "account_id": "acc_chk_17001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_sav_17002",
                    "month": "2025-06"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "subject": "help with retirement planning",
                    "description": "help with retirement planning"
                }
            ),
            Action(
                name="freeze_account",
                kwargs={
                    "account_id": "acc_chk_17001",
                    "reason": "Protect against hackers"
                }
            ),
            Action(
                name="freeze_account",
                kwargs={
                    "account_id": "acc_sav_17002",
                    "reason": "Protect against hackers"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_079",
        instruction=(
            "You are Gabriel Silva and want to review scheduled payments from your checking and update contact info."
            "The account in question is acc_chk_18001."
            "Find your profile, check scheduled payments for July 2025 from checking account, "
            "and update phone number to 555-234-5678. "
            "Add Jane Smith as a new beneficiary with account number 9876543210, "
            "routing number 122000661, at City National Bank. "
            "Then add BMX Trips, LLC. as a beneficiary with account number CDF456378 and banking with Barclays."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Gabriel", "last_name": "Silva"}
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "source_account_id": "acc_chk_18001",
                    "month": "2025-07"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "phone": "555-234-5678"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "beneficiary_name": "Jane Smith",
                    "account_number": "9876543210",
                    "routing_number": "122000661",
                    "bank_name": "City National Bank"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "beneficiary_name": "BMX Trips, LLC.",
                    "account_number": "CDF456378",
                    "bank_name": "Barclays"
                }
            ),
        ],
        outputs=["Scheduled payments reviewed, contact updated"]
    ),


    Task(
        annotator=0,
        user_id="BANK_080",
        instruction=(
            "You are Jane Smith, find your profile, search for deposits over $1000 in savings for June 2025, "
            "then transfer $100 from your checking into your savings."
            "Make a support ticket for setting up automated notifications on your mobile app."
            "Then get a financial report for your checkings account in June"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Jane", "last_name": "Smith"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_sav_2002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 1000.01,
                    "transaction_type": "Deposit"
                }
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_2001",
                    "to_account_id": "acc_sav_2002",
                    "amount": 100
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "subject": "setting up automated notifications",
                    "description": "setting up automated notifications"
                }
            ),
            Action(
                name="generate_financial_report",
                kwargs={
                    "account_id": "acc_chk_2001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_081",
        instruction=(
            "You are Santiago Muñoz and want to review account activity and create support ticket. "
            "Find your profile, get account transactions for the last 10 transactions, calculate account balance, "
            "and create a support ticket today about transaction fees."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Santiago", "last_name": "Muñoz"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}
            ),
            Action(
                name="get_account_transactions",
                kwargs={
                    "account_id": "acc_chk_20001",
                    "limit": 10
                }
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_20001"}
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19",
                    "subject": "Transaction Fees",
                    "description": "Questions about recent transaction fees"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_082",
        instruction=(
            "You are Yara Haddad and want to handle beneficiaries and payments tasks."
            "Find your profile, get all beneficiaries, validate routing number 111000025, "
            "and check scheduled payments for August 2025 from your checking account acc_chk_21001."
            "Then create a support ticket to receive help adding beneficiaries and what required info is needed to add them"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Yara", "last_name": "Haddad"}
            ),
            Action(
                name="get_customer_beneficiaries",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20"}
            ),
            Action(
                name="validate_routing_number",
                kwargs={"routing_number": "111000025"}
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "source_account_id": "acc_chk_21001",
                    "month": "2025-08"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "subject": "help adding beneficiaries and info required",
                    "description": "help adding beneficiaries and info required"
                }
            ),
        ],
        outputs=["0"]
    ),


    Task(
        annotator=0,
        user_id="BANK_083",
        instruction=(
            "You are Adetokunbo Adebayor and want to review spending and deposits. "
            "Find your profile, calculate total purchases from checking in July 2025, "
            "calculate total deposits to savings in July 2025, and generate account statement for checking."
            "Then transfer $1000 from your checkings into your savings"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Adetokunbo", "last_name": "Adebayor"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_sav_24002",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_24001",
                    "to_account_id": "acc_sav_24002",
                    "amount": 1000
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_084",
        instruction=(
            "You are Jane Smith and want to manage loans and transfers. "
            "Find your profile, get customer loans, transfer $400 from checking to savings as part of your regular savings routine. "
            "And then calculate monthly spending for June 2025."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Jane", "last_name": "Smith"}
            ),
            Action(
                name="get_customer_loans",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"}
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_2001",
                    "to_account_id": "acc_sav_2002",
                    "amount": 400,
                    "description": "Regular savings routine"
                }
            ),
            Action(
                name="calculate_monthly_spending",
                kwargs={
                    "account_id": "acc_chk_2001",
                    "month": 6,
                    "year": 2025
                }
            )
        ],
        outputs=["Loans reviewed, transfer completed, spending calculated"]
    ),


    Task(
        annotator=0,
        user_id="BANK_085",
        instruction=(
            "You are David Chen and want to search transactions and check account security. "
            "Find your profile, search for withdrawal transactions over $500 in June 2025, "
            "calculate total withdrawals, and freeze your account due to suspicious activity."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "David", "last_name": "Chen"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 500.01,
                    "transaction_type": "Withdrawal"
                }
            ),
            Action(
                name="calculate_total_withdrawal",
                kwargs={
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="freeze_account",
                kwargs={
                    "account_id": "acc_chk_3001",
                    "reason": "Suspicious activity detected"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_086",
        instruction=(
            "You are Maria Garcia and want to review credit and payments."
            "Find your profile, calculate credit utilization, get recent transactions (last 8), "
            "and calculate total bill payments for July 2025."
            "Before you finish, add John Doe as a beneficiary with account number As234fdg and routing number 126579823."
            "His bank is City National Bank."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Maria", "last_name": "Garcia"}
            ),
            Action(
                name="calculate_credit_utilization",
                kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"}
            ),
            Action(
                name="get_account_transactions",
                kwargs={
                    "account_id": "acc_chk_4001",
                    "limit": 8
                }
            ),
            Action(
                name="calculate_total_bill_payments",
                kwargs={
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "beneficiary_name": "John Doe",
                    "account_number": "As234fdg",
                    "routing_number": "126579823",
                    "bank_name": "City National Bank"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_087",
        instruction=(
            "You are Lakshmi Narayanan and want to handle account statements and get support. "
            "Find your profile, generate account statement for your savings account acc_sav_5001 for June 2025, "
            "get your support tickets, and create a new ticket asking about how to apply for a new loan."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="get_customer_support_tickets",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"}
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "subject": "Apply for new loan",
                    "description": "how to apply for a new loan"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_088",
        instruction=(
            "You are Fatima Al-Fassi and want to review checking payments and saving deposits comprehensively. "
            "Find your profile, calculate total payments for June 2025, calculate total deposits for June 2025, "
            "get scheduled payments for July 2025 going into checkings, and generate monthly summary for checkings."
            "Add David Chen as a new beneficiary for his medical services for July 2025"
            "His account number is B4FD12345, routing number is 987123, and his bank is Bank of Bahamas"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Fatima", "last_name": "Al-Fassi"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"}
            ),
            Action(
                name="calculate_total_payments",
                kwargs={
                    "account_id": "acc_chk_7001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_sav_7002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "source_account_id": "acc_chk_7001",
                    "month": "2025-07"
                }
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_chk_7001",
                    "month": "2025-06"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "beneficiary_name": "David Chen",
                    "account_number": "B4FD12345",
                    "routing_number": "987123",
                    "bank_name": "Bank of Bahamas"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_089",
        instruction=(
            "You are John Doe and you want to transfer $50 from your checking account to your savings account."
            "You need to verify your current balances before and after the transfer."
            "After the transfer, tell me what your new checking account balance is."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "John", "last_name": "Doe"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_1001"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_sav_1002"}
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_1001",
                    "to_account_id": "acc_sav_1002",
                    "amount": 50
                }
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_1001"}
            )
        ],
        outputs=["5180.50"]
    ),

    Task(
        annotator=0,
        user_id="BANK_090",
        instruction=(
            "You are Hans Müller and want to analyze account activity and handle transactions. "
            "Find your profile, search for purchase and deposit transactions in July 2025, "
            "calculate combined spending, and generate detailed monthly report."
            "Then create a support ticket today and get help setting up automated payments to your utility provider."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Hans", "last_name": "Müller"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"}
            ),
            Action(
                name="calculate_total_event_and_purchase_spending",
                kwargs={
                    "account_id": "acc_chk_8001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_sav_8002",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            ),
            Action(
                name="generate_detailed_monthly_report",
                kwargs={
                    "account_id": "acc_chk_8001",
                    "month": "2025-07"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "subject": "setting up automated payments",
                    "description": "setting up automated payments to your utility provider"
                }
            ),
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_091",
        instruction=(
            "You are Mohammed Al-Masri and want to check your checking account for any payments over $200, "
            "made in the month of June. First, find your customer profile. Retrieve your checking account."
            "Search for all transactions over $200 in June 2025. Create a support ticket about your payment review."
            "Then, generate a statement for your checking account for June 2025 and report the number of transactions above $200."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Mohammed", "last_name": "Al-Masri"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_26001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 200
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "subject": "Payment review",
                    "description": "Payment review"
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_chk_26001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_092",
        instruction=(
            "You are Kenji Tanaka and want to handle loans and scheduled payments. "
            "Find your profile, get loan applications, and retrieve scheduled payments for August 2025 on your checking "
            "with acc_chk_10001."
            "And update phone number to 555-345-6789."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Kenji", "last_name": "Tanaka"}
            ),
            Action(
                name="get_loan_applications_for_customer",
                kwargs={"customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"}
            ),
            Action(
                name="retrieve_scheduled_payments",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "source_account_id": "acc_chk_10001",
                    "month": "2025-08"
                }
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "phone": "555-345-6789"
                }
            )
        ],
        outputs=["Loan applications reviewed, scheduled payments checked, contact updated"]
    ),


    Task(
        annotator=0,
        user_id="BANK_093",
        instruction=(
            "You are Isabella Rossi and want to analyze deposits and purchases."
            "Find your profile, calculate total deposits and purchases for your accounts in June 2025, "
            "and generate account statements for checkings."
            "Then create a support ticket for finding more about credit card deals."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Isabella", "last_name": "Rossi"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10"}
            ),
            Action(
                name="calculate_total_deposits_and_purchases",
                kwargs={
                    "account_id": "acc_chk_11001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="generate_account_statement",
                kwargs={
                    "account_id": "acc_chk_11001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "subject": "finding more about credit card deals",
                    "description": "finding more about credit card deals"
                }
            ),
        ],
        outputs=["0"]
    ),


    Task(
        annotator=0,
        user_id="BANK_094",
        instruction=(
            "You are Liam O'Connor and want to manage account access and review activity."
            "First find your profile."
            "Search customers by email domain yahoo.com, get your checking account balance, "
            "and create a support ticket about online access issues with a description about how you cannot access the mobile banking app."
            "Then add Lisa Davis as a new beneficiary with account number 9876543210, routing number 111000025, "
            "who banks with Bank of America"
            "Then freeze your checking account to protect from possible fraud"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Liam", "last_name": "O'Connor"}
            ),
            Action(
                name="search_customers_by_email",
                kwargs={"email_domain": "yahoo.com"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_12001"}
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "subject": "Online Access Issues",
                    "description": "Cannot access mobile the banking app"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "beneficiary_name": "Lisa Davis",
                    "account_number": "9876543210",
                    "routing_number": "111000025",
                    "bank_name": "Bank of America"
                }
            ),
            Action(
                name="freeze_account",
                kwargs={
                    "account_id": "acc_chk_12001",
                    "reason": "Protect from possible fraud"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_095",
        instruction=(
            "You are Alex Petrov and want to perform a comprehensive account review. "
            "Find your profile, get recent transactions (last 12) from your checking account acc_chk_14001, "
            "check credit utilization, and generate monthly summary for July 2025 for your checking account."
            "Then add Lisa Davis as a new beneficiary with account number 9876543210, routing number 111000025, "
            "and with Bank of America"
            "Finally, create a support ticket asking for help with how to add more beneficiaries"
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Alex", "last_name": "Petrov"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}
            ),
            Action(
                name="get_account_transactions",
                kwargs={
                    "account_id": "acc_chk_14001",
                    "limit": 12
                }
            ),
            Action(
                name="calculate_credit_utilization",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"}
            ),
            Action(
                name="generate_monthly_account_summary",
                kwargs={
                    "account_id": "acc_chk_14001",
                    "month": "2025-07"
                }
            ),
            Action(
                name="add_beneficiary",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13",
                    "beneficiary_name": "Lisa Davis",
                    "account_number": "9876543210",
                    "routing_number": "111000025",
                    "bank_name": "Bank of America"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13",
                    "subject": "asking for help with how to add more beneficiaries",
                    "description": "asking for help with how to add more beneficiaries"
                }
            ),
        ],
        outputs=["0"]
    ),


    Task(
        annotator=0,
        user_id="BANK_096",
        instruction="You are John Doe and you want to transfer $3000 from your checking account to your savings account. You need to verify your current balances before and after the transfer. After the transfer, tell me what your new checking account balance is.",
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "John", "last_name": "Doe"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_1001"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_sav_1002"}
            ),
            Action(
                name="transfer_funds",
                kwargs={
                    "from_account_id": "acc_chk_1001",
                    "to_account_id": "acc_sav_1002",
                    "amount": 3000
                }
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_1001"}
            )
        ],
        outputs=["2230.50"]
    ),

    Task(
        annotator=0,
        user_id="BANK_097",
        instruction=(
            "You are Anja Novak and want to analyze spending patterns and account status."
            "Find your profile, search for purchase transactions over $200 in July 2025 on your checking account acc_chk_19001, "
            "calculate monthly spending for July 2025, and get support tickets with Open status."
            "You also need to get a loan for your next vacation. Apply for a person loan for $3,000."
            "Your annual income is 40000."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Anja", "last_name": "Novak"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_19001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "min_amount": 200.01,
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="calculate_monthly_spending",
                kwargs={
                    "account_id": "acc_chk_19001",
                    "month": 7,
                    "year": 2025
                }
            ),
            Action(
                name="get_customer_support_tickets",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "status": "Open"
                }
            ),
            Action(
                name="apply_for_loan",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "loan_type": "Personal",
                    "requested_amount": 3000,
                    "purpose": "Vacation",
                    "annual_income": 40000
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_098",
        instruction=(
            "You are Santiago Muñoz and want to perform a comprehensive financial review. "
            "Find your profile, calculate total expenditure for June 2025 on your checking account acc_chk_20001, "
            "get customer loans, calculate account balance for that account, and generate financial report for June 2025."
            "You heard that there was a data break and want to freeze your account for safety."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Santiago", "last_name": "Muñoz"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}
            ),
            Action(
                name="calculate_total_expenditure",
                kwargs={
                    "account_id": "acc_chk_20001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                }
            ),
            Action(
                name="get_customer_loans",
                kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"}
            ),
            Action(
                name="calculate_account_balance",
                kwargs={"account_id": "acc_chk_20001"}
            ),
            Action(
                name="generate_financial_report",
                kwargs={
                    "account_id": "acc_chk_20001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            ),
            Action(
                name="freeze_account",
                kwargs={
                    "account_id": "acc_chk_20001",
                    "reason": "Data break and safety"
                }
            )
        ],
        outputs=["0"]
    ),

    Task(
        annotator=0,
        user_id="BANK_099",
        instruction=(
            "You are Yara Haddad and want to manage account settings and payments. "
            "Find your profile, update email to yara.haddad.new@email.com, "
            "get all beneficiaries, and cancel a scheduled payment for payment ID sp_c7k9b8j1-i5j4-k3l2-m1n0-o9p8q7r6s5t4 since it is no longer needed."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Yara", "last_name": "Haddad"}
            ),
            Action(
                name="update_customer_contact",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "email": "yara.haddad.new@email.com"
                }
            ),
            Action(
                name="get_customer_beneficiaries",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20"}
            ),
            Action(
                name="cancel_scheduled_payment",
                kwargs={
                    "payment_id": "sp_c7k9b8j1-i5j4-k3l2-m1n0-o9p8q7r6s5t4",
                    "reason": "No longer needed"
                }
            )
        ],
        outputs=["0"]
    ),


    Task(
        annotator=0,
        user_id="BANK_100",
        instruction=(
            "You are Adetokunbo Adebayor and want to complete end-to-end account analysis. "
            "Find your profile, search for all transaction types in July 2025 on checking account acc_chk_24001, "
            "calculate total deposits for savings account acc_sav_24002 and withdrawals for checking account, "
            "generate detailed monthly report for checking account, "
            "and create a low priority support ticket with subject 'Account Review Completed' "
            "and description 'Comprehensive account analysis finished for July 2025'."
        ),
        actions=[
            Action(
                name="find_customer_by_name",
                kwargs={"first_name": "Adetokunbo", "last_name": "Adebayor"}
            ),
            Action(
                name="get_customer_accounts",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"}
            ),
            Action(
                name="search_transactions",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            ),
            Action(
                name="calculate_total_deposits",
                kwargs={
                    "account_id": "acc_sav_24002",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            ),
            Action(
                name="calculate_total_withdrawal",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            ),
            Action(
                name="generate_detailed_monthly_report",
                kwargs={
                    "account_id": "acc_chk_24001",
                    "month": "2025-07"
                }
            ),
            Action(
                name="create_support_ticket",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "subject": "Account Review Completed",
                    "description": "Comprehensive account analysis finished for July 2025",
                    "priority": "Low"
                }
            )
        ],
        outputs=["0"]
    )

]
