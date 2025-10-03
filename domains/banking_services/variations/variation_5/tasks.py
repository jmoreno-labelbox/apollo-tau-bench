from domains.dto import Action, Task

TASKS = [
    # 01. Create a new savings account for John Doe and transfer USD 500 from his checking into it
    Task(
        annotator="0",
        user_id="task_01",
        instruction=(
            "Handle the opening of a new Savings account as Kenji Tanaka, followed by transferring USD 500 from your current Checking account into it."
        ),
        actions=[
            # 1. Look up Kenji Tanaka
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "John", "last_name": "Doe"},
            ),
            # 2. List all of his accounts
            Action(
                name="GetAllAccountsOfCustomerByCustomerId",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            # 3. Determine the code for Savings
            Action(
                name="GetAccountTypeAndAccountTypeCode",
                kwargs={"account_type": "Savings"},
            ),
            # 4. Create the new Savings account
            Action(
                name="CreateNewAccountForCustomer",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Savings",
                    "account_type_code": "sav",
                    "currency": "USD",
                },
            ),
            # 5. Fetch details for all Savings accounts
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Savings",
                },
            ),
            Action(
                name="CheckAccountBalance",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_id": "acc_chk_1001",
                    "requested_amount": 500.0,
                },
            ),
            # 6. Transfer USD 500 from Checking to the new Savings account
            Action(
                name="TransferMoneySameCurrency",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_chk_1001",
                    "target_account_id": "acc_1",
                    "currency": "USD",
                    "amount": 500.0,
                },
            ),
        ],
        outputs=[
            '"message": "Transfer successful (same currency).",'
            '"source_account_id": "acc_chk_1001",'
            '"target_account_id": "acc_1",'
            '"amount_transferred": 500.0,'
            '"currency": "USD",'
            '"source_balance": 4730.50,'
            '"target_balance": 500.0'
        ],
    ),

    # 02. Add an existing beneficiary for Jane Smith and send her USD 200 from Checking → Savings
    Task(
        annotator="0",
        user_id="task_02",
        instruction=(
            "Coordinate a transfer of CAD 250 from your Checking account to your personal beneficiary, Kenji Tanaka, as Elena Popescu."
        ),
        actions=[
            # 1. Look up Elena Popescu
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "Jane", "last_name": "Smith"},
            ),
            # 2. List her accounts
            Action(
                name="GetAllAccountsOfCustomerByCustomerId",
                kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
            ),
            # 3. Fetch her Checking account details (to check balance)
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_type": "Checking",},
            ),
            Action(
                name="CheckAccountBalance",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "account_id": "acc_chk_2001",
                    "requested_amount": 250.0,
                },
            ),
            # 4. Get details for beneficiary “Kenji Tanaka”
            Action(
                name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "beneficiary_name": "Kenji Tanaka",
                },
            ),
            # 5. (Optional) Compute how much CAD is needed for USD 200
            Action(
                name="GetCurrencyConversionAmount",
                kwargs={
                    "source_currency": "CAD",
                    "source_amount": 250.0,
                    "target_currency": "USD",
                },
            ),
            # 6. Pay to John Doe with conversion
            Action(
                name="PayToBeneficiaryWithConversion",
                kwargs={
                    "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f",
                    "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                    "source_account_id": "acc_chk_2001",
                    "source_amount": 250.0,
                    "source_currency": "CAD",
                    "target_currency": "USD",
                },
            ),
        ],
        outputs=[
            "\"message\": \"Paid 200.00 USD to beneficiary 'Kenji Tanaka'.\", "
            "\"source_account_id\": \"acc_chk_2001\", "
            "\"beneficiary_account_number\": \"1122334455\", "
            "\"source_amount\": 250.0, "
            "\"source_currency\": \"CAD\", "
            "\"target_amount\": 200.0, "
            "\"target_currency\": \"USD\", "
            "\"new_source_balance\": 2850.75\""
        ],
    ),


    # # 03. Oliver Williams set up a recurring monthly payment to Utility Co.
    Task(
        annotator="0",
        user_id="task_03",
        instruction=(
            "As Sofia Andersson, schedule a monthly GBP 100 payment beginning next month on the date 2025-08-24 from your Checking account to your business beneficiary, Manchester Electricity Co."
        ),
        actions=[
            # 1. Look up Sofia Andersson
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "Oliver", "last_name": "Williams"},
            ),
            # 2. List all of her accounts
            Action(
                name="GetAllAccountsOfCustomerByCustomerId",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"},
            ),
            # 3. Fetch her Checking account details
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_type": "Checking",
                },
            ),
            # 4. Get details for business beneficiary Manchester Electricity Co.
            Action(
                name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_name": "London Electricity Co.",
                },
            ),
            # 5. Check balance of the source account for GBP 100
            Action(
                name="CheckAccountBalance",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_id": "acc_chk_6001",
                    "requested_amount": 100.0,
                },
            ),
            # 6. Schedule the monthly payment starting 2025-08-24
            Action(
                name="CreateNewSchedulePayment",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "source_account_id": "acc_chk_6001",
                    "beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d",
                    "amount": 100.0,
                    "currency": "GBP",
                    "frequency": "Monthly",
                    "start_date": "2025-08-24",
                },
            ),
        ],
        outputs=[
            "\"payment_id\": \"sp_1\", \"customer_id\": \"b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5\", "
            "\"source_account_id\": \"acc_chk_6001\", \"beneficiary_id\": \"bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d\", "
            "\"amount\": 100.0, \"currency\": \"GBP\", \"frequency\": \"Monthly\", "
            "\"start_date\": \"2025-08-24\", \"next_payment_date\": \"2025-09-24\", "
            "\"end_date\": null, \"status\": \"Active\""
        ],
    ),

    # # 04. David Brown → (use David Chen) apply for a personal loan of USD 5,000 and notify him
    Task(
        annotator="0",
        user_id="task_04",
        instruction=(
            "David Chen, proceed with applying for a home improvement personal loan of USD 5,000 over 24 months, using your property located at address '123 Maple Street, Springfield' as collateral."
        ),
        actions=[
            # 1. Look up Zoltan Nagy
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "David", "last_name": "Chen"},
            ),
            # 2. Submit the loan application for 24 months with collateral info
            Action(
                name="CreateNewLoanApplication",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "loan_type": "Personal",
                    "requested_amount": 5000.0,
                    "requested_term_months": 24,
                    "purpose": "Home improvement",
                },
            ),
            # 3. Process the application
            Action(
                name="ProcessLoanApplicationId",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "application_id": "app_1"
                    },
            ),
            # 4. Check application status
            Action(
                name="GetLoanApplicationStatusByCustomerIdAndType",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "loan_type": "Personal",
                },
            ),
            # 5. Create the actual loan record against the property collateral
            Action(
                name="AddNewLoanForCustomer",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "application_id": "app_1",
                    "collateral_type": "Property",
                    "collateral_info": "123 Maple Street, Springfield",
                    "currency": "USD",
                },
            )

        ],
        outputs=[
            "\"loan_id\": \"loan_1\",\"loan_account_id\": \"loanacc_1\" \"application_id\": \"app_1\", \"status\": \"Approved\""
        ],
    ),

    # # 05
    Task(
        annotator="0",
        user_id="task_05",
        instruction=(
            "Arrange to pay USD 500 from your Savings account to your Credit Card account as Kenji Tanaka, and subsequently verify the balances in your Checking, Savings, and Credit Card accounts."
        ),
        actions=[
            # 1. Look up Kenji Tanaka
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "John", "last_name": "Doe"},
            ),
            # 2. List all of his account IDs
            Action(
                name="GetAllAccountsOfCustomerByCustomerId",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            # 3. Pay USD 500 from Savings to Credit Card
            Action(
                name="TransferMoneySameCurrency",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_sav_1002",
                    "target_account_id": "acc_crd_1003",
                    "currency": "USD",
                    "amount": 500.0,
                },
            ),
            # 4. Fetch updated Checking account details
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Checking",
                },
            ),
            # 5. Fetch updated Savings account details
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Savings",
                },
            ),
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Credit Card",
                },
            ),
        ],
        outputs=[
            "\"message\": \"Transfer successful (same currency).\","
            "\"source_account_id\": \"acc_sav_1002\","
            "\"target_account_id\": \"acc_crd_1003\","
            "\"amount_transferred\": 500.0,"
            "\"currency\": \"USD\","
            "\"account_type\": \"Checking\", \"balance\": 5230.50\"",
            "\"account_type\": \"Savings\", \"balance\": 15280.00\"",
            "\"account_type\": \"Credit Card\", \"balance\": -2000.00\""
        ],
    ),

    # # # 06
    Task(
        annotator="0",
        user_id="task_06",
        instruction=(
            "You are Sofia Andersson. "
            "You have relocated to a new address (789 Pine Street, College Town, TX 77840) and updated your phone number to 555-222-3333, designating it as primary. "
            "Amend your profile and then retrieve your updated record."
        ),
        actions=[
            # 1. Look up Sofia Andersson
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "Maria", "last_name": "Garcia"},
            ),
            # 2. Open a support ticket for the profile update
            Action(
                name="AddSupportTicketForCustomerId",
                kwargs={
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
            ),
            # 3. Update the mailing address
            Action(
                name="UpdateAddressForCustomerId",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "mailing_address": {
                        "street_address": "789 Pine Street",
                        "city": "College Town",
                        "state": "TX",
                        "postal_code": "77840",
                        "country": "USA"
                    },
                    "set_as_primary": True
                },
            ),
            # 4. Update the phone number
            Action(
                name="UpdateContactNumberOfCustomerId",
                kwargs={
                    "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                    "new_phone_number": "555-222-3333",
                    "set_as_primary": True
                },
            ),
            # 5. Close the support ticket
            Action(
                name="ChangeSupportTicketStatus",
                kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                        "ticket_id": "tkt_1", "new_status": "Resolved"},
            ),
            # 6. Fetch the updated customer record by ID
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "Maria", "last_name": "Garcia"},
            ),
        ],
        outputs=[
            "\"customer_id\": \"f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9\", "
            "\"mailing_address\": {\"street_address\": \"789 Pine Street\", \"city\": \"College Town\", "
            "\"state\": \"TX\", \"postal_code\": \"77840\", \"country\": \"USA\"}, "
            "\"phone_numbers\": [{\"type\": \"Mobile\", \"number\": \"555-222-3333\", \"is_primary\": true}]"
        ],
    ),

    # # # 07
    Task(
        annotator="0",
        user_id="task_07",
        instruction=(
            "You are John Doe. "
            "You have your monthly salary of USD 3,000 deposited by Employer Inc. "
            "into your Checking account. "
            "Proceed to transfer 20% which totals USD 600 from Checking to your Savings account, and subsequently verify the balances in both accounts."
        ),
        actions=[
            # 1. Look up Kenji Tanaka
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "John", "last_name": "Doe"},
            ),
            # 2. List all of his accounts
            Action(
                name="GetAllAccountsOfCustomerByCustomerId",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
            # 3. Fetch current Checking account details
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Checking",
                },
            ),

            # 4. Receive salary payment of USD 3,000 into Checking
            Action(
                name="ReceivePayment",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_id": "acc_chk_1001",
                    "amount": 3000.0,
                    "currency": "USD",
                },
            ),

            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Savings",
                },
            ),

            Action(
                name="TransferMoneySameCurrency",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_chk_1001",
                    "target_account_id": "acc_sav_1002",
                    "currency": "USD",
                    "amount": 600.0,
                },
            ),

            # 7. Confirm Checking balance
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Checking",
                },
            ),
            # 8. Confirm Savings balance
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Savings",
                },
            ),
        ],
        outputs=[
            "\"account_type\": \"Checking\", \"balance\": 7630.50\"",
            "\"account_type\": \"Savings\", \"balance\": 16380.00\""
        ],
    ),

    # # 08
    Task(
    annotator=0,
    user_id="task_08",
    instruction=(
            "You are Chloe Dubois. "
            "You must transfer EUR 200 from your Checking account (acc_chk_9001) to your beneficiary Marie Dubois, then assess your total balance across all accounts."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Chloe ", "last_name": "Dubois"},
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "beneficiary_name": "Marie Dubois"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "account_id": "acc_chk_9001",
                "requested_amount": 200.0
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "source_account_id": "acc_chk_9001",
                "beneficiary_id": "bene_4f3a2b1c-9d8e-7f6a-5b4c-3d2e1f0a9b8c",
                "amount": 200.0,
                "currency": "EUR"
            },
        ),
        Action(
            name="CalculateTotalBalance",
            kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                "account_ids": ["acc_chk_9001","acc_crd_9002"]
            },
        ),
    ],
    outputs=[
        "\"total_balance\": 2500.00\",\"Currency\": \"EUR\""
    ],
),
    # # 09
    Task(
        annotator="0",
        user_id="task_09",
        instruction=(
            "You are Kenji Tanaka on 2025-07-24T15:30:00Z. "
            "Introduce a new personal beneficiary named Jane Doe (your sister) at ABC Bank, with the account number 123456789 and routing number 021000021."
        ),
        actions=[
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "John", "last_name": "Doe"},
            ),
            # 1. Add the new beneficiary for Kenji Tanaka
            Action(
                name="AddNewBeneficiaryForCustomer",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Jane Doe",
                    "beneficiary_type": "Personal",
                    "relationship": "Sister",
                    "bank_name": "ABC Bank",
                    "account_number": "123456789",
                    "routing_number": "021000021",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            ),
            # 2. Fetch the newly added beneficiary’s details
            Action(
                name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Jane Doe"
                },
            ),
        ],
        outputs=[
            "\"beneficiary_id\": \"bene_1\","
            "\"beneficiary_name\": \"Jane Doe\","
            "\"beneficiary_type\": \"Personal\","
            "\"relationship\": \"Sister\","
            "\"account_details\": {\"bank_name\": \"ABC Bank\", \"account_number\": \"123456789\", \"routing_number\": \"021000021\"},"
            "\"date_added\": \"2025-07-24T15:30:00Z\""
        ],
    ),

    # # 10
    Task(
        annotator="0",
        user_id="task_10",
        instruction=(
            "You are Zoltan Nagy. Remove your beneficiary Metropolis Power & Light from your list."
        ),
        actions=[
            # 1. Look up Kenji Tanaka
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "David", "last_name": "Chen"},
            ),
            # 2. Get details for beneficiary “Metropolis Power & Light” to obtain beneficiary_id
            Action(
                name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                kwargs={
                    "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                    "beneficiary_name": "Metropolis Power & Light",
                },
            ),
            # 3. Remove the beneficiary by ID
            Action(
                name="RemoveBeneficiaryByBeneficiaryId",
                kwargs={
                "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a",
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                },
            ),
            # 4. Confirm removal by listing all remaining beneficiaries
            Action(
                name="GetAllBeneficiariesForCustomerId",
                kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"},
            ),
        ],
        outputs=[
        "\"status\": \"Removed\", "
        "\"remaining_beneficiaries\": []\""
        ],
    ),

    # # 11
    Task(
        annotator="0",
        user_id="task_11",
        instruction=(
            "You are Liam O'Connor. To ensure security, limit access to your Checking account."
        ),
        actions=[
            Action(
                    name="GetCustomerDetailsByName",
                    kwargs={"first_name": "Liam", "last_name": "O'Connor"},
                ),
                # 2. List all of his accounts
            Action(
                name="GetAllAccountsOfCustomerByCustomerId",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11"},
            ),
            # 3. Determine the code for Savings
            Action(
                name="GetAccountTypeAndAccountTypeCode",
                kwargs={"account_type": "Checking"},
            ),
            Action(
                    name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                    kwargs={
                        "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                        "account_type": "Checking",
                    },
                ),
            # 2. Create a high‐priority support ticket for blocking the account
            Action(
                name="AddSupportTicketForCustomerId",
                kwargs={
                    "customer_id":    "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "priority":       "High",
                    "channel":        "Web Portal",
                    "category":       "Security",
                    "target_id":      "acc_chk_12001",
                    "target_entity":  "Account",
                    "operation":      "Block",
                    "parameters":     {}
                },
            ),
            # 3. Block the account
            Action(
                name="BlockAccountForCustomerId",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "account_id":  "acc_chk_12001"
                },
            ),
            # 4. Confirm the updated account details by customer_id and account_type
            Action(
                name="GetAccountDetailsByCustomerIdAndAccountId",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "account_id":  "acc_chk_12001"
                },
            ),
        ],
        outputs=[
            "\"ticket_id\": \"tkt_1\","
            "\"status\": \"Blocked\","
            "\"account_id\": \"acc_chk_12001\","
            "\"account_type\": \"Checking\","
            "\"balance\": 4500.00\""
        ],
    ),

    # # 12
    Task(
        annotator="0",
        user_id="task_12",
        instruction=(
            "You are Zoltan Nagy. "
            "You are checking on the progress of your Business loan application. "
            "You intend to create a support ticket for further information."
        ),
        actions=[
            # 1. Look up the customer by name
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "Liam", "last_name": "O'Connor"},
            ),
            # 2. Check the current status of their Personal loan application
            Action(
                name="GetLoanApplicationStatusByCustomerIdAndType",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "loan_type":   "Business"
                },
            ),
            # 3. If the status is still Pending, create a medium‑priority support ticket
            Action(
                name="AddSupportTicketForCustomerId",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-11",
                    "priority":    "Medium",
                    "channel":     "Web Portal",
                    "category":    "Loan Inquiry",
                    "target_id":   "app_b1c2d3e4-f5a6-b7c8-d9e0-f1a2b3c4d5e6",
                    "target_entity": "Loan Application",
                    "operation":   "Inquiry",
                    "parameters":  {}
                },
            ),
        ],
        outputs=[
            # If pending:
            "\"ticket_id\": \"tkt_1\", \"status\": \"Open\", \"category\": \"Loan Inquiry\", \"target_id\": \"app_b1c2d3e4-f5a6-b7c8-d9e0-f1a2b3c4d5e6\""
        ],
    ),


    # # 13
    Task(
    annotator="0",
    user_id="task_13",
    instruction=(
            "You are John Doe. "
            "You've relocated to a new address at 456 Elm St, Newcity, AZ 85001, USA. "
            "Kindly document this change by generating a support ticket and subsequently updating your residential address."
        ),
    actions=[
        # 1. Look up the customer by name
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "John", "last_name": "Doe"},
        ),
        # 2. Open a support ticket for the address change
        Action(
            name="AddSupportTicketForCustomerId",
            kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "priority": "Medium",
                "channel": "Web Portal",
                "category": "Profile Update",
                "target_id":   "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
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
        ),
        # 3. Apply the address update
        Action(
            name="UpdateAddressForCustomerId",
            kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "residential_address": {
                    "street_address": "456 Elm St",
                    "city": "Newcity",
                    "state": "AZ",
                    "postal_code": "85001",
                    "country": "USA"
                }
            },
        ),
        # 4. Close the support ticket
        Action(
            name="ChangeSupportTicketStatus",
            kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e","ticket_id": "tkt_1", "new_status": "Resolved"},
        ),
        # 5. Verify the updated customer record
        Action(
            name="GetCustomerDetailsByCustomerId",
            kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
        ),
        ],
        outputs=[
            "\"customer_id\": \"c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e\"",
            "\"residential_address\": {"
                "\"street_address\": \"456 Elm St\", "
                "\"city\": \"Newcity\", "
                "\"state\": \"AZ\", "
                "\"postal_code\": \"85001\", "
                "\"country\": \"USA\""
            "}"
        ],
    ),

    ## 14
    Task(
        annotator=0,
        user_id="task_14",
        instruction=(
            "You are John Doe on 2025-07-24T15:30:00Z. "
            "You wish to add a new personal beneficiary named Alice Johnson (your friend) at Metro Bank with account number 555123456 and routing number 111000025. "
            "Then, move USD 300 from your Checking account (acc_chk_1001) to this beneficiary, and afterward, eliminate the beneficiary from your list."
        ),
        actions=[
            # 1. Look up Kenji Tanaka
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "John", "last_name": "Doe"},
            ),
            # 2. Add the new beneficiary
            Action(
                name="AddNewBeneficiaryForCustomer",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",  # Kenji Tanaka’s ID :contentReference[oaicite:1]{index=1}
                    "beneficiary_name": "Alice Johnson",
                    "beneficiary_type": "Personal",
                    "relationship": "Friend",
                    "bank_name": "Metro Bank",
                    "account_number": "555123456",
                    "routing_number": "111000025",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            ),
            # 3. Fetch the newly added beneficiary’s details to get its ID
            Action(
                name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Alice Johnson"
                },
            ),
            # 4. Check that John’s Checking account has at least USD 300
            Action(
                name="CheckAccountBalance",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_id": "acc_chk_1001",
                    "requested_amount": 300.0
                },
            ),
            # 5. Pay the beneficiary in the same currency
            Action(
                name="PayToBeneficiarySameCurrency",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_1",
                    "source_account_id": "acc_chk_1001",
                    "amount": 300.0,
                    "currency": "USD"
                },
            ),
            # 6. Remove the beneficiary
            Action(
                name="RemoveBeneficiaryByBeneficiaryId",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_1"
                },
            ),
            # 7. Verify removal by listing all beneficiaries
            Action(
                name="GetAllBeneficiariesForCustomerId",
                kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
            ),
        ],
        outputs=[
            # From step 2
            "\"beneficiary_id\": \"bene_1\"",
            # From step 5
            "\"new_source_balance\": 4930.50",
            # From step 6
            "\"status\": \"Beneficiary removed successfully.\"",
            # From step 7: final list should exclude Alice Johnson
            # Elena Popescu…
            "{\"beneficiary_id\": \"bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d\", "
            "\"beneficiary_name\": \"Elena Popescu\", "
            "\"beneficiary_type\": \"Personal\", "
            "\"relationship\": \"Friend\", "
            "\"account_details\": {\"account_number\": \"9876543210\", \"bank_name\": \"City National Bank\", \"routing_number\": \"122000661\", \"country\": \"USA\"}}",  # :contentReference[oaicite:4]{index=4}
            # Anytown Utility Services…
            "{\"beneficiary_id\": \"bene_8b7c6d5e-4f3a-2b1c-9d8e-7f6a5b4c3d2e\", "
            "\"beneficiary_name\": \"Anytown Utility Services\", "
            "\"beneficiary_type\": \"Business\", "
            "\"relationship\": \"Utility Provider\", "
            "\"account_details\": {\"account_number\": \"5555666677\", \"bank_name\": \"Bank of Anytown\", \"routing_number\": \"021000021\", \"country\": \"USA\"}}",  # :contentReference[oaicite:5]{index=5}
        ],
    ),

    # # 15
    Task(
        annotator=0,
        user_id="task_15",
        instruction=(
            "You are Chloe Dubois. "
            "Your credit card ending in 2424 has been misplaced. "
            "Using your Mobile app, please initiate a support ticket to block that credit card, and then mark the ticket as resolved."
        ),
        actions=[
            # 1. Look up Kenji Tanaka’s customer record
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "Chloe", "last_name": "Dubois"},
            ),
            # 2. Open a support ticket to block the lost card
            Action(
                name="AddSupportTicketForCustomerId",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",  # Kenji Tanaka’s ID :contentReference[oaicite:2]{index=2}
                    "priority": "High",
                    "channel": "Mobile App",
                    "category": "Card Loss",
                    "target_entity": "Account",
                    "target_id": "acc_crd_9002",  # Chloe’s credit card :contentReference[oaicite:3]{index=3}
                    "operation": "BlockAccount",
                },
            ),
            # 3. Block the credit card account
            Action(
                name="BlockAccountForCustomerId",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "account_id": "acc_crd_9002"
                },
            ),
            # 4. Close the support ticket
            Action(
                name="ChangeSupportTicketStatus",
                kwargs={"ticket_id": "tkt_1","customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2", "new_status": "Resolved"},
            ),
            # 5. Verify that the credit card status is now blocked
            Action(
                name="GetAccountDetailsByCustomerIdAndAccountId",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "account_id": "acc_crd_9002"
                },
            ),
        ],
        outputs=[
            # From step 2
            "\"ticket_id\": \"tkt_1\"",
            "\"account_id\": \"acc_crd_9002\", \"status\": \"Blocked\""
        ],
    ),

    ##16
    Task(
        annotator=0,
        user_id="task_16",
        instruction=(
            "Assume the identity of John Doe. "
            "Seek to obtain a home loan amounting to USD 250000 over a span of 360 months for the purpose of purchasing a new home. "
            "Kindly initiate a new loan application with the loan type 'Mortgage' for 'Home Purchase' and proceed to check its status thereafter."
        ),
        actions=[
            # 1. Look up Kenji Tanaka’s customer record
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "John", "last_name": "Doe"},
            ),
            # 2. Create a new loan application for a home loan
            Action(
                name="CreateNewLoanApplication",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",  # John Doe’s ID :contentReference[oaicite:1]{index=1}
                    "loan_type": "Mortgage",
                    "requested_amount": 250000.0,
                    "requested_term_months": 360,
                    "purpose": "Home Purchase"
                },
            ),
            # 3. Check the status of the newly created home loan application
            Action(
                name="GetLoanApplicationStatusByCustomerIdAndType",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "loan_type": "Mortgage"
                },
            ),
        ],
        outputs=[
            "\"application_id\": \"app_1\"",
            "\"application_status\": \"Submitted\""
        ],
    ),

    # 17
    Task(
        annotator=0,
        user_id="task_17",
        instruction=(
            "Act as John Doe on 2025-07-24T15:30:00Z. "
            "Aim to include your son Michael Doe as a personal beneficiary (relation “Son”) at First National Bank, account number 777777777, with routing 111000222. "
            "Follow up by transferring USD 100 from your Savings account to him, and verify the updated balance."
        ),
        actions=[
            # 1. Look up Kenji Tanaka’s customer record
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "John", "last_name": "Doe"},
            ),
            # 2. Add Michael Doe as a new beneficiary
            Action(
                name="AddNewBeneficiaryForCustomer",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Michael Doe",
                    "beneficiary_type": "Personal",
                    "relationship": "Son",
                    "bank_name": "First National Bank",
                    "account_number": "777777777",
                    "routing_number": "111000222",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            ),
            # 3. Fetch that beneficiary’s ID
            Action(
                name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Michael Doe"
                },
            ),
            # 4. Fetch John’s Savings account details
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Savings"
                },
            ),
            # 5. Ensure the Savings account has at least $100 USD
            Action(
                name="CheckAccountBalance",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_id": "acc_sav_1002",  # John’s Savings :contentReference[oaicite:1]{index=1}
                    "requested_amount": 100.0
                },
            ),
            # 6. Transfer $100 USD to Michael Doe
            Action(
                name="PayToBeneficiarySameCurrency",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_1",
                    "source_account_id": "acc_sav_1002",
                    "amount": 100.0,
                    "currency": "USD"
                },
            ),
            # 7. Fetch Savings account details again to verify new balance
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_type": "Savings"
                },
            ),
        ],
        outputs=[

            "\"beneficiary_id\": \"bene_1\"",

            "\"new_source_balance\": 15680.00",

        ],
    ),

    # 18
    Task(
        annotator=0,
        user_id="task_18",
        instruction=(
            "Portray John Doe on 2025-07-24T15:30:00Z. "
            "Seek to register your daughter, Emily Doe, as a personal beneficiary (relation “Daughter”) at Family Bank with account number 888888888 and routing number 111000333. "
            "Then orchestrate a monthly payment of USD 200 from your Savings account, starting from 2025-08-24."
        ),
        actions=[
            # 1. Look up John Doe’s customer record
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "John", "last_name": "Doe"},
            ),
            # 2. Add Emily Doe as a new beneficiary
            Action(
                name="AddNewBeneficiaryForCustomer",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Emily Doe",
                    "beneficiary_type": "Personal",
                    "relationship": "Daughter",
                    "bank_name": "Family Bank",
                    "account_number": "888888888",
                    "routing_number": "111000333",
                    "date_added": "2025-07-24T15:30:00Z"
                },
            ),
            # 3. Fetch that beneficiary’s ID
            Action(
                name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_name": "Emily Doe"
                },
            ),
            Action(
                name="CheckAccountBalance",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "account_id": "acc_sav_1002",
                    "requested_amount": 200.0,
                },
            ),
            # 4. Create a monthly scheduled payment starting next month (2025-08-24)
            Action(
                name="CreateNewSchedulePayment",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "source_account_id": "acc_sav_1002",  # John's Savings account :contentReference[oaicite:1]{index=1}
                    "beneficiary_id": "bene_1",
                    "amount": 200.0,
                    "currency": "USD",
                    "frequency": "Monthly",
                    "start_date": "2025-08-24"
                },
            ),
            # 5. Retrieve the scheduled payment ID to confirm
            Action(
                name="GetPaymentIdByCustomerIdAndBeneficiaryId",
                kwargs={
                    "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                    "beneficiary_id": "bene_1"
                },
            ),
        ],
        outputs=[
            # From step 2: new beneficiary ID
            "\"beneficiary_id\": \"bene_1\"",
            # From step 4: confirmation of schedule
            "\"payment_id\": \"sp_1\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"amount\": 200.0, \"currency\": \"USD\""
        ],
    ),

    # # 19
    Task(
        annotator="0",
        user_id="task_19",
        instruction=(
            "Identify as Zoltan Nagy. "
            "Cancel your current monthly INR 4,000 payment arrangement to your business beneficiary Global ISP and subsequently delete that beneficiary."
        ),
        actions=[
            # 1. Look up Zoltan Nagy
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"},
            ),
            # 2. List his accounts
            Action(
                name="GetAllAccountsOfCustomerByCustomerId",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"},
            ),
            # 3. List his beneficiaries
            Action(
                name="GetAllBeneficiariesForCustomerId",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"},
            ),
            # 4. Fetch the scheduled payment ID for Global ISP
            Action(
                name="GetPaymentIdByCustomerIdAndBeneficiaryId",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_id": "bene_5e4f3a2b-1c9d-8e7f-6a5b-4c3d2e1f0a9b",
                },
            ),
            # 5. Cancel that scheduled payment
            Action(
                name="CancelPaymentByScheduledPaymentId",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                        "scheduled_payment_id": "sp_b3a2c1d9-c3d2-e1f0-a9b8-c7d6e5f4a3b2"},
            ),
            # 6. Remove the beneficiary
            Action(
                name="RemoveBeneficiaryByBeneficiaryId",
                kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "beneficiary_id": "bene_5e4f3a2b-1c9d-8e7f-6a5b-4c3d2e1f0a9b"},
            ),
        ],
        outputs=[
            "\"message\": \"Your scheduled payment sp_b3a2c1d9-c3d2-e1f0-a9b8-c7d6e5f4a3b2 has been cancelled and beneficiary 'Global ISP' removed.\""
        ],
    ),

    # # 20
    Task(
        annotator=0,
        user_id="task_20",
        instruction=(
            "You are Chloe Dubois. "
            "With a new mobile number 480‑555‑1234, initiate a support ticket to revise your contact number, complete the updating process, and subsequently close the ticket."
        ),
        actions=[
            # 1. Look up Chloe by name
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "Chloe", "last_name": "Dubois"},
            ),
            # 2. Open support ticket for contact update
            Action(
                name="AddSupportTicketForCustomerId",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "priority": "Medium",
                    "channel": "Web Portal",
                    "category": "Profile Update",
                    "target_entity": "CustomerProfile",
                    "target_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "operation": "UpdateContactNumber",
                    "parameters": {"new_phone_number": "480-555-1234"}
                },
            ),
            # 3. Apply the new contact number
            Action(
                name="UpdateContactNumberOfCustomerId",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                    "new_phone_number": "480-555-1234"
                },
            ),
            # 4. Close the support ticket
            Action(
                name="ChangeSupportTicketStatus",
                kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2",
                        "ticket_id": "tkt_1",
                        "new_status": "Resolved"},
            ),
            # 5. Verify via fetching contact details
            Action(
            name="GetCustomerDetailsByCustomerId",
            kwargs={"customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2"},
        ),
        ],
        outputs=[
            "\"ticket_id\": \"tkt_1\"",
            "\"contact_numbers\": [{\"type\":\"Mobile\",\"number\":\"480-555-1234\",\"is_primary\":false}, …]"
        ],
    ),

        # # 21
    Task(
        annotator=0,
        user_id="task_21",
        instruction=(
            "As Zoltan Nagy, you need to note the receipt of your monthly salary of INR 200,000 via Employer Direct Deposit into your Checking account (acc_chk_5002). "
            "Next, move INR 50,000 from your Checking account to your Savings account (acc_sav_5001) and finally confirm your account balances."
        ),
        actions=[
            # 1. Look up Lakshmi Narayanan
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"},
            ),
            # 2. Fetch his Checking account details
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Checking"
                },
            ),
            # 3. Record salary deposit of INR 200,000
            Action(
                name="ReceivePayment",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_id": "acc_chk_5002",
                    "amount": 200000.0,
                    "currency": "INR",
                    "source": "Employer Direct Deposit"
                },
            ),
            # 4. Fetch her Savings account details
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Savings"
                },
            ),
            # 5. Transfer INR 50,000 from Checking to Savings
            Action(
                name="TransferMoneySameCurrency",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "source_account_id": "acc_chk_5002",
                    "target_account_id": "acc_sav_5001",
                    "amount": 50000.0,
                    "currency": "INR"
                },
            ),
            # 6. Verify Checking account balance after transfer
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Checking"
                },
            ),
            # 7. Verify Savings account balance after transfer
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                    "account_type": "Savings"
                },
            ),
        ],
        outputs=[

            "\"checking_balance\": 250000.00\"",
            # From step 5
            "\"message\": \"Transferred 50000.00 INR from checking to savings.\"",
            "\"checking_balance\": 200000.00\"",
            "\"savings_balance\": 2550000.00\""
        ],
    ),

    Task(
    annotator="0",
    user_id="task_22",
    instruction=(
            "As Sofia Andersson, terminate your active monthly payment to the business beneficiary 'London Electricity Co.' and subsequently delete that beneficiary."
        ),
    actions=[
        # 1. Look up Sofia Andersson
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Oliver", "last_name": "Williams"},
        ),
        # 2. List her accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"},
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "beneficiary_name": "London Electricity Co."
            },
        ),

        # 4. Fetch the scheduled payment ID for Manchester Electricity Co.
        Action(
            name="GetPaymentIdByCustomerIdAndBeneficiaryId",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d",
            },
        ),
        # 5. Cancel that scheduled payment
        Action(
            name="CancelPaymentByScheduledPaymentId",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "scheduled_payment_id": "sp_c1d9b3a2-e1f0-a9b8-c7d6-e5f4a3b2c1d0",
            },
        ),
        # 6. Remove the beneficiary
        Action(
            name="RemoveBeneficiaryByBeneficiaryId",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d",
            },
        ),
        # 3. List his beneficiaries
        Action(
            name="GetAllBeneficiariesForCustomerId",
            kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"},
        ),
    ],
    outputs=[
        "\"List of Beneficiary\": \"[]\""
    ],
),
Task(
    annotator=0,
    user_id="task_23",
    instruction=(
            "Acting as Zoltan Nagy, you intend to apply for an Auto loan of USD 20,000 over 60 months for a vehicle purchase. "
            "Please initiate a new loan application, proceed to approval, establish the loan, and then access the loan details. "
            "I want to keep my Vehicle (1GKS1EKD4E1234567) as collateral."
        ),
    actions=[
        # 1. Look up Zoltan Nagy’s customer record
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        # 2. Submit a new Auto loan application
        Action(
            name="CreateNewLoanApplication",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",  # Zoltan Nagy’s ID :contentReference[oaicite:1]{index=1}
                "loan_type": "Auto",
                "requested_amount": 20000.0,
                "requested_term_months": 60,
                "purpose": "Vehicle Purchase"
            },
        ),
        # 3. Process that loan application
        Action(
            name="ProcessLoanApplicationId",
            kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a","application_id": "app_1"},
        ),
        # 4. Add the approved loan to David’s account
        Action(
            name="AddNewLoanForCustomer",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "application_id": "app_1",
                "collateral_type":"Vehicle",
                "collateral_info":"1GKS1EKD4E1234567",
                "currency": "USD"
            },
        ),
        # 5. Retrieve the new loan’s details
        Action(
            name="GetLoanInformationByLoanId",
            kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a","loan_id": "loan_1"},
        ),
    ],
    outputs=[
        "\"application_id\": \"app_1\"",
        "\"loan_id\": \"loan_1\"",
        "\"status\": \"Approved\"",
        "\"principal_amount\": 20000.0",
        "\"term_months\": 60"
    ],
),

Task(
    annotator=0,
    user_id="task_24",
    instruction=(
            "As Elena Popescu, you wish to apply for a home loan of USD 300,000 over 360 months for purchasing a new Home. "
            "Initiate a new loan application and subsequently review its status."
        ),
    actions=[
        # 1. Look up Elena Popescu’s customer record
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        # 2. Create a new home loan application
        Action(
            name="CreateNewLoanApplication",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "loan_type": "Home",
                "requested_amount": 300000.0,
                "requested_term_months": 360,
                "purpose": "Home Purchase"
            },
        ),
        # 3. Retrieve the status of the new home loan application
        Action(
            name="GetLoanApplicationStatusByCustomerIdAndType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "loan_type": "Home"
            },
        ),
    ],
    outputs=[
        "\"application_id\": \"app_1\"",
        "\"application_status\": \"Submitted\""
    ],
),
Task(
    annotator=0,
    user_id="task_25",
    instruction=(
            "As Elena Popescu, you wish to apply for a home loan of USD 300,000 over 360 months for purchasing a new Home. "
            "Initiate a new loan application and subsequently review its status."
        ),
    actions=[
        # 1. Look up Elena Popescu’s customer record
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        # 2. Create a new home loan application
        Action(
            name="CreateNewLoanApplication",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "loan_type": "Home",
                "requested_amount": 300000.0,
                "requested_term_months": 360,
                "purpose": "Home Purchase"
            },
        ),
        # 3. Retrieve the status of the new home loan application
        Action(
            name="GetLoanApplicationStatusByCustomerIdAndType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "loan_type": "Home"
            },
        ),
    ],
    outputs=[
        "\"application_id\": \"app_1\"",
        "\"application_status\": \"Submitted\""
    ],
),

Task(
    annotator=0,
    user_id="task_26",
    instruction=(
            "You are John Doe. "
            "Proceed to transfer USD 100 from your Checking account (acc_chk_1001) to your beneficiary Jane Smith (bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d), and then determine your total balance across all of your accounts."
        ),
    actions=[
        # 1. Look up John Doe’s customer record
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "John", "last_name": "Doe"},
        ),
        # 2. Fetch Elena Popescu’s beneficiary ID
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "beneficiary_name": "Elena Popescu"
            },
        ),
        # 3. Ensure Checking account has at least USD 100
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "account_id": "acc_chk_1001",
                "requested_amount": 100.0
            },
        ),
        # 4. Transfer USD 100 to Elena Popescu
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "source_account_id": "acc_chk_1001",
                "beneficiary_id": "bene_9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d",
                "amount": 100.0,
                "currency": "USD"
            },
        ),
        # 5. Calculate the total balance across all accounts
        Action(
            name="CalculateTotalBalance",
            kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e", "account_ids": ["acc_chk_1001","acc_sav_1002","acc_crd_1003"]},
        ),
    ],
    outputs=[
        "\"total_balance\": 18410.50\""
    ],
),
Task(
    annotator=0,
    user_id="task_27",
    instruction=(
            "You are David Chen. "
            "Your USD checking card has been lost. "
            "Kindly initiate a ticket to block your Checking account, access your account details by type, block it, resolve the ticket, and check the account status."
        ),
    actions=[
        # 1. Look up David Chen’s customer record
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        # 2. Fetch Checking account details by type
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_type": "Checking"
            },
        ),
        # 3. Open support ticket to block the account
        Action(
            name="AddSupportTicketForCustomerId",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "priority": "High",
                "channel": "Web Portal",
                "category": "Security",
                "target_entity": "Account",
                "target_id": "acc_chk_3001",
                "operation": "BlockAccount",
                "parameters": {}
            },
        ),
        # 4. Block the Checking account
        Action(
            name="BlockAccountForCustomerId",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_id": "acc_chk_3001"
            },
        ),
        # 5. Resolve the support ticket
        Action(
            name="ChangeSupportTicketStatus",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "ticket_id": "tkt_1",
                "new_status": "Resolved"
            },
        ),
        # 6. Verify account status by fetching details again
        Action(
                name="GetAccountDetailsByCustomerIdAndAccountId",
                kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_id": "acc_chk_3001"
            },
            ),
    ],
    outputs=[
        "\"ticket_id\": \"tkt_1\"",
        "\"account_id\": \"acc_chk_3001\", \"status\": \"Blocked\""
    ],
),


Task(
    annotator=0,
    user_id="task_28",
    instruction=(
            "You are Adetokunbo Adebayor. "
            "You want to update your email from ade.adebayor@example.ng to adetokunbo.adebayor@newmail.ng. "
            "Open a support ticket, complete the update, close the ticket, and afterward confirm your new email."
        ),
    actions=[
        # 1. Look up Oliver Williams’s customer record
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Adetokunbo", "last_name": "Adebayor"},
        ),
        # 2. Open a support ticket for email update
        Action(
            name="AddSupportTicketForCustomerId",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                "priority": "Medium",
                "channel": "Web Portal",
                "category": "Profile Update",
                "target_entity": "CustomerProfile",
                "target_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                "operation": "UpdateEmail",
                "parameters": {"new_email": "adetokunbo.adebayor@newmail.ng"}
            },
        ),
        # 3. Apply the new email
        Action(
            name="UpdateEmailForOfCustomerId",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                "new_email": "adetokunbo.adebayor@newmail.ng"
            },
        ),
        # 4. Resolve the support ticket
        Action(
            name="ChangeSupportTicketStatus",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23",
                "ticket_id": "tkt_1",
                "new_status": "Resolved"
            },
        ),
        # 5. Verify the updated email
        Action(
            name="GetCustomerDetailsByCustomerId",
            kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5-23"},
        ),
    ],
    outputs=[
        "\"ticket_id\": \"tkt_1\"",
        "\"email_address\": \"adetokunbo.adebayor@newmail.ng\""
    ],
),

Task(
    annotator=0,
    user_id="task_29",
    instruction=(
            "You are Kenji Tanaka. "
            "Initiate the opening of a new AUD Checking account, then proceed to transfer AUD 500 from your current Savings account into it, and subsequently confirm the new Checking balance."
        ),
    actions=[
        # 1. Look up Kenji Tanaka’s customer record
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Olivia", "last_name": "Jones"},
        ),
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Checking"},
        ),
        # 2. Create a new Checking account
        Action(
            name="CreateNewAccountForCustomer",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                "account_type": "Checking",
                "account_type_code" : "chk",
                "currency" : "AUD"
            },
        ),
        # 3. Transfer AUD 500 from Savings to the new Checking
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                "source_account_id": "acc_sav_17002",
                "target_account_id": "acc_1",
                "amount": 500.0,
                "currency": "AUD"
            },
        ),
        # 4. Verify the new Checking account balance
        Action(
            name="GetAccountDetailsByCustomerIdAndAccountId",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef-16",
                "account_id": "acc_1"
            }
        )
    ],
    outputs=[
        "\"account_id\": \"acc_1\"",
        "\"account_type\": \"Checking\"",
        "\"balance\": 500.0"
    ],
),
Task(
    annotator=0,
    user_id="task_30",
    instruction=(
            "You are Jane Smith. "
            "Set up a new CAD Credit Card account, and then promptly transfer CAD 500 from your existing Checking account into it."
        ),
    actions=[
        # 1. Look up Jane Smith’s customer record
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        # 2. List all of her accounts to confirm IDs
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
        ),
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Credit Card"},
        ),
        # 3. Create a new Savings account
        Action(
            name="CreateNewAccountForCustomer",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_type": "Credit Card",
                "account_type_code" : "crd",
                "currency" : "CAD"
            },
        ),
        # 4. Transfer CAD 500 from Checking to the new Savings
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "source_account_id": "acc_chk_2001",  # Jane’s CAD Checking :contentReference[oaicite:1]{index=1}
                "target_account_id": "acc_1",
                "amount": 500.0,
                "currency": "CAD"
            },
        ),
        # 5. Verify both account balances
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_type": "Checking"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_type": "Credit Card"
            },
        ),
    ],
    outputs=[
        "\"checking_balance\": 2600.75\"",
        "\"credit_card_balance\": 500\""
    ],
),

Task(
    annotator="0",
    user_id="task_31",
    instruction=(
            "As Elena Popescu, initiate the creation of a new Savings account and promptly transfer CAD 800 from your current Checking account into it."
        ),
    actions=[
        # 1. Look up Elena Popescu
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        # 2. List all of her accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
        ),
        # 3. Determine the code for Savings
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Savings"},
        ),
        # 4. Create the new Savings account
        Action(
            name="CreateNewAccountForCustomer",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_type": "Savings",
                "account_type_code": "sav",
                "currency": "CAD",
            },
        ),
        # 5. Fetch details for all Savings accounts
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_type": "Savings",
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_id": "acc_chk_2001",
                "requested_amount": 800.0,
            },
        ),
        # 6. Transfer CAD 800 from Checking to the new Savings account
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "source_account_id": "acc_chk_2001",
                "target_account_id": "acc_1",
                "currency": "CAD",
                "amount": 800.0,
            },
        ),
    ],
    outputs=[
        '"message": "Transfer successful (same currency).",'
        '"source_account_id": "acc_chk_2001",'
        '"target_account_id": "acc_1",'
        '"amount_transferred": 800.0,'
        '"currency": "CAD",'
        '"source_balance": 2300.75,'
        '"target_balance": 800.0'
    ],
),

Task(
    annotator="0",
    user_id="task_32",
    instruction=(
            "As Zoltan Nagy, establish a new Savings account and quickly transfer USD 1000 from your existing Checking account to it."
        ),
    actions=[
        # 1. Look up Zoltan Nagy
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        # 2. List all of his accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"},
        ),
        # 3. Determine the code for Savings
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Savings"},
        ),
        # 4. Create the new Savings account
        Action(
            name="CreateNewAccountForCustomer",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_type": "Savings",
                "account_type_code": "sav",
                "currency": "USD",
            },
        ),
        # 5. Fetch details for all Savings accounts
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_type": "Savings",
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_id": "acc_chk_3001",
                "requested_amount": 1000.0,
            },
        ),
        # 6. Transfer USD 1000 from Checking to the new Savings account
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "source_account_id": "acc_chk_3001",
                "target_account_id": "acc_1",
                "currency": "USD",
                "amount": 1000.0,
            },
        ),
    ],
    outputs=[
        '"message": "Transfer successful (same currency).",'
        '"source_account_id": "acc_chk_3001",'
        '"target_account_id": "acc_1",'
        '"amount_transferred": 1000.0,'
        '"currency": "USD",'
        '"source_balance": 11540.25,'
        '"target_balance": 1000.0'
    ],
),
Task(
    annotator="0",
    user_id="task_33",
    instruction=(
            "As Sofia Andersson, set up a new Savings account and immediately move USD 200 from your existing Checking account into it."
        ),
    actions=[
        # 1. Look up Sofia Andersson
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Maria", "last_name": "Garcia"},
        ),
        # 2. List all of her accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"},
        ),
        # 3. Determine the code for Savings
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Savings"},
        ),
        # 4. Create the new Savings account
        Action(
            name="CreateNewAccountForCustomer",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "account_type": "Savings",
                "account_type_code": "sav",
                "currency": "USD",
            },
        ),
        # 5. Fetch details for all Savings accounts
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "account_type": "Savings",
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "account_id": "acc_chk_4001",
                "requested_amount": 200.0,
            },
        ),
        # 6. Transfer USD 200 from Checking to the new Savings account
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "source_account_id": "acc_chk_4001",
                "target_account_id": "acc_1",
                "currency": "USD",
                "amount": 200.0,
            },
        ),
    ],
    outputs=[
        '"message": "Transfer successful (same currency).",'
        '"source_account_id": "acc_chk_4001",'
        '"target_account_id": "acc_1",'
        '"amount_transferred": 200.0,'
        '"currency": "USD",'
        '"source_balance": 1000.50,'
        '"target_balance": 200.0'
    ],
),

Task(
    annotator="0",
    user_id="task_34",
    instruction=(
            "As Zoltan Nagy, proceed to transfer USD 300 to your beneficiary Metropolis Power & Light from your Checking account."
        ),
    actions=[
        # 1. Look up Zoltan Nagy
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        # 2. List his accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"},
        ),
        # 3. Fetch his Checking account details (to check balance)
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_type": "Checking",
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_id": "acc_chk_3001",
                "requested_amount": 300.0,
            },
        ),
        # 4. Get details for beneficiary “Elena Popescu”
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_name": "Metropolis Power & Light",
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "source_account_id": "acc_chk_3001",
                "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a",
                "amount": 300.00,
                "currency": "USD"
            },
        ),
    ],
    outputs=[
        "\"message\": \"Paid 300.00 USD to beneficiary 'Metropolis Power & Light'.\", "
        "\"source_account_id\": \"acc_chk_3001\", "
        "\"beneficiary_account_number\": \"9988776655\", "
        "\"source_amount\": 300.0, "
        "\"source_currency\": \"USD\", "
        "\"target_amount\": 300.0, "
        "\"target_currency\": \"USD\", "
        "\"new_source_balance\": 12240.25\""
    ],
),

Task(
    annotator="0",
    user_id="task_35",
    instruction=(
            "As Chloe Dubois, organize a transfer of EUR 100 from your Checking account to your personal beneficiary Klaus Schmidt."
        ),
    actions=[
        # 1. Look up Sofia Andersson
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Hans", "last_name": "Müller"},
        ),
        # 2. List her accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"},
        ),
        # 3. Fetch her Checking account details (to check balance)
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "account_type": "Checking",
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "account_id": "acc_chk_8001",
                "requested_amount": 100.0,
            },
        ),
        # 4. Get details for beneficiary “Kenji Tanaka”
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "beneficiary_name": "Klaus Schmidt",
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "source_account_id": "acc_chk_8001",
                "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a",
                "amount": 100.00,
                "currency": "EUR"
            },
        ),
    ],
    outputs=[

        "\"source_account_id\": \"acc_chk_8001\", "
        "\"source_amount\": 100.0, "
        "\"source_currency\": \"EUR\", "
        "\"target_amount\": 100.0, "
        "\"target_currency\": \"EUR\", "
        "\"new_source_balance\": 7700.50\""
    ],
),
Task(
    annotator="0",
    user_id="task_36",
    instruction=(
            "You are Chloe Dubois and you intend to transfer EUR 1000 to your personal beneficiary Klaus Schmidt from your Checking account."
        ),
    actions=[
        # 1. Look up Sofia Andersson
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Hans", "last_name": "Müller"},
        ),
        # 2. List her accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1"},
        ),
        # 3. Fetch her Checking account details (to check balance)
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "account_type": "Checking",
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "account_id": "acc_chk_8001",
                "requested_amount": 1000.0,
            },
        ),
        # 4. Get details for beneficiary “Kenji Tanaka”
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "beneficiary_name": "Klaus Schmidt",
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "d4e5f6a1-b2c3-d4e5-f6a1-b2c3d4e5f6a1",
                "source_account_id": "acc_chk_8001",
                "beneficiary_id": "bene_9d8e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a",
                "amount": 1000.00,
                "currency": "EUR"
            },
        ),
    ],
    outputs=[

        "\"source_account_id\": \"acc_chk_8001\", "
        "\"source_amount\": 1000.0, "
        "\"source_currency\": \"EUR\", "
        "\"target_amount\": 1000.0, "
        "\"target_currency\": \"EUR\", "
        "\"new_source_balance\": 6800.50\""
    ],
),
# # 03. Oliver Williams set up a recurring monthly payment to Utility Co.
    Task(
        annotator="0",
        user_id="task_37",
        instruction=(
            "You are Sofia Andersson. "
            "Initiate a monthly GBP£100 payment starting next month, on date 2025-08-24, from your Checking account to your business beneficiary Manchester Electricity Co."
        ),
        actions=[
            # 1. Look up Sofia Andersson
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "Oliver", "last_name": "Williams"},
            ),
            # 2. List all of her accounts
            Action(
                name="GetAllAccountsOfCustomerByCustomerId",
                kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"},
            ),
            # 3. Fetch her Checking account details
            Action(
                name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_type": "Checking",
                },
            ),
            # 4. Get details for business beneficiary Manchester Electricity Co.
            Action(
                name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "beneficiary_name": "London Electricity Co.",
                },
            ),
            # 5. Check balance of the source account for GBP 100
            Action(
                name="CheckAccountBalance",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "account_id": "acc_chk_6001",
                    "requested_amount": 100.0,
                },
            ),
            # 6. Schedule the monthly payment starting 2025-08-24
            Action(
                name="CreateNewSchedulePayment",
                kwargs={
                    "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                    "source_account_id": "acc_chk_6001",
                    "beneficiary_id": "bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d",
                    "amount": 100.0,
                    "currency": "GBP",
                    "frequency": "Monthly",
                    "start_date": "2025-08-24",
                },
            ),
        ],
        outputs=[
            "\"payment_id\": \"sp_1\", \"customer_id\": \"b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5\", "
            "\"source_account_id\": \"acc_chk_6001\", \"beneficiary_id\": \"bene_3a2b1c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d\", "
            "\"amount\": 100.0, \"currency\": \"GBP\", \"frequency\": \"Monthly\", "
            "\"start_date\": \"2025-08-24\", \"next_payment_date\": \"2025-09-24\", "
            "\"end_date\": null, \"status\": \"Active\""
        ],
    ),
    # # 01. Zoltan Nagy set up a recurring monthly payment to Global ISP.
Task(
    annotator="0",
    user_id="task_38",
    instruction=(
            "You are Zoltan Nagy. "
            "Arrange for a monthly INR 1500 payment beginning next month, on date 2025-08-24, from your Checking account to your business beneficiary Global ISP."
        ),
    actions=[
        # 1. Look up Zoltan Nagy
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"},
        ),
        # 2. List all of his accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"},
        ),
        # 3. Fetch his Checking account details
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_type": "Checking",
            },
        ),
        # 4. Get details for business beneficiary Global ISP
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "beneficiary_name": "Global ISP",
            },
        ),
        # 5. Check balance of the source account for INR 1500
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_id": "acc_chk_5002",
                "requested_amount": 1500.0,
            },
        ),
        # 6. Schedule the monthly payment starting 2025-08-24
        Action(
            name="CreateNewSchedulePayment",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "source_account_id": "acc_chk_5002",
                "beneficiary_id": "bene_5e4f3a2b-1c9d-8e7f-6a5b-4c3d2e1f0a9b",
                "amount": 1500.0,
                "currency": "INR",
                "frequency": "Monthly",
                "start_date": "2025-08-24",
            },
        ),
    ],
    outputs=[
        "\"payment_id\": \"sp_1\", \"customer_id\": \"a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4\", "
        "\"source_account_id\": \"acc_chk_5002\", \"beneficiary_id\": \"bene_5e4f3a2b-1c9d-8e7f-6a5b-4c3d2e1f0a9b\", "
        "\"amount\": 1500.0, \"currency\": \"INR\", \"frequency\": \"Monthly\", "
        "\"start_date\": \"2025-08-24\", \"next_payment_date\": \"2025-09-24\", "
        "\"end_date\": null, \"status\": \"Active\""
    ],
),
Task(
    annotator="0",
    user_id="task_39",
    instruction=(
            "You are Zoltan Nagy. "
            "Organize a monthly USD 350 payment starting next month, on date 2025-08-24, from your Checking account to your business beneficiary Metropolis Power & Light."
        ),
    actions=[
        # 1. Look up Zoltan Nagy
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        # 2. List all of his accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"},
        ),
        # 3. Fetch his Checking account details
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_type": "Checking",
            },
        ),
        # 4. Get details for business beneficiary Metropolis Power & Light
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_name": "Metropolis Power & Light",
            },
        ),
        # 5. Check balance of the source account for USD 350
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_id": "acc_chk_3001",
                "requested_amount": 350.0,
            },
        ),
        # 6. Schedule the monthly payment starting 2025-08-24
        Action(
            name="CreateNewSchedulePayment",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "source_account_id": "acc_chk_3001",
                "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a",
                "amount": 350.0,
                "currency": "USD",
                "frequency": "Monthly",
                "start_date": "2025-08-24",
            },
        ),
    ],
    outputs=[
        "\"payment_id\": \"sp_1\", \"customer_id\": \"d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a\", "
        "\"source_account_id\": \"acc_chk_3001\", \"beneficiary_id\": \"bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a\", "
        "\"amount\": 350.0, \"currency\": \"USD\", \"frequency\": \"Monthly\", "
        "\"start_date\": \"2025-08-24\", \"next_payment_date\": \"2025-09-24\", "
        "\"end_date\": null, \"status\": \"Active\""
    ],
),
Task(
    annotator="0",
    user_id="task_40",
    instruction=(
            "You are Elena Popescu. "
            "Apply for an auto loan of CAD 25,000 for purchasing a new car over 36 months, using your vehicle VIN '1HGCM82633A123456' as collateral."
        ),
    actions=[
        # 1. Look up Elena Popescu
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        # 2. Submit the loan application for 36 months with collateral info
        Action(
            name="CreateNewLoanApplication",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "loan_type": "Auto",
                "requested_amount": 25000.0,
                "requested_term_months": 36,
                "purpose": "New car purchase",
            },
        ),
        # 3. Process the application
        Action(
            name="ProcessLoanApplicationId",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "application_id": "app_1",
            },
        ),
        # 4. Check application status
        Action(
            name="GetLoanApplicationStatusByCustomerIdAndType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "loan_type": "Auto",
            },
        ),
        # 5. Create the actual loan record against the vehicle collateral
        Action(
            name="AddNewLoanForCustomer",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "application_id": "app_1",
                "collateral_type": "Vehicle",
                "collateral_info": "VIN: 1HGCM82633A123456",
                "currency": "CAD",
            },
        )
    ],
    outputs=[
        "\"loan_id\": \"loan_1\",\"loan_account_id\": \"loanacc_1\" \"application_id\": \"app_1\", \"status\": \"Approved\""
    ],
),
Task(
    annotator="0",
    user_id="task_41",
    instruction=(
        "You are Sofia Andersson. Seek a student loan totaling USD 15,000 for tuition fees to be paid over 48 months, offering 'Maria Bekery Shop' (Property) as collateral."
    ),
    actions=[
        # 1. Look up Sofia Andersson
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Maria", "last_name": "Garcia"},
        ),
        # 2. Submit the loan application for 48 months
        Action(
            name="CreateNewLoanApplication",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "loan_type": "Student",
                "requested_amount": 15000.0,
                "requested_term_months": 48,
                "purpose": "Tuition fees",
            },
        ),
        # 3. Process the application
        Action(
            name="ProcessLoanApplicationId",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "application_id": "app_1",
            },
        ),
        # 4. Check application status
        Action(
            name="GetLoanApplicationStatusByCustomerIdAndType",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "loan_type": "Student",
            },
        ),
        # 5. Create the actual loan record
        Action(
            name="AddNewLoanForCustomer",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "application_id": "app_1",
                "collateral_type": "Property",
                "collateral_info": "Maria Bekery Shop",
                "currency": "USD",
            },
        )
    ],
    outputs=[
        "\"loan_id\": \"loan_1\",\"loan_account_id\": \"loanacc_1\" \"application_id\": \"app_1\", \"status\": \"Approved\""
    ],
),
Task(
    annotator="0",
    user_id="task_42",
    instruction=(
            "You are Zoltan Nagy. "
            "Submit an application for a business loan of INR 500,000 aimed at office expansion over 60 months, utilizing your IT Equipment and Servers (Business Assets) as collateral."
        ),
    actions=[
        # 1. Look up Zoltan Nagy
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"},
        ),
        # 2. Submit the loan application for 60 months with collateral info
        Action(
            name="CreateNewLoanApplication",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "loan_type": "Business",
                "requested_amount": 500000.0,
                "requested_term_months": 60,
                "purpose": "Office expansion",
            },
        ),
        # 3. Process the application
        Action(
            name="ProcessLoanApplicationId",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "application_id": "app_1",
            },
        ),
        # 4. Check application status
        Action(
            name="GetLoanApplicationStatusByCustomerIdAndType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "loan_type": "Business",
            },
        ),
        # 5. Create the actual loan record against the IT equipment collateral
        Action(
            name="AddNewLoanForCustomer",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "application_id": "app_1",
                "collateral_type": "Business Assets",
                "collateral_info": "IT Equipment and Servers",
                "currency": "INR",
            },
        )
    ],
    outputs=[
        "\"loan_id\": \"loan_1\",\"loan_account_id\": \"loanacc_1\" \"application_id\": \"app_1\", \"status\": \"Approved\""
    ],
),
Task(
    annotator="0",
    user_id="task_43",
    instruction=(
            "You are Sofia Andersson. "
            "Request a personal loan of GBP 3,000 intended for home renovations over 18 months, with your savings provided as collateral."
        ),
    actions=[
        # 1. Look up Sofia Andersson
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Oliver", "last_name": "Williams"},
        ),
        # 2. Submit the loan application for 18 months with collateral info
        Action(
            name="CreateNewLoanApplication",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "loan_type": "Personal",
                "requested_amount": 3000.0,
                "requested_term_months": 18,
                "purpose": "Home renovations",
            },
        ),
        # 3. Process the application
        Action(
            name="ProcessLoanApplicationId",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "application_id": "app_1",
            },
        ),
        # 4. Check application status
        Action(
            name="GetLoanApplicationStatusByCustomerIdAndType",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "loan_type": "Personal",
            },
        ),
        # 5. Create the actual loan record against the savings collateral
        Action(
            name="AddNewLoanForCustomer",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "application_id": "app_1",
                "collateral_type": "Savings",
                "collateral_info": "Savings account balance",
                "currency": "GBP",
            },
        )
    ],
    outputs=[
        "\"loan_id\": \"loan_1\",\"loan_account_id\": \"loanacc_1\" \"application_id\": \"app_1\", \"status\": \"Approved\""
    ],
),


Task(
    annotator="0",
    user_id="task_44",
    instruction=(
            "You are Elena Popescu. "
            "Receive your monthly salary of CAD 4,000 from Creative Minds LLC into your Checking account, subsequently transfer 25%, equivalent to CAD 1,000, from Checking to your Savings account, then verify the balances in both accounts."
        ),
    actions=[
        # 1. Look up Elena Popescu
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        # 2. List all of her accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
        ),
        # 3. Fetch current Checking account details
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_type": "Checking",
            },
        ),
        # 4. Receive salary payment of CAD 4,000 into Checking
        Action(
            name="ReceivePayment",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_id": "acc_chk_2001",
                "amount": 4000.0,
                "currency": "CAD",
            },
        ),
        # 5. Fetch Savings account details
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_type": "Savings",
            },
        ),
        # 6. Transfer CAD 1,000 from Checking to Savings
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "source_account_id": "acc_chk_2001",
                "target_account_id": "acc_sav_2002",
                "currency": "CAD",
                "amount": 1000.0,
            },
        ),
        # 7. Confirm Checking balance
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_type": "Checking",
            },
        ),
        # 8. Confirm Savings balance
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_type": "Savings",
            },
        ),
    ],
    outputs=[
        "\"account_type\": \"Checking\", \"balance\": 6100.75\"",
        "\"account_type\": \"Savings\", \"balance\": 23000.00\""
    ],
),
Task(
    annotator="0",
    user_id="task_45",
    instruction=(
            "You are Zoltan Nagy. "
            "Obtain your monthly salary of USD 12,000 from City General Hospital into your Checking account, thereafter transfer 10%, which is USD 1,200, from Checking to your Investment account, then check the balances in both accounts."
        ),
    actions=[
        # 1. Look up Zoltan Nagy
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        # 2. List all of his accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"},
        ),
        # 3. Fetch current Checking account details
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_type": "Checking",
            },
        ),
        # 4. Receive salary payment of USD 12,000 into Checking
        Action(
            name="ReceivePayment",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_id": "acc_chk_3001",
                "amount": 12000.0,
                "currency": "USD",
            },
        ),
        # 5. Fetch Investment account details
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_type": "Investment",
            },
        ),
        # 6. Transfer USD 1,200 from Checking to Investment
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "source_account_id": "acc_chk_3001",
                "target_account_id": "acc_inv_3002",
                "currency": "USD",
                "amount": 1200.0,
            },
        ),
        # 7. Confirm Checking balance
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_type": "Checking",
            },
        ),
        # 8. Confirm Investment balance
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_type": "Investment",
            },
        ),
    ],
    outputs=[
        "\"account_type\": \"Checking\", \"balance\": 23340.25\"",
        "\"account_type\": \"Investment\", \"balance\": 151200.00\""
    ],
),
Task(
    annotator="0",
    user_id="task_46",
    instruction=(
            "Identify yourself as Zoltan Nagy. "
            "First, handle the receipt of your monthly scholarship of INR 1,200 from State University deposited into your Checking account. "
            "Next, proceed to transfer 50%, which amounts to INR 600, from Checking to your Savings account, and ultimately verify the balances in both accounts."
        ),
    actions=[
        # 1. Look up Sofia Andersson
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"},
        ),
        # 2. List all of her accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"},
        ),
        # 3. Fetch current Checking account details
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_type": "Checking",
            },
        ),
        # 4. Receive scholarship payment of USD 1,200 into Checking
        Action(
            name="ReceivePayment",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_id": "acc_chk_5002",
                "amount": 1200.0,
                "currency": "INR",
            },
        ),
        # 5. Create and fetch Savings account details
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_type": "Savings",
            },
        ),
        # 6. Transfer USD 600 from Checking to Savings
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "source_account_id": "acc_chk_5002",
                "target_account_id": "acc_sav_5001",
                "currency": "INR",
                "amount": 600.0,
            },
        ),
        # 7. Confirm Checking balance
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_type": "Checking",
            },
        ),
        # 8. Confirm Savings balance
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_type": "Savings",
            },
        ),
    ],
    outputs=[
        "\"account_type\": \"Checking\", \"balance\": 2500600.0\"",
        "\"account_type\": \"Savings\", \"balance\": 50600.0\""
    ],
),
Task(
    annotator="0",
    user_id="task_47",
    instruction=(
            "Identify yourself as Zoltan Nagy. "
            "Initially, await the receipt of your monthly salary of INR 250,000 from Global Tech Services into your Checking account. "
            "Subsequently, coordinate the transfer of 20%, which equates to INR 50,000, from Checking to your Savings account, and in conclusion, confirm the balances in both accounts."
        ),
    actions=[
        # 1. Look up Zoltan Nagy
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"},
        ),
        # 2. List all of his accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"},
        ),
        # 3. Fetch current Checking account details
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_type": "Checking",
            },
        ),
        # 4. Receive salary payment of INR 250,000 into Checking
        Action(
            name="ReceivePayment",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_id": "acc_chk_5002",
                "amount": 250000.0,
                "currency": "INR",
            },
        ),
        # 5. Fetch Savings account details
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_type": "Savings",
            },
        ),
        # 6. Transfer INR 50,000 from Checking to Savings
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "source_account_id": "acc_chk_5002",
                "target_account_id": "acc_sav_5001",
                "currency": "INR",
                "amount": 50000.0,
            },
        ),
        # 7. Confirm Checking balance
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_type": "Checking",
            },
        ),
        # 8. Confirm Savings balance
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_type": "Savings",
            },
        ),
    ],
    outputs=[
        "\"account_type\": \"Checking\", \"balance\": 250000.00\"",
        "\"account_type\": \"Savings\", \"balance\": 2550000.00\""
    ],
),
Task(
    annotator="0",
    user_id="task_48",
    instruction=(
            "Identify yourself as Oliver Williams. "
            "Begin by receiving your monthly salary of AED 1,800 from Sparky & Co. "
            "into your Checking account. "
            "Afterwards, arrange the transfer of 15%, equivalent to AED 270, from Checking to your Savings account, and finally, validate the balances in both accounts."
        ),
    actions=[
        # 1. Look up Sofia Andersson
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Fatima", "last_name": "Al-Fassi"},
        ),
        # 2. List all of her accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"},
        ),
        # 3. Fetch current Checking account details
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "account_type": "Checking",
            },
        ),
        # 4. Receive salary payment of GBP 1,800 into Checking
        Action(
            name="ReceivePayment",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "account_id": "acc_chk_7001",
                "amount": 1800.0,
                "currency": "AED",
            },
        ),
        # 5. Fetch Savings account details
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "account_type": "Savings",
            },
        ),
        # 6. Transfer GBP 270 from Checking to Savings
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "source_account_id": "acc_chk_7001",
                "target_account_id": "acc_sav_7002",
                "currency": "AED",
                "amount": 270.0,
            },
        ),
        # 7. Confirm Checking balance
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "account_type": "Checking",
            },
        ),
        # 8. Confirm Savings balance
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "account_type": "Savings",
            },
        ),
    ],
    outputs=[
        "\"account_type\": \"Checking\", \"balance\": 151530.0\"",
        "\"account_type\": \"Savings\", \"balance\": 750270.0\""
    ],
),
Task(
        annotator=0,
        user_id="task_49",
        instruction=(
            "Identify yourself as Kenji Tanaka. "
            "Given that your Savings account (acc_sav_10002) is being targeted by a scam, you need to block it for security reasons. "
            "Utilize the Web Portal to submit a support ticket to block the Savings account, and then ensure the ticket is marked as resolved."
        ),
        actions=[
            # 1. Look up Kenji Tanaka’s customer record
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "Kenji", "last_name": "Tanaka"},
            ),
            # 2. Open a support ticket to block the lost card
            Action(
                name="AddSupportTicketForCustomerId",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",  # Kenji Tanaka’s ID :contentReference[oaicite:2]{index=2}
                    "priority": "High",
                    "channel": "Web Portal",
                    "category": "Security",
                    "target_entity": "Account",
                    "target_id": "acc_sav_10002",  # Chloe’s credit card :contentReference[oaicite:3]{index=3}
                    "operation": "BlockAccount",
                },
            ),
            # 3. Block the credit card account
            Action(
                name="BlockAccountForCustomerId",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "account_id": "acc_sav_10002"
                },
            ),
            # 4. Close the support ticket
            Action(
                name="ChangeSupportTicketStatus",
                kwargs={"ticket_id": "tkt_1","customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "new_status": "Resolved"},
            ),
            # 5. Verify that the credit card status is now blocked
            Action(
                name="GetAccountDetailsByCustomerIdAndAccountId",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "account_id": "acc_sav_10002"
                },
            ),
        ],
        outputs=[
            # From step 2
            "\"ticket_id\": \"tkt_1\"",
            "\"account_id\": \"acc_sav_10002\", \"status\": \"Blocked\""
        ],
    ),
Task(
    annotator=0,
    user_id="task_50",
    instruction=(
            "Identify yourself as Kenji Tanaka. "
            "You are required to transfer JPY 1000 from your Checking account (acc_chk_10001) to your beneficiary, Yuki Tanaka. "
            "Subsequently, calculate your total balance across all of your accounts."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Kenji", "last_name": "Tanaka"},
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "beneficiary_name": "Yuki Tanaka"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "account_id": "acc_chk_10001",
                "requested_amount": 1000.00
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "source_account_id": "acc_chk_10001",
                "beneficiary_id": "bene_2b1c9d8e-7f6a-5b4c-3d2e-1f0a9b8c7d6e",
                "amount": 1000.00,
                "currency": "JPY"
            },
        ),
        Action(
            name="CalculateTotalBalance",
            kwargs={
                "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                "account_ids": ["acc_chk_10001","acc_sav_10002"]
            },
        ),
    ],
    outputs=[
        "\"total_balance\": 17499000.00\""
    ],
),

Task(
    annotator="0",
    user_id="task_51",
    instruction=(
            "You are Zoltan Nagy. "
            "Terminate the active monthly payment to your business beneficiary Metropolis Power & Light and subsequently delete that beneficiary."
        ),
    actions=[
        # 1. Look up Zoltan Nagy
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        # 2. List his accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"},
        ),
        # 3. List his beneficiaries
        Action(
            name="GetAllBeneficiariesForCustomerId",
            kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"},
        ),
        # 4. Fetch the scheduled payment ID for Metropolis Power & Light
        Action(
            name="GetPaymentIdByCustomerIdAndBeneficiaryId",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a",
            },
        ),
        # 5. Cancel that scheduled payment
        Action(
            name="CancelPaymentByScheduledPaymentId",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "scheduled_payment_id": "sp_b3a2c1d9-e7f6-a5b4-c3d2-e1f0a9b8c7d6",
            },
        ),
        # 6. Remove the beneficiary
        Action(
            name="RemoveBeneficiaryByBeneficiaryId",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_id": "bene_6d5e4f3a-2b1c-9d8e-7f6a-5b4c3d2e1f0a",
            },
        ),
    ],
    outputs=[
        "\"List of Beneficiary\": \"[]\""
    ],
),

Task(
    annotator="0",
    user_id="task_52",
    instruction=(
        "You are John Doe. Block your Checking account for security reasons."
    ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "John", "last_name": "Doe"},
        ),
        # 2. List all of his accounts
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e"},
        ),
        # 3. Determine the code for Checking
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Checking"},
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "account_type": "Checking",
            },
        ),
        # 4. Create a high-priority support ticket for blocking the account
        Action(
            name="AddSupportTicketForCustomerId",
            kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "priority": "High",
                "channel": "Web Portal",
                "category": "Security",
                "target_id": "acc_chk_1001",
                "target_entity": "Account",
                "operation": "Block",
                "parameters": {}
            },
        ),
        # 5. Block the account
        Action(
            name="BlockAccountForCustomerId",
            kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "account_id": "acc_chk_1001"
            },
        ),
        # 6. Confirm updated account details
        Action(
                name="GetAccountDetailsByCustomerIdAndAccountId",
                kwargs={
                "customer_id": "c3e8f1d2-9a8b-4f7c-8a6e-2b9f3d1a4c7e",
                "account_id": "acc_chk_1001"
            },
            ),
    ],
    outputs=[
        "\"ticket_id\": \"tkt_1\","
        "\"status\": \"Blocked\","
        "\"account_id\": \"acc_chk_1001\","
        "\"account_type\": \"Checking\","
        "\"balance\": 5230.00\""
    ],
),
Task(
    annotator="0",
    user_id="task_53",
    instruction=(
        "You are Jane Smith. Block your Checking account for security purposes."
    ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
        ),
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Checking"},
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_type": "Checking",
            },
        ),
        Action(
            name="AddSupportTicketForCustomerId",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "priority": "High",
                "channel": "Web Portal",
                "category": "Security",
                "target_id": "acc_chk_2001",
                "target_entity": "Account",
                "operation": "Block",
                "parameters": {}
            },
        ),
        Action(
            name="BlockAccountForCustomerId",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_id": "acc_chk_2001"
            },
        ),
        Action(
                name="GetAccountDetailsByCustomerIdAndAccountId",
                kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_id": "acc_chk_2001"
            },
            ),
    ],
    outputs=[
        "\"ticket_id\": \"tkt_1\","
        "\"status\": \"Blocked\","
        "\"account_id\": \"acc_chk_2001\","
        "\"account_type\": \"Checking\","
        "\"balance\": 3100.75\""
    ],
),

Task(
    annotator="0",
    user_id="task_54",
    instruction=(
        "You are David Chen. For security reasons, block your Checking account."
    ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"},
        ),
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Checking"},
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_type": "Checking",
            },
        ),
        Action(
            name="AddSupportTicketForCustomerId",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "priority": "High",
                "channel": "Web Portal",
                "category": "Security",
                "target_id": "acc_chk_3001",
                "target_entity": "Account",
                "operation": "Block",
                "parameters": {}
            },
        ),
        Action(
            name="BlockAccountForCustomerId",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_id": "acc_chk_3001"
            },
        ),
        Action(
                name="GetAccountDetailsByCustomerIdAndAccountId",
                kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_id": "acc_chk_3001"
            },
            ),
    ],
    outputs=[
        "\"ticket_id\": \"tkt_1\","
        "\"status\": \"Blocked\","
        "\"account_id\": \"acc_chk_3001\","
        "\"account_type\": \"Checking\","
        "\"balance\": 12500.00\""
    ],
),

Task(
    annotator="0",
    user_id="task_55",
    instruction=(
        "You are Maria Garcia. For security measures, block your Checking account."
    ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Maria", "last_name": "Garcia"},
        ),
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"},
        ),
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Checking"},
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "account_type": "Checking",
            },
        ),
        Action(
            name="AddSupportTicketForCustomerId",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "priority": "High",
                "channel": "Web Portal",
                "category": "Security",
                "target_id": "acc_chk_4001",
                "target_entity": "Account",
                "operation": "Block",
                "parameters": {}
            },
        ),
        Action(
            name="BlockAccountForCustomerId",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "account_id": "acc_chk_4001"
            },
        ),
        Action(
                name="GetAccountDetailsByCustomerIdAndAccountId",
                kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "account_id": "acc_chk_4001"
            },
            ),
    ],
    outputs=[
        "\"ticket_id\": \"tkt_1\","
        "\"status\": \"Blocked\","
        "\"account_id\": \"acc_chk_4001\","
        "\"account_type\": \"Checking\","
        "\"balance\": 1200.50\""
    ],
),

Task(
    annotator="0",
    user_id="task_56",
    instruction=(
            "You are Jane Smith. "
            "You've recently moved to 789 Oak Avenue, Montreal, ON M5H 2N2, Canada. "
            "Utilize the Mobile App to file a ticket. "
            "Please create a support ticket and update your residential address to reflect this."
        ),
    actions=[
        # 1. Look up Elena Popescu
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        # 2. Open a support ticket
        Action(
            name="AddSupportTicketForCustomerId",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "priority": "Medium",
                "channel": "Mobile App",
                "category": "Profile Update",
                "target_id":   "a1b2c3d4-e5f6-7890-1234-567890abcdef",
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
        ),
        # 3. Apply the update
        Action(
            name="UpdateAddressForCustomerId",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "residential_address": {
                    "street_address": "789 Oak Avenue",
                    "city": "Montreal",
                    "state": "ON",
                    "postal_code": "M5H 2N2",
                    "country": "Canada"
                }
            },
        ),
        # 4. Close the ticket
        Action(
            name="ChangeSupportTicketStatus",
            kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef","ticket_id": "tkt_1", "new_status": "Resolved"},
        ),
        # 5. Verify updated record
        Action(
            name="GetCustomerDetailsByCustomerId",
            kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
        ),
        ],
        outputs=[
            "\"customer_id\": \"a1b2c3d4-e5f6-7890-1234-567890abcdef\"",
            "\"residential_address\": {"
                "\"street_address\": \"789 Oak Avenue\", "
                "\"city\": \"Toronto\", "
                "\"state\": \"ON\", "
                "\"postal_code\": \"M5H 2N2\", "
                "\"country\": \"Canada\""
            "}"
        ],
    ),
Task(
    annotator="0",
    user_id="task_57",
    instruction=(
            "You are David Chen. "
            "By raising a support ticket, apply the update to your profile with the new address 12 Market Street, Oakland, CA 94103, USA."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        Action(
            name="AddSupportTicketForCustomerId",
            kwargs={
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
        ),
        Action(
            name="UpdateAddressForCustomerId",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "residential_address": {
                    "street_address": "12 Market Street",
                    "city": "Oakland",
                    "state": "CA",
                    "postal_code": "94103",
                    "country": "USA"
                }
            },
        ),
        Action(
            name="ChangeSupportTicketStatus",
            kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a","ticket_id": "tkt_1", "new_status": "Resolved"},
        ),
        Action(
            name="GetCustomerDetailsByCustomerId",
            kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"},
        ),
        ],
        outputs=[
            "\"customer_id\": \"d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a\"",
            "\"residential_address\": {"
                "\"street_address\": \"12 Market Street\", "
                "\"city\": \"San Francisco\", "
                "\"state\": \"CA\", "
                "\"postal_code\": \"94103\", "
                "\"country\": \"USA\""
            "}"
        ],
    ),

Task(
    annotator="0",
    user_id="task_58",
    instruction=(
            "You are Maria Garcia. "
            "After relocating to 45 Sunset Blvd, Orlando, FL 33101, USA, open a support ticket to document this change and update your residential address."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Maria", "last_name": "Garcia"},
        ),
        Action(
            name="AddSupportTicketForCustomerId",
            kwargs={
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
        ),
        Action(
            name="UpdateAddressForCustomerId",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "residential_address": {
                    "street_address": "45 Sunset Blvd",
                    "city": "Orlando",
                    "state": "FL",
                    "postal_code": "33101",
                    "country": "USA"
                }
            },
        ),
        Action(
            name="ChangeSupportTicketStatus",
            kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9","ticket_id": "tkt_1", "new_status": "Resolved"},
        ),
        Action(
            name="GetCustomerDetailsByCustomerId",
            kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"},
        ),
        ],
        outputs=[
            "\"customer_id\": \"f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9\"",
            "\"residential_address\": {"
                "\"street_address\": \"45 Sunset Blvd\", "
                "\"city\": \"Miami\", "
                "\"state\": \"FL\", "
                "\"postal_code\": \"33101\", "
                "\"country\": \"USA\""
            "}"
        ],
    ),
Task(
    annotator="0",
    user_id="task_59",
    instruction=(
            "You are Lakshmi Narayanan. "
            "Raise a support ticket and save the address change to update your new residence at 22 MG Road, Bengaluru, KA 560001, India."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"},
        ),
        Action(
            name="AddSupportTicketForCustomerId",
            kwargs={
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
        ),
        Action(
            name="UpdateAddressForCustomerId",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "residential_address": {
                    "street_address": "22 MG Road",
                    "city": "Bengaluru",
                    "state": "KA",
                    "postal_code": "560001",
                    "country": "India"
                }
            },
        ),
        Action(
            name="ChangeSupportTicketStatus",
            kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4","ticket_id": "tkt_1", "new_status": "Resolved"},
        ),
        Action(
            name="GetCustomerDetailsByCustomerId",
            kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"},
        ),
        ],
        outputs=[
            "\"customer_id\": \"a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4\"",
            "\"residential_address\": {"
                "\"street_address\": \"22 MG Road\", "
                "\"city\": \"Bengaluru\", "
                "\"state\": \"KA\", "
                "\"postal_code\": \"560001\", "
                "\"country\": \"India\""
            "}"
        ],
    ),

Task(
    annotator="0",
    user_id="task_60",
    instruction=(
            "You are Oliver Williams. "
            "Using the Mobile App, update your address to 55 Baker Street, Manchester, W1U 7EU, UK, by logging this request as a support ticket and confirming the change."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Oliver", "last_name": "Williams"},
        ),
        Action(
            name="AddSupportTicketForCustomerId",
            kwargs={
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
        ),
        Action(
            name="UpdateAddressForCustomerId",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "residential_address": {
                    "street_address": "55 Baker Street",
                    "city": "Manchester",
                    "state": "Manchester",
                    "postal_code": "W1U 7EU",
                    "country": "UK"
                }
            },
        ),
        Action(
            name="ChangeSupportTicketStatus",
            kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5","ticket_id": "tkt_1", "new_status": "Resolved"},
        ),
        Action(
            name="GetCustomerDetailsByCustomerId",
            kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"},
        ),
        ],
        outputs=[
            "\"customer_id\": \"b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5\"",
            "\"residential_address\": {"
                "\"street_address\": \"55 Baker Street\", "
                "\"city\": \"London\", "
                "\"state\": \"London\", "
                "\"postal_code\": \"W1U 7EU\", "
                "\"country\": \"UK\""
            "}"
        ],
    ),
Task(
    annotator="0",
    user_id="task_61",
    instruction=(
            "You are Fatima Al-Fassi. "
            "Provide your updated residential address as Villa 12, Palm Jumeirah, Abu Dhabi 00000, UAE by submitting a support ticket and initiating the update."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Fatima", "last_name": "Al-Fassi"},
        ),
        Action(
            name="AddSupportTicketForCustomerId",
            kwargs={
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
        ),
        Action(
            name="UpdateAddressForCustomerId",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "residential_address": {
                    "street_address": "Villa 12, Palm Jumeirah",
                    "city": "Abu Dhabi",
                    "state": "Abu Dhabi",
                    "postal_code": "00000",
                    "country": "UAE"
                }
            },
        ),
        Action(
            name="ChangeSupportTicketStatus",
            kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6","ticket_id": "tkt_1", "new_status": "Resolved"},
        ),
        Action(
            name="GetCustomerDetailsByCustomerId",
            kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"},
        ),
        ],
        outputs=[
            "\"customer_id\": \"c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6\"",
            "\"residential_address\": {"
                "\"street_address\": \"Villa 12, Palm Jumeirah\", "
                "\"city\": \"Dubai\", "
                "\"state\": \"Dubai\", "
                "\"postal_code\": \"00000\", "
                "\"country\": \"UAE\""
            "}"
        ],
    ),

Task(
    annotator=0,
    user_id="task_62",
    instruction=(
            "You are Jane Smith on 2025-07-24T15:30:00Z. "
            "Proceed to include your son, Ryan Smith, as a personal beneficiary (relationship “Son”) at Maple Bank with account number 777777777 and routing number 002111444. "
            "Next, arrange a monthly payment of CAD 300 from your Checking account, starting next month on 2025-08-24."
        ),
    actions=[
        # 1. Look up Jane Smith’s customer record
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        # 2. Add Ryan Smith as a new beneficiary
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_name": "Ryan Smith",
                "beneficiary_type": "Personal",
                "relationship": "Son",
                "bank_name": "Maple Bank",
                "account_number": "777777777",
                "routing_number": "002111444",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        # 3. Fetch that beneficiary’s ID
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_name": "Ryan Smith"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_id": "acc_chk_2001",
                "requested_amount": 300.0,
            },
        ),
        # 4. Create a monthly scheduled payment starting next month (2025-08-24)
        Action(
            name="CreateNewSchedulePayment",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "source_account_id": "acc_chk_2001",
                "beneficiary_id": "bene_1",
                "amount": 300.0,
                "currency": "CAD",
                "frequency": "Monthly",
                "start_date": "2025-08-24"
            },
        ),
        # 5. Retrieve the scheduled payment ID to confirm
        Action(
            name="GetPaymentIdByCustomerIdAndBeneficiaryId",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_1"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\"",
        "\"payment_id\": \"sp_1\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"amount\": 300.0, \"currency\": \"CAD\""
    ],
),
Task(
    annotator=0,
    user_id="task_63",
    instruction=(
            "You are David Chen on 2025-07-24T15:30:00Z. "
            "Proceed to add your nephew, Eric Chen, as a personal beneficiary (relationship “Nephew”) at City Bank with account number 999999999 and routing number 021000021. "
            "Then plan a monthly payment of USD 150 from your Checking account, starting next month on 2025-08-24."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_name": "Eric Chen",
                "beneficiary_type": "Personal",
                "relationship": "Nephew",
                "bank_name": "City Bank",
                "account_number": "999999999",
                "routing_number": "021000021",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_name": "Eric Chen"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_id": "acc_chk_3001",
                "requested_amount": 150.0,
            },
        ),
        Action(
            name="CreateNewSchedulePayment",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "source_account_id": "acc_chk_3001",
                "beneficiary_id": "bene_1",
                "amount": 150.0,
                "currency": "USD",
                "frequency": "Monthly",
                "start_date": "2025-08-24"
            },
        ),
        Action(
            name="GetPaymentIdByCustomerIdAndBeneficiaryId",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_id": "bene_1"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\"",
        "\"payment_id\": \"sp_1\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"amount\": 150.0, \"currency\": \"USD\""
    ],
),

Task(
    annotator=0,
    user_id="task_64",
    instruction=(
            "You are Maria Garcia on 2025-07-24T15:30:00Z. "
            "Choose to include your sister, Lucia Garcia, as a personal beneficiary (relationship “Sister”) at Horizon Bank with account number 333333333 and routing number 111222444. "
            "Then organize a monthly payment of USD 250 from your Checking account, beginning next month on 2025-08-24."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Maria", "last_name": "Garcia"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "beneficiary_name": "Lucia Garcia",
                "beneficiary_type": "Personal",
                "relationship": "Sister",
                "bank_name": "Horizon Bank",
                "account_number": "333333333",
                "routing_number": "111222444",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "beneficiary_name": "Lucia Garcia"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "account_id": "acc_chk_4001",
                "requested_amount": 250.0,
            },
        ),
        Action(
            name="CreateNewSchedulePayment",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "source_account_id": "acc_chk_4001",
                "beneficiary_id": "bene_1",
                "amount": 250.0,
                "currency": "USD",
                "frequency": "Monthly",
                "start_date": "2025-08-24"
            },
        ),
        Action(
            name="GetPaymentIdByCustomerIdAndBeneficiaryId",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "beneficiary_id": "bene_1"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\"",
        "\"payment_id\": \"sp_1\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"amount\": 250.0, \"currency\": \"USD\""
    ],
),
Task(
    annotator=0,
    user_id="task_65",
    instruction=(
            "You are Lakshmi Narayanan on 2025-07-24T15:30:00Z. "
            "Proceed to add your father, Narayan Rao, as a personal beneficiary (relationship “Father”) at State Bank of India with account number 222222222 and IFSC code SBIN000111. "
            "Then prepare a monthly payment of INR 5,000 from your Savings account, starting next month on 2025-08-24."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "beneficiary_name": "Narayan Rao",
                "beneficiary_type": "Personal",
                "relationship": "Father",
                "bank_name": "State Bank of India",
                "account_number": "222222222",
                "routing_number": "SBIN000111",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "beneficiary_name": "Narayan Rao"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_id": "acc_sav_5001",
                "requested_amount": 5000.0,
            },
        ),
        Action(
            name="CreateNewSchedulePayment",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "source_account_id": "acc_sav_5001",
                "beneficiary_id": "bene_1",
                "amount": 5000.0,
                "currency": "INR",
                "frequency": "Monthly",
                "start_date": "2025-08-24"
            },
        ),
        Action(
            name="GetPaymentIdByCustomerIdAndBeneficiaryId",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "beneficiary_id": "bene_1"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\"",
        "\"payment_id\": \"sp_1\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"amount\": 5000.0, \"currency\": \"INR\""
    ],
),


Task(
    annotator=0,
    user_id="task_66",
    instruction=(
            "As Oliver Williams on 2025-07-24T15:30:00Z, include your wife, Sophia Williams, as a personal beneficiary (relationship “Wife”) at Manchester Bank. "
            "Use the account number 444444444 and sort code 30-00-01. "
            "Next, arrange for a monthly payment of GBP 400 from your Checking account, commencing next month on 2025-08-24."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Oliver", "last_name": "Williams"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "beneficiary_name": "Sophia Williams",
                "beneficiary_type": "Personal",
                "relationship": "Wife",
                "bank_name": "London Bank",
                "account_number": "444444444",
                "routing_number": "30-00-01",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "beneficiary_name": "Sophia Williams"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "account_id": "acc_chk_6001",
                "requested_amount": 400.0,
            },
        ),
        Action(
            name="CreateNewSchedulePayment",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "source_account_id": "acc_chk_6001",
                "beneficiary_id": "bene_1",
                "amount": 400.0,
                "currency": "GBP",
                "frequency": "Monthly",
                "start_date": "2025-08-24"
            },
        ),
        Action(
            name="GetPaymentIdByCustomerIdAndBeneficiaryId",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "beneficiary_id": "bene_1"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\"",
        "\"payment_id\": \"sp_10\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"amount\": 400.0, \"currency\": \"GBP\""
    ],
),
Task(
    annotator=0,
    user_id="task_67",
    instruction=(
            "In the role of Fatima Al-Fassi on 2025-07-24T15:30:00Z, add your mother, Aisha Al-Fassi, as a personal beneficiary (relationship “Mother”) at Emirates Bank, using account number 555555555 and routing number EB000123. "
            "Subsequently, plan a monthly payment of AED 1,000 from your Savings account, starting next month from the date 2025-08-24."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Fatima", "last_name": "Al-Fassi"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "beneficiary_name": "Aisha Al-Fassi",
                "beneficiary_type": "Personal",
                "relationship": "Mother",
                "bank_name": "Emirates Bank",
                "account_number": "555555555",
                "routing_number": "EB000123",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "beneficiary_name": "Aisha Al-Fassi"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "account_id": "acc_sav_7002",
                "requested_amount": 1000.0,
            },
        ),
        Action(
            name="CreateNewSchedulePayment",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "source_account_id": "acc_sav_7002",
                "beneficiary_id": "bene_1",
                "amount": 1000.0,
                "currency": "AED",
                "frequency": "Monthly",
                "start_date": "2025-08-24"
            },
        ),
        Action(
            name="GetPaymentIdByCustomerIdAndBeneficiaryId",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "beneficiary_id": "bene_1"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\"",
        "\"payment_id\": \"sp_11\", \"frequency\": \"Monthly\", \"start_date\": \"2025-08-24\", \"amount\": 1000.0, \"currency\": \"AED\""
    ],
),

Task(
    annotator=0,
    user_id="task_68",
    instruction=(
            "Acting as Jane Smith, you wish to apply for a car loan amounting to CAD 40,000, intended to be paid over a period of 60 months for buying a new vehicle. "
            "Kindly submit a new loan application, and then check its status."
        ),
    actions=[
        # 1. Look up Elena Popescu’s customer record
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        # 2. Create a new loan application for a car loan
        Action(
            name="CreateNewLoanApplication",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "loan_type": "Car Loan",
                "requested_amount": 40000.0,
                "requested_term_months": 60,
                "purpose": "Vehicle Purchase"
            },
        ),
        # 3. Check the status of the newly created car loan application
        Action(
            name="GetLoanApplicationStatusByCustomerIdAndType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "loan_type": "Car Loan"
            },
        ),
    ],
    outputs=[
        "\"application_id\": \"app_10\"",
        "\"application_status\": \"Submitted\""
    ],
),

Task(
    annotator=0,
    user_id="task_69",
    instruction=(
            "In the position of David Chen, you intend to apply for a personal loan of USD 15,000 over a 48-month term for the purpose of home renovation. "
            "Please submit a new loan application and then verify its status."
        ),
    actions=[
        # 1. Look up Zoltan Nagy’s customer record
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        # 2. Create a new loan application for a personal loan
        Action(
            name="CreateNewLoanApplication",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "loan_type": "Personal",
                "requested_amount": 15000.0,
                "requested_term_months": 48,
                "purpose": "Home Renovation"
            },
        ),
        # 3. Check the status of the newly created personal loan application
        Action(
            name="GetLoanApplicationStatusByCustomerIdAndType",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "loan_type": "Personal"
            },
        ),
    ],
    outputs=[
        "\"application_id\": \"app_11\"",
        "\"application_status\": \"Submitted\""
    ],
),

Task(
    annotator=0,
    user_id="task_70",
    instruction=(
            "You are Lakshmi Narayanan, and you wish to create a new RON Checking account. "
            "Afterward, transfer RON 1000 from your existing Savings account into it, then confirm the balance of the new Checking account."
        ),
    actions=[
        # 1. Look up Kenji Tanaka’s customer record
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Elena", "last_name": "Popescu"},
        ),
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Checking"},
        ),
        # 2. Create a new Checking account
        Action(
            name="CreateNewAccountForCustomer",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                "account_type": "Checking",
                "account_type_code" : "chk",
                "currency" : "RON"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                "account_type": "Savings"
            },
        ),
        # 3. Transfer AUD 500 from Savings to the new Checking
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                "source_account_id": "acc_sav_25001",
                "target_account_id": "acc_1",
                "amount": 1000,
                "currency": "RON"
            },
        ),
        # 4. Verify the new Checking account balance
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-24",
                "account_type": "Checking"
            },
        ),
    ],
    outputs=[
        "\"account_id\": \"acc_1\"",
        "\"account_type\": \"Checking\"",
        "\"balance\": 1000.0"
    ],
),

Task(
    annotator=0,
    user_id="task_71",
    instruction=(
            "Your name is Oliver Williams. "
            "Your objective is to apply for a business loan amounting to GBP 120,000 over a period of 84 months to grow your business. "
            "Initiate a new loan application and afterwards check the status of the application."
        ),
    actions=[
        # 1. Look up Sofia Andersson’s customer record
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Oliver", "last_name": "Williams"},
        ),
        # 2. Create a new loan application for a business loan
        Action(
            name="CreateNewLoanApplication",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "loan_type": "Business",
                "requested_amount": 120000.0,
                "requested_term_months": 84,
                "purpose": "Business Expansion"
            },
        ),
        # 3. Check the status of the newly created business loan application
        Action(
            name="GetLoanApplicationStatusByCustomerIdAndType",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "loan_type": "Business"
            },
        ),
    ],
    outputs=[
        "\"application_id\": \"app_12\"",
        "\"application_status\": \"Submitted\""
    ],
),

Task(
    annotator=0,
    user_id="task_72",
    instruction=(
            "Your identity is Jane Smith as of 2025-07-24T15:30:00Z. "
            "Aim to add your daughter Lily Smith as a personal beneficiary (relationship “Daughter”) with account number 222222222 at Maple Bank (routing 002000111), then proceed to transfer CAD 200 from your Checking account to her and verify the updated balance."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_name": "Lily Smith",
                "beneficiary_type": "Personal",
                "relationship": "Daughter",
                "bank_name": "Maple Bank",
                "account_number": "222222222",
                "routing_number": "002000111",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_name": "Lily Smith"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_type": "Checking"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_id": "acc_chk_2001",
                "requested_amount": 200.0
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_id": "bene_1",
                "source_account_id": "acc_chk_2001",
                "amount": 200.0,
                "currency": "CAD"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_type": "Checking"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\"",
        "\"new_source_balance\": 2900.75"
    ],
),

Task(
    annotator=0,
    user_id="task_73",
    instruction=(
            "Identifying as David Chen on 2025-07-24T15:30:00Z, you aim to add your brother Alex Chen as a personal beneficiary (relationship “Brother”) with account number 333333333 at City Bank (routing 021000021). "
            "Subsequently, transfer USD 500 from your Checking account to him and confirm the updated balance."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_name": "Alex Chen",
                "beneficiary_type": "Personal",
                "relationship": "Brother",
                "bank_name": "City Bank",
                "account_number": "333333333",
                "routing_number": "021000021",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_name": "Alex Chen"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_type": "Checking"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_id": "acc_chk_3001",
                "requested_amount": 500.0
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_id": "bene_1",
                "source_account_id": "acc_chk_3001",
                "amount": 500.0,
                "currency": "USD"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_type": "Checking"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\"",
        "\"new_source_balance\": 12040.25"
    ],
),
Task(
    annotator=0,
    user_id="task_74",
    instruction=(
            "Recognize yourself as Maria Garcia on 2025-07-24T15:30:00Z. "
            "You intend to include your friend Carla Lopez as a personal beneficiary (relationship “Friend”) with account number 444444444 at Horizon Bank (routing 111222444). "
            "Following this, transfer USD 150 from your Checking account to her and verify the new balance."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Maria", "last_name": "Garcia"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "beneficiary_name": "Carla Lopez",
                "beneficiary_type": "Personal",
                "relationship": "Friend",
                "bank_name": "Horizon Bank",
                "account_number": "444444444",
                "routing_number": "111222444",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "beneficiary_name": "Carla Lopez"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "account_type": "Checking"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "account_id": "acc_chk_4001",
                "requested_amount": 150.0
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "beneficiary_id": "bene_1",
                "source_account_id": "acc_chk_4001",
                "amount": 150.0,
                "currency": "USD"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "account_type": "Checking"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\"",
        "\"new_source_balance\": 1050.50"
    ],
),
Task(
    annotator=0,
    user_id="task_75",
    instruction=(
            "You are known as Lakshmi Narayanan on 2025-07-24T15:30:00Z. "
            "Plan to add your father, Narayan Rao, as a personal beneficiary (relationship “Father”) with account number 555555555 at State Bank of India (IFSC SBIN000123). "
            "After that, move INR 1,000 from your Savings account to him and confirm the updated balance."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "beneficiary_name": "Narayan Rao",
                "beneficiary_type": "Personal",
                "relationship": "Father",
                "bank_name": "State Bank of India",
                "account_number": "555555555",
                "routing_number": "SBIN000123",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "beneficiary_name": "Narayan Rao"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_type": "Savings"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_id": "acc_sav_5001",
                "requested_amount": 1000.0
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "beneficiary_id": "bene_1",
                "source_account_id": "acc_sav_5001",
                "amount": 1000.0,
                "currency": "INR"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_type": "Savings"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\"",
        "\"new_source_balance\": 2,499,000.00"
    ],
),
Task(
    annotator=0,
    user_id="task_76",
    instruction=(
            "Acting as Oliver Williams on 2025-07-24T15:30:00Z, your goal is to list your wife, Sophia Williams, as a personal beneficiary (relationship “Wife”) using account number 666666666 at Manchester Bank (sort code 30-00-01), subsequently transfer GBP 300 from your Checking account to her, and verify the updated balance."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Oliver", "last_name": "Williams"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "beneficiary_name": "Sophia Williams",
                "beneficiary_type": "Personal",
                "relationship": "Wife",
                "bank_name": "London Bank",
                "account_number": "666666666",
                "routing_number": "30-00-01",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "beneficiary_name": "Sophia Williams"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "account_type": "Checking"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "account_id": "acc_chk_6001",
                "requested_amount": 300.0
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "beneficiary_id": "bene_1",
                "source_account_id": "acc_chk_6001",
                "amount": 300.0,
                "currency": "GBP"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "account_type": "Checking"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\"",
        "\"new_source_balance\": 550.75"
    ],
),

Task(
    annotator=0,
    user_id="task_77",
    instruction=(
            "In the role of Fatima Al-Fassi on 2025-07-24T15:30:00Z, you intend to designate your mother, Aisha Al-Fassi, as a personal beneficiary (relationship “Mother”) with account number 777123777 at Emirates Bank (routing EB000123), followed by transferring AED 1,000 from your Savings account to her, and confirm the new balance."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Fatima", "last_name": "Al-Fassi"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "beneficiary_name": "Aisha Al-Fassi",
                "beneficiary_type": "Personal",
                "relationship": "Mother",
                "bank_name": "Emirates Bank",
                "account_number": "777123777",
                "routing_number": "EB000123",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "beneficiary_name": "Aisha Al-Fassi"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "account_type": "Savings"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "account_id": "acc_sav_7002",
                "requested_amount": 1000.0
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "beneficiary_id": "bene_1",
                "source_account_id": "acc_sav_7002",
                "amount": 1000.0,
                "currency": "AED"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "account_type": "Savings"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\"",
        "\"new_source_balance\": 749000.0"
    ],
),
Task(
    annotator=0,
    user_id="task_78",
    instruction=(
            "Identifying as Anja Novak on 2025-07-24T15:30:00Z, you aim to add your friend, Sofia Lopez, as a personal beneficiary (relationship “Friend”) with account number 888888888 at Santander Bank (routing 123456789), then proceed to transfer EUR 500 from your Checking account to her, and verify the updated balance."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Anja", "last_name": "Novak"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                "beneficiary_name": "Sofia Lopez",
                "beneficiary_type": "Personal",
                "relationship": "Friend",
                "bank_name": "Santander Bank",
                "account_number": "888888888",
                "routing_number": "123456789",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                "beneficiary_name": "Sofia Lopez"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                "account_type": "Checking"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                "account_id": "acc_chk_19001",
                "requested_amount": 500.0
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                "beneficiary_id": "bene_1",
                "source_account_id": "acc_chk_19001",
                "amount": 500.0,
                "currency": "EUR"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                "account_type": "Checking"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\"",
        "\"new_source_balance\": 3000.00"
    ],
),

Task(
    annotator=0,
    user_id="task_79",
    instruction=(
            "Taking on the persona of Yara Haddad on 2025-07-24T15:30:00Z, your task is to add your son, Noah Johnson, as a personal beneficiary (relationship “Son”) with account number 111111111 at Metro Bank (routing 111000999), then continue to transfer USD 300 from your Checking account to him, and validate the new balance."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Yara", "last_name": "Haddad"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                "beneficiary_name": "Noah Johnson",
                "beneficiary_type": "Personal",
                "relationship": "Son",
                "bank_name": "Metro Bank",
                "account_number": "111111111",
                "routing_number": "111000999",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                "beneficiary_name": "Noah Johnson"
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                "account_type": "Checking"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                "account_id": "acc_chk_21001",
                "requested_amount": 300.0
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                "beneficiary_id": "bene_1",
                "source_account_id": "acc_chk_21001",
                "amount": 300.0,
                "currency": "USD"
            },
        ),
        Action(
                name="GetAccountDetailsByCustomerIdAndAccountId",
                kwargs={
                    "customer_id": "e5f6a1b2-c3d4-e5f6-a1b2-c3d4e5f6a1b2-20",
                    "account_id": "acc_chk_21001"
                },
            ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\"",
        "\"new_source_balance\": 14700.00"
    ],
),
Task(
    annotator=0,
    user_id="task_80",
    instruction=(
            "You are posing as David Chen. "
            "The task is to apply for a home loan amounting to USD 250,000 over a term of 300 months to fund the purchase of a new property. "
            "Proceed by submitting a new loan application and afterward check the application status."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        Action(
            name="CreateNewLoanApplication",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "loan_type": "Home",
                "requested_amount": 250000.0,
                "requested_term_months": 300,
                "purpose": "Home Purchase"
            },
        ),
        Action(
            name="GetLoanApplicationStatusByCustomerIdAndType",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "loan_type": "Home"
            },
        ),
    ],
    outputs=[
        "\"application_id\": \"app_13\"",
        "\"application_status\": \"Submitted\""
    ],
),
Task(
    annotator=0,
    user_id="task_81",
    instruction=(
            "Your name is Maria Garcia. "
            "You intend to apply for a home loan of USD 320,000 over 360 months to buy a new home. "
            "Submit a new loan application and then check its status."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Maria", "last_name": "Garcia"},
        ),
        Action(
            name="CreateNewLoanApplication",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "loan_type": "Home",
                "requested_amount": 320000.0,
                "requested_term_months": 360,
                "purpose": "Home Purchase"
            },
        ),
        Action(
            name="GetLoanApplicationStatusByCustomerIdAndType",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "loan_type": "Home"
            },
        ),
    ],
    outputs=[
        "\"application_id\": \"app_14\"",
        "\"application_status\": \"Submitted\""
    ],
),
Task(
    annotator=0,
    user_id="task_82",
    instruction=(
            "You are Oliver Williams. "
            "You plan to apply for a home loan of GBP 200,000 over 300 months to purchase a townhome. "
            "Submit a new loan application and then retrieve its status."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Oliver", "last_name": "Williams"},
        ),
        Action(
            name="CreateNewLoanApplication",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "loan_type": "Home",
                "requested_amount": 200000.0,
                "requested_term_months": 300,
                "purpose": "Townhome Purchase"
            },
        ),
        Action(
            name="GetLoanApplicationStatusByCustomerIdAndType",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "loan_type": "Home"
            },
        ),
    ],
    outputs=[
        "\"application_id\": \"app_15\"",
        "\"application_status\": \"Submitted\""
    ],
),
Task(
    annotator=0,
    user_id="task_83",
    instruction=(
            "Your name is Lakshmi Narayanan. "
            "You wish to apply for a home loan of INR 5,000,000 over 240 months to purchase a villa. "
            "Submit a new loan application and then check its status."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"},
        ),
        Action(
            name="CreateNewLoanApplication",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "loan_type": "Home",
                "requested_amount": 5000000.0,
                "requested_term_months": 240,
                "purpose": "Villa Purchase"
            },
        ),
        Action(
            name="GetLoanApplicationStatusByCustomerIdAndType",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "loan_type": "Home"
            },
        ),
    ],
    outputs=[
        "\"application_id\": \"app_16\"",
        "\"application_status\": \"Submitted\""
    ],
),

Task(
        annotator=0,
        user_id="task_84",
        instruction=(
            "You are Noah Kim. "
            "Your Checking account faces a hacking threat, so for security reasons, you wish to block it. "
            "You are using your Mobile app to file the ticket. "
            "Please open a support ticket to block that Checking account, then mark the ticket resolved."
        ),
        actions=[
            # 1. Look up Kenji Tanaka’s customer record
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "Noah", "last_name": "Kim"},
            ),
            # 2. Open a support ticket to block the lost card
            Action(
                name="AddSupportTicketForCustomerId",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",  # Kenji Tanaka’s ID :contentReference[oaicite:2]{index=2}
                    "priority": "High",
                    "channel": "Mobile App",
                    "category": "Security",
                    "target_entity": "Account",
                    "target_id": "acc_chk_16001",  # Chloe’s credit card :contentReference[oaicite:3]{index=3}
                    "operation": "BlockAccount",
                },
            ),
            # 3. Block the credit card account
            Action(
                name="BlockAccountForCustomerId",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "account_id": "acc_chk_16001"
                },
            ),
            # 4. Close the support ticket
            Action(
                name="ChangeSupportTicketStatus",
                kwargs={"ticket_id": "tkt_1","customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15", "new_status": "Resolved"},
            ),
            # 5. Verify that the credit card status is now blocked
            Action(
                name="GetAccountDetailsByCustomerIdAndAccountId",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3-15",
                    "account_id": "acc_chk_16001"
                },
            ),
        ],
        outputs=[
            # From step 2
            "\"ticket_id\": \"tkt_1\"",
            "\"account_id\": \"acc_chk_16001\", \"status\": \"Blocked\""
        ],
    ),
Task(
        annotator=0,
        user_id="task_85",
        instruction=(
            "Your name is Anja Novak. "
            "Your Checking account is being scammed, so for security, you wish to block it. "
            "You are using your Web portal to file the ticket. "
            "Please open a support ticket to block that Checking account, then mark the ticket resolved."
        ),
        actions=[
            # 1. Look up Kenji Tanaka’s customer record
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "Anja", "last_name": "Novak"},
            ),
            # 2. Open a support ticket to block the lost card
            Action(
                name="AddSupportTicketForCustomerId",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",  # Kenji Tanaka’s ID :contentReference[oaicite:2]{index=2}
                    "priority": "High",
                    "channel": "Web portal",
                    "category": "Security",
                    "target_entity": "Account",
                    "target_id": "acc_chk_19001",  # Chloe’s credit card :contentReference[oaicite:3]{index=3}
                    "operation": "BlockAccount",
                },
            ),
            # 3. Block the credit card account
            Action(
                name="BlockAccountForCustomerId",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "account_id": "acc_chk_19001"
                },
            ),
            # 4. Close the support ticket
            Action(
                name="ChangeSupportTicketStatus",
                kwargs={"ticket_id": "tkt_1","customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18", "new_status": "Resolved"},
            ),
            # 5. Verify that the credit card status is now blocked
            Action(
                name="GetAccountDetailsByCustomerIdAndAccountId",
                kwargs={
                    "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6-18",
                    "account_id": "acc_chk_19001"
                },
            ),
        ],
        outputs=[
            # From step 2
            "\"ticket_id\": \"tkt_1\"",
            "\"account_id\": \"acc_chk_19001\", \"status\": \"Blocked\""
        ],
    ),
Task(
    annotator=0,
    user_id="task_86",
    instruction=(
            "Your name is Jane Smith. "
            "It is necessary to transfer CAD 100 from your Checking account (acc_chk_2001) to the beneficiary Kenji Tanaka, then determine your total balance across all of your accounts."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_name": "Kenji Tanaka"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_id": "acc_chk_2001",
                "requested_amount": 100.0
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "source_account_id": "acc_chk_2001",
                "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f",
                "amount": 100.0,
                "currency": "CAD"
            },
        ),
        Action(
            name="CalculateTotalBalance",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_ids": ["acc_chk_2001","acc_sav_2002"]
            },
        ),
    ],
    outputs=[
        "\"total_balance\": 25000.75\""
    ],
),

Task(
    annotator=0,
    user_id="task_87",
    instruction=(
            "You are Fatima Al-Fassi. "
            "Transfer AED 1000 from your Savings account (acc_sav_7002) to the beneficiary Abu Dhabi International School, then compute your total balance across all accounts."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Fatima", "last_name": "Al-Fassi"},
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "beneficiary_name": "Dubai International School"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "account_id": "acc_sav_7002",
                "requested_amount": 1000.00
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "source_account_id": "acc_sav_7002",
                "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f",
                "amount": 1000.00,
                "currency": "AED"
            },
        ),
        Action(
            name="CalculateTotalBalance",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "account_ids": ["acc_chk_7001","acc_sav_7002"]
            },
        ),
    ],
    outputs=[
        "\"total_balance\": 899000.00\""
    ],
),

Task(
    annotator=0,
    user_id="task_88",
    instruction=(
            "You are Fatima Al-Fassi. "
            "Transfer AED 1000 from your Savings account (acc_sav_7002) to the beneficiary Abu Dhabi International School, then compute your total balance across all accounts."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Fatima", "last_name": "Al-Fassi"},
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "beneficiary_name": "Dubai International School"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "account_id": "acc_sav_7002",
                "requested_amount": 1000.00
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "source_account_id": "acc_sav_7002",
                "beneficiary_id": "bene_1c9d8e7f-6a5b-4c3d-2e1f-0a9b8c7d6e5f",
                "amount": 1000.00,
                "currency": "AED"
            },
        ),
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6"},
        ),
        Action(
            name="CalculateTotalBalance",
            kwargs={
                "customer_id": "c3d4e5f6-a1b2-c3d4-e5f6-a1b2c3d4e5f6",
                "account_ids": ["acc_chk_7001","acc_sav_7002"]
            },
        ),
    ],
    outputs=[
        "\"total_balance\": 899000.00\""
    ],
),



Task(
    annotator=0,
    user_id="task_89",
    instruction=(
            "Your name is Jane Smith. "
            "You need to initiate a transfer of CAD 1000 from your Checking account (acc_chk_2001) to your beneficiary Kenji Tanaka, then assess your total balance across all of your accounts."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_name": "Kenji Tanaka"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_id": "acc_chk_2001",
                "requested_amount": 1000.0
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "source_account_id": "acc_chk_2001",
                "beneficiary_id": "bene_7c6d5e4f-3a2b-1c9d-8e7f-6a5b4c3d2e1f",
                "amount": 1000.0,
                "currency": "CAD"
            },
        ),
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
        ),
        Action(
            name="CalculateTotalBalance",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_ids": ["acc_chk_2001","acc_sav_2002"]
            },
        ),
    ],
    outputs=[
        "\"total_balance\": 24100.75\""
    ],
),


Task(
    annotator=0,
    user_id="task_90",
    instruction=(
            "You are Lakshmi Narayanan. "
            "You must transfer INR 2,000 from your Checking account (acc_chk_5002) to your beneficiary Global ISP, then evaluate your total balance across all your accounts."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"},
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "beneficiary_name": "Global ISP"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_id": "acc_chk_5002",
                "requested_amount": 2000.0
            },
        ),
        Action(
            name="PayToBeneficiarySameCurrency",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "source_account_id": "acc_chk_5002",
                "beneficiary_id": "bene_5e4f3a2b-1c9d-8e7f-6a5b-4c3d2e1f0a9b",
                "amount": 2000.0,
                "currency": "INR"
            },
        ),
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"},
        ),
        Action(
            name="CalculateTotalBalance",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_ids": ["acc_chk_5002","acc_sav_5001"]
            },
        ),
    ],
    outputs=[
        "\"total_balance\": 2548000.0\""
    ],
),
Task(
    annotator="0",
    user_id="task_91",
    instruction=(
            "You are Elena Popescu on 2025-07-24T15:30:00Z. "
            "Include a new personal beneficiary titled Ryan Smith (your brother) at Maple Bank, account number 987654321, routing number 122105155."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_name": "Ryan Smith",
                "beneficiary_type": "Personal",
                "relationship": "Brother",
                "bank_name": "Maple Bank",
                "account_number": "987654321",
                "routing_number": "122105155",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "beneficiary_name": "Ryan Smith"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\","
        "\"beneficiary_name\": \"Ryan Smith\","
        "\"beneficiary_type\": \"Personal\","
        "\"relationship\": \"Brother\","
        "\"account_details\": {\"bank_name\": \"Maple Bank\", \"account_number\": \"987654321\", \"routing_number\": \"122105155\"},"
        "\"date_added\": \"2025-07-24\""
    ],
),
Task(
    annotator="0",
    user_id="task_92",
    instruction=(
            "You are Zoltan Nagy on 2025-07-24T15:30:00Z. "
            "Incorporate a new personal beneficiary named Alex Lee (your friend) at City National Bank, account number 111222333, routing number 021000089."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_name": "Alex Lee",
                "beneficiary_type": "Personal",
                "relationship": "Friend",
                "bank_name": "City National Bank",
                "account_number": "111222333",
                "routing_number": "021000089",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "beneficiary_name": "Alex Lee"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\","
        "\"beneficiary_name\": \"Alex Lee\","
        "\"beneficiary_type\": \"Personal\","
        "\"relationship\": \"Friend\","
        "\"account_details\": {\"bank_name\": \"City National Bank\", \"account_number\": \"111222333\", \"routing_number\": \"021000089\"},"
        "\"date_added\": \"2025-07-24\""
    ],
),
Task(
        annotator=0,
        user_id="task_93",
        instruction=(
            "You are Kenji Tanaka. "
            "Since your password for Checking account (acc_chk_10001) is compromised, block it for security reasons. "
            "Use your Web Portal to file the ticket. "
            "Please submit a support ticket to block that Checking account, then mark the ticket resolved."
        ),
        actions=[
            # 1. Look up Kenji Tanaka’s customer record
            Action(
                name="GetCustomerDetailsByName",
                kwargs={"first_name": "Kenji", "last_name": "Tanaka"},
            ),
            # 2. Open a support ticket to block the lost card
            Action(
                name="AddSupportTicketForCustomerId",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",  # Kenji Tanaka’s ID :contentReference[oaicite:2]{index=2}
                    "priority": "High",
                    "channel": "Web Portal",
                    "category": "Security",
                    "target_entity": "Account",
                    "target_id": "acc_chk_10001",  # Chloe’s credit card :contentReference[oaicite:3]{index=3}
                    "operation": "BlockAccount",
                },
            ),
            # 3. Block the credit card account
            Action(
                name="BlockAccountForCustomerId",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "account_id": "acc_chk_10001"
                },
            ),
            # 4. Close the support ticket
            Action(
                name="ChangeSupportTicketStatus",
                kwargs={"ticket_id": "tkt_1","customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3", "new_status": "Resolved"},
            ),
            # 5. Verify that the credit card status is now blocked
            Action(
                name="GetAccountDetailsByCustomerIdAndAccountId",
                kwargs={
                    "customer_id": "f6a1b2c3-d4e5-f6a1-b2c3-d4e5f6a1b2c3",
                    "account_id": "acc_chk_10001"
                },
            ),
        ],
        outputs=[
            # From step 2
            "\"ticket_id\": \"tkt_1\"",
            "\"account_id\": \"acc_chk_10001\", \"status\": \"Blocked\""
        ],
    ),
Task(
    annotator="0",
    user_id="task_94",
    instruction=(
            "You are Sofia Andersson on 2025-07-24T15:30:00Z. "
            "Insert a new personal beneficiary called Sophia Williams (your wife) at Manchester Bank, account number 555666777, routing number 040000000."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Oliver", "last_name": "Williams"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "beneficiary_name": "Sophia Williams",
                "beneficiary_type": "Personal",
                "relationship": "Wife",
                "bank_name": "London Bank",
                "account_number": "555666777",
                "routing_number": "040000000",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "beneficiary_name": "Sophia Williams"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\","
        "\"beneficiary_name\": \"Sophia Williams\","
        "\"beneficiary_type\": \"Personal\","
        "\"relationship\": \"Wife\","
        "\"account_details\": {\"bank_name\": \"London Bank\", \"account_number\": \"555666777\", \"routing_number\": \"040000000\"},"
        "\"date_added\": \"2025-07-24T15:30:00Z\""
    ],
),

Task(
    annotator="0",
    user_id="task_95",
    instruction=(
            "You are Zoltan Nagy on 2025-07-24T15:30:00Z. "
            "Enter a new personal beneficiary titled Narayan Rao (your father) at State Bank of India, account number 888999000, routing number SBIN000123."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"},
        ),
        Action(
            name="AddNewBeneficiaryForCustomer",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "beneficiary_name": "Narayan Rao",
                "beneficiary_type": "Personal",
                "relationship": "Father",
                "bank_name": "State Bank of India",
                "account_number": "888999000",
                "routing_number": "SBIN000123",
                    "date_added": "2025-07-24T15:30:00Z"
            },
        ),
        Action(
            name="GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "beneficiary_name": "Narayan Rao"
            },
        ),
    ],
    outputs=[
        "\"beneficiary_id\": \"bene_1\","
        "\"beneficiary_name\": \"Narayan Rao\","
        "\"beneficiary_type\": \"Personal\","
        "\"relationship\": \"Father\","
        "\"account_details\": {\"bank_name\": \"State Bank of India\", \"account_number\": \"888999000\", \"routing_number\": \"SBIN000123\"},"
        "\"date_added\": \"2025-07-24T15:30:00Z\""
    ],
),
Task(
    annotator="0",
    user_id="task_96",
    instruction=(
            "Assume you are Elena Popescu and initiate the creation of a new Savings account, followed by an immediate transfer of CAD 600 from your existing Checking account into it."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Jane", "last_name": "Smith"},
        ),
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"},
        ),
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Savings"},
        ),
        Action(
            name="CreateNewAccountForCustomer",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_type": "Savings",
                "account_type_code": "sav",
                "currency": "CAD",
            },
        ),
        Action(
            name="GetAccountDetailsByCustomerIdAndAccountId",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_id": "acc_1"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "account_id": "acc_chk_2001",
                "requested_amount": 600.0,
            },
        ),
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "source_account_id": "acc_chk_2001",
                "target_account_id": "acc_1",
                "currency": "CAD",
                "amount": 600.0,
            },
        ),
    ],
    outputs=[
        '"message": "Transfer successful (same currency).",'
        '"source_account_id": "acc_chk_2001",'
        '"target_account_id": "acc_1",'
        '"amount_transferred": 600.0,'
        '"currency": "CAD",'
        '"source_balance": 2500.75,'
        '"target_balance": 600.0'
    ],
),
Task(
    annotator="0",
    user_id="task_97",
    instruction=(
            "Assume you are Zoltan Nagy and open a new Savings account, then promptly transfer USD 800 from your existing Checking account into it."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "David", "last_name": "Chen"},
        ),
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"},
        ),
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Savings"},
        ),
        Action(
            name="CreateNewAccountForCustomer",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_type": "Savings",
                "account_type_code": "sav",
                "currency": "USD",
            },
        ),
        Action(
            name="GetAccountDetailsByCustomerIdAndAccountId",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_id": "acc_1"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "account_id": "acc_chk_3001",
                "requested_amount": 800.0,
            },
        ),
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
                "source_account_id": "acc_chk_3001",
                "target_account_id": "acc_1",
                "currency": "USD",
                "amount": 800.0,
            },
        ),
    ],
    outputs=[
        '"message": "Transfer successful (same currency).",'
        '"source_account_id": "acc_chk_3001",'
        '"target_account_id": "acc_1",'
        '"amount_transferred": 800.0,'
        '"currency": "USD",'
        '"source_balance": 8720.00,'
        '"target_balance": 800.0'
    ],
),

Task(
    annotator="0",
    user_id="task_98",
    instruction=(
            "Assume you are Sofia Andersson and start by creating a new Savings account, then make an immediate transfer of USD 700 from your current Checking account into it."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Maria", "last_name": "Garcia"},
        ),
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9"},
        ),
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Savings"},
        ),
        Action(
            name="CreateNewAccountForCustomer",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "account_type": "Savings",
                "account_type_code": "sav",
                "currency": "USD",
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "account_type": "Savings",
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "account_id": "acc_chk_4001",
                "requested_amount": 700.0,
            },
        ),
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "f4g5h6i7-j8k9-l0m1-n2o3-p4q5r6s7t8u9",
                "source_account_id": "acc_chk_4001",
                "target_account_id": "acc_1",
                "currency": "USD",
                "amount": 700.0,
            },
        ),
    ],
    outputs=[
        '"source_account_id": "acc_chk_4001",'
        '"target_account_id": "acc_1",'
        '"amount_transferred": 700.0,'
        '"currency": "USD",'
        '"source_balance": 6550.00,'
        '"target_balance": 700.0'
    ],
),
Task(
    annotator="0",
    user_id="task_99",
    instruction=(
            "Assume you are Sofia Andersson and proceed to establish a new Savings account, with an immediate transfer of GBP 400 from your current Checking account into it."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Oliver", "last_name": "Williams"},
        ),
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5"},
        ),
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Savings"},
        ),
        Action(
            name="CreateNewAccountForCustomer",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "account_type": "Savings",
                "account_type_code": "sav",
                "currency": "GBP",
            },
        ),
        Action(
            name="GetCustomerAccountDetailsByCustomerIdAndAccountType",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "account_type": "Savings",
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "account_id": "acc_chk_6001",
                "requested_amount": 400.0,
            },
        ),
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "b2c3d4e5-f6a1-b2c3-d4e5-f6a1b2c3d4e5",
                "source_account_id": "acc_chk_6001",
                "target_account_id": "acc_1",
                "currency": "GBP",
                "amount": 400.0,
            },
        ),
    ],
    outputs=[
        '"message": "Transfer successful (same currency).",'
        '"source_account_id": "acc_chk_6001",'
        '"target_account_id": "acc_1",'
        '"amount_transferred": 400.0,'
        '"currency": "GBP",'
        '"source_balance": 3200.00,'
        '"target_balance": 400.0'
    ],
),
Task(
    annotator="0",
    user_id="task_100",
    instruction=(
            "Assume you are Zoltan Nagy and initiate the process of opening a new Savings account, followed by an immediate transfer of INR 50,000 from your present Checking account into it."
        ),
    actions=[
        Action(
            name="GetCustomerDetailsByName",
            kwargs={"first_name": "Lakshmi", "last_name": "Narayanan"},
        ),
        Action(
            name="GetAllAccountsOfCustomerByCustomerId",
            kwargs={"customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4"},
        ),
        Action(
            name="GetAccountTypeAndAccountTypeCode",
            kwargs={"account_type": "Savings"},
        ),
        Action(
            name="CreateNewAccountForCustomer",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_type": "Savings",
                "account_type_code": "sav",
                "currency": "INR",
            },
        ),
        Action(
            name="GetAccountDetailsByCustomerIdAndAccountId",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_id": "acc_1"
            },
        ),
        Action(
            name="CheckAccountBalance",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "account_id": "acc_chk_5002",
                "requested_amount": 50000.0,
            },
        ),
        Action(
            name="TransferMoneySameCurrency",
            kwargs={
                "customer_id": "a1b2c3d4-e5f6-a1b2-c3d4-e5f6a1b2c3d4",
                "source_account_id": "acc_chk_5002",
                "target_account_id": "acc_1",
                "currency": "INR",
                "amount": 50000.0,
            },
        ),
    ],
    outputs=[
        '"source_account_id": "acc_chk_5002",'
        '"target_account_id": "acc_1",'
        '"amount_transferred": 50000.0,'
        '"currency": "INR",'
        '"source_balance": 0.00,'
        '"target_balance": 50000.0'
    ],
),


]
