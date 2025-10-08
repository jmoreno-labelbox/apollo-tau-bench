# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "BANK_001",
        "instruction": "Assume the identity of Kenji Tanaka and aim to transfer $500 from your checking account to your savings account.Confirm the balances available both before and after completing the transfer. Once the transfer has been finalized, inform me about your new checking account balance. Lastly, add Elena Popescu as a new beneficiary with account number 9876543210, routing number 122000661, at City National Bank.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_1001"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_sav_1002"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_1001",
                    "to_account_id": "acc_sav_1002",
                    "amount": 500
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_1001"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Elena Popescu",
                    "account_number": "9876543210",
                    "routing_number": "122000661",
                    "bank_name": "City National Bank"
                }
            }
        ],
        "outputs": [
                "4730.50"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_002",
        "instruction": "Playing the role of Elena Popescu, you intend to seek a $25000 personal loan for the purpose of home renovation. Your yearly income stands at $75000. After applying, open a support ticket to inquire about the status. Then, review your credit utilization across all accounts and report your total credit utilization percentage. Afterward, include ATX, Inc. as a beneficiary with account number A23d45fg at Barclays.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "ApplyForLoan",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "loan_type": "Personal",
                    "requested_amount": 25000,
                    "purpose": "Home renovation",
                    "annual_income": 75000
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "subject": "Loan Application Status",
                    "description": "Loan Application Status"
                },
            },
            {
                "name": "CalculateCreditUtilization",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_name": "ATX, Inc.",
                    "account_number": "A23d45fg",
                    "bank_name": "Barclays"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_003",
        "instruction": "Identify yourself as Chloe Dubois, intending to arrange a monthly payment of \u20ac1500 to Klaus Schmidt for your apartment rent. Initially, locate your checking account. Then verify that Klaus Schmidt is a listed beneficiary and establish the monthly payment starting 2024-08-01. Check your existing mortgage loan balance. Finally, add Soft Solutions, LLC. as a beneficiary with account number BGT543456 at Barclays.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Hans",
                    "last_name": "Müller"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"
                },
            },
            {
                "name": "GetCustomerBeneficiaries",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"
                },
            },
            {
                "name": "SetupScheduledPayment",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "from_account_id": "acc_chk_8001",
                    "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a",
                    "amount": 1500,
                    "frequency": "Monthly",
                    "start_date": "2024-08-01"
                },
            },
            {
                "name": "GetCustomerLoans",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "beneficiary_name": "Soft Solutions, LLC.",
                    "account_number": "BGT543456",
                    "bank_name": "Barclays"
                }
            }
        ],
        "outputs": [
                "180000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_004",
        "instruction": "Identify as Chloe Dubois and seek to compensate your business partner after a recent sale. As a company owner, examine major payments dispensed from your checking account last month. Access your customer record. Acquire your checking account and also Kenji Tanaka's records. Investigate all transactions exceeding $500 in June 2025. Disburse a $200 payment to your partner, Kenji Tanaka, to his checking account. File a support ticket to learn how to receive alerts for beneficiary payments. Then, register Patty Gordon as a beneficiary, with account number VCG552431 at CitiBank.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Sofia",
                    "last_name": "Andersson"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14"
                },
            },
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 500
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_15001",
                    "to_account_id": "acc_chk_1001",
                    "amount": 200
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "subject": "Notifications of beneficiary payments",
                    "description": "get notified when beneficiary payments occur"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "beneficiary_name": "Patty Gordon",
                    "account_number": "VCG552431",
                    "bank_name": "CitiBank"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_005",
        "instruction": "Assume the identity of Oliver Williams with the aim to designate a new beneficiary, Elena Popescu, who is your insurance specialist. Start by obtaining your customer record and accessing your business checking account. Investigate all outgoing withdrawal transactions above $1,000 in July 2025. Proceed to register Elena Popescu as a new beneficiary with account number 9876543210, routing number 122000661, at City National Bank. Subsequently, generate an account statement for July 2025 and document the total number of outgoing transactions greater than $1,000.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Adetokunbo",
                    "last_name": "Adebayor"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "min_amount": 1000,
                    "transaction_type": "Withdrawal"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "beneficiary_name": "Elena Popescu",
                    "account_number": "9876543210",
                    "routing_number": "122000661",
                    "bank_name": "City National Bank"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_006",
        "instruction": "You are Kenji Tanaka with the aim of remodeling your kitchen and reviewing your credit card transactions for the past month. Your annual income is $45000. Initially, locate your customer profile and access your credit card account. Identify all charges exceeding $200 in June 2025 that are considered expensive. Apply for a personal loan of $10,000 to finance your kitchen remodel. Next, produce a statement for your credit card covering June 2025 and tally the transactions surpassing $200.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Dubois"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_crd_9002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 200
                },
            },
            {
                "name": "ApplyForLoan",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "loan_type": "Personal",
                    "requested_amount": 10000,
                    "purpose": "Remodel kitchen",
                    "annual_income": 45000
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_crd_9002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_007",
        "instruction": "You are Gabriel Silva and need to overview your recent checking account activities. Also, you need to cancel a scheduled payment to Elena Popescu due to the end of her service contract. Begin by locating your customer profile and accessing your checking account. Look for incoming transactions surpassing $300 in June 2025. Cancel your scheduled payment using payment_id sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f. Subsequently, generate a statement for your checking account for June 2025 and report the number of incoming transactions exceeding $300.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Aisha",
                    "last_name": "Khan"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_13001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 300,
                    "transaction_type": "Incoming"
                },
            },
            {
                "name": "CancelScheduledPayment",
                "arguments": {
                    "payment_id": "sp_d9b3a2c1-6a5b-4c3d-2e1f-0a9b8c7d6e5f"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_chk_13001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_008",
        "instruction": "You are Chloe Dubois with the intention of reviewing your savings account activity for the past month. First, locate your customer profile and retrieve your savings account. Search for deposits greater than $1,000 in June 2025. Cancel your scheduled payment using payment_id sp_f1h3a2g4-f8g7-h6i5-j4k3-l2m1n0o9p8q6. You have questions about performing a payment cancellation and require assistance. Create a support ticket asking for help with this payment cancellation. Lastly, create a statement for your savings account in June 2025 and report the total number of deposits over $1,000.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Hans",
                    "last_name": "Müller"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_sav_8002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 1000,
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CancelScheduledPayment",
                "arguments": {
                    "payment_id": "sp_f1h3a2g4-f8g7-h6i5-j4k3-l2m1n0o9p8q6"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "subject": "Payment cancellation",
                    "description": "Payment cancellation"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_sav_8002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_009",
        "instruction": "You are Lakshmi Narayanan aiming to review your savings account for recent interest earnings. Your annual income is $36000. Start by finding your customer profile and retrieving your savings account. Search for all interest-earned transactions in June 2025. Apply for a personal loan of $1,000 for your small business needs. Then, draft a statement for your savings account for June 2025 and report the total interest credited. Finally, add Soft Solutions, LLC. as a beneficiary with account number BGT543456 at Barclays.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Elena",
                    "last_name": "Popescu"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Interest"
                },
            },
            {
                "name": "ApplyForLoan",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "loan_type": "Personal",
                    "requested_amount": 1000,
                    "purpose": "Small business loan",
                    "annual_income": 36000
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "beneficiary_name": "Soft Solutions, LLC.",
                    "account_number": "BGT543456",
                    "bank_name": "Barclays"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_010",
        "instruction": "You are Zoltan Nagy and plan to transfer $2000 from your checking account to your savings account. Verify your current balances both before and after the transfer. After completing the transfer, indicate your new checking account balance. Lastly, add Soft Solutions, LLC. as a beneficiary with account number BGT543456 at Barclays.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_5002"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_sav_5001"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_5002",
                    "to_account_id": "acc_sav_5001",
                    "amount": 2000
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_5002"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "Soft Solutions, LLC.",
                    "account_number": "BGT543456",
                    "bank_name": "Barclays"
                }
            }
        ],
        "outputs": [
                "48000"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_011",
        "instruction": "Assume the role of Zoltan Nagy, examining your checking account for significant transactions. With an annual income of $350000, begin by locating your customer profile to access your checking account. Identify transactions exceeding $5,000 in June 2025. Apply for a student loan amounting to $10,000 for your son's college expenses. Afterwards, create a statement for your checking account for June 2025 and count the transactions over $5,000.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_5002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 5000
                },
            },
            {
                "name": "ApplyForLoan",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "loan_type": "Student",
                    "requested_amount": 10000,
                    "purpose": "Son's college tuition",
                    "annual_income": 350000
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_chk_5002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_012",
        "instruction": ["You are Sofia Andersson and want a summary of all incoming payments to your checking account last month.First, find your customer profile. Retrieve your checking account.Search for all incoming transactions in June 2025. Create a support ticket about your account review.Then, generate a statement for your checking account for June 2025 and report the total number of incoming transactions."],
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Williams"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_6001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "subject": "Account review",
                    "description": "Account review"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_chk_6001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_013",
        "instruction": "Take on the identity of Oliver Williams, focusing on the withdrawals from your savings account during June 2025. Initially, find your customer profile. Gain access to your savings account. Identify all withdrawal activities that took place in June 2025. Proceed to open a support ticket about your withdrawal inspection. Then, generate a statement for your savings account for June 2025 and calculate the total withdrawal transactions.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Fatima",
                    "last_name": "Al-Fassi"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_sav_7002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "subject": "Withdrawal review",
                    "description": "Withdrawal review"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_sav_7002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_014",
        "instruction": "Act as Sofia Andersson, intent on reviewing your checking account payments over $200 completed in June. Begin by locating your customer profile. Reach your checking account. Identify all transactions exceeding $200 in June 2025. Initiate a support ticket for your payment examination. Next, create a statement for your checking account for June 2025 and keep track of the number of transactions over $200.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 200
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "subject": "Payment review",
                    "description": "Payment review"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_015",
        "instruction": "Assume the identity of Santiago Mu\u00f1oz, verifying purchases equal to or exceeding $300 made on your checking account last month. Start by finding your customer profile to gain access to your checking account. Identify transactions over $300 in June 2025. Update your contact details using the new email address isabella.rossi.updated@email.com. Following this action, create a statement for your checking account for June 2025 and record the purchases over $300.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Isabella",
                    "last_name": "Rossi"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_11001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 300,
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "email": "isabella.rossi.updated@email.com"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_chk_11001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_016",
        "instruction": "Take the role of Zoltan Nagy to examine outgoing payments from your checking account for last month. Begin by identifying your customer profile. Access your checking account, identifying all outgoing withdrawals of $500 or more in June 2025. Update your contact details with a new phone number 555-123-9999. Subsequently, produce a statement for your checking account for June 2025 and report the total outgoing transactions over $500.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Liam",
                    "last_name": "O'Connor"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_12001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 500,
                    "transaction_type": "Withdrawal"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "phone": "555-123-9999"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_chk_12001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_017",
        "instruction": "As Adetokunbo Adebayor, your task is to outline all deposits made into your savings account during June 2025. Start by identifying your customer profile. Access your savings account. Identify all deposit transactions within June 2025. Modify your contact information to incorporate a new email address kenji.tanaka.updated@email.com. Then, compose a statement for your savings account for June 2025, detailing the total deposits made.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Kenji",
                    "last_name": "Tanaka"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_sav_10002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "email": "kenji.tanaka.updated@email.com"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_sav_10002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_018",
        "instruction": "You are Santiago Mu\u00f1oz and wish to review your checking account transactions for June 2025. Initially, locate your customer profile and access your checking account (acc_chk_19001).1. Identify all purchase transactions in June 2025 for your checking account.2. Determine the total expenditure for the month.3. Retrieve any payments scheduled from your checking account during June 2025.4. Update your contact details with a new email address anja.novak.updated@email.com.5. Produce a summary reflecting total purchases and scheduled payments for June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Anja",
                    "last_name": "Novak"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_19001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_19001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "source_account_id": "acc_chk_19001",
                    "month": "2025-06"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "email": "anja.novak.updated@email.com"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_chk_19001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Summary for Santiago Muñoz: total purchase amount and scheduled payments for acc_chk_19001 in June 2025."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_019",
        "instruction": "You are Elena Popescu and intend to examine the activity in your checking account for June 2025. Begin by finding your customer profile and accessing your checking account (acc_chk_20001).1. Locate all purchase transactions in June 2025 for your checking account.2. Assess the total spending for the month.3. Extract any scheduled payments from your checking account for June 2025.4. Update your contact information with the new phone number 555-789-1234.5. Create a summary displaying total purchases and scheduled payments for June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Santiago",
                    "last_name": "Muñoz"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_20001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_20001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19",
                    "source_account_id": "acc_chk_20001",
                    "month": "2025-06"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19",
                    "phone": "555-789-1234"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_chk_20001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Summary for Elena Popescu: total purchase amount and scheduled payments for acc_chk_20001 in June 2025."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_020",
        "instruction": "You are Isabella Rossi and you want to inspect your checking account activity for June 2025. First, find your customer profile and access your checking account (acc_chk_21001).1. Discover all purchase transactions in June 2025 for your checking account.2. Calculate the month's total expenses.3. Obtain any planned payments from your checking account for June 2025.4. Refresh your contact information with a new email address yara.haddad.updated@email.com.5. Create a summary that includes total purchases and scheduled payments for June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Yara",
                    "last_name": "Haddad"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_21001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_21001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "source_account_id": "acc_chk_21001",
                    "month": "2025-06"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "email": "yara.haddad.updated@email.com"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_chk_21001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Summary for Isabella Rossi: total purchase amount and scheduled payments for acc_chk_21001 in June 2025."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_021",
        "instruction": "You are Oliver Williams, looking to evaluate account activity and manage transactions. Locate your profile, identify purchase and deposit transactions for your checking account in July 2025, compute combined expenses, and then produce a comprehensive monthly report. Next, initiate a support ticket to receive assistance in establishing automated payments to your water provider. Lastly, add ATX, Inc. as a beneficiary with account number A23d45fg at Barclays.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Fatima",
                    "last_name": "Al-Fassi"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"
                },
            },
            {
                "name": "CalculateTotalEventAndPurchaseSpending",
                "arguments": {
                    "account_id": "acc_chk_7001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_chk_7001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                },
            },
            {
                "name": "GenerateDetailedMonthlyReport",
                "arguments": {
                    "account_id": "acc_chk_7001",
                    "month": "2025-07"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "subject": "setting up automated payments to your water provider",
                    "description": "setting up automated payments to your water provider"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "beneficiary_name": "ATX, Inc.",
                    "account_number": "A23d45fg",
                    "bank_name": "Barclays"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_022",
        "instruction": "You are Sofia Andersson and aim to review your financial activity for June 2025. Begin by locating your customer profile. Retrieve your checking account (acc_chk_6001). 1. Locate all purchase transactions in June 2025. 2. Compute the total amount spent on these purchases. 3. Retrieve any scheduled payments from your checking account for June 2025. 4. Identify any support tickets related to your checking account opened or resolved in June 2025. 5. Update your contact information with the new phone number 555-456-7890. Lastly, prepare a summary incorporating total purchases, scheduled payments, and support tickets related to your checking account for June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Williams"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_6001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_6001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "source_account_id": "acc_chk_6001",
                    "month": "2025-06"
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "account_id": "acc_chk_6001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "phone": "555-456-7890"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_chk_6001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Summary for Sofia Andersson: total purchase amount, scheduled payments, and support tickets for acc_chk_6001 in June 2025."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_023",
        "instruction": "You are Kenji Tanaka and wish to transfer $1500 from your checking account to your savings account. Ensure you confirm your current balances before and after the transfer. Once the transfer is complete, inform me of your new checking account balance. Finally, add Soft Solutions, LLC. as a beneficiary with account number BGT543456 at Barclays.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_1001"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_sav_1002"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_1001",
                    "to_account_id": "acc_sav_1002",
                    "amount": 1500
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_1001"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Soft Solutions, LLC.",
                    "account_number": "BGT543456",
                    "bank_name": "Barclays"
                }
            }
        ],
        "outputs": [
                "3730.50"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_024",
        "instruction": "You are Kenji Tanaka and intend to examine your financial activity for June 2025. Start with locating your customer profile and retrieve all your accounts. For your checking account (acc_chk_9001): 1. Locate all purchase transactions in June 2025. 2. Compute the total spent on purchases for the month. 3. Retrieve any scheduled payments made from your checking account in June 2025. Additionally: 4. Identify any support tickets related to your customer ID opened or resolved in June 2025. 5. Update your contact information with the new phone number 555-321-6789. Lastly, generate a summary illustrating: - Total purchases from checking - Scheduled payments from checking - Support tickets involving your customer ID in June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Dubois"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_9001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_9001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "source_account_id": "acc_chk_9001",
                    "month": "2025-06"
                },
            },
            {
                "name": "GetSupportTicketsForAccount",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "phone": "555-321-6789"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_chk_9001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Summary for Kenji Tanaka: total purchase amount, scheduled payments, and support tickets for acc_chk_9001 in June 2025."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_025",
        "instruction": "You are Zoltan Nagy and want to assess your savings and checking activity for June 2025. Start by locating your customer profile and retrieve your savings account (acc_sav_5001) and checking account (acc_chk_5002). 1. Find all deposit transactions in June 2025 for your savings account. 2. Compute the total deposits for the month. 3. Locate all purchase transactions in June 2025 for your checking account. 4. Calculate the total spent on purchases from your checking account for the month. 5. Retrieve any scheduled payments from your checking account for June 2025. 6. Identify any support tickets related to status changes for your savings or checking account opened or resolved in June 2025. 7. Update your contact information with the new email address lakshmi.narayanan.newupdated@email.com. Finally, produce summaries showing: - Total deposits into savings - Total purchases from checking - Scheduled payments from checking - Support tickets for status changes in June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_5002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_5002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "source_account_id": "acc_chk_5002",
                    "month": "2025-06"
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "account_ids": [
                        "acc_sav_5001",
                        "acc_chk_5002"
                    ],
                    "fields": [
                        "status"
                    ],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "email": "lakshmi.narayanan.newupdated@email.com"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_chk_5002",
                    "month": "2025-06"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_sav_5001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Reviewed total deposits, purchases, scheduled payments, and made a support tickets"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_026",
        "instruction": "You are Zoltan Nagy and plan to examine your business loan and checking account activity for June 2025. Begin with finding your customer profile and retrieve your business loan account (acc_loan_12002) and checking account (acc_chk_12001). 1. Locate all loan payment transactions in June 2025 for your business loan account. 2. Calculate the total paid on the loan for the month. 3. Locate all purchase transactions in June 2025 for your checking account. 4. Compute the total spent on purchases from your checking account for the month. 5. Retrieve any scheduled payments from your checking account for June 2025. 6. Identify any support tickets related to your loan or checking account opened or resolved in June 2025. 7. Update your contact information with the new phone number 555-987-6543.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Liam",
                    "last_name": "O'Connor"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_loan_12002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Payment"
                },
            },
            {
                "name": "CalculateTotalPayments",
                "arguments": {
                    "account_id": "acc_loan_12002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Payment"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_12001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_12001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "source_account_id": "acc_chk_12001",
                    "month": "2025-06"
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "account_ids": [
                        "acc_loan_12002",
                        "acc_chk_12001"
                    ],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "phone": "555-987-6543"
                }
            }
        ],
        "outputs": [
                "Updated contact phone number for Zoltan Nagy."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_027",
        "instruction": "You are Zoltan Nagy and need to review your investment and checking account activities for June 2025. Begin by locating your customer profile and accessing your investment account (acc_inv_3002) and checking account (acc_chk_3001).1. Investigate all deposit and purchase transactions in June 2025 for your investment account.2. Determine the total amount deposited and total spent on purchases in your investment account for the month.3. Look up all ATM withdrawal transactions in June 2025 for your checking account.4. Ascertain the total withdrawn from your checking account via ATM for the month.5. Access any scheduled payments from your checking account for June 2025.6. Identify any support tickets related to your accounts opened or resolved in June 2025.7. Modify your contact information with a new email address david.chen.updated@email.com.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_inv_3002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": [
                        "Deposit",
                        "Purchase"
                    ]
                },
            },
            {
                "name": "CalculateTotalDepositsAndPurchases",
                "arguments": {
                    "account_id": "acc_inv_3002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "ATM Withdrawal"
                },
            },
            {
                "name": "CalculateTotalAtmWithdrawals",
                "arguments": {
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "source_account_id": "acc_chk_3001",
                    "month": "2025-06"
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_ids": [
                        "acc_inv_3002",
                        "acc_chk_3001"
                    ],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "email": "david.chen.updated@email.com"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_028",
        "instruction": "You are Oliver Williams and need to examine account activity and handle transactions. Locate your profile, research purchase and deposit transactions in July 2025, compute combined spending, and compile a detailed monthly report. Then initiate a support ticket and seek help setting up automated payments to your utility provider.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Adetokunbo",
                    "last_name": "Adebayor"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"
                },
            },
            {
                "name": "CalculateTotalEventAndPurchaseSpending",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_sav_24002",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                },
            },
            {
                "name": "GenerateDetailedMonthlyReport",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "month": "2025-07"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "subject": "setting up automated payments to your utility provider",
                    "description": "setting up automated payments to your utility provider"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_029",
        "instruction": "You are Chloe Dubois and aim to assess your checking account activities for June 2025. Initially, locate your customer profile and access your checking account (acc_chk_8001).1. Investigate all purchase transactions in June 2025 for your checking account.2. Determine the total paid on purchases for the month.3. Access any scheduled payments from your checking account for June 2025.4. Identify any support tickets related to your checking account opened or resolved in June 2025.5. Modify your contact information with a new email address hans.muller.updated@email.com. Finally, compile a summary showing: - Total purchases from checking - Scheduled payments from checking - Support tickets for checking account in June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Hans",
                    "last_name": "Müller"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_8001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_8001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "source_account_id": "acc_chk_8001",
                    "month": "2025-06"
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "account_ids": [
                        "acc_chk_8001"
                    ],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "email": "hans.muller.updated@email.com"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_chk_8001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Total purchases from checking: [amount]",
                "Scheduled payments from checking: [count/details]",
                "Support tickets for checking account in June: [count/details]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_030",
        "instruction": "You are Chloe Dubois and require a comprehensive assessment of your banking and financial activities for June 2025. Begin by locating your customer profile and accessing your checking account (acc_chk_15001).1. Investigate all purchase transactions and concert/event ticket purchases in June 2025 for your checking account.2. Determine the total amount spent on purchases and tickets for the month.3. Look up all deposit transactions in June 2025 for your checking account.4. Ascertain total deposits for the month.5. Access any scheduled payments from your checking account for June 2025.6. Identify any support tickets related to your checking account opened or resolved in June 2025.7. Retrieve your loan application history prior to July 2025 and their statuses.8. Identify any changes to your account status, nickname, or beneficiary details via support tickets in June 2025.9. Investigate any bill payment transactions in June 2025 for your checking account.10. Ascertain the total bill payments for the month.11. Update your contact information with a new phone number 555-111-2222.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Sofia",
                    "last_name": "Andersson"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": [
                        "Purchase"
                    ],
                    "description_keywords": [
                        "Concert",
                        "Ticket",
                        "Event"
                    ]
                },
            },
            {
                "name": "CalculateTotalEventAndPurchaseSpending",
                "arguments": {
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": [
                        "Deposit"
                    ]
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "source_account_id": "acc_chk_15001",
                    "month": "2025-06"
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "GetLoanApplicationsForCustomer",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "before_date": "2025-07-01T00:00:00Z"
                },
            },
            {
                "name": "GetAccountChangesFromTickets",
                "arguments": {
                    "account_id": "acc_chk_15001"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": [
                        "Bill Payment"
                    ]
                },
            },
            {
                "name": "CalculateTotalBillPayments",
                "arguments": {
                    "account_id": "acc_chk_15001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "phone": "555-111-2222"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_031",
        "instruction": "You are Adetokunbo Adebayor and need a comprehensive assessment of your banking activity for June 2025. Start by locating your customer profile. Your checking account is acc_chk_10001, and your savings account is acc_sav_10002.1. Investigate all purchase transactions in June 2025 for your checking account.2. Determine the total amount spent on purchases for the month.3. Look up all deposit transactions in June 2025 for your savings account.4. Ascertain total deposits for the month.5. Access any scheduled payments from both accounts for June 2025.6. Identify any support tickets related to status changes or beneficiary management for either account opened or resolved in June 2025.7. Retrieve your loan application history prior to July 2025 and their statuses.8. Investigate all bi-weekly or monthly scheduled payments from your savings account in June 2025.9. Identify any changes to your account status or beneficiary details via support tickets in June 2025.10. Update your contact information with a new phone number 555-444-7777.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Kenji",
                    "last_name": "Tanaka"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_10001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_10001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_sav_10002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_sav_10002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "source_account_ids": [
                        "acc_chk_10001",
                        "acc_sav_10002"
                    ],
                    "month": "2025-06"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "source_account_id": "acc_sav_10002",
                    "month": "2025-06",
                    "frequency": [
                        "Bi-Weekly",
                        "Monthly"
                    ]
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "account_ids": [
                        "acc_chk_10001",
                        "acc_sav_10002"
                    ],
                    "fields": [
                        "status",
                        "beneficiaries"
                    ],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "GetLoanApplicationsForCustomer",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "before_date": "2025-07-01T00:00:00Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "phone": "555-444-7777"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_032",
        "instruction": "You are Adetokunbo Adebayor and require a detailed review of your checking account (acc_chk_23001) activity for June 2025. Initially, access your customer profile and account. Then: 1. Locate all purchase transactions in June 2025 for acc_chk_23001. 2. Sum up the total spent on purchases for June. 3. Locate all deposit transactions in June 2025 for acc_chk_23001. 4. Sum up the total deposited for that month. 5. Retrieve any scheduled payments from acc_chk_23001 for June 2025, emphasizing any recurring (monthly or weekly) payments. 6. Identify any support tickets regarding payment issues or account inquiries for acc_chk_23001 that were initiated or resolved in June 2025. 7. Update your contact details to include a new email address mei.lin.updated@email.com. 8. Compile a summary detailing: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Mei",
                    "last_name": "Lin"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_23001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_23001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_23001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_chk_23001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "source_account_id": "acc_chk_23001",
                    "month": "2025-06"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "source_account_id": "acc_chk_23001",
                    "month": "2025-06",
                    "frequency": [
                        "Monthly",
                        "Weekly"
                    ]
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "account_id": "acc_chk_23001",
                    "fields": [
                        "payment issues",
                        "account inquiries"
                    ],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "email": "mei.lin.updated@email.com"
                },
            },
            {
                "name": "GenerateDetailedMonthlySummary",
                "arguments": {
                    "account_id": "acc_chk_23001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Comprehensive summary for Adetokunbo Adebayor: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for acc_chk_23001 in June 2025."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_033",
        "instruction": "You are Oliver Williams and require a detailed review of your checking account (acc_chk_24001) activity for June 2025. Initially, access your customer profile and account. Then: 1. Locate all purchase transactions in June 2025 for acc_chk_24001. 2. Compute the total spent on purchases in June. 3. Locate all deposit transactions in June 2025 for acc_chk_24001. 4. Compute the total deposited for that month. 5. Retrieve any scheduled payments from acc_chk_24001 for June 2025, emphasizing any recurring (monthly or weekly) payments. 6. Identify any support tickets regarding payment issues or account inquiries for acc_chk_24001 that were initiated or resolved in June 2025. 7. Update your contact details to include a new phone number 555-888-9999.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Adetokunbo",
                    "last_name": "Adebayor"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "source_account_id": "acc_chk_24001",
                    "month": "2025-06"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "source_account_id": "acc_chk_24001",
                    "month": "2025-06",
                    "frequency": [
                        "Monthly",
                        "Weekly"
                    ]
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "fields": [
                        "payment issues",
                        "account inquiries"
                    ],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "phone": "555-888-9999"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_034",
        "instruction": "You are Lakshmi Narayanan and require a detailed review of your savings account (acc_sav_25001) activity for June 2025. Initially, access your customer profile and account. Then: 1. Locate all withdrawal transactions in June 2025 for acc_sav_25001. 2. Sum up the total withdrawn for that month. 3. Locate all deposit transactions in June 2025 for acc_sav_25001. 4. Sum up the total deposited for the month. 5. Retrieve any scheduled payments from acc_sav_25001 for June 2025, emphasizing any recurring (monthly or weekly) payments. 6. Identify any support tickets concerning withdrawal or deposit issues for acc_sav_25001 that were initiated or resolved in June 2025. 7. Update your contact details to include a new email address elena.popescu.updated@email.com. 8. Compile a summary for your savings in June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Elena",
                    "last_name": "Popescu"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Withdrawal"
                },
            },
            {
                "name": "CalculateTotalWithdrawal",
                "arguments": {
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "source_account_id": "acc_sav_25001",
                    "month": "2025-06"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "source_account_id": "acc_sav_25001",
                    "month": "2025-06",
                    "frequency": [
                        "Monthly",
                        "Weekly"
                    ]
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "account_id": "acc_sav_25001",
                    "fields": [
                        "withdrawal issues",
                        "deposit issues"
                    ],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "email": "elena.popescu.updated@email.com"
                },
            },
            {
                "name": "GenerateDetailedMonthlyReport",
                "arguments": {
                    "account_id": "acc_sav_25001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Comprehensive summary for Lakshmi Narayanan: total withdrawals, total deposits, scheduled payments (with recurring details), and support tickets for acc_sav_25001 in June 2025."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_035",
        "instruction": "You are Isabella Rossi and require a detailed review of your checking account (acc_chk_26001) activity for June 2025. Initially, access your customer profile and account. Then: 1. Locate all purchase transactions in June 2025 for acc_chk_26001. 2. Compute the total spent on purchases in June. 3. Locate all deposit transactions in June 2025 for acc_chk_26001. 4. Compute the total deposited for that month. 5. Retrieve any scheduled payments from acc_chk_26001 for June 2025, emphasizing any recurring (monthly or weekly) payments. 6. Identify any support tickets regarding payment issues or account inquiries for acc_chk_26001 that were initiated or resolved in June 2025. 7. Update your contact details to include a new phone number 555-777-3333. 8. Compile a summary detailing: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Mohammed",
                    "last_name": "Al-Masri"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_26001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_26001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_26001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_chk_26001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "source_account_id": "acc_chk_26001",
                    "month": "2025-06"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "source_account_id": "acc_chk_26001",
                    "month": "2025-06",
                    "frequency": [
                        "Monthly",
                        "Weekly"
                    ]
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "account_id": "acc_chk_26001",
                    "fields": [
                        "payment issues",
                        "account inquiries"
                    ],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "phone": "555-777-3333"
                },
            },
            {
                "name": "GenerateDetailedMonthlySummary",
                "arguments": {
                    "account_id": "acc_chk_26001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Comprehensive summary for Isabella Rossi: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for acc_chk_26001 in June 2025."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_036",
        "instruction": "You are Kenji Tanaka and require a detailed review of your checking account (acc_chk_1001) activity for June 2025. Initially, access your customer profile and account. Then: 1. Locate all purchase transactions in June 2025 for acc_chk_1001. 2. Compute the total spent on purchases in June. 3. Locate all deposit transactions in June 2025 for acc_chk_1001. 4. Compute the total deposited for that month. 5. Retrieve any scheduled payments from acc_chk_1001 for June 2025, emphasizing any recurring (monthly or weekly) payments. 6. Identify any support tickets regarding payment issues or account inquiries for acc_chk_1001 that were initiated or resolved in June 2025. 7. Update your contact details to include a new email address john.doe.updated@email.com. 8. Compile a summary detailing: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_chk_1001",
                    "month": "2025-06"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_chk_1001",
                    "month": "2025-06",
                    "frequency": [
                        "Monthly",
                        "Weekly"
                    ]
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "account_id": "acc_chk_1001",
                    "fields": [
                        "payment issues",
                        "account inquiries"
                    ],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "email": "john.doe.updated@email.com"
                },
            },
            {
                "name": "GenerateDetailedMonthlySummary",
                "arguments": {
                    "account_id": "acc_chk_1001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Comprehensive summary for Kenji Tanaka: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for acc_chk_1001 in June 2025."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_037",
        "instruction": "As Elena Popescu, you seek a thorough examination of your checking account (acc_chk_2001) activity for June 2025. Begin by accessing your customer profile and account. Then:1. Identify all purchase transactions for acc_chk_2001 in June 2025.2. Compute the total expenditure on purchases in June.3. Identify all deposit transactions for acc_chk_2001 in June 2025.4. Compute the total deposits for the month.5. Access any scheduled payments from acc_chk_2001 for June 2025, and emphasize any recurring (monthly or weekly) payments.6. Search for any support tickets pertaining to payment issues or account queries for acc_chk_2001 that were opened or resolved in June 2025.7. Refresh your contact details by adding a new phone number 555-222-3333.8. Create a summary displaying: total purchases, total deposits, scheduled payments (with recurring information), and support tickets for June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_2001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_2001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_2001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_chk_2001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "source_account_id": "acc_chk_2001",
                    "month": "2025-06"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "source_account_id": "acc_chk_2001",
                    "month": "2025-06",
                    "frequency": [
                        "Monthly",
                        "Weekly"
                    ]
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "account_id": "acc_chk_2001",
                    "fields": [
                        "payment issues",
                        "account inquiries"
                    ],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "phone": "555-222-3333"
                },
            },
            {
                "name": "GenerateDetailedMonthlySummary",
                "arguments": {
                    "account_id": "acc_chk_2001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Comprehensive summary for Elena Popescu: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for acc_chk_2001 in June 2025."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_038",
        "instruction": "As Zoltan Nagy, you wish to undertake a detailed analysis of your checking account (acc_chk_3001) activity for June 2025. Start by retrieving your customer profile and account. Proceed to:1. Identify all purchase transactions for acc_chk_3001 in June 2025.2. Compute the total expenditure on purchases in June.3. Identify all deposit transactions for acc_chk_3001 in June 2025.4. Compute the total deposits for the month.5. Access any scheduled payments from acc_chk_3001 for June 2025, and emphasize any recurring (monthly or weekly) payments.6. Search for any support tickets pertaining to payment issues or account queries for acc_chk_3001 that were opened or resolved in June 2025.7. Refresh your contact details by adding a new email address david.chen.updated2@email.com.8. Create a summary displaying: total purchases, total deposits, scheduled payments (with recurring information), and support tickets for June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "source_account_id": "acc_chk_3001",
                    "month": "2025-06"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "source_account_id": "acc_chk_3001",
                    "month": "2025-06",
                    "frequency": [
                        "Monthly",
                        "Weekly"
                    ]
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "account_id": "acc_chk_3001",
                    "fields": [
                        "payment issues",
                        "account inquiries"
                    ],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "email": "david.chen.updated2@email.com"
                },
            },
            {
                "name": "GenerateDetailedMonthlySummary",
                "arguments": {
                    "account_id": "acc_chk_3001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Comprehensive summary for Zoltan Nagy: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for acc_chk_3001 in June 2025."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_039",
        "instruction": "As Sofia Andersson, you aim for a comprehensive analysis of your checking account (acc_chk_4001) activity for June 2025. Start with finding your customer profile and account. Move on to:1. Identify all purchase transactions for acc_chk_4001 in June 2025.2. Compute the total expenditure on purchases in June.3. Identify all deposit transactions for acc_chk_4001 in June 2025.4. Compute the total deposits for the month.5. Access any scheduled payments from acc_chk_4001 for June 2025, and emphasize any recurring (monthly or weekly) payments.6. Search for any support tickets pertaining to payment issues or account queries for acc_chk_4001 that were opened or resolved in June 2025.7. Refresh your contact details by adding a new phone number 555-333-4444.8. Create a summary displaying: total purchases, total deposits, scheduled payments (with recurring information), and support tickets for June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "source_account_id": "acc_chk_4001",
                    "month": "2025-06"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "source_account_id": "acc_chk_4001",
                    "month": "2025-06",
                    "frequency": [
                        "Monthly",
                        "Weekly"
                    ]
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "account_id": "acc_chk_4001",
                    "fields": [
                        "payment issues",
                        "account inquiries"
                    ],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "phone": "555-333-4444"
                },
            },
            {
                "name": "GenerateDetailedMonthlySummary",
                "arguments": {
                    "account_id": "acc_chk_4001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Comprehensive summary for Sofia Andersson: total purchases, total deposits, scheduled payments (with recurring details), and support tickets for acc_chk_4001 in June 2025."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_040",
        "instruction": "As Zoltan Nagy, you are interested in a detailed review of your savings account (acc_sav_5001) activity for June 2025. Start by accessing your customer profile and account. Continue by:1. Identifying all withdrawal transactions for acc_sav_5001 in June 2025.2. Calculating the total amount withdrawn for the month.3. Identifying all deposit transactions for acc_sav_5001 in June 2025.4. Calculating the total deposits for the month.5. Accessing any scheduled payments from acc_sav_5001 for June 2025, and emphasizing any recurring (monthly or weekly) payments.6. Searching for any support tickets related to withdrawal, deposit, or payment issues for acc_sav_5001 opened or resolved in June 2025.7. Updating your contact information with a new email address lakshmi.narayanan.final@email.com.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Withdrawal"
                },
            },
            {
                "name": "CalculateTotalWithdrawal",
                "arguments": {
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "source_account_id": "acc_sav_5001",
                    "month": "2025-06"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "source_account_id": "acc_sav_5001",
                    "month": "2025-06",
                    "frequency": [
                        "Monthly",
                        "Weekly"
                    ]
                },
            },
            {
                "name": "GetSupportTicketsForAccounts",
                "arguments": {
                    "account_id": "acc_sav_5001",
                    "fields": [
                        "withdrawal issues",
                        "deposit issues",
                        "payment issues"
                    ],
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "email": "lakshmi.narayanan.final@email.com"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_041",
        "instruction": "As Kenji Tanaka, you wish to transfer $2000 from your checking account to your savings account. Ensure you verify your current balances both before and after the transfer. After completing the transfer, inform me of your new checking account balance. Finally, add Soft Solutions, LLC. as a beneficiary with account number SFGTY65466 at CitiBank.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_1001"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_sav_1002"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_1001",
                    "to_account_id": "acc_sav_1002",
                    "amount": 2000
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_1001"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Soft Solutions, LLC.",
                    "account_number": "SFGTY65466",
                    "bank_name": "CitiBank"
                }
            }
        ],
        "outputs": [
                "3230.50"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_042",
        "instruction": "You are Kenji Tanaka, and you intend to move $2500 from your checking to your savings account. Confirm your current balances both before and after this transfer. After completing it, let me know your updated checking account balance. Include Patty Gordon as a beneficiary using account number VCG552431 at CitiBank. Change your contact email to john.newdoe@example.usa.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_1001"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_sav_1002"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_1001",
                    "to_account_id": "acc_sav_1002",
                    "amount": 2500
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_1001"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Patty Gordon",
                    "account_number": "VCG552431",
                    "bank_name": "CitiBank"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "email": "john.newdoe@example.usa"
                }
            }
        ],
        "outputs": [
                "2730.50"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_043",
        "instruction": "You are Zoltan Nagy, needing to update your email address to liam.oconnornew@example.ie. First, locate your customer profile and then modify your contact details. Include Patty Gordon as a beneficiary using account number VCG552431 at CitiBank. Finally, set up a high-priority support ticket with the subject 'Billing Inquiry' and the description 'Question about monthly fees.' Ensure these tasks are completed today as they are urgent.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Liam",
                    "last_name": "O'Connor"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "email": "liam.oconnornew@example.ie"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "beneficiary_name": "Patty Gordon",
                    "account_number": "VCG552431",
                    "bank_name": "CitiBank"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                }
            }
        ],
        "outputs": [
                "Contact information updated successfully"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_044",
        "instruction": "You are Zoltan Nagy, seeking to locate all purchase transactions exceeding $100 from your checking account during July 2025. Additionally, you are considering a new car loan. For the sum of $25,000, apply for a personal loan, keeping in mind that your annual income is $4,000,000.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Alex",
                    "last_name": "Petrov"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_14001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "min_amount": 100.01,
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "ApplyForLoan",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13",
                    "loan_type": "Personal",
                    "requested_amount": 25000,
                    "purpose": "New car",
                    "annual_income": 4000000
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_045",
        "instruction": "You are Kenji Tanaka and wish to transfer $500 from your checking to your savings account. Locate your customer profile, access your accounts, and proceed with the transfer. Include Patty Gordon as a beneficiary with account number VCG552431 at CitiBank. Lastly, set up a high-priority support ticket with the subject 'Billing Inquiry' and the description 'Question about monthly fees.'.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Olivia",
                    "last_name": "Jones"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_17001",
                    "to_account_id": "acc_sav_17002",
                    "amount": 500
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "beneficiary_name": "Patty Gordon",
                    "account_number": "VCG552431",
                    "bank_name": "CitiBank"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                }
            }
        ],
        "outputs": [
                "Transfer completed successfully"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_046",
        "instruction": "You are Gabriel Silva and you aim to create a support ticket regarding a billing problem. Start by finding your customer profile and initiating a high-priority support ticket with the subject 'Billing Inquiry' and the description 'Question about monthly fees.' Include Patty Gordon as a beneficiary using account number VCG552431 at CitiBank. Following that, due to suspected fraud, freeze your checking account with ID acc_chk_22001.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Zoltan",
                    "last_name": "Nagy"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21",
                    "beneficiary_name": "Patty Gordon",
                    "account_number": "VCG552431",
                    "bank_name": "CitiBank"
                },
            },
            {
                "name": "FreezeAccount",
                "arguments": {
                    "account_id": "acc_chk_22001",
                    "reason": "Suspected fraud"
                }
            }
        ],
        "outputs": [
                "Support ticket created"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_047",
        "instruction": "As Adetokunbo Adebayor, you want to review your credit card usage and proceed with a loan application to invest in a company. Access your customer profile and determine your credit utilization across all credit cards. Subsequently, submit an application for an investment loan amounting to $1,000. Your annual income for the loan is indicated as 0. Lastly, include Patty Gordon as a beneficiary with CitiBank account number VCG552431.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Mei",
                    "last_name": "Lin"
                },
            },
            {
                "name": "CalculateCreditUtilization",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22"
                },
            },
            {
                "name": "ApplyForLoan",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "loan_type": "Investment",
                    "requested_amount": 1000,
                    "purpose": "To invest in a company",
                    "annual_income": 0
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "beneficiary_name": "Patty Gordon",
                    "account_number": "VCG552431",
                    "bank_name": "CitiBank"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_048",
        "instruction": "You are Gabriel Silva and intend to add a new beneficiary named Lisa Davis, linked to account number 9876543210 and routing number 111000025 at Bank of America. Initiate a high-priority support ticket with the subject 'Billing Inquiry' and the description 'Question about monthly fees.' Lastly, freeze your checking account due to potential hacking threats. Your checking number is acc_chk_13001.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Aisha",
                    "last_name": "Khan"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12",
                    "beneficiary_name": "Lisa Davis",
                    "account_number": "9876543210",
                    "routing_number": "111000025",
                    "bank_name": "Bank of America"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-12",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                },
            },
            {
                "name": "FreezeAccount",
                "arguments": {
                    "account_id": "acc_chk_13001",
                    "reason": "Possible hacking breeches"
                }
            }
        ],
        "outputs": [
                "Beneficiary added successfully"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_049",
        "instruction": "You are Zoltan Nagy interested in reviewing all your current loans. You are also considering obtaining a new loan to initiate a business venture. Locate your customer profile and extract all loans linked to your account. Then, apply for a loan amounting to $1,000,000, with your annual income being $250,000. Add a new beneficiary, Ben Harris, account number 34AD567, routing number 1243Df34, banking at Bank of America. Raise a support ticket requesting assistance to schedule an appointment at a branch office with a retirement planner.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "GetCustomerLoans",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                },
            },
            {
                "name": "ApplyForLoan",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "loan_type": "Business",
                    "requested_amount": 1000000,
                    "purpose": "Start a business",
                    "annual_income": 250000
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Ben Harris",
                    "account_number": "34AD567",
                    "routing_number": "1243Df34",
                    "bank_name": "Bank of America"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "subject": "setting up an apointment at a branch office with a retirement planner",
                    "description": "setting up an apointment at a branch office with a retirement planner"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_050",
        "instruction": "As Zoltan Nagy, you want to produce financial reports for both accounts and then consult a financial advisor. Access your profile, retrieve accounts, and generate financial reports for your checking and savings for June 2025. Then, initiate a new support ticket requesting a financial advisor's assistance for retirement planning. Finally, freeze your accounts to guard against potential hacking.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "GenerateFinancialReport",
                "arguments": {
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_chk_5002",
                    "month": "2025-06"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "subject": "help with retirement planning",
                    "description": "help with retirement planning"
                },
            },
            {
                "name": "FreezeAccount",
                "arguments": {
                    "account_id": "acc_sav_5001",
                    "reason": "Protect against hackers"
                },
            },
            {
                "name": "FreezeAccount",
                "arguments": {
                    "account_id": "acc_chk_5002",
                    "reason": "Protect against hackers"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_051",
        "instruction": "You are Mohammed Al-Masri intending to freeze your checking account due to suspected fraudulent activity. Access your customer profile to obtain your checking account. Add a new beneficiary named Lisa Davis with account number 9876543210 and routing number 111000025 at Bank of America. Open a high-priority support ticket with the subject 'Billing Inquiry' and the description 'Question about monthly fees.' Then, freeze your checking account, citing 'Suspected fraud' as the reason.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Gabriel",
                    "last_name": "Silva"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "beneficiary_name": "Lisa Davis",
                    "account_number": "9876543210",
                    "routing_number": "111000025",
                    "bank_name": "Bank of America"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                },
            },
            {
                "name": "FreezeAccount",
                "arguments": {
                    "account_id": "acc_chk_18001",
                    "reason": "Suspected fraud"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_052",
        "instruction": "As Kenji Tanaka, aim to assess your financial activities for June 2025. Start by locating your customer profile and accessing all your accounts. For your checking account (acc_chk_1001): 1. Identify all purchase transactions in June 2025. 2. Compute the total spending on purchases for the month. 3. Retrieve any scheduled payments executed from your checking account in June 2025. Additionally: 4. Locate any support tickets tied to your customer ID created or resolved in June 2025. 5. Refresh your contact details with a new phone number 555-321-6789. In conclusion, create a summary showing: - Total purchases from checking - Scheduled payments from checking - Support tickets involving your customer ID in June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_chk_1001",
                    "month": "2025-06"
                },
            },
            {
                "name": "GetSupportTicketsForAccount",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "phone": "555-321-6789"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_chk_1001",
                    "month": "2025-06"
                }
            }
        ],
        "outputs": [
                "Summary for Kenji Tanaka: total purchase amount, scheduled payments, and support tickets for acc_chk_1001 in June 2025."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_053",
        "instruction": "As Santiago Mu\u00f1oz, initiate a support ticket seeking assistance with an overseas payment needed by your employer. Update your contact information by adding a new phone number 555-111-2222. Incorporate Soft Solutions, LLC. as a beneficiary with account number SFGTY65466 at CitiBank. Prior to concluding, freeze your checking account acc_chk_11001 to safeguard it against hackers.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Isabella",
                    "last_name": "Rossi"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "subject": "help making a payment to a foreign country",
                    "description": "help making a payment to a foreign country as required by my employer."
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "phone": "555-111-2222"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "beneficiary_name": "Soft Solutions, LLC.",
                    "account_number": "SFGTY65466",
                    "bank_name": "CitiBank"
                },
            },
            {
                "name": "FreezeAccount",
                "arguments": {
                    "account_id": "acc_chk_11001",
                    "reason": "Protect from hackers"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_054",
        "instruction": "Being Sofia Andersson, you wish to gather specifics regarding a particular transaction. Access your customer profile and obtain details for transaction ID txn_4e5f6a7b-8c9d-0e1f-2a3b-4c5d6e7f8g9h. Subsequently, include your customer support representative Zoltan Nagy as a beneficiary. Search for his by name. He banks at India National Bank with the account number IN3456789012. Generate a high-priority support ticket with the subject 'Billing Inquiry' and a description 'Question about monthly fees'. Before leaving, amend your customer contact phone number to 555-321-6789.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Kim"
                },
            },
            {
                "name": "GetTransactionDetails",
                "arguments": {
                    "transaction_id": "txn_4e5f6a7b-8c9d-0e1f-2a3b-4c5d6e7f8g9h"
                },
            },
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "beneficiary_name": "Zoltan Nagy",
                    "account_number": "IN3456789012",
                    "bank_name": "India National Bank"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "phone": "555-321-6789"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_055",
        "instruction": "As Oliver Williams, your goal is to compute your monthly expenses for July 2025 on your checking account. Furthermore, add Zoltan Nagy as your beneficiary. His account number is IN3456789012 with India National Bank. Create a high-priority support ticket with the subject 'Billing Inquiry' and description 'Question about monthly fees'. Before departing, revise your customer contact phone number to 555-321-6789.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Adetokunbo",
                    "last_name": "Adebayor"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"
                },
            },
            {
                "name": "CalculateMonthlySpending",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "month": 7,
                    "year": 2025
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "beneficiary_name": "Zoltan Nagy",
                    "account_number": "IN3456789012",
                    "bank_name": "India National Bank"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "phone": "555-321-6789"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_056",
        "instruction": "Acting as Santiago Mu\u00f1oz, you wish to revise your phone number to 555-987-6543. Locate your customer profile and update your contact details. You are keen on obtaining a loan for personal expenditures. Apply for a new $10,000 loan. Your annual income stands at $40,000. Produce a monthly report for your checking account acc_chk_19001 for July. Generate a high-priority support ticket with the subject 'Loan Inquiry' and description 'Question about a loan'.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Anja",
                    "last_name": "Novak"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "phone": "555-987-6543"
                },
            },
            {
                "name": "ApplyForLoan",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "loan_type": "Personal",
                    "requested_amount": 10000,
                    "purpose": "Personal spending",
                    "annual_income": 40000
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_chk_19001",
                    "month": "2025-07"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "subject": "Loan Inquiry",
                    "description": "Question about a loan",
                    "priority": "High"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_057",
        "instruction": "As Gabriel Silva, conduct a search for customers using emails with the domain dupont.fr. Additionally, include Marie Dubois as a beneficiary; her IBAN is FR7630006000011234567890189, and her bank is BNP Paribas. Initiate a high-priority support ticket titled 'Billing Inquiry' with the description 'Question about monthly fees.' Modify your phone contact to 415-667-9999 and update your email to newegg@aol.com.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Zoltan",
                    "last_name": "Nagy"
                },
            },
            {
                "name": "SearchCustomersByEmail",
                "arguments": {
                    "email_domain": "dupont.fr"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21",
                    "beneficiary_name": "Marie Dubois",
                    "iban": "FR7630006000011234567890189",
                    "bank_name": "BNP Paribas"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21",
                    "subject": "Billing Inquiry",
                    "description": "Question about monthly fees",
                    "priority": "High"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-21",
                    "phone": "415-667-9999",
                    "email": "newegg@aol.com"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_058",
        "instruction": "Being Adetokunbo Adebayor, access your support tickets. Locate your customer profile and obtain all your support tickets records. Next, add Manchester Electricity Co. as a beneficiary, with the account number 12345678 and the bank Barclays. Generate a support ticket inquiring about tracking beneficiary activity through the mobile app.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Mei",
                    "last_name": "Lin"
                },
            },
            {
                "name": "GetCustomerSupportTickets",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "beneficiary_name": "London Electricity Co.",
                    "account_number": "12345678",
                    "bank_name": "Barclays"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-22",
                    "subject": "tracking beneficiary activity on the mobile app",
                    "description": "asking how to track beneficiary activity on the mobile app"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_059",
        "instruction": "As Oliver Williams, compute the total deposits into your savings account for June 2025. Follow this by creating a support ticket concerning bugs in the mobile app. Proceed to register Manchester Electricity Co. as a beneficiary, with account number 12345678 at Barclays. Move $50 from your checking to savings account. Subsequently, add Nana Piccao as another beneficiary with account number 46746fd45 at the Bank of Egypt.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Adetokunbo",
                    "last_name": "Adebayor"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_sav_24002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "subject": "Bugs In Mobile App",
                    "description": "Bugs In Mobile App"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "beneficiary_name": "London Electricity Co.",
                    "account_number": "12345678",
                    "bank_name": "Barclays"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_24001",
                    "to_account_id": "acc_sav_24002",
                    "amount": 50
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "beneficiary_name": "Nana Piccao",
                    "account_number": "46746fd45",
                    "bank_name": "Bank of Egypt"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_060",
        "instruction": "While acting as Lakshmi Narayanan, determine the total withdrawals from your savings account for July 2025. Next, generate a support ticket for assistance with understanding loan applications. Include Nana Piccao as a new beneficiary, with account number 46746fd45 at the Bank of Egypt. Update your phone number to 415-445-1212 and your email to fastapi@aol.com. Lastly, produce an account statement for savings in June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Elena",
                    "last_name": "Popescu"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24"
                },
            },
            {
                "name": "CalculateTotalWithdrawal",
                "arguments": {
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "subject": "Understanding loan applications",
                    "description": "Needs help understanding loan applications"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "beneficiary_name": "Nana Piccao",
                    "account_number": "46746fd45",
                    "bank_name": "Bank of Egypt"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "phone": "415-445-1212",
                    "email": "fastapi@aol.com"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_sav_25001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_061",
        "instruction": "As Isabella Rossi, create an account statement for your checking account for June 2025. Add ATX, Inc. as a beneficiary using the account number A23d45fg at Barclays. Submit a customer support ticket requesting help with adding a backup email to your account. Update your phone number to 415-1234-8888 and change your email to slowapi@aol.com.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Mohammed",
                    "last_name": "Al-Masri"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_chk_26001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "beneficiary_name": "ATX, Inc.",
                    "account_number": "A23d45fg",
                    "bank_name": "Barclays"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "subject": "Help adding a backup email",
                    "description": "Help adding a backup email"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "phone": "415-1234-8888",
                    "email": "slowapi@aol.com"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_062",
        "instruction": "As Kenji Tanaka, seek out withdrawal transactions from your checking account and compute the total amount for July 2025. Following that, initiate a customer support ticket requesting assistance for adding a backup email to your account.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "transaction_type": "Withdrawal"
                },
            },
            {
                "name": "CalculateTotalWithdrawal",
                "arguments": {
                    "account_id": "acc_chk_1001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "subject": "Help adding a backup email",
                    "description": "Help adding a backup email"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_063",
        "instruction": "As Elena Popescu, locate deposit transactions in your savings account for June 2025 and calculate the total. Consult customer support for assistance with setting up automated notifications on your mobile app. Afterward, move $500 from your checking account into your savings.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_sav_2002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_sav_2002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "subject": "setting up automated notifications",
                    "description": "setting up automated notifications"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_2001",
                    "to_account_id": "acc_sav_2002",
                    "amount": 500
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_064",
        "instruction": "Identify yourself as Zoltan Nagy and update your email to david.chen.updated@email.com, and also verify your checking account balance. Move $1,000 from your checking to investment account. Add Anna O'Connor as a beneficiary using account number 6754FG6894 at the Bank of Cork. Finally, include Kenji Tanaka as a beneficiary with account number As234fdg and routing number 126579823. His bank is City National Bank.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "email": "david.chen.updated@email.com"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_3001"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_3001",
                    "to_account_id": "acc_inv_3002",
                    "amount": 1000
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Anna O'Connor",
                    "account_number": "6754FG6894",
                    "bank_name": "Bank of Dublin"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Kenji Tanaka",
                    "account_number": "As234fdg",
                    "routing_number": "126579823",
                    "bank_name": "City National Bank"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_065",
        "instruction": "Assuming the identity of Sofia Andersson, inspect purchase transactions over $250 from your checking account in July 2025. Then, freeze your account as a precautionary measure against suspected hackers.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "min_amount": 250.01,
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "FreezeAccount",
                "arguments": {
                    "account_id": "acc_chk_4001",
                    "reason": "Suspected hackers"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_066",
        "instruction": "As Zoltan Nagy, prepare a monthly account summary for your savings account for July 2025. Having relocated for a job, update your phone contact to 415-921-6543. Then, add Lisa Davis as a new beneficiary with account number 9876543210, routing number 111000025, banking with Bank of America. Additionally, add BMX Trips, LLC. as a beneficiary with account number CDF456378 banking with Barclays.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_sav_5001",
                    "month": "2025-07"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "phone": "415-921-6543"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "Lisa Davis",
                    "account_number": "9876543210",
                    "routing_number": "111000025",
                    "bank_name": "Bank of America"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "BMX Trips, LLC.",
                    "account_number": "CDF456378",
                    "bank_name": "Barclays"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_067",
        "instruction": "Your name is Sofia Andersson and you wish to open a support ticket concerning account access problems. Start a medium priority ticket titled 'Account Access' and include the description 'Unable to login to online banking'.Add Kenji Tanaka as a beneficiary with account number As234fdg and routing number 126579823.His bank is City National BankChange your phone number to 552-345-6111.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Williams"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "subject": "Account Access",
                    "description": "Unable to login to online banking",
                    "priority": "Medium"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_name": "Kenji Tanaka",
                    "account_number": "As234fdg",
                    "routing_number": "126579823",
                    "bank_name": "City National Bank"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "phone": "552-345-6111"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_068",
        "instruction": "You are Oliver Williams, and aim to calculate the total ATM withdrawals from your checking account for June 2025.Next, you need to transfer $200 from your savings to your checking.Finally, compute your checking balance.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Fatima",
                    "last_name": "Al-Fassi"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"
                },
            },
            {
                "name": "CalculateTotalAtmWithdrawals",
                "arguments": {
                    "account_id": "acc_chk_7001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_sav_7002",
                    "to_account_id": "acc_chk_7001",
                    "amount": 200
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_7001"
                }
            }
        ],
        "outputs": [
                "150200"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_069",
        "instruction": "Your name is Chloe Dubois and you're interested in verifying any scheduled payments from your checking account for August 2025. Next, you should move $1000 from your savings acc_sav_8002 to your checking acc_chk_8001. Then include Lisa Davis as a new beneficiary with account number 9876543210, routing number 111000025, and associated with Bank of America. Apply for a $10,000 personal loan to assist in financing your car mechanic hobbies; your annual income stands at $95,000.Before concluding, determine your checking balance.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Hans",
                    "last_name": "Müller"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "source_account_id": "acc_chk_8001",
                    "month": "2025-08"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_sav_8002",
                    "to_account_id": "acc_chk_8001",
                    "amount": 1000
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "beneficiary_name": "Lisa Davis",
                    "account_number": "9876543210",
                    "routing_number": "111000025",
                    "bank_name": "Bank of America"
                },
            },
            {
                "name": "ApplyForLoan",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "loan_type": "Personal",
                    "requested_amount": 10000,
                    "purpose": "Car mechanic hobbies",
                    "annual_income": 95000
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_8001"
                }
            }
        ],
        "outputs": [
                8800.5
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_070",
        "instruction": "You are Kenji Tanaka and intend to look up all transactions from your checking account between June 1-15, 2025.Next, you will need to send your friend Adetokunbo Adebayor $150 as a gift from your checking.Kenji's account number is acc_chk_10001.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Dubois"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_9001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-15T23:59:59Z"
                },
            },
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Kenji",
                    "last_name": "Tanaka"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_9001",
                    "to_account_id": "acc_chk_10001",
                    "amount": 150
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_071",
        "instruction": "You are Adetokunbo Adebayor and you're reviewing your checking account activity for July 2025. Locate your customer profile, retrieve your checking account, find all purchase transactions in July 2025, and calculate the total spent on purchases.Finally, you need to transfer $50 from your checking to your savings.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Kenji",
                    "last_name": "Tanaka"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_10001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_10001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_10001",
                    "to_account_id": "acc_sav_10002",
                    "amount": 50
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_072",
        "instruction": "As Santiago Mu\u00f1oz, you intend to transfer money and modify your contact information. Locate your customer profile, move $150 from your checking account to Zoltan Nagy's checking acc_chk_12001, and change your email to isabella.rossi.new@email.com. Include BMX Trips, LLC. as a beneficiary with account number CDF456378 and banking with Barclays. Next, set up a support ticket for a review of your checking account.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Isabella",
                    "last_name": "Rossi"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_11001",
                    "to_account_id": "acc_chk_12001",
                    "amount": 150
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "email": "isabella.rossi.new@email.com"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "beneficiary_name": "BMX Trips, LLC.",
                    "account_number": "CDF456378",
                    "bank_name": "Barclays"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "subject": "Checking account review",
                    "description": "Checking account review"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_073",
        "instruction": "Zoltan Nagy wishes to examine deposits to his checking account. Locate your profile, access your checking account, look for deposits in June 2025, determine the total deposits, and produce a monthly summary. Subsequently, add your sister Anna O'Connor as a beneficiary with account number 6754FG6894 at the Bank of Cork.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Liam",
                    "last_name": "O'Connor"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_12001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_chk_12001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_chk_12001",
                    "month": "2025-06"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "beneficiary_name": "Anna O'Connor",
                    "account_number": "6754FG6894",
                    "bank_name": "Bank of Dublin"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_074",
        "instruction": "As Elena Popescu, your goal is to assemble a summary of all incoming payments to your checking account from the previous month. Begin by locating your customer profile, retrieve your checking account, and locate every incoming transaction in June 2025. Set up a support ticket for your account review. Afterwards, prepare a statement for June 2025 for your checking account and count the total number of incoming transactions.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Santiago",
                    "last_name": "Muñoz"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_20001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19",
                    "subject": "Account review",
                    "description": "Account review"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_chk_20001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_075",
        "instruction": "Zoltan Nagy aims to assess his loan status and process a payment. Find your profile, access your loans, and execute a $300 loan payment from your checking account.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Alex",
                    "last_name": "Petrov"
                },
            },
            {
                "name": "GetCustomerLoans",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"
                },
            },
            {
                "name": "ProcessLoanPayment",
                "arguments": {
                    "loan_id": "loan_auto_007",
                    "payment_amount": 300,
                    "from_account_id": "acc_chk_14001"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_076",
        "instruction": "Chloe Dubois needs to review support tickets and create a new one. Access your profile, review existing support tickets, then establish a new ticket about card replacement with high priority and description 'Lost credit card, need replacement'. Add Elena Popescu as a new beneficiary with account number 9876543210, routing number 122000661, at City National Bank. Conclude by updating your email contact to fasttrack@email.com.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Sofia",
                    "last_name": "Andersson"
                },
            },
            {
                "name": "GetCustomerSupportTickets",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "subject": "Card Replacement",
                    "description": "Lost credit card, need replacement",
                    "priority": "High"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "beneficiary_name": "Elena Popescu",
                    "account_number": "9876543210",
                    "routing_number": "122000661",
                    "bank_name": "City National Bank"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-14",
                    "email": "fasttrack@email.com"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_077",
        "instruction": "Identify yourself as Sofia Andersson and aim to assess expenses and review credit usage. Locate your profile, compute July 2025 monthly spending on your checking account, and verify your credit card usage. Afterward, update your account email to new.noah.kim@hotmail.com. Include Elena Popescu as a beneficiary with account number 9876543210, routing number 122000661, at City National Bank. Additionally, incorporate BMX Trips, LLC. as a beneficiary with account number CDF456378 and their banking institution as Barclays.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Kim"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15"
                },
            },
            {
                "name": "CalculateMonthlySpending",
                "arguments": {
                    "account_id": "acc_chk_16001",
                    "month": 7,
                    "year": 2025
                },
            },
            {
                "name": "CalculateCreditUtilization",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "email": "new.noah.kim@hotmail.com"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "beneficiary_name": "Elena Popescu",
                    "account_number": "9876543210",
                    "routing_number": "122000661",
                    "bank_name": "City National Bank"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "beneficiary_name": "BMX Trips, LLC.",
                    "account_number": "CDF456378",
                    "bank_name": "Barclays"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_078",
        "instruction": "Recognize yourself as Kenji Tanaka and intend to create financial reports for both your accounts, then seek assistance from a financial advisor. Find your profile, access accounts, and generate financial reports for both the checking and savings accounts for June 2025. Following that, open a new support ticket requesting a financial advisor's help with retirement planning. Conclude by freezing your accounts to safeguard against hacking threats.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Olivia",
                    "last_name": "Jones"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16"
                },
            },
            {
                "name": "GenerateFinancialReport",
                "arguments": {
                    "account_id": "acc_chk_17001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_sav_17002",
                    "month": "2025-06"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "subject": "help with retirement planning",
                    "description": "help with retirement planning"
                },
            },
            {
                "name": "FreezeAccount",
                "arguments": {
                    "account_id": "acc_chk_17001",
                    "reason": "Protect against hackers"
                },
            },
            {
                "name": "FreezeAccount",
                "arguments": {
                    "account_id": "acc_sav_17002",
                    "reason": "Protect against hackers"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_079",
        "instruction": "Identify yourself as Mohammed Al-Masri with the aim to review upcoming payments from your checking account and refresh contact details. The account reference is acc_chk_18001. Access your profile, inspect scheduled payments for July 2025 from your checking account, and update your phone number to 555-234-5678. Add Elena Popescu as a beneficiary with account number 9876543210, routing number 122000661, at City National Bank. Also, include BMX Trips, LLC. as a beneficiary with account number CDF456378, with Barclays as the banking partner.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Gabriel",
                    "last_name": "Silva"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "source_account_id": "acc_chk_18001",
                    "month": "2025-07"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "phone": "555-234-5678"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "beneficiary_name": "Elena Popescu",
                    "account_number": "9876543210",
                    "routing_number": "122000661",
                    "bank_name": "City National Bank"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-17",
                    "beneficiary_name": "BMX Trips, LLC.",
                    "account_number": "CDF456378",
                    "bank_name": "Barclays"
                }
            }
        ],
        "outputs": [
                "Scheduled payments reviewed, contact updated"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_080",
        "instruction": "You are Elena Popescu; locate your profile, and search for any deposits more than $1000 in your savings for June 2025. Then, transfer $100 from checking into savings. Initiate a support ticket to enable automated notifications on the mobile app. Finally, acquire a financial report for your checking account for June.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_sav_2002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 1000.01,
                    "transaction_type": "Deposit"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_2001",
                    "to_account_id": "acc_sav_2002",
                    "amount": 100
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "subject": "setting up automated notifications",
                    "description": "setting up automated notifications"
                },
            },
            {
                "name": "GenerateFinancialReport",
                "arguments": {
                    "account_id": "acc_chk_2001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_081",
        "instruction": "Identify as Elena Popescu with objectives to scrutinize account activity and initiate a support ticket. Access your profile, retrieve the account for the last 10 transactions, determine the account balance, and file a support ticket today regarding transaction fee concerns.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Santiago",
                    "last_name": "Muñoz"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"
                },
            },
            {
                "name": "GetAccountTransactions",
                "arguments": {
                    "account_id": "acc_chk_20001",
                    "limit": 10
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_20001"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19",
                    "subject": "Transaction Fees",
                    "description": "Questions about recent transaction fees"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_082",
        "instruction": "Being Isabella Rossi, focus on tasks related to beneficiaries and payments. Locate your profile, retrieve all beneficiaries, confirm routing number 111000025, and inspect your scheduled payments for August 2025 from your checking account acc_chk_21001. Afterward, initiate a support ticket to request assistance with adding beneficiaries and understand the information required for that process.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Yara",
                    "last_name": "Haddad"
                },
            },
            {
                "name": "GetCustomerBeneficiaries",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20"
                },
            },
            {
                "name": "ValidateRoutingNumber",
                "arguments": {
                    "routing_number": "111000025"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "source_account_id": "acc_chk_21001",
                    "month": "2025-08"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "subject": "help adding beneficiaries and info required",
                    "description": "help adding beneficiaries and info required"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_083",
        "instruction": "As Oliver Williams, prioritize reviewing your spending and deposits. Start by finding your profile, total up all purchases from your checking account in July 2025, sum up deposits to your savings in the same month, and create an account statement for your checking. Follow this by transferring $1000 from your checking account to your savings.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Adetokunbo",
                    "last_name": "Adebayor"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_sav_24002",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_24001",
                    "to_account_id": "acc_sav_24002",
                    "amount": 1000
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_084",
        "instruction": "Assuming the role of Elena Popescu, your focus is on managing loans and transfers. Begin by locating your profile, then review your customer loans, and transfer $400 from checking to savings as part of your savings routine. Subsequently, compute your monthly expenditure for June 2025.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "GetCustomerLoans",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_2001",
                    "to_account_id": "acc_sav_2002",
                    "amount": 400,
                    "description": "Regular savings routine"
                },
            },
            {
                "name": "CalculateMonthlySpending",
                "arguments": {
                    "account_id": "acc_chk_2001",
                    "month": 6,
                    "year": 2025
                }
            }
        ],
        "outputs": [
                "Loans reviewed, transfer completed, spending calculated"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_085",
        "instruction": "As Zoltan Nagy, your task is to search transactions and ensure account security. First, find your profile, then look for withdrawal transactions exceeding $500 in June 2025, calculate the total withdrawals, and freeze your account if any suspicious activities are detected.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 500.01,
                    "transaction_type": "Withdrawal"
                },
            },
            {
                "name": "CalculateTotalWithdrawal",
                "arguments": {
                    "account_id": "acc_chk_3001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "FreezeAccount",
                "arguments": {
                    "account_id": "acc_chk_3001",
                    "reason": "Suspicious activity detected"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_086",
        "instruction": "Taking on the role of Sofia Andersson, concentrate on reviewing credit and payments. First, locate your profile, compute your credit utilization, access the most recent transactions (last 8), and calculate total bill payments for July 2025. Before concluding, add Kenji Tanaka as a beneficiary, providing his account number As234fdg and routing number 126579823. His bank is City National Bank.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "CalculateCreditUtilization",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"
                },
            },
            {
                "name": "GetAccountTransactions",
                "arguments": {
                    "account_id": "acc_chk_4001",
                    "limit": 8
                },
            },
            {
                "name": "CalculateTotalBillPayments",
                "arguments": {
                    "account_id": "acc_chk_4001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "beneficiary_name": "Kenji Tanaka",
                    "account_number": "As234fdg",
                    "routing_number": "126579823",
                    "bank_name": "City National Bank"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_087",
        "instruction": "You are Zoltan Nagy and seek to manage account statements and obtain support. Locate your profile, produce an account statement for your savings account acc_sav_5001 for June 2025, retrieve your support tickets, and initiate a new ticket inquiring about how to apply for a new loan.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_sav_5001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "GetCustomerSupportTickets",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "subject": "Apply for new loan",
                    "description": "how to apply for a new loan"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_088",
        "instruction": "You are Oliver Williams and aim to thoroughly review checking payments and saving deposits. Locate your profile, determine total payments for June 2025, determine total deposits for June 2025, retrieve scheduled payments for July 2025 directed to checkings, and compile a monthly summary for checkings. Add Zoltan Nagy as a new beneficiary for his medical services for July 2025. His account number is B4FD12345, routing number is 987123, and his bank is Bank of Bahamas.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Fatima",
                    "last_name": "Al-Fassi"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"
                },
            },
            {
                "name": "CalculateTotalPayments",
                "arguments": {
                    "account_id": "acc_chk_7001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_sav_7002",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "source_account_id": "acc_chk_7001",
                    "month": "2025-07"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_chk_7001",
                    "month": "2025-06"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "beneficiary_name": "Zoltan Nagy",
                    "account_number": "B4FD12345",
                    "routing_number": "987123",
                    "bank_name": "Bank of Bahamas"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_089",
        "instruction": "You are Kenji Tanaka and intend to transfer $50 from your checking account to your savings account. You need to confirm your current balances before and after the transfer. After executing the transfer, inform me of your new checking account balance.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_1001"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_sav_1002"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_1001",
                    "to_account_id": "acc_sav_1002",
                    "amount": 50
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_1001"
                }
            }
        ],
        "outputs": [
                "5180.50"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_090",
        "instruction": "You are Chloe Dubois and wish to evaluate account activity and manage transactions. Locate your profile, search for purchase and deposit transactions in July 2025, compute combined spending, and prepare a detailed monthly report. Then, initiate a support ticket today to acquire assistance with setting up automated payments to your utility provider.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Hans",
                    "last_name": "Müller"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"
                },
            },
            {
                "name": "CalculateTotalEventAndPurchaseSpending",
                "arguments": {
                    "account_id": "acc_chk_8001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_sav_8002",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                },
            },
            {
                "name": "GenerateDetailedMonthlyReport",
                "arguments": {
                    "account_id": "acc_chk_8001",
                    "month": "2025-07"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "subject": "setting up automated payments",
                    "description": "setting up automated payments to your utility provider"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_091",
        "instruction": "You are Isabella Rossi and need to inspect your checking account for payments over $200 made in June. Begin by finding your customer profile. Access your checking account. Search for all transactions over $200 in June 2025. Create a support ticket regarding your payment review. Then, compile a statement for your checking account for June 2025 and report the number of transactions exceeding $200.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Mohammed",
                    "last_name": "Al-Masri"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_26001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "min_amount": 200
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-25",
                    "subject": "Payment review",
                    "description": "Payment review"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_chk_26001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_092",
        "instruction": "You are Adetokunbo Adebayor and wish to oversee loans and scheduled payments. Locate your profile, access loan applications, and obtain scheduled payments for August 2025 on your checking with acc_chk_10001. Additionally, update phone number to 555-345-6789.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Kenji",
                    "last_name": "Tanaka"
                },
            },
            {
                "name": "GetLoanApplicationsForCustomer",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3"
                },
            },
            {
                "name": "RetrieveScheduledPayments",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "source_account_id": "acc_chk_10001",
                    "month": "2025-08"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "phone": "555-345-6789"
                }
            }
        ],
        "outputs": [
                "Loan applications reviewed, scheduled payments checked, contact updated"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_093",
        "instruction": "You are Santiago Mu\u00f1oz needing to examine deposits and purchases. Locate your profile, compute total deposits and purchases for your accounts in June 2025, and produce account statements for checkings. Then initiate a support ticket to inquire about credit card deals.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Isabella",
                    "last_name": "Rossi"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10"
                },
            },
            {
                "name": "CalculateTotalDepositsAndPurchases",
                "arguments": {
                    "account_id": "acc_chk_11001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "GenerateAccountStatement",
                "arguments": {
                    "account_id": "acc_chk_11001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-10",
                    "subject": "finding more about credit card deals",
                    "description": "finding more about credit card deals"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_094",
        "instruction": "You are Zoltan Nagy and aim to control account access and inspect activity. Initially find your profile. Search customers by email domain yahoo.com, retrieve your checking account balance, and file a support ticket regarding online access issues with a description on inability to access the mobile banking app. Next, add Lisa Davis as a new beneficiary with account number 9876543210, routing number 111000025, who banks with Bank of America. Consequently, freeze your checking account to shield it from potential fraud.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Liam",
                    "last_name": "O'Connor"
                },
            },
            {
                "name": "SearchCustomersByEmail",
                "arguments": {
                    "email_domain": "yahoo.com"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_12001"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "subject": "Online Access Issues",
                    "description": "Cannot access mobile the banking app"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "beneficiary_name": "Lisa Davis",
                    "account_number": "9876543210",
                    "routing_number": "111000025",
                    "bank_name": "Bank of America"
                },
            },
            {
                "name": "FreezeAccount",
                "arguments": {
                    "account_id": "acc_chk_12001",
                    "reason": "Protect from possible fraud"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_095",
        "instruction": "You are Zoltan Nagy and intend to conduct a complete account review. Identify your profile, retrieve recent transactions (last 12) from your checking account acc_chk_14001, inspect credit utilization, and produce a monthly summary for July 2025 for your checking account. Then add Lisa Davis as a new beneficiary with account number 9876543210, routing number 111000025, with Bank of America. Finally, initiate a support ticket requesting assistance with adding more beneficiaries.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Alex",
                    "last_name": "Petrov"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"
                },
            },
            {
                "name": "GetAccountTransactions",
                "arguments": {
                    "account_id": "acc_chk_14001",
                    "limit": 12
                },
            },
            {
                "name": "CalculateCreditUtilization",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13"
                },
            },
            {
                "name": "GenerateMonthlyAccountSummary",
                "arguments": {
                    "account_id": "acc_chk_14001",
                    "month": "2025-07"
                },
            },
            {
                "name": "AddBeneficiary",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13",
                    "beneficiary_name": "Lisa Davis",
                    "account_number": "9876543210",
                    "routing_number": "111000025",
                    "bank_name": "Bank of America"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-13",
                    "subject": "asking for help with how to add more beneficiaries",
                    "description": "asking for help with how to add more beneficiaries"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_096",
        "instruction": "You are Kenji Tanaka and intend to transfer $3000 from your checking account to your savings account. Confirm your current balances before and after the transfer. After transferring, update me on your new checking account balance.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_1001"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_sav_1002"
                },
            },
            {
                "name": "TransferFunds",
                "arguments": {
                    "from_account_id": "acc_chk_1001",
                    "to_account_id": "acc_sav_1002",
                    "amount": 3000
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_1001"
                }
            }
        ],
        "outputs": [
                "2230.50"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_097",
        "instruction": "As Santiago Mu\u00f1oz, you need to assess spending patterns and your account status. Locate your profile, identify purchase transactions exceeding $200 in July 2025 within your checking account acc_chk_19001, calculate the monthly spending for July 2025, and retrieve support tickets currently marked as Open. Furthermore, you need to secure a loan for your upcoming vacation. Proceed with applying for a personal loan of $3,000. Your annual income is 40000.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Anja",
                    "last_name": "Novak"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_19001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z",
                    "min_amount": 200.01,
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "CalculateMonthlySpending",
                "arguments": {
                    "account_id": "acc_chk_19001",
                    "month": 7,
                    "year": 2025
                },
            },
            {
                "name": "GetCustomerSupportTickets",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "status": "Open"
                },
            },
            {
                "name": "ApplyForLoan",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "loan_type": "Personal",
                    "requested_amount": 3000,
                    "purpose": "Vacation",
                    "annual_income": 40000
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_098",
        "instruction": "As Elena Popescu, you intend to carry out a thorough financial review. Access your profile, compute the total expenditure for June 2025 on your checking account acc_chk_20001, acquire information on customer loans, determine the account balance for that account, and prepare a financial report for June 2025. Due to concerns about a recent data breach, you wish to freeze your account for security.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Santiago",
                    "last_name": "Muñoz"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"
                },
            },
            {
                "name": "CalculateTotalExpenditure",
                "arguments": {
                    "account_id": "acc_chk_20001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z",
                    "transaction_type": "Purchase"
                },
            },
            {
                "name": "GetCustomerLoans",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1-19"
                },
            },
            {
                "name": "CalculateAccountBalance",
                "arguments": {
                    "account_id": "acc_chk_20001"
                },
            },
            {
                "name": "GenerateFinancialReport",
                "arguments": {
                    "account_id": "acc_chk_20001",
                    "start_date": "2025-06-01T00:00:00Z",
                    "end_date": "2025-06-30T23:59:59Z"
                },
            },
            {
                "name": "FreezeAccount",
                "arguments": {
                    "account_id": "acc_chk_20001",
                    "reason": "Data break and safety"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_099",
        "instruction": "You are Isabella Rossi and aim to adjust account settings and manage payments. Access your profile, update your email to yara.haddad.new@email.com, list all beneficiaries, and cancel a scheduled payment identified by payment ID sp_c7k9b8j1-i5j4-k3l2-m1n0-o9p8q7r6s5t4 as it is no longer required.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Yara",
                    "last_name": "Haddad"
                },
            },
            {
                "name": "UpdateCustomerContact",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "email": "yara.haddad.new@email.com"
                },
            },
            {
                "name": "GetCustomerBeneficiaries",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20"
                },
            },
            {
                "name": "CancelScheduledPayment",
                "arguments": {
                    "payment_id": "sp_c7k9b8j1-i5j4-k3l2-m1n0-o9p8q7r6s5t4",
                    "reason": "No longer needed"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "BANK_100",
        "instruction": "As Oliver Williams, you plan to execute a comprehensive account analysis. Locate your profile, look up all types of transactions in July 2025 on your checking account acc_chk_24001, compute total deposits for savings account acc_sav_24002 and withdrawals for the checking account, develop a detailed monthly report for the checking account, and initiate a low priority support ticket with the subject 'Account Review Completed' and description 'Comprehensive account analysis finished for July 2025'.",
        "actions": [
            {
                "name": "FindCustomerByName",
                "arguments": {
                    "first_name": "Adetokunbo",
                    "last_name": "Adebayor"
                },
            },
            {
                "name": "GetCustomerAccounts",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"
                },
            },
            {
                "name": "SearchTransactions",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                },
            },
            {
                "name": "CalculateTotalDeposits",
                "arguments": {
                    "account_id": "acc_sav_24002",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                },
            },
            {
                "name": "CalculateTotalWithdrawal",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "start_date": "2025-07-01T00:00:00Z",
                    "end_date": "2025-07-31T23:59:59Z"
                },
            },
            {
                "name": "GenerateDetailedMonthlyReport",
                "arguments": {
                    "account_id": "acc_chk_24001",
                    "month": "2025-07"
                },
            },
            {
                "name": "CreateSupportTicket",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "subject": "Account Review Completed",
                    "description": "Comprehensive account analysis finished for July 2025",
                    "priority": "Low"
                }
            }
        ],
        "outputs": [
                "0"
        ]
    }
]
