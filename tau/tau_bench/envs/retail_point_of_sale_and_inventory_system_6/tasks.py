
tasks = [
    {
        "annotator": 0,
        "user_id": "marketer_01",
        "instruction": "Conduct a customer segmentation analysis for bronze membership customers on 2025-08-25 at STORE-005 with store manager EMP-1045. Search for all bronze tier customers, analyze customer demographics and purchasing patterns, evaluate marketing opt-in rates, and increase customer loyalty points by adding 500 points to the first bronze customer.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "membership_level": "bronze"
                },
            },
            {
                "name": "FindCustomers",
                "arguments": {
                    "membership_level": "bronze",
                    "opt_in_marketing": true
                },
            },
            {
                "name": "FindCustomers",
                "arguments": {
                    "membership_level": "bronze",
                    "opt_in_marketing": false
                },
            },
            {
                "name": "UpdateCustomer",
                "arguments": {
                    "timestamp": "2025-08-25T16:45:00Z",
                    "customer_id": "CUST-5003",
                    "loyalty_points": 960
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "employee_id": "EMP-1045"
                }
            }
        ],
        "outputs": [
                "\"bronze_customers\": [{\"customer_id\": \"CUST-5003\", \"name\": \"Sophia Singh\", \"opt_in_marketing\": true}, {\"customer_id\": \"CUST-5005\", \"name\": \"Ava Martinez\", \"opt_in_marketing\": false}, {\"customer_id\": \"CUST-5007\", \"name\": \"Olivia Romano\", \"opt_in_marketing\": false}]",
                "\"marketing_opt_ins\": [{\"customer_id\": \"CUST-5003\", \"name\": \"Sophia Singh\", \"opt_in_marketing\": true}]",
                "\"marketing_opt_outs\": [{\"customer_id\": \"CUST-5005\", \"name\": \"Ava Martinez\", \"opt_in_marketing\": false}, {\"customer_id\": \"CUST-5007\", \"name\": \"Olivia Romano\", \"opt_in_marketing\": false}]",
                "\"customer_updated\": {\"customer_id\": \"CUST-5003\", \"loyalty_points\": 960, \"updated_at\": \"2025-08-25T16:45:00Z\"}",
                "\"manager_info\": {\"employee_id\": \"EMP-1045\", \"name\": \"Megan Young\", \"role\": \"Store Manager\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_00",
        "instruction": "Process a customer request for James O'Connor to opt out of marketing communications. Confirm customer details, review current marketing preferences, update the preference, and log the change.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "James O'Connor"
                },
            },
            {
                "name": "FindCustomers",
                "arguments": {
                    "customer_id": "CUST-5008"
                },
            },
            {
                "name": "FindCustomers",
                "arguments": {
                    "email": "james.oconnor@example.com"
                },
            },
            {
                "name": "UpdateCustomer",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "customer_id": "CUST-5008",
                    "opt_in_marketing": false
                },
            },
            {
                "name": "FindCustomers",
                "arguments": {
                    "customer_id": "CUST-5008"
                }
            }
        ],
        "outputs": [
                "{\n  \"customer_verification\": {\"customer_id\": \"CUST-5008\", \"name\": \"James O'Connor\", \"email\": \"james.oconnor@example.com\"}\n}",
                "{\n  \"preference_check\": {\"customer_id\": \"CUST-5008\", \"current_opt_in\": true}\n}",
                "{\n  \"customer_updated\": {\"customer_id\": \"CUST-5008\", \"opt_in_marketing\": false}\n}",
                "{\n  \"verification_complete\": {\"customer_id\": \"CUST-5008\", \"status\": \"updated\"}\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "manager_04",
        "instruction": "Carry out a customer loyalty program analysis on 2025-11-20 at STORE-005 with store manager EMP-1045. Investigate customer data across all membership levels, identify high-value customers, examine recent transaction patterns, and implement targeted enhancements including point adjustments and membership upgrades.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "membership_level": "platinum"
                },
            },
            {
                "name": "FindCustomers",
                "arguments": {
                    "membership_level": "gold"
                },
            },
            {
                "name": "FindCustomers",
                "arguments": {
                    "membership_level": "silver"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "customer_id": "CUST-5001"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "customer_id": "CUST-5004"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "customer_id": "CUST-5006"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "customer_id": "CUST-5001",
                    "store_id": "STORE-005"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "customer_id": "CUST-5004",
                    "store_id": "STORE-005"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "customer_id": "CUST-5006",
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "UpdateCustomer",
                "arguments": {
                    "timestamp": "2025-11-20T16:45:00Z",
                    "customer_id": "CUST-5004",
                    "loyalty_points": 1570
                },
            },
            {
                "name": "UpdateCustomer",
                "arguments": {
                    "timestamp": "2025-11-20T16:45:00Z",
                    "customer_id": "CUST-5006",
                    "membership_level": "gold"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "employee_id": "EMP-1045"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "store_id": "STORE-005",
                    "role": "Store Manager"
                }
            }
        ],
        "outputs": [
                "\"loyalty_program_analysis\": {\"platinum_customers\": 1, \"gold_customers\": 2, \"silver_customers\": 4, \"total_active_members\": 7}",
                "\"high_value_customers\": [{\"customer_id\": \"CUST-5001\", \"name\": \"Emma Wilson\", \"loyalty_points\": 1240, \"total_spent\": 789.97}, {\"customer_id\": \"CUST-5004\", \"name\": \"Liam Anderson\", \"loyalty_points\": 1520, \"total_spent\": 205.48}]",
                "\"transaction_patterns\": [{\"customer_id\": \"CUST-5001\", \"recent_transactions\": 1, \"avg_transaction_value\": 789.97}, {\"customer_id\": \"CUST-5004\", \"recent_transactions\": 1, \"avg_transaction_value\": 205.48}]",
                "\"loyalty_updates\": [{\"customer_id\": \"CUST-5004\", \"loyalty_points\": 1570, \"points_added\": 50, \"updated_at\": \"2025-11-20T16:45:00Z\"}, {\"customer_id\": \"CUST-5006\", \"membership_level\": \"gold\", \"upgraded_from\": \"silver\", \"updated_at\": \"2025-11-20T16:45:00Z\"}]",
                "\"employee_verification\": {\"employee_id\": \"EMP-1045\", \"name\": \"Megan Young\", \"role\": \"Store Manager\", \"store_id\": \"STORE-005\", \"authorization_level\": \"manager\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_08",
        "instruction": "Process a new customer registration for Alice Smith with phone number +1-555-777-7897, email a.smith@example.com, address 987 Sycamore Street, Riverside, IL, 62704, birthdate 1994-10-20. Set up the account at bronze level and confirm the registration.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Alice Smith"
                },
            },
            {
                "name": "FindCustomers",
                "arguments": {
                    "email": "a.smith@example.com"
                },
            },
            {
                "name": "FindCustomers",
                "arguments": {
                    "phone_number": "+1-555-777-7897"
                },
            },
            {
                "name": "CreateCustomer",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "name": "Alice Smith",
                    "phone_number": "+1-555-777-7897",
                    "email": "a.smith@example.com",
                    "address": "987 Sycamore Street, Riverside, IL, 62704",
                    "birthdate": "1994-10-20",
                    "membership_level": "bronze"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "role": "Store Manager"
                }
            }
        ],
        "outputs": [
                "{\n  \"duplicate_check\": {\"existing_customers_found\": 0, \"duplicate_prevention\": \"successful\"}\n}",
                "{\n  \"customer_created\": {\"customer_id\": \"CUST-5013\", \"name\": \"Alice Smith\", \"membership_level\": \"bronze\"}\n}",
                "{\n  \"employee_verification\": {\"role\": \"Store Manager\", \"authorization\": \"confirmed\"}\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "manager_09",
        "instruction": "As the manager of STORE-002, after a busy day where you sold 3 'ELEC-GAMLP15', 3 'CLTH-WINJKT01', and 17 'CLTH-SLFJEAN34', adjust the inventory accordingly and then review low stock items.",
        "actions": [
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "ELEC-GAMLP15",
                    "relative_quantity": -3
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "CLTH-WINJKT01",
                    "relative_quantity": -3
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "CLTH-SLFJEAN34",
                    "relative_quantity": -17
                },
            },
            {
                "name": "CheckLowStockItems",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-002"
                }
            }
        ],
        "outputs": [
                "{\n  \"stock_updated\": {\"ELEC-GAMLP15\": -3, \"CLTH-WINJKT01\": -3, \"CLTH-SLFJEAN34\": -17}\n}",
                "{\n  \"low_stock_check\": {\"store_id\": \"STORE-002\", \"items_checked\": 3}\n}",
                "{\n  \"inventory_summary\": {\"store_id\": \"STORE-002\", \"total_items\": 15, \"status\": \"updated\"}\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "inventory_manager_03",
        "instruction": "On 2025-09-15, at STORE-002, department manager EMP-1008 performs a product replacement for the ProSlice chef knife. The manager finds the old SKU KITCH-CHEFKNF8, checks current inventory levels, confirms supplier information, creates the new product KITCH-CHEFKNF9, and removes the old product.",
        "actions": [
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "CreateProduct",
                "arguments": {
                    "sku": "KITCH-CHEFKNF9",
                    "name": "ProSlice 9\" Chef Knife",
                    "category": "Home & Kitchen",
                    "price": 39.95,
                    "description": "High-carbon stainless steel knife with ergonomic handle.",
                    "supplier_id": "SUP-1002",
                    "weight_kg": 0.24,
                    "dimensions_cm": "38x8x3",
                    "brand": "ProSlice",
                    "cost": 18.75,
                    "barcode": "0123456789018",
                    "tax_rate": 0.0825
                },
            },
            {
                "name": "RemoveProduct",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                }
            }
        ],
        "outputs": [
                "\"old_product\": {\"sku\": \"KITCH-CHEFKNF8\", \"name\": \"ProSlice 8\" Chef Knife\", \"status\": \"active\", \"supplier_id\": \"SUP-1002\"}",
                "\"inventory_analysis\": [{\"store_id\": \"STORE-002\", \"sku\": \"KITCH-CHEFKNF8\", \"quantity\": 35}]",
                "\"supplier_verification\": {\"sku\": \"KITCH-CHEFKNF8\", \"supplier_id\": \"SUP-1002\", \"status\": \"verified\"}",
                "\"new_product\": {\"success\": \"complete\", \"sku\": \"KITCH-CHEFKNF9\", \"name\": \"ProSlice 9\\\" Chef Knife\"}",
                "\"old_product_removed\": {\"success\": \"Removed product: KITCH-CHEFKNF8\"}",
                "\"replacement_complete\": {\"replacement_date\": \"2025-09-15\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "supplier_01",
        "instruction": "On 2025-09-01, at STORE-002, supplier SUP-1001 executes a promotion replacement campaign. The supplier cancels the existing promotion PROMO-001, establishes a new summer TV sale promotion with 20% discount for SKU ELEC-4KTV55 starting from 2025-09-01, ending on 2025-12-31, with a usage limit of 50, description 'Summer TV sale promotion', validates the promotion creation, and checks product discountability status.",
        "actions": [
            {
                "name": "FindPromotions",
                "arguments": {
                    "promotion_id": "PROMO-001"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "CancelPromotion",
                "arguments": {
                    "promotion_id": "PROMO-001"
                },
            },
            {
                "name": "CreatePromotion",
                "arguments": {
                    "name": "Summer TV Sale",
                    "type": "percentage",
                    "discount_value": 20,
                    "description": "Summer TV sale promotion",
                    "applicable_skus": [
                        "ELEC-4KTV55"
                    ],
                    "start_date": "2025-09-01",
                    "end_date": "2025-12-31",
                    "status": "active",
                    "usage_limit": 50
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                }
            }
        ],
        "outputs": [
                "\"existing_promotion\": {\"promotion_id\": \"PROMO-001\", \"name\": \"Summer Electronics Sale\", \"status\": \"canceled\"}",
                "\"product_details\": {\"sku\": \"ELEC-4KTV55\", \"name\": \"4K Smart TV 55\"\", \"is_discountable\": true}",
                "\"promotion_canceled\": {\"success\": \"complete\"}",
                "\"new_promotion\": {\"success\": \"complete\"}",
                "\"updated_product\": {\"sku\": \"ELEC-4KTV55\", \"is_discountable\": true, \"discount_rate\": 0.2}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "inventory_manager_01",
        "instruction": "You are responsible for inventory management at STORE-002. Complete a thorough inventory audit for electronics items, evaluate current stock levels, identify low stock items, review supplier information, assess reorder needs, and restock the ELEC-GAMLP15 item from 3 to 8 units while recording the restocking process.",
        "actions": [
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "category": "Electronics"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "ELEC-GAMLP15"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "AUDIO-NCEBUDS01"
                },
            },
            {
                "name": "CheckLowStockItems",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "GetProfitMargins",
                "arguments": {
                    "sku_list": "[\"ELEC-GAMLP15\", \"AUDIO-NCEBUDS01\"]",
                    "ignore_discounts": true
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "ELEC-GAMLP15"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "AUDIO-NCEBUDS01"
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "ELEC-GAMLP15",
                    "quantity": 8
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "ELEC-GAMLP15"
                }
            }
        ],
        "outputs": [
                "\"inventory_audit\": {\"total_electronics_items\": 2, \"low_stock_items\": 1, \"reorder_needed\": true}",
                "\"electronics_products\": [{\"sku\": \"ELEC-GAMLP15\", \"name\": \"GigaPlay 15\\\" Gaming Laptop\", \"price\": 1499.0, \"category\": \"Electronics\"}, {\"sku\": \"AUDIO-NCEBUDS01\", \"name\": \"QuietTone Wireless Earbuds\", \"price\": 149.99, \"category\": \"Electronics\"}]",
                "\"low_stock_analysis\": [{\"sku\": \"ELEC-GAMLP15\", \"current_stock\": 3, \"reorder_level\": 3, \"status\": \"low_stock\"}]",
                "\"profit_margin_analysis\": [{\"sku\": \"ELEC-GAMLP15\", \"profit_margin\": 0.2728, \"priority\": \"high\"}, {\"sku\": \"AUDIO-NCEBUDS01\", \"profit_margin\": 0.45, \"priority\": \"medium\"}]",
                "\"stock_verification\": [{\"sku\": \"ELEC-GAMLP15\", \"before_quantity\": 3, \"after_quantity\": 8, \"restocked\": true}]",
                "\"restocking_documentation\": {\"sku\": \"ELEC-GAMLP15\", \"quantity_added\": 5, \"total_cost\": 5450.0, \"restock_date\": \"2025-01-01T09:10:00Z\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_02",
        "instruction": "On 2025-08-20, at STORE-001, customer service representative EMP-1002 registers a new customer, Bob Smith, with phone number +1-555-777-7896, email b.smith@example.com, address 987 Sycamore Street, Springfield, IL, 62704, and birthdate 1992-08-20. The representative verifies employee authorization, checks for existing customer records to prevent duplicates, and creates the customer account with 50 loyalty points at bronze membership level.",
        "actions": [
            {
                "name": "FindEmployees",
                "arguments": {
                    "employee_id": "EMP-1002"
                },
            },
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Bob Smith"
                },
            },
            {
                "name": "FindCustomers",
                "arguments": {
                    "email": "b.smith@example.com"
                },
            },
            {
                "name": "FindCustomers",
                "arguments": {
                    "phone_number": "+1-555-777-7896"
                },
            },
            {
                "name": "CreateCustomer",
                "arguments": {
                    "name": "Bob Smith",
                    "phone_number": "+1-555-777-7896",
                    "email": "b.smith@example.com",
                    "address": "987 Sycamore Street, Springfield, IL, 62704",
                    "birthdate": "1992-08-20",
                    "membership_level": "bronze",
                    "loyalty_points": 50
                }
            }
        ],
        "outputs": [
                "\"employee_verification\": {\"employee_id\": \"EMP-1002\", \"name\": \"Sarah Anderson\", \"role\": \"Cashier\", \"authorization_level\": \"customer_service\"}",
                "\"duplicate_check\": {\"existing_customers_found\": 0, \"duplicate_prevention\": \"successful\"}",
                "\"customer_created\": {\"customer_id\": \"CUST-5013\", \"name\": \"Bob Smith\", \"loyalty_points\": 50, \"membership_level\": \"bronze\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "manager_01",
        "instruction": "As a store manager at STORE-002, lead a comprehensive electronics inventory optimization campaign. First, evaluate current electronics inventory levels across all categories, identify low stock items, assess profit margins for high-value electronics, and then execute a strategic restocking plan. Specifically, restock the ELEC-GAMLP15 gaming laptop from 3 to 15 units, update the AUDIO-NCEBUDS01 wireless earbuds to 12 units, and confirm the inventory updates.",
        "actions": [
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "category": "Electronics"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "ELEC-GAMLP15"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "AUDIO-NCEBUDS01"
                },
            },
            {
                "name": "CheckLowStockItems",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "GetProfitMargins",
                "arguments": {
                    "sku_list": "[\"ELEC-GAMLP15\", \"AUDIO-NCEBUDS01\"]",
                    "ignore_discounts": true
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "ELEC-GAMLP15"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "AUDIO-NCEBUDS01"
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "ELEC-GAMLP15",
                    "quantity": 15
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "AUDIO-NCEBUDS01",
                    "quantity": 12
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "ELEC-GAMLP15"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "AUDIO-NCEBUDS01"
                }
            }
        ],
        "outputs": [
                "\"electronics_inventory_analysis\": {\"total_electronics_items\": 2, \"low_stock_items\": 1, \"optimization_needed\": true}",
                "\"electronics_products\": [{\"sku\": \"ELEC-GAMLP15\", \"name\": \"GigaPlay 15\\\" Gaming Laptop\", \"price\": 1499.0, \"category\": \"Electronics\"}, {\"sku\": \"AUDIO-NCEBUDS01\", \"name\": \"QuietTone Wireless Earbuds\", \"price\": 149.99, \"category\": \"Electronics\"}]",
                "\"low_stock_analysis\": [{\"sku\": \"ELEC-GAMLP15\", \"current_stock\": 3, \"reorder_level\": 5, \"status\": \"low_stock\"}]",
                "\"profit_margin_analysis\": [{\"sku\": \"ELEC-GAMLP15\", \"profit_margin\": 0.35, \"priority\": \"high\"}, {\"sku\": \"AUDIO-NCEBUDS01\", \"profit_margin\": 0.28, \"priority\": \"medium\"}]",
                "\"stock_verification\": [{\"sku\": \"ELEC-GAMLP15\", \"before_quantity\": 3, \"after_quantity\": 15, \"restocked\": true}, {\"sku\": \"AUDIO-NCEBUDS01\", \"before_quantity\": 8, \"after_quantity\": 12, \"restocked\": true}]",
                "\"inventory_optimization\": {\"campaign_timestamp\": \"2025-01-01T09:10:00Z\", \"optimization_status\": \"complete\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "manager_06",
        "instruction": "As the strategic store manager at STORE-001, you are overseeing a pre-event inventory preparation initiative for an upcoming major sporting event. Start by assessing the current TV inventory levels, evaluating profit margins for electronics, and then executing a restocking strategy. Specifically, raise the stock of ELEC-4KTV55 4K Smart TV from 8 to 20 units and confirm the inventory updates.",
        "actions": [
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "TV"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-001",
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "GetProfitMargins",
                "arguments": {
                    "sku_list": "[\"ELEC-4KTV55\"]",
                    "ignore_discounts": true
                },
            },
            {
                "name": "CheckLowStockItems",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-001",
                    "sku": "ELEC-4KTV55",
                    "quantity": 20
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-001",
                    "sku": "ELEC-4KTV55"
                }
            }
        ],
        "outputs": [
                "\"pre_event_analysis\": {\"sporting_event_preparation\": true, \"inventory_optimization_needed\": true}",
                "\"tv_product\": {\"sku\": \"ELEC-4KTV55\", \"name\": \"4K Smart TV 55\"\", \"price\": 699.99, \"category\": \"Electronics\"}",
                "\"initial_inventory\": [{\"id\": \"INV-0001\", \"sku\": \"ELEC-4KTV55\", \"store_id\": \"STORE-001\", \"quantity\": 8, \"status\": \"in_stock\"}]",
                "\"profit_margin_analysis\": [{\"sku\": \"ELEC-4KTV55\", \"profit_margin\": 0.25, \"priority\": \"high\"}]",
                "\"inventory_updated\": {\"success\": true, \"tv_new_quantity\": 20}",
                "\"pre_event_documentation\": {\"campaign_timestamp\": \"2025-01-01T09:10:00Z\", \"preparation_status\": \"complete\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_03",
        "instruction": "On 2025-09-05, manager EMP-1045 performs a review and update of the customer account for CUST-5004. The manager checks customer details, reviews transaction history, evaluates loyalty program status, confirms employee authorization, and updates the customer's marketing preferences to opt-in status.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "customer_id": "CUST-5004"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "customer_id": "CUST-5004"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "customer_id": "CUST-5004",
                    "status": "pending"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "customer_id": "CUST-5004",
                    "status": "returned"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "employee_id": "EMP-1045"
                },
            },
            {
                "name": "UpdateCustomer",
                "arguments": {
                    "timestamp": "2025-09-05T14:30:00Z",
                    "customer_id": "CUST-5004",
                    "opt_in_marketing": true
                }
            }
        ],
        "outputs": [
                "\"customer_verification\": {\"customer_id\": \"CUST-5004\", \"name\": \"Liam Anderson\", \"membership_level\": \"platinum\", \"loyalty_points\": 1520, \"total_transactions\": 1}",
                "\"transaction_analysis\": [{\"transaction_id\": \"TXN-0004\", \"total_amount\": 205.48, \"status\": \"completed\", \"store_id\": \"STORE-004\", \"employee_id\": \"EMP-1032\"}]",
                "\"pending_items_check\": {\"pending_transactions\": 0, \"pending_returns\": 0, \"account_clear\": true}",
                "\"authorization_verification\": {\"employee_id\": \"EMP-1045\", \"name\": \"Megan Young\", \"role\": \"Store Manager\", \"authorization_level\": \"manager\"}",
                "\"customer_updated\": {\"customer_id\": \"CUST-5004\", \"opt_in_marketing\": true, \"updated_at\": \"2025-09-05T14:30:00Z\"}",
                "\"review_complete\": {\"customer_id\": \"CUST-5004\", \"review_timestamp\": \"2025-09-05T14:30:00Z\", \"reviewed_by\": \"EMP-1045\", \"status\": \"reviewed\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_01",
        "instruction": "As a customer named Olivia Romano, you wish to buy several products. The items you are looking for are: 2 gaming console, 2 almond butter, 2 AAA Batteries, 1 office chair, 1 thermostat. Some items may not be in stock; if that occurs, proceed to purchase all available items. You might need to visit various stores to gather all of the items. You are set to pay the exact amount using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Olivia Romano"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "almond butter"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AAA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "office chair"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "thermostat"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-ALMBTR500"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "OFFC-ERGCHR01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SMRT-THERM02"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SMRT-THERM02",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5007",
                    "payment_method": "credit_card",
                    "payment_amount": 224.07,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5007",
                    "payment_method": "credit_card",
                    "payment_amount": 25.98,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5007",
                    "payment_method": "credit_card",
                    "payment_amount": 174.39,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SMRT-THERM02",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 224.07,\n  \"tax_amount\": 17.08,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 23.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5007\",\n  \"line_items\": [\n    {\n      \"sku\": \"OFFC-ERGCHR01\",\n      \"quantity\": 1,\n      \"unit_price\": 229.99,\n      \"discount\": 23.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 25.98,\n  \"tax_amount\": 0.0,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5007\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-ALMBTR500\",\n      \"quantity\": 2,\n      \"unit_price\": 12.99,\n      \"discount\": 0.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 174.39,\n  \"tax_amount\": 13.29,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 17.9,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5007\",\n  \"line_items\": [\n    {\n      \"sku\": \"SMRT-THERM02\",\n      \"quantity\": 1,\n      \"unit_price\": 179.0,\n      \"discount\": 17.9\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "inventory_manager_00",
        "instruction": "In your role as an inventory manager for the store chain, assess returned transactions and eliminate defective inventory.",
        "actions": [
            {
                "name": "FindTransaction",
                "arguments": {
                    "status": "returned"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-BIKHLM01"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "SPORT-BIKHLM01"
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-004",
                    "sku": "SPORT-BIKHLM01",
                    "quantity": 3
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-BIKHLM01"
                }
            }
        ],
        "outputs": [
                "{\n  \"returned_items\": [{\"sku\": \"SPORT-BIKHLM01\", \"return_count\": 1, \"return_reason\": \"defective\"}]}",
                "{\n  \"defective_inventory_removed\": {\"store_id\": \"STORE-004\", \"sku\": \"SPORT-BIKHLM01\", \"quantity\": 3, \"status\": \"defective_unit_removed\"}}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "employee_02",
        "instruction": "As an employee named Sarah Anderson, you are moving soon and will be closer to STORE-002 compared to your current position at STORE-001. You\u2019ve learned that STORE-002 requires 2 cashiers; check their current cashier count, analyze the staffing situation, review your performance metrics, and evaluate transfer possibilities. If STORE-002 has fewer than 2 cashiers, proceed to update your role to 'Sales Associate' to facilitate your transfer. If not, resign and delete your record from the employee database.",
        "actions": [
            {
                "name": "FindEmployees",
                "arguments": {
                    "name": "Sarah Anderson"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "role": "Cashier",
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "role": "Sales Associate",
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "employee_id": "EMP-1002"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "employee_id": "EMP-1002",
                    "status": "completed"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "employee_id": "EMP-1002",
                    "status": "returned"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "employee_id": "EMP-1002",
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "EMP-1002",
                    "role": "Sales Associate",
                    "timestamp": "2025-01-01T09:10:00Z"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "employee_id": "EMP-1002"
                }
            }
        ],
        "outputs": [
                "{\n  \"current_employee\": {\"employee_id\": \"EMP-1002\", \"name\": \"Sarah Anderson\", \"role\": \"Cashier\", \"store_id\": \"STORE-001\"}}",
                "{\n  \"target_store_staffing\": {\"store_id\": \"STORE-002\", \"cashiers\": 1, \"sales_associates\": 2, \"total_employees\": 3}}",
                "{\n  \"transaction_history\": {\"completed_transactions\": 45, \"returned_transactions\": 2, \"total_transactions\": 47}}",
                "{\n  \"performance_metrics\": {\"transactions_processed\": 45, \"return_rate\": 0.043, \"store_performance\": \"consistent\"}}",
                "{\n  \"performance_analysis\": {\"strengths\": [\"consistent_transaction_processing\"], \"areas_for_improvement\": [\"reduce_returns\"], \"transfer_readiness\": \"good\"}}",
                "{\n  \"transfer_analysis\": {\"current_cashiers_at_target\": 1, \"needed_cashiers\": 2, \"transfer_recommended\": true, \"performance_justification\": \"strong_metrics\"}}",
                "{\n  \"role_update\": {\"employee_id\": \"EMP-1002\", \"name\": \"Sarah Anderson\", \"role\": \"Sales Associate\", \"performance_reviewed\": true}}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "employee_03",
        "instruction": "You are an employee named Amanda Romano. With your upcoming move, you will be nearer to STORE-004 than your current location at STORE-002. You\u2019ve heard that STORE-004 requires 1 sales associate; verify how many sales associates they currently employ, assess staffing needs, review your performance, and determine the feasibility of a transfer. If STORE-004 has less than 1 sales associate, transition yourself to STORE-004. If not, resign and remove your record from the employee database.",
        "actions": [
            {
                "name": "FindEmployees",
                "arguments": {
                    "name": "Amanda Romano"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "store_id": "STORE-004"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "role": "Sales Associate",
                    "store_id": "STORE-004"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "role": "Cashier",
                    "store_id": "STORE-004"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "employee_id": "EMP-1009"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "employee_id": "EMP-1009"
                },
            },
            {
                "name": "RemoveEmployee",
                "arguments": {
                    "employee_id": "EMP-1009"
                }
            }
        ],
        "outputs": [
                "{\n  \"current_employee\": {\"employee_id\": \"EMP-1009\", \"name\": \"Amanda Romano\", \"role\": \"Sales Associate\", \"store_id\": \"STORE-002\"}}",
                "{\n  \"target_store_staffing\": {\"store_id\": \"STORE-004\", \"sales_associates\": 1, \"cashiers\": 0, \"total_employees\": 1}}",
                "{\n  \"performance_review\": {\"transactions_processed\": 1, \"customer_satisfaction\": 4.1, \"attendance_rate\": 0.92}}",
                "{\n  \"transfer_analysis\": {\"current_sales_associates_at_target\": 1, \"needed_sales_associates\": 1, \"transfer_not_needed\": true}}",
                "{\n  \"termination\": {\"employee_id\": \"EMP-1009\", \"name\": \"Amanda Romano\", \"status\": \"removed\", \"reason\": \"No transfer opportunity available\"}}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "manager_08",
        "instruction": "In your role as the manager of STORE-002, after a busy day, you have sold 3 'ELEC-GAMLP15', 3 'CLTH-WINJKT01', and 17 'CLTH-SLFJEAN34'. Adjust the stock accordingly and subsequently check for low stock items. If any items are low or critical, restock them to their reorder levels: ELEC-GAMLP15 to 3 units, CLTH-WINJKT01 to 4 units, and CLTH-SLFJEAN34 to 15 units.",
        "actions": [
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "ELEC-GAMLP15",
                    "relative_quantity": -3
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "CLTH-WINJKT01",
                    "relative_quantity": -3
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "CLTH-SLFJEAN34",
                    "relative_quantity": -17
                },
            },
            {
                "name": "CheckLowStockItems",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "ELEC-GAMLP15",
                    "quantity": 3
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "CLTH-WINJKT01",
                    "quantity": 4
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "CLTH-SLFJEAN34",
                    "quantity": 15
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "manager_07",
        "instruction": "As the manager of STORE-001, since Sarah Anderson has resigned, you need to remove her from the database. Given the necessity for a cashier to handle transactions, you will need to find a temporary replacement. A Sales Associate can fill in, so determine if any are available. Additionally, ensure you update the replacement employee's role and follow proper handover protocols.",
        "actions": [
            {
                "name": "FindEmployees",
                "arguments": {
                    "name": "Sarah Anderson",
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "role": "Sales Associate",
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "role": "Cashier",
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "employee_id": "EMP-1002"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "store_id": "STORE-001",
                    "status": "pending"
                },
            },
            {
                "name": "RemoveEmployee",
                "arguments": {
                    "employee_id": "EMP-1002"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "employee_id": "EMP-1003",
                    "role": "Cashier"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "employee_id": "EMP-1003"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "employee_id": "EMP-1003"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "store_id": "STORE-001",
                    "status": "completed"
                }
            }
        ],
        "outputs": [
                "{\n  \"departed_employee\": {\"employee_id\": \"EMP-1002\", \"name\": \"Sarah Anderson\", \"role\": \"Cashier\", \"status\": \"removed\"}}",
                "{\n  \"replacement_employee\": {\"employee_id\": \"EMP-1003\", \"name\": \"Michael Rodriguez\", \"role\": \"Cashier\", \"previous_role\": \"Sales Associate\"}}",
                "{\n  \"pending_transactions\": [{\"transaction_id\": \"TNX-0013\", \"status\": \"completed\"}]}",
                "{\n  \"handover_procedures\": {\"pending_transactions_checked\": true, \"replacement_employee_ready\": true}}",
                "{\n  \"role_update\": {\"action\": \"Updated employee role\", \"new_cashier\": \"EMP-1003\", \"timestamp\": \"2025-01-01T09:10:00Z\"}}",
                "{\n  \"handover_complete\": {\"status\": \"Sarah Anderson removed, Michael Rodriguez promoted to Cashier, pending transactions reviewed\"}}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "inventory_manager_02",
        "instruction": "As the inventory manager at STORE-002, review the current stock of clothing items and restock the CLTH-WINJKT01 item from 6 to 15 units.",
        "actions": [
            {
                "name": "FindProducts",
                "arguments": {
                    "category": "Apparel"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "CLTH-WINJKT01"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-002",
                    "sku": "CLTH-WINJKT01",
                    "quantity": 15
                }
            }
        ],
        "outputs": [
                "\"apparel_products\": [{\"sku\": \"CLTH-WINJKT01\", \"name\": \"ArcticShield Men's Parka - Large\", \"category\": \"Apparel\"}, {\"sku\": \"CLTH-SLFJEAN34\", \"name\": \"Men's Slim Fit Jeans - 34W 32L\", \"category\": \"Apparel\"}]",
                "\"store_inventory\": [{\"sku\": \"CLTH-WINJKT01\", \"quantity\": 15}, {\"sku\": \"CLTH-SLFJEAN34\", \"quantity\": 30}]",
                "\"stock_updated\": {\"sku\": \"CLTH-WINJKT01\", \"new_quantity\": 15}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "manager_02",
        "instruction": "On 2025-08-15, at STORE-001, cashier EMP-1002 performs an inventory damage assessment for SKU ELEC-4KTV55. The cashier checks current inventory status, verifies product details and pricing, adjusts the stock quantity to account for 2 damaged units, validates the update against safety stock levels, assesses whether the item needs reordering based on the new status, examines profit margins for the damaged units, and documents the comprehensive damage assessment process with timestamp '2025-08-15T11:30:00Z' using phone number +1-555-000-0000, email damage.log@store.com, address Internal Log, and birthdate 2025-08-15.",
        "actions": [
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-001",
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "GetProfitMargins",
                "arguments": {
                    "sku_list": "[\"ELEC-4KTV55\"]",
                    "ignore_discounts": true
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-001",
                    "sku": "ELEC-4KTV55",
                    "relative_quantity": -2
                },
            },
            {
                "name": "CheckLowStockItems",
                "arguments": {
                    "store_id": "STORE-001",
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-001",
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "employee_id": "EMP-1002"
                },
            },
            {
                "name": "CreateCustomer",
                "arguments": {
                    "timestamp": "2025-08-15T11:30:00Z",
                    "name": "Damage Assessment Log",
                    "phone_number": "+1-555-000-0000",
                    "email": "damage.log@store.com",
                    "address": "Internal Log",
                    "birthdate": "2025-08-15"
                }
            }
        ],
        "outputs": [
                "\"initial_inventory\": {\"id\": \"INV-0001\", \"sku\": \"ELEC-4KTV55\", \"store_id\": \"STORE-001\", \"quantity\": 8, \"status\": \"in_stock\"}",
                "\"product_details\": {\"sku\": \"ELEC-4KTV55\", \"name\": \"4K Smart TV 55\"\", \"price\": 699.99, \"category\": \"Electronics\", \"supplier_id\": \"SUP-1001\"}",
                "\"profit_analysis\": [{\"sku\": \"ELEC-4KTV55\", \"profit\": 219.99, \"profit_margin\": 0.314, \"profit_margin_percent\": 45.83}]",
                "\"stock_updated\": {\"success\": true}",
                "\"low_stock_check\": []",
                "\"final_inventory\": {\"id\": \"INV-0001\", \"sku\": \"ELEC-4KTV55\", \"store_id\": \"STORE-001\", \"quantity\": 6, \"status\": \"in_stock\"}",
                "\"manager_info\": {\"employee_id\": \"EMP-1002\", \"name\": \"Sarah Anderson\", \"role\": \"Cashier\"}",
                "\"damage_assessment_log\": {\"customer_id\": \"CUST-5013\", \"name\": \"Damage Assessment Log\", \"phone_number\": \"+1-555-000-0000\", \"email\": \"damage.log@store.com\", \"address\": \"Internal Log\", \"birthdate\": \"2025-08-15\", \"timestamp\": \"2025-08-15T11:30:00Z\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_04",
        "instruction": "On 2025-09-10, at STORE-001, cashier EMP-1002 updates customer information for Sophia Singh. The cashier retrieves the customer record, confirms current contact details and membership status, changes the phone number to +1-555-0789-099, validates the update, and documents the entire information update procedure with timestamp '2025-09-10T11:20:00Z'.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Sophia Singh"
                },
            },
            {
                "name": "FindTransaction",
                "arguments": {
                    "customer_id": "CUST-5003"
                },
            },
            {
                "name": "UpdateCustomer",
                "arguments": {
                    "timestamp": "2025-09-10T11:20:00Z",
                    "customer_id": "CUST-5003",
                    "phone_number": "+1-555-0789-099"
                },
            },
            {
                "name": "FindCustomers",
                "arguments": {
                    "customer_id": "CUST-5003"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "employee_id": "EMP-1002"
                }
            }
        ],
        "outputs": [
                "\"customer_found\": {\"customer_id\": \"CUST-5003\", \"name\": \"Sophia Singh\", \"phone_number\": \"+1-555-0789-012\", \"loyalty_points\": 460}",
                "\"transaction_history\": [{\"transaction_id\": \"TNX-0003\", \"total_amount\": 37.58}]",
                "\"customer_updated\": {\"customer_id\": \"CUST-5003\", \"name\": \"Sophia Singh\", \"phone_number\": \"+1-555-0789-099\"}",
                "\"update_verified\": {\"customer_id\": \"CUST-5003\", \"phone_number\": \"+1-555-0789-099\", \"updated_at\": \"2025-09-10T11:20:00Z\"}",
                "\"employee_info\": {\"employee_id\": \"EMP-1002\", \"name\": \"Sarah Anderson\", \"role\": \"Cashier\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "employee_01",
        "instruction": "On 2025-08-30, at STORE-001, customer service representative EMP-1004 oversees an employee promotion for Sarah Anderson. The representative finds the employee record, checks current role, updates the role to Floor Supervisor, validates the promotion, and documents the complete promotion procedure with timestamp '2025-08-30T09:30:00Z'.",
        "actions": [
            {
                "name": "FindEmployees",
                "arguments": {
                    "name": "Sarah Anderson"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "store_id": "STORE-001",
                    "role": "Cashier"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "timestamp": "2025-08-30T09:30:00Z",
                    "employee_id": "EMP-1002",
                    "role": "Floor Supervisor"
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "employee_id": "EMP-1002"
                }
            }
        ],
        "outputs": [
                "\"employee_found\": {\"employee_id\": \"EMP-1002\", \"name\": \"Sarah Anderson\", \"role\": \"Cashier\", \"store_id\": \"STORE-001\"}",
                "\"current_cashiers\": [{\"employee_id\": \"EMP-1002\", \"name\": \"Sarah Anderson\"}]",
                "\"promotion_processed\": {\"employee_id\": \"EMP-1002\", \"name\": \"Sarah Anderson\", \"role\": \"Floor Supervisor\"}",
                "\"promotion_verified\": {\"employee_id\": \"EMP-1002\", \"role\": \"Floor Supervisor\", \"updated_at\": \"2025-08-30T09:30:00Z\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_05",
        "instruction": "As a customer with id 'CUST-5004', you are looking to purchase new electronics for your home theater setup. You want a new 4K TV, a bluetooth speaker, and a gaming console. The TV is essential; however, the speaker and gaming console are optional. You must check current promotions, ensure product availability across stores, compare prices, verify your loyalty points balance, find suitable checkout employees, and make informed purchasing decisions. If no TVs are available, do not place any orders. Otherwise, proceed with the order including any optional items. You might need to visit various stores to acquire all the items. Payment will be made using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "customer_id": "CUST-5004"
                },
            },
            {
                "name": "FindPromotions",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "TV"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "bluetooth speaker"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-BTSPKR02"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "AUDIO-BTSPKR02"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": "[{\"sku\" : \"ELEC-4KTV55\", \"quantity\" : 1}]"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": "[{\"sku\" : \"AUDIO-BTSPKR02\", \"quantity\" : 1}]"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-005"
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5004",
                    "payment_method": "credit_card",
                    "payment_amount": 681.96,
                    "status": "completed",
                    "line_items": "[{\"sku\" : \"ELEC-4KTV55\", \"quantity\" : 1}]"
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "store_id": "STORE-005",
                    "employee_id": "EMP-1050",
                    "customer_id": "CUST-5004",
                    "payment_method": "credit_card",
                    "payment_amount": 123.83,
                    "status": "completed",
                    "line_items": "[{\"sku\" : \"AUDIO-BTSPKR02\", \"quantity\" : 1}]"
                }
            }
        ],
        "outputs": [
                "\"customer_info\": {\"customer_id\": \"CUST-5004\", \"name\": \"Liam Anderson\", \"loyalty_points\": 750, \"membership_level\": \"platinum\"}",
                "\"active_promotions\": [{\"promotion_id\": \"PROMO-001\", \"name\": \"Spring Electronics Sale\", \"discount_value\": 10}]",
                "\"tv_product\": {\"sku\": \"ELEC-4KTV55\", \"name\": \"4K Smart TV 55\"\", \"price\": 699.99, \"category\": \"Electronics\"}",
                "\"speaker_product\": {\"sku\": \"AUDIO-BTSPKR02\", \"name\": \"Bluetooth Speaker\", \"price\": 129.99, \"category\": \"Electronics\"}",
                "\"tv_availability\": [{\"id\": \"INV-0001\", \"sku\": \"ELEC-4KTV55\", \"store_id\": \"STORE-001\", \"quantity\": 8}]",
                "\"speaker_availability\": [{\"id\": \"INV-0015\", \"sku\": \"AUDIO-BTSPKR02\", \"store_id\": \"STORE-005\", \"quantity\": 15}]",
                "\"tv_price_details\": {\"sku\": \"ELEC-4KTV55\", \"unit_price\": 699.99, \"discount_rate\": 0.1, \"tax_rate\": 0.0825}",
                "\"speaker_price_details\": {\"sku\": \"AUDIO-BTSPKR02\", \"unit_price\": 129.99, \"discount_rate\": 0.12, \"tax_rate\": 0.0825}",
                "\"checkout_employee_store1\": {\"employee_id\": \"EMP-1002\", \"name\": \"Sarah Anderson\", \"role\": \"Cashier\"}",
                "\"checkout_employee_store5\": {\"employee_id\": \"EMP-1050\", \"name\": \"David Wilson\", \"role\": \"Floor Supervisor\"}",
                "\"tv_transaction_preview\": {\"total_amount\": 681.96, \"tax_amount\": 51.97, \"discount_total\": 70.0}",
                "\"speaker_transaction_preview\": {\"total_amount\": 123.83, \"tax_amount\": 9.44, \"discount_total\": 15.6}",
                "\"tv_purchase\": {\"transaction_id\": \"TNX-0013\", \"store_id\": \"STORE-001\", \"total_amount\": 681.96, \"status\": \"completed\"}",
                "\"speaker_purchase\": {\"transaction_id\": \"TNX-0014\", \"store_id\": \"STORE-005\", \"total_amount\": 123.83, \"status\": \"completed\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_06",
        "instruction": "As a customer with id 'CUST-5006', you are in search of everyday items for a wellness and productivity setup. You require a new desk lamp, a yoga mat, and some sparkling water. You need to review your membership benefits, compare prices at different stores, confirm product quality and availability, check for applicable discounts, and optimize your purchase for the best value. There is a possibility that you may have to visit several stores to gather all the items; however, if all items can be found at one store, then centralize the order to that store. Payment will be made in cash with a single $100 bill.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "customer_id": "CUST-5006"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "yoga mat"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "desk lamp"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-YOGMAT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-DESKLMP01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "SPORT-YOGMAT01"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "HOME-DESKLMP01"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": "[{\"sku\" : \"SPORT-YOGMAT01\", \"quantity\" : 1},{\"sku\" : \"HOME-DESKLMP01\", \"quantity\" : 1},{\"sku\" : \"GROC-SPRWAT6P\", \"quantity\" : 1}]"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5006",
                    "payment_method": "cash",
                    "payment_amount": 100.0,
                    "status": "completed",
                    "line_items": "[{\"sku\" : \"SPORT-YOGMAT01\", \"quantity\" : 1},{\"sku\" : \"HOME-DESKLMP01\", \"quantity\" : 1},{\"sku\" : \"GROC-SPRWAT6P\", \"quantity\" : 1}]"
                }
            }
        ],
        "outputs": [
                "\"customer_info\": {\"customer_id\": \"CUST-5006\", \"name\": \"William Zhang\", \"loyalty_points\": 980, \"membership_level\": \"silver\"}",
                "\"yoga_product\": {\"sku\": \"SPORT-YOGMAT01\", \"name\": \"Yoga Mat\", \"price\": 29.99, \"category\": \"Sports\"}",
                "\"lamp_product\": {\"sku\": \"HOME-DESKLMP01\", \"name\": \"Desk Lamp\", \"price\": 34.99, \"category\": \"Home\"}",
                "\"water_product\": {\"sku\": \"GROC-SPRWAT6P\", \"name\": \"Sparkling Water 6-Pack\", \"price\": 7.99, \"category\": \"Grocery\"}",
                "\"yoga_availability\": [{\"id\": \"INV-0003\", \"sku\": \"SPORT-YOGMAT01\", \"store_id\": \"STORE-001\", \"quantity\": 12}]",
                "\"lamp_availability\": [{\"id\": \"INV-0004\", \"sku\": \"HOME-DESKLMP01\", \"store_id\": \"STORE-001\", \"quantity\": 8}]",
                "\"water_availability\": [{\"id\": \"INV-0005\", \"sku\": \"GROC-SPRWAT6P\", \"store_id\": \"STORE-001\", \"quantity\": 25}]",
                "\"yoga_price_details\": {\"sku\": \"SPORT-YOGMAT01\", \"unit_price\": 29.99, \"discount_rate\": 0.15, \"tax_rate\": 0.0825}",
                "\"lamp_price_details\": {\"sku\": \"HOME-DESKLMP01\", \"unit_price\": 34.99, \"discount_rate\": 0.08, \"tax_rate\": 0.0825}",
                "\"water_price_details\": {\"sku\": \"GROC-SPRWAT6P\", \"unit_price\": 7.99, \"discount_rate\": 0.05, \"tax_rate\": 0.0}",
                "\"transaction_preview\": {\"total_amount\": 70.03, \"tax_amount\": 4.76, \"discount_total\": 7.7}",
                "\"checkout_employee\": {\"employee_id\": \"EMP-1002\", \"name\": \"Sarah Anderson\", \"role\": \"Cashier\"}",
                "\"consolidated_purchase\": {\"transaction_id\": \"TNX-0013\", \"store_id\": \"STORE-001\", \"total_amount\": 70.03, \"change_given\": 29.97, \"status\": \"completed\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_07",
        "instruction": "As a customer with id 'CUST-5006', you aim to purchase a new smart thermostat. Payment will be made using a credit card. If possible, upgrade to a gold membership before purchasing the smart thermostat.",
        "actions": [
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "SMRT-THERM02"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SMRT-THERM02"
                },
            },
            {
                "name": "UpdateCustomer",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "customer_id": "CUST-5006",
                    "membership_level": "gold"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5006",
                    "payment_method": "credit_card",
                    "payment_amount": 174.39,
                    "status": "completed",
                    "line_items": "[{\"sku\" : \"SMRT-THERM02\", \"quantity\" : 1}]"
                }
            }
        ],
        "outputs": [
                "{\n  \"smart_thermostat_product\": {\"sku\": \"SMRT-THERM02\", \"name\": \"Smart Thermostat\", \"price\": 179.0, \"category\": \"Electronics\"}\n}",
                "{\n  \"smart_thermostat_availability\": [{\"id\": \"INV-0019\", \"sku\": \"SMRT-THERM02\", \"store_id\": \"STORE-002\", \"quantity\": 15}]\n}",
                "{\n  \"customer_updated\": {\"customer_id\": \"CUST-5006\", \"membership_level\": \"gold\", \"updated_at\": \"2025-01-01T09:10:00Z\"}\n}",
                "{\n  \"checkout_employee\": {\"employee_id\": \"EMP-1011\", \"name\": \"Ethan Walker\", \"role\": \"Cashier\"}\n}",
                "{\n  \"smart_thermostat_purchase\": {\"transaction_id\": \"TNX-0013\", \"store_id\": \"STORE-002\", \"total_amount\": 174.39, \"status\": \"completed\"}\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "manager_05",
        "instruction": "As a manager at 'STORE-001', you have observed that 30 units of 'GROC-ALMBTR500' have become unfit for sale due to improper storage conditions. You need to perform an inventory audit, update the current stock, evaluate the effects on profit margins, determine if the item requires reordering, validate supplier information by reviewing the product details, and assess safety stock levels.",
        "actions": [
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-001",
                    "sku": "GROC-ALMBTR500"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "sku": "GROC-ALMBTR500"
                },
            },
            {
                "name": "GetProfitMargins",
                "arguments": {
                    "sku_list": "[\"GROC-ALMBTR500\"]",
                    "ignore_discounts": true
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-001",
                    "sku": "GROC-ALMBTR500",
                    "relative_quantity": -30
                },
            },
            {
                "name": "CheckLowStockItems",
                "arguments": {
                    "store_id": "STORE-001",
                    "sku": "GROC-ALMBTR500"
                },
            },
            {
                "name": "UpdateStockQuantity",
                "arguments": {
                    "store_id": "STORE-001",
                    "sku": "GROC-ALMBTR500",
                    "quantity": 40
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "store_id": "STORE-001",
                    "sku": "GROC-ALMBTR500"
                }
            }
        ],
        "outputs": [
                "\"initial_inventory\": {\"id\": \"INV-0007\", \"sku\": \"GROC-ALMBTR500\", \"store_id\": \"STORE-001\", \"quantity\": 60, \"status\": \"in_stock\"}",
                "\"product_details\": {\"sku\": \"GROC-ALMBTR500\", \"name\": \"Organic Almond Butter 500g\", \"supplier_id\": \"SUP-1004\", \"cost\": 5.25}",
                "\"profit_analysis\": [{\"sku\": \"GROC-ALMBTR500\", \"profit\": 2.6, \"profit_margin\": 0.331, \"profit_margin_percent\": 49.5}]",
                "\"damaged_stock_removed\": {\"success\": true}",
                "\"low_stock_check\": [{\"store_id\": \"STORE-001\", \"sku\": \"GROC-ALMBTR500\", \"status\": \"low_stock\", \"quantity\": 30, \"reorder_level\": 35}]",
                "\"stock_replenished\": {\"success\": true}",
                "\"final_inventory\": {\"id\": \"INV-0007\", \"sku\": \"GROC-ALMBTR500\", \"store_id\": \"STORE-001\", \"quantity\": 40, \"status\": \"in_stock\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "marketing_manager_03",
        "instruction": "As a marketing manager for the store chain, you have been tasked with developing a promotion that will attract basic members to encourage new signups. The suppliers have indicated their willingness to provide a 5% discount on any item from 2024-01-01 until 2024-05-31, but it will be limited to 10 participants. Identify which items are most frequently purchased by those members and then establish a promotion for that item titled 'Basic Members Upgrade Special' with the description '5 percent off for basic members to upgrade'.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "membership_level": "basic"
                },
            },
            {
                "name": "GetTopSellingItems",
                "arguments": {
                    "customer_id": "CUST-5008"
                },
            },
            {
                "name": "GetTopSellingItems",
                "arguments": {
                    "customer_id": "CUST-5012"
                },
            },
            {
                "name": "CreatePromotion",
                "arguments": {
                    "name": "Basic Members Upgrade Special",
                    "type": "percentage",
                    "discount_value": 5,
                    "description": "5 percent off for basic members to upgrade",
                    "applicable_skus": "[\"BOOK-KDSSTY01\"]",
                    "start_date": "2024-01-01",
                    "end_date": "2024-05-31",
                    "status": "active",
                    "usage_limit": 10
                }
            }
        ],
        "outputs": [
                "{\"success\": \"complete\"}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_09",
        "instruction": "As a customer named Mia Kim, you wish to purchase a coffee maker and a bath towel from STORE-001. Payment will be made using a credit card. The coffee maker has a price of $59.95, and the bath towel costs $14.50.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Mia Kim"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "coffee maker"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "towel"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOM-COFMKR12"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-BTHTWL01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": "[{\"sku\" : \"HOM-COFMKR12\", \"quantity\" : 1}, {\"sku\" : \"HOME-BTHTWL01\", \"quantity\" : 1}]"
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5011",
                    "payment_method": "credit_card",
                    "payment_amount": 70.08,
                    "status": "completed",
                    "line_items": "[{\"sku\" : \"HOM-COFMKR12\", \"quantity\" : 1}, {\"sku\" : \"HOME-BTHTWL01\", \"quantity\" : 1}]"
                }
            }
        ],
        "outputs": [
                "{\n  \"customer_info\": {\"customer_id\": \"CUST-5011\", \"name\": \"Mia Kim\", \"loyalty_points\": 560, \"membership_level\": \"silver\"}\n}",
                "{\n  \"coffee_maker_product\": {\"sku\": \"HOM-COFMKR12\", \"name\": \"Coffee Maker\", \"price\": 59.95, \"category\": \"Home\"}\n}",
                "{\n  \"towel_product\": {\"sku\": \"HOME-BTHTWL01\", \"name\": \"Bath Towel\", \"price\": 14.50, \"category\": \"Home\"}\n}",
                "{\n  \"coffee_maker_availability\": [{\"id\": \"INV-0003\", \"sku\": \"HOM-COFMKR12\", \"store_id\": \"STORE-001\", \"quantity\": 25}]\n}",
                "{\n  \"towel_availability\": [{\"id\": \"INV-0012\", \"sku\": \"HOME-BTHTWL01\", \"store_id\": \"STORE-001\", \"quantity\": 100}]\n}",
                "{\n  \"checkout_employee\": {\"employee_id\": \"EMP-1002\", \"name\": \"Sarah Anderson\", \"role\": \"Cashier\"}\n}",
                "{\n  \"purchase\": {\"transaction_id\": \"TNX-0013\", \"store_id\": \"STORE-001\", \"total_amount\": 70.08, \"status\": \"completed\"}\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_10",
        "instruction": "As a customer named Mia Kim, you are interested in purchasing several products. You want a desk lamp, gaming console, speaker, and granola bars. Some of these items may not be in stock; if that happens, proceed to buy all of the available items. You might need to visit multiple stores to collect all the items. Payment will be made in cash, having $10,000 for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Mia Kim"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "desk lamp"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "speaker"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "granola bars"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-DESKLMP01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-BTSPKR02"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-GRNLBR12"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-005"
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5011",
                    "payment_method": "cash",
                    "payment_amount": 10000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5011",
                    "payment_method": "cash",
                    "payment_amount": 10000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "store_id": "STORE-005",
                    "employee_id": "EMP-1050",
                    "customer_id": "CUST-5011",
                    "payment_method": "cash",
                    "payment_amount": 10000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                ""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_20",
        "instruction": "As a customer named Logan Smith, you are looking to buy several products. The items you are interested in are: 2 office chairs, 1 pack of AA Batteries, 2 fry pans, and 1 coffee maker. Some items may not be obtainable, but if that occurs, proceed to purchase all available items. You may need to visit several stores to gather all of the items. Payment will be made in cash, with $1,000 available for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Logan Smith"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "office chair"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "coffee maker"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "OFFC-ERGCHR01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-RCHAA04"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOM-COFMKR12"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 2
                        },
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 1
                        },
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5012",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5012",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 2
                        },
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 1
                        },
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 55.16,\n  \"tax_amount\": 4.2,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 8.99,\n  \"change_given\": 944.84,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOM-COFMKR12\",\n      \"quantity\": 1,\n      \"unit_price\": 59.95,\n      \"discount\": 8.99\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 514.73,\n  \"tax_amount\": 39.22,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 53.32,\n  \"change_given\": 485.27,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"OFFC-ERGCHR01\",\n      \"quantity\": 2,\n      \"unit_price\": 229.99,\n      \"discount\": 46.0\n    },\n    {\n      \"sku\": \"ELEC-RCHAA04\",\n      \"quantity\": 1,\n      \"unit_price\": 18.95,\n      \"discount\": 1.33\n    },\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 2,\n      \"unit_price\": 24.95,\n      \"discount\": 5.99\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_21",
        "instruction": "As a customer named William Zhang, you are interested in purchasing a few products. The items you wish to acquire are: 1 jeans, 1 speaker. If some items are unavailable, proceed to buy all the items that are available. You might need to visit several stores to collect all the items. You will be paying the exact amount using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "William Zhang"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "jeans"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "speaker"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-BTSPKR02"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-005"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-005",
                    "employee_id": "EMP-1050",
                    "customer_id": "CUST-5006",
                    "payment_method": "credit_card",
                    "payment_amount": 123.83,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5006",
                    "payment_method": "credit_card",
                    "payment_amount": 53.58,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-005\",\n  \"employee_id\": \"EMP-1050\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 123.83,\n  \"tax_amount\": 9.44,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 15.6,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-BTSPKR02\",\n      \"quantity\": 1,\n      \"unit_price\": 129.99,\n      \"discount\": 15.6\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 53.58,\n  \"tax_amount\": 4.08,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-SLFJEAN34\",\n      \"quantity\": 1,\n      \"unit_price\": 49.5,\n      \"discount\": 0.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_22",
        "instruction": "Identify yourself as a customer named Emma Wilson seeking to purchase a few products. The items you desire are: 2 desk lamp, 2 thermostat, 1 office chair, 1 parka, 2 coffee maker. In the event that some items are not available, feel free to buy all of the available items. You may have to visit various stores to secure all the items. The payment will be made using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Emma Wilson"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "desk lamp"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "thermostat"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "office chair"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "parka"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "coffee maker"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-DESKLMP01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SMRT-THERM02"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "OFFC-ERGCHR01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-WINJKT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOM-COFMKR12"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 2
                        },
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SMRT-THERM02",
                            "quantity": 2
                        },
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5001",
                    "payment_method": "credit_card",
                    "payment_amount": 180.02,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 2
                        },
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5001",
                    "payment_method": "credit_card",
                    "payment_amount": 553.91,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SMRT-THERM02",
                            "quantity": 2
                        },
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5001",
                    "payment_method": "credit_card",
                    "payment_amount": 224.07,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 180.02,\n  \"tax_amount\": 13.72,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 23.58,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5001\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-DESKLMP01\",\n      \"quantity\": 2,\n      \"unit_price\": 34.99,\n      \"discount\": 5.6\n    },\n    {\n      \"sku\": \"HOM-COFMKR12\",\n      \"quantity\": 2,\n      \"unit_price\": 59.95,\n      \"discount\": 17.98\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 553.91,\n  \"tax_amount\": 42.21,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 35.8,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5001\",\n  \"line_items\": [\n    {\n      \"sku\": \"SMRT-THERM02\",\n      \"quantity\": 2,\n      \"unit_price\": 179.0,\n      \"discount\": 35.8\n    },\n    {\n      \"sku\": \"CLTH-WINJKT01\",\n      \"quantity\": 1,\n      \"unit_price\": 189.5,\n      \"discount\": 0.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 224.07,\n  \"tax_amount\": 17.08,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 23.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5001\",\n  \"line_items\": [\n    {\n      \"sku\": \"OFFC-ERGCHR01\",\n      \"quantity\": 1,\n      \"unit_price\": 229.99,\n      \"discount\": 23.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_23",
        "instruction": "Position yourself as a customer named Mia Kim who is looking to buy a few products. The items you intend to purchase are: 2 floor light, 2 parka. Should any items be unavailable, proceed to purchase all available items. You may find it necessary to visit multiple stores to obtain all of the items. Payment will be made in cash, with a total of 1000 available for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Mia Kim"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "floor light"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "parka"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-WINJKT01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5011",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 410.27,\n  \"tax_amount\": 31.27,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 589.73,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-WINJKT01\",\n      \"quantity\": 2,\n      \"unit_price\": 189.5,\n      \"discount\": 0.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_24",
        "instruction": "Act as a customer named Ava Martinez aiming to purchase a few products. The items you seek are: 2 coffee maker, 2 jeans. If certain items are not available, feel free to buy all of the items that are in stock. You may need to visit different stores to gather all of the items. You will be paying the exact amount using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Ava Martinez"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "coffee maker"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "jeans"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOM-COFMKR12"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5005",
                    "payment_method": "credit_card",
                    "payment_amount": 107.17,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5005",
                    "payment_method": "credit_card",
                    "payment_amount": 110.33,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 107.17,\n  \"tax_amount\": 8.17,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5005\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-SLFJEAN34\",\n      \"quantity\": 2,\n      \"unit_price\": 49.5,\n      \"discount\": 0.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 110.33,\n  \"tax_amount\": 8.41,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 17.98,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5005\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOM-COFMKR12\",\n      \"quantity\": 2,\n      \"unit_price\": 59.95,\n      \"discount\": 17.98\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_25",
        "instruction": "Represent yourself as a customer named Mia Kim who intends to buy a few products. The items you are looking for are: 2 desk lamp, 2 speaker, 2 knife. In case some items are not available, simply purchase all the items that are. You may be required to visit various stores to collect all of the items. You will be paying in cash, with a total of 1000 available.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Mia Kim"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "desk lamp"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "speaker"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-DESKLMP01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-BTSPKR02"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-005"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-005",
                    "employee_id": "EMP-1050",
                    "customer_id": "CUST-5011",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5011",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5011",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-005\",\n  \"employee_id\": \"EMP-1050\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 247.65,\n  \"tax_amount\": 18.87,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 31.2,\n  \"change_given\": 752.35,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-BTSPKR02\",\n      \"quantity\": 2,\n      \"unit_price\": 129.99,\n      \"discount\": 31.2\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 69.69,\n  \"tax_amount\": 5.31,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 5.6,\n  \"change_given\": 930.31,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-DESKLMP01\",\n      \"quantity\": 2,\n      \"unit_price\": 34.99,\n      \"discount\": 5.6\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 70.93,\n  \"tax_amount\": 5.41,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 14.38,\n  \"change_given\": 929.07,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 2,\n      \"unit_price\": 39.95,\n      \"discount\": 14.38\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_26",
        "instruction": "Take on the role of a customer named William Zhang who is seeking to buy a few products. The items you wish to purchase are: 1 sparkling water, 2 towel, 1 AA Batteries. If certain items are unavailable, proceed to buy all of the available ones. You might have to visit multiple stores to gather all of the items. Payment will be made in cash, with a total of 1000 available to cover the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "William Zhang"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "towel"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AA Batteries"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-BTHTWL01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-RCHAA04"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        },
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5006",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        },
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5006",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 37.41,\n  \"tax_amount\": 2.27,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 1.85,\n  \"change_given\": 962.59,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 1,\n      \"unit_price\": 7.99,\n      \"discount\": 0.4\n    },\n    {\n      \"sku\": \"HOME-BTHTWL01\",\n      \"quantity\": 2,\n      \"unit_price\": 14.5,\n      \"discount\": 1.45\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 19.07,\n  \"tax_amount\": 1.45,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 1.33,\n  \"change_given\": 980.93,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-RCHAA04\",\n      \"quantity\": 1,\n      \"unit_price\": 18.95,\n      \"discount\": 1.33\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_27",
        "instruction": "Facilitate a customer purchase for Ava Martinez who wants to acquire 1 yoga mat and 1 TV. Some items may not be in stock, so purchase all available options. You might need to visit various stores. The customer will pay in cash with 1000 available.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Ava Martinez"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "yoga mat"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "TV"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-YOGMAT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 1
                        },
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5005",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 1
                        },
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 709.55,\n  \"tax_amount\": 54.07,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 74.5,\n  \"change_given\": 290.45,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5005\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-YOGMAT01\",\n      \"quantity\": 1,\n      \"unit_price\": 29.99,\n      \"discount\": 4.5\n    },\n    {\n      \"sku\": \"ELEC-4KTV55\",\n      \"quantity\": 1,\n      \"unit_price\": 699.99,\n      \"discount\": 70.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_28",
        "instruction": "Position yourself as a customer named Emma Wilson searching to buy a few products. The items you wish to acquire are: 1 AAA Batteries, 2 earbuds. Should any items be unavailable, go ahead and purchase all of the available items. You may need to visit multiple stores to obtain all of the items. Payment will be made using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Emma Wilson"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AAA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "earbuds"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-NCEBUDS01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5001",
                    "payment_method": "credit_card",
                    "payment_amount": 285.76,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 285.76,\n  \"tax_amount\": 21.78,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 36.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5001\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-NCEBUDS01\",\n      \"quantity\": 2,\n      \"unit_price\": 149.99,\n      \"discount\": 36.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_29",
        "instruction": "Represent yourself as a customer named Olivia Romano who is looking to buy a few products. The items you want are: 1 sparkling water, 1 knife, 1 AA Batteries, 2 gaming console, 1 floor light. If certain items are unavailable, proceed to buy all available items. You may need to visit several stores to get all of the items. Payment will be made using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Olivia Romano"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "floor light"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-RCHAA04"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5007",
                    "payment_method": "credit_card",
                    "payment_amount": 19.07,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5007",
                    "payment_method": "credit_card",
                    "payment_amount": 7.59,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5007",
                    "payment_method": "credit_card",
                    "payment_amount": 35.46,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 19.07,\n  \"tax_amount\": 1.45,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 1.33,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5007\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-RCHAA04\",\n      \"quantity\": 1,\n      \"unit_price\": 18.95,\n      \"discount\": 1.33\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 7.59,\n  \"tax_amount\": 0.0,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0,\n  \"discount_total\": 0.4,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5007\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 1,\n      \"unit_price\": 7.99,\n      \"discount\": 0.4\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 35.46,\n  \"tax_amount\": 2.7,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 7.19,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5007\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 1,\n      \"unit_price\": 39.95,\n      \"discount\": 7.19\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_30",
        "instruction": "Conduct yourself as a customer named Mia Kim who is interested in purchasing a few products. The items you want are: 1 earbuds, 2 yoga mat, 2 helmet, 1 desk lamp, 1 granola bars. In case some items may not be available, feel free to go ahead and purchase all available items. You may find it necessary to visit multiple stores to collect every item. The payment will be made using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Mia Kim"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "earbuds"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "yoga mat"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "helmet"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "desk lamp"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "granola bars"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-NCEBUDS01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-YOGMAT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-BIKHLM01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-DESKLMP01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-GRNLBR12"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-004"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 2
                        },
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-004",
                    "employee_id": "EMP-1034",
                    "customer_id": "CUST-5011",
                    "payment_method": "credit_card",
                    "payment_amount": 154.15,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5011",
                    "payment_method": "credit_card",
                    "payment_amount": 90.04,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 2
                        },
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5011",
                    "payment_method": "credit_card",
                    "payment_amount": 142.88,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5011",
                    "payment_method": "credit_card",
                    "payment_amount": 14.24,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-004\",\n  \"employee_id\": \"EMP-1034\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 154.15,\n  \"tax_amount\": 11.75,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 35.6,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-BIKHLM01\",\n      \"quantity\": 2,\n      \"unit_price\": 89.0,\n      \"discount\": 35.6\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 90.04,\n  \"tax_amount\": 6.87,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 11.8,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-YOGMAT01\",\n      \"quantity\": 2,\n      \"unit_price\": 29.99,\n      \"discount\": 9.0\n    },\n    {\n      \"sku\": \"HOME-DESKLMP01\",\n      \"quantity\": 1,\n      \"unit_price\": 34.99,\n      \"discount\": 2.8\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 142.88,\n  \"tax_amount\": 10.89,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 18.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-NCEBUDS01\",\n      \"quantity\": 1,\n      \"unit_price\": 149.99,\n      \"discount\": 18.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0016\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 14.24,\n  \"tax_amount\": 0.0,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0,\n  \"discount_total\": 0.75,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-GRNLBR12\",\n      \"quantity\": 1,\n      \"unit_price\": 14.99,\n      \"discount\": 0.75\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_31",
        "instruction": "Act as a customer named James O'Connor seeking to purchase several products. The desired items include: 1 knife, 1 gaming console, and 1 sparkling water. If some items are not available, proceed to buy all available items. You might need to check multiple stores to collect all items. You will be paying in cash, with a budget of 1000 for your purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "James O'Connor"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 35.46,\n  \"tax_amount\": 2.7,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 7.19,\n  \"change_given\": 964.54,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 1,\n      \"unit_price\": 39.95,\n      \"discount\": 7.19\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 7.59,\n  \"tax_amount\": 0.0,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0,\n  \"discount_total\": 0.4,\n  \"change_given\": 992.41,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 1,\n      \"unit_price\": 7.99,\n      \"discount\": 0.4\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_32",
        "instruction": "Imagine yourself as a customer named William Zhang wanting to buy a few products. The items on your list are: 2 knife, 2 desk lamp, 2 fry pan, and 2 sparkling water. If certain items are out of stock, go ahead and acquire all available items instead. You may need to visit different stores to gather everything you want. Payment will be made in cash, as you have 1000 ready for the transaction.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "William Zhang"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "desk lamp"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-DESKLMP01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5006",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5006",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5006",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 70.93,\n  \"tax_amount\": 5.41,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 14.38,\n  \"change_given\": 929.07,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 2,\n      \"unit_price\": 39.95,\n      \"discount\": 14.38\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 84.87,\n  \"tax_amount\": 5.31,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 6.4,\n  \"change_given\": 915.13,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-DESKLMP01\",\n      \"quantity\": 2,\n      \"unit_price\": 34.99,\n      \"discount\": 5.6\n    },\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 2,\n      \"unit_price\": 7.99,\n      \"discount\": 0.8\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 47.53,\n  \"tax_amount\": 3.62,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 5.99,\n  \"change_given\": 952.47,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 2,\n      \"unit_price\": 24.95,\n      \"discount\": 5.99\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_33",
        "instruction": "Consider yourself a customer named Sophia Singh who wishes to buy several items. Your desired purchases consist of: 2 jeans, 2 fry pan, and 1 earbuds. In case some items are unavailable, feel free to purchase all the items that are in stock. You may have to go to various stores to find all the products. The payment will be made using a credit card for the exact amount.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Sophia Singh"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "jeans"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "earbuds"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-NCEBUDS01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        },
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5003",
                    "payment_method": "credit_card",
                    "payment_amount": 47.53,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5003",
                    "payment_method": "credit_card",
                    "payment_amount": 250.05,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        },
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 47.53,\n  \"tax_amount\": 3.62,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 5.99,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5003\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 2,\n      \"unit_price\": 24.95,\n      \"discount\": 5.99\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 250.05,\n  \"tax_amount\": 19.06,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 18.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5003\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-SLFJEAN34\",\n      \"quantity\": 2,\n      \"unit_price\": 49.5,\n      \"discount\": 0.0\n    },\n    {\n      \"sku\": \"AUDIO-NCEBUDS01\",\n      \"quantity\": 1,\n      \"unit_price\": 149.99,\n      \"discount\": 18.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_34",
        "instruction": "Identify as a customer named Sophia Singh interested in acquiring a few products. The items you are looking for are: 2 floor light, 1 AAA Batteries, and 2 fry pan. If any items are not in stock, go ahead and buy whatever is available. You might visit different stores to get all the desired products. The payment will be settled with a credit card for the exact amount.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Sophia Singh"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "floor light"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AAA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5003",
                    "payment_method": "credit_card",
                    "payment_amount": 47.53,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 47.53,\n  \"tax_amount\": 3.62,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 5.99,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5003\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 2,\n      \"unit_price\": 24.95,\n      \"discount\": 5.99\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_35",
        "instruction": "Envision yourself as a customer named Logan Smith aiming to buy some products. The items you intend to purchase are: 1 floor light, 1 jeans, 1 helmet, 2 yoga mat, and 2 coffee maker. Should any items be unavailable, feel free to buy all items that are accessible. You may need to travel to various stores to gather everything. You will be making the purchase in cash, with 1000 available.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Logan Smith"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "floor light"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "jeans"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "helmet"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "yoga mat"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "coffee maker"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-BIKHLM01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-YOGMAT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOM-COFMKR12"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-004"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 2
                        },
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5012",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 2
                        },
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-004",
                    "employee_id": "EMP-1034",
                    "customer_id": "CUST-5012",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5012",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 165.52,\n  \"tax_amount\": 12.62,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 26.98,\n  \"change_given\": 834.48,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-YOGMAT01\",\n      \"quantity\": 2,\n      \"unit_price\": 29.99,\n      \"discount\": 9.0\n    },\n    {\n      \"sku\": \"HOM-COFMKR12\",\n      \"quantity\": 2,\n      \"unit_price\": 59.95,\n      \"discount\": 17.98\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-004\",\n  \"employee_id\": \"EMP-1034\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 77.07,\n  \"tax_amount\": 5.87,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 17.8,\n  \"change_given\": 922.93,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-BIKHLM01\",\n      \"quantity\": 1,\n      \"unit_price\": 89.0,\n      \"discount\": 17.8\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 53.58,\n  \"tax_amount\": 4.08,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 946.42,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-SLFJEAN34\",\n      \"quantity\": 1,\n      \"unit_price\": 49.5,\n      \"discount\": 0.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_36",
        "instruction": "Picture yourself as a customer named Logan Smith looking to acquire a few items. The items you wish to purchase are: 1 yoga mat, 1 sparkling water, and 2 speaker. If some products are out of stock, proceed with acquiring all available ones. You may have to check multiple stores to fulfill your shopping list. The exact amount will be paid using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Logan Smith"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "yoga mat"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "speaker"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-YOGMAT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-BTSPKR02"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-005"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 1
                        },
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5012",
                    "payment_method": "credit_card",
                    "payment_amount": 35.18,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 1
                        },
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-005",
                    "employee_id": "EMP-1050",
                    "customer_id": "CUST-5012",
                    "payment_method": "credit_card",
                    "payment_amount": 247.65,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 35.18,\n  \"tax_amount\": 2.1,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 4.9,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-YOGMAT01\",\n      \"quantity\": 1,\n      \"unit_price\": 29.99,\n      \"discount\": 4.5\n    },\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 1,\n      \"unit_price\": 7.99,\n      \"discount\": 0.4\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-005\",\n  \"employee_id\": \"EMP-1050\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 247.65,\n  \"tax_amount\": 18.87,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 31.2,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-BTSPKR02\",\n      \"quantity\": 2,\n      \"unit_price\": 129.99,\n      \"discount\": 31.2\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_37",
        "instruction": "Visualize yourself as a customer named Liam Anderson who is aiming to buy a few products. The items you want to acquire are: 1 AA Batteries, 2 jeans, 1 towel, and 1 helmet. In the event that some items are not available, go ahead and purchase everything you can find that is available. You may need to visit multiple stores to secure all the items. Payment will be made using a credit card for the exact total.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Liam Anderson"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "jeans"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "towel"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "helmet"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-RCHAA04"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-BTHTWL01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-BIKHLM01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-004"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-004",
                    "employee_id": "EMP-1034",
                    "customer_id": "CUST-5004",
                    "payment_method": "credit_card",
                    "payment_amount": 77.07,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5004",
                    "payment_method": "credit_card",
                    "payment_amount": 107.17,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5004",
                    "payment_method": "credit_card",
                    "payment_amount": 14.92,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5004",
                    "payment_method": "credit_card",
                    "payment_amount": 19.07,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-004\",\n  \"employee_id\": \"EMP-1034\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 77.07,\n  \"tax_amount\": 5.87,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 17.8,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-BIKHLM01\",\n      \"quantity\": 1,\n      \"unit_price\": 89.0,\n      \"discount\": 17.8\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 107.17,\n  \"tax_amount\": 8.17,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-SLFJEAN34\",\n      \"quantity\": 2,\n      \"unit_price\": 49.5,\n      \"discount\": 0.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 14.92,\n  \"tax_amount\": 1.14,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.73,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-BTHTWL01\",\n      \"quantity\": 1,\n      \"unit_price\": 14.5,\n      \"discount\": 0.73\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0016\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 19.07,\n  \"tax_amount\": 1.45,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 1.33,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-RCHAA04\",\n      \"quantity\": 1,\n      \"unit_price\": 18.95,\n      \"discount\": 1.33\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_38",
        "instruction": "Think of yourself as a customer named Sophia Singh wanting to purchase several products. The items you are interested in are: 2 jeans, 2 fry pan, and 1 granola bars. If specific items are unavailable, feel free to purchase all the items that are in stock. You may have to venture to different stores to complete your list. The payment will be made with a credit card for the exact amount.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Sophia Singh"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "jeans"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "granola bars"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-GRNLBR12"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5003",
                    "payment_method": "credit_card",
                    "payment_amount": 61.77,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5003",
                    "payment_method": "credit_card",
                    "payment_amount": 107.17,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 61.77,\n  \"tax_amount\": 3.62,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 6.74,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5003\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 2,\n      \"unit_price\": 24.95,\n      \"discount\": 5.99\n    },\n    {\n      \"sku\": \"GROC-GRNLBR12\",\n      \"quantity\": 1,\n      \"unit_price\": 14.99,\n      \"discount\": 0.75\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 107.17,\n  \"tax_amount\": 8.17,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5003\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-SLFJEAN34\",\n      \"quantity\": 2,\n      \"unit_price\": 49.5,\n      \"discount\": 0.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_39",
        "instruction": "Assume the role of a customer named James O'Connor looking to buy several products. The desired items include: 1 spoon set, 1 fry pan, 2 earbuds, and 1 gaming console. If certain items are not available, proceed to buy all available items. You might have to check out various stores to collect everything desired. You will pay in cash, as you have 1000 for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "James O'Connor"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "spoon set"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "earbuds"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-NCEBUDS01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 23.77,\n  \"tax_amount\": 1.81,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 2.99,\n  \"change_given\": 976.23,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 1,\n      \"unit_price\": 24.95,\n      \"discount\": 2.99\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 285.76,\n  \"tax_amount\": 21.78,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 36.0,\n  \"change_given\": 714.24,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-NCEBUDS01\",\n      \"quantity\": 2,\n      \"unit_price\": 149.99,\n      \"discount\": 36.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_40",
        "instruction": "Identify yourself as a customer named Logan Smith on the lookout for several products. The items you want to acquire are: 1 sparkling water, 2 desk lamp, 1 almond butter, and 2 knife. If any of the items are not in stock, go ahead and purchase whatever is available. You may need to visit multiple locations to gather all items. Payment will be in cash, with a budget of 1000 for your shopping.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Logan Smith"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "desk lamp"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "almond butter"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-DESKLMP01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-ALMBTR500"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        },
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5012",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        },
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5012",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 90.27,\n  \"tax_amount\": 5.31,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 6.0,\n  \"change_given\": 909.73,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 1,\n      \"unit_price\": 7.99,\n      \"discount\": 0.4\n    },\n    {\n      \"sku\": \"HOME-DESKLMP01\",\n      \"quantity\": 2,\n      \"unit_price\": 34.99,\n      \"discount\": 5.6\n    },\n    {\n      \"sku\": \"GROC-ALMBTR500\",\n      \"quantity\": 1,\n      \"unit_price\": 12.99,\n      \"discount\": 0.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 70.93,\n  \"tax_amount\": 5.41,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 14.38,\n  \"change_given\": 929.07,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 2,\n      \"unit_price\": 39.95,\n      \"discount\": 14.38\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_41",
        "instruction": "As a customer named Sophia Singh, you are interested in purchasing a few products. The items you desire include: 2 floor lights, 1 speaker, 1 granola bar, and 1 office chair. Should any items be unavailable, proceed to buy all the available ones. You might need to check multiple stores to collect all the items. Payment will be made in cash, and you have 1000 for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Sophia Singh"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "floor light"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "speaker"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "granola bars"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "office chair"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-BTSPKR02"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-GRNLBR12"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "OFFC-ERGCHR01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-005"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 1
                        },
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5003",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 1
                        },
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-005",
                    "employee_id": "EMP-1050",
                    "customer_id": "CUST-5003",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 238.31,\n  \"tax_amount\": 17.08,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 23.75,\n  \"change_given\": 761.69,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5003\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-GRNLBR12\",\n      \"quantity\": 1,\n      \"unit_price\": 14.99,\n      \"discount\": 0.75\n    },\n    {\n      \"sku\": \"OFFC-ERGCHR01\",\n      \"quantity\": 1,\n      \"unit_price\": 229.99,\n      \"discount\": 23.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-005\",\n  \"employee_id\": \"EMP-1050\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 123.83,\n  \"tax_amount\": 9.44,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 15.6,\n  \"change_given\": 876.17,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5003\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-BTSPKR02\",\n      \"quantity\": 1,\n      \"unit_price\": 129.99,\n      \"discount\": 15.6\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_42",
        "instruction": "As a customer named Emma Wilson, you are looking to acquire a few products. The items you wish to get are: 1 floor light, 2 sparkling waters, and 2 spoon sets. If certain items are not available, feel free to purchase all the available ones. You may need to explore multiple stores for all the items. Payment will be made in the exact amount using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Emma Wilson"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "floor light"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "spoon set"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5001",
                    "payment_method": "credit_card",
                    "payment_amount": 15.18,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 15.18,\n  \"tax_amount\": 0.0,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0,\n  \"discount_total\": 0.8,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5001\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 2,\n      \"unit_price\": 7.99,\n      \"discount\": 0.8\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_43",
        "instruction": "Identifying as a customer named James O'Connor, you plan to buy a few products. The items you seek consist of: 1 knife, 1 gaming console, and 1 sparkling water. In case some items are unavailable, go ahead and acquire all of the available ones. You may have to visit various stores to obtain all the items. Payment will be in cash, and you have 1000 to cover the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "James O'Connor"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 35.46,\n  \"tax_amount\": 2.7,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 7.19,\n  \"change_given\": 964.54,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 1,\n      \"unit_price\": 39.95,\n      \"discount\": 7.19\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 7.59,\n  \"tax_amount\": 0.0,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0,\n  \"discount_total\": 0.4,\n  \"change_given\": 992.41,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 1,\n      \"unit_price\": 7.99,\n      \"discount\": 0.4\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_44",
        "instruction": "In the role of a customer named Ava Martinez, you are on a mission to purchase a few products. The desired items include: 1 knife, 2 earbuds, 1 AAA battery, 2 fry pans, and 2 jeans. If any items are out of stock, proceed to buy all the available ones. You might have to check several stores to gather all the items. Payment will be made in cash, and you are equipped with 1000 for this purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Ava Martinez"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "earbuds"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AAA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "jeans"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-NCEBUDS01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 1
                        },
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 2
                        },
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5005",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5005",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 1
                        },
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 2
                        },
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 47.53,\n  \"tax_amount\": 3.62,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 5.99,\n  \"change_given\": 952.47,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5005\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 2,\n      \"unit_price\": 24.95,\n      \"discount\": 5.99\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 428.39,\n  \"tax_amount\": 32.65,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 43.19,\n  \"change_given\": 571.61,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5005\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 1,\n      \"unit_price\": 39.95,\n      \"discount\": 7.19\n    },\n    {\n      \"sku\": \"AUDIO-NCEBUDS01\",\n      \"quantity\": 2,\n      \"unit_price\": 149.99,\n      \"discount\": 36.0\n    },\n    {\n      \"sku\": \"CLTH-SLFJEAN34\",\n      \"quantity\": 2,\n      \"unit_price\": 49.5,\n      \"discount\": 0.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_45",
        "instruction": "As a customer named Mia Kim, you intend to buy a few products. The items you want to purchase are: 2 jeans, 2 AAA batteries, and 1 helmet. Should there be any unavailable items, feel free to buy all the ones that are available. You may need to visit multiple stores to get all the items. You will be paying in cash, and you have 1000 for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Mia Kim"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "jeans"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AAA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "helmet"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-BIKHLM01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-004"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5011",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-004",
                    "employee_id": "EMP-1034",
                    "customer_id": "CUST-5011",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 107.17,\n  \"tax_amount\": 8.17,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 892.83,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-SLFJEAN34\",\n      \"quantity\": 2,\n      \"unit_price\": 49.5,\n      \"discount\": 0.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-004\",\n  \"employee_id\": \"EMP-1034\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 77.07,\n  \"tax_amount\": 5.87,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 17.8,\n  \"change_given\": 922.93,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-BIKHLM01\",\n      \"quantity\": 1,\n      \"unit_price\": 89.0,\n      \"discount\": 17.8\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_46",
        "instruction": "Identifying as a customer named Mia Kim, you are interested in purchasing several products. The items on your list include: 1 speaker, 2 fry pans, 2 floor lights, and 1 TV. If certain items are not available, go ahead and purchase all the ones that are. Be prepared to visit multiple stores to collect all the items. You will be paying the exact amount using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Mia Kim"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "speaker"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "floor light"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "TV"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-BTSPKR02"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-005"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-005",
                    "employee_id": "EMP-1050",
                    "customer_id": "CUST-5011",
                    "payment_method": "credit_card",
                    "payment_amount": 123.83,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5011",
                    "payment_method": "credit_card",
                    "payment_amount": 681.96,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5011",
                    "payment_method": "credit_card",
                    "payment_amount": 47.53,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-005\",\n  \"employee_id\": \"EMP-1050\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 123.83,\n  \"tax_amount\": 9.44,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 15.6,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-BTSPKR02\",\n      \"quantity\": 1,\n      \"unit_price\": 129.99,\n      \"discount\": 15.6\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 681.96,\n  \"tax_amount\": 51.97,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 70.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-4KTV55\",\n      \"quantity\": 1,\n      \"unit_price\": 699.99,\n      \"discount\": 70.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 47.53,\n  \"tax_amount\": 3.62,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 5.99,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 2,\n      \"unit_price\": 24.95,\n      \"discount\": 5.99\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_47",
        "instruction": "Taking the role of a customer named Emma Wilson, you are looking to buy several products. The items you seek consist of: 2 desk lamps, 2 spoon sets, 1 sparkling water, 2 granola bars, and 2 floor lights. In case some items are unavailable, feel free to buy all the available items. You may need to explore multiple stores for all the items. Payment will be made in cash, and you have 1000 for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Emma Wilson"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "desk lamp"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "spoon set"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "granola bars"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "floor light"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-DESKLMP01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-GRNLBR12"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5001",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5001",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 77.28,\n  \"tax_amount\": 5.31,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 6.0,\n  \"change_given\": 922.72,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5001\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-DESKLMP01\",\n      \"quantity\": 2,\n      \"unit_price\": 34.99,\n      \"discount\": 5.6\n    },\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 1,\n      \"unit_price\": 7.99,\n      \"discount\": 0.4\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 28.48,\n  \"tax_amount\": 0.0,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0,\n  \"discount_total\": 1.5,\n  \"change_given\": 971.52,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5001\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-GRNLBR12\",\n      \"quantity\": 2,\n      \"unit_price\": 14.99,\n      \"discount\": 1.5\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_48",
        "instruction": "As a customer named Noah Tran, you wish to purchase a few products. The items you desire are: 2 fry pans, 2 AA batteries, and 2 parkas. Should any items be unavailable, proceed to acquire all the available ones. You may have to visit multiple stores to get everything you want. Payment will be made in the exact amount using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Noah Tran"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "parka"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-RCHAA04"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-WINJKT01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        },
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5002",
                    "payment_method": "credit_card",
                    "payment_amount": 410.27,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5002",
                    "payment_method": "credit_card",
                    "payment_amount": 85.69,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        },
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 410.27,\n  \"tax_amount\": 31.27,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5002\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-WINJKT01\",\n      \"quantity\": 2,\n      \"unit_price\": 189.5,\n      \"discount\": 0.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 85.69,\n  \"tax_amount\": 6.53,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 8.64,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5002\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 2,\n      \"unit_price\": 24.95,\n      \"discount\": 5.99\n    },\n    {\n      \"sku\": \"ELEC-RCHAA04\",\n      \"quantity\": 2,\n      \"unit_price\": 18.95,\n      \"discount\": 2.65\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_49",
        "instruction": "In the role of a customer named Mia Kim, you are planning to buy a few products. The items you wish to acquire are: 2 jeans and 1 helmet. If some items are unavailable, go ahead and purchase all of the available items. You might need to check multiple stores to obtain all the items. Payment will be in the exact amount using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Mia Kim"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "jeans"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "helmet"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-BIKHLM01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-004"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-004",
                    "employee_id": "EMP-1034",
                    "customer_id": "CUST-5011",
                    "payment_method": "credit_card",
                    "payment_amount": 77.07,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5011",
                    "payment_method": "credit_card",
                    "payment_amount": 107.17,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-004\",\n  \"employee_id\": \"EMP-1034\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 77.07,\n  \"tax_amount\": 5.87,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 17.8,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-BIKHLM01\",\n      \"quantity\": 1,\n      \"unit_price\": 89.0,\n      \"discount\": 17.8\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 107.17,\n  \"tax_amount\": 8.17,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-SLFJEAN34\",\n      \"quantity\": 2,\n      \"unit_price\": 49.5,\n      \"discount\": 0.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_50",
        "instruction": "As a customer named Charlotte Dubois, you are looking to purchase a few products. The items you seek include: 1 parka, 1 desk lamp, and 1 knife. Should any items be out of stock, feel free to buy all the available ones. You may have to check several stores to gather all the items. Payment will be made in the exact amount using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Charlotte Dubois"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "parka"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "desk lamp"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-WINJKT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-DESKLMP01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 1
                        },
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5009",
                    "payment_method": "credit_card",
                    "payment_amount": 240.59,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 1
                        },
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5009",
                    "payment_method": "credit_card",
                    "payment_amount": 34.85,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 240.59,\n  \"tax_amount\": 18.33,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 7.19,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5009\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-WINJKT01\",\n      \"quantity\": 1,\n      \"unit_price\": 189.5,\n      \"discount\": 0.0\n    },\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 1,\n      \"unit_price\": 39.95,\n      \"discount\": 7.19\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 34.85,\n  \"tax_amount\": 2.66,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 2.8,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5009\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-DESKLMP01\",\n      \"quantity\": 1,\n      \"unit_price\": 34.99,\n      \"discount\": 2.8\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_51",
        "instruction": "As a customer named Liam Anderson, you are in search of a few products. The items you're looking for include: 1 towel, 1 desk lamp, 2 fry pans, and 1 AAA Batteries. If some items are unavailable, proceed to purchase all available items. You might need to visit several stores to gather all the items. You'll be paying the exact amount with a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Liam Anderson"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "towel"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "desk lamp"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AAA Batteries"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-BTHTWL01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-DESKLMP01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 1
                        },
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5004",
                    "payment_method": "credit_card",
                    "payment_amount": 47.53,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5004",
                    "payment_method": "credit_card",
                    "payment_amount": 49.77,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 1
                        },
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 47.53,\n  \"tax_amount\": 3.62,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 5.99,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 2,\n      \"unit_price\": 24.95,\n      \"discount\": 5.99\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 49.77,\n  \"tax_amount\": 3.8,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 3.53,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-BTHTWL01\",\n      \"quantity\": 1,\n      \"unit_price\": 14.5,\n      \"discount\": 0.73\n    },\n    {\n      \"sku\": \"HOME-DESKLMP01\",\n      \"quantity\": 1,\n      \"unit_price\": 34.99,\n      \"discount\": 2.8\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_52",
        "instruction": "Acting as a customer named Liam Anderson, you are looking to acquire a few products. The items you desire are: 2 fry pans, 2 AA Batteries, and 1 sparkling water. Should any items be unavailable, proceed to buy all items that are available. You may have to go to multiple stores to secure all items. Payment will be made in exact amount via credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Liam Anderson"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-RCHAA04"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        },
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5004",
                    "payment_method": "credit_card",
                    "payment_amount": 85.69,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        },
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5004",
                    "payment_method": "credit_card",
                    "payment_amount": 7.59,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 85.69,\n  \"tax_amount\": 6.53,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 8.64,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 2,\n      \"unit_price\": 24.95,\n      \"discount\": 5.99\n    },\n    {\n      \"sku\": \"ELEC-RCHAA04\",\n      \"quantity\": 2,\n      \"unit_price\": 18.95,\n      \"discount\": 2.65\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 7.59,\n  \"tax_amount\": 0.0,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0,\n  \"discount_total\": 0.4,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 1,\n      \"unit_price\": 7.99,\n      \"discount\": 0.4\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_53",
        "instruction": "As a customer named Emma Wilson, you are aiming to purchase a few products. The items you wish to obtain are: 1 parka, 1 knife, and 1 floor light. If certain items aren't available, continue with the purchase of all available items. You may need to visit different stores to collect all the items. You will pay the exact amount using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Emma Wilson"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "parka"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "floor light"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-WINJKT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 1
                        },
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5001",
                    "payment_method": "credit_card",
                    "payment_amount": 240.59,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 1
                        },
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 240.59,\n  \"tax_amount\": 18.33,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 7.19,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5001\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-WINJKT01\",\n      \"quantity\": 1,\n      \"unit_price\": 189.5,\n      \"discount\": 0.0\n    }\n, {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 1,\n      \"unit_price\": 39.95,\n      \"discount\": 7.19\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_54",
        "instruction": "Identifying as a customer named Liam Anderson, you are on the lookout for a few products. The items you seek consist of: 1 AAA Batteries, 1 gaming console, 1 AA Batteries, 2 laptops, and 1 spoon set. If any choice is unavailable, proceed to acquire all available items. You may have to visit a number of stores to gather all items. Payment will be made in exact amount via credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Liam Anderson"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AAA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "laptop"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "spoon set"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-RCHAA04"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-GAMLP15"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-GAMLP15",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5004",
                    "payment_method": "credit_card",
                    "payment_amount": 19.07,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5004",
                    "payment_method": "credit_card",
                    "payment_amount": 3245.34,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-GAMLP15",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 19.07,\n  \"tax_amount\": 1.45,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 1.33,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-RCHAA04\",\n      \"quantity\": 1,\n      \"unit_price\": 18.95,\n      \"discount\": 1.33\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 3245.34,\n  \"tax_amount\": 247.34,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-GAMLP15\",\n      \"quantity\": 2,\n      \"unit_price\": 1499.0,\n      \"discount\": 0.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_55",
        "instruction": "Taking on the role of a customer named William Zhang, you are looking to buy a few products. The items you want include: 1 sparkling water and 2 yoga mats. If some products aren't in stock, feel free to purchase all available ones. You might need to go to multiple stores to gather everything. You are paying in cash with 1000 available for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "William Zhang"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "yoga mat"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-YOGMAT01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        },
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5006",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        },
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 62.78,\n  \"tax_amount\": 4.21,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 9.4,\n  \"change_given\": 937.22,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 1,\n      \"unit_price\": 7.99,\n      \"discount\": 0.4\n    },\n    {\n      \"sku\": \"SPORT-YOGMAT01\",\n      \"quantity\": 2,\n      \"unit_price\": 29.99,\n      \"discount\": 9.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_56",
        "instruction": "You are acting as a customer named James O'Connor who is seeking to buy a few products. The items you want to procure are: 1 office chair, 2 towels, and 2 helmets. If certain items are not available, please proceed to buy all items that can be obtained. You may have to visit different stores in order to get everything. Payment will be made in exact amount with a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "James O'Connor"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "office chair"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "towel"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "helmet"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "OFFC-ERGCHR01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-BTHTWL01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-BIKHLM01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-004"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-004",
                    "employee_id": "EMP-1034",
                    "customer_id": "CUST-5008",
                    "payment_method": "credit_card",
                    "payment_amount": 154.15,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5008",
                    "payment_method": "credit_card",
                    "payment_amount": 224.07,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5008",
                    "payment_method": "credit_card",
                    "payment_amount": 29.82,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-004\",\n  \"employee_id\": \"EMP-1034\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 154.15,\n  \"tax_amount\": 11.75,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 35.6,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-BIKHLM01\",\n      \"quantity\": 2,\n      \"unit_price\": 89.0,\n      \"discount\": 35.6\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 224.07,\n  \"tax_amount\": 17.08,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 23.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"OFFC-ERGCHR01\",\n      \"quantity\": 1,\n      \"unit_price\": 229.99,\n      \"discount\": 23.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 29.82,\n  \"tax_amount\": 2.27,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 1.45,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-BTHTWL01\",\n      \"quantity\": 2,\n      \"unit_price\": 14.5,\n      \"discount\": 1.45\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_57",
        "instruction": "As a customer named James O'Connor, you are planning to buy a few products. The items you desire include: 2 knives, 2 gaming consoles, 2 towels, and 1 granola bars. If any items are unavailable, go ahead and purchase all the items that are available. You may need to shop in multiple stores to collect everything. You will be paying the exact total using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "James O'Connor"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "towel"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "granola bars"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-BTHTWL01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-GRNLBR12"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5008",
                    "payment_method": "credit_card",
                    "payment_amount": 29.82,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5008",
                    "payment_method": "credit_card",
                    "payment_amount": 70.93,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5008",
                    "payment_method": "credit_card",
                    "payment_amount": 14.24,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 29.82,\n  \"tax_amount\": 2.27,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 1.45,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-BTHTWL01\",\n      \"quantity\": 2,\n      \"unit_price\": 14.5,\n      \"discount\": 1.45\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 70.93,\n  \"tax_amount\": 5.41,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 14.38,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 2,\n      \"unit_price\": 39.95,\n      \"discount\": 14.38\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 14.24,\n  \"tax_amount\": 0.0,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0,\n  \"discount_total\": 0.75,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-GRNLBR12\",\n      \"quantity\": 1,\n      \"unit_price\": 14.99,\n      \"discount\": 0.75\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_58",
        "instruction": "Identifying as a customer named Liam Anderson, you aim to purchase a few products. The items on your list are: 1 gaming console, 1 coffee maker, and 2 fry pans. If some items aren't reachable, continue to buy all the available ones. Multiple store visits might be necessary to gather all items. You will make your payment in cash with 1000 available for this purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Liam Anderson"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "coffee maker"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOM-COFMKR12"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5004",
                    "payment_method": "cash",
                    "payment_amount": 47.53,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5004",
                    "payment_method": "cash",
                    "payment_amount": 55.16,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 47.53,\n  \"tax_amount\": 3.62,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 5.99,\n  \"change_given\": 952.47,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 2,\n      \"unit_price\": 24.95,\n      \"discount\": 5.99\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 55.16,\n  \"tax_amount\": 4.2,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 8.99,\n  \"change_given\": 944.84,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOM-COFMKR12\",\n      \"quantity\": 1,\n      \"unit_price\": 59.95,\n      \"discount\": 8.99\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_59",
        "instruction": "You are representing a customer named Noah Tran who wishes to purchase a few products. The desired items are: 1 laptop and 1 thermostat. If certain products are unavailable, proceed to buy those that are accessible. You may need to visit several stores to complete your collection. Payment will be made in cash with 10000 available for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Noah Tran"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "laptop"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "thermostat"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-GAMLP15"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SMRT-THERM02"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-GAMLP15",
                            "quantity": 1
                        },
                        {
                            "sku": "SMRT-THERM02",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5002",
                    "payment_method": "cash",
                    "payment_amount": 10000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-GAMLP15",
                            "quantity": 1
                        },
                        {
                            "sku": "SMRT-THERM02",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 1797.06,\n  \"tax_amount\": 136.96,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 17.9,\n  \"change_given\": 8202.94,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5002\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-GAMLP15\",\n      \"quantity\": 1,\n      \"unit_price\": 1499.0,\n      \"discount\": 0.0\n    },\n    {\n      \"sku\": \"SMRT-THERM02\",\n      \"quantity\": 1,\n      \"unit_price\": 179.0,\n      \"discount\": 17.9\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_60",
        "instruction": "As a customer named James O'Connor, you are looking to buy a few products. The items you want include: 1 towel, 2 earbuds, 2 jeans, and 1 thermostat. If some items are not in stock, kindly proceed to purchase all available items. Visiting multiple stores might be required to gather everything. You will pay the exact amount via credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "James O'Connor"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "towel"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "earbuds"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "jeans"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "thermostat"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-BTHTWL01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-NCEBUDS01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SMRT-THERM02"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 2
                        },
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        },
                        {
                            "sku": "SMRT-THERM02",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5008",
                    "payment_method": "credit_card",
                    "payment_amount": 14.92,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5008",
                    "payment_method": "credit_card",
                    "payment_amount": 567.32,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 2
                        },
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        },
                        {
                            "sku": "SMRT-THERM02",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 14.92,\n  \"tax_amount\": 1.14,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.73,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-BTHTWL01\",\n      \"quantity\": 1,\n      \"unit_price\": 14.5,\n      \"discount\": 0.73\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 567.32,\n  \"tax_amount\": 43.24,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 53.9,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-NCEBUDS01\",\n      \"quantity\": 2,\n      \"unit_price\": 149.99,\n      \"discount\": 36.0\n    },\n    {\n      \"sku\": \"CLTH-SLFJEAN34\",\n      \"quantity\": 2,\n      \"unit_price\": 49.5,\n      \"discount\": 0.0\n    },\n    {\n      \"sku\": \"SMRT-THERM02\",\n      \"quantity\": 1,\n      \"unit_price\": 179.0,\n      \"discount\": 17.9\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_61",
        "instruction": "As a customer named Logan Smith, you wish to purchase several products. The desired items are: 1 earbuds, 2 coffee maker, 1 gaming console, 2 TV, 1 floor light. Some items might not be available; therefore, proceed to buy all the items that are available. You might need to visit various stores to collect all of the products. The payment will be made in full using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Logan Smith"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "earbuds"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "coffee maker"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "TV"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "floor light"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-NCEBUDS01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOM-COFMKR12"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 2
                        },
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5012",
                    "payment_method": "credit_card",
                    "payment_amount": 1474.26,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 2
                        },
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5012",
                    "payment_method": "credit_card",
                    "payment_amount": 142.88,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 1474.26,\n  \"tax_amount\": 112.36,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 157.98,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOM-COFMKR12\",\n      \"quantity\": 2,\n      \"unit_price\": 59.95,\n      \"discount\": 17.98\n    },\n    {\n      \"sku\": \"ELEC-4KTV55\",\n      \"quantity\": 2,\n      \"unit_price\": 699.99,\n      \"discount\": 140.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 142.88,\n  \"tax_amount\": 10.89,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 18.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-NCEBUDS01\",\n      \"quantity\": 1,\n      \"unit_price\": 149.99,\n      \"discount\": 18.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_62",
        "instruction": "As a customer named Ava Martinez, you aim to buy several products. The items on your list include: 2 AA Batteries, 1 jeans, 2 gaming console, 1 yoga mat, 1 coffee maker. Some items may not be in stock; if that occurs, proceed to purchase all available items. You may need to travel to different stores to acquire everything. Payment will be done in cash, with a total of 1000 available for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Ava Martinez"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "jeans"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "yoga mat"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "coffee maker"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-RCHAA04"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-YOGMAT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOM-COFMKR12"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 1
                        },
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5005",
                    "payment_method": "cash",
                    "payment_amount": 82.75,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 1
                        },
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5005",
                    "payment_method": "cash",
                    "payment_amount": 53.58,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5005",
                    "payment_method": "cash",
                    "payment_amount": 38.16,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 82.75,\n  \"tax_amount\": 6.3,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 13.49,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5005\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-YOGMAT01\",\n      \"quantity\": 1,\n      \"unit_price\": 29.99,\n      \"discount\": 4.5\n    },\n    {\n      \"sku\": \"HOM-COFMKR12\",\n      \"quantity\": 1,\n      \"unit_price\": 59.95,\n      \"discount\": 8.99\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 53.58,\n  \"tax_amount\": 4.08,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5005\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-SLFJEAN34\",\n      \"quantity\": 1,\n      \"unit_price\": 49.5,\n      \"discount\": 0.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 38.16,\n  \"tax_amount\": 2.91,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 2.65,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5005\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-RCHAA04\",\n      \"quantity\": 2,\n      \"unit_price\": 18.95,\n      \"discount\": 2.65\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_63",
        "instruction": "As a customer named Olivia Romano, you intend to buy a few products. The items you are looking for are: 1 almond butter, 1 AAA Batteries, 1 fry pan. Some items may not be available; if so, proceed to purchase everything that is in stock. You may need to visit multiple stores to gather all of the items. A credit card will be used for the full payment.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Olivia Romano"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "almond butter"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AAA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-ALMBTR500"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5007",
                    "payment_method": "credit_card",
                    "payment_amount": 12.99,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5007",
                    "payment_method": "credit_card",
                    "payment_amount": 23.77,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 12.99,\n  \"tax_amount\": 0.0,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5007\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-ALMBTR500\",\n      \"quantity\": 1,\n      \"unit_price\": 12.99,\n      \"discount\": 0.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 23.77,\n  \"tax_amount\": 1.81,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 2.99,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5007\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 1,\n      \"unit_price\": 24.95,\n      \"discount\": 2.99\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_64",
        "instruction": "As a customer named William Zhang, you want to buy several products. The items on your shopping list are: 2 knife, 2 almond butter. If some items are not available, proceed to acquire all items that you can find. It may be necessary to visit different stores to get everything. Payment will be made in full via credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "William Zhang"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "almond butter"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-ALMBTR500"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5006",
                    "payment_method": "credit_card",
                    "payment_amount": 25.98,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5006",
                    "payment_method": "credit_card",
                    "payment_amount": 70.93,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 25.98,\n  \"tax_amount\": 0.0,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-ALMBTR500\",\n      \"quantity\": 2,\n      \"unit_price\": 12.99,\n      \"discount\": 0.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 70.93,\n  \"tax_amount\": 5.41,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 14.38,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 2,\n      \"unit_price\": 39.95,\n      \"discount\": 14.38\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_65",
        "instruction": "As a customer named James O'Connor, you seek to purchase a few items. The items you wish to buy include: 2 AAA Batteries, 2 yoga mat, 2 sparkling water, 2 spoon set, 1 fry pan. If certain items are unavailable, please proceed to purchase all items that are accessible. You may need to check various stores to collect all the products. A credit card will be used to pay the exact amount.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "James O'Connor"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AAA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "yoga mat"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "spoon set"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-YOGMAT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5008",
                    "payment_method": "credit_card",
                    "payment_amount": 70.37,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5008",
                    "payment_method": "credit_card",
                    "payment_amount": 23.77,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 70.37,\n  \"tax_amount\": 4.21,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 9.8,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-YOGMAT01\",\n      \"quantity\": 2,\n      \"unit_price\": 29.99,\n      \"discount\": 9.0\n    },\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 2,\n      \"unit_price\": 7.99,\n      \"discount\": 0.8\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 23.77,\n  \"tax_amount\": 1.81,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 2.99,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 1,\n      \"unit_price\": 24.95,\n      \"discount\": 2.99\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_66",
        "instruction": "As a customer named Liam Anderson, you are looking to buy several products. The items you want are: 1 parka, 2 jeans, 2 speaker, 1 desk lamp, 2 helmet. If some items cannot be found, proceed to buy whatever is available. You may have to go to several stores to obtain all of them. Payment will be made in cash, and you have 1000 available for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Liam Anderson"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "parka"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "jeans"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "speaker"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "desk lamp"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "helmet"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-WINJKT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-BTSPKR02"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-DESKLMP01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-BIKHLM01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-004"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-005"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 1
                        },
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-004",
                    "employee_id": "EMP-1034",
                    "customer_id": "CUST-5004",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5004",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-005",
                    "employee_id": "EMP-1050",
                    "customer_id": "CUST-5004",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5004",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 1
                        },
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-004\",\n  \"employee_id\": \"EMP-1034\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 154.15,\n  \"tax_amount\": 11.75,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 35.6,\n  \"change_given\": 845.85,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-BIKHLM01\",\n      \"quantity\": 2,\n      \"unit_price\": 89.0,\n      \"discount\": 35.6\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 34.85,\n  \"tax_amount\": 2.66,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 2.8,\n  \"change_given\": 965.15,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-DESKLMP01\",\n      \"quantity\": 1,\n      \"unit_price\": 34.99,\n      \"discount\": 2.8\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-005\",\n  \"employee_id\": \"EMP-1050\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 247.65,\n  \"tax_amount\": 18.87,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 31.2,\n  \"change_given\": 752.35,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-BTSPKR02\",\n      \"quantity\": 2,\n      \"unit_price\": 129.99,\n      \"discount\": 31.2\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0016\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 312.3,\n  \"tax_amount\": 23.8,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 687.7,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-WINJKT01\",\n      \"quantity\": 1,\n      \"unit_price\": 189.5,\n      \"discount\": 0.0\n    },\n    {\n      \"sku\": \"CLTH-SLFJEAN34\",\n      \"quantity\": 2,\n      \"unit_price\": 49.5,\n      \"discount\": 0.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_67",
        "instruction": "As a customer named Olivia Romano, you are interested in purchasing a few items. The desired items include: 1 AAA Batteries, 2 fry pan, 2 TV, 1 almond butter. In case some items are not in stock, proceed to buy all items that are available. You might need to visit multiple stores to gather everything. Payment will be made in cash, with 2000 set aside for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Olivia Romano"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AAA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "TV"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "almond butter"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-ALMBTR500"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5007",
                    "payment_method": "cash",
                    "payment_amount": 2000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5007",
                    "payment_method": "cash",
                    "payment_amount": 2000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 1376.92,\n  \"tax_amount\": 103.95,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 140.0,\n  \"change_given\": 623.08,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5007\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-4KTV55\",\n      \"quantity\": 2,\n      \"unit_price\": 699.99,\n      \"discount\": 140.0\n    }\n, {\n      \"sku\": \"GROC-ALMBTR500\",\n      \"quantity\": 1,\n      \"unit_price\": 12.99,\n      \"discount\": 0.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 47.53,\n  \"tax_amount\": 3.62,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 5.99,\n  \"change_given\": 1952.47,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5007\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 2,\n      \"unit_price\": 24.95,\n      \"discount\": 5.99\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_68",
        "instruction": "As a customer named William Zhang, you are looking to buy several products. The items you desire are: 2 parka, 1 spoon set, 1 gaming console, 2 coffee maker, 2 AAA Batteries. If certain items are not available, please go ahead and purchase whatever you can. It may require visiting multiple stores to collect all the items. A credit card will be used for the complete payment.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "William Zhang"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "parka"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "spoon set"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "coffee maker"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AAA Batteries"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-WINJKT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOM-COFMKR12"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5006",
                    "payment_method": "credit_card",
                    "payment_amount": 110.33,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5006",
                    "payment_method": "credit_card",
                    "payment_amount": 410.27,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 110.33,\n  \"tax_amount\": 8.41,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 17.98,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOM-COFMKR12\",\n      \"quantity\": 2,\n      \"unit_price\": 59.95,\n      \"discount\": 17.98\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 410.27,\n  \"tax_amount\": 31.27,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-WINJKT01\",\n      \"quantity\": 2,\n      \"unit_price\": 189.5,\n      \"discount\": 0.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_69",
        "instruction": "As a customer named James O'Connor, you want to purchase a few items. The products you wish to buy are: 2 fry pan, 2 TV, 1 speaker. If any items are unavailable, please proceed to buy whatever is accessible. You may need to visit different stores to get everything. Payment will be made in cash, and you have 2000 available for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "James O'Connor"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "TV"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "speaker"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-BTSPKR02"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-005"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 2000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-005",
                    "employee_id": "EMP-1050",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 2000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 2000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 1363.93,\n  \"tax_amount\": 103.95,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 140.0,\n  \"change_given\": 636.07,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-4KTV55\",\n      \"quantity\": 2,\n      \"unit_price\": 699.99,\n      \"discount\": 140.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-005\",\n  \"employee_id\": \"EMP-1050\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 123.83,\n  \"tax_amount\": 9.44,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 15.6,\n  \"change_given\": 1876.17,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-BTSPKR02\",\n      \"quantity\": 1,\n      \"unit_price\": 129.99,\n      \"discount\": 15.6\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 47.53,\n  \"tax_amount\": 3.62,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 5.99,\n  \"change_given\": 1952.47,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 2,\n      \"unit_price\": 24.95,\n      \"discount\": 5.99\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_70",
        "instruction": "As a customer named William Zhang, you aim to buy a few products. The items you want are: 1 thermostat, 1 helmet, 1 floor light, 2 office chair, 2 knife. If some items are not available, please go ahead and purchase all available items. You may need to visit multiple stores to acquire them all. A credit card will be used for the exact payment.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "William Zhang"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "thermostat"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "helmet"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "floor light"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "office chair"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SMRT-THERM02"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-BIKHLM01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "OFFC-ERGCHR01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-004"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SMRT-THERM02",
                            "quantity": 1
                        },
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5006",
                    "payment_method": "credit_card",
                    "payment_amount": 245.32,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SMRT-THERM02",
                            "quantity": 1
                        },
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5006",
                    "payment_method": "credit_card",
                    "payment_amount": 448.13,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-004",
                    "employee_id": "EMP-1034",
                    "customer_id": "CUST-5006",
                    "payment_method": "credit_card",
                    "payment_amount": 77.07,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 245.32,\n  \"tax_amount\": 18.7,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 32.28,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"SMRT-THERM02\",\n      \"quantity\": 1,\n      \"unit_price\": 179.0,\n      \"discount\": 17.9\n    },\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 2,\n      \"unit_price\": 39.95,\n      \"discount\": 14.38\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 448.13,\n  \"tax_amount\": 34.15,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 46.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"OFFC-ERGCHR01\",\n      \"quantity\": 2,\n      \"unit_price\": 229.99,\n      \"discount\": 46.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-004\",\n  \"employee_id\": \"EMP-1034\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 77.07,\n  \"tax_amount\": 5.87,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 17.8,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-BIKHLM01\",\n      \"quantity\": 1,\n      \"unit_price\": 89.0,\n      \"discount\": 17.8\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_71",
        "instruction": "As a customer named James O'Connor, you are seeking to purchase several products. The requested items include: 2 laptop, 2 TV. In case some items are unavailable, proceed to buy all of the available products. You might need to visit different stores to acquire everything. The payment will be made in cash, with a total of 5000 for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "James O'Connor"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "laptop"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "TV"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-GAMLP15"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-GAMLP15",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 5000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 5000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-GAMLP15",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 1363.93,\n  \"tax_amount\": 103.95,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 140.0,\n  \"change_given\": 3636.07,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-4KTV55\",\n      \"quantity\": 2,\n      \"unit_price\": 699.99,\n      \"discount\": 140.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 3245.34,\n  \"tax_amount\": 247.34,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 1754.66,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-GAMLP15\",\n      \"quantity\": 2,\n      \"unit_price\": 1499.0,\n      \"discount\": 0.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_72",
        "instruction": "As a customer named Logan Smith, you are aiming to buy a few products. The items you desire are: 2 sparkling water, 1 gaming console, 2 floor light, 2 parka. If some items are not available, feel free to buy all of the accessible ones. You might have to visit various stores to gather all the products. The payment will be made using a credit card for the full amount.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Logan Smith"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "floor light"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "parka"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-WINJKT01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5012",
                    "payment_method": "credit_card",
                    "payment_amount": 410.27,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5012",
                    "payment_method": "credit_card",
                    "payment_amount": 15.18,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 410.27,\n  \"tax_amount\": 31.27,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-WINJKT01\",\n      \"quantity\": 2,\n      \"unit_price\": 189.5,\n      \"discount\": 0.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 15.18,\n  \"tax_amount\": 0.0,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0,\n  \"discount_total\": 0.8,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 2,\n      \"unit_price\": 7.99,\n      \"discount\": 0.8\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_73",
        "instruction": "As a customer named William Zhang, you're looking to acquire several products. The items you're interested in are: 2 knife, 2 helmet. If any items are not in stock, continue to purchase everything that is available. You might have to go to multiple stores to collect all of the items. Payment will be made in cash with a budget of 1000.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "William Zhang"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "helmet"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-BIKHLM01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-004"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-004",
                    "employee_id": "EMP-1034",
                    "customer_id": "CUST-5006",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5006",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-004\",\n  \"employee_id\": \"EMP-1034\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 154.15,\n  \"tax_amount\": 11.75,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 35.6,\n  \"change_given\": 845.85,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-BIKHLM01\",\n      \"quantity\": 2,\n      \"unit_price\": 89.0,\n      \"discount\": 35.6\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 70.93,\n  \"tax_amount\": 5.41,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 14.38,\n  \"change_given\": 929.07,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5006\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 2,\n      \"unit_price\": 39.95,\n      \"discount\": 14.38\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_74",
        "instruction": "As a customer named Emma Wilson, you're on the hunt for a few products. The items you wish to purchase are: 1 helmet, 2 gaming console, 2 sparkling water. Should some items be unavailable, feel free to buy all the available products. You may need to visit different stores to obtain everything. The payment will be made in cash, with a limit of 1000.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Emma Wilson"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "helmet"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-BIKHLM01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-004"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5001",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-004",
                    "employee_id": "EMP-1034",
                    "customer_id": "CUST-5001",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 15.18,\n  \"tax_amount\": 0.0,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0,\n  \"discount_total\": 0.8,\n  \"change_given\": 984.82,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5001\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 2,\n      \"unit_price\": 7.99,\n      \"discount\": 0.8\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-004\",\n  \"employee_id\": \"EMP-1034\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 77.07,\n  \"tax_amount\": 5.87,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 17.8,\n  \"change_given\": 922.93,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5001\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-BIKHLM01\",\n      \"quantity\": 1,\n      \"unit_price\": 89.0,\n      \"discount\": 17.8\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_75",
        "instruction": "As a customer named Mia Kim, you're aiming to purchase several products. The items you want include: 2 laptop, 1 speaker, 1 fry pan, 1 knife, 1 gaming console. If certain items are not available, proceed to buy all of the items that are in stock. You may have to check multiple stores to find everything. The payment will be made with a credit card for the exact total.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Mia Kim"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "laptop"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "speaker"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "fry pan"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-GAMLP15"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-BTSPKR02"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-FRYPAN10"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-005"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-GAMLP15",
                            "quantity": 2
                        },
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5011",
                    "payment_method": "credit_card",
                    "payment_amount": 23.77,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-FRYPAN10",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5011",
                    "payment_method": "credit_card",
                    "payment_amount": 3280.8,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-GAMLP15",
                            "quantity": 2
                        },
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-005",
                    "employee_id": "EMP-1050",
                    "customer_id": "CUST-5011",
                    "payment_method": "credit_card",
                    "payment_amount": 123.83,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 23.77,\n  \"tax_amount\": 1.81,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 2.99,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-FRYPAN10\",\n      \"quantity\": 1,\n      \"unit_price\": 24.95,\n      \"discount\": 2.99\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 3280.8,\n  \"tax_amount\": 250.04,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 7.19,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-GAMLP15\",\n      \"quantity\": 2,\n      \"unit_price\": 1499.0,\n      \"discount\": 0.0\n    },\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 1,\n      \"unit_price\": 39.95,\n      \"discount\": 7.19\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-005\",\n  \"employee_id\": \"EMP-1050\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 123.83,\n  \"tax_amount\": 9.44,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 15.6,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5011\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-BTSPKR02\",\n      \"quantity\": 1,\n      \"unit_price\": 129.99,\n      \"discount\": 15.6\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_76",
        "instruction": "As a customer named Sophia Singh, you are looking to buy a few products. The items you require are: 2 spoon set, 2 AA Batteries. If some items aren\u2019t available, go ahead and purchase all of the remaining products. You may need to explore multiple stores to find everything you need. Payment will be made in cash, with a total budget of 1000.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Sophia Singh"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "spoon set"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AA Batteries"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-RCHAA04"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5003",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 38.16,\n  \"tax_amount\": 2.91,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 2.65,\n  \"change_given\": 961.84,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5003\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-RCHAA04\",\n      \"quantity\": 2,\n      \"unit_price\": 18.95,\n      \"discount\": 2.65\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_77",
        "instruction": "As a customer named Noah Tran, you are interested in buying a few items. The products you are looking for are: 2 towel, 1 almond butter, 1 AAA Batteries, 1 earbuds. If any items are not on the shelf, feel free to purchase all of the items that are available. You might need to visit several stores to collect all the necessary items. The payment will be made using a credit card for the exact amount.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Noah Tran"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "towel"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "almond butter"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AAA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "earbuds"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-BTHTWL01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-ALMBTR500"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-NCEBUDS01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5002",
                    "payment_method": "credit_card",
                    "payment_amount": 42.81,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5002",
                    "payment_method": "credit_card",
                    "payment_amount": 142.88,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 42.81,\n  \"tax_amount\": 2.27,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 1.45,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5002\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-BTHTWL01\",\n      \"quantity\": 2,\n      \"unit_price\": 14.5,\n      \"discount\": 1.45\n    },\n    {\n      \"sku\": \"GROC-ALMBTR500\",\n      \"quantity\": 1,\n      \"unit_price\": 12.99,\n      \"discount\": 0.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 142.88,\n  \"tax_amount\": 10.89,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 18.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5002\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-NCEBUDS01\",\n      \"quantity\": 1,\n      \"unit_price\": 149.99,\n      \"discount\": 18.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_78",
        "instruction": "As a customer named Benjamin Cohen, you're searching to acquire a few products. The items you wish to buy consist of: 1 office chair, 1 TV, 2 knife, 1 granola bars, 1 coffee maker. In case some items are out of stock, go ahead and purchase all available ones. You may have to check multiple stores to gather everything. The payment will be made using a credit card for the exact price.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Benjamin Cohen"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "office chair"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "TV"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "granola bars"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "coffee maker"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "OFFC-ERGCHR01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-GRNLBR12"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOM-COFMKR12"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        },
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 1
                        },
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5010",
                    "payment_method": "credit_card",
                    "payment_amount": 238.31,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        },
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5010",
                    "payment_method": "credit_card",
                    "payment_amount": 737.12,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 1
                        },
                        {
                            "sku": "HOM-COFMKR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5010",
                    "payment_method": "credit_card",
                    "payment_amount": 70.93,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 238.31,\n  \"tax_amount\": 17.08,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 23.75,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5010\",\n  \"line_items\": [\n    {\n      \"sku\": \"OFFC-ERGCHR01\",\n      \"quantity\": 1,\n      \"unit_price\": 229.99,\n      \"discount\": 23.0\n    },\n    {\n      \"sku\": \"GROC-GRNLBR12\",\n      \"quantity\": 1,\n      \"unit_price\": 14.99,\n      \"discount\": 0.75\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 737.12,\n  \"tax_amount\": 56.17,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 78.99,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5010\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-4KTV55\",\n      \"quantity\": 1,\n      \"unit_price\": 699.99,\n      \"discount\": 70.0\n    },\n    {\n      \"sku\": \"HOM-COFMKR12\",\n      \"quantity\": 1,\n      \"unit_price\": 59.95,\n      \"discount\": 8.99\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 70.93,\n  \"tax_amount\": 5.41,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 14.38,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5010\",\n  \"line_items\": [\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 2,\n      \"unit_price\": 39.95,\n      \"discount\": 14.38\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_79",
        "instruction": "As a customer named James O'Connor, you\u2019re looking to purchase a few products. The items you want consist of: 2 almond butter, 1 office chair, 2 yoga mat. Should certain items not be available, feel free to buy all available products. You might have to explore multiple stores to gather all the items. The payment will be made in cash, with a total of 1000 for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "James O'Connor"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "almond butter"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "office chair"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "yoga mat"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-ALMBTR500"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "OFFC-ERGCHR01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-YOGMAT01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 2
                        },
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 2
                        },
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 81.17,\n  \"tax_amount\": 4.21,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 9.0,\n  \"change_given\": 918.83,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-ALMBTR500\",\n      \"quantity\": 2,\n      \"unit_price\": 12.99,\n      \"discount\": 0.0\n    },\n    {\n      \"sku\": \"SPORT-YOGMAT01\",\n      \"quantity\": 2,\n      \"unit_price\": 29.99,\n      \"discount\": 9.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 224.07,\n  \"tax_amount\": 17.08,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 23.0,\n  \"change_given\": 775.93,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"OFFC-ERGCHR01\",\n      \"quantity\": 1,\n      \"unit_price\": 229.99,\n      \"discount\": 23.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_80",
        "instruction": "As a customer named Noah Tran, you are aiming to buy a few products. The items on your list are: 2 jeans, 1 office chair. If some items are not available, proceed with the purchase of all accessible products. You may need to visit different stores to acquire everything. The payment will be made using a credit card for the exact amount.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Noah Tran"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "jeans"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "office chair"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "OFFC-ERGCHR01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5002",
                    "payment_method": "credit_card",
                    "payment_amount": 224.07,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5002",
                    "payment_method": "credit_card",
                    "payment_amount": 107.17,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 224.07,\n  \"tax_amount\": 17.08,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 23.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5002\",\n  \"line_items\": [\n    {\n      \"sku\": \"OFFC-ERGCHR01\",\n      \"quantity\": 1,\n      \"unit_price\": 229.99,\n      \"discount\": 23.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 107.17,\n  \"tax_amount\": 8.17,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5002\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-SLFJEAN34\",\n      \"quantity\": 2,\n      \"unit_price\": 49.5,\n      \"discount\": 0.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_81",
        "instruction": "Act as a customer named Liam Anderson who intends to buy several products. The items you wish to acquire are: 1 AA Batteries, 1 yoga mat, 1 granola bars, 2 towel. Some products may not be in stock; if that happens, proceed to purchase all of the items that are available. You might need to visit different stores to collect all the products. You will pay the exact amount using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Liam Anderson"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "yoga mat"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "granola bars"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "towel"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-RCHAA04"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-YOGMAT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-GRNLBR12"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-BTHTWL01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 1
                        },
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 1
                        },
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5004",
                    "payment_method": "credit_card",
                    "payment_amount": 33.31,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-RCHAA04",
                            "quantity": 1
                        },
                        {
                            "sku": "GROC-GRNLBR12",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5004",
                    "payment_method": "credit_card",
                    "payment_amount": 57.41,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-YOGMAT01",
                            "quantity": 1
                        },
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 33.31,\n  \"tax_amount\": 1.45,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 2.08,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-RCHAA04\",\n      \"quantity\": 1,\n      \"unit_price\": 18.95,\n      \"discount\": 1.33\n    },\n    {\n      \"sku\": \"GROC-GRNLBR12\",\n      \"quantity\": 1,\n      \"unit_price\": 14.99,\n      \"discount\": 0.75\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 57.41,\n  \"tax_amount\": 4.37,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 5.95,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5004\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-YOGMAT01\",\n      \"quantity\": 1,\n      \"unit_price\": 29.99,\n      \"discount\": 4.5\n    },\n    {\n      \"sku\": \"HOME-BTHTWL01\",\n      \"quantity\": 2,\n      \"unit_price\": 14.5,\n      \"discount\": 1.45\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_82",
        "instruction": "Imagine you are a customer named James O'Connor who is planning to purchase a few items. The products you are looking for are: 2 desk lamp, 1 sparkling water. Some products may be unavailable; if this occurs, go ahead and buy all of the items that you can find. You may have to go to several stores to acquire all of the desired items. You will be paying the exact amount using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "James O'Connor"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "desk lamp"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "sparkling water"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-DESKLMP01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-SPRWAT6P"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5008",
                    "payment_method": "credit_card",
                    "payment_amount": 77.28,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 2
                        },
                        {
                            "sku": "GROC-SPRWAT6P",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 77.28,\n  \"tax_amount\": 5.31,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 6.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-DESKLMP01\",\n      \"quantity\": 2,\n      \"unit_price\": 34.99,\n      \"discount\": 5.6\n    },\n    {\n      \"sku\": \"GROC-SPRWAT6P\",\n      \"quantity\": 1,\n      \"unit_price\": 7.99,\n      \"discount\": 0.4\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_83",
        "instruction": "Pretend you are a customer named Noah Tran who wants to buy a few products. The items you wish to get are: 2 parka, 1 helmet. If some items are not available, go ahead and purchase everything that is in stock. You may need to visit various stores to obtain all of the products. You will pay in cash, and you have 1000 for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Noah Tran"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "parka"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "helmet"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-WINJKT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "SPORT-BIKHLM01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-004"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-004",
                    "employee_id": "EMP-1034",
                    "customer_id": "CUST-5002",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "SPORT-BIKHLM01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5002",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-004\",\n  \"employee_id\": \"EMP-1034\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 77.07,\n  \"tax_amount\": 5.87,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 17.8,\n  \"change_given\": 922.93,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5002\",\n  \"line_items\": [\n    {\n      \"sku\": \"SPORT-BIKHLM01\",\n      \"quantity\": 1,\n      \"unit_price\": 89.0,\n      \"discount\": 17.8\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 410.27,\n  \"tax_amount\": 31.27,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 589.73,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5002\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-WINJKT01\",\n      \"quantity\": 2,\n      \"unit_price\": 189.5,\n      \"discount\": 0.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_84",
        "instruction": "Envision yourself as a customer named Ava Martinez who seeks to buy a few items. The products you are interested in are: 1 gaming console, 1 TV. If some items are not available, feel free to buy all of the items that are available. You may need to visit multiple stores to gather all the items. You will be paying in cash, with 1000 at your disposal for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Ava Martinez"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "TV"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5005",
                    "payment_method": "cash",
                    "payment_amount": 1000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 681.96,\n  \"tax_amount\": 51.97,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 70.0,\n  \"change_given\": 318.04,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5005\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-4KTV55\",\n      \"quantity\": 1,\n      \"unit_price\": 699.99,\n      \"discount\": 70.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_85",
        "instruction": "Consider yourself as a customer named Sophia Singh who is on the lookout for a few products. The items you wish to acquire are: 2 jeans, 2 parka. If some products are unavailable, please proceed to buy all of the items that are available. You may have to visit different stores to collect everything you want. You will pay in cash, and you have 1000 to complete your purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Sophia Singh"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "jeans"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "parka"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-SLFJEAN34"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-WINJKT01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        },
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5003",
                    "payment_method": "cash",
                    "payment_amount": 1000,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-SLFJEAN34",
                            "quantity": 2
                        },
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 517.44,\n  \"tax_amount\": 39.44,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 482.56,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5003\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-SLFJEAN34\",\n      \"quantity\": 2,\n      \"unit_price\": 49.5,\n      \"discount\": 0.0\n    },\n    {\n      \"sku\": \"CLTH-WINJKT01\",\n      \"quantity\": 2,\n      \"unit_price\": 189.5,\n      \"discount\": 0.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_86",
        "instruction": "Visualize being a customer named James O'Connor who aims to buy a few products. The items you want include: 2 towel, 1 AAA Batteries, 1 gaming console, 2 laptop, 2 parka. Should some items not be available, feel free to go ahead and purchase all of the available items. You might need to visit multiple stores to get everything on your list. You will be paying in cash, having 10000 for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "James O'Connor"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "towel"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "AAA Batteries"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "gaming console"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "laptop"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "parka"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-BTHTWL01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-GAMLP15"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-WINJKT01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-GAMLP15",
                            "quantity": 2
                        },
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 10000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-GAMLP15",
                            "quantity": 2
                        },
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5008",
                    "payment_method": "cash",
                    "payment_amount": 10000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 3655.61,\n  \"tax_amount\": 278.61,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 6344.39,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-GAMLP15\",\n      \"quantity\": 2,\n      \"unit_price\": 1499.0,\n      \"discount\": 0.0\n    }\n, {\n      \"sku\": \"CLTH-WINJKT01\",\n      \"quantity\": 2,\n      \"unit_price\": 189.5,\n      \"discount\": 0.0\n    }  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 29.82,\n  \"tax_amount\": 2.27,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 1.45,\n  \"change_given\": 9970.18,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5008\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-BTHTWL01\",\n      \"quantity\": 2,\n      \"unit_price\": 14.5,\n      \"discount\": 1.45\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_87",
        "instruction": "Assume the role of a customer named Logan Smith who intends to buy several products. The items on your list are: 1 office chair, 1 speaker, 1 almond butter, 2 TV. If some items are unavailable, proceed to buy all of the products that can be found. You may need to go to multiple stores to get everything. You will pay the exact amount using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Logan Smith"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "office chair"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "speaker"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "almond butter"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "TV"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "OFFC-ERGCHR01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-BTSPKR02"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "GROC-ALMBTR500"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-005"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 1
                        },
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-005",
                    "employee_id": "EMP-1050",
                    "customer_id": "CUST-5012",
                    "payment_method": "credit_card",
                    "payment_amount": 123.83,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5012",
                    "payment_method": "credit_card",
                    "payment_amount": 1376.92,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "GROC-ALMBTR500",
                            "quantity": 1
                        },
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5012",
                    "payment_method": "credit_card",
                    "payment_amount": 224.07,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-005\",\n  \"employee_id\": \"EMP-1050\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 123.83,\n  \"tax_amount\": 9.44,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 15.6,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-BTSPKR02\",\n      \"quantity\": 1,\n      \"unit_price\": 129.99,\n      \"discount\": 15.6\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 1376.92,\n  \"tax_amount\": 103.95,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 140.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"GROC-ALMBTR500\",\n      \"quantity\": 1,\n      \"unit_price\": 12.99,\n      \"discount\": 0.0\n    },\n    {\n      \"sku\": \"ELEC-4KTV55\",\n      \"quantity\": 2,\n      \"unit_price\": 699.99,\n      \"discount\": 140.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 224.07,\n  \"tax_amount\": 17.08,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 23.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"OFFC-ERGCHR01\",\n      \"quantity\": 1,\n      \"unit_price\": 229.99,\n      \"discount\": 23.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_88",
        "instruction": "Picture yourself as a customer named Benjamin Cohen looking to acquire a few products. The items on your list include: 2 towel, 1 laptop, 1 TV. If some products happen to be out of stock, please proceed to purchase all of the available items. You might need to visit several stores to complete your shopping. You will be paying in cash, and you have 3000 for the purchase.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Benjamin Cohen"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "towel"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "laptop"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "TV"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-BTHTWL01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-GAMLP15"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-4KTV55"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 2
                        },
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-GAMLP15",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5010",
                    "payment_method": "cash",
                    "payment_amount": 3000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 2
                        },
                        {
                            "sku": "ELEC-4KTV55",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5010",
                    "payment_method": "cash",
                    "payment_amount": 3000.0,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-GAMLP15",
                            "quantity": 1
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 711.78,\n  \"tax_amount\": 54.24,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 71.45,\n  \"change_given\": 2288.22,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5010\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-BTHTWL01\",\n      \"quantity\": 2,\n      \"unit_price\": 14.5,\n      \"discount\": 1.45\n    },\n    {\n      \"sku\": \"ELEC-4KTV55\",\n      \"quantity\": 1,\n      \"unit_price\": 699.99,\n      \"discount\": 70.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 1622.67,\n  \"tax_amount\": 123.67,\n  \"payment_method\": \"cash\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 1377.33,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5010\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-GAMLP15\",\n      \"quantity\": 1,\n      \"unit_price\": 1499.0,\n      \"discount\": 0.0\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_89",
        "instruction": "Take on the identity of a customer named Logan Smith who wishes to purchase a few items. The products you are looking for are: 2 office chair, 1 laptop, 1 towel, 1 earbuds, 2 knife. If some items are unavailable, please go ahead and buy all of the items that are available. You may need to visit different stores to gather everything you want. You will pay the exact amount using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Logan Smith"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "office chair"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "laptop"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "towel"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "earbuds"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "knife"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "OFFC-ERGCHR01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "ELEC-GAMLP15"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-BTHTWL01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-NCEBUDS01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "KITCH-CHEFKNF8"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-003"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "ELEC-GAMLP15",
                            "quantity": 1
                        },
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 1
                        },
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5012",
                    "payment_method": "credit_card",
                    "payment_amount": 14.92,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-BTHTWL01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-003",
                    "employee_id": "EMP-1020",
                    "customer_id": "CUST-5012",
                    "payment_method": "credit_card",
                    "payment_amount": 448.13,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "OFFC-ERGCHR01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5012",
                    "payment_method": "credit_card",
                    "payment_amount": 1836.48,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "ELEC-GAMLP15",
                            "quantity": 1
                        },
                        {
                            "sku": "AUDIO-NCEBUDS01",
                            "quantity": 1
                        },
                        {
                            "sku": "KITCH-CHEFKNF8",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 14.92,\n  \"tax_amount\": 1.14,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.73,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-BTHTWL01\",\n      \"quantity\": 1,\n      \"unit_price\": 14.5,\n      \"discount\": 0.73\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-003\",\n  \"employee_id\": \"EMP-1020\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 448.13,\n  \"tax_amount\": 34.15,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 46.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"OFFC-ERGCHR01\",\n      \"quantity\": 2,\n      \"unit_price\": 229.99,\n      \"discount\": 46.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 1836.48,\n  \"tax_amount\": 139.97,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 32.38,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5012\",\n  \"line_items\": [\n    {\n      \"sku\": \"ELEC-GAMLP15\",\n      \"quantity\": 1,\n      \"unit_price\": 1499.0,\n      \"discount\": 0.0\n    },\n    {\n      \"sku\": \"AUDIO-NCEBUDS01\",\n      \"quantity\": 1,\n      \"unit_price\": 149.99,\n      \"discount\": 18.0\n    },\n    {\n      \"sku\": \"KITCH-CHEFKNF8\",\n      \"quantity\": 2,\n      \"unit_price\": 39.95,\n      \"discount\": 14.38\n    }\n  ]\n}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "customer_90",
        "instruction": "Imagine being a customer named Olivia Romano who seeks to acquire a few products. The items you want are: 1 parka, 2 speaker, 1 floor light, 2 spoon set, 2 desk lamp. If certain items are not available, feel free to proceed with purchasing all of the available products. You may have to visit multiple stores to gather all of the items. You will pay the exact amount using a credit card.",
        "actions": [
            {
                "name": "FindCustomers",
                "arguments": {
                    "name": "Olivia Romano"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "parka"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "speaker"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "floor light"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "spoon set"
                },
            },
            {
                "name": "FindProducts",
                "arguments": {
                    "name": "desk lamp"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "CLTH-WINJKT01"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "AUDIO-BTSPKR02"
                },
            },
            {
                "name": "FindItems",
                "arguments": {
                    "sku": "HOME-DESKLMP01"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-001"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-002"
                },
            },
            {
                "name": "FindCheckOutEmployee",
                "arguments": {
                    "store_id": "STORE-005"
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "TransactionPriceInfo",
                "arguments": {
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "customer_id": "CUST-5007",
                    "payment_method": "credit_card",
                    "payment_amount": 69.69,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "HOME-DESKLMP01",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-002",
                    "employee_id": "EMP-1011",
                    "customer_id": "CUST-5007",
                    "payment_method": "credit_card",
                    "payment_amount": 205.13,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "CLTH-WINJKT01",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "MakeTransaction",
                "arguments": {
                    "timestamp": "2025-01-01T09:10:00Z",
                    "store_id": "STORE-005",
                    "employee_id": "EMP-1050",
                    "customer_id": "CUST-5007",
                    "payment_method": "credit_card",
                    "payment_amount": 247.65,
                    "status": "completed",
                    "line_items": [
                        {
                            "sku": "AUDIO-BTSPKR02",
                            "quantity": 2
                        }
                    ]
                }
            }
        ],
        "outputs": [
                "{\n  \"transaction_id\": \"TNX-0013\",\n  \"store_id\": \"STORE-001\",\n  \"employee_id\": \"EMP-1002\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 69.69,\n  \"tax_amount\": 5.31,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 5.6,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5007\",\n  \"line_items\": [\n    {\n      \"sku\": \"HOME-DESKLMP01\",\n      \"quantity\": 2,\n      \"unit_price\": 34.99,\n      \"discount\": 5.6\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0014\",\n  \"store_id\": \"STORE-002\",\n  \"employee_id\": \"EMP-1011\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 205.13,\n  \"tax_amount\": 15.63,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 0.0,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5007\",\n  \"line_items\": [\n    {\n      \"sku\": \"CLTH-WINJKT01\",\n      \"quantity\": 1,\n      \"unit_price\": 189.5,\n      \"discount\": 0.0\n    }\n  ]\n}",
                "{\n  \"transaction_id\": \"TNX-0015\",\n  \"store_id\": \"STORE-005\",\n  \"employee_id\": \"EMP-1050\",\n  \"timestamp\": \"2025-01-01T09:10:00Z\",\n  \"total_amount\": 247.65,\n  \"tax_amount\": 18.87,\n  \"payment_method\": \"credit_card\",\n  \"tax_rate\": 0.0825,\n  \"discount_total\": 31.2,\n  \"change_given\": 0.0,\n  \"status\": \"completed\",\n  \"customer_id\": \"CUST-5007\",\n  \"line_items\": [\n    {\n      \"sku\": \"AUDIO-BTSPKR02\",\n      \"quantity\": 2,\n      \"unit_price\": 129.99,\n      \"discount\": 31.2\n    }\n  ]\n}"
        ]
    }
]
