
tasks = [
    {
        "annotator": 0,
        "user_id": "task_01",
        "instruction": "Handle the opening of a new Savings account as Kenji Tanaka, followed by transferring USD\u00a0500 from your current Checking account into it.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Savings"
                },
            },
            {
                "name": "CreateNewAccountForCustomer",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Savings",
                    "account_type_code": "sav",
                    "currency": "USD"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Savings"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_id": "acc_chk_1001",
                    "requested_amount": 500.0
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_chk_1001",
                    "target_account_id": "acc_1",
                    "currency": "USD",
                    "amount": 500.0
                }
            }
        ],
        "outputs": [
                "\"message\": \"Transfer successful (same currency).\",\"source_account_id\": \"acc_chk_1001\",\"target_account_id\": \"acc_1\",\"amount_transferred\": 500.0,\"currency\": \"USD\",\"source_balance\": 4730.50,\"target_balance\": 500.0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_02",
        "instruction": "Coordinate a transfer of CAD 250 from your Checking account to your personal beneficiary, Kenji Tanaka, as Elena Popescu.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Checking"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_id": "acc_chk_2001",
                    "requested_amount": 250.0
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_name": "Kenji Tanaka"
                },
            },
            {
                "name": "GetCurrencyConversionAmount",
                "arguments": {
                    "source_currency": "CAD",
                    "source_amount": 250.0,
                    "target_currency": "USD"
                },
            },
            {
                "name": "PayToBeneficiaryWithConversion",
                "arguments": {
                    "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f",
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "source_account_id": "acc_chk_2001",
                    "source_amount": 250.0,
                    "source_currency": "CAD",
                    "target_currency": "USD"
                }
            }
        ],
        "outputs": [
                "\"message\": \"Paid 200.00 USD to beneficiary 'Kenji Tanaka'.\", \"source_account_id\": \"acc_chk_2001\", \"beneficiary_account_number\": \"1122334455\", \"source_amount\": 250.0, \"source_currency\": \"CAD\", \"target_amount\": 200.0, \"target_currency\": \"USD\", \"new_source_balance\": 2850.75\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_03",
        "instruction": "As Sofia Andersson, schedule a monthly GBP\u00a0100 payment beginning next month on the date 2025-08-24 from your Checking account to your business beneficiary, Manchester Electricity Co.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Williams"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_name": "London Electricity Co."
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_id": "acc_chk_6001",
                    "requested_amount": 100.0
                },
            },
            {
                "name": "CreateNewSchedulePayment",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "source_account_id": "acc_chk_6001",
                    "beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d",
                    "amount": 100.0,
                    "currency": "GBP",
                    "frequency": "Monthly",
                    "start_date": "2025-08-24"
                }
            }
        ],
        "outputs": [
                "\"payment_id\": \"sp_1\", \"customer_id\": \"b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5\", \"source_account_id\": \"acc_chk_6001\", \"beneficiary_id\": \"bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d\", \"amount\": 100.0, \"currency\": \"GBP\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"next_payment_date\": \"2025-09-24\", \"end_date\": null, \"status\": \"Active\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_04",
        "instruction": "David Chen, proceed with applying for a home improvement personal loan of USD 5,000 over 24 months, using your property located at address '123 Maple Street, Springfield' as collateral.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "loan_type": "Personal",
                    "requested_amount": 5000.0,
                    "requested_term_months": 24,
                    "purpose": "Home improvement"
                },
            },
            {
                "name": "ProcessLoanApplicationId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "application_id": "app_1"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "loan_type": "Personal"
                },
            },
            {
                "name": "AddNewLoanForCustomer",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "application_id": "app_1",
                    "collateral_type": "Property",
                    "collateral_info": "123 Maple Street, Springfield",
                    "currency": "USD"
                }
            }
        ],
        "outputs": [
                "\"loan_id\": \"loan_1\",\"loan_account_id\": \"loanacc_1\" \"application_id\": \"app_1\", \"status\": \"Approved\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_05",
        "instruction": "Arrange to pay USD\u00a0500 from your Savings account to your Credit Card account as Kenji Tanaka, and subsequently verify the balances in your Checking, Savings, and Credit Card accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_sav_1002",
                    "target_account_id": "acc_crd_1003",
                    "currency": "USD",
                    "amount": 500.0
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Savings"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Credit Card"
                }
            }
        ],
        "outputs": [
                "\"message\": \"Transfer successful (same currency).\",\"source_account_id\": \"acc_sav_1002\",\"target_account_id\": \"acc_crd_1003\",\"amount_transferred\": 500.0,\"currency\": \"USD\",\"account_type\": \"Checking\", \"balance\": 5230.50\"",
                "\"account_type\": \"Savings\", \"balance\": 15280.00\"",
                "\"account_type\": \"Credit Card\", \"balance\": -2000.00\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_06",
        "instruction": "You are Sofia Andersson. You have relocated to a new address (789 Pine Street, College Town, TX\u00a077840) and updated your phone number to 555-222-3333, designating it as primary. Amend your profile and then retrieve your updated record.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "category": "Profile Update",
                    "target_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "target_entity": "CustomerProfile",
                    "operation": "Update",
                    "parameters": {
                        "new_address": "789 Pine Street, College Town, TX 77840",
                        "new_phone_number": "555-222-3333"
                    }
                },
            },
            {
                "name": "UpdateAddressForCustomerId",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "mailing_address": {
                        "street_address": "789 Pine Street",
                        "city": "College Town",
                        "state": "TX",
                        "postal_code": "77840",
                        "country": "USA"
                    },
                    "set_as_primary": true
                },
            },
            {
                "name": "UpdateContactNumberOfCustomerId",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "new_phone_number": "555-222-3333",
                    "set_as_primary": true
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "ticket_id": "tkt_1",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                }
            }
        ],
        "outputs": [
                "\"customer_id\": \"f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9\", \"mailing_address\": {\"street_address\": \"789 Pine Street\", \"city\": \"College Town\", \"state\": \"TX\", \"postal_code\": \"77840\", \"country\": \"USA\"}, \"phone_numbers\": [{\"type\": \"Mobile\", "number": \"555-222-3333\", \"is_primary\": true}]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_07",
        "instruction": "You are John\u00a0Doe. You have your monthly salary of USD\u00a03,000 deposited by Employer Inc. into your Checking account. Proceed to transfer 20% which totals USD\u00a0600 from Checking to your Savings account, and subsequently verify the balances in both accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Checking"
                },
            },
            {
                "name": "ReceivePayment",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_id": "acc_chk_1001",
                    "amount": 3000.0,
                    "currency": "USD"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Savings"
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_chk_1001",
                    "target_account_id": "acc_sav_1002",
                    "currency": "USD",
                    "amount": 600.0
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Savings"
                }
            }
        ],
        "outputs": [
                "\"account_type\": \"Checking\", \"balance\": 7630.50\"",
                "\"account_type\": \"Savings\", \"balance\": 16380.00\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_08",
        "instruction": "You are Chloe\u202fDubois. You must transfer EUR\u202f200 from your Checking account (acc_chk_9001) to your beneficiary Marie Dubois, then assess your total balance across all accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Chloe ",
                    "last_name": "Dubois"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "beneficiary_name": "Marie Dubois"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "account_id": "acc_chk_9001",
                    "requested_amount": 200.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "source_account_id": "acc_chk_9001",
                    "beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c",
                    "amount": 200.0,
                    "currency": "EUR"
                },
            },
            {
                "name": "CalculateTotalBalance",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "account_ids": [
                        "acc_chk_9001",
                        "acc_crd_9002"
                    ]
                }
            }
        ],
        "outputs": [
                "\"total_balance\": 2500.00\",\"Currency\": \"EUR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_09",
        "instruction": "You are Kenji Tanaka on 2025-07-24T15:30:00Z. Introduce a new personal beneficiary named Jane Doe (your sister) at ABC Bank, with the account number 123456789 and routing number 021000021.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Jane Doe",
                    "beneficiary_type": "Personal",
                    "relationship": "Sister",
                    "bank_name": "ABC Bank",
                    "account_number": "123456789",
                    "routing_number": "021000021",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Jane Doe"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\",\"beneficiary_name\": \"Jane Doe\",\"beneficiary_type\": \"Personal\",\"relationship\": \"Sister\",\"account_details\": {\"bank_name\": \"ABC Bank\", \"account_number\": \"123456789\", \"routing_number\": \"021000021\"},\"date_added\": \"2025-07-24T15:30:00Z\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_10",
        "instruction": "You are Zoltan Nagy. Remove your beneficiary Metropolis Power & Light from your list.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Metropolis Power & Light"
                },
            },
            {
                "name": "RemoveBeneficiaryByBeneficiaryId",
                "arguments": {
                    "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a",
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                },
            },
            {
                "name": "GetAllBeneficiariesForCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                }
            }
        ],
        "outputs": [
                "\"status\": \"Removed\", \"remaining_beneficiaries\": []\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_11",
        "instruction": "You are Liam\u00a0O'Connor. To ensure security, limit access to your Checking account.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Liam",
                    "last_name": "O'Connor"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "account_type": "Checking"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "priority": "High",
                    "channel": "Web Portal",
                    "category": "Security",
                    "target_id": "acc_chk_12001",
                    "target_entity": "Account",
                    "operation": "Block",
                    "parameters": {}
                },
            },
            {
                "name": "BlockAccountForCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "account_id": "acc_chk_12001"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "account_id": "acc_chk_12001"
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"tkt_1\",\"status\": \"Blocked\",\"account_id\": \"acc_chk_12001\",\"account_type\": \"Checking\",\"balance\": 4500.00\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_12",
        "instruction": "You are Zoltan Nagy. You are checking on the progress of your Business loan application. You intend to create a support ticket for further information.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Liam",
                    "last_name": "O'Connor"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "loan_type": "Business"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "category": "Loan Inquiry",
                    "target_id": "app_b1c2d3e4-f5a6-b7c8-d9e0-f1a2b3c4d5e6",
                    "target_entity": "Loan Application",
                    "operation": "Inquiry",
                    "parameters": {}
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"tkt_1\", \"status\": \"Open\", \"category\": \"Loan Inquiry\", \"target_id\": \"app_b1c2d3e4-f5a6-b7c8-d9e0-f1a2b3c4d5e6\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_13",
        "instruction": "You are John\u202fDoe. You've relocated to a new address at 456 Elm St, Newcity, AZ\u202f85001, USA. Kindly document this change by generating a support ticket and subsequently updating your residential address.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "category": "Profile Update",
                    "target_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "target_entity": "CustomerProfile",
                    "operation": "UpdateAddress",
                    "parameters": {
                        "new_residential_address": {
                            "street_address": "456 Elm St",
                            "city": "Newcity",
                            "state": "AZ",
                            "postal_code": "85001",
                            "country": "USA"
                        }
                    }
                },
            },
            {
                "name": "UpdateAddressForCustomerId",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "residential_address": {
                        "street_address": "456 Elm St",
                        "city": "Newcity",
                        "state": "AZ",
                        "postal_code": "85001",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "ticket_id": "tkt_1",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetCustomerDetailsByCustomerId",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                }
            }
        ],
        "outputs": [
                "\"customer_id\": \"c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e\"",
                "\"residential_address\": {\"street_address\": \"456 Elm St\", \"city\": \"Newcity\", \"state\": \"AZ\", \"postal_code\": \"85001\", \"country\": \"USA\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_14",
        "instruction": "You are John\u202fDoe on 2025-07-24T15:30:00Z. You wish to add a new personal beneficiary named Alice\u202fJohnson (your friend) at Metro\u202fBank with account number 555123456 and routing number 111000025. Then, move USD\u00a0300 from your Checking account (acc_chk_1001) to this beneficiary, and afterward, eliminate the beneficiary from your list.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Alice Johnson",
                    "beneficiary_type": "Personal",
                    "relationship": "Friend",
                    "bank_name": "Metro Bank",
                    "account_number": "555123456",
                    "routing_number": "111000025",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Alice Johnson"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_id": "acc_chk_1001",
                    "requested_amount": 300.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_1",
                    "source_account_id": "acc_chk_1001",
                    "amount": 300.0,
                    "currency": "USD"
                },
            },
            {
                "name": "RemoveBeneficiaryByBeneficiaryId",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_1"
                },
            },
            {
                "name": "GetAllBeneficiariesForCustomerId",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"new_source_balance\": 4930.50",
                "\"status\": \"Beneficiary removed successfully.\"",
                "{\"beneficiary_id\": \"bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d\", \"beneficiary_name\": \"Elena Popescu\", \"beneficiary_type\": \"Personal\", \"relationship\": \"Friend\", \"account_details\": {\"account_number\": \"9876543210\", \"bank_name\": \"City National Bank\", \"routing_number\": \"122000661\", \"country\": \"USA\"}}",
                "{\"beneficiary_id\": \"bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e\", \"beneficiary_name\": \"Anytown Utility Services\", \"beneficiary_type\": \"Business\", \"relationship\": \"Utility Provider\", \"account_details\": {\"account_number\": \"5555666677\", \"bank_name\": \"Bank of Anytown\", \"routing_number\": \"021000021\", \"country\": \"USA\"}}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_15",
        "instruction": "You are Chloe\u202fDubois. Your credit card ending in 2424 has been misplaced. Using your Mobile app, please initiate a support ticket to block that credit card, and then mark the ticket as resolved.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Dubois"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "priority": "High",
                    "channel": "Mobile App",
                    "category": "Card Loss",
                    "target_entity": "Account",
                    "target_id": "acc_crd_9002",
                    "operation": "BlockAccount"
                },
            },
            {
                "name": "BlockAccountForCustomerId",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "account_id": "acc_crd_9002"
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "ticket_id": "tkt_1",
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "account_id": "acc_crd_9002"
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"tkt_1\"",
                "\"account_id\": \"acc_crd_9002\", \"status\": \"Blocked\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_16",
        "instruction": "Assume the identity of John\u202fDoe. Seek to obtain a home loan amounting to USD\u202f250000 over a span of 360 months for the purpose of purchasing a new home. Kindly initiate a new loan application with the loan type 'Mortgage' for 'Home Purchase' and proceed to check its status thereafter.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "loan_type": "Mortgage",
                    "requested_amount": 250000.0,
                    "requested_term_months": 360,
                    "purpose": "Home Purchase"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "loan_type": "Mortgage"
                }
            }
        ],
        "outputs": [
                "\"application_id\": \"app_1\"",
                "\"application_status\": \"Submitted\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_17",
        "instruction": "Act as John\u202fDoe on 2025-07-24T15:30:00Z. Aim to include your son Michael\u202fDoe as a personal beneficiary (relation \u201cSon\u201d) at First\u202fNational\u202fBank, account number 777777777, with routing 111000222. Follow up by transferring USD\u00a0100 from your Savings account to him, and verify the updated balance.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Michael Doe",
                    "beneficiary_type": "Personal",
                    "relationship": "Son",
                    "bank_name": "First National Bank",
                    "account_number": "777777777",
                    "routing_number": "111000222",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Michael Doe"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Savings"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_id": "acc_sav_1002",
                    "requested_amount": 100.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_1",
                    "source_account_id": "acc_sav_1002",
                    "amount": 100.0,
                    "currency": "USD"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Savings"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"new_source_balance\": 15680.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_18",
        "instruction": "Portray John\u202fDoe on 2025-07-24T15:30:00Z. Seek to register your daughter, Emily\u202fDoe, as a personal beneficiary (relation \u201cDaughter\u201d) at Family\u202fBank with account number 888888888 and routing number 111000333. Then orchestrate a monthly payment of USD\u202f200 from your Savings account, starting from 2025-08-24.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Emily Doe",
                    "beneficiary_type": "Personal",
                    "relationship": "Daughter",
                    "bank_name": "Family Bank",
                    "account_number": "888888888",
                    "routing_number": "111000333",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Emily Doe"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_id": "acc_sav_1002",
                    "requested_amount": 200.0
                },
            },
            {
                "name": "CreateNewSchedulePayment",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_sav_1002",
                    "beneficiary_id": "bene_1",
                    "amount": 200.0,
                    "currency": "USD",
                    "frequency": "Monthly",
                    "start_date": "2025-08-24"
                },
            },
            {
                "name": "GetPaymentIdByCustomerIdAndBeneficiaryId",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_1"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"payment_id\": \"sp_1\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"amount\": 200.0, \"currency\": \"USD\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_19",
        "instruction": "Identify as Zoltan Nagy. Cancel your current monthly INR\u00a04,000 payment arrangement to your business beneficiary Global ISP and subsequently delete that beneficiary.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "GetAllBeneficiariesForCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "GetPaymentIdByCustomerIdAndBeneficiaryId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_id": "bene_5e4f3a2b-1c9d-8e7f-6a5b-4c3d2e1f0a9b"
                },
            },
            {
                "name": "CancelPaymentByScheduledPaymentId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "scheduled_payment_id": "sp_b3a2c1d9-c3d2-e1f0-a9b8-c7d6e5f4a3b2"
                },
            },
            {
                "name": "RemoveBeneficiaryByBeneficiaryId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_id": "bene_5e4f3a2b-1c9d-8e7f-6a5b-4c3d2e1f0a9b"
                }
            }
        ],
        "outputs": [
                "\"message\": \"Your scheduled payment sp_b3a2c1d9-c3d2-e1f0-a9b8-c7d6e5f4a3b2 has been cancelled and beneficiary 'Global ISP' removed.\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_20",
        "instruction": "You are Chloe\u202fDubois. With a new mobile number 480\u2011555\u20111234, initiate a support ticket to revise your contact number, complete the updating process, and subsequently close the ticket.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Dubois"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "category": "Profile Update",
                    "target_entity": "CustomerProfile",
                    "target_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "operation": "UpdateContactNumber",
                    "parameters": {
                        "new_phone_number": "480-555-1234"
                    }
                },
            },
            {
                "name": "UpdateContactNumberOfCustomerId",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "new_phone_number": "480-555-1234"
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "ticket_id": "tkt_1",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetCustomerDetailsByCustomerId",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"tkt_1\"",
                "\"contact_numbers\": [{\"type\":\"Mobile\","number":\"480-555-1234\",\"is_primary\":false}, …]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_21",
        "instruction": "As Zoltan Nagy, you need to note the receipt of your monthly salary of INR 200,000 via Employer Direct Deposit into your Checking account (acc_chk_5002). Next, move INR 50,000 from your Checking account to your Savings account (acc_sav_5001) and finally confirm your account balances.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Checking"
                },
            },
            {
                "name": "ReceivePayment",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_id": "acc_chk_5002",
                    "amount": 200000.0,
                    "currency": "INR",
                    "source": "Employer Direct Deposit"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Savings"
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "source_account_id": "acc_chk_5002",
                    "target_account_id": "acc_sav_5001",
                    "amount": 50000.0,
                    "currency": "INR"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Savings"
                }
            }
        ],
        "outputs": [
                "\"checking_balance\": 250000.00\"",
                "\"message\": \"Transferred 50000.00 INR from checking to savings.\"",
                "\"checking_balance\": 200000.00\"",
                "\"savings_balance\": 2550000.00\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_22",
        "instruction": "As Sofia Andersson, terminate your active monthly payment to the business beneficiary 'London Electricity Co.' and subsequently delete that beneficiary.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Williams"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_name": "London Electricity Co."
                },
            },
            {
                "name": "GetPaymentIdByCustomerIdAndBeneficiaryId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d"
                },
            },
            {
                "name": "CancelPaymentByScheduledPaymentId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "scheduled_payment_id": "sp_c1d9b3a2-e1f0-a9b8-c7d6-e5f4a3b2c1d0"
                },
            },
            {
                "name": "RemoveBeneficiaryByBeneficiaryId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d"
                },
            },
            {
                "name": "GetAllBeneficiariesForCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"
                }
            }
        ],
        "outputs": [
                "\"List of Beneficiary\": \"[]\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_23",
        "instruction": "Acting as Zoltan Nagy, you intend to apply for an Auto loan of USD 20,000 over 60 months for a vehicle purchase. Please initiate a new loan application, proceed to approval, establish the loan, and then access the loan details. I want to keep my Vehicle (1GKS1EKD4E1234567) as collateral.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "loan_type": "Auto",
                    "requested_amount": 20000.0,
                    "requested_term_months": 60,
                    "purpose": "Vehicle Purchase"
                },
            },
            {
                "name": "ProcessLoanApplicationId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "application_id": "app_1"
                },
            },
            {
                "name": "AddNewLoanForCustomer",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "application_id": "app_1",
                    "collateral_type": "Vehicle",
                    "collateral_info": "1GKS1EKD4E1234567",
                    "currency": "USD"
                },
            },
            {
                "name": "GetLoanInformationByLoanId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "loan_id": "loan_1"
                }
            }
        ],
        "outputs": [
                "\"application_id\": \"app_1\"",
                "\"loan_id\": \"loan_1\"",
                "\"status\": \"Approved\"",
                "\"principal_amount\": 20000.0",
                "\"term_months\": 60"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_24",
        "instruction": "As Elena Popescu, you wish to apply for a home loan of USD 300,000 over 360 months for purchasing a new Home. Initiate a new loan application and subsequently review its status.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "loan_type": "Home",
                    "requested_amount": 300000.0,
                    "requested_term_months": 360,
                    "purpose": "Home Purchase"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "loan_type": "Home"
                }
            }
        ],
        "outputs": [
                "\"application_id\": \"app_1\"",
                "\"application_status\": \"Submitted\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_25",
        "instruction": "As Elena Popescu, you wish to apply for a home loan of USD 300,000 over 360 months for purchasing a new Home. Initiate a new loan application and subsequently review its status.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "loan_type": "Home",
                    "requested_amount": 300000.0,
                    "requested_term_months": 360,
                    "purpose": "Home Purchase"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "loan_type": "Home"
                }
            }
        ],
        "outputs": [
                "\"application_id\": \"app_1\"",
                "\"application_status\": \"Submitted\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_26",
        "instruction": "You are John\u202fDoe. Proceed to transfer USD\u202f100 from your Checking account (acc_chk_1001) to your beneficiary Jane\u202fSmith (bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d), and then determine your total balance across all of your accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Elena Popescu"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_id": "acc_chk_1001",
                    "requested_amount": 100.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_chk_1001",
                    "beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d",
                    "amount": 100.0,
                    "currency": "USD"
                },
            },
            {
                "name": "CalculateTotalBalance",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_ids": [
                        "acc_chk_1001",
                        "acc_sav_1002",
                        "acc_crd_1003"
                    ]
                }
            }
        ],
        "outputs": [
                "\"total_balance\": 18410.50\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_27",
        "instruction": "You are David\u202fChen. Your USD checking card has been lost. Kindly initiate a ticket to block your Checking account, access your account details by type, block it, resolve the ticket, and check the account status.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_type": "Checking"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "priority": "High",
                    "channel": "Web Portal",
                    "category": "Security",
                    "target_entity": "Account",
                    "target_id": "acc_chk_3001",
                    "operation": "BlockAccount",
                    "parameters": {}
                },
            },
            {
                "name": "BlockAccountForCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_chk_3001"
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "ticket_id": "tkt_1",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_chk_3001"
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"tkt_1\"",
                "\"account_id\": \"acc_chk_3001\", \"status\": \"Blocked\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_28",
        "instruction": "You are Adetokunbo\u202fAdebayor. You want to update your email from ade.adebayor@example.ng to adetokunbo.adebayor@newmail.ng. Open a support ticket, complete the update, close the ticket, and afterward confirm your new email.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Adetokunbo",
                    "last_name": "Adebayor"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "category": "Profile Update",
                    "target_entity": "CustomerProfile",
                    "target_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "operation": "UpdateEmail",
                    "parameters": {
                        "new_email": "adetokunbo.adebayor@newmail.ng"
                    }
                },
            },
            {
                "name": "UpdateEmailForOfCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "new_email": "adetokunbo.adebayor@newmail.ng"
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                    "ticket_id": "tkt_1",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetCustomerDetailsByCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"tkt_1\"",
                "\"email_address\": \"adetokunbo.adebayor@newmail.ng\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_29",
        "instruction": "You are Kenji Tanaka. Initiate the opening of a new AUD Checking account, then proceed to transfer AUD 500 from your current Savings account into it, and subsequently confirm the new Checking balance.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Olivia",
                    "last_name": "Jones"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Checking"
                },
            },
            {
                "name": "CreateNewAccountForCustomer",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "account_type": "Checking",
                    "account_type_code": "chk",
                    "currency": "AUD"
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "source_account_id": "acc_sav_17002",
                    "target_account_id": "acc_1",
                    "amount": 500.0,
                    "currency": "AUD"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                    "account_id": "acc_1"
                }
            }
        ],
        "outputs": [
                "\"account_id\": \"acc_1\"",
                "\"account_type\": \"Checking\"",
                "\"balance\": 500.0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_30",
        "instruction": "You are Jane\u202fSmith. Set up a new CAD Credit Card account, and then promptly transfer CAD\u202f500 from your existing Checking account into it.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Credit Card"
                },
            },
            {
                "name": "CreateNewAccountForCustomer",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Credit Card",
                    "account_type_code": "crd",
                    "currency": "CAD"
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "source_account_id": "acc_chk_2001",
                    "target_account_id": "acc_1",
                    "amount": 500.0,
                    "currency": "CAD"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Credit Card"
                }
            }
        ],
        "outputs": [
                "\"checking_balance\": 2600.75\"",
                "\"credit_card_balance\": 500\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_31",
        "instruction": "As Elena Popescu, initiate the creation of a new Savings account and promptly transfer CAD 800 from your current Checking account into it.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Savings"
                },
            },
            {
                "name": "CreateNewAccountForCustomer",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Savings",
                    "account_type_code": "sav",
                    "currency": "CAD"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Savings"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_id": "acc_chk_2001",
                    "requested_amount": 800.0
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "source_account_id": "acc_chk_2001",
                    "target_account_id": "acc_1",
                    "currency": "CAD",
                    "amount": 800.0
                }
            }
        ],
        "outputs": [
                "\"message\": \"Transfer successful (same currency).\",\"source_account_id\": \"acc_chk_2001\",\"target_account_id\": \"acc_1\",\"amount_transferred\": 800.0,\"currency\": \"CAD\",\"source_balance\": 2300.75,\"target_balance\": 800.0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_32",
        "instruction": "As Zoltan Nagy, establish a new Savings account and quickly transfer USD 1000 from your existing Checking account to it.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Savings"
                },
            },
            {
                "name": "CreateNewAccountForCustomer",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_type": "Savings",
                    "account_type_code": "sav",
                    "currency": "USD"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_type": "Savings"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_chk_3001",
                    "requested_amount": 1000.0
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "source_account_id": "acc_chk_3001",
                    "target_account_id": "acc_1",
                    "currency": "USD",
                    "amount": 1000.0
                }
            }
        ],
        "outputs": [
                "\"message\": \"Transfer successful (same currency).\",\"source_account_id\": \"acc_chk_3001\",\"target_account_id\": \"acc_1\",\"amount_transferred\": 1000.0,\"currency\": \"USD\",\"source_balance\": 11540.25,\"target_balance\": 1000.0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_33",
        "instruction": "As Sofia Andersson, set up a new Savings account and immediately move USD 200 from your existing Checking account into it.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Savings"
                },
            },
            {
                "name": "CreateNewAccountForCustomer",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "account_type": "Savings",
                    "account_type_code": "sav",
                    "currency": "USD"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "account_type": "Savings"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "account_id": "acc_chk_4001",
                    "requested_amount": 200.0
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "source_account_id": "acc_chk_4001",
                    "target_account_id": "acc_1",
                    "currency": "USD",
                    "amount": 200.0
                }
            }
        ],
        "outputs": [
                "\"message\": \"Transfer successful (same currency).\",\"source_account_id\": \"acc_chk_4001\",\"target_account_id\": \"acc_1\",\"amount_transferred\": 200.0,\"currency\": \"USD\",\"source_balance\": 1000.50,\"target_balance\": 200.0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_34",
        "instruction": "As Zoltan Nagy, proceed to transfer USD 300 to your beneficiary Metropolis Power & Light from your Checking account.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_type": "Checking"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_chk_3001",
                    "requested_amount": 300.0
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Metropolis Power & Light"
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "source_account_id": "acc_chk_3001",
                    "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a",
                    "amount": 300.0,
                    "currency": "USD"
                }
            }
        ],
        "outputs": [
                "\"message\": \"Paid 300.00 USD to beneficiary 'Metropolis Power & Light'.\", \"source_account_id\": \"acc_chk_3001\", \"beneficiary_account_number\": \"9988776655\", \"source_amount\": 300.0, \"source_currency\": \"USD\", \"target_amount\": 300.0, \"target_currency\": \"USD\", \"new_source_balance\": 12240.25\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_35",
        "instruction": "As Chloe Dubois, organize a transfer of EUR 100 from your Checking account to your personal beneficiary Klaus Schmidt.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Hans",
                    "last_name": "Müller"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "account_type": "Checking"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "account_id": "acc_chk_8001",
                    "requested_amount": 100.0
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "beneficiary_name": "Klaus Schmidt"
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "source_account_id": "acc_chk_8001",
                    "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a",
                    "amount": 100.0,
                    "currency": "EUR"
                }
            }
        ],
        "outputs": [
                "\"source_account_id\": \"acc_chk_8001\", \"source_amount\": 100.0, \"source_currency\": \"EUR\", \"target_amount\": 100.0, \"target_currency\": \"EUR\", \"new_source_balance\": 7700.50\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_36",
        "instruction": "You are Chloe Dubois and you intend to transfer EUR 1000 to your personal beneficiary Klaus Schmidt from your Checking account.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Hans",
                    "last_name": "Müller"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "account_type": "Checking"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "account_id": "acc_chk_8001",
                    "requested_amount": 1000.0
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "beneficiary_name": "Klaus Schmidt"
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                    "source_account_id": "acc_chk_8001",
                    "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a",
                    "amount": 1000.0,
                    "currency": "EUR"
                }
            }
        ],
        "outputs": [
                "\"source_account_id\": \"acc_chk_8001\", \"source_amount\": 1000.0, \"source_currency\": \"EUR\", \"target_amount\": 1000.0, \"target_currency\": \"EUR\", \"new_source_balance\": 6800.50\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_37",
        "instruction": "You are Sofia Andersson. Initiate a monthly GBP\u00a3100 payment starting next month, on date 2025-08-24, from your Checking account to your business beneficiary Manchester Electricity Co.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Williams"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_name": "London Electricity Co."
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_id": "acc_chk_6001",
                    "requested_amount": 100.0
                },
            },
            {
                "name": "CreateNewSchedulePayment",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "source_account_id": "acc_chk_6001",
                    "beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d",
                    "amount": 100.0,
                    "currency": "GBP",
                    "frequency": "Monthly",
                    "start_date": "2025-08-24"
                }
            }
        ],
        "outputs": [
                "\"payment_id\": \"sp_1\", \"customer_id\": \"b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5\", \"source_account_id\": \"acc_chk_6001\", \"beneficiary_id\": \"bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d\", \"amount\": 100.0, \"currency\": \"GBP\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"next_payment_date\": \"2025-09-24\", \"end_date\": null, \"status\": \"Active\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_38",
        "instruction": "You are Zoltan Nagy. Arrange for a monthly INR 1500 payment beginning next month, on date 2025-08-24, from your Checking account to your business beneficiary Global ISP.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "Global ISP"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_id": "acc_chk_5002",
                    "requested_amount": 1500.0
                },
            },
            {
                "name": "CreateNewSchedulePayment",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "source_account_id": "acc_chk_5002",
                    "beneficiary_id": "bene_5e4f3a2b-1c9d-8e7f-6a5b-4c3d2e1f0a9b",
                    "amount": 1500.0,
                    "currency": "INR",
                    "frequency": "Monthly",
                    "start_date": "2025-08-24"
                }
            }
        ],
        "outputs": [
                "\"payment_id\": \"sp_1\", \"customer_id\": \"a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4\", \"source_account_id\": \"acc_chk_5002\", \"beneficiary_id\": \"bene_5e4f3a2b-1c9d-8e7f-6a5b-4c3d2e1f0a9b\", \"amount\": 1500.0, \"currency\": \"INR\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"next_payment_date\": \"2025-09-24\", \"end_date\": null, \"status\": \"Active\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_39",
        "instruction": "You are Zoltan Nagy. Organize a monthly USD 350 payment starting next month, on date 2025-08-24, from your Checking account to your business beneficiary Metropolis Power & Light.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Metropolis Power & Light"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_chk_3001",
                    "requested_amount": 350.0
                },
            },
            {
                "name": "CreateNewSchedulePayment",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "source_account_id": "acc_chk_3001",
                    "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a",
                    "amount": 350.0,
                    "currency": "USD",
                    "frequency": "Monthly",
                    "start_date": "2025-08-24"
                }
            }
        ],
        "outputs": [
                "\"payment_id\": \"sp_1\", \"customer_id\": \"d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a\", \"source_account_id\": \"acc_chk_3001\", \"beneficiary_id\": \"bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a\", \"amount\": 350.0, \"currency\": \"USD\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"next_payment_date\": \"2025-09-24\", \"end_date\": null, \"status\": \"Active\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_40",
        "instruction": "You are Elena Popescu. Apply for an auto loan of CAD 25,000 for purchasing a new car over 36 months, using your vehicle VIN '1HGCM82633A123456' as collateral.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "loan_type": "Auto",
                    "requested_amount": 25000.0,
                    "requested_term_months": 36,
                    "purpose": "New car purchase"
                },
            },
            {
                "name": "ProcessLoanApplicationId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "application_id": "app_1"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "loan_type": "Auto"
                },
            },
            {
                "name": "AddNewLoanForCustomer",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "application_id": "app_1",
                    "collateral_type": "Vehicle",
                    "collateral_info": "VIN: 1HGCM82633A123456",
                    "currency": "CAD"
                }
            }
        ],
        "outputs": [
                "\"loan_id\": \"loan_1\",\"loan_account_id\": \"loanacc_1\" \"application_id\": \"app_1\", \"status\": \"Approved\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_41",
        "instruction": "You are Sofia Andersson. Seek a student loan totaling USD 15,000 for tuition fees to be paid over 48 months, offering 'Maria Bekery Shop' (Property) as collateral.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "loan_type": "Student",
                    "requested_amount": 15000.0,
                    "requested_term_months": 48,
                    "purpose": "Tuition fees"
                },
            },
            {
                "name": "ProcessLoanApplicationId",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "application_id": "app_1"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "loan_type": "Student"
                },
            },
            {
                "name": "AddNewLoanForCustomer",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "application_id": "app_1",
                    "collateral_type": "Property",
                    "collateral_info": "Maria Bekery Shop",
                    "currency": "USD"
                }
            }
        ],
        "outputs": [
                "\"loan_id\": \"loan_1\",\"loan_account_id\": \"loanacc_1\" \"application_id\": \"app_1\", \"status\": \"Approved\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_42",
        "instruction": "You are Zoltan Nagy. Submit an application for a business loan of INR 500,000 aimed at office expansion over 60 months, utilizing your IT Equipment and Servers (Business Assets) as collateral.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "loan_type": "Business",
                    "requested_amount": 500000.0,
                    "requested_term_months": 60,
                    "purpose": "Office expansion"
                },
            },
            {
                "name": "ProcessLoanApplicationId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "application_id": "app_1"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "loan_type": "Business"
                },
            },
            {
                "name": "AddNewLoanForCustomer",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "application_id": "app_1",
                    "collateral_type": "Business Assets",
                    "collateral_info": "IT Equipment and Servers",
                    "currency": "INR"
                }
            }
        ],
        "outputs": [
                "\"loan_id\": \"loan_1\",\"loan_account_id\": \"loanacc_1\" \"application_id\": \"app_1\", \"status\": \"Approved\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_43",
        "instruction": "You are Sofia Andersson. Request a personal loan of GBP 3,000 intended for home renovations over 18 months, with your savings provided as collateral.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Williams"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "loan_type": "Personal",
                    "requested_amount": 3000.0,
                    "requested_term_months": 18,
                    "purpose": "Home renovations"
                },
            },
            {
                "name": "ProcessLoanApplicationId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "application_id": "app_1"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "loan_type": "Personal"
                },
            },
            {
                "name": "AddNewLoanForCustomer",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "application_id": "app_1",
                    "collateral_type": "Savings",
                    "collateral_info": "Savings account balance",
                    "currency": "GBP"
                }
            }
        ],
        "outputs": [
                "\"loan_id\": \"loan_1\",\"loan_account_id\": \"loanacc_1\" \"application_id\": \"app_1\", \"status\": \"Approved\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_44",
        "instruction": "You are Elena Popescu. Receive your monthly salary of CAD 4,000 from Creative Minds LLC into your Checking account, subsequently transfer 25%, equivalent to CAD 1,000, from Checking to your Savings account, then verify the balances in both accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Checking"
                },
            },
            {
                "name": "ReceivePayment",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_id": "acc_chk_2001",
                    "amount": 4000.0,
                    "currency": "CAD"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Savings"
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "source_account_id": "acc_chk_2001",
                    "target_account_id": "acc_sav_2002",
                    "currency": "CAD",
                    "amount": 1000.0
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Savings"
                }
            }
        ],
        "outputs": [
                "\"account_type\": \"Checking\", \"balance\": 6100.75\"",
                "\"account_type\": \"Savings\", \"balance\": 23000.00\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_45",
        "instruction": "You are Zoltan Nagy. Obtain your monthly salary of USD 12,000 from City General Hospital into your Checking account, thereafter transfer 10%, which is USD 1,200, from Checking to your Investment account, then check the balances in both accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_type": "Checking"
                },
            },
            {
                "name": "ReceivePayment",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_chk_3001",
                    "amount": 12000.0,
                    "currency": "USD"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_type": "Investment"
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "source_account_id": "acc_chk_3001",
                    "target_account_id": "acc_inv_3002",
                    "currency": "USD",
                    "amount": 1200.0
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_type": "Investment"
                }
            }
        ],
        "outputs": [
                "\"account_type\": \"Checking\", \"balance\": 23340.25\"",
                "\"account_type\": \"Investment\", \"balance\": 151200.00\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_46",
        "instruction": "Identify yourself as Zoltan Nagy. First, handle the receipt of your monthly scholarship of INR 1,200 from State University deposited into your Checking account. Next, proceed to transfer 50%, which amounts to INR 600, from Checking to your Savings account, and ultimately verify the balances in both accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Checking"
                },
            },
            {
                "name": "ReceivePayment",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_id": "acc_chk_5002",
                    "amount": 1200.0,
                    "currency": "INR"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Savings"
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "source_account_id": "acc_chk_5002",
                    "target_account_id": "acc_sav_5001",
                    "currency": "INR",
                    "amount": 600.0
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Savings"
                }
            }
        ],
        "outputs": [
                "\"account_type\": \"Checking\", \"balance\": 2500600.0\"",
                "\"account_type\": \"Savings\", \"balance\": 50600.0\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_47",
        "instruction": "Identify yourself as Zoltan Nagy. Initially, await the receipt of your monthly salary of INR 250,000 from Global Tech Services into your Checking account. Subsequently, coordinate the transfer of 20%, which equates to INR 50,000, from Checking to your Savings account, and in conclusion, confirm the balances in both accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Checking"
                },
            },
            {
                "name": "ReceivePayment",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_id": "acc_chk_5002",
                    "amount": 250000.0,
                    "currency": "INR"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Savings"
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "source_account_id": "acc_chk_5002",
                    "target_account_id": "acc_sav_5001",
                    "currency": "INR",
                    "amount": 50000.0
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Savings"
                }
            }
        ],
        "outputs": [
                "\"account_type\": \"Checking\", \"balance\": 250000.00\"",
                "\"account_type\": \"Savings\", \"balance\": 2550000.00\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_48",
        "instruction": "Identify yourself as Oliver Williams. Begin by receiving your monthly salary of AED 1,800 from Sparky & Co. into your Checking account. Afterwards, arrange the transfer of 15%, equivalent to AED 270, from Checking to your Savings account, and finally, validate the balances in both accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Fatima",
                    "last_name": "Al-Fassi"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "account_type": "Checking"
                },
            },
            {
                "name": "ReceivePayment",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "account_id": "acc_chk_7001",
                    "amount": 1800.0,
                    "currency": "AED"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "account_type": "Savings"
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "source_account_id": "acc_chk_7001",
                    "target_account_id": "acc_sav_7002",
                    "currency": "AED",
                    "amount": 270.0
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "account_type": "Savings"
                }
            }
        ],
        "outputs": [
                "\"account_type\": \"Checking\", \"balance\": 151530.0\"",
                "\"account_type\": \"Savings\", \"balance\": 750270.0\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_49",
        "instruction": "Identify yourself as Kenji\u202fTanaka. Given that your Savings account (acc_sav_10002) is being targeted by a scam, you need to block it for security reasons. Utilize the Web Portal to submit a support ticket to block the Savings account, and then ensure the ticket is marked as resolved.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Kenji",
                    "last_name": "Tanaka"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "priority": "High",
                    "channel": "Web Portal",
                    "category": "Security",
                    "target_entity": "Account",
                    "target_id": "acc_sav_10002",
                    "operation": "BlockAccount"
                },
            },
            {
                "name": "BlockAccountForCustomerId",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "account_id": "acc_sav_10002"
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "ticket_id": "tkt_1",
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "account_id": "acc_sav_10002"
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"tkt_1\"",
                "\"account_id\": \"acc_sav_10002\", \"status\": \"Blocked\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_50",
        "instruction": "Identify yourself as Kenji\u202fTanaka. You are required to transfer JPY\u202f1000 from your Checking account (acc_chk_10001) to your beneficiary, Yuki Tanaka. Subsequently, calculate your total balance across all of your accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Kenji",
                    "last_name": "Tanaka"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "beneficiary_name": "Yuki Tanaka"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "account_id": "acc_chk_10001",
                    "requested_amount": 1000.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "source_account_id": "acc_chk_10001",
                    "beneficiary_id": "bene_2b1c9d8e-7f6a-5b4c-3d2e-1f0a9b8c7d6e",
                    "amount": 1000.0,
                    "currency": "JPY"
                },
            },
            {
                "name": "CalculateTotalBalance",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "account_ids": [
                        "acc_chk_10001",
                        "acc_sav_10002"
                    ]
                }
            }
        ],
        "outputs": [
                "\"total_balance\": 17499000.00\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_51",
        "instruction": "You are Zoltan Nagy. Terminate the active monthly payment to your business beneficiary Metropolis Power & Light and subsequently delete that beneficiary.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                },
            },
            {
                "name": "GetAllBeneficiariesForCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                },
            },
            {
                "name": "GetPaymentIdByCustomerIdAndBeneficiaryId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a"
                },
            },
            {
                "name": "CancelPaymentByScheduledPaymentId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "scheduled_payment_id": "sp_b3a2c1d9-e7f6-a5b4-c3d2-e1f0a9b8c7d6"
                },
            },
            {
                "name": "RemoveBeneficiaryByBeneficiaryId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a"
                }
            }
        ],
        "outputs": [
                "\"List of Beneficiary\": \"[]\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_52",
        "instruction": "You are John\u00a0Doe. Block your Checking account for security reasons.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "John",
                    "last_name": "Doe"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Checking"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "priority": "High",
                    "channel": "Web Portal",
                    "category": "Security",
                    "target_id": "acc_chk_1001",
                    "target_entity": "Account",
                    "operation": "Block",
                    "parameters": {}
                },
            },
            {
                "name": "BlockAccountForCustomerId",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_id": "acc_chk_1001"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_id": "acc_chk_1001"
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"tkt_1\",\"status\": \"Blocked\",\"account_id\": \"acc_chk_1001\",\"account_type\": \"Checking\",\"balance\": 5230.00\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_53",
        "instruction": "You are Jane\u00a0Smith. Block your Checking account for security purposes.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Checking"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "priority": "High",
                    "channel": "Web Portal",
                    "category": "Security",
                    "target_id": "acc_chk_2001",
                    "target_entity": "Account",
                    "operation": "Block",
                    "parameters": {}
                },
            },
            {
                "name": "BlockAccountForCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_id": "acc_chk_2001"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_id": "acc_chk_2001"
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"tkt_1\",\"status\": \"Blocked\",\"account_id\": \"acc_chk_2001\",\"account_type\": \"Checking\",\"balance\": 3100.75\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_54",
        "instruction": "You are David\u00a0Chen. For security reasons, block your Checking account.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_type": "Checking"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "priority": "High",
                    "channel": "Web Portal",
                    "category": "Security",
                    "target_id": "acc_chk_3001",
                    "target_entity": "Account",
                    "operation": "Block",
                    "parameters": {}
                },
            },
            {
                "name": "BlockAccountForCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_chk_3001"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_chk_3001"
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"tkt_1\",\"status\": \"Blocked\",\"account_id\": \"acc_chk_3001\",\"account_type\": \"Checking\",\"balance\": 12500.00\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_55",
        "instruction": "You are Maria\u00a0Garcia. For security measures, block your Checking account.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Checking"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "account_type": "Checking"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "priority": "High",
                    "channel": "Web Portal",
                    "category": "Security",
                    "target_id": "acc_chk_4001",
                    "target_entity": "Account",
                    "operation": "Block",
                    "parameters": {}
                },
            },
            {
                "name": "BlockAccountForCustomerId",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "account_id": "acc_chk_4001"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "account_id": "acc_chk_4001"
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"tkt_1\",\"status\": \"Blocked\",\"account_id\": \"acc_chk_4001\",\"account_type\": \"Checking\",\"balance\": 1200.50\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_56",
        "instruction": "You are Jane\u202fSmith. You've recently moved to 789 Oak Avenue, Montreal, ON\u202fM5H\u202f2N2, Canada. Utilize the Mobile App to file a ticket. Please create a support ticket and update your residential address to reflect this.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "priority": "Medium",
                    "channel": "Mobile App",
                    "category": "Profile Update",
                    "target_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "target_entity": "CustomerProfile",
                    "operation": "UpdateAddress",
                    "parameters": {
                        "new_residential_address": {
                            "street_address": "789 Oak Avenue",
                            "city": "Montreal",
                            "state": "ON",
                            "postal_code": "M5H 2N2",
                            "country": "Canada"
                        }
                    }
                },
            },
            {
                "name": "UpdateAddressForCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "residential_address": {
                        "street_address": "789 Oak Avenue",
                        "city": "Montreal",
                        "state": "ON",
                        "postal_code": "M5H 2N2",
                        "country": "Canada"
                    }
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "ticket_id": "tkt_1",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetCustomerDetailsByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
                }
            }
        ],
        "outputs": [
                "\"customer_id\": \"a1b2c3d4-e5f6-7890-1234-567890abcdef\"",
                "\"residential_address\": {\"street_address\": \"789 Oak Avenue\", \"city\": \"Toronto\", \"state\": \"ON\", \"postal_code\": \"M5H 2N2\", \"country\": \"Canada\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_57",
        "instruction": "You are David\u202fChen. By raising a support ticket, apply the update to your profile with the new address 12 Market Street, Oakland, CA\u202f94103, USA.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "category": "Profile Update",
                    "target_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "target_entity": "CustomerProfile",
                    "operation": "UpdateAddress",
                    "parameters": {
                        "new_residential_address": {
                            "street_address": "12 Market Street",
                            "city": "Oakland",
                            "state": "CA",
                            "postal_code": "94103",
                            "country": "USA"
                        }
                    }
                },
            },
            {
                "name": "UpdateAddressForCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "residential_address": {
                        "street_address": "12 Market Street",
                        "city": "Oakland",
                        "state": "CA",
                        "postal_code": "94103",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "ticket_id": "tkt_1",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetCustomerDetailsByCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                }
            }
        ],
        "outputs": [
                "\"customer_id\": \"d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a\"",
                "\"residential_address\": {\"street_address\": \"12 Market Street\", \"city\": \"San Francisco\", \"state\": \"CA\", \"postal_code\": \"94103\", \"country\": \"USA\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_58",
        "instruction": "You are Maria\u202fGarcia. After relocating to 45 Sunset Blvd, Orlando, FL\u202f33101, USA, open a support ticket to document this change and update your residential address.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "category": "Profile Update",
                    "target_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "target_entity": "CustomerProfile",
                    "operation": "UpdateAddress",
                    "parameters": {
                        "new_residential_address": {
                            "street_address": "45 Sunset Blvd",
                            "city": "Orlando",
                            "state": "FL",
                            "postal_code": "33101",
                            "country": "USA"
                        }
                    }
                },
            },
            {
                "name": "UpdateAddressForCustomerId",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "residential_address": {
                        "street_address": "45 Sunset Blvd",
                        "city": "Orlando",
                        "state": "FL",
                        "postal_code": "33101",
                        "country": "USA"
                    }
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "ticket_id": "tkt_1",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetCustomerDetailsByCustomerId",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"
                }
            }
        ],
        "outputs": [
                "\"customer_id\": \"f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9\"",
                "\"residential_address\": {\"street_address\": \"45 Sunset Blvd\", \"city\": \"Miami\", \"state\": \"FL\", \"postal_code\": \"33101\", \"country\": \"USA\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_59",
        "instruction": "You are Lakshmi\u202fNarayanan. Raise a support ticket and save the address change to update your new residence at 22 MG Road, Bengaluru, KA\u202f560001, India.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "category": "Profile Update",
                    "target_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "target_entity": "CustomerProfile",
                    "operation": "UpdateAddress",
                    "parameters": {
                        "new_residential_address": {
                            "street_address": "22 MG Road",
                            "city": "Bengaluru",
                            "state": "KA",
                            "postal_code": "560001",
                            "country": "India"
                        }
                    }
                },
            },
            {
                "name": "UpdateAddressForCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "residential_address": {
                        "street_address": "22 MG Road",
                        "city": "Bengaluru",
                        "state": "KA",
                        "postal_code": "560001",
                        "country": "India"
                    }
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "ticket_id": "tkt_1",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetCustomerDetailsByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                }
            }
        ],
        "outputs": [
                "\"customer_id\": \"a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4\"",
                "\"residential_address\": {\"street_address\": \"22 MG Road\", \"city\": \"Bengaluru\", \"state\": \"KA\", \"postal_code\": \"560001\", \"country\": \"India\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_60",
        "instruction": "You are Oliver\u202fWilliams. Using the Mobile App, update your address to 55 Baker Street, Manchester, W1U\u202f7EU, UK, by logging this request as a support ticket and confirming the change.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Williams"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "priority": "Medium",
                    "channel": "Mobile App",
                    "category": "Profile Update",
                    "target_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "target_entity": "CustomerProfile",
                    "operation": "UpdateAddress",
                    "parameters": {
                        "new_residential_address": {
                            "street_address": "55 Baker Street",
                            "city": "Manchester",
                            "state": "Manchester",
                            "postal_code": "W1U 7EU",
                            "country": "UK"
                        }
                    }
                },
            },
            {
                "name": "UpdateAddressForCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "residential_address": {
                        "street_address": "55 Baker Street",
                        "city": "Manchester",
                        "state": "Manchester",
                        "postal_code": "W1U 7EU",
                        "country": "UK"
                    }
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "ticket_id": "tkt_1",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetCustomerDetailsByCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"
                }
            }
        ],
        "outputs": [
                "\"customer_id\": \"b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5\"",
                "\"residential_address\": {\"street_address\": \"55 Baker Street\", \"city\": \"London\", \"state\": \"London\", \"postal_code\": \"W1U 7EU\", \"country\": \"UK\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_61",
        "instruction": "You are Fatima\u202fAl-Fassi. Provide your updated residential address as Villa 12, Palm Jumeirah, Abu Dhabi\u202f00000, UAE by submitting a support ticket and initiating the update.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Fatima",
                    "last_name": "Al-Fassi"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "category": "Profile Update",
                    "target_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "target_entity": "CustomerProfile",
                    "operation": "UpdateAddress",
                    "parameters": {
                        "new_residential_address": {
                            "street_address": "Villa 12, Palm Jumeirah",
                            "city": "Abu Dhabi",
                            "state": "Abu Dhabi",
                            "postal_code": "00000",
                            "country": "UAE"
                        }
                    }
                },
            },
            {
                "name": "UpdateAddressForCustomerId",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "residential_address": {
                        "street_address": "Villa 12, Palm Jumeirah",
                        "city": "Abu Dhabi",
                        "state": "Abu Dhabi",
                        "postal_code": "00000",
                        "country": "UAE"
                    }
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "ticket_id": "tkt_1",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetCustomerDetailsByCustomerId",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"
                }
            }
        ],
        "outputs": [
                "\"customer_id\": \"c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6\"",
                "\"residential_address\": {\"street_address\": \"Villa 12, Palm Jumeirah\", \"city\": \"Dubai\", \"state\": \"Dubai\", \"postal_code\": \"00000\", \"country\": \"UAE\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_62",
        "instruction": "You are Jane\u202fSmith on 2025-07-24T15:30:00Z. Proceed to include your son, Ryan\u202fSmith, as a personal beneficiary (relationship \u201cSon\u201d) at Maple\u202fBank with account number 777777777 and routing number 002111444. Next, arrange a monthly payment of CAD\u202f300 from your Checking account, starting next month on 2025-08-24.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_name": "Ryan Smith",
                    "beneficiary_type": "Personal",
                    "relationship": "Son",
                    "bank_name": "Maple Bank",
                    "account_number": "777777777",
                    "routing_number": "002111444",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_name": "Ryan Smith"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_id": "acc_chk_2001",
                    "requested_amount": 300.0
                },
            },
            {
                "name": "CreateNewSchedulePayment",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "source_account_id": "acc_chk_2001",
                    "beneficiary_id": "bene_1",
                    "amount": 300.0,
                    "currency": "CAD",
                    "frequency": "Monthly",
                    "start_date": "2025-08-24"
                },
            },
            {
                "name": "GetPaymentIdByCustomerIdAndBeneficiaryId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_id": "bene_1"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"payment_id\": \"sp_1\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"amount\": 300.0, \"currency\": \"CAD\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_63",
        "instruction": "You are David\u202fChen on 2025-07-24T15:30:00Z. Proceed to add your nephew, Eric\u202fChen, as a personal beneficiary (relationship \u201cNephew\u201d) at City\u202fBank with account number 999999999 and routing number 021000021. Then plan a monthly payment of USD\u202f150 from your Checking account, starting next month on 2025-08-24.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Eric Chen",
                    "beneficiary_type": "Personal",
                    "relationship": "Nephew",
                    "bank_name": "City Bank",
                    "account_number": "999999999",
                    "routing_number": "021000021",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Eric Chen"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_chk_3001",
                    "requested_amount": 150.0
                },
            },
            {
                "name": "CreateNewSchedulePayment",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "source_account_id": "acc_chk_3001",
                    "beneficiary_id": "bene_1",
                    "amount": 150.0,
                    "currency": "USD",
                    "frequency": "Monthly",
                    "start_date": "2025-08-24"
                },
            },
            {
                "name": "GetPaymentIdByCustomerIdAndBeneficiaryId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_id": "bene_1"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"payment_id\": \"sp_1\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"amount\": 150.0, \"currency\": \"USD\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_64",
        "instruction": "You are Maria\u202fGarcia on 2025-07-24T15:30:00Z. Choose to include your sister, Lucia\u202fGarcia, as a personal beneficiary (relationship \u201cSister\u201d) at Horizon\u202fBank with account number 333333333 and routing number 111222444. Then organize a monthly payment of USD\u202f250 from your Checking account, beginning next month on 2025-08-24.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "beneficiary_name": "Lucia Garcia",
                    "beneficiary_type": "Personal",
                    "relationship": "Sister",
                    "bank_name": "Horizon Bank",
                    "account_number": "333333333",
                    "routing_number": "111222444",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "beneficiary_name": "Lucia Garcia"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "account_id": "acc_chk_4001",
                    "requested_amount": 250.0
                },
            },
            {
                "name": "CreateNewSchedulePayment",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "source_account_id": "acc_chk_4001",
                    "beneficiary_id": "bene_1",
                    "amount": 250.0,
                    "currency": "USD",
                    "frequency": "Monthly",
                    "start_date": "2025-08-24"
                },
            },
            {
                "name": "GetPaymentIdByCustomerIdAndBeneficiaryId",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "beneficiary_id": "bene_1"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"payment_id\": \"sp_1\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"amount\": 250.0, \"currency\": \"USD\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_65",
        "instruction": "You are Lakshmi\u202fNarayanan on 2025-07-24T15:30:00Z. Proceed to add your father, Narayan\u202fRao, as a personal beneficiary (relationship \u201cFather\u201d) at State\u202fBank of India with account number 222222222 and IFSC code SBIN000111. Then prepare a monthly payment of INR\u202f5,000 from your Savings account, starting next month on 2025-08-24.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "Narayan Rao",
                    "beneficiary_type": "Personal",
                    "relationship": "Father",
                    "bank_name": "State Bank of India",
                    "account_number": "222222222",
                    "routing_number": "SBIN000111",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "Narayan Rao"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_id": "acc_sav_5001",
                    "requested_amount": 5000.0
                },
            },
            {
                "name": "CreateNewSchedulePayment",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "source_account_id": "acc_sav_5001",
                    "beneficiary_id": "bene_1",
                    "amount": 5000.0,
                    "currency": "INR",
                    "frequency": "Monthly",
                    "start_date": "2025-08-24"
                },
            },
            {
                "name": "GetPaymentIdByCustomerIdAndBeneficiaryId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_id": "bene_1"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"payment_id\": \"sp_1\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"amount\": 5000.0, \"currency\": \"INR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_66",
        "instruction": "As Oliver\u202fWilliams on 2025-07-24T15:30:00Z, include your wife, Sophia\u202fWilliams, as a personal beneficiary (relationship \u201cWife\u201d) at Manchester\u202fBank. Use the account number 444444444 and sort code 30-00-01. Next, arrange for a monthly payment of GBP\u202f400 from your Checking account, commencing next month on 2025-08-24.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Williams"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_name": "Sophia Williams",
                    "beneficiary_type": "Personal",
                    "relationship": "Wife",
                    "bank_name": "London Bank",
                    "account_number": "444444444",
                    "routing_number": "30-00-01",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_name": "Sophia Williams"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_id": "acc_chk_6001",
                    "requested_amount": 400.0
                },
            },
            {
                "name": "CreateNewSchedulePayment",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "source_account_id": "acc_chk_6001",
                    "beneficiary_id": "bene_1",
                    "amount": 400.0,
                    "currency": "GBP",
                    "frequency": "Monthly",
                    "start_date": "2025-08-24"
                },
            },
            {
                "name": "GetPaymentIdByCustomerIdAndBeneficiaryId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_id": "bene_1"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"payment_id\": \"sp_10\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"amount\": 400.0, \"currency\": \"GBP\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_67",
        "instruction": "In the role of Fatima\u202fAl-Fassi on 2025-07-24T15:30:00Z, add your mother, Aisha\u202fAl-Fassi, as a personal beneficiary (relationship \u201cMother\u201d) at Emirates\u202fBank, using account number 555555555 and routing number EB000123. Subsequently, plan a monthly payment of AED\u202f1,000 from your Savings account, starting next month from the date 2025-08-24.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Fatima",
                    "last_name": "Al-Fassi"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "beneficiary_name": "Aisha Al-Fassi",
                    "beneficiary_type": "Personal",
                    "relationship": "Mother",
                    "bank_name": "Emirates Bank",
                    "account_number": "555555555",
                    "routing_number": "EB000123",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "beneficiary_name": "Aisha Al-Fassi"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "account_id": "acc_sav_7002",
                    "requested_amount": 1000.0
                },
            },
            {
                "name": "CreateNewSchedulePayment",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "source_account_id": "acc_sav_7002",
                    "beneficiary_id": "bene_1",
                    "amount": 1000.0,
                    "currency": "AED",
                    "frequency": "Monthly",
                    "start_date": "2025-08-24"
                },
            },
            {
                "name": "GetPaymentIdByCustomerIdAndBeneficiaryId",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "beneficiary_id": "bene_1"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"payment_id\": \"sp_11\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"amount\": 1000.0, \"currency\": \"AED\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_68",
        "instruction": "Acting as Jane\u202fSmith, you wish to apply for a car loan amounting to CAD\u202f40,000, intended to be paid over a period of 60 months for buying a new vehicle. Kindly submit a new loan application, and then check its status.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "loan_type": "Car Loan",
                    "requested_amount": 40000.0,
                    "requested_term_months": 60,
                    "purpose": "Vehicle Purchase"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "loan_type": "Car Loan"
                }
            }
        ],
        "outputs": [
                "\"application_id\": \"app_10\"",
                "\"application_status\": \"Submitted\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_69",
        "instruction": "In the position of David\u202fChen, you intend to apply for a personal loan of USD\u202f15,000 over a 48-month term for the purpose of home renovation. Please submit a new loan application and then verify its status.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "loan_type": "Personal",
                    "requested_amount": 15000.0,
                    "requested_term_months": 48,
                    "purpose": "Home Renovation"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "loan_type": "Personal"
                }
            }
        ],
        "outputs": [
                "\"application_id\": \"app_11\"",
                "\"application_status\": \"Submitted\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_70",
        "instruction": "You are Lakshmi Narayanan, and you wish to create a new RON Checking account. Afterward, transfer RON 1000 from your existing Savings account into it, then confirm the balance of the new Checking account.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Elena",
                    "last_name": "Popescu"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Checking"
                },
            },
            {
                "name": "CreateNewAccountForCustomer",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "account_type": "Checking",
                    "account_type_code": "chk",
                    "currency": "RON"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "account_type": "Savings"
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "source_account_id": "acc_sav_25001",
                    "target_account_id": "acc_1",
                    "amount": 1000,
                    "currency": "RON"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                    "account_type": "Checking"
                }
            }
        ],
        "outputs": [
                "\"account_id\": \"acc_1\"",
                "\"account_type\": \"Checking\"",
                "\"balance\": 1000.0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_71",
        "instruction": "Your name is Oliver\u202fWilliams. Your objective is to apply for a business loan amounting to GBP\u202f120,000 over a period of 84 months to grow your business. Initiate a new loan application and afterwards check the status of the application.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Williams"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "loan_type": "Business",
                    "requested_amount": 120000.0,
                    "requested_term_months": 84,
                    "purpose": "Business Expansion"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "loan_type": "Business"
                }
            }
        ],
        "outputs": [
                "\"application_id\": \"app_12\"",
                "\"application_status\": \"Submitted\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_72",
        "instruction": "Your identity is Jane\u202fSmith as of 2025-07-24T15:30:00Z. Aim to add your daughter Lily\u202fSmith as a personal beneficiary (relationship \u201cDaughter\u201d) with account number 222222222 at Maple\u202fBank (routing 002000111), then proceed to transfer CAD\u00a0200 from your Checking account to her and verify the updated balance.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_name": "Lily Smith",
                    "beneficiary_type": "Personal",
                    "relationship": "Daughter",
                    "bank_name": "Maple Bank",
                    "account_number": "222222222",
                    "routing_number": "002000111",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_name": "Lily Smith"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Checking"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_id": "acc_chk_2001",
                    "requested_amount": 200.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_id": "bene_1",
                    "source_account_id": "acc_chk_2001",
                    "amount": 200.0,
                    "currency": "CAD"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Checking"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"new_source_balance\": 2900.75"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_73",
        "instruction": "Identifying as David\u202fChen on 2025-07-24T15:30:00Z, you aim to add your brother Alex\u202fChen as a personal beneficiary (relationship \u201cBrother\u201d) with account number 333333333 at City\u202fBank (routing 021000021). Subsequently, transfer USD\u00a0500 from your Checking account to him and confirm the updated balance.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Alex Chen",
                    "beneficiary_type": "Personal",
                    "relationship": "Brother",
                    "bank_name": "City Bank",
                    "account_number": "333333333",
                    "routing_number": "021000021",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Alex Chen"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_type": "Checking"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_chk_3001",
                    "requested_amount": 500.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_id": "bene_1",
                    "source_account_id": "acc_chk_3001",
                    "amount": 500.0,
                    "currency": "USD"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_type": "Checking"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"new_source_balance\": 12040.25"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_74",
        "instruction": "Recognize yourself as Maria\u202fGarcia on 2025-07-24T15:30:00Z. You intend to include your friend Carla\u202fLopez as a personal beneficiary (relationship \u201cFriend\u201d) with account number 444444444 at Horizon\u202fBank (routing 111222444). Following this, transfer USD\u00a0150 from your Checking account to her and verify the new balance.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "beneficiary_name": "Carla Lopez",
                    "beneficiary_type": "Personal",
                    "relationship": "Friend",
                    "bank_name": "Horizon Bank",
                    "account_number": "444444444",
                    "routing_number": "111222444",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "beneficiary_name": "Carla Lopez"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "account_type": "Checking"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "account_id": "acc_chk_4001",
                    "requested_amount": 150.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "beneficiary_id": "bene_1",
                    "source_account_id": "acc_chk_4001",
                    "amount": 150.0,
                    "currency": "USD"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "account_type": "Checking"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"new_source_balance\": 1050.50"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_75",
        "instruction": "You are known as Lakshmi\u202fNarayanan on 2025-07-24T15:30:00Z. Plan to add your father, Narayan\u202fRao, as a personal beneficiary (relationship \u201cFather\u201d) with account number 555555555 at State\u202fBank of India (IFSC SBIN000123). After that, move INR\u202f1,000 from your Savings account to him and confirm the updated balance.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "Narayan Rao",
                    "beneficiary_type": "Personal",
                    "relationship": "Father",
                    "bank_name": "State Bank of India",
                    "account_number": "555555555",
                    "routing_number": "SBIN000123",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "Narayan Rao"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Savings"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_id": "acc_sav_5001",
                    "requested_amount": 1000.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_id": "bene_1",
                    "source_account_id": "acc_sav_5001",
                    "amount": 1000.0,
                    "currency": "INR"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Savings"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"new_source_balance\": 2,499,000.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_76",
        "instruction": "Acting as Oliver\u202fWilliams on 2025-07-24T15:30:00Z, your goal is to list your wife, Sophia\u202fWilliams, as a personal beneficiary (relationship \u201cWife\u201d) using account number 666666666 at Manchester\u202fBank (sort code 30-00-01), subsequently transfer GBP\u202f300 from your Checking account to her, and verify the updated balance.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Williams"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_name": "Sophia Williams",
                    "beneficiary_type": "Personal",
                    "relationship": "Wife",
                    "bank_name": "London Bank",
                    "account_number": "666666666",
                    "routing_number": "30-00-01",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_name": "Sophia Williams"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_type": "Checking"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_id": "acc_chk_6001",
                    "requested_amount": 300.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_id": "bene_1",
                    "source_account_id": "acc_chk_6001",
                    "amount": 300.0,
                    "currency": "GBP"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_type": "Checking"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"new_source_balance\": 550.75"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_77",
        "instruction": "In the role of Fatima\u202fAl-Fassi on 2025-07-24T15:30:00Z, you intend to designate your mother, Aisha\u202fAl-Fassi, as a personal beneficiary (relationship \u201cMother\u201d) with account number 777123777 at Emirates\u202fBank (routing EB000123), followed by transferring AED\u202f1,000 from your Savings account to her, and confirm the new balance.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Fatima",
                    "last_name": "Al-Fassi"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "beneficiary_name": "Aisha Al-Fassi",
                    "beneficiary_type": "Personal",
                    "relationship": "Mother",
                    "bank_name": "Emirates Bank",
                    "account_number": "777123777",
                    "routing_number": "EB000123",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "beneficiary_name": "Aisha Al-Fassi"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "account_type": "Savings"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "account_id": "acc_sav_7002",
                    "requested_amount": 1000.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "beneficiary_id": "bene_1",
                    "source_account_id": "acc_sav_7002",
                    "amount": 1000.0,
                    "currency": "AED"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "account_type": "Savings"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"new_source_balance\": 749000.0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_78",
        "instruction": "Identifying as Anja\u202fNovak on 2025-07-24T15:30:00Z, you aim to add your friend, Sofia\u202fLopez, as a personal beneficiary (relationship \u201cFriend\u201d) with account number 888888888 at Santander\u202fBank (routing 123456789), then proceed to transfer EUR\u202f500 from your Checking account to her, and verify the updated balance.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Anja",
                    "last_name": "Novak"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "beneficiary_name": "Sofia Lopez",
                    "beneficiary_type": "Personal",
                    "relationship": "Friend",
                    "bank_name": "Santander Bank",
                    "account_number": "888888888",
                    "routing_number": "123456789",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "beneficiary_name": "Sofia Lopez"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "account_type": "Checking"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "account_id": "acc_chk_19001",
                    "requested_amount": 500.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "beneficiary_id": "bene_1",
                    "source_account_id": "acc_chk_19001",
                    "amount": 500.0,
                    "currency": "EUR"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "account_type": "Checking"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"new_source_balance\": 3000.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_79",
        "instruction": "Taking on the persona of Yara\u202fHaddad on 2025-07-24T15:30:00Z, your task is to add your son, Noah\u202fJohnson, as a personal beneficiary (relationship \u201cSon\u201d) with account number 111111111 at Metro\u202fBank (routing 111000999), then continue to transfer USD\u202f300 from your Checking account to him, and validate the new balance.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Yara",
                    "last_name": "Haddad"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "beneficiary_name": "Noah Johnson",
                    "beneficiary_type": "Personal",
                    "relationship": "Son",
                    "bank_name": "Metro Bank",
                    "account_number": "111111111",
                    "routing_number": "111000999",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "beneficiary_name": "Noah Johnson"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "account_type": "Checking"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "account_id": "acc_chk_21001",
                    "requested_amount": 300.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "beneficiary_id": "bene_1",
                    "source_account_id": "acc_chk_21001",
                    "amount": 300.0,
                    "currency": "USD"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "account_id": "acc_chk_21001"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\"",
                "\"new_source_balance\": 14700.00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_80",
        "instruction": "You are posing as David\u202fChen. The task is to apply for a home loan amounting to USD\u202f250,000 over a term of 300\u202fmonths to fund the purchase of a new property. Proceed by submitting a new loan application and afterward check the application status.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "loan_type": "Home",
                    "requested_amount": 250000.0,
                    "requested_term_months": 300,
                    "purpose": "Home Purchase"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "loan_type": "Home"
                }
            }
        ],
        "outputs": [
                "\"application_id\": \"app_13\"",
                "\"application_status\": \"Submitted\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_81",
        "instruction": "Your name is Maria\u202fGarcia. You intend to apply for a home loan of USD\u202f320,000 over 360\u202fmonths to buy a new home. Submit a new loan application and then check its status.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "loan_type": "Home",
                    "requested_amount": 320000.0,
                    "requested_term_months": 360,
                    "purpose": "Home Purchase"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "loan_type": "Home"
                }
            }
        ],
        "outputs": [
                "\"application_id\": \"app_14\"",
                "\"application_status\": \"Submitted\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_82",
        "instruction": "You are Oliver\u202fWilliams. You plan to apply for a home loan of GBP\u202f200,000 over 300\u202fmonths to purchase a townhome. Submit a new loan application and then retrieve its status.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Williams"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "loan_type": "Home",
                    "requested_amount": 200000.0,
                    "requested_term_months": 300,
                    "purpose": "Townhome Purchase"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "loan_type": "Home"
                }
            }
        ],
        "outputs": [
                "\"application_id\": \"app_15\"",
                "\"application_status\": \"Submitted\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_83",
        "instruction": "Your name is Lakshmi\u202fNarayanan. You wish to apply for a home loan of INR\u202f5,000,000 over 240\u202fmonths to purchase a villa. Submit a new loan application and then check its status.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "CreateNewLoanApplication",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "loan_type": "Home",
                    "requested_amount": 5000000.0,
                    "requested_term_months": 240,
                    "purpose": "Villa Purchase"
                },
            },
            {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "loan_type": "Home"
                }
            }
        ],
        "outputs": [
                "\"application_id\": \"app_16\"",
                "\"application_status\": \"Submitted\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_84",
        "instruction": "You are Noah\u202fKim. Your Checking account faces a hacking threat, so for security reasons, you wish to block it. You are using your Mobile app to file the ticket. Please open a support ticket to block that Checking account, then mark the ticket resolved.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Kim"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "priority": "High",
                    "channel": "Mobile App",
                    "category": "Security",
                    "target_entity": "Account",
                    "target_id": "acc_chk_16001",
                    "operation": "BlockAccount"
                },
            },
            {
                "name": "BlockAccountForCustomerId",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "account_id": "acc_chk_16001"
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "ticket_id": "tkt_1",
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "account_id": "acc_chk_16001"
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"tkt_1\"",
                "\"account_id\": \"acc_chk_16001\", \"status\": \"Blocked\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_85",
        "instruction": "Your name is Anja\u202fNovak. Your Checking account is being scammed, so for security, you wish to block it. You are using your Web portal to file the ticket. Please open a support ticket to block that Checking account, then mark the ticket resolved.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Anja",
                    "last_name": "Novak"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "priority": "High",
                    "channel": "Web portal",
                    "category": "Security",
                    "target_entity": "Account",
                    "target_id": "acc_chk_19001",
                    "operation": "BlockAccount"
                },
            },
            {
                "name": "BlockAccountForCustomerId",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "account_id": "acc_chk_19001"
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "ticket_id": "tkt_1",
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "account_id": "acc_chk_19001"
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"tkt_1\"",
                "\"account_id\": \"acc_chk_19001\", \"status\": \"Blocked\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_86",
        "instruction": "Your name is Jane\u202fSmith. It is necessary to transfer CAD\u202f100 from your Checking account (acc_chk_2001) to the beneficiary Kenji Tanaka, then determine your total balance across all of your accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_name": "Kenji Tanaka"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_id": "acc_chk_2001",
                    "requested_amount": 100.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "source_account_id": "acc_chk_2001",
                    "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f",
                    "amount": 100.0,
                    "currency": "CAD"
                },
            },
            {
                "name": "CalculateTotalBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_ids": [
                        "acc_chk_2001",
                        "acc_sav_2002"
                    ]
                }
            }
        ],
        "outputs": [
                "\"total_balance\": 25000.75\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_87",
        "instruction": "You are Fatima\u202fAl-Fassi. Transfer AED 1000 from your Savings account (acc_sav_7002) to the beneficiary Abu Dhabi International School, then compute your total balance across all accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Fatima",
                    "last_name": "Al-Fassi"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "beneficiary_name": "Dubai International School"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "account_id": "acc_sav_7002",
                    "requested_amount": 1000.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "source_account_id": "acc_sav_7002",
                    "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f",
                    "amount": 1000.0,
                    "currency": "AED"
                },
            },
            {
                "name": "CalculateTotalBalance",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "account_ids": [
                        "acc_chk_7001",
                        "acc_sav_7002"
                    ]
                }
            }
        ],
        "outputs": [
                "\"total_balance\": 899000.00\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_88",
        "instruction": "You are Fatima\u202fAl-Fassi. Transfer AED 1000 from your Savings account (acc_sav_7002) to the beneficiary Abu Dhabi International School, then compute your total balance across all accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Fatima",
                    "last_name": "Al-Fassi"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "beneficiary_name": "Dubai International School"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "account_id": "acc_sav_7002",
                    "requested_amount": 1000.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "source_account_id": "acc_sav_7002",
                    "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f",
                    "amount": 1000.0,
                    "currency": "AED"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"
                },
            },
            {
                "name": "CalculateTotalBalance",
                "arguments": {
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                    "account_ids": [
                        "acc_chk_7001",
                        "acc_sav_7002"
                    ]
                }
            }
        ],
        "outputs": [
                "\"total_balance\": 899000.00\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_89",
        "instruction": "Your name is Jane\u202fSmith. You need to initiate a transfer of CAD\u202f1000 from your Checking account (acc_chk_2001) to your beneficiary Kenji Tanaka, then assess your total balance across all of your accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_name": "Kenji Tanaka"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_id": "acc_chk_2001",
                    "requested_amount": 1000.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "source_account_id": "acc_chk_2001",
                    "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f",
                    "amount": 1000.0,
                    "currency": "CAD"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
                },
            },
            {
                "name": "CalculateTotalBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_ids": [
                        "acc_chk_2001",
                        "acc_sav_2002"
                    ]
                }
            }
        ],
        "outputs": [
                "\"total_balance\": 24100.75\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_90",
        "instruction": "You are Lakshmi\u202fNarayanan. You must transfer INR\u202f2,000 from your Checking account (acc_chk_5002) to your beneficiary Global\u202fISP, then evaluate your total balance across all your accounts.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "Global ISP"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_id": "acc_chk_5002",
                    "requested_amount": 2000.0
                },
            },
            {
                "name": "PayToBeneficiarySameCurrency",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "source_account_id": "acc_chk_5002",
                    "beneficiary_id": "bene_5e4f3a2b-1c9d-8e7f-6a5b-4c3d2e1f0a9b",
                    "amount": 2000.0,
                    "currency": "INR"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "CalculateTotalBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_ids": [
                        "acc_chk_5002",
                        "acc_sav_5001"
                    ]
                }
            }
        ],
        "outputs": [
                "\"total_balance\": 2548000.0\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_91",
        "instruction": "You are Elena Popescu on 2025-07-24T15:30:00Z. Include a new personal beneficiary titled Ryan Smith (your brother) at Maple Bank, account number 987654321, routing number 122105155.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_name": "Ryan Smith",
                    "beneficiary_type": "Personal",
                    "relationship": "Brother",
                    "bank_name": "Maple Bank",
                    "account_number": "987654321",
                    "routing_number": "122105155",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_name": "Ryan Smith"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\",\"beneficiary_name\": \"Ryan Smith\",\"beneficiary_type\": \"Personal\",\"relationship\": \"Brother\",\"account_details\": {\"bank_name\": \"Maple Bank\", \"account_number\": \"987654321\", \"routing_number\": \"122105155\"},\"date_added\": \"2025-07-24\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_92",
        "instruction": "You are Zoltan Nagy on 2025-07-24T15:30:00Z. Incorporate a new personal beneficiary named Alex Lee (your friend) at City National Bank, account number 111222333, routing number 021000089.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Alex Lee",
                    "beneficiary_type": "Personal",
                    "relationship": "Friend",
                    "bank_name": "City National Bank",
                    "account_number": "111222333",
                    "routing_number": "021000089",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Alex Lee"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\",\"beneficiary_name\": \"Alex Lee\",\"beneficiary_type\": \"Personal\",\"relationship\": \"Friend\",\"account_details\": {\"bank_name\": \"City National Bank\", \"account_number\": \"111222333\", \"routing_number\": \"021000089\"},\"date_added\": \"2025-07-24\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_93",
        "instruction": "You are Kenji\u202fTanaka. Since your password for Checking account (acc_chk_10001) is compromised, block it for security reasons. Use your Web Portal to file the ticket. Please submit a support ticket to block that Checking account, then mark the ticket resolved.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Kenji",
                    "last_name": "Tanaka"
                },
            },
            {
                "name": "AddSupportTicketForCustomerId",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "priority": "High",
                    "channel": "Web Portal",
                    "category": "Security",
                    "target_entity": "Account",
                    "target_id": "acc_chk_10001",
                    "operation": "BlockAccount"
                },
            },
            {
                "name": "BlockAccountForCustomerId",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "account_id": "acc_chk_10001"
                },
            },
            {
                "name": "ChangeSupportTicketStatus",
                "arguments": {
                    "ticket_id": "tkt_1",
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "new_status": "Resolved"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "account_id": "acc_chk_10001"
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"tkt_1\"",
                "\"account_id\": \"acc_chk_10001\", \"status\": \"Blocked\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_94",
        "instruction": "You are Sofia Andersson on 2025-07-24T15:30:00Z. Insert a new personal beneficiary called Sophia Williams (your wife) at Manchester Bank, account number 555666777, routing number 040000000.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Williams"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_name": "Sophia Williams",
                    "beneficiary_type": "Personal",
                    "relationship": "Wife",
                    "bank_name": "London Bank",
                    "account_number": "555666777",
                    "routing_number": "040000000",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_name": "Sophia Williams"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\",\"beneficiary_name\": \"Sophia Williams\",\"beneficiary_type\": \"Personal\",\"relationship\": \"Wife\",\"account_details\": {\"bank_name\": \"London Bank\", \"account_number\": \"555666777\", \"routing_number\": \"040000000\"},\"date_added\": \"2025-07-24T15:30:00Z\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_95",
        "instruction": "You are Zoltan Nagy on 2025-07-24T15:30:00Z. Enter a new personal beneficiary titled Narayan Rao (your father) at State Bank of India, account number 888999000, routing number SBIN000123.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "AddNewBeneficiaryForCustomer",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "Narayan Rao",
                    "beneficiary_type": "Personal",
                    "relationship": "Father",
                    "bank_name": "State Bank of India",
                    "account_number": "888999000",
                    "routing_number": "SBIN000123",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            },
            {
                "name": "GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_name": "Narayan Rao"
                }
            }
        ],
        "outputs": [
                "\"beneficiary_id\": \"bene_1\",\"beneficiary_name\": \"Narayan Rao\",\"beneficiary_type\": \"Personal\",\"relationship\": \"Father\",\"account_details\": {\"bank_name\": \"State Bank of India\", \"account_number\": \"888999000\", \"routing_number\": \"SBIN000123\"},\"date_added\": \"2025-07-24T15:30:00Z\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_96",
        "instruction": "Assume you are Elena Popescu and initiate the creation of a new Savings account, followed by an immediate transfer of CAD\u00a0600 from your existing Checking account into it.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Jane",
                    "last_name": "Smith"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Savings"
                },
            },
            {
                "name": "CreateNewAccountForCustomer",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Savings",
                    "account_type_code": "sav",
                    "currency": "CAD"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_id": "acc_1"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_id": "acc_chk_2001",
                    "requested_amount": 600.0
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "source_account_id": "acc_chk_2001",
                    "target_account_id": "acc_1",
                    "currency": "CAD",
                    "amount": 600.0
                }
            }
        ],
        "outputs": [
                "\"message\": \"Transfer successful (same currency).\",\"source_account_id\": \"acc_chk_2001\",\"target_account_id\": \"acc_1\",\"amount_transferred\": 600.0,\"currency\": \"CAD\",\"source_balance\": 2500.75,\"target_balance\": 600.0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_97",
        "instruction": "Assume you are Zoltan Nagy and open a new Savings account, then promptly transfer USD\u00a0800 from your existing Checking account into it.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Chen"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Savings"
                },
            },
            {
                "name": "CreateNewAccountForCustomer",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_type": "Savings",
                    "account_type_code": "sav",
                    "currency": "USD"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_1"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "account_id": "acc_chk_3001",
                    "requested_amount": 800.0
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "source_account_id": "acc_chk_3001",
                    "target_account_id": "acc_1",
                    "currency": "USD",
                    "amount": 800.0
                }
            }
        ],
        "outputs": [
                "\"message\": \"Transfer successful (same currency).\",\"source_account_id\": \"acc_chk_3001\",\"target_account_id\": \"acc_1\",\"amount_transferred\": 800.0,\"currency\": \"USD\",\"source_balance\": 8720.00,\"target_balance\": 800.0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_98",
        "instruction": "Assume you are Sofia Andersson and start by creating a new Savings account, then make an immediate transfer of USD\u00a0700 from your current Checking account into it.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Maria",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Savings"
                },
            },
            {
                "name": "CreateNewAccountForCustomer",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "account_type": "Savings",
                    "account_type_code": "sav",
                    "currency": "USD"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "account_type": "Savings"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "account_id": "acc_chk_4001",
                    "requested_amount": 700.0
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "source_account_id": "acc_chk_4001",
                    "target_account_id": "acc_1",
                    "currency": "USD",
                    "amount": 700.0
                }
            }
        ],
        "outputs": [
                "\"source_account_id\": \"acc_chk_4001\",\"target_account_id\": \"acc_1\",\"amount_transferred\": 700.0,\"currency\": \"USD\",\"source_balance\": 6550.00,\"target_balance\": 700.0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_99",
        "instruction": "Assume you are Sofia Andersson and proceed to establish a new Savings account, with an immediate transfer of GBP\u00a0400 from your current Checking account into it.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Williams"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Savings"
                },
            },
            {
                "name": "CreateNewAccountForCustomer",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_type": "Savings",
                    "account_type_code": "sav",
                    "currency": "GBP"
                },
            },
            {
                "name": "GetCustomerAccountDetailsByCustomerIdAndAccountType",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_type": "Savings"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_id": "acc_chk_6001",
                    "requested_amount": 400.0
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "source_account_id": "acc_chk_6001",
                    "target_account_id": "acc_1",
                    "currency": "GBP",
                    "amount": 400.0
                }
            }
        ],
        "outputs": [
                "\"message\": \"Transfer successful (same currency).\",\"source_account_id\": \"acc_chk_6001\",\"target_account_id\": \"acc_1\",\"amount_transferred\": 400.0,\"currency\": \"GBP\",\"source_balance\": 3200.00,\"target_balance\": 400.0"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_100",
        "instruction": "Assume you are Zoltan Nagy and initiate the process of opening a new Savings account, followed by an immediate transfer of INR\u00a050,000 from your present Checking account into it.",
        "actions": [
            {
                "name": "GetCustomerDetailsByName",
                "arguments": {
                    "first_name": "Lakshmi",
                    "last_name": "Narayanan"
                },
            },
            {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"
                },
            },
            {
                "name": "GetAccountTypeAndAccountTypeCode",
                "arguments": {
                    "account_type": "Savings"
                },
            },
            {
                "name": "CreateNewAccountForCustomer",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Savings",
                    "account_type_code": "sav",
                    "currency": "INR"
                },
            },
            {
                "name": "GetAccountDetailsByCustomerIdAndAccountId",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_id": "acc_1"
                },
            },
            {
                "name": "CheckAccountBalance",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_id": "acc_chk_5002",
                    "requested_amount": 50000.0
                },
            },
            {
                "name": "TransferMoneySameCurrency",
                "arguments": {
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "source_account_id": "acc_chk_5002",
                    "target_account_id": "acc_1",
                    "currency": "INR",
                    "amount": 50000.0
                }
            }
        ],
        "outputs": [
                "\"source_account_id\": \"acc_chk_5002\",\"target_account_id\": \"acc_1\",\"amount_transferred\": 50000.0,\"currency\": \"INR\",\"source_balance\": 0.00,\"target_balance\": 50000.0"
        ]
    }
]
